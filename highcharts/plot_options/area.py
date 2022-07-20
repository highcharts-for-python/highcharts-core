from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.plot_options.series import SeriesOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class AreaOptions(SeriesOptions):
    """General options to apply to all Area series types.

    .. figure:: _static/area-example.png
      :alt: Area Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._fill_color = None
        self._fill_opacity = 0.75
        self._line_color = None
        self._negative_fill_color = None
        self._track_by_area = False

        self.fill_color = kwargs.pop('fill_color', None)
        self.fill_opacity = kwargs.pop('fill_opacity', 0.75)
        self.line_color = kwargs.pop('line_color', None)
        self.negative_fill_color = kwargs.pop('negative_fill_color', None)
        self.track_by_area = kwargs.pop('track_by_area', False)

        super(self).__init__(**kwargs)

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
        if not value:
            self._fill_color = None
        elif isinstance(value, constants.EnforcedNullType):
            self._fill_color = constants.EnforcedNull
        elif isinstance(value, (Gradient, Pattern)):
            self._fill_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._fill_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Gradient.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._fill_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._fill_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Pattern.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._fill_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
        if not value:
            self._line_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._line_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._line_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Gradient.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._line_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._line_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Pattern.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._line_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def negative_fill_color(self) -> Optional[str | Gradient | Pattern]:
        """A separate color for the negative part of the area.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._negative_fill_color

    @negative_fill_color.setter
    def negative_fill_color(self, value):
        if not value:
            self._negative_fill_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._negative_fill_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._negative_fill_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._negative_fill_color = Gradient.from_dict(value)
                else:
                    self._negative_fill_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._negative_fill_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._negative_fill_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._negative_fill_color = Pattern.from_dict(value)
                else:
                    self._negative_fill_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._negative_fill_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', 0.75),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', False),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'fillColor': self.fill_color,
            'fillOpacity': self.fill_opacity,
            'lineColor': self.line_color,
            'negativeFillColor': self.negative_fill_color,
            'trackByArea': self.track_by_area,
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class AreaRangeOptions(AreaOptions):
    """General options to apply to all AreaRange series types. The area range series
    is a carteseian series with higher and lower values for each point along an X
    axis, where the area between the values is shaded.

    .. figure:: _static/arearange-example.png
      :alt: AreaRange Example Chart
      :align: center

    """
    pass


class AreaSplineOptions(AreaOptions):
    """General options to apply to all AreaSpline series types. The area spline series
    is an area series where the graph between the points is smoothed into a spline.

    .. figure:: _static/areaspline-example.png
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

    .. figure:: _static/line-example.png
      :alt: Line Example Chart
      :align: center

    """
    pass
