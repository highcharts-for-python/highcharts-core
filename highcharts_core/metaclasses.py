"""Set of metaclasses used throughout the library."""
import datetime
from abc import ABC, abstractmethod
from collections import UserDict
from typing import Optional, List
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

from highcharts_core import constants, errors, utility_functions
from highcharts_core.decorators import validate_types
from highcharts_core.js_literal_functions import serialize_to_js_literal, assemble_js_literal,\
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

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return None

    def _process_required_modules(self, scripts = None, include_extension = False) -> List[str]:
        """Return the list of URLs from which the Highcharts JavaScript modules
        needed to render the chart can be retrieved.
        
        :param scripts: Initial set of scripts that are context-dependent.
        :type scripts: :class:`list <python:list>` of :class:`str <python:str>`
        
        :param include_extension: if ``True``, will return script names with the 
          ``'.js'`` extension included. Defaults to ``False``.
        :type include_extension: :class:`bool <python:bool>`

        :rtype: :class:`list <python:list>`
        """
        if not scripts:
            scripts = []
            
        properties = [x[1:] for x in self.__dict__
                      if x.startswith('_') and hasattr(self, x[1:])]

        for property_name in properties:
            property_value = getattr(self, property_name, None)
            if property_value is None:
                continue
            if checkers.is_iterable(property_value, forbid_literals = (str, bytes, dict)):
                additional_scripts = []
                for item in property_value:
                    if hasattr(item, 'get_required_modules'):
                        item_scripts = [x for x in item.get_required_modules()
                                        if x not in scripts]
                        additional_scripts.extend(item_scripts)
                if additional_scripts:
                    scripts.extend(additional_scripts)
                    continue
            if isinstance(property_value, HighchartsMeta):
                additional_scripts = [x for x in property_value.get_required_modules()
                                      if x not in scripts]
                if additional_scripts:
                    scripts.extend(additional_scripts)
                    continue
            property_name_as_camelCase = utility_functions.to_camelCase(property_name)
            dot_path = f'{self._dot_path}.' or ''
            dot_path += property_name_as_camelCase
            scripts.extend([x for x in constants.MODULE_REQUIREMENTS.get(dot_path, [])
                            if x not in scripts])

        if include_extension:
            final_scripts = []
            for script in scripts:
                if script.endswith('.css') or script.endswith('.js'):
                    final_scripts.append(script)
                elif script.startswith('css/'):
                    final_scripts.append(f'{script}.css')
                else:
                    final_scripts.append(f'{script}.js')
            return final_scripts
            
        return scripts

    def get_required_modules(self, include_extension = False) -> List[str]:
        """Return the list of URLs from which the Highcharts JavaScript modules
        needed to render the chart can be retrieved.
        
        :param include_extension: if ``True``, will return script names with the 
          ``'.js'`` extension included. Defaults to ``False``.
        :type include_extension: :class:`bool <python:bool>`

        :rtype: :class:`list <python:list>`
        """
        initial_scripts = constants.MODULE_REQUIREMENTS.get(self._dot_path, [])
        prelim_scripts = self._process_required_modules(initial_scripts, include_extension = include_extension)
        scripts = []
        
        has_all_indicators = False
        for script in prelim_scripts:
            if script.endswith('indicators-all.js'):
                has_all_indicators = True
        
        for script in prelim_scripts:
            if '/indicators/' in script and has_all_indicators:
                continue
            scripts.append(script)
            
        return scripts

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
    def trim_iterable(untrimmed,
                      to_json = False):
        """Convert any :class:`EnforcedNullType` values in ``untrimmed`` to ``'null'``.

        :param untrimmed: The iterable whose members may still be
          :obj:`None <python:None>` or Python objects.
        :type untrimmed: iterable

        :param to_json: If ``True``, will remove all members from ``untrimmed`` that are
          not serializable to JSON. Defaults to ``False``.
        :type to_json: :class:`bool <python:bool>`

        :rtype: iterable
        """
        if not checkers.is_iterable(untrimmed, forbid_literals = (str, bytes, dict)):
            return untrimmed

        trimmed = []
        for item in untrimmed:
            if checkers.is_type(item, 'CallbackFunction') and to_json:
                continue
            elif item is None or item == constants.EnforcedNull:
                trimmed.append('null')
            elif hasattr(item, 'trim_dict'):
                untrimmed_item = item._to_untrimmed_dict()
                item_as_dict = HighchartsMeta.trim_dict(untrimmed_item, to_json = to_json)
                if item_as_dict:
                    trimmed.append(item_as_dict)
            elif isinstance(item, dict):
                if item:
                    trimmed.append(HighchartsMeta.trim_dict(item, to_json = to_json))
            elif checkers.is_iterable(item, forbid_literals = (str, bytes, dict)):
                if item:
                    trimmed.append(HighchartsMeta.trim_iterable(item, to_json = to_json))
            else:
                trimmed.append(item)

        return trimmed

    @staticmethod
    def trim_dict(untrimmed: dict,
                  to_json: bool = False) -> dict:
        """Remove keys from ``untrimmed`` whose values are :obj:`None <python:None>` and
        convert values that have ``.to_dict()`` methods.

        :param untrimmed: The :class:`dict <python:dict>` whose values may still be
          :obj:`None <python:None>` or Python objects.
        :type untrimmed: :class:`dict <python:dict>`

        :param to_json: If ``True``, will remove all keys from ``untrimmed`` that are not
          serializable to JSON. Defaults to ``False``.
        :type to_json: :class:`bool <python:bool>`

        :returns: Trimmed :class:`dict <python:dict>`
        :rtype: :class:`dict <python:dict>`
        """
        as_dict = {}
        for key in untrimmed:
            value = untrimmed.get(key, None)
            # bool -> Boolean
            if isinstance(value, bool):
                as_dict[key] = value
            # Callback Function
            elif checkers.is_type(value, 'CallbackFunction') and to_json:
                continue
            # HighchartsMeta -> dict --> object
            elif value and hasattr(value, '_to_untrimmed_dict'):
                untrimmed_value = value._to_untrimmed_dict()
                trimmed_value = HighchartsMeta.trim_dict(untrimmed_value,
                                                         to_json = to_json)
                if trimmed_value:
                    as_dict[key] = trimmed_value
            # Enforced null
            elif isinstance(value, constants.EnforcedNullType):
                as_dict[key] = 'null'
            # dict -> object
            elif isinstance(value, dict):
                trimmed_value = HighchartsMeta.trim_dict(value,
                                                         to_json = to_json)
                if trimmed_value:
                    as_dict[key] = trimmed_value
            # iterable -> array
            elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
                trimmed_value = HighchartsMeta.trim_iterable(value, to_json = to_json)
                if trimmed_value:
                    as_dict[key] = trimmed_value
            # Pandas Timestamp
            elif checkers.is_type(value, 'Timestamp'):
                as_dict[key] = value.timestamp()
            # other truthy -> str / number
            elif value:
                trimmed_value = HighchartsMeta.trim_iterable(value, to_json = to_json)
                if trimmed_value:
                    as_dict[key] = trimmed_value
            # other falsy -> str / number
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
        if allow_snake_case:
            clean_as_dict = {utility_functions.to_camelCase(key): as_dict[key]
                             for key in as_dict}
        else:
            clean_as_dict = {key: as_dict[key]
                             for key in as_dict}

        kwargs = cls._get_kwargs_from_dict(clean_as_dict)

        return cls(**kwargs)

    @classmethod
    def from_json(cls,
                  as_json_or_file,
                  allow_snake_case: bool = True):
        """Construct an instance of the class from a JSON string.

        :param as_json_or_file: The JSON string for the object or the filename of a file
          that contains the JSON string.
        :type as_json: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :param allow_snake_case: If ``True``, interprets ``snake_case`` keys as equivalent
          to ``camelCase`` keys. Defaults to ``True``.
        :type allow_snake_case: :class:`bool <python:bool>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`HighchartsMeta`
        """
        is_file = checkers.is_file(as_json_or_file)
        if is_file:
            with open(as_json_or_file, 'r') as file_:
                as_str = file_.read()
        else:
            as_str = as_json_or_file

        as_dict = json.loads(as_str)

        if checkers.is_iterable(as_dict, forbid_literals = (str, bytes, dict, UserDict)):
            return [cls.from_dict(x, allow_snake_case = allow_snake_case)
                    for x in as_dict]

        return cls.from_dict(as_dict,
                             allow_snake_case = allow_snake_case)

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

    def to_json(self,
                filename = None,
                encoding = 'utf-8'):
        """Generate a JSON string/byte string representation of the object compatible with
        the Highcharts JavaScript library.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A JSON representation of the object compatible with the Highcharts
          library.
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self._to_untrimmed_dict()

        as_dict = self.trim_dict(untrimmed, to_json = True)

        for key in as_dict:
            if as_dict[key] == constants.EnforcedNull or as_dict[key] == 'null':
                as_dict[key] = None
        try:
            as_json = json.dumps(as_dict, encoding = encoding)
        except TypeError:
            as_json = json.dumps(as_dict)

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

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
        if """document.addEventListener('DOMContentLoaded', function() {\n""" in as_str:
            as_str = as_str.replace(
                """document.addEventListener('DOMContentLoaded', function() {\n""", ''
            )
            as_str = as_str[:-3]
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

        return cls.from_dict(as_dict,
                             allow_snake_case = allow_snake_case)

    @classmethod
    def _copy_dict_key(cls,
                       key,
                       original,
                       other,
                       overwrite = True,
                       **kwargs):
        """Copies the value of ``key`` from ``original`` to ``other``.

        :param key: The key that is to be copied.
        :type key: :class:`str <python:str>`

        :param original: The original :class:`dict <python:dict>` from which it should
          be copied.
        :type original: :class:`dict <python:dict>`

        :param other: The :class:`dict <python:dict>` to which it should be copied.
        :type other: :class:`dict <python:dict>`

        :returns: The value that should be placed in ``other`` for ``key``.
        """
        original_value = original[key]
        other_value = other.get(key, None)

        if isinstance(original_value, (dict, UserDict)):
            new_value = {}
            for subkey in original_value:
                new_key_value = cls._copy_dict_key(subkey,
                                                   original_value,
                                                   other_value,
                                                   overwrite = overwrite,
                                                   **kwargs)
                new_value[subkey] = new_key_value

            return new_value

        elif checkers.is_iterable(original_value,
                                  forbid_literals = (str,
                                                     bytes,
                                                     dict,
                                                     UserDict)):
            if overwrite:
                new_value = [x for x in original_value]

                return new_value

            return other_value

        elif other_value and not overwrite:
            return other_value

        return original_value

    def copy(self,
             other = None,
             overwrite = True,
             **kwargs):
        """Copy the configuration settings from this instance to the ``other`` instance.

        :param other: The target instance to which the properties of this instance should
          be copied. If :obj:`None <python:None>`, will create a new instance and populate
          it with properties copied from ``self``. Defaults to :obj:`None <python:None>`.
        :type other: :class:`HighchartsMeta`

        :param overwrite: if ``True``, properties in ``other`` that are already set will
          be overwritten by their counterparts in ``self``. Defaults to ``True``.
        :type overwrite: :class:`bool <python:bool>`

        :param kwargs: Additional keyword arguments. Some special descendents of
          :class:`HighchartsMeta` may have special implementations of this method which
          rely on additional keyword arguments.

        :returns: A mutated version of ``other`` with new property values

        """
        if not other:
            other = self.__class__()

        if not isinstance(other, self.__class__):
            raise errors.HighchartsValueError(f'other is expected to be a '
                                              f'{self.__class__.__name__} instance. Was: '
                                              f'{other.__class__.__name__}')

        self_as_dict = self.to_dict()
        other_as_dict = other.to_dict()

        new_dict = {}
        for key in self_as_dict:
            new_dict[key] = self._copy_dict_key(key,
                                                original = self_as_dict,
                                                other = other_as_dict,
                                                overwrite = overwrite,
                                                **kwargs)

        cls = other.__class__

        other = cls.from_dict(new_dict)

        return other


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

    def to_json(self,
                filename = None,
                encoding = 'utf-8'):
        """Generate a JSON string/byte string representation of the object compatible with
        the Highcharts JavaScript library.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string.

        :param filename: The name of a file to which the JSON string should be persisted.
          Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A JSON representation of the object compatible with the Highcharts
          library.
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        if filename:
            filename = validators.path(filename)

        as_dict = self.to_dict()
        try:
            as_json = json.dumps(as_dict, encoding = encoding)
        except TypeError:
            as_json = json.dumps(as_dict)

        if filename:
            if isinstance(as_json, bytes):
                write_type = 'wb'
            else:
                write_type = 'w'

            with open(filename, write_type, encoding = encoding) as file_:
                file_.write(as_json)

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
