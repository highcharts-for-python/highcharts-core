from typing import Optional, List
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

from validator_collection import validators

from highcharts.decorators import validate_types, class_sensitive
from highcharts.metaclasses import HighchartsMeta


class AttributeObject(UserDict):
    """Special :class:`dict <python:dict>` class used to construct an arbitrary set of
    SVG attributes. Each key represents the key to the attribute (expressed as a string),
    while the value represents the value of the attribute.

    Keys are validated to be valid variable names.
    """

    def __setitem__(self, key, item):
        if key not in self:
            key = validators.variable_name(key, allow_empty = False)

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


class ASTNode(HighchartsMeta):
    """Generic representation of an AST node."""

    def __init__(self, **kwargs):
        self._attributes = None
        self._children = []
        self._tag_name = None
        self._text_content = None

        self.attributes = kwargs.pop('attributes', None)
        self.children = kwargs.pop('children', [])
        self.tag_name = kwargs.pop('tag_name', None)
        self.text_content = kwargs.pop('text_content', None)

    @property
    def attributes(self) -> Optional[AttributeObject]:
        """Map of attributes that are used to describe the node.

        Basically corresponds to a :class:`dict <python:dict>`, where keys have to
        generally conform to standard variable-naming conventions and values are basic
        literals (string, array, numer, boolean, :class:`dict <python:dict>`, etc.)

        :rtype: :class:`SVGAttributeMap` or :obj:`None <python:None>`
        """
        return self._attributes

    @attributes.setter
    @class_sensitive(AttributeObject)
    def attributes(self, value):
        self._attributes = value

    @property
    def children(self) -> List:
        """Collection of :class:`ASTNode` instances that should be considered children
        of this node.

        :rtype: :class:`list <python:list>` of :class:`ASTNode` objects
        """
        return self._children

    @children.setter
    def children(self, value):
        if not value:
            self._children = []
        else:
            value = validate_types(value,
                                   types = self.__class__,
                                   allow_none = False,
                                   force_iterable = True)
            self._children = value

    @property
    def tag_name(self) -> Optional[str]:
        """The name given to the SVG tag.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = validators.string(value, allow_empty = True)

    @property
    def text_content(self) -> Optional[str]:
        """Text content that populates the tag, if applicable.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text_content

    @text_content.setter
    def text_content(self, value):
        self._text_content = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'attributes': as_dict.pop('attributes', None),
            'children': as_dict.pop('children', []),
            'tag_name': as_dict.pop('tagName', None),
            'text_content': as_dict.pop('textContent', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'attributes': self.attributes,
            'children': self.children,
            'tagName': self.tag_name,
            'textContent': self.text_content
        }

        return self.trim_dict(untrimmed)


class ASTMap(UserDict):
    """Special :class:`dict <python:dict>` class used to construct a JavaScript object
    literal map. Each key represents a key or node within that map, while
    the value for that key is an :class:`ASTNode`.

    Keys are validated to be valid variable names, while each value is validated to be an
    :class:`ASTNode`.

    """

    def __setitem__(self, key, item):
        if key not in self:
            key = validators.variable_name(key, allow_empty = False)

        item = validate_types(item,
                              types = ASTNode,
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
