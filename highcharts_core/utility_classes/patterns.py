from typing import Optional
from decimal import Decimal
from fractions import Fraction

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.animation import AnimationOptions


class PatternOptions(HighchartsMeta):
    """Definition of a pattern."""

    def __init__(self, **kwargs):
        self._aspect_ratio = None
        self._background_color = None
        self._color = None
        self._height = None
        self._id = None
        self._image = None
        self._opacity = None
        self._path = None
        self._pattern_transform = None
        self._width = None
        self._x = None
        self._y = None

        self.aspect_ratio = kwargs.get('aspect_ratio', None)
        self.background_color = kwargs.get('background_color', None)
        self.color = kwargs.get('color', None)
        self.height = kwargs.get('height', None)
        self.id = kwargs.get('id', None)
        self.image = kwargs.get('image', None)
        self.opacity = kwargs.get('opacity', None)
        self.path = kwargs.get('path', None)
        self.pattern_transform = kwargs.get('pattern_transform', None)
        self.width = kwargs.get('width', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def aspect_ratio(self) -> Optional[int | float | Decimal | Fraction]:
        """For automatically calculated width and height on images, it is possible to set
        an aspect ratio. The image will be zoomed to fill the bounding box, maintaining
        the aspect ratio defined.

        :returns: The aspect ratio applied.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, value):
        self._aspect_ratio = validators.numeric(value, allow_empty = True)

    @property
    def background_color(self) -> Optional[str]:
        """Background color for the pattern if a :meth:`PatternOptions.path` is set (not
        images).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str]:
        """Pattern color, used as default path stroke.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """Height of the pattern expressed in pixels.

        .. note::

          For images this is automatically set to the height of the element bounding box
          if not supplied.

          For non-image patterns the default is ``32px``.

          Note that automatic resizing of image patterns to fill a bounding box
          dynamically is only supported for patterns with an automatically calculated ID.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def id(self) -> Optional[str]:
        """ID to assign to the pattern.

        .. note::

          This is automatically computed if not specified explicitly, and identical
          patterns are reused.

          To refer to an existing pattern for a Highcharts color in JavaScript, use color:
          ``"url(#pattern-id)"``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def image(self) -> Optional[str]:
        """URL to an image to use as the pattern.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises ValueError: if value provided is not URL or path-like
        """
        return self._image

    @image.setter
    def image(self, value):
        try:
            self._image = validators.url(value, allow_empty = True)
        except ValueError:
            self._image = validators.path(value, allow_empty = True)

    @property
    def opacity(self) -> Optional[float]:
        """Opacity of the pattern as a float value from 0 to 1.

        :rtype: :class:`float <python:float` or :obj:`None <python:None>`

        :raises ValueError: if outside the range 0 - 1
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.float(value,
                                         allow_empty = True,
                                         minimum = 0,
                                         maximum = 1)

    @property
    def path(self) -> Optional[str]:
        """An SVG path expressed as a string.

        .. note::

          If a path is supplied for the pattern, the :meth:`PatternOptions.image` property
          is ignored.

        .. warning::

          Highcharts for Python does not yet support the JavaScript
          ``Highcharts.SVGAttributes`` object. Only strings are currently supported.

        .. todo:

          Add ``Highcharts.SVGAttributes`` to utility classes.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._path

    @path.setter
    def path(self, value):
        self._path = validators.string(value, allow_empty = True)

    @property
    def pattern_transform(self) -> Optional[str]:
        """SVG ``patternTransform`` to apply to the entire pattern.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pattern_transform

    @pattern_transform.setter
    def pattern_transform(self, value):
        self._pattern_transform = validators.string(value, allow_empty = True)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """Width of the pattern expressed in pixels.

        .. note::

          For images this is automatically set to the width of the element bounding box
          if not supplied.

          For non-image patterns the default is ``32px``.

          Note that automatic resizing of image patterns to fill a bounding box
          dynamically is only supported for patterns with an automatically calculated ID.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """Horizontal offset applied to the pattern. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """Vertical offset applied to the pattern. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'aspect_ratio': as_dict.get('aspectRatio', None),
            'background_color': as_dict.get('backgroundColor', None),
            'color': as_dict.get('color', None),
            'height': as_dict.get('height', None),
            'id': as_dict.get('id', None),
            'image': as_dict.get('image', None),
            'opacity': as_dict.get('opacity', None),
            'path': as_dict.get('path', None),
            'pattern_transform': as_dict.get('patternTransform', None),
            'width': as_dict.get('width', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'aspectRatio': self.aspect_ratio,
            'backgroundColor': self.background_color,
            'color': self.color,
            'height': self.height,
            'id': self.id,
            'image': self.image,
            'opacity': self.opacity,
            'path': self.path,
            'patternTransform': self.pattern_transform,
            'width': self.width,
            'x': self.x,
            'y': self.y
        }

        return untrimmed


class Pattern(HighchartsMeta):
    """Holds a pattern definition."""

    def __init__(self, **kwargs):
        self._animation = None
        self._pattern_options = None
        self._pattern_index = None

        self.animation = kwargs.get('animation', None)
        self.pattern_options = kwargs.get('pattern_options', None)
        self.pattern_index = kwargs.get('pattern_index', None)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Animations options for the loading of image patterns.

        :returns: Settings for the animation of image patterns.
        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def pattern_options(self) -> Optional[PatternOptions]:
        """Options to define a Pattern.

        :rtype: :class:`PatternOptions` or :obj:`None <python:None>`
        """
        return self._pattern_options

    @pattern_options.setter
    @class_sensitive(PatternOptions)
    def pattern_options(self, value):
        self._pattern_options = value

    @property
    def pattern_index(self) -> Optional[int]:
        """An optional index that indicates which of Highcharts default patterns to apply.

        Default patterns are part of the (JavaScript) ``Highcharts.patterns`` array, and
        additional patterns may be added to that array as well.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._pattern_index

    @pattern_index.setter
    def pattern_index(self, value):
        self._pattern_index = validators.integer(value,
                                                 allow_empty = True,
                                                 minimum = True,
                                                 coerce_value = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        pattern_options = as_dict.get('pattern', None) or \
                          as_dict.get('pattern_options', None) or \
                          as_dict.get('patternOptions', None)
        kwargs = {
            'animation': as_dict.get('animation', None),
            'pattern_options': pattern_options,
            'pattern_index': as_dict.get('patternIndex', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'animation': self.animation,
            'pattern': self.pattern_options,
            'patternIndex': self.pattern_index
        }

        return untrimmed
