from typing import Optional, List

from validator_collection import validators

from highcharts.decorators import validate_types, class_sensitive
from highcharts.utility_classes.ast import AttributeObject, ASTNode, ASTMap


class MarkerAttributeObject(AttributeObject):
    """Special subclass of the :class:`SVGAttributeMap` which provides properties for
    annotation markers.

    While this class also is a special subclass of :class:`dict <python:dict>`, it also
    propagates values from certain named properties to corresponding key entries in the
    underling :class:`dict <python:dict>`'s data map.

    """

    def __init__(self, *args, **kwargs):
        self._id = None
        self._ref_x = None
        self._ref_y = None
        self._marker_width = 10
        self._marker_height = 10

        self.id = kwargs.pop('id', None)
        self.ref_x = kwargs.pop('refX', None)
        self.ref_y = kwargs.pop('refY', None)
        self.marker_width = kwargs.pop('marker_width', 10)
        self.marker_height = kwargs.pop('marker_height', 10)

        super().__init__(*args, **kwargs)

    @property
    def id(self) -> Optional[str]:
        """The identifier applied to the marker.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        value = validators.string(value, allow_empty = True)
        self._id = value
        self['id'] = value

    @property
    def ref_x(self) -> Optional[int]:
        """TBD

        .. todo::

          Determine what purpose the refX and refY properties serve.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._ref_x

    @ref_x.setter
    def ref_x(self, value):
        value = validators.integer(value, allow_empty = True, coerce_value = True)
        self._ref_x = value
        self['refX'] = value

    @property
    def ref_y(self) -> Optional[int]:
        """TBD

        .. todo::

          Determine what purpose the refX and refY properties serve.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._ref_y

    @ref_y.setter
    def ref_y(self, value):
        value = validators.integer(value, allow_empty = True, coerce_value = True)
        self._ref_y = value
        self['refY'] = value

    @property
    def marker_width(self) -> Optional[int]:
        """The width of the marker, expressed in pixels.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._marker_width

    @marker_width.setter
    def marker_width(self, value):
        value = validators.integer(value, allow_empty = True, coerce_value = True)
        self._marker_width = value
        self['markerWidth'] = value

    @property
    def marker_height(self) -> Optional[int]:
        """The height of the marker, expressed in pixels.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._marker_height

    @marker_height.setter
    def marker_height(self, value):
        value = validators.integer(value, allow_empty = True, coerce_value = True)
        self._marker_height = value
        self['markerHeight'] = value


class MarkerASTNode(ASTNode):
    """:class:`ASTNode` that enforces a Marker Attribute set.."""

    @property
    def attributes(self) -> Optional[MarkerAttributeObject]:
        """Map of attributes that are used to describe the node.

        Basically corresponds to a :class:`dict <python:dict>`, where keys have to
        generally conform to standard variable-naming conventions and values are basic
        literals (string, array, numer, boolean, :class:`dict <python:dict>`, etc.)

        :rtype: :class:`MarkerAttributeObject` or :obj:`None <python:None>`
        """
        return self._attributes

    @attributes.setter
    @class_sensitive(MarkerAttributeObject)
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
                                   types = ASTNode,
                                   allow_none = False,
                                   force_iterable = True)
            self._children = value


class MarkerDefinition(ASTMap):
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
                              types = MarkerASTNode,
                              allow_none = False)

        super().__setitem__(key, item)
