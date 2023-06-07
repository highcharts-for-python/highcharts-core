from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.date_time_label_formats import DateTimeLabelFormats

from highcharts_core.options.axes.generic import GenericAxis
from highcharts_core.options.axes.breaks import AxisBreak
from highcharts_core.options.axes.plot_bands import PlotBand, PlotLine
from highcharts_core.options.axes.title import AxisTitle


class NumericAxis(GenericAxis):
    """Base class that is used for defining numeric axes."""

    def __init__(self, **kwargs):
        self._align_ticks = None
        self._allow_decimals = None
        self._alternate_grid_color = None
        self._breaks = None
        self._categories = None
        self._date_time_label_formats = None
        self._linked_to = None
        self._min_range = None
        self._min_tick_interval = None
        self._offset = None
        self._opposite = None
        self._pane = None
        self._plot_bands = None
        self._plot_lines = None
        self._reversed_stacks = None
        self._title = None
        self._zoom_enabled = None

        self.align_ticks = kwargs.get('align_ticks', None)
        self.allow_decimals = kwargs.get('allow_decimals', None)
        self.alternate_grid_color = kwargs.get('alternate_grid_color', None)
        self.breaks = kwargs.get('breaks', None)
        self.categories = kwargs.get('categories', None)
        self.date_time_label_formats = kwargs.get('date_time_label_formats', None)
        self.linked_to = kwargs.get('linked_to', None)
        self.min_range = kwargs.get('min_range', None)
        self.min_tick_interval = kwargs.get('min_tick_interval', None)
        self.offset = kwargs.get('offset', None)
        self.opposite = kwargs.get('opposite', None)
        self.pane = kwargs.get('pane', None)
        self.plot_bands = kwargs.get('plot_bands', None)
        self.plot_lines = kwargs.get('plot_lines', None)
        self.reversed_stacks = kwargs.get('reversed_stacks', None)
        self.title = kwargs.get('title', None)
        self.zoom_enabled = kwargs.get('zoom_enabled', None)

        super().__init__(**kwargs)

    @property
    def align_ticks(self) -> Optional[bool]:
        """If ``True`` and using multiple axes, the ticks of two or more opposite axes
        will automatically be aligned by adding ticks to the axis or axes with the least
        ticks, as if ``tick_amount`` were specified. This can be prevented by setting
        ``align_ticks`` to ``False``.

        Defaults to ``True``.

        .. hint::

          If the grid lines look messy, it's a good idea to hide them for the secondary
          axis by setting ``grid_line_width`` to ``0``.

        .. warning::

          If ``start_on_tick`` or ``end_on_tick`` in the axis options are set to
          ``False``, then tick alignment will be disabled for the axis.

        .. warning::

          Aways disabled for logarithmic axes.

        :returns: Flag indicating whether ot align ticks along the axes.
        :rtype: :class:`bool <python:bool>`  or :obj:`None <python:None>`
        """
        return self._align_ticks

    @align_ticks.setter
    def align_ticks(self, value):
        if value is None:
            self._align_ticks = None
        else:
            self._align_ticks = bool(value)

    @property
    def allow_decimals(self) -> Optional[bool]:
        """If ``True``, allow decimals in the axis' ticks. If :obj:`None <python:None>`,
        decimals are allowed on small scale axes. Defaults to :obj:`None <python:None>`.

        .. hint::

          When counting integers, like persons or hits on a web page, decimals should be
          avoided in the labels.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_decimals

    @allow_decimals.setter
    def allow_decimals(self, value):
        if value is None:
            self._allow_decimals = None
        else:
            self._allow_decimals = bool(value)

    @property
    def alternate_grid_color(self) -> Optional[str | Gradient | Pattern]:
        """When using an alternate grid color, a band is painted across the plot area
        between every other grid line. This setting determines the color of that band.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._alternate_grid_color

    @alternate_grid_color.setter
    def alternate_grid_color(self, value):
        from highcharts_core import utility_functions
        self._alternate_grid_color = utility_functions.validate_color(value)

    @property
    def breaks(self) -> Optional[List[AxisBreak]]:
        """A collection that defines breaks to render in the axis. Defaults to
        :obj:`None <python:None>`.

        .. note::

          The sections defined as breaks will be left out and all the points shifted
          closer to each other.

        :rtype: :class:`list <python:list>` of :class:`AxisBreak`, or
          :obj:`None <python:None>`
        """
        return self._breaks

    @breaks.setter
    @class_sensitive(AxisBreak, force_iterable = True)
    def breaks(self, value):
        self._breaks = value

    @property
    def categories(self) -> Optional[List[str]]:
        """If categories are present for the x-axis, displays category names along the
        x-axis instead of numerical values. Defaults to :obj:`None <python:None>`.

        .. hint::

          While categories can also be defined by giving each data point a name and
          setting axis type to ``'category'``, if you have multiple series, best practice
          remains using the :meth:`categories <NumericAxis.categories>` setting for ease
          of maintenance.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._categories

    @categories.setter
    def categories(self, value):
        if not value:
            self._categories = None
        else:
            self._categories = [validators.string(x, allow_empty = True) or '' for x in validators.iterable(value)]

    @property
    def date_time_label_formats(self) -> Optional[DateTimeLabelFormats]:
        """For a datetime axis, the scale will automatically adjust to the appropriate
        unit. This setting gives the default string representations used for each unit.
        Defaults to :obj:`None <python:None>`.

        .. note::

          For intermediate values, different units may be used, for example the day unit
          can be used on midnight and hour unit  used for intermediate values on the same
          axis.

        .. seealso::

          * :class:`DateTimeLabelFormats`

        :rtype: :class:`DateTimeLabelFormats` or :obj:`None <python:None>`
        """
        return self._date_time_label_formats

    @date_time_label_formats.setter
    @class_sensitive(DateTimeLabelFormats)
    def date_time_label_formats(self, value):
        self._date_time_label_formats = value

    @property
    def linked_to(self) -> Optional[int]:
        """The index of another axis that this axis is linked to.

        When an axis is linked to a master axis, it will take the same extremes as the
        master as assigned by :meth:`NumericAxis.min` or :meth:`NumericAxis.max` or by the
        (JavaScript) ``setExtremes()`` method. It can be used to show additional info, or
        to ease reading the chart by duplicating the scales.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._linked_to

    @linked_to.setter
    def linked_to(self, value):
        self._linked_to = validators.integer(value,
                                             allow_empty = True,
                                             minimum = 0)

    @property
    def min_range(self) -> Optional[int | float | Decimal]:
        """The minimum range to display on this axis. The entire axis will not be allowed
        to span over a smaller interval than this, particularly when zooming. Defaults to
        :obj:`None <python:None>`.

        For example, for a datetime axis the main unit is milliseconds. If ``min_range``
        is set to ``3600000``, the user won't be able to zoom in more than to one hour.

        If :obj:`None <pythoN:None>`, the ``min_range`` for the x-axis will automatically
        be set to five times the smallest interval between any of the data points.

        On a logarithmic axis, the unit for the minimum range is the power. So a
        ``min_range`` of ``1`` means that the axis can be zoomed to 10-100, 100-1000,
        1000-10,000 etc.

        .. warning::

          The following settings also impact how the extremes of the axis are computed:

            * :meth:`NumericAxis.min_padding`
            * :meth:`NumericAxis.max_padding`
            * :meth:`NumericAxis.start_on_tick`
            * :meth:`NumericAxis.end_on_tick`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_range

    @min_range.setter
    def min_range(self, value):
        self._min_range = validators.numeric(value, allow_empty = True)

    @property
    def min_tick_interval(self) -> Optional[int | float | Decimal]:
        """The minimum tick interval allowed in axis values. Defaults to
        :obj:`None <python:None>`, which applies the closest distance between two points
        on the axis.

        For example, this setting can be used to prevent the axis from showing hours as
        minor tick marks.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_tick_interval

    @min_tick_interval.setter
    def min_tick_interval(self, value):
        self._min_tick_interval = validators.numeric(value, allow_empty = True)

    @property
    def offset(self) -> Optional[int | float | Decimal]:
        """The distance in pixels from the plot area to the axis line. Defaults to
        :obj:`None <python:None>`.

        A positive offset moves the axis (along with its line, labels, and ticks) away
        from the plot area. This is typically used when two or more axes are displayed on
        the same side of the plot.

        With multiple axes, the ``offset`` is dynamically adjusted to avoid collision,
        though this can be overridden by setting ``offset`` explicitly.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = validators.numeric(value, allow_empty = True)

    @property
    def opposite(self) -> Optional[bool]:
        """If ``True``, displays the axis on the opposite side of where it would normally
        appear. Defaults to ``False``.

        Vertical axes would normally appear on the left side of the chart, while
        horizontal axes would normally appear on the bottom of the chart. Thus, the
        opposite side would be the right and top respectively.

        .. hint::

          This feature is typically used with dual or multiple axes.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._opposite

    @opposite.setter
    def opposite(self, value):
        if value is None:
            self._opposite = None
        else:
            self._opposite = bool(value)

    @property
    def pane(self) -> Optional[int]:
        """Indicates the index in the panes array. When :obj:`None <python:None>`, the
        first pane will be used. Defaults to :obj:`None <python:None>`.

        .. warning::

          Used for circular gauges and polar charts.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._pane

    @pane.setter
    def pane(self, value):
        self._pane = validators.integer(value,
                                        allow_empty = True,
                                        minimum = 0)

    @property
    def plot_bands(self) -> Optional[List[PlotBand]]:
        """A collection of colored bands stretching across the plot area which can be used
        to visually mark an interval along the axis. Defaults to
        :obj:`None <python:None>`.

        .. note::

          In a :term:`gauge chart`, a plot band on the :class:`YAxis` (value axis) will
          stretch along the perimeter of the gauge.

        :rtype: :class:`list <python:list>` of :class:`PlotBand` instances, or
          :obj:`None <python:None>`
        """
        return self._plot_bands

    @plot_bands.setter
    @class_sensitive(PlotBand, force_iterable = True)
    def plot_bands(self, value):
        self._plot_bands = value

    @property
    def plot_lines(self) -> Optional[List[PlotLine]]:
        """A collection of lines stretching across the plot area which can be used
        to visually mark specific values on the axis. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`PlotLine` instances, or
          :obj:`None <python:None>`
        """
        return self._plot_lines

    @plot_lines.setter
    @class_sensitive(PlotLine, force_iterable = True)
    def plot_lines(self, value):
        self._plot_lines = value

    @property
    def reversed_stacks(self) -> Optional[bool]:
        """This option determines how stacks should be ordered within a group. Setting
        this to ``True`` will reverse the order of series within a group relative to
        its automatic ordering.

        For example, if :class:`XAxis.reversed`` is ``True``, then the default behavior is
        to reverse the order of the series so that the first series comes last in a group.
        To retain the original order, set this option to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._reversed_stacks

    @reversed_stacks.setter
    def reversed_stacks(self, value):
        if value is None:
            self._reversed_stacks = None
        else:
            self._reversed_stacks = bool(value)

    @property
    def title(self) -> Optional[AxisTitle]:
        """The axis title, displayed next to the axis line. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`AxisTitle` or :obj:`None <python:None>`
        """
        return self._title

    @title.setter
    @class_sensitive(AxisTitle)
    def title(self, value):
        self._title = value

    @property
    def zoom_enabled(self) -> Optional[bool]:
        """If ``True``, the axis supports zooming in to view more granular sub-sections
        of the data. If ``False``, the axis will not zoom. Defaults to ``True``.

        .. hint::

          If :meth:`Chart.zoom_type` is set, setting this value to ``False`` can override
          the ability to zoom in on this specific axis.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._zoom_enabled

    @zoom_enabled.setter
    def zoom_enabled(self, value):
        if value is None:
            self._zoom_enabled = None
        else:
            self._zoom_enabled = bool(value)

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
            'crossing': as_dict.get('crossing', None),
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
            'zoom_enabled': as_dict.get('zoomEnabled', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'alignTicks': self.align_ticks,
            'allowDecimals': self.allow_decimals,
            'alternateGridColor': self.alternate_grid_color,
            'angle': self.angle,
            'breaks': self.breaks,
            'categories': self.categories,
            'ceiling': self.ceiling,
            'className': self.class_name,
            'crossing': self.crossing,
            'dateTimeLabelFormats': self.date_time_label_formats,
            'endOnTick': self.end_on_tick,
            'events': self.events,
            'floor': self.floor,
            'gridLineColor': self.grid_line_color,
            'gridLineDashStyle': self.grid_line_dash_style,
            'gridLineInterpolation': self.grid_line_interpolation,
            'gridLineWidth': self.grid_line_width,
            'gridZIndex': self.grid_z_index,
            'id': self.id,
            'labels': self.labels,
            'linkedTo': self.linked_to,
            'margin': self.margin,
            'max': self.max,
            'maxPadding': self.max_padding,
            'min': self.min,
            'minorGridLineColor': self.minor_grid_line_color,
            'minorGridLineDashStyle': self.minor_grid_line_dash_style,
            'minorGridLineWidth': self.minor_grid_line_width,
            'minorTickColor': self.minor_tick_color,
            'minorTickInterval': self.minor_tick_interval,
            'minorTickLength': self.minor_tick_length,
            'minorTickPosition': self.minor_tick_position,
            'minorTicks': self.minor_ticks,
            'minorTickWidth': self.minor_tick_width,
            'minPadding': self.min_padding,
            'minRange': self.min_range,
            'minTickInterval': self.min_tick_interval,
            'offset': self.offset,
            'opposite': self.opposite,
            'pane': self.pane,
            'panningEnabled': self.panning_enabled,
            'plotBands': self.plot_bands,
            'plotLines': self.plot_lines,
            'reversed': self.reversed,
            'reversedStacks': self.reversed_stacks,
            'showFirstLabel': self.show_first_label,
            'showLastLabel': self.show_last_label,
            'softMax': self.soft_max,
            'softMin': self.soft_min,
            'startOfWeek': self.start_of_week,
            'startOnTick': self.start_on_tick,
            'tickAmount': self.tick_amount,
            'tickColor': self.tick_color,
            'tickInterval': self.tick_interval,
            'tickLength': self.tick_length,
            'tickmarkPlacement': self.tickmark_placement,
            'tickPixelInterval': self.tick_pixel_interval,
            'tickPosition': self.tick_position,
            'tickPositioner': self.tick_positioner,
            'tickPositions': self.tick_positions,
            'tickWidth': self.tick_width,
            'title': self.title,
            'type': self.type,
            'uniqueNames': self.unique_names,
            'units': self.units,
            'visible': self.visible,
            'zIndex': self.z_index,
            'zoomEnabled': self.zoom_enabled,
        }

        return untrimmed
