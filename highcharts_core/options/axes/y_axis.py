from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.data_labels import DataLabel

from highcharts_core.options.axes.x_axis import XAxis


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

        self.max_color = kwargs.get('max_color', None)
        self.min_color = kwargs.get('min_color', None)
        self.stack_labels = kwargs.get('stack_labels', None)
        self.stops = kwargs.get('stops', None)
        self.tooltip_value_format = kwargs.get('tooltip_value_format', None)

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
        from highcharts_core import utility_functions
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
        from highcharts_core import utility_functions
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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'align_ticks': as_dict.get('alignTicks', None),
            'allow_decimals': as_dict.get('allowDecimals', None),
            'alternate_grid_color': as_dict.get('alternateGridColor', None),
            'angle': as_dict.get('angle', None),
            'breaks': as_dict.get('breaks', None),
            'categories': as_dict.get('categories', None),
            'ceiling': as_dict.get('ceiling', None),
            'class_name': as_dict.get('className', None),
            'date_time_label_formats': as_dict.get('dateTimeLabelFormats', None),
            'end_on_tick': as_dict.get('endOnTick', None),
            'events': as_dict.get('events', None),
            'floor': as_dict.get('floor', None),
            'grid_line_color': as_dict.get('gridLineColor', None),
            'grid_line_dash_style': as_dict.get('gridLineDashStyle', None),
            'grid_line_interpolation': as_dict.get('gridLineInterpolation', None),
            'grid_line_width': as_dict.get('gridLineWidth', None),
            'grid_z_index': as_dict.get('gridZIndex', None),
            'id': as_dict.get('id', None),
            'labels': as_dict.get('labels', None),
            'linked_to': as_dict.get('linkedTo', None),
            'margin': as_dict.get('margin', None),
            'max': as_dict.get('max', None),
            'max_padding': as_dict.get('maxPadding', None),
            'min': as_dict.get('min', None),
            'minor_grid_line_color': as_dict.get('minorGridLineColor', None),
            'minor_grid_line_dash_style': as_dict.get('minorGridLineDashStyle', None),
            'minor_grid_line_width': as_dict.get('minorGridLineWidth', None),
            'minor_tick_color': as_dict.get('minorTickColor', None),
            'minor_tick_interval': as_dict.get('minorTickInterval', None),
            'minor_tick_length': as_dict.get('minorTickLength', None),
            'minor_tick_position': as_dict.get('minorTickPosition', None),
            'minor_ticks': as_dict.get('minorTicks', None),
            'minor_tick_width': as_dict.get('minorTickWidth', None),
            'min_padding': as_dict.get('minPadding', None),
            'min_range': as_dict.get('minRange', None),
            'min_tick_interval': as_dict.get('minTickInterval', None),
            'offset': as_dict.get('offset', None),
            'opposite': as_dict.get('opposite', None),
            'pane': as_dict.get('pane', None),
            'panning_enabled': as_dict.get('panningEnabled', None),
            'plot_bands': as_dict.get('plotBands', None),
            'plot_lines': as_dict.get('plotLines', None),
            'reversed': as_dict.get('reversed', None),
            'reversed_stacks': as_dict.get('reversedStacks', None),
            'show_first_label': as_dict.get('showFirstLabel', None),
            'show_last_label': as_dict.get('showLastLabel', None),
            'soft_max': as_dict.get('softMax', None),
            'soft_min': as_dict.get('softMin', None),
            'start_of_week': as_dict.get('startOfWeek', None),
            'start_on_tick': as_dict.get('startOnTick', None),
            'tick_amount': as_dict.get('tickAmount', None),
            'tick_color': as_dict.get('tickColor', None),
            'tick_interval': as_dict.get('tickInterval', None),
            'tick_length': as_dict.get('tickLength', None),
            'tickmark_placement': as_dict.get('tickmarkPlacement', None),
            'tick_pixel_interval': as_dict.get('tickPixelInterval', None),
            'tick_position': as_dict.get('tickPosition', None),
            'tick_positioner': as_dict.get('tickPositioner', None),
            'tick_positions': as_dict.get('tickPositions', None),
            'tick_width': as_dict.get('tickWidth', None),
            'title': as_dict.get('title', None),
            'type': as_dict.get('type', None),
            'unique_names': as_dict.get('uniqueNames', None),
            'units': as_dict.get('units', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),
            'zoom_enabled': as_dict.get('zoomEnabled', None),

            'crosshair': as_dict.get('crosshair', None),
            'height': as_dict.get('height', None),
            'left': as_dict.get('left', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'show_empty': as_dict.get('showEmpty', None),
            'top': as_dict.get('top', None),
            'width': as_dict.get('width', None),

            'max_color': as_dict.get('maxColor', None),
            'min_color': as_dict.get('minColor', None),
            'stack_labels': as_dict.get('stackLabels', None),
            'stops': as_dict.get('stops', None),
            'tooltip_value_format': as_dict.get('tooltipValueFormat', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'maxColor': self.max_color,
            'minColor': self.min_color,
            'stackLabels': self.stack_labels,
            'stops': self.stops,
            'tooltipValueFormat': self.tooltip_value_format
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
