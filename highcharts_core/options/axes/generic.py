from typing import Optional, List
from decimal import Decimal
import datetime

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.events import AxisEvents
from highcharts_core.utility_classes.javascript_functions import CallbackFunction

from highcharts_core.options.axes.accessibility import AxisAccessibility
from highcharts_core.options.axes.labels import AxisLabelOptions

NoneType = type(None)


class GenericAxis(HighchartsMeta):
    """Base class that is used for defining axis classes."""

    def __init__(self, **kwargs):
        self._accessibility = None
        self._angle = None
        self._ceiling = None
        self._class_name = None
        self._crossing = None
        self._end_on_tick = None
        self._events = None
        self._floor = None
        self._grid_line_color = None
        self._grid_line_dash_style = None
        self._grid_line_interpolation = None
        self._grid_line_width = None
        self._grid_z_index = None
        self._id = None
        self._labels = None
        self._margin = None
        self._max = None
        self._max_padding = None
        self._min = None
        self._minor_grid_line_color = None
        self._minor_grid_line_dash_style = None
        self._minor_grid_line_width = None
        self._minor_tick_color = None
        self._minor_tick_interval = None
        self._minor_tick_length = None
        self._minor_tick_position = None
        self._minor_ticks = None
        self._minor_tick_width = None
        self._min_padding = None
        self._panning_enabled = None
        self._reversed = None
        self._show_first_label = None
        self._show_last_label = None
        self._soft_max = None
        self._soft_min = None
        self._start_of_week = None
        self._start_on_tick = None
        self._tick_amount = None
        self._tick_color = None
        self._tick_interval = None
        self._tick_length = None
        self._tickmark_placement = None
        self._tick_pixel_interval = None
        self._tick_position = None
        self._tick_positioner = None
        self._tick_positions = None
        self._tick_width = None
        self._type = None
        self._unique_names = None
        self._units = None
        self._visible = None
        self._z_index = None

        self.accessibility = kwargs.get('accessibility', None)
        self.angle = kwargs.get('angle', None)
        self.ceiling = kwargs.get('ceiling', None)
        self.class_name = kwargs.get('class_name', None)
        self.crossing = kwargs.get('crossing', None)
        self.end_on_tick = kwargs.get('end_on_tick', None)
        self.events = kwargs.get('events', None)
        self.floor = kwargs.get('floor', None)
        self.grid_line_color = kwargs.get('grid_line_color', None)
        self.grid_line_dash_style = kwargs.get('grid_line_dash_style', None)
        self.grid_line_interpolation = kwargs.get('grid_line_interpolation', None)
        self.grid_line_width = kwargs.get('grid_line_width', None)
        self.grid_z_index = kwargs.get('grid_z_index', None)
        self.id = kwargs.get('id', None)
        self.labels = kwargs.get('labels', None)
        self.margin = kwargs.get('margin', None)
        self.max = kwargs.get('max', None)
        self.max_padding = kwargs.get('max_padding', None)
        self.min = kwargs.get('min', None)
        self.minor_grid_line_color = kwargs.get('minor_grid_line_color', None)
        self.minor_grid_line_dash_style = kwargs.get('minor_grid_line_dash_style', None)
        self.minor_grid_line_width = kwargs.get('minor_grid_line_width', None)
        self.minor_tick_color = kwargs.get('minor_tick_color', None)
        self.minor_tick_interval = kwargs.get('minor_tick_interval', None)
        self.minor_tick_length = kwargs.get('minor_tick_length', None)
        self.minor_tick_position = kwargs.get('minor_tick_position', None)
        self.minor_ticks = kwargs.get('minor_ticks', None)
        self.minor_tick_width = kwargs.get('minor_tick_width', None)
        self.min_padding = kwargs.get('min_padding', None)
        self.panning_enabled = kwargs.get('panning_enabled', None)
        self.reversed = kwargs.get('reversed', None)
        self.show_first_label = kwargs.get('show_first_label', None)
        self.show_last_label = kwargs.get('show_last_label', None)
        self.soft_max = kwargs.get('soft_max', None)
        self.soft_min = kwargs.get('soft_min', None)
        self.start_of_week = kwargs.get('start_of_week', None)
        self.start_on_tick = kwargs.get('start_on_tick', None)
        self.tick_amount = kwargs.get('tick_amount', None)
        self.tick_color = kwargs.get('tick_color', None)
        self.tick_interval = kwargs.get('tick_interval', None)
        self.tick_length = kwargs.get('tick_length', None)
        self.tickmark_placement = kwargs.get('tickmark_placement', None)
        self.tick_pixel_interval = kwargs.get('tick_pixel_interval', None)
        self.tick_position = kwargs.get('tick_position', None)
        self.tick_positioner = kwargs.get('tick_positioner', None)
        self.tick_positions = kwargs.get('tick_positions', None)
        self.tick_width = kwargs.get('tick_width', None)
        self.type = kwargs.get('type', None)
        self.unique_names = kwargs.get('unique_names', None)
        self.units = kwargs.get('units', None)
        self.visible = kwargs.get('visible', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def accessibility(self) -> Optional[AxisAccessibility]:
        """Accessibility options for an axis object.

        :rtype: :class:`AxisAccessibility` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(AxisAccessibility)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def angle(self) -> Optional[int | float | Decimal]:
        """In a polar chart, this is the angle of the Y axis in degrees, where ``0`` is
        up and ``90`` is right.  Defaults to ``0``.

        .. note::

          The angle determines the position of the axis line and the labels, though the
          coordinate system is unaffected.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = validators.numeric(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def ceiling(self) -> Optional[int | float | Decimal]:
        """The highest allowed value for automatically computed axis extremes. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._ceiling

    @ceiling.setter
    def ceiling(self, value):
        self._ceiling = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A class name that can then be used for styling the axis using CSS. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          The the ``class_name`` is applied to group elements for the grid, axis elements,
          and labels.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def crossing(self) -> Optional[int | float | Decimal]:
        """The value on a perpendicular axis where this axis should cross. Defaults to :obj:`None <python:None>`.

        .. tip::

          This\ris typically used on mathematical plots where the axes cross at ``0``.
          
        .. warning::
        
          When ``.crossing`` is set, space will *not* be reserved at the sides of the chart for 
          axis labels and title, so those may be clipped. In this case, it is better to place the
          axes without the ``.crossing`` option.
        
        :rtype: numeric
        """
        return self._crossing
    
    @crossing.setter
    def crossing(self, value):
        self._crossing = validators.numeric(value, allow_empty = True)

    @property
    def end_on_tick(self) -> Optional[bool]:
        """If ``True`` forces the axis to end on a tick. Defaults to ``False`` for
        :class:`XAxis`, ``True`` for :class:`YAxis`, and ``False`` for :class:`ZAxis`.

        .. hint::

          Use this option with the :meth:`GenericAxis.max_padding` setting to control the
          axis end.

        .. warning::

          This option is always disabled on a :class:`YAxis`, when panning type is either
          ``y`` or ``xy``.

        :rtype: :class:`bool <python:bool>`  or :obj:`None <python:None>`
        """
        return self._end_on_tick

    @end_on_tick.setter
    def end_on_tick(self, value):
        if value is None:
            self._end_on_tick = None
        else:
            self._end_on_tick = bool(value)

    @property
    def events(self) -> Optional[AxisEvents]:
        """Event handlers for the axis.

        :rtype: :class:`SeriesEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(AxisEvents)
    def events(self, value):
        self._events = value

    @property
    def floor(self) -> Optional[int | float | Decimal]:
        """The lowest allowed value for automatically computed axis extremes. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = validators.numeric(value, allow_empty = True)

    @property
    def grid_line_color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the grid lines extending the ticks across the plot area.
        Defaults to ``'#e6e6e6'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._grid_line_color

    @grid_line_color.setter
    def grid_line_color(self, value):
        from highcharts_core import utility_functions
        self._grid_line_color = utility_functions.validate_color(value)

    @property
    def grid_line_dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the grid lines. Defaults to ``Solid``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._grid_line_dash_style

    @grid_line_dash_style.setter
    def grid_line_dash_style(self, value):
        if not value:
            self._grid_line_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'grid_line_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._grid_line_dash_style = value

    @property
    def grid_line_interpolation(self) -> Optional[str]:
        """Whether the grid lines should draw as a polygon with straight lines between
        categories, or as circles. Defaults to :obj:`None <python:None>`.

        Acceptable values are:

          * ``'circle'``
          * ``'polygon'``

        .. warning::

          Only applies to :term:`polar charts <Polar Chart>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._grid_line_interpolation

    @grid_line_interpolation.setter
    def grid_line_interpolation(self, value):
        if not value:
            self._grid_line_interpolation = None
        else:
            value = validators.string(value)
            if value not in ['circle', 'polygon']:
                raise errors.HighchartsValueError(f'grid_line_interpolation expects '
                                                  f'"circle" or "polygon". Received: '
                                                  f'{value}')

            self._grid_line_interpolation = value

    @property
    def grid_line_width(self) -> Optional[int | float | Decimal]:
        """The width of the grid lines extending the ticks across the plot area. Defaults
        to ``0`` for :class:`XAxis`, ``1`` for :class:`YAxis`, and
        :obj:`None <python:None>` for :class:`ZAxis`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._grid_line_width

    @grid_line_width.setter
    def grid_line_width(self, value):
        self._grid_line_width = validators.numeric(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def grid_z_index(self) -> Optional[int | float | Decimal]:
        """The Z-index of the grid lines. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._grid_z_index

    @grid_z_index.setter
    def grid_z_index(self, value):
        self._grid_z_index = validators.numeric(value, allow_empty = True)

    @property
    def id(self) -> Optional[str]:
        """An id assigned to the axis. Defaults to :obj:`None <python:None>`.

        .. hint::

          This can be used after rendering to get a pointer to the axis object through the
          (JavaScript) ``chart.get()`` method.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def labels(self) -> Optional[AxisLabelOptions]:
        """Configuration settings for the axis labels, which show the number or category
        for each tick. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`AxisLabeLOptions` or :obj:`None <python:None>`
        """
        return self._labels

    @labels.setter
    @class_sensitive(AxisLabelOptions)
    def labels(self, value):
        self._labels = value

    @property
    def margin(self) -> Optional[int | float | Decimal]:
        """If there are multiple axes on the same side of the chart, the margin between
        the axes, expressed in pixels. Defaults to ``0`` for vertical axes, ``15`` for
        horizontal axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = validators.numeric(value, allow_empty = True)

    @property
    def max(self) -> Optional[int | float | Decimal | datetime.date | datetime.datetime]:
        """The maximum value of the axis. If :obj:`None <python:None>`, the ``max`` value
        is automatically calculated. Defaults to :obj:`None <python:None>`.

        .. note::

          If the :meth:`GenericAxis.end_on_tick` is ``True``, the ``max`` value might be
          rounded up.

        .. warning::

          If a :meth:`GenericAxis.tick_amount` is set, the axis may be extended beyond the
          set ``max`` in order to reach the given number of ticks. The same may happen in
          a chart with multiple axes, determined by
          :meth:`Chart.align_ticks` where a ``tick_amount`` is applied internally.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max

    @max.setter
    def max(self, value):
        if value is None:
            self._max = None
        elif checkers.is_date(value):
            self._max = validators.date(value)
        elif checkers.is_datetime(value):
            self._max = validators.datetime(value)
        else:
            self._max = validators.numeric(value, allow_empty = True)

    @property
    def max_padding(self) -> Optional[int | float | Decimal]:
        """Padding of the max value relative to the length of the axis. Defaults to
        ``0.01``.

        For example, a value of ``0.05`` will make a 100px axis 5px longer.

        .. hint::

          This is useful when you don't want the highest data value to appear on the edge
          of the plot area.

        .. warning::

          When the :meth:`GenericAxis.max` option is set or a max extreme is set using
          (JavaScript) ``axis.setExtremes()``, the ``max_padding`` will be ignored.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_padding

    @max_padding.setter
    def max_padding(self, value):
        self._max_padding = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def min(self) -> Optional[int | float | Decimal | datetime.date | datetime.datetime]:
        """The minimum value of the axis. If :obj:`None <python:None>`, the ``min`` value
        is automatically calculated. Defaults to :obj:`None <python:None>`.

        .. note::

          If the :meth:`GenericAxis.start_on_tick` is ``True``, the ``min`` value might be
          rounded down.

        .. warning::

          The automatically-calculated ``min`` value is also affected by:

            * :meth:`GenericAxis.floor`
            * :meth:`GenericAxis.soft_min`
            * :meth:`GenericAxis.min_padding`
            * :meth:`GenericAxis.min_range`
            * :meth:`GenericTypeOptions.threshold`
            * :meth:`SeriesOptions.soft_threshold`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min

    @min.setter
    def min(self, value):
        if value is None:
            self._min = None
        elif checkers.is_date(value):
            self._min = validators.date(value)
        elif checkers.is_datetime(value):
            self._min = validators.datetime(value)
        else:
            self._min = validators.numeric(value, allow_empty = True)

    @property
    def minor_grid_line_color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the minor (secondary) grid lines. Defaults to ``'#f2f2f2'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._minor_grid_line_color

    @minor_grid_line_color.setter
    def minor_grid_line_color(self, value):
        from highcharts_core import utility_functions
        self._minor_grid_line_color = utility_functions.validate_color(value)

    @property
    def minor_grid_line_dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the grid lines. Defaults to ``Solid``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._minor_grid_line_dash_style

    @minor_grid_line_dash_style.setter
    def minor_grid_line_dash_style(self, value):
        if not value:
            self._minor_grid_line_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'minor_grid_line_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._minor_grid_line_dash_style = value

    @property
    def minor_grid_line_width(self) -> Optional[int | float | Decimal]:
        """Width of the minor, secondary grid lines. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._minor_grid_line_width

    @minor_grid_line_width.setter
    def minor_grid_line_width(self, value):
        self._minor_grid_line_width = validators.numeric(value,
                                                         allow_empty = True,
                                                         minimum = 0)

    @property
    def minor_tick_color(self) -> Optional[str | Gradient | Pattern]:
        """Color for the minor tick marks. Defaults to ``'#999999'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._minor_tick_color

    @minor_tick_color.setter
    def minor_tick_color(self, value):
        from highcharts_core import utility_functions
        self._minor_tick_color = utility_functions.validate_color(value)

    @property
    def minor_tick_interval(self) -> Optional[str | int | float | Decimal]:
        """Specific tick interval in axis units for the minor ticks. Defaults to
        :obj:`None <python:None>`.

        On a linear axis, if ``"auto"``, the minor tick interval is calculated as a fifth
        of the :meth:`GenericAxis.tick_interval`. If :obj:`None <python:None>`, minor ticks
        are not shown.

        On logarithmic axes, the unit is the power of the value. For example, setting the
        ``minor_tick_interval`` to ``1`` puts one tick on each of 0.1, 1, 10, 100, etc.
        Setting the value to ``0.1`` produces 9 ticks between 1 and 10, 10 and 100 etc.

        .. warning:

          If user settings dictate minor ticks to become too dense, Highcharts will ignore
          the settings to prevent performance problems.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._minor_tick_interval

    @minor_tick_interval.setter
    def minor_tick_interval(self, value):
        if not value:
            self._minor_tick_interval = None
        else:
            if isinstance(value, str):
                value = validators.string(value)
                value = value.lower()
                if value != 'auto':
                    raise errors.HighchartsValueError(f'minor_tick_interval only accepts'
                                                      f' a string value of "auto". '
                                                      f'Received a string value of: '
                                                      f'{value}')
            else:
                value = validators.numeric(value)

            self._minor_tick_interval = value

    @property
    def minor_tick_length(self) -> Optional[int | float | Decimal]:
        """The length of the minor tick marks, in pixels. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._minor_tick_length

    @minor_tick_length.setter
    def minor_tick_length(self, value):
        self._minor_tick_length = validators.numeric(value, allow_empty = True)

    @property
    def minor_tick_position(self) -> Optional[str]:
        """The position of the minor tick marks relative to the axis line. Defaults to
        ``'outside'``.

        Accepts either:

          * ``'outside'``
          * ``'inside'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._minor_tick_position

    @minor_tick_position.setter
    def minor_tick_position(self, value):
        if not value:
            self._minor_tick_position = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['inside', 'outside']:
                raise errors.HighchartsValueError(f'minor_tick_position expects either '
                                                  f'"inside" or "outside". Received: '
                                                  f'{value}')

            self._minor_tick_position = value

    @property
    def minor_ticks(self) -> Optional[bool]:
        """Enable (``True``) or disable (``False``) minor ticks. Defaults to ``False``.

        .. note::

          Unless :meth:`GenericAxis.minor_tick_interval` is set, the minor tick interval is
          calculated as a fifth of the tickInterval.

        .. note::

          On a logarithmic axis, minor ticks are laid out based on a best guess,
          attempting to fit approximately 5 minor ticks between each major tick.

        .. warning::

          On category axes (where text is displayed in each position, rather than a
          numerical value), minor ticks are not supported.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._minor_ticks

    @minor_ticks.setter
    def minor_ticks(self, value):
        if value is None:
            self._minor_ticks = None
        else:
            self._minor_ticks = bool(value)

    @property
    def minor_tick_width(self) -> Optional[int | float | Decimal]:
        """The width of the minor tick marks, in pixels. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._minor_tick_width

    @minor_tick_width.setter
    def minor_tick_width(self, value):
        self._minor_tick_width = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def min_padding(self) -> Optional[int | float | Decimal]:
        """Padding of the min value relative to the length of the axis. Defaults to
        ``0.01``.

        For example, a value of ``0.05`` will make a 100px axis 5px longer.

        .. hint::

          This is useful when you don't want the lowest data value to appear on the edge
          of the plot area.

        .. warning::

          When the :meth:`GenericAxis.min` option is set or a min extreme is set using
          (JavaScript) ``axis.setExtremes()``, the ``min_padding`` will be ignored.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_padding

    @min_padding.setter
    def min_padding(self, value):
        self._min_padding = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def panning_enabled(self) -> Optional[bool]:
        """If ``True``, allows the axis to pan. ``False`` prevents the axis from panning.
        Defaults to ``True``.

        .. note::

          If :meth:`Chart.panning` is ``True`` and this option is ``False``, then this
          specific axis will not pan.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._panning_enabled

    @panning_enabled.setter
    def panning_enabled(self, value):
        if value is None:
            self._panning_enabled = None
        else:
            self._panning_enabled = bool(value)

    @property
    def reversed(self) -> Optional[bool]:
        """If ``True``, reverses the axis so that the highest number is closest to the
        origin. Defaults to :obj:`None <python:None>`.

        .. note::

          If the chart is inverted, the :class:`XAxis` is reversed by default.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._reversed

    @reversed.setter
    def reversed(self, value):
        if value is None:
            self._reversed = None
        else:
            self._reversed = bool(value)

    @property
    def show_first_label(self) -> Optional[bool]:
        """If ``True``, renders the first tick label by the axis. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_first_label

    @show_first_label.setter
    def show_first_label(self, value):
        if value is None:
            self._show_first_label = None
        else:
            self._show_first_label = bool(value)

    @property
    def show_last_label(self) -> Optional[bool]:
        """If ``True``, renders the last tick label by the axis. If
        :obj:`None <python:None>`, defaults to ``True`` on
        :term:`cartesian charts` and ``False`` on
        :term:`polar charts <Polar Chart>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_last_label

    @show_last_label.setter
    def show_last_label(self, value):
        if value is None:
            self._show_last_label = None
        else:
            self._show_last_label = bool(value)

    @property
    def soft_max(self) -> Optional[int | float | Decimal]:
        """A soft maximum for the axis. Defaults to :obj:`None <python:None>`.

        If the series data maximum is less than this, the axis will stay at this maximum,
        but if the series data maximum is higher than this value, the axis will flex to
        show all data.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._soft_max

    @soft_max.setter
    def soft_max(self, value):
        self._soft_max = validators.numeric(value, allow_empty = True)

    @property
    def soft_min(self) -> Optional[int | float | Decimal]:
        """A soft minimum for the axis. Defaults to :obj:`None <python:None>`.

        If the series data minimum is less than this, the axis will stay at this minimum,
        but if the series data minimum is higher than this value, the axis will flex to
        show all data.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._soft_min

    @soft_min.setter
    def soft_min(self, value):
        self._soft_min = validators.numeric(value, allow_empty = True)

    @property
    def start_of_week(self) -> Optional[int]:
        """For datetime axes, this decides where to put the tick between weeks. Defaults
        to ``1`` (Monday).

        .. note::

          ``0`` = Sunday, ``1`` = Monday, etc.

        .. hint::

          As a convenience, if you supply a string with the day of week (e.g.
          ``'Monday'``), the Highcharts for Python library wlil automatically convert it
          to the appropriate numerical value.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._start_of_week

    @start_of_week.setter
    def start_of_week(self, value):
        if value is None:
            self._start_of_week = None
        else:
            if isinstance(value, str):
                value = value.lower()
                if value not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
                                 'friday', 'saturday']:
                    raise errors.HighchartsValueError(f'start_of_week expects an integer '
                                                      f'in the range 0 - 6, or a day '
                                                      f'of the week. Received: {value}')
                value = constants.DAYS_OF_WEEK.get(value)
            else:
                value = validators.integer(value, minimum = 0, maximum = 6)

            self._start_of_week = value

    @property
    def start_on_tick(self) -> Optional[bool]:
        """If ``True`` forces the axis to start on a tick. Defaults to ``False`` for
        :class:`XAxis`, ``True`` for :class:`YAxis`, and ``False`` for :class:`ZAxis`.

        .. hint::

          Use this option with the :meth:`GenericAxis.min_padding` setting to control the
          axis start.

        .. warning::

          This option is always disabled on a :class:`YAxis`, when panning type is either
          ``y`` or ``xy``.

        :rtype: :class:`bool <python:bool>`  or :obj:`None <python:None>`
        """
        return self._start_on_tick

    @start_on_tick.setter
    def start_on_tick(self, value):
        if value is None:
            self._start_on_tick = None
        else:
            self._start_on_tick = bool(value)

    @property
    def tick_amount(self) -> Optional[int]:
        """The amount of ticks to draw on the axis. Defaults to :obj:`None <python:None>`.

        .. hint::

          This provides greater control for aligning the ticks of multiple charts or panes
          within a chart.

        .. warning::

          This option overrides the :meth:`GenericAxis.tick_pixel_interval` option.

        .. note::

          This option only has an effect on linear axes. Datetime, logarithmic, or
          category axes are not affected.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._tick_amount

    @tick_amount.setter
    def tick_amount(self, value):
        self._tick_amount = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def tick_color(self) -> Optional[str | Gradient | Pattern]:
        """Color for the main tick marks. Defaults to ``'#ccd6eb'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._tick_color

    @tick_color.setter
    def tick_color(self, value):
        from highcharts_core import utility_functions
        self._tick_color = utility_functions.validate_color(value)

    @property
    def tick_interval(self) -> Optional[int | float | Decimal]:
        """The interval of the tick marks in axis units. Defaults to
        :obj:`None <python:None>`.

        When :obj:`None <python:None>`, the ``tick_interval`` is automatically computed
        to approximately follow :meth:`GenericAxis.tick_pixel_interval` on linear and
        datetime axes. On category axes, :obj:`None <python:None>` will default to ``1``
        (one category).

        .. note::

          Datetime axes are based on milliseconds, so for example an interval of one day
          is expressed as ``24 * 3600 * 1000``.

        On logarithmic axes, the unit is the power of the value. For example, setting the
        ``tick_interval`` to ``1`` puts one tick on each of 0.1, 1, 10, 100, etc.
        Setting the value to ``0.1`` produces 9 ticks between 1 and 10, 10 and 100 etc.

        .. warning:

          If the ``tick_interval`` is too dense for labels to be drawn, Highcharts will
          automatically remove ticks.

        .. warning::

          If the chart has multiple axes, the :meth:`GenericAxis.align_ticks` setting may
          interfere with ``tick_interval``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._tick_interval

    @tick_interval.setter
    def tick_interval(self, value):
        self._tick_interval = validators.numeric(value, allow_empty = True)

    @property
    def tick_length(self) -> Optional[int | float | Decimal]:
        """The length of the main tick marks, in pixels. Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._tick_length

    @tick_length.setter
    def tick_length(self, value):
        self._tick_length = validators.numeric(value, allow_empty = True)

    @property
    def tickmark_placement(self) -> Optional[str]:
        """If ``'on'``, the tick mark is placed in the center of the category. If
        ``'between'``, the tick mark is placed between categories. If
        :obj:`None <python:None>`, defaults to ``'between'`` if
        :meth:`tick_interval <GenericAxis.tick_interval>` is ``1``, otherwise defaults to
        ``'on'``.

        .. warning::

          Applies to category axes only.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._tickmark_placement

    @tickmark_placement.setter
    def tickmark_placement(self, value):
        if not value:
            self._tickmark_placement = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['on', 'between']:
                raise errors.HighchartsValueError(f'tickmark_placement expects either '
                                                  f'"on" or "between". Received: {value}')

            self._tickmark_placement = value

    @property
    def tick_pixel_interval(self) -> Optional[int | float | Decimal]:
        """If :meth:`tick_interval <GenericAxis.tick_interval>` is :obj:`None <python:None>`,
        this setting establishes the approximate interval between major tick marks,
        expressed in pixels. Defaults to ``100``.

        .. warning::

          Does not apply to categorized axes.

        .. note::

          The tick interval is also influenced by the
          :meth:`min_tick_interval <GenericAxis.min_tick_interval>` setting, which, by
          default, prevents ticks from being denser than the data points.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._tick_pixel_interval

    @tick_pixel_interval.setter
    def tick_pixel_interval(self, value):
        self._tick_pixel_interval = validators.numeric(value, allow_empty = True)

    @property
    def tick_position(self) -> Optional[str]:
        """The position of the major tick marks relative to the axis line. Defaults to
        ``'outside'``.

        Accepts either:

          * ``'outside'``
          * ``'inside'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._tick_position

    @tick_position.setter
    def tick_position(self, value):
        if not value:
            self._tick_position = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['inside', 'outside']:
                raise errors.HighchartsValueError(f'tick_position expects either '
                                                  f'"inside" or "outside". Received: '
                                                  f'{value}')

            self._tick_position = value

    @property
    def tick_positioner(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function returning an array defining where the ticks are
        laid out on the axis.

        .. warning::

          This overrides the default behaviour of
          :meth:`tick_pixel_interval <GenericAxis.tick_pixel_interval>` and
          :meth:`tick_interval <GenericAxis.tick_interval>`.

        The automatic tick positions are accessible (in JavaScript) through
        ``this.tickPositions`` and can be modified by the callback.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._tick_positioner

    @tick_positioner.setter
    @class_sensitive(CallbackFunction)
    def tick_positioner(self, value):
        self._tick_positioner = value

    @property
    def tick_positions(self) -> Optional[List[int | float | Decimal]]:
        """An array that explicitly positions the major tick marks along the axis.
        Defaults to :obj:`None <python:None>`.

        .. warning::

          Setting tick positions explicitly using this setting overrides the default
          behavior of :meth:`tick_pixel_interval <GenericAxis.tick_pixel_interval>` and
          :meth:`tick_interval <GenericAxis.tick_interval>`.

        :rtype: :class:`list <python:list>` of numeric values, or
          :obj:`None <python:None>`
        """
        return self._tick_positions

    @tick_positions.setter
    def tick_positions(self, value):
        if not value:
            self._tick_positions = None
        else:
            self._tick_positions = [validators.numeric(x)
                                    for x in validators.iterable(value)]

    @property
    def tick_width(self) -> Optional[int | float | Decimal]:
        """The width of the main tick marks, in pixels. Defaults to ``0`` on category
        axes, otherwise defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._tick_width

    @tick_width.setter
    def tick_width(self, value):
        self._tick_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def type(self) -> Optional[str]:
        """The type of axis. Defaults to ``'linear'``.

        Accepts the following values:

          * ``'linear'``
          * ``'logarithmic'``
          * ``'datetime'``
          * ``'category'``

        .. note::

          In a ``'datetime'`` axis, the numbers are given in milliseconds, and tick marks
          are placed on appropriate values like full hours or days.

        .. note::

          In a ``'category'`` axis, either the :meth:`categories <GenericAxis.categories>`
          setting determines the categories rendered on the axis, or the categories are
          derived from the point names of the chart's series.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.AXIS_TYPES:
                raise errors.HighchartsValueError(f'type expects a recognized  axis type.'
                                                  f'Received: {value}')

            self._type = value

    @property
    def unique_names(self) -> Optional[bool]:
        """If ``True``, points are placed on the axis according to their names. If the
        same point name is repeated in the same or another series, the point is placed on
        the same axis position as other points of the same name. When ``False``, the
        points are laid out in increasing positions regardless of their names, and the
        axis category will take the name of the last point in each position. Defaults
        to ``True``.

        .. warning::

          Applies only to category axes.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._unique_names

    @unique_names.setter
    def unique_names(self, value):
        if value is None:
            self._unique_names = None
        else:
            self._unique_names = bool(value)

    @property
    def units(self) -> Optional[List[List[str | List[int | float | Decimal | constants.EnforcedNullType | NoneType]]]]:
        """An array determining what time intervals the data is allowed to be grouped to.
        Each array item is an array where the first value is the time unit expressed as a
        :class:`str <python:str>` and the second value is another array of allowed
        multiples.

        .. warning::

          Only applies to datetime axes.

        Defaults to :obj:`None <python:None>`, which behaves as:

        .. code-block:: python

          {
              'units': [
                  [
                      'millisecond', # unit name
                      [1, 2, 5, 10, 20, 25, 50, 100, 200, 500] # allowed multiples
                  ],
                  [
                      'second',
                      [1, 2, 5, 10, 15, 30]
                  ],
                  [
                      'minute',
                      [1, 2, 5, 10, 15, 30]
                  ],
                  [
                      'hour',
                      [1, 2, 3, 4, 6, 8, 12]
                  ],
                  [
                      'day',
                      [1]
                  ],
                  [
                      'week',
                      [1]
                  ],
                  [
                      'month',
                      [1, 3, 6]
                  ],
                  [
                      'year',
                      None
                  ]
              ]
          }

        :rtype: :class:`list <python:list>` of :class:`list <python:list>` of
          :class:`str <python:str>` and :class:`list <python:list>` of numerics, or
          :obj:`None <python:None>`
        """
        return self._units

    @units.setter
    def units(self, value):
        if not value:
            self._units = None
        else:
            value = validators.iterable(value)
            value = [validators.iterable(x) for x in value]
            for item in value:
                if len(item) != 2:
                    raise errors.HighchartsValueError(f'Each entry in the units list '
                                                      f'is expected to be a 2-member '
                                                      f'list. However, was a {value}-'
                                                      f'member list.')
                validators.string(item[0])
                if item[1] and not isinstance(item[1], constants.EnforcedNullType):
                    [validators.numeric(x) for x in item[1]]

            self._units = value

    @property
    def visible(self) -> Optional[bool]:
        """If ``True``, renders the axis (including title, line, ticks, and labels). If
        ``False``, hides the axis (including title, line, ticks, and labels). Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is None:
            self._visible = None
        else:
            self._visible = bool(value)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The Z-index for the axis group (including title, line, ticks, and labels).
        Defaults to ``'2'``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)
