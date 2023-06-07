from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_core.options.plot_options.accessibility import TypeOptionsAccessibility
from highcharts_core.options.series.labels import SeriesLabel
from highcharts_core.options.plot_options.points import OnPointOptions
from highcharts_core.options.plot_options.points import Point
from highcharts_core.options.plot_options.sonification import SeriesSonification
from highcharts_core.options.tooltips import Tooltip
from highcharts_core.utility_classes.animation import AnimationOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.data_labels import DataLabel
from highcharts_core.utility_classes.events import SeriesEvents
from highcharts_core.utility_classes.markers import Marker
from highcharts_core.utility_classes.states import States
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class GenericTypeOptions(HighchartsMeta):
    """Generic class that is used as a base class for type-specific :class:`PlotOptions`.
    """

    def __init__(self, **kwargs):
        self._accessibility = None
        self._allow_point_select = None
        self._animation = None
        self._class_name = None
        self._clip = None
        self._color = None
        self._cursor = None
        self._custom = None
        self._dash_style = None
        self._data_labels = None
        self._description = None
        self._enable_mouse_tracking = None
        self._events = None
        self._include_in_data_export = None
        self._keys = None
        self._label = None
        self._legned_symbol = None
        self._linked_to = None
        self._marker = None
        self._on_point = None
        self._opacity = None
        self._point = None
        self._point_description_formatter = None
        self._selected = None
        self._show_checkbox = None
        self._show_in_legend = None
        self._skip_keyboard_navigation = None
        self._sonification = None
        self._states = None
        self._sticky_tracking = None
        self._threshold = None
        self._tooltip = None
        self._turbo_threshold = None
        self._visible = None

        self.accessibility = kwargs.get('accessibility', None)
        self.allow_point_select = kwargs.get('allow_point_select', None)
        self.animation = kwargs.get('animation', None)
        self.class_name = kwargs.get('class_name', None)
        self.clip = kwargs.get('clip', None)
        self.color = kwargs.get('color', None)
        self.cursor = kwargs.get('cursor', None)
        self.custom = kwargs.get('custom', None)
        self.dash_style = kwargs.get('dash_style', None)
        self.data_labels = kwargs.get('data_labels', None)
        self.description = kwargs.get('description', None)
        self.enable_mouse_tracking = kwargs.get('enable_mouse_tracking', None)
        self.events = kwargs.get('events', None)
        self.include_in_data_export = kwargs.get('include_in_data_export', None)
        self.keys = kwargs.get('keys', None)
        self.label = kwargs.get('label', None)
        self.legend_symbol = kwargs.get('legend_symbol', None)
        self.linked_to = kwargs.get('linked_to', None)
        self.marker = kwargs.get('marker', None)
        self.on_point = kwargs.get('on_point', None)
        self.opacity = kwargs.get('opacity', None)
        self.point = kwargs.get('point', None)
        self.point_description_formatter = kwargs.get('point_description_formatter', None)
        self.selected = kwargs.get('selected', None)
        self.show_checkbox = kwargs.get('show_checkbox', None)
        self.show_in_legend = kwargs.get('show_in_legend', None)
        self.skip_keyboard_navigation = kwargs.get('skip_keyboard_navigation', None)
        self.sonification = kwargs.get('sonification', None)
        self.states = kwargs.get('states', None)
        self.sticky_tracking = kwargs.get('sticky_tracking', None)
        self.threshold = kwargs.get('threshold', None)
        self.tooltip = kwargs.get('tooltip', None)
        self.turbo_threshold = kwargs.get('turbo_threshold', None)
        self.visible = kwargs.get('visible', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return f'plotOptions.{self.type}'

    @property
    def type(self) -> str:
        """Indicates the type of series that is represented by this instance.

        .. warning::

          This proprety is read-only!

        :rtype: :class:`str <python:str>`
        """
        class_name = self.__class__.__name__
        class_name = class_name.replace('TypeOptions', '')
        class_name = class_name.replace('Options', '')
        if class_name.endswith('Series') and class_name != 'Series':
            class_name = class_name.replace('Series', '')

        return class_name.lower()

    @type.setter
    def type(self, value):
        raise errors.HighchartsReadOnlyError('type is a read-only property and cannot be '
                                             'set manually')

    @property
    def accessibility(self) -> Optional[TypeOptionsAccessibility]:
        """Accessibility options for a series.

        :rtype: :class:`TypeOptionsAccessibility` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(TypeOptionsAccessibility)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def allow_point_select(self) -> Optional[bool]:
        """Allow this series' points to be selected by clicking on the graphic (columns,
        point markers, pie slices, map areas etc).

        The selected points can be handled in JavaScript by point select and unselect
        events, or collectively by the (JavaScript) ``getSelectedPoints()`` function.

        And alternative way of selecting points is through dragging.

        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_point_select

    @allow_point_select.setter
    def allow_point_select(self, value):
        if value is None:
            self._allow_point_select = None
        else:
            self._allow_point_select = bool(value)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Enable or disable the initial animation when a series is displayed.

        The animation can also be set as a configuration object. Please note that this
        option only applies to the initial animation of the series itself. For other
        animations, see :class:`Chart.animation` and the ``animation`` parameter under the
        (JavaScript) API methods. The following properties are supported:

          * ``defer``: The animation delay time in milliseconds.
          * ``duration``: The duration of the animation in milliseconds.
          * ``easing``: Can be a string reference to an easing function set on the Math
            object or a function.

        .. warning::

          Due to poor performance, animation is disabled in old IE browsers for several
          chart types.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def class_name(self) -> Optional[str]:
        """The additional CSS class name to apply to the series' graphical elements.

        .. note::

          This option is additive to the default class names - it does not replace them.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def clip(self) -> Optional[bool]:
        """If ``False``, allows the series to be rendered in the entire plot area. If
        ``True``, constrains where the series can be rendered within the plot area.
        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._clip

    @clip.setter
    def clip(self, value):
        if value is None:
            self._clip = None
        else:
            self._clip = bool(value)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The main color of the series.

        In line type series it applies to the line and the point markers unless otherwise
        specified. In bar type series it applies to the bars unless a color is specified
        per point. The default value is pulled from the :meth:`Options.colors` array.

        :returns: The main color applied to the series.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def cursor(self) -> Optional[str]:
        """The style of cursor to use when the user's mouse hovers over the data series.

        Acceptable values are:

          * ``'alias'``
          * ``'all-scroll'``
          * ``'auto'``
          * ``'cell'``
          * ``'col-resize'``
          * ``'context-menu'``
          * ``'copy'``
          * ``'crosshair'``
          * ``'default'``
          * ``'e-resize'``
          * ``'ew-resize'``
          * ``'grab'``
          * ``'grabbing'``
          * ``'help'``
          * ``'move'``
          * ``'n-resize'``
          * ``'ne-resize'``
          * ``'nesw-resize'``
          * ``'no-drop'``
          * ``'none'``
          * ``'not-allowed'``
          * ``'ns-resize'``
          * ``'nw-resize'``
          * ``'nwse-resize'``
          * ``'pointer'``
          * ``'progress'``
          * ``'row-resize'``
          * ``'s-resize'``
          * ``'se-resize'``
          * ``'sw-resize'``
          * ``'text'``
          * ``'vertical-text'``
          * ``'w-resize'``
          * ``'wait'``
          * ``'zoom-in'``
          * ``'zoom-out'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        if not value:
            self._cursor = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.SUPPORTED_CURSOR_VALUES:
                raise errors.HighchartsValueError(f'cursor expects a valid cursor value. '
                                                  f'Received: {value}')
            self._cursor = value

    @property
    def custom(self) -> Optional[JavaScriptDict]:
        """A reserved subspace to store options and values for customized functionality.

        Here you can add additional data for your own event callbacks and formatter
        callbacks.

        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._custom

    @custom.setter
    @class_sensitive(JavaScriptDict)
    def custom(self, value):
        self._custom = value

    @property
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the graph, or for some series types the
        outline of each shape.

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
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        if not value:
            self._dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'dash_style expects a recognized value'
                                                  f', but received: {value}')
            self._dash_style = value

    @property
    def data_labels(self) -> Optional[DataLabel | List[DataLabel]]:
        """Options for the series data labels, appearing next to each data point.

        .. note::

          To have multiple data labels per data point, you can also supply a collection of
          :class:`DataLabel` configuration settings.

        :rtype: :class:`DataLabel`, :class:`list <python:list>` of :class:`DataLabel`, or
          :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    def data_labels(self, value):
        if not value:
            self._data_labels = None
        else:
            if checkers.is_iterable(value):
                self._data_labels = validate_types(value,
                                                   types = DataLabel,
                                                   allow_none = False,
                                                   force_iterable = True)
            else:
                self._data_labels = validate_types(value,
                                                   types = DataLabel,
                                                   allow_none = False)

    @property
    def description(self) -> Optional[str]:
        """A description of the series to add to the screen reader information about the
        series.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def enable_mouse_tracking(self) -> Optional[bool]:
        """If ``True``, enables mouse tracking for the series (used to capture point
        tooltips, click events on graphs and points, etc.). If ``False``, disables
        mouse tracking for the series (which can help performance). Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enable_mouse_tracking

    @enable_mouse_tracking.setter
    def enable_mouse_tracking(self, value):
        if value is None:
            self._enable_mouse_tracking = None
        else:
            self._enable_mouse_tracking = bool(value)

    @property
    def events(self) -> Optional[SeriesEvents]:
        """General event handlers for the series items.

        .. note::

          These event hooks can also be attached to the series at run time using the
          (JavaScript) ``Highcharts.addEvent()`` function.

        :rtype: :class:`SeriesEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(SeriesEvents)
    def events(self, value):
        self._events = value

    @property
    def include_in_data_export(self) -> Optional[bool]:
        """If ``False``, will prevent the data series from being included in any form of
        data export. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._include_in_data_export

    @include_in_data_export.setter
    def include_in_data_export(self, value):
        if value is None:
            self._include_in_data_export = None
        else:
            self._include_in_data_export = bool(value)

    @property
    def keys(self) -> Optional[List[str]]:
        """An array specifying which option maps to which key in the data point array.

        This makes it convenient to work with unstructured data arrays from different
        sources.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._keys

    @keys.setter
    def keys(self, value):
        if not value:
            self._keys = None
        else:
            self._keys = [validators.string(x)
                          for x in validators.iterable(value)]

    @property
    def label(self) -> Optional[SeriesLabel]:
        """Series labels are placed as close to the series as possible in a natural way,
        seeking to avoid other series. The goal of this feature is to make the chart more
        easily readable, like if a human designer placed the labels in the optimal
        position.

        .. note::

          The series labels currently work with series types having a graph or an area.

        :rtype: :class:`SeriesLabel` or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(SeriesLabel)
    def label(self, value):
        self._label = value

    @property
    def legend_symbol(self) -> Optional[str]:
        """The type of legend symbol to render for the series. Accepts either 
        ``'lineMarker'`` or ``'rectangle'``. Defaults to ``'rectangle'``.
        
        :rtype: :class:`str <python:str>`
        """
        return self._legend_symbol
    
    @legend_symbol.setter
    def legend_symbol(self, value):
        if not value:
            self._legend_symbol = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value == 'linemarker':
                value = 'lineMarker'
            if value not in ['lineMarker', 'rectangle']:
                raise errors.HighchartsValueError(f'legend_symbol expects either '
                                                  f'"lineMarker" or "rectangle". '
                                                  f'Received: "{value}".')
            self._legend_symbol = value

    @property
    def linked_to(self) -> Optional[str]:
        """The id of another series to link to.

        .. hint::

          The value can be ``':previous'`` to link to the previous series. When two series
          are linked, only the first one appears in the legend. Toggling the visibility of
          this also toggles the linked series.

        .. note::

          If the master series uses data sorting and linked series does not have its own
          sorting definition, the linked series will be sorted in the same order as the
          master one.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._linked_to

    @linked_to.setter
    def linked_to(self, value):
        self._linked_to = validators.string(value, allow_empty = True)

    @property
    def marker(self) -> Optional[Marker]:
        """Options for the point markers of line-like series.

        Properties like ``fill_color``, ``line_color`` and ``line_width`` define the
        visual appearance of the markers. Other series types, like column series, don't
        have markers, but have visual options on the series level instead.

        :rtype: :class:`Marker` or :obj:`None <python:None>`
        """
        return self._marker

    @marker.setter
    @class_sensitive(Marker)
    def marker(self, value):
        self._marker = value

    @property
    def on_point(self) -> Optional[OnPointOptions]:
        """Options for the Series on point feature, which is currently only supported by
        ``pie`` and ``sunburst`` chargs.

        :rtype: :class:`OnPointOptions` or :obj:`None <python:None>`
        """
        return self._on_point

    @on_point.setter
    @class_sensitive(OnPointOptions)
    def on_point(self, value):
        self._on_point = value

    @property
    def opacity(self) -> Optional[float]:
        """Opacity of a series parts: line, fill (e.g. area), and labels.

        :rtype: :class:`float <python:float>`
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.float(value,
                                         allow_empty = True,
                                         minimum = 0.0,
                                         maximum = 1.0)

    @property
    def point(self) -> Optional[Point]:
        """Properties for each single point.

        :rtype: :class:`Point` or :obj:`None <python:None>`
        """
        return self._point

    @point.setter
    @class_sensitive(Point)
    def point(self, value):
        self._point = value

    @property
    def point_description_formatter(self) -> Optional[CallbackFunction]:
        """Same as for :meth:`Accessibility.series.description_formatter`, only for an
        individual series. Overrides the chart-wide configuration.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._point_description_formatter

    @point_description_formatter.setter
    @class_sensitive(CallbackFunction)
    def point_description_formatter(self, value):
        self._point_description_formatter = value

    @property
    def selected(self) -> Optional[bool]:
        """If ``True``, the series is selected initially (by default, without user
        interaction). Defaults to ``False``.

        .. note::

          If :meth:`GenericTypeOptions.show_checkbox` is ``True``, then the checkbox
          will be checked if ``selected`` is ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._selected

    @selected.setter
    def selected(self, value):
        if value is None:
            self._selected = None
        else:
            self._selected = bool(value)

    @property
    def show_checkbox(self) -> Optional[bool]:
        """If ``True``, a checkbox is displayed next to the legend item to allow selecting
        the series.

        .. note::

          The state of the checkbox is controlled by the
          :meth:`GenericTypeOptions.selected` property.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_checkbox

    @show_checkbox.setter
    def show_checkbox(self, value):
        if value is None:
            self._show_checkbox = None
        else:
            self._show_checkbox = bool(value)

    @property
    def show_in_legend(self) -> Optional[bool]:
        """Whether to display this particular series or series type in the legend.
        Standalone series are shown in the legend by default, and linked series are not.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_in_legend

    @show_in_legend.setter
    def show_in_legend(self, value):
        if value is None:
            self._show_in_legend = None
        else:
            self._show_in_legend = bool(value)

    @property
    def skip_keyboard_navigation(self) -> Optional[bool]:
        """If ``True``, the accessibility module will skip past this series when executing
        keyboard navigation.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._skip_keyboard_navigation

    @skip_keyboard_navigation.setter
    def skip_keyboard_navigation(self, value):
        if value is None:
            self._skip_keyboard_navigation = None
        else:
            self._skip_keyboard_navigation = bool(value)

    @property
    def sonification(self) -> Optional[SeriesSonification]:
        """Sonification configuration for the series type/series.
        
        :rtype: :class:`SeriesSonification <highcharts_core.options.plot_options.sonification.SeriesSonification>` or
          :obj:`None <python:None>`
        """
        return self._sonification
    
    @sonification.setter
    @class_sensitive(SeriesSonification)
    def sonification(self, value):
        self._sonification = value

    @property
    def states(self) -> Optional[States]:
        """Configuration for state-specific configuration to apply to the data series.

        :rtype: :class:`States` or :obj:`None <python:None>`
        """
        return self._states

    @states.setter
    @class_sensitive(States)
    def states(self, value):
        self._states = value

    @property
    def sticky_tracking(self) -> Optional[bool]:
        """Sticky tracking of mouse events.

        When ``True``, the (JavaScript) ``mouseOut`` event on a series is not triggered
        until the mouse moves over another series, or out of the plot area.

        When ``False``, the (JavaScript) ``mouseOut`` event on a series is triggered when
        the mouse leaves the area around the series' graph or markers. This also implies
        the tooltip when not shared.

        When ``False`` and :meth:`PlotOptions.tooltip.shared` is also ``False``, the
        tooltip will be hidden when moving the mouse between series.

        Defaults to ``True`` for line and area type series, but to ``False`` for columns,
        pies, etc.

        .. note::

          The boost module will force this option because of technical limitations.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._sticky_tracking

    @sticky_tracking.setter
    def sticky_tracking(self, value):
        if value is None:
            self._sticky_tracking = None
        else:
            self._sticky_tracking = bool(value)

    @property
    def threshold(self) -> Optional[constants.EnforcedNullType | int | float | Decimal]:
        """The Y axis value to serve as the base for the columns, for distinguishing
        between values above and below a threshold. Defaults to ``0``.

        If :class:`EnforcedNullType`, the columns extend from the padding Y axis minimum.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        if value == constants.EnforcedNull:
            self._threshold = constants.EnforcedNull
        else:
            self._threshold = validators.numeric(value, allow_empty = True)

    @property
    def tooltip(self) -> Optional[Tooltip]:
        """A configuration object for the tooltip rendering of each single series.
        Properties are inherited from tooltip, but only the following properties can be
        defined on a series level.

        :rtype: :class:`Tooltip` or :obj:`None <python:None>`
        """
        return self._tooltip

    @tooltip.setter
    @class_sensitive(Tooltip)
    def tooltip(self, value):
        self._tooltip = value

    @property
    def turbo_threshold(self) -> Optional[int]:
        """When a series contains a data array longer than this value, only one
        dimensional arrays of numbers, or two dimensional arrays with x and y values are
        allowed. Also, only the first point is tested, and the rest are assumed to be the
        same format. This saves expensive data checking and indexing in long series.
        Set it to ``0`` or :obj:`None <python:None>` to disable.

        Defaults to ``1000``.

        .. note::

          In boost mode, turbo threshold is forced. Only array of numbers or two
          dimensional arrays are allowed.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._turbo_threshold

    @turbo_threshold.setter
    def turbo_threshold(self, value):
        self._turbo_threshold = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def visible(self) -> Optional[bool]:
        """If ``True``, the series is initially visible. If ``False``, the series is
        hidden by default. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is None:
            self._visible = None
        else:
            self._visible = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
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
            'visible': as_dict.get('visible', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'allowPointSelect': self.allow_point_select,
            'animation': self.animation,
            'className': self.class_name,
            'clip': self.clip,
            'color': self.color,
            'cursor': self.cursor,
            'custom': self.custom,
            'dashStyle': self.dash_style,
            'dataLabels': self.data_labels,
            'description': self.description,
            'enableMouseTracking': self.enable_mouse_tracking,
            'events': self.events,
            'includeInDataExport': self.include_in_data_export,
            'keys': self.keys,
            'label': self.label,
            'legendSymbol': self.legend_symbol,
            'linkedTo': self.linked_to,
            'marker': self.marker,
            'onPoint': self.on_point,
            'opacity': self.opacity,
            'point': self.point,
            'pointDescriptionFormatter': self.point_description_formatter,
            'selected': self.selected,
            'showCheckbox': self.show_checkbox,
            'showInLegend': self.show_in_legend,
            'skipKeyboardNavigation': self.skip_keyboard_navigation,
            'sonification': self.sonification,
            'states': self.states,
            'stickyTracking': self.sticky_tracking,
            'threshold': self.threshold,
            'tooltip': self.tooltip,
            'turboThreshold': self.turbo_threshold,
            'visible': self.visible,
            'type': self.type
        }

        return untrimmed
