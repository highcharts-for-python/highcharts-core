from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class AreaOptions(SeriesOptions):
    """General options to apply to all Area series types.

    .. figure:: ../../../_static/area-example.png
      :alt: Area Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._fill_color = None
        self._fill_opacity = None
        self._line_color = None
        self._negative_fill_color = None
        self._track_by_area = None

        self.fill_color = kwargs.get('fill_color', None)
        self.fill_opacity = kwargs.get('fill_opacity', None)
        self.line_color = kwargs.get('line_color', None)
        self.negative_fill_color = kwargs.get('negative_fill_color', None)
        self.track_by_area = kwargs.get('track_by_area', None)

        super().__init__(**kwargs)

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern | constants.EnforcedNullType]:
        """Fill color or gradient for the area. When :class:`EnforcedNullType`, the
        series' color is used with the series'
        :meth:`fill_opacity <AreaOptions.fill_opacity>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`EnforcedNullType`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        from highcharts_core import utility_functions
        self._fill_color = utility_functions.validate_color(value)

    @property
    def fill_opacity(self) -> Optional[int | float | Decimal]:
        """Fill opacity for the area. Defaults to ``0.75``.

        When you set an explicit :meth:`fill_color <AreaOptions.fill_color>`, the
        ``fill_opacity`` is not applied. Instead, you should define the opacity in the
        :meth:`fill_color <AreaOptions.fill_color>` with an rgba color definition.

        The ``fill_opacity`` setting, also the default setting, overrides the alpha
        component of the color setting.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._fill_opacity

    @fill_opacity.setter
    def fill_opacity(self, value):
        self._fill_opacity = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """A separate color for the graph line. When :obj:`None <python:None>`, by default
        the line takes the color of the series, but the ``line_color`` setting allows
        setting a separate color for the line without altering the
        :meth:`fill_color <AreaOptions.fill_color>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        from highcharts_core import utility_functions
        self._line_color = utility_functions.validate_color(value)

    @property
    def negative_fill_color(self) -> Optional[str | Gradient | Pattern]:
        """A separate color for the negative part of the area.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._negative_fill_color

    @negative_fill_color.setter
    def negative_fill_color(self, value):
        from highcharts_core import utility_functions
        self._negative_fill_color = utility_functions.validate_color(value)

    @property
    def track_by_area(self) -> Optional[bool]:
        """When ``True``, the whole area should respond to mouseover tooltips and other
        mouse or touch events. When ``False``, only the line responds to mouse/touch
        events. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._track_by_area

    @track_by_area.setter
    def track_by_area(self, value):
        if value is None:
            self._track_by_area = None
        else:
            self._track_by_area = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'track_by_area': as_dict.get('trackByArea', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fillColor': self.fill_color,
            'fillOpacity': self.fill_opacity,
            'lineColor': self.line_color,
            'negativeFillColor': self.negative_fill_color,
            'trackByArea': self.track_by_area,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class AreaRangeOptions(AreaOptions):
    """General options to apply to all AreaRange series types. The area range series
    is a carteseian series with higher and lower values for each point along an X
    axis, where the area between the values is shaded.

    .. figure:: ../../../_static/arearange-example.png
      :alt: AreaRange Example Chart
      :align: center

    """
    pass


class AreaSplineOptions(AreaOptions):
    """General options to apply to all AreaSpline series types. The area spline series
    is an area series where the graph between the points is smoothed into a spline.

    .. figure:: ../../../_static/areaspline-example.png
      :alt: AreaSpline Example Chart
      :align: center

    """
    pass


class AreaSplineRangeOptions(AreaOptions):
    """General options to apply to all AreaSplineRange series types. The area spline
    range series is a carteseian series type with higher and lower Y values along an X
    axis. The area inside the range is colored, and the graph outlining the area is a
    smoothed spline."""
    pass


class LineOptions(AreaOptions):
    """General options to apply to all Line series types.

    A line series displays information as a series of data points connected by
    straight line segments.

    .. figure:: ../../../_static/line-example.png
      :alt: Line Example Chart
      :align: center

    """
    pass


class StreamGraphOptions(AreaOptions):
    """General options to apply to all Stream Graph series types.

    A streamgraph is a type of stacked area graph which is displaced around a central
    axis, resulting in a flowing, organic shape.

    .. figure:: ../../../_static/streamgraph-example.png
      :alt: StreamGraph Example Chart
      :align: center

    """
    pass
