from typing import Optional, List

from validator_collection import validators, checkers
import esprima
from esprima.error_handler import Error as ParseError

from highcharts_core import errors
from highcharts_core.decorators import validate_types
from highcharts_core.metaclasses import HighchartsMeta


class CallbackFunction(HighchartsMeta):
    """Representation of a JavaScript callback function's source code."""

    def __init__(self, **kwargs):
        self._function_name = None
        self._arguments = None
        self._body = None

        self.function_name = kwargs.get('function_name', None)
        self.arguments = kwargs.get('arguments', None)
        self.body = kwargs.get('body', None)

    def __str__(self) -> str:
        if self.function_name:
            prefix = f'function {self.function_name}'
        else:
            prefix = 'function'

        arguments = '('
        if self.arguments:
            for argument in self.arguments:
                arguments += f'{argument},'
            arguments = arguments[:-1]

        arguments += ')'

        as_str = f'{prefix}{arguments}'
        as_str += ' {'
        if self.body:
            as_str += '\n'
            as_str += self.body

        as_str += '}'

        return as_str

    @property
    def function_name(self) -> Optional[str]:
        """An optional name to be given to the function.

        .. warning::

          Most Highcharts Callback function definitions are anonymous, meaning that they
          are named within the object into which they are embedded. As a result,
          this setting should be used sparingly.

        :rtype: :class:`str <python:str>`
        """
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = validators.variable_name(value, allow_empty = True)

    @property
    def arguments(self) -> Optional[List[str]]:
        """Collection of named arguments (parameters) that will be passed to the function.

        :rtype: :class:`list <python:list>` of :obj:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._arguments

    @arguments.setter
    def arguments(self, value):
        if not value:
            self._arguments = None
        else:
            self._arguments = [validators.variable_name(x)
                               for x in validators.iterable(value)]

    @property
    def body(self) -> Optional[str]:
        """The source code of the function itself.

        .. note::

          Should *not* be wrapped in ``{ ... }``. It should just be the source code of the
          the function itself.

        .. hint::

          When writing this code in Python, it is best to use the three-quotation-mark
          string pattern, like so:

          .. code-block:: python

            callback = CallbackFunction()
            callback.body = \"\"\"
            ... some JavaScript logic goes here
            \"\"\"

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._body

    @body.setter
    def body(self, value):
        self._body = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'function_name': as_dict.get('function_name',
                                         as_dict.get('functionName', None)),
            'arguments': as_dict.get('arguments', None),
            'body': as_dict.get('body', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'function_name': self.function_name,
            'arguments': self.arguments,
            'body': self.body
        }

    def to_json(self, encoding = 'utf-8'):
        return None

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> str:
        if filename:
            filename = validators.path(filename)

        as_str = str(self)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    @classmethod
    def _convert_from_js_ast(cls, property_definition, original_str):
        """Create a :class:`CallbackFunction` instance from a
        :class:`esprima.nodes.FunctionExpression` instance.

        :param property_definition: The :class:`esprima.nodes.FunctionExpression`
          instance, including ``loc`` (indicating the line and column in the original
          string) and ``range`` (indicating the character range for the property
          definition in the original string).
        :type property_definition: :class:`esprima.nodes.FunctionExpression`

        :param original_str: The original :class:`str <python:str>` of the JavaScript from
          which ``property_definition`` was parsed.
        :type original_str: :class:`str <python:str>`

        :returns: :class:`CallbackFunction`
        """
        if not checkers.is_type(property_definition, ('FunctionDeclaration',
                                                      'FunctionExpression',
                                                      'MethodDefinition',
                                                      'Property')):
            raise errors.HighchartsParseError(f'property_definition should contain a '
                                              f'FunctionExpression, FunctionDeclaration, '
                                              'MethodDefinition, or Property instance. '
                                              f'Received: '
                                              f'{property_definition.__class__.__name__}')

        if property_definition.type not in ['MethodDefinition', 'Property']:
            body = property_definition.body
        else:
            body = property_definition.value.body

        body_range = body.range
        body_start = body_range[0] + 1
        body_end = body_range[1] - 1

        if property_definition.type == 'FunctionDeclaration':
            function_name = property_definition.id.name
        elif property_definition.type == 'MethodDefinition':
            function_name = property_definition.key.name
        elif property_definition.type == 'FunctionExpression' and \
             property_definition.id is not None:
            function_name = property_definition.id.name
        else:
            function_name = None

        function_body = original_str[body_start:body_end]

        if property_definition.type in ['MethodDefinition', 'Property']:
            arguments = [x.name for x in property_definition.value.params]
        else:
            arguments = [x.name for x in property_definition.params]

        return cls(function_name = function_name,
                   arguments = arguments,
                   body = function_body)

    @classmethod
    def from_js_literal(cls,
                        as_str_or_file,
                        allow_snake_case: bool = True,
                        _break_loop_on_failure: bool = False):
        """Return a Python object representation of a Highcharts JavaScript object
        literal.

        :param as_str_or_file: The JavaScript object literal, represented either as a
          :class:`str <python:str>` or as a filename which contains the JS object literal.
        :type as_str_or_file: :class:`str <python:str>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :param _break_loop_on_failure: If ``True``, will break any looping operations in
          the event of a failure. Otherwise, will attempt to repair the failure. Defaults
          to ``False``.
        :type _break_loop_on_failure: :class:`bool <python:bool>`

        :returns: A Python object representation of the Highcharts JavaScript object
          literal.
        :rtype: :class:`HighchartsMeta`
        """
        is_file = checkers.is_file(as_str_or_file)
        if is_file:
            with open(as_str_or_file, 'r') as file_:
                as_str = file_.read()
        else:
            as_str = as_str_or_file

        parsed, updated_str = cls._validate_js_function(as_str)
        if parsed.body[0].type == 'FunctionDeclaration':
            property_definition = parsed.body[0]
        elif parsed.body[0].type == 'MethodDefinition':
            property_definition = parsed.body[0].body[0]
        elif parsed.body[0].type != 'FunctionDeclaration':
            property_definition = parsed.body[0].declarations[0].init

        return cls._convert_from_js_ast(property_definition, updated_str)

    @classmethod
    def _validate_js_function(cls,
                              as_str,
                              range = True,
                              _break_loop_on_failure = False):
        """Parse a JavaScript function from within ``as_str``.

        :param as_str: A string that potentially contains a JavaScript function.
        :rtype: :class:`str <python:str>`

        :param range: If ``True``, include each node's ``loc`` and ``range`` in the AST
          produced. Defaults to ``True``.
        :type range: :class:`bool <python:bool>`

        :param _break_loop_on_failure: If ``True``, prevents

        :returns: 2-member tuple, with the first being a parsed AST of the function and
          the second being the string that ultimatley produced that parsed AST.
        :rtype: :class:`tuple <python:tuple>` of :class:`esprima.nodes.Script`,
          :class:`str <python:str>`
        """
        try:
            parsed = esprima.parseScript(as_str, loc = range, range = range)
        except ParseError:
            try:
                parsed = esprima.parseModule(as_str, loc = range, range = range)
            except ParseError:
                if not _break_loop_on_failure and as_str.startswith('function'):
                    as_str = f"""const testFunction = {as_str}"""
                    return cls._validate_js_function(as_str,
                                                     range = range,
                                                     _break_loop_on_failure = True)
                elif not _break_loop_on_failure:
                    as_str = f"""const testFunction = function {as_str}"""
                    return cls._validate_js_function(as_str,
                                                     range = range,
                                                     _break_loop_on_failure = True)
                else:
                    raise errors.HighchartsParseError('._validate_js_function() expects '
                                                      'a str containing a valid '
                                                      'JavaScript function. Could not '
                                                      'find a valid function.')

        return parsed, as_str


class JavaScriptClass(HighchartsMeta):
    """Representation of a JavaScript class."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._methods = None

        self.class_name = kwargs.get('class_name', None)
        self.methods = kwargs.get('methods', None)

    def __str__(self) -> str:
        if not self.class_name:
            raise errors.HighchartsMissingClassNameError('Unable to serialize. The '
                                                         'JavaScriptClass instance has '
                                                         'no class_name provided.')
        as_str = f'class {self.class_name} '
        as_str += '{\n'
        for method in self.methods or []:
            method_str = f'{method.function_name}'
            argument_str = '('
            for argument in method.arguments or []:
                argument_str += f'{argument},'
            if method.arguments:
                argument_str = argument_str[:-1]
            argument_str += ') {\n'

            method_str += argument_str

            method_str += method.body + '\n}\n'

            as_str += method_str

        as_str += '}'

        return as_str

    @property
    def class_name(self) -> Optional[str]:
        """The name of the JavaScript class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.variable_name(value, allow_empty = True)

    @property
    def methods(self) -> Optional[List[CallbackFunction]]:
        """Collection of methods that are to be defined within the class. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          All methods *must* have a :meth:`function_name <CallbackFunction.function_name>`
          set.

        .. warning::

          One of the methods *must* have a
          :meth:`function_name <CallbackFunction.function_name>` of ``'constructor'`` and
          be used as a constructor for the class.

        .. note::

          For the sake of simplicity, the :class:`JavaScriptClass` does not support
          ECMAScript's more robust public/private field declaration syntax, nor does it
          support the definition of getters or generators.

        :rtype: :class:`list <python:list>` of :class:`CallbackFunction`, or
          :obj:`None <python:None>`

        :raises HighchartsJavaScriptError: if one or more methods lacks a function name OR
          if there is no ``constructor`` method included in
          :meth:`.methods <JavaScriptClass.methods>`.
        """
        return self._methods

    @methods.setter
    def methods(self, value):
        if not value:
            self._methods = None
        else:
            value = validate_types(value,
                                   types = CallbackFunction,
                                   force_iterable = True)
            has_constructor = False
            for method in value:
                if not method.function_name:
                    raise errors.HighchartsJavaScriptError('All JavaScriptClass methods '
                                                           'require a function name.')
                if method.function_name == 'constructor':
                    has_constructor = True

            if not has_constructor:
                raise errors.HighchartsJavaScriptError('A JavaScriptClass requires at '
                                                       'least one "constructor" method. '
                                                       'Yours had none.')

            self._methods = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'methods': as_dict.get('methods', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'className': self.class_name,
            'methods': self.methods
        }

    @classmethod
    def _convert_from_js_ast(cls, definition, original_str):
        """Create a :class:`JavaScriptClass` instance from a
        :class:`esprima.nodes.ClassDeclaration` instance.

        :param property_definition: The :class:`esprima.nodes.ClassDeclaration` instance,
          including ``loc`` (indicating the line and column in the original string) and
          ``range`` (indicating the character range for the property definition in the
          original string).
        :type property_definition: :class:`esprima.nodes.ClassDeclaration`

        :param original_str: The original :class:`str <python:str>` of the JavaScript from
          which ``definition`` was parsed.
        :type original_str: :class:`str <python:str>`

        :returns: :class:`JavaScriptClass`
        """
        if not checkers.is_type(definition, ('ClassDeclaration', 'ClassExpression')):
            raise errors.HighchartsParseError(f'definition should contain a '
                                              f'ClassDeclaration or ClassExpression'
                                              ' instance. Received: '
                                              f'{definition.__class__.__name__}')

        class_name = definition.id.name

        method_definitions = [x for x in definition.body.body]
        method_strings = []
        for method in method_definitions:
            method_start = method.range[0]
            method_end = method.range[1]
            method_string = original_str[method_start:method_end]
            method_strings.append(method_string)

        methods = [CallbackFunction.from_js_literal(x) for x in method_strings]

        return cls(class_name = class_name,
                   methods = methods)

    @classmethod
    def from_js_literal(cls,
                        as_str_or_file):
        """Return a Python object representation of a JavaScript class.

        :param as_str_or_file: The JavaScript object literal, represented either as a
          :class:`str <python:str>` or as a filename which contains the JS object literal.
        :type as_str_or_file: :class:`str <python:str>`

        :param _break_loop_on_failure: If ``True``, will break any looping operations in
          the event of a failure. Otherwise, will attempt to repair the failure. Defaults
          to ``False``.
        :type _break_loop_on_failure: :class:`bool <python:bool>`

        :returns: A Python object representation of the Highcharts JavaScript object
          literal.
        :rtype: :class:`HighchartsMeta`
        """
        is_file = checkers.is_file(as_str_or_file)
        if is_file:
            with open(as_str_or_file, 'r') as file_:
                as_str = file_.read()
        else:
            as_str = as_str_or_file

        try:
            parsed = esprima.parseScript(as_str, range = True)
        except ParseError:
            try:
                parsed = esprima.parseModule(as_str, range = True)
            except ParseError:
                raise errors.HighchartsParseError('unable to find a JavaScript class '
                                                  'declaration in ``as_str``.')

        definition = parsed.body[0]

        return cls._convert_from_js_ast(definition, as_str)

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> str:
        if filename:
            filename = validators.path(filename)

        as_str = str(self)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str


class VariableName(HighchartsMeta):
    """Object that represents a (JavaScript) variable name that may be referenced in
    **Highcharts for Python** items."""

    def __init__(self, **kwargs):
        self._variable_name = None

        self.variable_name = kwargs.get('variable_name', None)

    @property
    def variable_name(self) -> Optional[str]:
        """The name of the (JavaScript) variable which will be incorporated into
        serializations of **Highcharts for Python** objects as needed.

        :rtype: :class:`str <python:str>`
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, value):
        self._variable_name = validators.variable_name(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'variable_name': as_dict.get('variable_name', as_dict.get('variableName',
                                                                      None)),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'variableName': self.variable_name,
        }

        return untrimmed
