from typing import Optional, Any, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts import errors, constants
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.animation import AnimationOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.shadows import ShadowOptions
from highcharts.chart.events import ChartEvents
from highcharts.chart.options_3d import Options3D
from highcharts.axes.parallel_axes import ParallelAxesOptions
from highcharts.chart.reset_zoom_button import ResetZoomButtonOptions
from highcharts.chart.scrollable_plot_area import ScrollablePlotArea


class PanningOptions(HighchartsMeta):
    """Configures panning behavior in a chart.

    .. hint::

      Best used with :meth:`Chart.pan_key` to combine zooming and panning.

    .. note::

      On touch devices, when the :meth:`Tooltip.follow_touch_move` property is
      ``True`` (default), panning requires two fingers. To allow panning with one
      finger, set ``follow_touch_move`` to ``False``.

    """

    def __init__(self, **kwargs):
        self._enabled = False
        self._type = 'x'

        self.enabled = kwargs.pop('enabled', False)
        self.type = kwargs.pop('type', 'x')

    @property
    def enabled(self) -> bool:
        """If ``True``, enables chart panning. Defaults to ``False``.

        :returns: Flag enabling or disabling chart panning.
        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @property
    def type(self) -> str:
        """Determines in what dimensions the user can pan the chart. Defaults to ``'x'``.

        Accepts:

          * ``'x'``
          * ``'y'``
          * ``'xy'``

        :rtype: :class:`str`
        """
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = 'x'
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['x', 'y', 'xy']:
                raise errors.HighchartsValueError(f'Panning.type expects a value of '
                                                  f'either "x", "y", "xy", or None. '
                                                  f'Received: {value}')
            self._type = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.pop('enabled', False),
            'type': as_dict.pop('type', 'x')
        }

        return cls(**kwargs)

    def to_dict(self):
        return {
            'enabled': self.enabled,
            'type': self.type
        }


class Chart(HighchartsMeta):
    """Configuration settings that apply to a chart."""

    def __init__(self, **kwargs):
        self._align_thresholds = False
        self._align_ticks = True
        self._allow_mutating_data = True
        self._animation = None
        self._background_color = constants.DEFAULT_CHART_BACKGROUND_COLOR
        self._border_color = constants.DEFAULT_CHART_BORDER_COLOR
        self._border_radius = constants.DEFAULT_CHART_BORDER_RADIUS
        self._border_width = constants.DEFAULT_CHART_BORDER_WIDTH
        self._class_name = None
        self._color_count = constants.DEFAULT_CHART_COLOR_COUNT
        self._display_errors = True
        self._events = None
        self._height = constants.EnforcedNull
        self._ignore_hidden_series = True
        self._inverted = False
        self._margin_bottom = None
        self._margin_left = None
        self._margin_right = None
        self._margin_top = None
        self._number_formatter = None
        self._options_3d = None
        self._pan_key = None
        self._panning = None
        self._parallel_axes = None
        self._parallel_coordinates = None
        self._pinch_type = None
        self._plot_background_color = constants.DEFAULT_CHART_PLOT_BACKGROUND_COLOR
        self._plot_background_image = None
        self._plot_border_color = constants.DEFAULT_CHART_PLOT_BORDER_COLOR
        self._plot_border_width = constants.DEFAULT_CHART_PLOT_BORDER_WIDTH
        self._plot_shadow = False
        self._polar = False
        self._reflow = True
        self._render_to = None
        self._reset_zoom_button = None
        self._scrollable_plot_area = None
        self._selection_marker_fill = constants.DEFAULT_CHART_SELECTION_MARKER_FILL
        self._shadow = False
        self._show_axes = None
        self._spacing_bottom = constants.DEFAULT_CHART_SPACING_BOTTOM
        self._spacing_left = constants.DEFAULT_CHART_SPACING_LEFT
        self._spacing_top = constants.DEFAULT_CHART_SPACING_TOP
        self._spacing_right = constants.DEFAULT_CHART_SPACING_RIGHT
        self._style = constants.DEFAULT_CHART_STYLE
        self._styled_mode = False
        self._type = constants.DEFAULT_CHART_TYPE
        self._width = constants.EnforcedNull
        self._zoom_by_single_touch = False
        self._zoom_key = None
        self._zoom_type = None

        self.align_thresholds = kwargs.pop('align_thresholds', False)
        self.align_ticks = kwargs.pop('align_ticks', True)
        self.allow_mutating_data = kwargs.pop('allow_mutating_data', True)
        self.animation = kwargs.pop('animation', None)
        self.background_color = kwargs.pop('background_color',
                                           constants.DEFAULT_CHART_BACKGROUND_COLOR)
        self.border_color = kwargs.pop('border_color',
                                       constants.DEFAULT_CHART_BORDER_COLOR)
        self.border_radius = kwargs.pop('border_radius',
                                        constants.DEFAULT_CHART_BORDER_RADIUS)
        self.border_width = kwargs.pop('border_width',
                                       constants.DEFAULT_CHART_BORDER_WIDTH)
        self.class_name = kwargs.pop('class_name', None)
        self.color_count = kwargs.pop('color_count', constants.DEFAULT_CHART_COLOR_COUNT)
        self.display_errors = kwargs.pop('display_errors', True)
        self.events = kwargs.pop('events', None)
        self.height = kwargs.pop('height', constants.EnforcedNull)
        self.ignore_hidden_series = kwargs.pop('ignore_hidden_series', True)
        self.inverted = kwargs.pop('inverted', False)
        self.margin_bottom = kwargs.pop('margin_bottom', None)
        self.margin_left = kwargs.pop('margin_left', None)
        self.margin_right = kwargs.pop('margin_right', None)
        self.margin_top = kwargs.pop('margin_top', None)
        self.number_formatter = kwargs.pop('number_formatter', None)
        self.options_3d = kwargs.pop('options_3d', None)
        self.pan_key = kwargs.pop('pan_key', None)
        self.panning = kwargs.pop('panning', None)
        self.parallel_axes = kwargs.pop('parallel_axes', None)
        self.parallel_coordinates = kwargs.pop('parallel_coordinates', None)
        self.pinch_type = kwargs.pop('pinch_type', None)
        self.plot_background_color = kwargs.pop('plot_background_color',
                                                constants.DEFAULT_CHART_PLOT_BACKGROUND_COLOR)
        self.plot_background_image = kwargs.pop('plot_background_image', None)
        self.plot_border_color = kwargs.pop('plot_border_color',
                                            constants.DEFAULT_CHART_PLOT_BORDER_COLOR)
        self.plot_border_width = kwargs.pop('plot_border_width',
                                            constants.DEFAULT_CHART_PLOT_BORDER_WIDTH)
        self.plot_shadow = kwargs.pop('plot_shadow', False)
        self.polar = kwargs.pop('polar', False)
        self.reflow = kwargs.pop('reflow', True)
        self.render_to = kwargs.pop('render_to', None)
        self.reset_zoom_button = kwargs.pop('reset_zoom_button', None)
        self.scrollable_plot_area = kwargs.pop('scrollable_plot_area', None)
        self.selection_marker_fill = kwargs.pop('selection_marker_fill',
                                                constants.DEFAULT_CHART_SELECTION_MARKER_FILL)
        self.shadow = kwargs.pop('shadow', False)
        self.show_axes = kwargs.pop('show_axes', None)
        self.spacing_bottom = kwargs.pop('spacing_bottom',
                                         constants.DEFAULT_CHART_SPACING_BOTTOM)
        self.spacing_left = kwargs.pop('spacing_left',
                                       constants.DEFAULT_CHART_SPACING_LEFT)
        self.spacing_top = kwargs.pop('spacing_top', constants.DEFAULT_CHART_SPACING_TOP)
        self.spacing_right = kwargs.pop('spacing_right',
                                        constants.DEFAULT_CHART_SPACING_RIGHT)
        self.style = kwargs.pop('style', constants.DEFAULT_CHART_STYLE)
        self.styled_mode = kwargs.pop('styled_mode', False)
        self.type = kwargs.pop('type', constants.DEFAULT_CHART_TYPE)
        self.width = kwargs.pop('width', constants.EnforcedNull)
        self.zoom_by_single_touch = kwargs.pop('zoom_by_single_touch', False)
        self.zoom_key = kwargs.pop('zoom_key', None)
        self.zoom_type = kwargs.pop('zoom_type', None)

    @property
    def align_thresholds(self) -> bool:
        """When using multiple axes, align the thresholds. When ``True``, other ticks will
        also be aligned. Defaults to ``False``.

        .. note::

          For line series and some other series types, the threshold option is set to
          ``null`` by default. This will in turn cause their y-axis to not have a
          threshold. In order to avoid that, set the series threshold to ``0`` or another
          number.

        .. note::

          If :meth:`AxisOptions.start_on_tick` or :meth:`AxisOptions.end_on_tick` are set
          to ``False``, or if the axis is logarithmic, the threshold will not be aligned.

        :returns: Flag indicating whether thresholds should be aligned.
        :rtype: :class:`bool <python:bool>`
        """
        return self._align_thresholds

    @align_thresholds.setter
    def align_thresholds(self, value):
        self._align_thresholds = bool(value)

    @property
    def align_ticks(self) -> bool:
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
        :rtype: :class:`bool <python:bool>`
        """
        return self._align_ticks

    @align_ticks.setter
    def align_ticks(self, value):
        self._align_ticks = bool(value)

    @property
    def allow_mutating_data(self) -> bool:
        """If ``True``, the original data source will be allowed to be mutated. However,
        if ``False`` then Highcharts will create a copy of the original data to prevent
        inadvertent mutation. Defaults to ``True``.

        .. note::

          By default, (for memory and performance reasons) the chart does not copy the
          data but keeps it as a reference.

          In some cases, this might result in mutating the original data source. In order
          to prevent that, set this property to ``False``. Please note that changing this
          may decrease performance, especially with bigger sets of data.

        :returns: Flag indicating whether to allow mutation by referencing th eoriginal
          data (``True``), or prevent it by copying the original data (``False``).
        :rtype: :class:`bool <python:bool>`
        """
        return self._allow_mutating_data

    @allow_mutating_data.setter
    def allow_mutating_data(self, value):
        self._allow_mutating_data = bool(value)

    @property
    def animation(self) -> Optional[Any[bool, AnimationOptions]]:
        """Configures the overall animation for all chart updating.

        The animation can be configured as either a boolean or a :class:`AnimationOptions`
        object. If ``True``, it will apply the ``'swing'`` jQuery easing and a duration of
        500 ms by default. If used as a :class:`AnimationOptions` instance, you have more
        fine-grianed configuration control.

        Animation can be disabled throughout the chart by setting it to ``False`` here.
        It can be overridden for each individual API method as a function parameter. The
        only animation not affected by this option is the initial series animation, see
        :meth:`PlotOptions.series.animation`.

        When zooming on a series with less than 100 points, the chart redraw will be done
        with animation, but in case of more data points, it is necessary to set this
        option to ensure animation on zoom.

        :returns: Settings for the animation of image patterns.
        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if value is None:
            self._animation = None
        elif value is False:
            self._animation = False
        elif value is True:
            self._animation = True
        else:
            self._animation = validate_types(value,
                                             types = AnimationOptions)

    @property
    def background_color(self) -> Optional[Any[str, Gradient, Pattern]]:
        f"""The background color or gradient for the outer chart area. Defaults to
        ``'{constants.DEFAULT_CHART_BACKGROUND_COLOR}'``.

        :returns: The backgorund color for the outer chart area.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if not value:
            self._background_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._background_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._background_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Gradient.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._background_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._background_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Pattern.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._background_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_color(self) -> Optional[Any[str, Gradient, Pattern]]:
        f"""The color of the outer chart border. Defaults to
        ``'{constants.DEFAULT_CHART_BORDER_COLOR}'``.

        :returns: The color of the outer chart border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_radius(self) -> Optional[Any[int, float, Decimal]]:
        f"""The border radius (in pixels) applied to the outer chart border. Defaults to
        ``{constants.DEFAULT_CHART_BORDER_RADIUS}``.

        :returns: The border radius to apply to the outer chart border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[Any[int, float, Decimal]]:
        f"""The border width (in pixels) applied to the outer chart border. Defaults to
        ``{constants.DEFAULT_CHART_BORDER_WIDTH}``.

        :returns: The border width to apply to the outer chart border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        f"""A classname to apply styling using CSS.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color_count(self) -> Optional[int]:
        f"""In styled mode, sets how many colors the class names should rotate between.
        Defaults to ``{constants.DEFAULT_CHART_COLOR_COUNT}``

        With ten colors, series (or points) are given class names like
        ``highcharts-color-0``, ``highcharts-color-0`` [...] ``highcharts-color-9``. The
        equivalent in non-styled mode is to set colors using the colors setting.

        :returns: The number of colors to cycle through in styled mode.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_count

    @color_count.setter
    def color_count(self, value):
        self._color_count = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0,
                                               coerce_value = True)

    @property
    def display_errors(self) -> bool:
        """If ``True``, will display errors on the chart itself. If ``False``, will only
        report errors to the console. Defaults to ``True``.

        :returns: Flag indicating whether ot display errors on the chart.
        :rtype: :class:`bool <python:bool>`
        """
        return self._display_errors

    @display_errors.setter
    def display_errors(self, value):
        self._display_errors = bool(value)

    @property
    def events(self) -> Optional[ChartEvents]:
        """Definition of JavaScript event listeners to apply to the chart.

        :rtype: :class:`ChartEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(ChartEvents)
    def events(self, value):
        self._events = value

    @property
    def height(self) -> Any[constants.EnforcedNullType, int, float, Decimal, str]:
        """An explicit height for the chart.

        Defaults to :class:`EnforcedNull <EnforcedNullType>`` which indicates
        a JavaScript value of ``null`` (as opposed to :obj:`None <python:None>`) which
        results in ``undefined`` when converted JavaScript.

        If a number, the height is given in pixels. If given a percentage string (for
        example ``'56%'``), the height is given as the percentage of the actual chart
        width. This allows for preserving the aspect ratio across responsive sizes.

        By default (when null) the height is calculated from the offset height of the
        containing element, or 400 pixels if the containing element's height is 0.

        :rtype: :class:`EnforcedNullType` or numeric or :class:`str <python:str>`
        """
        return self._height or constants.EnforcedNull

    @height.setter
    def height(self, value):
        if value is None:
            self._height = constants.EnforcedNull
        else:
            try:
                try:
                    self._height = validators.numeric(value,
                                                      allow_empty = False,
                                                      minimum = 0)
                except ValueError:
                    self._height = validators.string(value,
                                                     allow_empty = False)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported data type.')

    @property
    def ignore_hidden_series(self) -> bool:
        """If ``True``, the axes will scale to the remaining visible series once one
        series is hidden. If ``False``, hiding and showing a series will not affect the
        axes or the other series.

        Defaults to ``True``.

        .. note::

          For stacks, once one series within the stack is hidden, the rest of the stack
          will close in around it even if the axis is not affected.

        :returns: Flag indicating whether to ignore hidden series.
        :rtype: :class:`bool <python:bool>`
        """
        return self._ignore_hidden_series

    @ignore_hidden_series.setter
    def ignore_hidden_series(self, value):
        self._ignore_hidden_series = bool(value)

    @property
    def inverted(self) -> bool:
        """If ``True``, inverts the axes so that the x-axis is vertical and y-axis is
        horizontal. Defaults to ``False``.

        .. hint::

          When ``True``, the x-axis is reversed by default.

        .. warning::

          If a bar series is present in the chart, it will be inverted automatically.

        .. hint::

          Inverting the chart doesn't have an effect if there are no cartesian series in
          the chart, or if the chart is a polar chart type.

        :returns: Flag indicating whether to invert the axes.
        :rtype: :class:`bool <python:bool>`
        """
        return self._inverted

    @inverted.setter
    def inverted(self, value):
        self._inverted = bool(value)

    @property
    def margin(self) -> Optional[List[Any[int, float, Decimal]]]:
        """The margin between the outer edge of the chart and the plot area. The numbers
        in the array designate top, right, bottom and left respectively.

        By default there is no margin. The actual space is dynamically calculated from the
        offset of axis labels, axis title, title, subtitle and legend in addition to the
        ``spacing_top``, ``spacing_right``, ``spacing_bottom`` and ``spacing_left``
        options.

        .. note::

          This property is a convenience property to consolidate simple margin
          configuration across the ``margin_top``, ``margin_right``, ``margin_bottom``,
          and ``margin_left`` options. Values will be propagated between all options.

        :rtype: :class:`list <python:list>` of four numeric values or
          :obj:`None <python:None>`
        """
        result = [self.margin_top,
                  self.margin_right,
                  self.margin_bottom,
                  self.margin_left]

        if not any(result):
            return None

        return result

    @margin.setter
    def margin(self, value):
        if value is None:
            self.margin_top = None
            self.margin_right = None
            self.margin_bottom = None
            self.margin_left = None
        elif checkers.is_iterable(value):
            if len(value) != 4:
                raise errors.HighchartsValueError(f'margin expects either a single value '
                                                  f'or an iterable of four values. '
                                                  f'Received an iterable of {len(value)} '
                                                  f'values ({value})')
            self.margin_top = value[0]
            self.margin_right = value[1]
            self.margin_bottom = value[2]
            self.margin_left = value[3]
        else:
            self.margin_top = value
            self.margin_right = value
            self.margin_bottom = value
            self.margin_left = value

    @property
    def margin_bottom(self) -> Optional[Any[int, float, Decimal]]:
        """The margin between the bottom outer edge of the chart and the plot area. Use
        this to set a fixed pixel value for the margin as opposed to the default dynamic
        margin.

        By default, not set.

        .. seealso::

          * :meth:`Chart.spacing_bottom`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin_bottom

    @margin_bottom.setter
    def margin_bottom(self, value):
        self._margin_bottom = validators.numeric(value, allow_empty = True)

    @property
    def margin_left(self) -> Optional[Any[int, float, Decimal]]:
        """The margin between the left outer edge of the chart and the plot area. Use
        this to set a fixed pixel value for the margin as opposed to the default dynamic
        margin.

        By default, not set.

        .. seealso::

          * :meth:`Chart.spacing_left`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin_left

    @margin_left.setter
    def margin_left(self, value):
        self._margin_left = validators.numeric(value, allow_empty = True)

    @property
    def margin_right(self) -> Optional[Any[int, float, Decimal]]:
        """The margin between the right outer edge of the chart and the plot area. Use
        this to set a fixed pixel value for the margin as opposed to the default dynamic
        margin.

        By default, not set.

        .. seealso::

          * :meth:`Chart.spacing_right`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin_right

    @margin_right.setter
    def margin_right(self, value):
        self._margin_right = validators.numeric(value, allow_empty = True)

    @property
    def margin_top(self) -> Optional[Any[int, float, Decimal]]:
        """The margin between the top outer edge of the chart and the plot area. Use
        this to set a fixed pixel value for the margin as opposed to the default dynamic
        margin.

        By default, not set.

        .. seealso::

          * :meth:`Chart.spacing_top`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin_top

    @margin_top.setter
    def margin_top(self, value):
        self._margin_top = validators.numeric(value, allow_empty = True)

    @property
    def number_formatter(self) -> Optional[str]:
        """JavaScript Callback function to override the default function that formats all
        the numbers in the chart. Returns a string with the formatted number.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._number_formatter

    @number_formatter.setter
    def number_formatter(self, value):
        self._number_formatter = validators.string(value, allow_empty = True)

    @property
    def options_3d(self) -> Optional[Options3D]:
        """Options to render charts in three dimensions.

        .. note::

          This feature requires the JavaScript ``highcharts-3d.js`` module, found in the
          download package or online at
          `code.highcharts.com/highcharts-3d.js <https://code.highcharts.com/highcharts-3d.js>`_.

        :rtype: :class:`Options3D` or :obj:`None <python:None>`
        """
        return self._options_3d

    @options_3d.setter
    @class_sensitive(Options3D)
    def options_3d(self, value):
        self._options_3d = value

    @property
    def pan_key(self) -> Optional[str]:
        """Allows setting a key to switch between zooming and panning.

        Accepts the following values:

          * ``'alt'``
          * ``'ctrl'``
          * ``'meta'`` (the command key on Mac and Windows key on Windows)
          * ``'shift'``.

        The keys are mapped directly to the key properties of the click event argument
        (``event.altKey``, ``event.ctrlKey``, ``event.metaKey``, and ``event.shiftKey``).

        :returns: The key that switches between zooming and panning.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pan_key

    @pan_key.setter
    def pan_key(self, value):
        if not value:
            self._pan_key = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['alt', 'ctrl', 'meta', 'shift']:
                raise errors.HighchartsValueError(f'pan_key expects a value of "alt", '
                                                  f'"ctrl", "meta", or "shift". Was: '
                                                  f'{value}')
            self._pan_key = value

    @property
    def panning(self) -> Optional[PanningOptions]:
        """Configures panning behavior in a chart.

        .. hint::

          Best used with :meth:`Chart.pan_key` to combine zooming and panning.

        .. note::

          On touch devices, when the :meth:`Tooltip.follow_touch_move` property is
          ``True`` (default), panning requires two fingers. To allow panning with one
          finger, set ``follow_touch_move`` to ``False``.

        :returns: Configuration settings for panning behavior.
        :rtype: :class:`PanningOptions` or :obj:`None <python:None>`
        """
        return self._panning

    @panning.setter
    @class_sensitive(PanningOptions)
    def panning(self, value):
        self._panning = value

    @property
    def parallel_axes(self) -> Optional[ParallelAxesOptions]:
        """Common options for all Y-Axes rendered in a parallel coordinates plot.

        .. note::

          This feature requires in JavaScript ``modules/parallel-coordinates.js``.

        :rtype: :class:`ParallelAxesOptions` or :obj:`None <python:None>`
        """
        return self._parallel_axes

    @parallel_axes.setter
    @class_sensitive(ParallelAxesOptions)
    def parallel_axes(self, value):
        self._parallel_axes = value

    @property
    def parallel_coordinates(self) -> bool:
        """If ``True``, renders charts as a parallel coordinates plot. Defaults to
        ``False``.

        In a parallel coordinates plot (||-coords) by default all required Y-axes are
        generated and the legend is disabled.

        .. note::

          This feature requires the JavaScript module ``modules/parallel-coordinates.js``.

        .. seealso::

          * `Parallel Coordinates Demo <https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples//highcharts/demo/parallel-coordinates/>`_

        :returns: Flag indicating whether the chart is a parallel coordinates plot.
        :rtype: :class:`bool <python:bool>`
        """
        return self._parallel_coordinates

    @parallel_coordinates.setter
    def parallel_coordinates(self, value):
        self._parallel_coordinates = bool(value)

    @property
    def pinch_type(self) -> Optional[str]:
        """Equivalent to :meth:`Chart.zoom_type` but for multi-touch gestures only.
        By default, is not specified.

        Accepts:

          * ``'x'``
          * ``'y'``
          * ``'xy'``
          * :obj:`None <python:None>`

        If not specified explicitly, the pinch type is the same as the
        :meth:`Chart.zoom_type`. However, pinching can be enabled separately in some
        cases, for example in stock charts where a mouse drag pans the chart, while
        pinching is enabled. When :meth:`Tooltip.follow_touch_move` is ``True``,
        pinch type only applies to two-finger touches.

        :returns: The configuration of the pinch directional support.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pinch_type

    @pinch_type.setter
    def pinch_type(self, value):
        if not value:
            self._pinch_type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['x', 'y', 'xy']:
                raise errors.HighchartsValueError(f'pinch_type is expected to be either '
                                                  f'"x", "y", "xy", or None. Was: '
                                                  f'{value}')
            self._pinch_type = value

    @property
    def plot_background_color(self) -> Optional[Any[str, Gradient, Pattern]]:
        f"""The background color or gradient for the plot area. Defaults to
        ``'{constants.DEFAULT_CHART_PLOT_BACKGROUND_COLOR}'``.

        :returns: The backgorund color for the plot area.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._plot_background_color

    @plot_background_color.setter
    def plot_background_color(self, value):
        if not value:
            self._plot_background_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._plot_background_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._plot_background_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._plot_background_color = Gradient.from_dict(value)
                else:
                    self._plot_background_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._plot_background_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._plot_background_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._plot_background_color = Pattern.from_dict(value)
                else:
                    self._plot_background_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._plot_background_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def plot_background_image(self) -> Optional[str]:
        """The URL for an image to use as the background of the plot area.

        .. hint::

           To set an image as the background for the entire chart, set a CSS background
           image to the container element.

         .. note::

           Note that for the image to be applied to exported charts, its URL needs to be
           accessible by the export server.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises HighchartsValueError: if a value is supplied that is not a URL or not
          path-like

        """
        return self._plot_background_image

    @plot_background_image.setter
    def plot_background_image(self, value):
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
    def plot_border_color(self) -> Optional[Any[str, Gradient, Pattern]]:
        f"""The color of the outer chart border. Defaults to
        ``'{constants.DEFAULT_CHART_PLOT_BORDER_COLOR}'``.

        :returns: The color of the outer chart border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._plot_border_color

    @plot_border_color.setter
    def plot_border_color(self, value):
        if not value:
            self._plot_border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._plot_border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._plot_border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._plot_border_color = Gradient.from_dict(value)
                else:
                    self._plot_border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._plot_border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._plot_border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._plot_border_color = Pattern.from_dict(value)
                else:
                    self._plot_border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._plot_border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def plot_border_width(self) -> Optional[Any[int, float, Decimal]]:
        f"""The border width (in pixels) applied to the outer chart border. Defaults to
        ``{constants.DEFAULT_CHART_PLOT_BORDER_WIDTH}``.

        :returns: The border width to apply to the outer chart border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._plot_border_width

    @plot_border_width.setter
    def plot_border_width(self, value):
        self._plot_border_width = validators.numeric(value, allow_empty = True)

    @property
    def plot_shadow(self) -> Any[bool, ShadowOptions]:
        """Configuration of a drop shadow applied to the plot area. Accepts either a
        boolean value of ``False`` which disables any shadow, or a :class:`ShadowOptions`
        instance with the applicable configuration.

        Defaults to ``False``.

        .. warning::

          Requires that :meth:`Chart.plot_background_color` be set.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._plot_shadow

    @plot_shadow.setter
    def plot_shadow(self, value):
        if value is False:
            self._plot_shadow = False
        else:
            value = validate_types(value,
                                   types = ShadowOptions,
                                   allow_none = False)
            self._plot_shadow = value

    @property
    def polar(self) -> bool:
        """If ``True``, cartesian charts like line, spline, area, and column are
        transformed into the polar coordinate system. This produces polar charts (also
        known as radar charts). Defaults to ``False``.

        :returns: Flag indicating whether to render the chart as a polar chart.
        :rtype: :class:`bool <python:bool>`
        """
        return self._polar

    @polar.setter
    def polar(self, value):
        self._polar = bool(value)

    @property
    def reflow(self) -> bool:
        """If ``True``, reflows the chart to fit the width of the container ``div`` when
        the window is resized. Defaults to ``True``.

        :returns: Flag indicating whether to reflow the chart in response to window
          resizing.
        :rtype: :class:`bool <python:bool>`
        """
        return self._reflow

    @reflow.setter
    def reflow(self, value):
        self._reflow = bool(value)

    @property
    def render_to(self) -> Optional[str]:
        """The ID of the HTML element where the chart will be rendered.

        .. note::

          In JavaScript, the HTML element can also be passed by direct reference, or as
          the first argument of the chart constructor, in which case the option is not
          needed.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._render_to

    @render_to.setter
    def render_to(self, value):
        self._render_to = validators.string(value, allow_empty = True)

    @property
    def reset_zoom_button(self) -> Optional[ResetZoomButtonOptions]:
        """Configuration settings for the button that appears after a selection zoom,
        allowing the user to reset zoom.

        :rtype: :class:`ResetZoomButtonOptions` or :obj:`None <python:None>`
        """
        return self._reset_zoom_button

    @reset_zoom_button.setter
    @class_sensitive(ResetZoomButtonOptions)
    def reset_zoom_button(self, value):
        self._reset_zoom_button = value

    @property
    def scrollable_plot_area(self) -> Optional[ScrollablePlotArea]:
        """Configuration settings to make the plot area scrollable.

        This feature provides a minimum size for the plot area of the chart. If the size
        gets smaller than this, typically on mobile devices, a native browser scrollbar is
        presented. This scrollbar provides smooth scrolling for the contents of the plot
        area, whereas the title, legend and unaffected axes are fixed.

        .. hint::

          Since v7.1.2, a scrollable plot area can be defined for either horizontal or
          vertical scrolling, depending on whether the `minimum_width` or `minimum_height`
          options are set.

        :rtype: :class:`ScrollablePlotArea` or :obj:`None <python:None>`
        """
        return self._scrollable_plot_area

    @scrollable_plot_area.setter
    @class_sensitive(ScrollablePlotArea)
    def scrollable_plot_area(self, value):
        self._scrollable_plot_area = value

    @property
    def selection_marker_fill(self) -> Optional[Any[str, Gradient, Pattern]]:
        f"""The background color or the marker square when selecting (zooming in on) an
        area of the chart. Defaults to
        ``'{constants.DEFAULT_CHART_SELECTION_MARKER_FILL}'``.

        :returns: The backgorund color of the marker square when selecting an area of the
          chart.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._selection_marker_fill

    @selection_marker_fill.setter
    def selection_marker_fill(self, value):
        if not value:
            self._selection_marker_fill = None
        elif isinstance(value, (Gradient, Pattern)):
            self._selection_marker_fill = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._selection_marker_fill = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._selection_marker_fill = Gradient.from_dict(value)
                else:
                    self._selection_marker_fill = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._selection_marker_fill = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._selection_marker_fill = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._selection_marker_fill = Pattern.from_dict(value)
                else:
                    self._selection_marker_fill = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._selection_marker_fill = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def shadow(self) -> Any[bool, ShadowOptions]:
        """Configuration of a drop shadow applied to the outer chart area. Accepts either
        a boolean value of ``False`` which disables any shadow, or a
        :class:`ShadowOptions` instance with the applicable configuration.

        Defaults to ``False``.

        .. warning::

          Requires that :meth:`Chart.background_color` be set.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if value is False:
            self._shadow = False
        else:
            value = validate_types(value,
                                   types = ShadowOptions,
                                   allow_none = False)
            self._shadow = value

    @property
    def show_axes(self) -> Optional[bool]:
        """If ``True``, shows axes initially (before series have been added to the chart).

        .. warning::

          This property only applies to empty charts where series are added dynamically.

        :returns: Flag indicating whether to show axes on empty dynamic charts before
          series have been added.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_axes

    @show_axes.setter
    def show_axes(self, value):
        if value is None:
            self._show_axes = None
        else:
            self._show_axes = bool(value)

    @property
    def spacing(self) -> Optional[List[Any[int, float, Decimal]]]:
        f"""The distance between the outer edge of the chart and the content, like title or
        legend, or axis title and labels if present. The numbers in the array designate
        top, right, bottom and left respectively.

        By default, ``{constants.DEFAULT_CHART_SPACING}``.

        .. note::

          This property is a convenience property to consolidate simple spacing
          configuration across the ``spacing_top``, ``spacing_right``, ``spacing_bottom``,
          and ``spacing_left`` options. Values will be propagated between all options.

        :rtype: :class:`list <python:list>` of four numeric values or
          :obj:`None <python:None>`
        """
        result = [self.spacing_top,
                  self.spacing_right,
                  self.spacing_bottom,
                  self.spacing_left]

        if not any(result):
            return None

        return result

    @spacing.setter
    def spacing(self, value):
        if value is None:
            self.spacing_top = None
            self.spacing_right = None
            self.spacing_bottom = None
            self.spacing_left = None
        elif checkers.is_iterable(value):
            if len(value) != 4:
                raise errors.HighchartsValueError(f'spacing expects either a single value '
                                                  f'or an iterable of four values. '
                                                  f'Received an iterable of {len(value)} '
                                                  f'values ({value})')
            self.spacing_top = value[0]
            self.spacing_right = value[1]
            self.spacing_bottom = value[2]
            self.spacing_left = value[3]
        else:
            self.spacing_top = value
            self.spacing_right = value
            self.spacing_bottom = value
            self.spacing_left = value

    @property
    def spacing_bottom(self) -> Optional[Any[int, float, Decimal]]:
        f"""The spacing between the bottom edge of the chart and the content (plot area,
        axis title and labels, title, subtitle or legend in top position).

        By default, ``{constants.DEFAULT_CHART_SPACING_BOTTOM}``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_bottom

    @spacing_bottom.setter
    def spacing_bottom(self, value):
        self._spacing_bottom = validators.numeric(value, allow_empty = True)

    @property
    def spacing_left(self) -> Optional[Any[int, float, Decimal]]:
        f"""The spacing between the left edge of the chart and the content (plot area,
        axis title and labels, title, subtitle or legend in top position).

        Defaults to ``{constants.DEFAULT_CHART_SPACING_LEFT}``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_left

    @spacing_left.setter
    def spacing_left(self, value):
        self._spacing_left = validators.numeric(value, allow_empty = True)

    @property
    def spacing_right(self) -> Optional[Any[int, float, Decimal]]:
        f"""The spacing between the right edge of the chart and the content (plot area,
        axis title and labels, title, subtitle or legend in top position).

        Defaults to ``{constants.DEFAULT_CHART_SPACING_RIGHT}``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_right

    @spacing_right.setter
    def spacing_right(self, value):
        self._spacing_right = validators.numeric(value, allow_empty = True)

    @property
    def spacing_top(self) -> Optional[Any[int, float, Decimal]]:
        f"""The spacing between the top edge of the chart and the content (plot area, axis
        title and labels, title, subtitle or legend in top position).

        Defaults to ``{constants.DEFAULT_CHART_SPACING_TOP}``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_top

    @spacing_top.setter
    def spacing_top(self, value):
        self._spacing_top = validators.numeric(value, allow_empty = True)

    @property
    def style(self) -> Optional[str]:
        f"""Additional CSS styles to apply inline to the container div.

        Defaults to ``{constants.DEFAULT_CHART_STYLE}``.

        .. note::

          Since the default font styles are applied in the renderer, it is ignorant of the
          individual chart options and must be set globally.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @property
    def styled_mode(self) -> bool:
        """If ``True``, sets the chart to operate in **styled mode**, where no
        presentational attributes or CSS are applied to the chart SVG. Instead, CSS rules
        are required to style the chart. Defaults to ``False``.

        .. seealso::

          * The Default Style Sheet:
            `https://code.highcharts.com/css/highcharts.css <https://code.highcharts.com/css/highcharts.css>`_.

        :rtype: :class:`bool <python:bool>`
        """
        return self._styled_mode

    @styled_mode.setter
    def styled_mode(self, value):
        self._styled_mode = bool(value)

    @property
    def type(self) -> str:
        """The default series type for the chart. Defaults to ``'line'``.

        Can be any of the chart types listed under :class:`PlotOptions` and
        :class:`Series`, or can be a series provided by an additional module.

        .. note::

          In TypeScript this option has no effect in sense of typing and instead the type option must always be set in the series.

        :rtype: :class:`str <python:str>`
        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = validators.string(value, allow_empty = True)

    @property
    def width(self) -> Any[constants.EnforcedNullType, int, float, Decimal, str]:
        """An explicit width for the chart.

        Defaults to :class:`EnforcedNull <EnforcedNullType>`` which indicates
        a JavaScript value of ``null`` (as opposed to :obj:`None <python:None>` which
        results in ``undefined`` when converted JavaScript.)

        If a number, the width is given in pixels. If given a percentage string (for
        example ``'56%'``), the width is given as the percentage of the actual chart
        width. This allows for preserving the aspect ratio across responsive sizes.

        By default (when null) the width is calculated from the offset width of the
        containing element.

        :rtype: :class:`EnforcedNullType` or numeric or :class:`str <python:str>`
        """
        return self._width or constants.EnforcedNull

    @width.setter
    def width(self, value):
        if value is None:
            self._width = constants.EnforcedNull
        else:
            try:
                try:
                    self._width = validators.numeric(value,
                                                      allow_empty = False,
                                                      minimum = 0)
                except ValueError:
                    self._width = validators.string(value,
                                                     allow_empty = False)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported data type.')

    @property
    def zoom_by_single_touch(self) -> bool:
        """If ``True``, enables zooming with a single touch (in combination with
        :meth:`Chart.zoom_type`) while two-finger pinch will still work as per
        :meth:`Chart.pinch_type`. Defaults to ``False``.

        .. warning::

          Enabling zoom by single touch will interfere with touch-dragging the chart to
          read the tooltip, and if vertical zooming is enabled will make it hard to scroll
          vertically on the page.

        :rtype: :class:`bool <python:bool>`
        """
        return self._zoom_by_single_touch

    @zoom_by_single_touch.setter
    def zoom_by_single_touch(self, value):
        self._zoom_by_single_touch = bool(value)

    @property
    def zoom_key(self) -> Optional[str]:
        """Sets a key to hold when dragging to zoom the chart.

        .. hint::

          This is useful to avoid zooming while moving points.

        .. hint::

          This should be set to a different key than :meth:`Chart.pan_key`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_key

    @zoom_key.setter
    def zoom_key(self, value):
        self._zoom_key = validators.string(value, allow_empty = True)

    @property
    def zoom_type(self) -> Optional[str]:
        """Determines in which dimensions the user can zoom by dragging the mouse. By
        default, not set.

        Accepts:

          * ``'x'``
          * ``'y'``
          * ``'xy'``
          * :obj:`None <python:None>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_type

    @zoom_type.setter
    def zoom_type(self, value):
        if not value:
            self._zoom_type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['x', 'y', 'xy']:
                raise errors.HighchartsValueError(f'zoom_type is expected to be either '
                                                  f'"x", "y", "xy", or None. Was: '
                                                  f'{value}')
            self._zoom_type = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'align_thresholds': as_dict.pop('alignThresholds', False),
            'align_ticks': as_dict.pop('alignTicks', True),
            'allow_mutating_data': as_dict.pop('allowMutatingData', True),
            'animation': as_dict.pop('animation', None),
            'background_color': as_dict.pop('backgroundColor',
                                            constants.DEFAULT_CHART_BACKGROUND_COLOR),
            'border_color': as_dict.pop('borderColor',
                                        constants.DEFAULT_CHART_BORDER_COLOR),
            'border_radius': as_dict.pop('borderRadius',
                                         constants.DEFAULT_CHART_BORDER_RADIUS),
            'border_width': as_dict.pop('borderWidth',
                                        constants.DEFAULT_CHART_BORDER_WIDTH),
            'class_name': as_dict.pop('className', None),
            'color_count': as_dict.pop('colorCount', constants.DEFAULT_CHART_COLOR_COUNT),
            'display_errors': as_dict.pop('displayErrors', True),
            'events': as_dict.pop('events', None),
            'height': as_dict.pop('height', constants.EnforcedNull),
            'ignore_hidden_series': as_dict.pop('ignoreHiddenSeries', True),
            'inverted': as_dict.pop('inverted', False),
            'margin': as_dict.pop('margin', None),
            'margin_bottom': as_dict.pop('marginBottom', None),
            'margin_left': as_dict.pop('marginLeft', None),
            'margin_right': as_dict.pop('marginRight', None),
            'margin_top': as_dict.pop('marginTop', None),
            'number_formatter': as_dict.pop('numberFormatter', None),
            'options_3d': as_dict.pop('options3d', None),
            'pan_key': as_dict.pop('panKey', None),
            'panning': as_dict.pop('panning', None),
            'parallel_axes': as_dict.pop('parallelAxes', None),
            'parallel_coordinates': as_dict.pop('parallelCoordinates', None),
            'pinch_type': as_dict.pop('pinchType', None),
            'plot_background_color': as_dict.pop('plotBackgroundColor',
                                                 constants.DEFAULT_CHART_PLOT_BACKGROUND_COLOR),
            'plot_background_image': as_dict.pop('plotBackgroundImage', None),
            'plot_border_color': as_dict.pop('plotBorderColor',
                                             constants.DEFAULT_CHART_PLOT_BORDER_COLOR),
            'plot_border_width': as_dict.pop('plotBorderWidth',
                                             constants.DEFAULT_CHART_PLOT_BORDER_WIDTH),
            'plot_shadow': as_dict.pop('plotShadow', False),
            'polar': as_dict.pop('polar', False),
            'reflow': as_dict.pop('reflow', True),
            'render_to': as_dict.pop('renderTo', None),
            'reset_zoom_button': as_dict.pop('resetZoomButton', None),
            'scollable_plot_area': as_dict.pop('scrollablePlotArea', None),
            'selection_marker_fill': as_dict.pop('selectionMarkerFill',
                                                 constants.DEFAULT_CHART_SELECTION_MARKER_FILL),
            'shadow': as_dict.pop('shadow', False),
            'show_axes': as_dict.pop('showAxes', None),
            'spacing': as_dict.pop('spacing', None),
            'spacing_bottom': as_dict.pop('spacingBottom', None),
            'spacing_left': as_dict.pop('spacingLeft', None),
            'spacing_top': as_dict.pop('spacingTop', None),
            'spacing_right': as_dict.pop('spacingRight', None),
            'style': as_dict.pop('style', constants.DEFAULT_CHART_STYLE),
            'styled_mode': as_dict.pop('styledMode', False),
            'type': as_dict.pop('type', constants.DEFAULT_CHART_TYPE),
            'width': as_dict.pop('width', constants.EnforcedNull),
            'zoom_by_single_touch': as_dict.pop('zoomBySingleTouch', False),
            'zoom_key': as_dict.pop('zoomKey', None),
            'zoom_type': as_dict.pop('zoomType', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'alignThresholds': self.align_thresholds,
            'alignTicks': self.align_ticks,
            'allowMutatingData': self.allow_mutating_data,
            'animation': self.animation,
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'colorCount': self.color_count,
            'displayErrors': self.display_errors,
            'events': self.events,
            'height': self.height,
            'ignoreHiddenSeries': self.ignore_hidden_series,
            'inverted': self.inverted,
            'margin': self.margin,
            'marginBottom': self.margin_bottom,
            'marginLeft': self.margin_left,
            'marginRight': self.margin_right,
            'marginTop': self.margin_top,
            'numberFormatter': self.number_formatter,
            'options3d': self.options_3d,
            'panKey': self.pan_key,
            'panning': self.panning,
            'parallelAxes': self.parallel_axes,
            'parallelCoordinates': self.parallel_coordinates,
            'pinchType': self.pinch_type,
            'plotBackgroundColor': self.plot_background_color,
            'plotBackgroundImage': self.plot_background_image,
            'plotBorderColor': self.plot_border_color,
            'plotBorderWidth': self.plot_border_width,
            'plotShadow': self.plot_shadow,
            'polar': self.polar,
            'reflow': self.reflow,
            'renderTo': self.render_to,
            'resetZoomButton': self.reset_zoom_button,
            'scrollablePlotArea': self.scrollable_plot_area,
            'selectionMarkerFill': self.selection_marker_fill,
            'shadow': self.shadow,
            'showAxes': self.show_axes,
            'spacing': self.spacing,
            'spacingBottom': self.spacing_bottom,
            'spacingLeft': self.spacing_left,
            'spacingRight': self.spacing_right,
            'spacingTop': self.spacing_top,
            'style': self.style,
            'styledMode': self.styled_mode,
            'type': self.type,
            'width': self.width,
            'zoomBySingleTouch': self.zoom_by_single_touch,
            'zoomKey': self.zoom_key,
            'zoomType': self.zoom_type
        }

        return self.trim_dict(untrimmed)
