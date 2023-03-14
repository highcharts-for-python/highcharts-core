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

from validator_collection import validators, errors as validator_errors


from highcharts_core.decorators import validate_types, class_sensitive
from highcharts_core.metaclasses import HighchartsMeta, JavaScriptDict


class AttributeObject(JavaScriptDict):
    """Special :class:`dict <python:dict>` class used to construct an arbitrary set of
    SVG attributes. Each key represents the key to the attribute (expressed as a string),
    while the value represents the value of the attribute.

    Keys are validated to be valid variable names.
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

        super().__setitem__(key, item)


class ASTNode(HighchartsMeta):
    """Generic representation of an AST node."""

    def __init__(self, **kwargs):
        self._attributes = None
        self._children = []
        self._tag_name = None
        self._text_content = None

        self.attributes = kwargs.get('attributes', None)
        self.children = kwargs.get('children', [])
        self.tag_name = kwargs.get('tag_name', None)
        self.text_content = kwargs.get('text_content', None)

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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'attributes': as_dict.get('attributes', None),
            'children': as_dict.get('children', []),
            'tag_name': as_dict.get('tagName', None),
            'text_content': as_dict.get('textContent', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'attributes': self.attributes,
            'children': self.children,
            'tagName': self.tag_name,
            'textContent': self.text_content
        }

        return untrimmed


class ASTMap(JavaScriptDict):
    """Special :class:`dict <python:dict>` class used to construct a JavaScript object
    literal map. Each key represents a key or node within that map, while
    the value for that key is an :class:`ASTNode`.

    Keys are validated to be valid variable names, while each value is validated to be an
    :class:`ASTNode`.

    """
    _valid_value_types = ASTNode
    _allow_empty_value = True


class TextPath(HighchartsMeta):
    """Options for a label text which should follow marker's shape.

    .. note::

      Border and background are disabled for a label that follows a path.

    .. warning::

      Only SVG-based renderer supports this option. Setting :meth:`DataLabel.use_html` to
      ``True`` will disable this option.

    """

    def __init__(self, **kwargs):
        self._attributes = None
        self._enabled = None

        self.attributes = kwargs.get('attributes', None)
        self.enabled = kwargs.get('enabled', None)

    @property
    def attributes(self) -> Optional[AttributeObject]:
        """Presentation attributes for the text path.

        :rtype: :class:`AttributeObject` or :obj:`None <python:None>`
        """
        return self._attributes

    @attributes.setter
    @class_sensitive(AttributeObject)
    def attributes(self, value):
        self._attributes = value

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the use of a text path for links or marker data labels.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'attributes': as_dict.get('attributes', None),
            'enabled': as_dict.get('enabled', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'attributes': self.attributes,
            'enabled': self.enabled
        }

        return untrimmed
