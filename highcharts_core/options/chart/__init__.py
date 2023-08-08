from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import errors, constants, utility_functions
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.utility_classes.animation import AnimationOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.shadows import ShadowOptions
from highcharts_core.utility_classes.events import ChartEvents
from highcharts_core.options.chart.options_3d import Options3D
from highcharts_core.options.axes.parallel_axes import ParallelAxesOptions
from highcharts_core.options.chart.scrollable_plot_area import ScrollablePlotArea
from highcharts_core.options.chart.zooming import ZoomingOptions


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
        self._enabled = None
        self._type = None

        self.enabled = kwargs.get('enabled', None)
        self.type = kwargs.get('type', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables chart panning. Defaults to ``False``.

        :returns: Flag enabling or disabling chart panning.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def type(self) -> Optional[str]:
        """Determines in what dimensions the user can pan the chart. Defaults to ``'x'``.

        Accepts:

          * ``'x'``
          * ``'y'``
          * ``'xy'``

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['x', 'y', 'xy']:
                raise errors.HighchartsValueError(f'Panning.type expects a value of '
                                                  f'either "x", "y", "xy", or None. '
                                                  f'Received: {value}')
            self._type = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'type': as_dict.get('type', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'enabled': self.enabled,
            'type': self.type
        }


class ChartOptions(HighchartsMeta):
    """Configuration settings that apply to a chart."""

    def __init__(self, **kwargs):
        self._align_thresholds = None
        self._align_ticks = None
        self._allow_mutating_data = None
        self._animation = None
        self._background_color = None
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._class_name = None
        self._color_count = None
        self._display_errors = None
        self._events = None
        self._height = None
        self._ignore_hidden_series = None
        self._inverted = None
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
        self._plot_background_color = None
        self._plot_background_image = None
        self._plot_border_color = None
        self._plot_border_width = None
        self._plot_shadow = None
        self._polar = None
        self._reflow = None
        self._render_to = None
        self._scrollable_plot_area = None
        self._selection_marker_fill = None
        self._shadow = None
        self._show_axes = None
        self._spacing_bottom = None
        self._spacing_left = None
        self._spacing_top = None
        self._spacing_right = None
        self._style = None
        self._styled_mode = None
        self._type = None
        self._width = None
        self._zooming = None

        self.align_thresholds = kwargs.get('align_thresholds', None)
        self.align_ticks = kwargs.get('align_ticks', None)
        self.allow_mutating_data = kwargs.get('allow_mutating_data', None)
        self.animation = kwargs.get('animation', None)
        self.background_color = kwargs.get('background_color', None)
        self.border_color = kwargs.get('border_color', None)
        self.border_radius = kwargs.get('border_radius', None)
        self.border_width = kwargs.get('border_width', None)
        self.class_name = kwargs.get('class_name', None)
        self.color_count = kwargs.get('color_count', None)
        self.display_errors = kwargs.get('display_errors', None)
        self.events = kwargs.get('events', None)
        self.height = kwargs.get('height', None)
        self.ignore_hidden_series = kwargs.get('ignore_hidden_series', None)
        self.inverted = kwargs.get('inverted', None)
        self.margin = kwargs.get('margin', None)
        if not kwargs.get('margin', None):
            self.margin_bottom = kwargs.get('margin_bottom', None)
            self.margin_left = kwargs.get('margin_left', None)
            self.margin_right = kwargs.get('margin_right', None)
            self.margin_top = kwargs.get('margin_top', None)
        self.number_formatter = kwargs.get('number_formatter', None)
        self.options_3d = kwargs.get('options_3d', None)
        self.pan_key = kwargs.get('pan_key', None)
        self.panning = kwargs.get('panning', None)
        self.parallel_axes = kwargs.get('parallel_axes', None)
        self.parallel_coordinates = kwargs.get('parallel_coordinates', None)
        self.plot_background_color = kwargs.get('plot_background_color', None)
        self.plot_background_image = kwargs.get('plot_background_image', None)
        self.plot_border_color = kwargs.get('plot_border_color', None)
        self.plot_border_width = kwargs.get('plot_border_width', None)
        self.plot_shadow = kwargs.get('plot_shadow', None)
        self.polar = kwargs.get('polar', None)
        self.reflow = kwargs.get('reflow', None)
        self.render_to = kwargs.get('render_to', None)
        self.scrollable_plot_area = kwargs.get('scrollable_plot_area', None)
        self.selection_marker_fill = kwargs.get('selection_marker_fill', None)
        self.shadow = kwargs.get('shadow', None)
        self.show_axes = kwargs.get('show_axes', None)
        self.spacing = kwargs.get('spacing', None)
        if not kwargs.get('spacing', None):
            self.spacing_bottom = kwargs.get('spacing_bottom', None)
            self.spacing_left = kwargs.get('spacing_left', None)
            self.spacing_top = kwargs.get('spacing_top', None)
            self.spacing_right = kwargs.get('spacing_right', None)
        self.style = kwargs.get('style', None)
        self.styled_mode = kwargs.get('styled_mode', None)
        self.type = kwargs.get('type', None)
        self.width = kwargs.get('width', None)
        self.zooming = kwargs.get('zooming', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'chart'

    @property
    def align_thresholds(self) -> Optional[bool]:
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
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._align_thresholds

    @align_thresholds.setter
    def align_thresholds(self, value):
        if value is None:
            self._align_thresholds = None
        else:
            self._align_thresholds = bool(value)

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
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._align_ticks

    @align_ticks.setter
    def align_ticks(self, value):
        if value is None:
            self._align_ticks = None
        else:
            self._align_ticks = bool(value)

    @property
    def allow_mutating_data(self) -> Optional[bool]:
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
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_mutating_data

    @allow_mutating_data.setter
    def allow_mutating_data(self, value):
        if value is None:
            self._allow_mutating_data = None
        else:
            self._allow_mutating_data = bool(value)

    @property
    def animation(self) -> Optional[bool | AnimationOptions]:
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
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or gradient for the outer chart area. Defaults to
        ``'#ffffff'``.

        :returns: The background color for the outer chart area.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        from highcharts_core import utility_functions
        self._background_color = utility_functions.validate_color(value)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the outer chart border. Defaults to
        ``'#335cad'``.

        :returns: The color of the outer chart border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The border radius (in pixels) applied to the outer chart border. Defaults to
        ``0``.

        :returns: The border radius to apply to the outer chart border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width (in pixels) applied to the outer chart border. Defaults to
        ``0``.

        :returns: The border width to apply to the outer chart border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color_count(self) -> Optional[int]:
        """In styled mode, sets how many colors the class names should rotate between.
        Defaults to ``10``

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
    def display_errors(self) -> Optional[bool]:
        """If ``True``, will display errors on the chart itself. If ``False``, will only
        report errors to the console. Defaults to ``True``.

        :returns: Flag indicating whether ot display errors on the chart.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._display_errors

    @display_errors.setter
    def display_errors(self, value):
        if value is None:
            self._display_errors = None
        else:
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
    def height(self) -> Optional[constants.EnforcedNullType | int | float | Decimal | str]:
        """An explicit height for the chart. Defaults to :obj:`None <python:None>`.

        If a number, the height is given in pixels. If given a percentage string (for
        example ``'56%'``), the height is given as the percentage of the actual chart
        width. This allows for preserving the aspect ratio across responsive sizes.

        By default (when :obj:`None python:None>`) the height is calculated from the
        offset height of the containing element, or 400 pixels if the containing element's
        height is 0.

        :rtype: :class:`EnforcedNullType` or numeric or :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        if value is None or isinstance(value, constants.EnforcedNullType):
            self._height = None
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
    def ignore_hidden_series(self) -> Optional[bool]:
        """If ``True``, the axes will scale to the remaining visible series once one
        series is hidden. If ``False``, hiding and showing a series will not affect the
        axes or the other series.

        Defaults to ``True``.

        .. note::

          For stacks, once one series within the stack is hidden, the rest of the stack
          will close in around it even if the axis is not affected.

        :returns: Flag indicating whether to ignore hidden series.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._ignore_hidden_series

    @ignore_hidden_series.setter
    def ignore_hidden_series(self, value):
        if value is None:
            self._ignore_hidden_series = None
        else:
            self._ignore_hidden_series = bool(value)

    @property
    def inverted(self) -> Optional[bool]:
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
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._inverted

    @inverted.setter
    def inverted(self, value):
        if value is None:
            self._inverted = None
        else:
            self._inverted = bool(value)

    @property
    def margin(self) -> Optional[List[int | float | Decimal]]:
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
    def margin_bottom(self) -> Optional[int | float | Decimal]:
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
    def margin_left(self) -> Optional[int | float | Decimal]:
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
    def margin_right(self) -> Optional[int | float | Decimal]:
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
    def margin_top(self) -> Optional[int | float | Decimal]:
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
    def number_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript Callback function to override the default function that formats all
        the numbers in the chart. Returns a string with the formatted number.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._number_formatter

    @number_formatter.setter
    @class_sensitive(CallbackFunction)
    def number_formatter(self, value):
        self._number_formatter = value

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
    def panning(self, value):
        if value is None:
            self._panning = None
        else:
            if isinstance(value, bool):
                value = {
                    'enabled': value
                }
            value = validate_types(value, types = PanningOptions)
            
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
    def parallel_coordinates(self) -> Optional[bool]:
        """If ``True``, renders charts as a parallel coordinates plot. Defaults to
        ``False``.

        In a parallel coordinates plot (||-coords) by default all required Y-axes are
        generated and the legend is disabled.

        .. note::

          This feature requires the JavaScript module ``modules/parallel-coordinates.js``.

        .. seealso::

          * `Parallel Coordinates Demo <https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples//highcharts/demo/parallel-coordinates/>`_

        :returns: Flag indicating whether the chart is a parallel coordinates plot.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._parallel_coordinates

    @parallel_coordinates.setter
    def parallel_coordinates(self, value):
        if value is None:
            self._parallel_coordinates = None
        else:
            self._parallel_coordinates = bool(value)

    @property
    def plot_background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or gradient for the plot area. Defaults to
        ``None``.

        :returns: The background color for the plot area.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._plot_background_color

    @plot_background_color.setter
    def plot_background_color(self, value):
        from highcharts_core import utility_functions
        self._plot_background_color = utility_functions.validate_color(value)

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
            self._plot_background_image = None
        else:
            try:
                self._plot_background_image = validators.url(value)
            except ValueError:
                try:
                    self._plot_background_image = validators.path(value)
                except ValueError:
                    raise errors.HighchartsValueError(f'value provided ({value}) not a '
                                                      f'valid URL or path')

    @property
    def plot_border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the outer chart border. Defaults to
        ``'#cccccc'``.

        :returns: The color of the outer chart border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._plot_border_color

    @plot_border_color.setter
    def plot_border_color(self, value):
        from highcharts_core import utility_functions
        self._plot_border_color = utility_functions.validate_color(value)

    @property
    def plot_border_width(self) -> Optional[int | float | Decimal]:
        """The border width (in pixels) applied to the outer chart border. Defaults to
        ``0``.

        :returns: The border width to apply to the outer chart border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._plot_border_width

    @plot_border_width.setter
    def plot_border_width(self, value):
        self._plot_border_width = validators.numeric(value, allow_empty = True)

    @property
    def plot_shadow(self) -> Optional[bool | ShadowOptions]:
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
        if value is None:
            self._plot_shadow = None
        elif value is False:
            self._plot_shadow = False
        else:
            value = validate_types(value,
                                   types = ShadowOptions,
                                   allow_none = False)
            self._plot_shadow = value

    @property
    def polar(self) -> Optional[bool]:
        """If ``True``, cartesian charts like line, spline, area, and column are
        transformed into the polar coordinate system. This produces polar charts (also
        known as radar charts). Defaults to ``False``.

        :returns: Flag indicating whether to render the chart as a polar chart.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._polar

    @polar.setter
    def polar(self, value):
        if value is None:
            self._polar = None
        else:
            self._polar = bool(value)

    @property
    def reflow(self) -> Optional[bool]:
        """If ``True``, reflows the chart to fit the width of the container ``div`` when
        the window is resized. Defaults to ``True``.

        :returns: Flag indicating whether to reflow the chart in response to window
          resizing.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._reflow

    @reflow.setter
    def reflow(self, value):
        if value is None:
            self._reflow = None
        else:
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
    def selection_marker_fill(self) -> Optional[str | Gradient | Pattern]:
        """The background color or the marker square when selecting (zooming in on) an
        area of the chart. Defaults to
        ``'rgba(51,92,173,0.25)'``.

        :returns: The backgorund color of the marker square when selecting an area of the
          chart.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._selection_marker_fill

    @selection_marker_fill.setter
    def selection_marker_fill(self, value):
        self._selection_marker_fill = utility_functions.validate_color(value)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
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
        if value is None:
            self._shadow = None
        elif value is False:
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
    def spacing(self) -> Optional[List[int | float | Decimal]]:
        """The distance between the outer edge of the chart and the content, like title
        or legend, or axis title and labels if present. The numbers in the array designate
        top, right, bottom and left respectively.

        By default, ``[10,10,15,10]``.

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
                raise errors.HighchartsValueError(f'spacing expects either a single value'
                                                  f' or an iterable of four values. '
                                                  f'Received an iterable of {len(value)} '
                                                  f'values ({value})')
            value = [validators.numeric(x) for x in value]
            self.spacing_top = value[0]
            self.spacing_right = value[1]
            self.spacing_bottom = value[2]
            self.spacing_left = value[3]
        else:
            value = validators.numeric(value, allow_empty = False)
            self.spacing_top = value
            self.spacing_right = value
            self.spacing_bottom = value
            self.spacing_left = value

    @property
    def spacing_bottom(self) -> Optional[int | float | Decimal]:
        """The spacing between the bottom edge of the chart and the content (plot area,
        axis title and labels, title, subtitle or legend in top position).

        By default, ``15``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_bottom

    @spacing_bottom.setter
    def spacing_bottom(self, value):
        self._spacing_bottom = validators.numeric(value, allow_empty = True)

    @property
    def spacing_left(self) -> Optional[int | float | Decimal]:
        """The spacing between the left edge of the chart and the content (plot area,
        axis title and labels, title, subtitle or legend in top position).

        Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_left

    @spacing_left.setter
    def spacing_left(self, value):
        self._spacing_left = validators.numeric(value, allow_empty = True)

    @property
    def spacing_right(self) -> Optional[int | float | Decimal]:
        """The spacing between the right edge of the chart and the content (plot area,
        axis title and labels, title, subtitle or legend in top position).

        Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_right

    @spacing_right.setter
    def spacing_right(self, value):
        self._spacing_right = validators.numeric(value, allow_empty = True)

    @property
    def spacing_top(self) -> Optional[int | float | Decimal]:
        """The spacing between the top edge of the chart and the content (plot area, axis
        title and labels, title, subtitle or legend in top position).

        Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._spacing_top

    @spacing_top.setter
    def spacing_top(self, value):
        self._spacing_top = validators.numeric(value, allow_empty = True)

    @property
    def style(self) -> Optional[str | dict]:
        """Additional CSS styles to apply inline to the container div.

        Defaults to ``'{"fontFamily": "\"Lucida Grande\", \"Lucida Sans Unicode\", Verdana, Arial, Helvetica, sans-serif","fontSize":"12px"}'``.

        .. note::

          Since the default font styles are applied in the renderer, it is ignorant of the
          individual chart options and must be set globally.

        :rtype: :class:`str <python:str>` or :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        try:
            self._style = validators.dict(value, allow_empty = True)
        except (ValueError, TypeError):
            self._style = validators.string(value, 
                                            allow_empty = True,
                                            coerce_value = True)

    @property
    def styled_mode(self) -> Optional[bool]:
        """If ``True``, sets the chart to operate in **styled mode**, where no
        presentational attributes or CSS are applied to the chart SVG. Instead, CSS rules
        are required to style the chart. Defaults to ``False``.

        .. seealso::

          * `Available CSS Styles and Variables <https://www.highcharts.com/docs/chart-design-and-style/style-by-css>`__.
          * The Default Style Sheet:
            `https://code.highcharts.com/css/highcharts.css <https://code.highcharts.com/css/highcharts.css>`_.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._styled_mode

    @styled_mode.setter
    def styled_mode(self, value):
        if value is None:
            self._styled_mode = None
        else:
            self._styled_mode = bool(value)

    @property
    def type(self) -> Optional[str]:
        """The default series type for the chart. Defaults to ``'line'``.

        Can be any of the chart types listed under :class:`PlotOptions` and
        :class:`Series`, or can be a series provided by an additional module.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = validators.string(value, allow_empty = True)

    @property
    def width(self) -> Optional[constants.EnforcedNullType | int | float | Decimal | str]:
        """An explicit width for the chart.

        Defaults to :class:`EnforcedNull <EnforcedNullType>`` which indicates
        a JavaScript value of ``null`` (as opposed to :obj:`None <python:None>` which
        results in ``undefined`` when converted JavaScript.)

        If a number, the width is given in pixels. If given a percentage string (for
        example ``'56%'``), the width is given as the percentage of the actual chart
        width. This allows for preserving the aspect ratio across responsive sizes.

        By default (when null) the width is calculated from the offset width of the
        containing element.

        :rtype: :class:`EnforcedNullType` or numeric or :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        if value is None:
            self._width = None
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
    def zooming(self) -> Optional[ZoomingOptions]:
        """Chart zooming configuration.

        :rtype: :class:`ZoomingOptions <highcharts_maps.options.chart.zooming.ZoomingOptions>`
          or :obj:`None <python:None>`
        """
        return self._zooming

    @zooming.setter
    @class_sensitive(ZoomingOptions)
    def zooming(self, value):
        self._zooming = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align_thresholds': as_dict.get('alignThresholds', None),
            'align_ticks': as_dict.get('alignTicks', None),
            'allow_mutating_data': as_dict.get('allowMutatingData', None),
            'animation': as_dict.get('animation', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color_count': as_dict.get('colorCount', None),
            'display_errors': as_dict.get('displayErrors', None),
            'events': as_dict.get('events', None),
            'height': as_dict.get('height', None),
            'ignore_hidden_series': as_dict.get('ignoreHiddenSeries', None),
            'inverted': as_dict.get('inverted', None),
            'margin': as_dict.get('margin', None),
            'margin_bottom': as_dict.get('marginBottom', None),
            'margin_left': as_dict.get('marginLeft', None),
            'margin_right': as_dict.get('marginRight', None),
            'margin_top': as_dict.get('marginTop', None),
            'number_formatter': as_dict.get('numberFormatter', None),
            'options_3d': as_dict.get('options3d', None),
            'pan_key': as_dict.get('panKey', None),
            'panning': as_dict.get('panning', None),
            'parallel_axes': as_dict.get('parallelAxes', None),
            'parallel_coordinates': as_dict.get('parallelCoordinates', None),
            'plot_background_color': as_dict.get('plotBackgroundColor', None),
            'plot_background_image': as_dict.get('plotBackgroundImage', None),
            'plot_border_color': as_dict.get('plotBorderColor', None),
            'plot_border_width': as_dict.get('plotBorderWidth', None),
            'plot_shadow': as_dict.get('plotShadow', None),
            'polar': as_dict.get('polar', None),
            'reflow': as_dict.get('reflow', None),
            'render_to': as_dict.get('renderTo', None),
            'scrollable_plot_area': as_dict.get('scrollablePlotArea', None),
            'selection_marker_fill': as_dict.get('selectionMarkerFill', None),
            'shadow': as_dict.get('shadow', None),
            'show_axes': as_dict.get('showAxes', None),
            'spacing': as_dict.get('spacing', None),
            'spacing_bottom': as_dict.get('spacingBottom', None),
            'spacing_left': as_dict.get('spacingLeft', None),
            'spacing_top': as_dict.get('spacingTop', None),
            'spacing_right': as_dict.get('spacingRight', None),
            'style': as_dict.get('style', None),
            'styled_mode': as_dict.get('styledMode', None),
            'type': as_dict.get('type', None),
            'width': as_dict.get('width', None),
            'zooming': as_dict.get('zooming', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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
            'plotBackgroundColor': self.plot_background_color,
            'plotBackgroundImage': self.plot_background_image,
            'plotBorderColor': self.plot_border_color,
            'plotBorderWidth': self.plot_border_width,
            'plotShadow': self.plot_shadow,
            'polar': self.polar,
            'reflow': self.reflow,
            'renderTo': self.render_to,
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
            'zooming': self.zooming,
        }

        return untrimmed
