"""Set of metaclasses used throughout the library."""
from typing import Any
from abc import ABC, abstractmethod
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
from validator_collection import validators

from highcharts import constants


class HighchartsMeta(ABC):
    """Metaclass that is used to define the standard interface exposed for serializable
    objects."""

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs.get(key, None))

    @staticmethod
    def trim_dict(untrimmed):
        """Remove keys from ``untrimmed`` whose values are :obj:`None <python:None>` and
        convert values that have ``.to_dict()`` methods.

        :returns: Trimmed :class:`dict <python:dict>`
        :rtype: :class:`dict <python:dict>`
        """
        as_dict = {}
        for key in untrimmed:
            value = untrimmed.get(key, None)
            if value and hasattr(value, 'to_dict'):
                as_dict[key] = value.to_dict()
            elif value:
                as_dict[key] = value

        return as_dict

    @classmethod
    @abstractmethod
    def from_dict(cls, as_dict: dict):
        """Construct an instance of the class from a :class:`dict <python:dict>` object.

        :param as_dict: A :class:`dict <python:dict>` representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: A Python object representation of ``as_dict``.
        :rtype: :class:`HighchartsMeta`
        """
        raise NotImplementedError()

    @classmethod
    def from_json(cls, as_json: Any[str, bytes]):
        """Construct an instance of the class from a JSON string.

        :param as_json: The JSON string for the object.
        :type as_json: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`HighchartsMeta`
        """
        as_dict = json.loads(as_json)

        return cls.from_dict(as_dict)

    @abstractmethod
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
        raise NotImplementedError()

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
        for key in as_dict:
            if as_dict[key] == constants.EnforcedNull:
                as_dict[key] = None
        try:
            as_json = json.dumps(as_dict, encoding = encoding)
        except TypeError:
            as_json = json.dumps(as_dict)

        return as_json

    def to_js_literal(self):
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :rtype: :class:`str <python:str>`
        """
        as_dict = self.to_dict()
        as_json = self.to_json()

        keys_possible_code = [(key, as_dict[key]) for key in as_dict
                              if isinstance(as_dict[key], str) is True]
        for item in keys_possible_code:
            value = item[1]
            try:
                parse_result = esprima.parse(value)
            except ParseError:
                keys_possible_code.remove(item)

            first_obj = parse_result.get('body', None)
            if not first_obj:
                keys_possible_code.remove(item)
            first_type = first_obj.get('type', None)
            if first_type not in constants.ALLOWED_JS_LITERAL_TYPES:
                keys_possible_code.remove(item)

        # TODO: IMPLEMENT THIS METHOD

        raise NotImplementedError()




class JavaScriptDict(UserDict):
    """Special :class:`dict <python:dict>` class which constructs a JavaScript
    object that can be represented as a string.

    Keys are validated to be valid variable names, while values are validated to be
    strings.

    When serialized to :class:`str <python:str>`, keys are **not** wrapped in double
    quotes (as they would be in JSON) to ensure that the resulting string can be evaluated
    as JavaScript code.

    """

    def __setitem__(self, key, item):
        if key not in self:
            key = validators.variable_name(key, allow_empty = False)

        item = validators.string(item, allow_empty = True)

        super().__setitem__(key, item)

    def __str__(self):
        """Serializes the instance to a :class:`str <python:str>`, however applying
        special logic to ensure that the string can be executed as valid JavaScript code.
        These rules are as follows:

          #. Keys are not wrapped in single or double-quotes.
          #. Line indententation for keys is based on the JAVASCRIPT_INDENT_SPACES
             environment variable.
          #. Values are not wrapped in quotes (unlike JSON) so that they can be executed.

        .. hint::

          If you need a JSON represnetation of this class, you can call the
          :meth:`to_dict() <JavaScriptDict.to_dict>` method, which serializes to a
          standard JSON syntax.

        :returns: An executable JavaScript code snippet expressed as a string.
        :rtype: :class:`str <python:str>`
        """
        as_str = '{\n'
        for key in self:
            item = self[key]
            as_str += f'\n{constants.JAVASCRIPT_INDENT}{key}: {item}'
        as_str += '\n};'

        return as_str

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
