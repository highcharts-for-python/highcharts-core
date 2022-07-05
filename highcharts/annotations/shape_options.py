from typing import Optional, Any, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import validate_types
from highcharts.utility_classes import Gradient, Pattern
from highcharts.annotations.points import AnnotationPoint
from highcharts.metaclasses import HighchartsMeta


class ShapeOptions(HighchartsMeta):
    """Global options applied to all annotation shapes."""

    def __init__(self, **kwargs):
        self._dash_style = None
        self._fill = constants.DEFAULT_SHAPES_FILL
        self._height = None
        self._r = constants.DEFAULT_SHAPES_R
        self._ry = None
        self._snap = constants.DEFAULT_SHAPES_SNAP
        self._src = None
        self._stroke = constants.DEFAULT_SHAPES_STROKE
        self._stroke_width = constants.DEFAULT_SHAPES_STROKE_WIDTH
        self._type = constants.DEFAULT_SHAPES_TYPE
        self._width = None
        self._x_axis = None
        self._y_axis = None

        self.dash_style = kwargs.pop('dash_style', None)
        self.fill = kwargs.pop('fill', constants.DEFAULT_SHAPES_FILL)
        self.height = kwargs.pop('height', None)
        self.r = kwargs.pop('r', constants.DEFAULT_SHAPES_R)
        self.ry = kwargs.pop('ry', None)
        self.snap = kwargs.pop('snap', constants.DEFAULT_SHAPES_SNAP)
        self.src = kwargs.pop('src', None)
        self.stroke = kwargs.pop('stroke', constants.DEFAULT_SHAPES_STROKE)
        self.stroke_width = kwargs.pop('stroke_width',
                                       constants.DEFAULT_SHAPES_STROKE_WIDTH)
        self.type = kwargs.pop('type', constants.DEFAULT_SHAPES_TYPE)
        self.width = kwargs.pop('width', None)
        self.x_axis = kwargs.pop('x_axis', None)
        self.y_axis = kwargs.pop('y_axis', None)

    @property
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the shape's stroke.

        Accepts the following values:

          * ``'Solid'``
          * ``'ShortDash'``
          * ``'ShortDot'``
          * ``'ShortDashDot'``
          * ``'ShortDashDotDot'``
          * ``'Dot'``
          * ``'Dash'``
          * ``'LongDash'``
          * ``'DashDot'``
          * ``'LongDashDot'``
          * ``'LongDashDotDot'``

        :returns: The name of the dash style to apply to the shape's stroke.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._dash_style = None
        else:
            if value not in constants.SHAPES_ALLOWED_DASH_STYLES:
                raise errors.HighchartsValueError(f'dash_style expects a supported value.'
                                                  f' Received: {value}')
            self._dash_style = value

    @property
    def fill(self) -> Optional[Any[str, Gradient, Pattern]]:
        f"""The color of the shape's fill. Defaults to {constants.DEFAULT_SHAPES_FILL}.

        :rtype: :class:`str <python:str>` (for colors), :class:`Gradient` for gradients,
          :clsas:`Pattern` for pattern definitions, or :obj:`None <python:None>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        if not value:
            self._fill = None
        elif isinstance(value, (Gradient, Pattern)):
            self._fill = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._fill = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill = Gradient.from_dict(value)
                else:
                    self._fill = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._fill = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._fill = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill = Pattern.from_dict(value)
                else:
                    self._fill = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._fill = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def height(self) -> Optional[Any[int, float, Decimal]]:
        """The height of the shape in pixels.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def r(self) -> Optional[Any[int, float, Decimal]]:
        f"""The radius of the shape in pixels. Defaults to {constants.DEFAULT_SHAPES_R}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._r

    @r.setter
    def r(self, value):
        self._r = validators.numeric(value, allow_empty = True)

    @property
    def ry(self) -> Optional[Any[int, float, Decimal]]:
        """The radius of the shape along the vertical dimension. Used to draw ellipses.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._ry

    @ry.setter
    def ry(self, value):
        self._ry = validators.numeric(value, allow_empty = True)

    @property
    def snap(self) -> Optional[Any[int, float, Decimal]]:
        f"""Defines additional snapping area around an annotation making this annotation
        to focus. Defined in pixels.

        Defaults to ``{constants.DEFAULT_SHAPES_SNAP}``

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._snap

    @snap.setter
    def snap(self, value):
        self._snap = validators.numeric(value, allow_empty = True)

    @property
    def src(self) -> Optional[str]:
        """The URL for an image to use as the annotation shape.

        .. note::

          :meth:`ShapeOptions.type` has to be set to ``'image'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises HighchartsValueError: if a value is supplied that is not a URL or not
          path-like

        """
        return self._src

    @src.setter
    def src(self, value):
        if not value:
            self._src = None
        else:
            try:
                self._src = validators.url(value)
            except ValueError:
                try:
                    self._src = validators.path(value)
                except ValueError:
                    raise errors.HighchartsValueError(f'value provided ({value}) not a '
                                                      f'valid URL or path')

    @property
    def stroke(self) -> Optional[str]:
        f"""The color of the shape's stroke. Defaults to
        ``{constants.DEFAULT_SHAPES_STROKE}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        self._stroke = validators.string(value, allow_empty = True)

    @property
    def stroke_width(self) -> Optional[Any[int, float, Decimal]]:
        f"""The pixel stroke width of the shape. Defaults to
        ``{constants.DEFAULT_SHAPES_STROKE_WIDTH}``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        self._stroke_width = validators.numeric(value, allow_empty = True)

    @property
    def type(self) -> Optional[str]:
        f"""The type of the shape. Defaults to ``{constants.DEFAULT_SHAPES_TYPE}``.

        Accepts:

          * ``'rect'``
          * ``'circle'``
          * ``'ellipse'``
          * ``'image'``

        :returns: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises HighchartsValueError: if type not supported
        """
        return self._type

    @type.setter
    def type(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._type = None
        else:
            value = value.lower()
            if value not in ['rect', 'circle', 'ellipse']:
                raise errors.HighchartsValueError(f'ShapeOptions.type accepts either '
                                                  f'"rect", "circle", "image", or '
                                                  f'"ellipse". Received: {value}')
            self._type = value

    @property
    def width(self) -> Optional[Any[int, float, Decimal]]:
        """The width of the shape, expressed in pixels.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @property
    def x_axis(self) -> Optional[int]:
        """The X-Axis index to which the points should be attached.

        .. note::

          Used for the ``ellipse`` :meth:`type <ShapeOptions.type>`

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`

        :raises ValueError: if set to a negative value

        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        self._x_axis = validators.integer(value,
                                          allow_empty = True,
                                          minimum = 0,
                                          coerce_value = True)

    @property
    def y_axis(self) -> Optional[int]:
        """The Y-Axis index to which the points should be attached.

        .. note::

          Used for the ``ellipse`` :meth:`type <ShapeOptions.type>`

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`

        :raises ValueError: if set to a negative value
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        self._y_axis = validators.integer(value,
                                          allow_empty = True,
                                          minimum = 0,
                                          coerce_value = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'dash_style': as_dict.pop('dashStyle', None),
            'fill': as_dict.pop('fill', constants.DEFAULT_SHAPES_FILL),
            'height': as_dict.pop('height', None),
            'r': as_dict.pop('r', constants.DEFAULT_SHAPES_R),
            'ry': as_dict.pop('ry', None),
            'snap': as_dict.pop('snap', constants.DEFAULT_SHAPES_SNAP),
            'src': as_dict.pop('src', None),
            'stroke': as_dict.pop('stroke', constants.DEFAULT_SHAPES_STROKE),
            'stroke_width': as_dict.pop('strokeWidth',
                                        constants.DEFAULT_SHAPES_STROKE_WIDTH),
            'type': as_dict.pop('type', constants.DEFAULT_SHAPES_TYPE),
            'width': as_dict.pop('width', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'dashStyle': self.dash_style,
            'fill': self.fill,
            'height': self.height,
            'r': self.r,
            'ry': self.ry,
            'snap': self.snap,
            'src': self.src,
            'stroke': self.stroke,
            'strokeWidth': self.stroke_width,
            'type': self.type,
            'width': self.width,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis
        }

        return self.trim_dict(untrimmed)


class AnnotationShape(ShapeOptions):
    """Configuration for an annotation shape applied to a specific point.

    Used to override the global settings configured in :class:`ShapeOptions` and applied
    via :meth:`Annotation.shape_options`.
    """

    def __init__(self, **kwargs):
        self._marker_end = None
        self._marker_start = None
        self._point = None
        self._points = None

        self.marker_end = kwargs.pop('marker_end', None)
        self.marker_start = kwargs.pop('marker_start', None)
        self.point = kwargs.pop('point', None)
        self.points = kwargs.pop('points', None)

    @property
    def marker_end(self) -> Optional[str]:
        """ID of the marker which will be drawn at the final vertex of the path.

        .. note::

          Custom markers can be defined in the :meth:`Options.defs` property.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._marker_end

    @marker_end.setter
    def marker_end(self, value):
        self._marker_end = validators.string(value, allow_empty = True)

    @property
    def marker_start(self) -> Optional[str]:
        """ID of the marker which will be drawn at the first vertex of the path.

        .. note::

          Custom markers can be defined in the :meth:`Options.defs` property.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._marker_start

    @marker_start.setter
    def marker_start(self, value):
        self._marker_start = validators.string(value, allow_empty = True)

    @property
    def point(self) -> Optional[Any[str, AnnotationPoint]]:
        """Determines the point to which the shape will be connected.

        It can be either the ID of the point which exists in the series, or a new point
        with defined x, y properties and optionally axes.

        :rtype: :class:`str <python:str>` or :class:`AnnotationPoint` or
          :obj:`None <python:None>`

        :raises HighchartsValueError: if cannot resolve the value to an allowed type
        """
        return self._point

    @point.setter
    def point(self, value):
        if not value:
            self._point = None
        elif isinstance(value, AnnotationPoint):
            self._point = value
        elif isinstance(value, str):
            try:
                self._point = AnnotationPoint.from_json(value)
            except ValueError:
                self._point = validators.string(value)
        elif isinstance(value, dict):
            self._point = AnnotationPoint.from_dict(value)
        else:
            raise errors.HighchartsValueError('Unable to resolve the value supplied to a '
                                              'supported type.')

    @property
    def points(self) -> Optional[List[Any[str, AnnotationPoint]]]:
        """An array of points for the shape or a JavaScript callback function that returns
        that shape point.

        .. note::

          This option is available for shapes which can use multiple points such as path.
          A point can be either a :class:`AnnotationPoint` object or a point's id.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or
          :class:`AnnotationPoint`, OR :obj:`None <python:None>`
        """
        return self._points

    @points.setter
    def points(self, value):
        if not value:
            self._points = None
        elif checkers.is_iterable(value):
            try:
                value = [validate_types(x, types = AnnotationPoint)
                         for x in value]
            except ValueError:
                value = validators.string(value)

            self._points = value
        else:
            raise errors.HighchartsValueError('Unable to resolve the value to a '
                                              'supported type.')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'dash_style': as_dict.pop('dashStyle', None),
            'fill': as_dict.pop('fill', constants.DEFAULT_SHAPES_FILL),
            'height': as_dict.pop('height', None),
            'marker_end': as_dict.pop('markerEnd', None),
            'marker_start': as_dict.pop('markerStart', None),
            'point': as_dict.pop('point', None),
            'points': as_dict.pop('points', None),
            'r': as_dict.pop('r', constants.DEFAULT_SHAPES_R),
            'ry': as_dict.pop('ry', None),
            'snap': as_dict.pop('snap', constants.DEFAULT_SHAPES_SNAP),
            'src': as_dict.pop('src', None),
            'stroke': as_dict.pop('stroke', constants.DEFAULT_SHAPES_STROKE),
            'stroke_width': as_dict.pop('strokeWidth',
                                        constants.DEFAULT_SHAPES_STROKE_WIDTH),
            'type': as_dict.pop('type', constants.DEFAULT_SHAPES_TYPE),
            'width': as_dict.pop('width', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'dashStyle': self.dash_style,
            'fill': self.fill,
            'height': self.height,
            'markerEnd': self.marker_end,
            'markerStart': self.marker_start,
            'point': self.point,
            'points': self.points,
            'r': self.r,
            'ry': self.ry,
            'snap': self.snap,
            'src': self.src,
            'stroke': self.stroke,
            'strokeWidth': self.stroke_width,
            'type': self.type,
            'width': self.width,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis
        }

        return self.trim_dict(untrimmed)


__all__ = [
    'ShapeOptions'
]
