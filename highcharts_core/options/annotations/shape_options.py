from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import validate_types
from highcharts_core.utility_classes import Gradient, Pattern
from highcharts_core.options.annotations.points import AnnotationPoint
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.utility_functions import validate_color


class ShapeOptionsBase(HighchartsMeta):
    """Base set of options applied to all annotation shapes."""

    def __init__(self, **kwargs):
        self._dash_style = None
        self._fill = None
        self._height = None
        self._ry = None
        self._snap = None
        self._src = None
        self._stroke = None
        self._stroke_width = None
        self._x_axis = None
        self._y_axis = None

        self.dash_style = kwargs.get('dash_style', None)
        self.fill = kwargs.get('fill', None)
        self.height = kwargs.get('height', None)
        self.ry = kwargs.get('ry', None)
        self.snap = kwargs.get('snap', None)
        self.src = kwargs.get('src', None)
        self.stroke = kwargs.get('stroke', None)
        self.stroke_width = kwargs.get('stroke_width', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)

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
    def fill(self) -> Optional[str | Gradient | Pattern]:
        """The color of the shape's fill. Defaults to ``'rgba(0, 0, 0, 0.75)'``.

        :rtype: :class:`str <python:str>` (for colors), :class:`Gradient` for gradients,
          :class:`Pattern` for pattern definitions, or :obj:`None <python:None>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = validate_color(value)

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height of the shape in pixels.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def r(self) -> Optional[int | float | Decimal]:
        """The radius of the shape in pixels. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._r

    @r.setter
    def r(self, value):
        self._r = validators.numeric(value, allow_empty = True)

    @property
    def ry(self) -> Optional[int | float | Decimal]:
        """The radius of the shape along the vertical dimension. Used to draw ellipses.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._ry

    @ry.setter
    def ry(self, value):
        self._ry = validators.numeric(value, allow_empty = True)

    @property
    def snap(self) -> Optional[int | float | Decimal]:
        """Defines additional snapping area around an annotation making this annotation
        to focus. Defined in pixels.

        Defaults to ``2``.

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
        """The color of the shape's stroke. Defaults to
        ``'rgba(0, 0, 0, 0.75)'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        self._stroke = validators.string(value, allow_empty = True)

    @property
    def stroke_width(self) -> Optional[int | float | Decimal]:
        """The pixel stroke width of the shape. Defaults to
        ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        self._stroke_width = validators.numeric(value, allow_empty = True)

    @property
    def type(self) -> Optional[str]:
        """The type of the shape. Defaults to ``'rect'``.

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
    def width(self) -> Optional[int | float | Decimal]:
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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'dash_style': as_dict.get('dashStyle', None),
            'fill': as_dict.get('fill', None),
            'height': as_dict.get('height', None),
            'ry': as_dict.get('ry', None),
            'snap': as_dict.get('snap', None),
            'src': as_dict.get('src', None),
            'stroke': as_dict.get('stroke', None),
            'stroke_width': as_dict.get('strokeWidth', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dashStyle': self.dash_style,
            'fill': self.fill,
            'height': self.height,
            'ry': self.ry,
            'snap': self.snap,
            'src': self.src,
            'stroke': self.stroke,
            'strokeWidth': self.stroke_width,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis
        }

        return untrimmed


class ShapeOptions(ShapeOptionsBase):
    """Global options applied to all annotation shapes."""

    def __init__(self, **kwargs):
        self._r = None
        self._type = None
        self._width = None

        self.r = kwargs.get('r', None)
        self.type = kwargs.get('type', None)
        self.width = kwargs.get('width', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations.shapeOptions'

    @property
    def r(self) -> Optional[int | float | Decimal]:
        f"""The radius of the shape in pixels. Defaults to {constants.DEFAULT_SHAPES_R}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._r

    @r.setter
    def r(self, value):
        self._r = validators.numeric(value, allow_empty = True)

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
    def width(self) -> Optional[int | float | Decimal]:
        """The width of the shape, expressed in pixels.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'dash_style': as_dict.get('dashStyle', None),
            'fill': as_dict.get('fill', None),
            'height': as_dict.get('height', None),
            'r': as_dict.get('r', None),
            'ry': as_dict.get('ry', None),
            'snap': as_dict.get('snap', None),
            'src': as_dict.get('src', None),
            'stroke': as_dict.get('stroke', None),
            'stroke_width': as_dict.get('strokeWidth', None),
            'type': as_dict.get('type', None),
            'width': as_dict.get('width', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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

        return untrimmed


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

        self.marker_end = kwargs.get('marker_end', None)
        self.marker_start = kwargs.get('marker_start', None)
        self.point = kwargs.get('point', None)
        self.points = kwargs.get('points', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations.shapes'

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
    def point(self) -> Optional[str | AnnotationPoint]:
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
    def points(self) -> Optional[List[CallbackFunction | AnnotationPoint | str]]:
        """An array of points for the shape or a JavaScript callback function that returns
        that shape point.

        .. note::

          This option is available for shapes which can use multiple points such as path.
          A point can be either a :class:`AnnotationPoint` object or a point's id.

        :rtype: :class:`list <python:list>` of :class:`CallbackFunction` or
          :class:`str <python:str>` or :class:`AnnotationPoint` or
          :class:`str <python:str>`, OR :obj:`None <python:None>`
        """
        return self._points

    @points.setter
    def points(self, value):
        if not value:
            self._points = None
        elif checkers.is_iterable(value):
            processed_value = []
            for item in value:
                try:
                    item = validate_types(item, types = AnnotationPoint)
                except ValueError:
                    try:
                        item = validate_types(item, types = CallbackFunction)
                    except (ValueError, TypeError):
                        try:
                            item = validators.string(item, allow_empty = False)
                        except ValueError:
                            raise errors.HighchartsValueError(
                                f'points expects '
                                f'AnnotationPoint, '
                                f'CallbackFunction, or str'
                                f'instances. Received: '
                                f'{item.__class__.__name__}'
                            )
                processed_value.append(item)

            self._points = [x for x in processed_value]
        else:
            raise errors.HighchartsValueError('Unable to resolve the value to a '
                                              'supported type.')

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            # from ShapeOptions
            'dash_style': as_dict.get('dashStyle', None),
            'fill': as_dict.get('fill', None),
            'height': as_dict.get('height', None),
            'r': as_dict.get('r', None),
            'ry': as_dict.get('ry', None),
            'snap': as_dict.get('snap', None),
            'src': as_dict.get('src', None),
            'stroke': as_dict.get('stroke', None),
            'stroke_width': as_dict.get('strokeWidth', None),
            'type': as_dict.get('type', None),
            'width': as_dict.get('width', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),

            # from AnnotationShape
            'marker_end': as_dict.get('markerEnd', None),
            'marker_start': as_dict.get('markerStart', None),
            'point': as_dict.get('point', None),
            'points': as_dict.get('points', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'markerEnd': self.marker_end,
            'markerStart': self.marker_start,
            'point': self.point,
            'points': self.points,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


__all__ = [
    'ShapeOptions',
    'AnnotationShape',
    'ShapeOptionsBase'
]
