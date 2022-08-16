from typing import Optional
from collections import UserDict
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

from validator_collection import validators, errors as validator_errors

from highcharts import errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.javascript_functions import CallbackFunction


class MenuItem(HighchartsMeta):
    """Configuration for an item that appears in a context menu."""

    def __init__(self, **kwargs):
        self._onclick = None
        self._text = None
        self._text_key = None
        self._separator = False

        self.onclick = kwargs.get('onclick', None)
        self.text = kwargs.get('text', None)
        self.text_key = kwargs.get('text_key', None)
        self.separator = kwargs.get('separator', None)

    @property
    def onclick(self) -> Optional[CallbackFunction]:
        """JavaScript event callback function which fires when the menu item is clicked.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._onclick

    @onclick.setter
    @class_sensitive(CallbackFunction)
    def onclick(self, value):
        self._onclick = value

    @property
    def text(self) -> Optional[str]:
        """The text to display for the menu item.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @property
    def text_key(self) -> Optional[str]:
        """If internationalization is required, the key to a language string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text_key

    @text_key.setter
    def text_key(self, value):
        self._text_key = validators.string(value, allow_empty = True)

    @property
    def separator(self) -> Optional[bool]:
        """If ``True``, indicates that the item should be rendered as a separator.
        Defaults to ``False``, but may also be :obj:`None <python:None>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._separator

    @separator.setter
    def separator(self, value):
        if value is False or value is None:
            self._separator = value
        elif value:
            self._separator = True
        else:
            self._separator = False

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'onclick': as_dict.get('onclick', None),
            'text': as_dict.get('text', None),
            'text_key': as_dict.get('textKey', None),
            'separator': as_dict.get('separator', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'onclick': self.onclick,
            'text': self.text,
            'textKey': self.text_key,
            'separator': self.separator
        }

        return untrimmed


class MenuObject(UserDict):
    """Special :class:`dict <python:dict>` class used to construct a Highcharts menu
    configuration. Each key represents the identifier of a menu item, while the object
    is a configuration of that menu item's settings.

    Keys are validated to be valid variable names, while each value is validated to be a
    :class:`MenuItem`.

    """

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

        item = validate_types(item,
                              types = MenuItem,
                              allow_none = False)

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

    def _to_untrimmed_dict(self) -> dict:
        return self.data

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
