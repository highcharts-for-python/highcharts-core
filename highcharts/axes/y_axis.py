from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.data_labels import DataLabel

from highcharts.axes.x_axis import XAxis


class YAxis(XAxis):
    """Configuration settings for the Y axis or value axis.

    Normally, this is the vertical axis, though if the chart is inverted this becomes
    the horizontal axis."""

    def __init__(self, **kwargs):
        self._max_color = None
        self._min_color = None
        self._stack_labels = None
        self._stops = None
        self._tooltip_value_format = None

        self.max_color = kwargs.pop('max_color', None)
        self.min_color = kwargs.pop('min_color', None)
        self.stack_labels = kwargs.pop('stack_labels', None)
        self.stops = kwargs.pop('stops', None)
        self.tooltip_value_format = kwargs.pop('tooltip_value_format', None)

        super().__init__(**kwargs)

    @property
    def max_color(self) -> Optional[str | Gradient | Pattern]:
        """The color used to represent the maximum value of the Y-axis. Defaults to
        ``'#003399'``.

        .. warning::

          Only applies to :term:`gauge charts <Gauge Chart>`.

        .. warning::

          Will be ignored if :meth:`YAxis.stops` are set.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._max_color

    @max_color.setter
    def max_color(self, value):
        from highcharts import utility_functions
        self._max_color = utility_functions.validate_color(value)

    @property
    def min_color(self) -> Optional[str | Gradient | Pattern]:
        """The color used to represent the minimum value of the Y-axis. Defaults to
        ``'#e6bef5'``.

        .. warning::

          Only applies to :term:`gauge charts <Gauge Chart>`.

        .. warning::

          Will be ignored if :meth:`YAxis.stops` are set.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._min_color

    @min_color.setter
    def min_color(self, value):
        from highcharts import utility_functions
        self._min_color = utility_functions.validate_color(value)

    @property
    def stack_labels(self) -> Optional[DataLabel]:
        """Configuration settings for the labels that show the total value for each bar in
        a stacked column or bar chart.

        The label will be placed on top of positive columns and below negative columns.
        In case of an inverted column or bar chart, the label is placed to the right of
        positive bars and to the left of negative bars.

        :rtype: :class:`DataLabel` or :obj:`None <python:None>`
        """
        return self._stack_labels

    @stack_labels.setter
    @class_sensitive(DataLabel)
    def stack_labels(self, value):
        self._stack_labels = value

    @property
    def stops(self) -> Optional[List[List[int | float | Decimal | str]]]:
        """Color stops for use in the gradient of a solid gauge. Defaults to
        :obj:`None <python:None>`.

        .. hint::

          Use this in cases where a linear gradient between a
          :meth:`min_color <YAxis.min_color>` and :meth:`max_color <YAxis.max_color>` is
          not sufficient.

        .. note::

          Expects an iterable of 2-member iterables. Each 2-member iterable should be
          composed of a number and a string. The number should be a value between 0 and
          1 which assigns the relative position of the color in the gradient, while the
          string should represent the color itself.

        :rtype: :class:`list <python:list>` of :class:`list <python:list>`, where each
          second :class:`list <python:list>` consists of a :class:`float <python:float>`
          and a :class:`str <python:str>` / or :obj:`None <python:None>`
        """
        return self._stops

    @stops.setter
    def stops(self, value):
        if not value:
            self._stops = None
        else:
            value = validators.iterable(value)
            processed_items = []
            for item in value:
                item = validators.iterable(item)
                if len(item) != 2:
                    raise errors.HighchartsValueError(f'stops expects a list of 2-'
                                                      f'member iterables. Received a '
                                                      f'{len(item)}-member iterable.')
                item = [validators.float(item[0],
                                         minimum = 0,
                                         maximum = 1),
                        validators.string(item[1])]
                processed_items.append(item)

            self._stops = processed_items

    @property
    def tooltip_value_format(self) -> Optional[str]:
        """Format string that will be used for ``point.y`` and available in (JavaScript)
        ``tooltip.pointFormat`` as ``{point.formattedValue}``. Defaults to
        :obj:`None <python:None>`.

        If not set, the JavaScript ``{point.formattedValue}`` will use other options, in
        this order:

          #. :meth:`YAxis.labels.format <AxisLabelOptions.format>` if set
          #. If :meth:`YAxis.type` is ``'category'``, then category name will be
            displayed.
          #. If :meth:`YAxis.type` is ``'datetime'``, then the value will use the same
            format as :meth:`YAxis.labels`.
          #. If :meth:`YAxis.type` is ``'linear'`` or ``'logarithmic'``, then the simple
            value will be displayed.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`.
        """
        return self._tooltip_value_format

    @tooltip_value_format.setter
    def tooltip_value_format(self, value):
        self._tooltip_value_format = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'align_ticks': as_dict.pop('alignTicks', None),
            'allow_decimals': as_dict.pop('allowDecimals', None),
            'alternate_grid_color': as_dict.pop('alternateGridColor', None),
            'angle': as_dict.pop('angle', None),
            'breaks': as_dict.pop('breaks', None),
            'categories': as_dict.pop('categories', None),
            'ceiling': as_dict.pop('ceiling', None),
            'class_name': as_dict.pop('className', None),
            'date_time_label_formats': as_dict.pop('dateTimeLabelFormats', None),
            'end_on_tick': as_dict.pop('endOnTick', None),
            'events': as_dict.pop('events', None),
            'floor': as_dict.pop('floor', None),
            'grid_line_color': as_dict.pop('gridLineColor', None),
            'grid_line_dash_style': as_dict.pop('gridLineDashStyle', None),
            'grid_line_interpolation': as_dict.pop('gridLineInterpolation', None),
            'grid_line_width': as_dict.pop('gridLineWidth', None),
            'grid_z_index': as_dict.pop('gridZIndex', None),
            'id': as_dict.pop('id', None),
            'labels': as_dict.pop('labels', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'margin': as_dict.pop('margin', None),
            'max': as_dict.pop('max', None),
            'max_padding': as_dict.pop('maxPadding', None),
            'min': as_dict.pop('min', None),
            'minor_grid_line_color': as_dict.pop('minorGridLineColor', None),
            'minor_grid_line_dash_style': as_dict.pop('minorGridLineDashStyle', None),
            'minor_grid_line_width': as_dict.pop('minorGridLineWidth', None),
            'minor_tick_color': as_dict.pop('minorTickColor', None),
            'minor_tick_interval': as_dict.pop('minorTickInterval', None),
            'minor_tick_length': as_dict.pop('minorTickLength', None),
            'minor_tick_position': as_dict.pop('minorTickPosition', None),
            'minor_ticks': as_dict.pop('minorTicks', None),
            'minor_tick_width': as_dict.pop('minorTickWidth', None),
            'min_padding': as_dict.pop('minPadding', None),
            'min_range': as_dict.pop('minRange', None),
            'min_tick_interval': as_dict.pop('minTickInterval', None),
            'offset': as_dict.pop('offset', None),
            'opposite': as_dict.pop('opposite', None),
            'pane': as_dict.pop('pane', None),
            'panning_enabled': as_dict.pop('panningEnabled', None),
            'plot_bands': as_dict.pop('plotBands', None),
            'plot_lines': as_dict.pop('plotLines', None),
            'reversed': as_dict.pop('reversed', None),
            'reversed_stacks': as_dict.pop('reversedStacks', None),
            'show_first_label': as_dict.pop('showFirstLabel', None),
            'show_last_label': as_dict.pop('showLastLabel', None),
            'soft_max': as_dict.pop('softMax', None),
            'soft_min': as_dict.pop('softMin', None),
            'start_of_week': as_dict.pop('startOfWeek', None),
            'start_on_tick': as_dict.pop('startOnTick', None),
            'tick_amount': as_dict.pop('tickAmount', None),
            'tick_color': as_dict.pop('tickColor', None),
            'tick_interval': as_dict.pop('tickInterval', None),
            'tick_length': as_dict.pop('tickLength', None),
            'tickmark_placement': as_dict.pop('tickmarkPlacement', None),
            'tick_pixel_interval': as_dict.pop('tickPixelInterval', None),
            'tick_position': as_dict.pop('tickPosition', None),
            'tick_positioner': as_dict.pop('tickPositioner', None),
            'tick_positions': as_dict.pop('tickPositions', None),
            'tick_width': as_dict.pop('tickWidth', None),
            'title': as_dict.pop('title', None),
            'type': as_dict.pop('type', None),
            'unique_names': as_dict.pop('uniqueNames', None),
            'units': as_dict.pop('units', None),
            'visible': as_dict.pop('visible', None),
            'z_index': as_dict.pop('zIndex', None),
            'zoom_enabled': as_dict.pop('zoomEnabled', None),

            'crosshair': as_dict.pop('crosshair', None),
            'height': as_dict.pop('height', None),
            'left': as_dict.pop('left', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'show_empty': as_dict.pop('showEmpty', None),
            'top': as_dict.pop('top', None),
            'width': as_dict.pop('width', None),

            'max_color': as_dict.pop('maxColor', None),
            'min_color': as_dict.pop('minColor', None),
            'stack_labels': as_dict.pop('stackLabels', None),
            'stops': as_dict.pop('stops', None),
            'tooltip_value_format': as_dict.pop('tooltipValueFormat', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'maxColor': self.max_color,
            'minColor': self.min_color,
            'stackLabels': self.stack_labels,
            'stops': self.stops,
            'tooltipValueFormat': self.tooltip_value_format
        }

        parent_as_dict = super()._to_untrimmed_dict()
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
