"""Set of metaclasses used throughout the library."""
from abc import ABC, abstractmethod
from collections import UserDict
from typing import Optional
try:
    import orjson as json
except ImportError:
    try:
        import rapidjson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            import json

import esprima
from esprima.error_handler import Error as ParseError
from validator_collection import validators, checkers, errors as validator_errors

from highcharts import constants, errors, utility_functions
from highcharts.decorators import validate_types
from highcharts.js_literal_functions import serialize_to_js_literal, assemble_js_literal,\
    get_key_value_pairs


class HighchartsMeta(ABC):
    """Metaclass that is used to define the standard interface exposed for serializable
    objects."""

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs.get(key, None))

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False

        self_js_literal = self.to_js_literal()
        other_js_literal = other.to_js_literal()

        return self_js_literal == other_js_literal

    def _untrimmed_mro_ancestors(self, in_cls = None) -> dict:
        """Walk through the parent classes and consolidate the results of their
        :meth:`_to_untrimmed_dict() <HighchartsMeta._to_untrimmed_dict__>` methods into
        a single :class:`dict <python:dict>`.

        :rtype: :class:`dict <python:dict>`
        """
        return utility_functions.mro__to_untrimmed_dict(self, in_cls = in_cls)

    @abstractmethod
    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        """Generate the first-level of the :class:`dict <python:dict>` representation of
        the object.

        .. note::

          This method does *not* traverse the object structure to convert the object into
          a full :class:`dict <python:dict>` representation - it merely goes "part" of the
          way there to replace the Highcharts for Python keys with their correpsond
          Highcharts JS keys.

        :rtype: :class:`dict <python:dict>`
        """
        raise NotImplementedError()

    @staticmethod
    def trim_iterable(untrimmed):
        """Convert any :class:`EnforcedNullType` values in ``untrimmed`` to ``'null'``.

        :rtype: iterable
        """
        if not checkers.is_iterable(untrimmed, forbid_literals = (str, bytes, dict)):
            return untrimmed

        trimmed = []
        for item in untrimmed:
            if item is None or item == constants.EnforcedNull:
                trimmed.append('null')
            elif hasattr(item, 'to_dict'):
                item_as_dict = item.to_dict()
                if item_as_dict:
                    trimmed.append(item_as_dict)
            elif isinstance(item, dict):
                if item:
                    trimmed.append(item)
            elif checkers.is_iterable(item):
                if item:
                    trimmed.append(HighchartsMeta.trim_iterable(item))
            else:
                trimmed.append(item)

        return trimmed

    @staticmethod
    def trim_dict(untrimmed: Optional[dict]) -> dict:
        """Remove keys from ``untrimmed`` whose values are :obj:`None <python:None>` and
        convert values that have ``.to_dict()`` methods.

        :returns: Trimmed :class:`dict <python:dict>`
        :rtype: :class:`dict <python:dict>`
        """
        as_dict = {}
        for key in untrimmed:
            value = untrimmed.get(key, None)
            if isinstance(value, bool):
                as_dict[key] = value
            elif value and hasattr(value, 'to_dict'):
                trimmed_value = value.to_dict()
                if trimmed_value:
                    as_dict[key] = trimmed_value
            elif value == constants.EnforcedNull:
                as_dict[key] = 'null'
            elif isinstance(value, dict):
                trimmed_value = HighchartsMeta.trim_dict(value)
                if trimmed_value:
                    as_dict[key] = trimmed_value
            elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
                trimmed_value = HighchartsMeta.trim_iterable(value)
                if trimmed_value:
                    as_dict[key] = trimmed_value
            elif value:
                trimmed_value = HighchartsMeta.trim_iterable(value)
                if trimmed_value:
                    as_dict[key] = trimmed_value
            elif value in [0, 0., False]:
                as_dict[key] = value

        return as_dict

    @classmethod
    @abstractmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        raise NotImplementedError()

    @classmethod
    def from_dict(cls,
                  as_dict: dict,
                  allow_snake_case: bool = True):
        """Construct an instance of the class from a :class:`dict <python:dict>` object.

        :param as_dict: A :class:`dict <python:dict>` representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python object representation of ``as_dict``.
        :rtype: :class:`HighchartsMeta`
        """
        as_dict = validators.dict(as_dict, allow_empty = True) or {}
        clean_as_dict = {}
        for key in as_dict:
            if allow_snake_case:
                clean_key = utility_functions.to_camelCase(key)
            else:
                clean_key = key

            clean_as_dict[clean_key] = as_dict[key]

        kwargs = cls._get_kwargs_from_dict(as_dict)

        return cls(**kwargs)

    @classmethod
    def from_json(cls, as_json: str | bytes):
        """Construct an instance of the class from a JSON string.

        :param as_json: The JSON string for the object.
        :type as_json: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`HighchartsMeta`
        """
        as_dict = json.loads(as_json)

        return cls.from_dict(as_dict)

    def to_dict(self) -> dict:
        """Generate a :class:`dict <python:dict>` representation of the object compatible
        with the Highcharts JavaScript library.

        .. note::

          The :class:`dict <python:dict>` representation has a property structure and
          naming convention that is *intentionally* consistent with the Highcharts
          JavaScript library. This is not Pythonic, but it makes managing the interplay
          between the two languages much, much simpler.

        :returns: A :class:`dict <python:dict>` representation of the object.
        :rtype: :class:`dict <python:dict>`
        """
        untrimmed = self._to_untrimmed_dict()

        return self.trim_dict(untrimmed)

    def to_json(self, encoding = 'utf-8'):
        """Generate a JSON string/byte string representation of the object compatible with
        the Highcharts JavaScript library.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string. For more
          information, please see :doc:`JSON Serialization and Deserialization`.

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A JSON representation of the object compatible with the Highcharts
          library.
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        as_dict = self.to_dict()
        for key in as_dict:
            if as_dict[key] == constants.EnforcedNull:
                as_dict[key] = None
        try:
            as_json = json.dumps(as_dict, encoding = encoding)
        except TypeError:
            as_json = json.dumps(as_dict)

        return as_json

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            serialized = serialize_to_js_literal(item, encoding = encoding)
            if serialized is not None:
                as_dict[key] = serialized

        as_str = assemble_js_literal(as_dict)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    @classmethod
    def _validate_js_literal(cls,
                             as_str,
                             range = True,
                             _break_loop_on_failure = False):
        """Parse ``as_str`` as a valid JavaScript literal object.

        :param as_str: The string to parse as a JavaScript literal object.
        :type as_str: :class:`str <python:str>`

        :param range: If ``True``, includes location and range data for each node in the
          AST returned. Defaults to ``False``.
        :type range: :class:`bool <python:bool>`

        :param _break_loop_on_failure: If ``True``, will not loop if the method fails to
          parse/validate ``as_str``. Defaults to ``False``.
        :type _break_loop_on_failure: :class:`bool <python:bool>`

        :returns: The parsed AST representation of ``as_str`` and the updated string.
        :rtype: 2-member :class:`tuple <python:tuple>` of :class:`esprima.nodes.Script`
          and :class:`str <python:str>`
        """
        try:
            parsed = esprima.parseScript(as_str, loc = range, range = range)
        except ParseError:
            try:
                parsed = esprima.parseModule(as_str, loc = range, range = range)
            except ParseError:
                if not _break_loop_on_failure:
                    as_str = f"""var randomVariable = {as_str}"""
                    return cls._validate_js_literal(as_str,
                                                    range = range,
                                                    _break_loop_on_failure = True)
                else:
                    raise errors.HighchartsParseError('._validate_js_literal() expects '
                                                      'a str containing a valid '
                                                      'JavaScript literal object. Could '
                                                      'not find a valid literal.')

        return parsed, as_str

    @classmethod
    def from_js_literal(cls,
                        as_str_or_file,
                        _break_loop_on_failure = False):
        """Return a Python object representation of a Highcharts JavaScript object
        literal.

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

        parsed, updated_str = cls._validate_js_literal(as_str)

        as_dict = {}
        if not parsed.body:
            return cls()

        if len(parsed.body) > 1:
            raise errors.HighchartsCollectionError(f'each JavaScript object literal is '
                                                   f'expected to contain one object. '
                                                   f'However, you attempted to parse '
                                                   f'{len(parsed.body)} objects.')

        body = parsed.body[0]
        if not checkers.is_type(body, 'VariableDeclaration') and \
           _break_loop_on_failure is False:
            prefixed_str = f'var randomVariable = {as_str}'
            return cls.from_js_literal(prefixed_str,
                                       _break_loop_on_failure = True)
        elif not checkers.is_type(body, 'VariableDeclaration'):
            raise errors.HighchartsVariableDeclarationError('To parse a JavaScriot '
                                                            'object literal, it is '
                                                            'expected to be either a '
                                                            'variable declaration or a'
                                                            'standalone block statement.'
                                                            'Input received did not '
                                                            'conform.')
        declarations = body.declarations
        if not declarations:
            return cls()

        if len(declarations) > 1:
            raise errors.HighchartsCollectionError(f'each JavaScript object literal is '
                                                   f'expected to contain one object. '
                                                   f'However, you attempted to parse '
                                                   f'{len(parsed.body)} objects.')
        object_expression = declarations[0].init
        if not checkers.is_type(object_expression, 'ObjectExpression'):
            raise errors.HighchartsParseError(f'Highcharts expects an object literal to '
                                              f'to be defined as a standard '
                                              f'ObjectExpression. Received: '
                                              f'{type(object_expression)}')

        properties = object_expression.properties
        if not properties:
            return cls()

        key_value_pairs = [(x[0], x[1]) for x in get_key_value_pairs(properties,
                                                                     updated_str)]

        for pair in key_value_pairs:
            as_dict[pair[0]] = pair[1]

        return cls.from_dict(as_dict)


class JavaScriptDict(UserDict):
    """Special :class:`dict <python:dict>` class which constructs a JavaScript
    object that can be represented as a string.

    Keys are validated to be valid variable names, while values are validated to be
    strings.

    When serialized to :class:`str <python:str>`, keys are **not** wrapped in double
    quotes (as they would be in JSON) to ensure that the resulting string can be evaluated
    as JavaScript code.

    """
    _valid_value_types = None
    _allow_empty_value = True

    def __setitem__(self, key, item):
        validate_key = False
        try:
            validate_key = key not in self
        except AttributeError:
            validate_key = True

        if validate_key:
            try:
                key = validators.variable_name(key, allow_empty = False)
            except validator_errors.InvalidVariableNameError as error:
                if '-' in key:
                    try:
                        test_key = key.replace('-', '_')
                        validators.variable_name(test_key, allow_empty = False)
                    except validator_errors.InvalidVariableNameError:
                        raise error
                else:
                    raise error

        if self._valid_value_types:
            try:
                item = validate_types(item,
                                      types = self._valid_value_types,
                                      allow_none = self._allow_empty_value)
            except errors.HighchartsValueError as error:
                if self._allow_empty_value and not item:
                    item = None
                else:
                    try:
                        item = self._valid_value_types(item)
                    except (TypeError, ValueError, AttributeError):
                        raise error

        super().__setitem__(key, item)

    @classmethod
    def from_dict(cls, as_dict):
        """Construct an instance of the class from a :class:`dict <python:dict>` object.

        :param as_dict: A :class:`dict <python:dict>` representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: A Python object representation of ``as_dict``.
        :rtype: :class:`JavaScriptDict`
        """
        as_dict = validators.dict(as_dict, allow_empty = True)
        if not as_dict:
            return cls()

        as_obj = cls()
        for key in as_dict:
            as_obj[key] = as_dict.get(key, None)

        return as_obj

    @classmethod
    def from_json(cls, as_json):
        """Construct an instance of the class from a JSON string.

        :param as_json: The JSON string for the object.
        :type as_json: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`HighchartsMeta`
        """
        as_dict = json.loads(as_json)

        return cls.from_dict(as_dict)

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return self.data

    def to_dict(self):
        """Generate a :class:`dict <python:dict>` representation of the object compatible
        with the Highcharts JavaScript library.

        .. note::

          The :class:`dict <python:dict>` representation has a property structure and
          naming convention that is *intentionally* consistent with the Highcharts
          JavaScript library. This is not Pythonic, but it makes managing the interplay
          between the two languages much, much simpler.

        :returns: A :class:`dict <python:dict>` representation of the object.
        :rtype: :class:`dict <python:dict>`
        """
        return self.data

    def to_json(self, encoding = 'utf-8'):
        """Generate a JSON string/byte string representation of the object compatible with
        the Highcharts JavaScript library.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string. For more
          information, please see :doc:`JSON Serialization and Deserialization`.

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A JSON representation of the object compatible with the Highcharts
          library.
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        as_dict = self.to_dict()
        try:
            as_json = json.dumps(as_dict, encoding = encoding)
        except TypeError:
            as_json = json.dumps(as_dict)

        return as_json

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            serialized = serialize_to_js_literal(item, encoding = encoding)
            if serialized is not None:
                as_dict[key] = serialized

        as_str = assemble_js_literal(as_dict, keys_as_strings = True)

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    @classmethod
    def _validate_js_literal(cls,
                             as_str,
                             range = True,
                             _break_loop_on_failure = False):
        """Parse ``as_str`` as a valid JavaScript literal object.

        :param as_str: The string to parse as a JavaScript literal object.
        :type as_str: :class:`str <python:str>`

        :param range: If ``True``, includes location and range data for each node in the
          AST returned. Defaults to ``False``.
        :type range: :class:`bool <python:bool>`

        :param _break_loop_on_failure: If ``True``, will not loop if the method fails to
          parse/validate ``as_str``. Defaults to ``False``.
        :type _break_loop_on_failure: :class:`bool <python:bool>`

        :returns: The parsed AST representation of ``as_str`` and the updated string.
        :rtype: 2-member :class:`tuple <python:tuple>` of :class:`esprima.nodes.Script`
          and :class:`str <python:str>`
        """
        try:
            parsed = esprima.parseScript(as_str, loc = range, range = range)
        except ParseError:
            try:
                parsed = esprima.parseModule(as_str, loc = range, range = range)
            except ParseError:
                if not _break_loop_on_failure:
                    as_str = f"""var randomVariable = {as_str}"""
                    return cls._validate_js_literal(as_str,
                                                    range = range,
                                                    _break_loop_on_failure = True)
                else:
                    raise errors.HighchartsParseError('._validate_js_function() expects '
                                                      'a str containing a valid '
                                                      'JavaScript function. Could not '
                                                      'find a valid function.')

        return parsed, as_str
