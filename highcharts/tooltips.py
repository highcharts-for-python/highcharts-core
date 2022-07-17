from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.shadows import ShadowOptions
from highcharts.utility_classes.date_time_label_formats import DateTimeLabelFormats


class Tooltip(HighchartsMeta):
    """Options for the tooltip that appears when the user hovers over a series or
    point."""

    def __init__(self, **kwargs):
        self._animation = True
        self._background_color = None
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._class_name = None
        self._cluster_format = None
        self._date_time_label_formats = None
        self._distance = None
        self._enabled = True
        self._follow_pointer = False
        self._follow_touch_move = True
        self._footer_format = None
        self._formatter = None
        self._header_format = None
        self._header_shape = None
        self._hide_delay = None
        self._null_format = None
        self._null_formatter = None
        self._outside = None
        self._padding = None
        self._point_format = None
        self._point_formatter = None
        self._positioner = None
        self._shadow = True
        self._shape = None
        self._shared = False
        self._snap = None
        self._split = False
        self._stick_on_contact = False
        self._style = None
        self._use_html = False
        self._value_decimals = None
        self._value_prefix = None
        self._value_suffix = None
        self._x_date_format = None

        self.animation = kwargs.pop('animation', True)
        self.background_color = kwargs.pop('background_color', None)
        self.border_color = kwargs.pop('border_color', None)
        self.border_radius = kwargs.pop('border_radius',
                                        constants.DEFAULT_TOOLTIP.get('border_radius'))
        self.border_width = kwargs.pop('border_width',
                                       constants.DEFAULT_TOOLTIP.get('border_width'))
        self.class_name = kwargs.pop('class_name', None)
        self.cluster_format = kwargs.pop('cluster_format', None)
        self.date_time_label_formats = kwargs.pop('date_time_label_formats', None)
        self.distance = kwargs.pop('distance', constants.DEFAULT_TOOLTIP.get('distance'))
        self.enabled = kwargs.pop('enabled', True)
        self.follow_pointer = kwargs.pop('follow_pointer', False)
        self.follow_touch_move = kwargs.pop('follow_touch_move', True)
        self.footer_format = kwargs.pop('footer_format',
                                        constants.DEFAULT_TOOLTIP.get('footer_format'))
        self.formatter = kwargs.pop('formatter', None)
        self.header_format = kwargs.pop('header_format', None)
        self.header_shape = kwargs.pop('header_shape',
                                       constants.DEFAULT_TOOLTIP.get('header_shape'))
        self.hide_delay = kwargs.pop('hide_delay',
                                     constants.DEFAULT_TOOLTIP.get('hide_delay'))
        self.null_format = kwargs.pop('null_format', None)
        self.null_formatter = kwargs.pop('null_formatter', None)
        self.outside = kwargs.pop('outside', None)
        self.padding = kwargs.pop('padding', constants.DEFAULT_TOOLTIP.get('padding'))
        self.point_format = kwargs.pop('point_format', None)
        self.point_formatter = kwargs.pop('point_formatter', None)
        self.positioner = kwargs.pop('positioner', None)
        self.shadow = kwargs.pop('shadow', True)
        self.shape = kwargs.pop('shape', constants.DEFAULT_TOOLTIP.get('shape'))
        self.shared = kwargs.pop('shared', False)
        self.snap = kwargs.pop('snap', constants.DEFAULT_TOOLTIP.get('snap'))
        self.split = kwargs.pop('split', False)
        self.stick_on_contact = kwargs.pop('stick_on_contact', False)
        self.style = kwargs.pop('style', None)
        self.use_html = kwargs.pop('use_html', False)
        self.value_decimals = kwargs.pop('value_decimals', None)
        self.value_prefix = kwargs.pop('value_prefix', None)
        self.value_suffix = kwargs.pop('value_suffix', None)
        self.x_date_format = kwargs.pop('x_date_format', None)

    @property
    def animation(self) -> bool:
        """Flag which indicates whether animation is enabled on the toltip (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        self._animation = bool(value)

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The background color or gradient for the tooltip. Defaults to
        ``'{constants.DEFAULT_TOOLTIP.get('background_color', None)}'``.

        :returns: The backgorund color for the tooltip.
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
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the tooltip border.

        :returns: The color of the tooltip's border.
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
    def border_radius(self) -> Optional[int | float | Decimal | str]:
        f"""The border radius (in pixels) applied to
        the pane. Defaults to ``{constants.DEFAULT_TOOLTIP.get('border_radius')}``.

        :returns: The border radius of the tooltip.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        if value is None or value == '':
            self._border_radius = None
        else:
            try:
                self._border_radius = validators.string(value, allow_empty = True)
            except ValueError:
                self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        f"""The border width (in pixels) applied to the tooltip. Defaults to
        ``{constants.DEFAULT_TOOLTIP.get('border_width')}``.

        :returns: The border width to apply to the tooltip.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS. Defaults to :obj:`None <python:None>`.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def cluster_format(self) -> Optional[str]:
        """The HTML of the cluster point's in the tooltip.

        .. warning::

          Works only with ``marker-clusters`` module and analogously to
          :meth:`Tooltip.point_format`.

        .. note::

          The cluster tooltip can be also formatted using the :meth:`Tooltip.formatter`
          callback function and the :meth:`Point.is_cluster` flag.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cluster_format

    @cluster_format.setter
    def cluster_format(self, value):
        self._cluster_format = validators.string(value, allow_empty = True)

    @property
    def date_time_label_formats(self) -> Optional[DateTimeLabelFormats]:
        """For series on datetime axes, the date format in the tooltip's header will by
        default be guessed based on the closest data points. This property gives the
        default string representations used for each unit.

        Defaults to :obj:`None <python:None>`

        :rtype: :class:`DateTimeLabelFormats` or :obj:`None <python:None>`
        """
        return self._date_time_label_formats

    @date_time_label_formats.setter
    @class_sensitive(DateTimeLabelFormats)
    def date_time_label_formats(self, value):
        self._date_time_label_formats = value

    @property
    def distance(self) -> Optional[int | float | Decimal]:
        f"""The distance (in pixels) from the point to the tooltip. Defaults to
        ``{constants.DEFAULT_TOOLTIP.get('distance')}``.

        :returns: The distance from the point to the tooltip.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> bool:
        """If ``True``, enables the use of tooltips. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @property
    def follow_pointer(self) -> bool:
        """If ``True``, the tooltip will follow the mouse pointer as it moves across
        columns, pie slices, and other point types with an extent. Defaults to ``False``
        generally, except for pie, polygon, map, sankey, and wordcloud series types where
        the generic ``False`` is over-ridden by default.

        .. note::

          If :meth:`Tooltip.split` is ``True``, then this property is ignored.

        :rtype: :class:`bool <python:bool>`
        """
        return self._follow_pointer

    @follow_pointer.setter
    def follow_pointer(self, value):
        self._follow_pointer = bool(value)

    @property
    def follow_touch_move(self) -> bool:
        """If ``True``, the tooltip will follow the single finger touches on a touch base.
        Defaults to ``True``.

        .. note::

          If this is ``True`` and :meth:`Chart.panning` is set, this property will take
          over one-finger touch moves so the user will need to use two fingers for zooming
          and panning.

        .. note::

          There is a significant difference to behavior when compared to
          :meth:`Tooltip.follow_pointer`, which updates the *position* of the tooltip. For
          example, if :meth:`follow_pointer <Tooltip.follow_pointer>` is ``False`` for a
          column series, the tooltip will show above or below the column. However, when
          ``follow_touch_move`` is ``True``, the tooltip displayed will jump from column
          to column (above or below the column as applicable) as the user swipes across
          the plot area.

        :rtype: :class:`bool <python:bool>`
        """
        return self._follow_touch_move

    @follow_touch_move.setter
    def follow_touch_move(self, value):
        self._follow_touch_move = bool(value)

    @property
    def footer_format(self) -> Optional[str]:
        f"""A string to append to the tooltip format. Defaults to
        ``'{constants.DEFAULT_TOOLTIP.get('footer_format')}'`` (an empty string).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._footer_format

    @footer_format.setter
    def footer_format(self, value):
        if value == '':
            self._footer_format = value
        else:
            self._footer_format = validators.string(value, allow_empty = True)

    @property
    def formatter(self) -> Optional[str]:
        """JavaScript callback function to format the text of the tooltip from scratch.
        Defaults to :obj:`None <python:None>`

        In case of single or :meth:`shared <Tooltip.shared>`tooltips, a string should be
        returned. In case of :meth:`split <Tooltip.split>` tooltips, it should return an
        array where the first item is the header, and subsequent items are mapped to the
        points. Return ``false`` to disable the tooltip for a specific point on a series.

        .. note::

          A subset of HTML is supported. Unless :meth:`Tooltip.use_html` is ``True``, the
          HTML of the tooltip is parsed and converted to SVG, therefore this is *not* a
          complete HTML renderer. The following HTML tags are supported:
          ``b``, ``br``, ``em``, ``i``, ``span``, ``strong``.

          Spans can be styled with a ``style`` attribute, but only text-related CSS that
          is shared with SVG will be handled.

        .. note::

          The available data in the formatter differ a bit depending on whether the tooltip
          is shared, split, or belongs to a single point. In a shared/split tooltip, all
          properties except ``x``, which is common for all points, are kept in an array,
          ``this.points``.

          Available data are:

            * ``this.percentage`` (when not shared) / ``this.points[i].percentage``
              (when shared): Stacked series and pies only. The point's percentage of the
              total.
            * ``this.point`` (when not shared) / ``this.points[i].point`` (when shared):
              The point object. The point name, if defined, is available through
              ``this.point.name``.
            * ``this.points``: In a shared tooltip, this is an array containing all other
              properties for each point.
            * ``this.series`` (when not shared) / ``this.points[i].series`` (when shared):
              The series object. The series name is available through ``this.series.name``.
            * ``this.total`` (when not shared) / ``this.points[i].total`` (when shared):
              Stacked series only. The total value at this point's x value.
            * ``this.x``: The x value. This property is the same regardless of the tooltip
              being shared or not.
            * ``this.y`` (when not shared) / ``this.points[i].y`` (when shared): The y
              value.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    def formatter(self, value):
        self._formatter = validators.string(value, allow_empty = True)

    @property
    def header_format(self) -> Optional[str]:
        """The HTML of the tooltip header line. Defaults to :obj:`None <python:None>`.

        .. note::

          Variables are enclosed by curly brackets. Available variables are ``point.key``,
          ``series.name``, ``series.color``, and other members from the ``point`` and
          ``series`` objects.

          The ``point.key`` variable contains the category name, x value or datetime
          string depending on the type of axis. For datetime axes, the ``point.key`` date
          format can be set using :meth:`ToolTip.x_date_format`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._header_format

    @header_format.setter
    def header_format(self, value):
        self._header_format = validators.string(value, allow_empty = True)

    @property
    def header_shape(self) -> Optional[str]:
        f"""The name of a symbol to use for the border around the tooltip header.

        Defaults to ``'{constants.DEFAULT_TOOLTIP.get('header_shape')}'``.

        .. note::

          Applies only when :meth:`Tooltip.split` is enabled.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._header_shape

    @header_shape.setter
    def header_shape(self, value):
        if not value:
            self._header_shape = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['callout', 'circle', 'square']:
                raise errors.HighchartsValueError(f'shape expects a supported tooltip '
                                                  f'header shape. Was: {value}')
            self._header_shape = value

    @property
    def hide_delay(self) -> Optional[int]:
        """The number of milliseconds to wait until the tooltip is hidden when mouse out
        from a point or chart.

        Defaults to ``{constants.DEFAULT_TOOLTIP.get('hide_delay')}``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._hide_delay

    @hide_delay.setter
    def hide_delay(self, value):
        self._hide_delay = validators.integer(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def null_format(self) -> Optional[str]:
        """The HTML of the null point's line in the tooltip. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Works analogously to :meth:`Tooltip.point_format`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._null_format

    @null_format.setter
    def null_format(self, value):
        self._null_format = validators.string(value, allow_empty = True)

    @property
    def null_formatter(self) -> Optional[str]:
        """JavaScript callback function to format the text of the tooltip for visible null
        points.

        .. note::

          Works analogously to :meth:`Tooltip.formatter`.

        :rtype: :class:`str <python:None>` or :obj:`None <python:None>`
        """
        return self._null_formatter

    @null_formatter.setter
    def null_formatter(self, value):
        self._null_formatter = validators.string(value, allow_empty = True)

    @property
    def outside(self) -> Optional[bool]:
        """If ``True``, allows the tooltip to render outside of the chart's SVG element
        box. Defaults to ``False``, which causes the tooltip to be rendered inside the
        SVG element box which results in the tooltip being rendered inside the chart area.


        .. warning::

          When setting this property to ``False`` (the default) on small charts, the
          tooltip may either clip or overlap parts of the chart itself.

        When ``True``, a separate SVG element is created and overlaid on the page,
        allowing the tooltip to be aligned inside the page itself.

        .. note::

          If :meth:`Chart.scrollable_plot_area` is ``True``, then this will default to
          ``True``. Otherwise, it will default to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._outside

    @outside.setter
    def outside(self, value):
        if value is None:
            self._outside = None
        else:
            self._outside = bool(value)

    @property
    def padding(self) -> Optional[int | float | Decimal]:
        f"""The padding inside the tooltip, expressed in pixels.

        Defaults to ``{constants.DEFAULT_TOOLTIP.get('padding')}``.

        :returns: The padding to apply to the tooltip.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validators.numeric(value, allow_empty = True)

    @property
    def point_format(self) -> Optional[str]:
        """The HTML of the point's line in the tooltip. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Variables are enclosed by curly brackets. Available variables are ``point.x``,
          ``point.y``, ``series.name``, ``series.color``, and other properties of the same
          form.

          Furthermore, ``point.y`` can be extended by the :meth:`Tooltip.value_prefix` and
          :meth:`Tooltip.value_suffix` properties. This can also be overridden for each
          series, which makes it a good hook for displaying units.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_format

    @point_format.setter
    def point_format(self, value):
        self._point_format = validators.string(value, allow_empty = True)

    @property
    def point_formatter(self) -> Optional[str]:
        """JavaScript callback function to format the text of the tooltip's point line.

        :rtype: :class:`str <python:None>` or :obj:`None <python:None>`
        """
        return self._point_formatter

    @point_formatter.setter
    def point_formatter(self, value):
        self._point_formatter = validators.string(value, allow_empty = True)

    @property
    def positioner(self) -> Optional[str]:
        """A JavaScript callback function to place the tooltip in a custom position.

        The callback receives three (JavaScript) parameters: ``labelWidth``,
        ``labelHeight``, and ``point``, where ``point`` contains values for ``plotX`` and
        ``plotY`` telling where the reference point is in the plot area. Add
        ``chart.plotLeft`` and ``chart.plotTop`` to get the full coordinates.

        To find the actual hovered ``Point`` instance, use ``this.chart.hoverPoint``. For
        :meth:`shared <Tooltip.shared>` or :meth:`split <Tooltip.split>` tooltips, all the
        hover points are available in ``this.chart.hoverPoints``.

        The return should be an object containing x and y values, for example:
        ``{ x: 100, y: 100 }``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._positioner

    @positioner.setter
    def positioner(self, value):
        self._positioner = validators.string(value, allow_empty = True)

    @property
    def shadow(self) -> bool | ShadowOptions:
        """Configuration for the shadow to apply to the tooltip. Defaults to
        ``True``.

        If ``False``, no shadow is applied.

        :returns: The shadow configuration to apply or a boolean setting which hides the
          shadow or displays the default shadow.
        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if isinstance(value, bool) and value is False:
            self._shadow = False
        elif not value:
            self._shadow = False
        else:
            value = validate_types(value,
                                   types = ShadowOptions)
            self._shadow = value

    @property
    def shape(self) -> str:
        f"""The name of the symbol to use for the border around the tooltip. Defaults to
        ``'{constants.DEFAULT_TOOLTIP.get('shape')}'``.

        Accepts:

          * ``'rect'``
          * ``'circle'``
          * ``'callout'``

        .. note::

          When :meth:`Tooltip.split` is enabled, the shape is applied to all boxes except
          the header (which is controlled by :meth:`Tooltip.header_shape`).

        :returns: The shape to use for the border around the tooltip.
        :rtype: :class:`str <python:str>`
        """
        return self._shape

    @shape.setter
    def shape(self, value):
        value = validators.string(value, allow_empty = False)
        value = value.lower()
        if value not in ['callout',
                         'rect',
                         'circle']:
            raise errors.HighchartsValueError(f'shape expects a supported tooltip shape. '
                                              f'Was: {value}')
        self._shape = value

    @property
    def shared(self) -> bool:
        """When ``True``, the entire plot area will capture mouse movement or touch
        events. Defaults to ``False``.

        .. hint::

          If ``True``, tooltip texts for series types with ordered data (not pie, scatter,
          flags etc) will be shown in a single bubble. This is recommended for single
          series charts and for tablet/mobile optimized charts.

          See also :meth:`Tooltip.split`, which is better suited for charts with many
          series, especially line-type series. The :meth:`Tooltip.split` option takes
          precedence over :meth:`Tooltip.shared`.

        :rtype: :class:`bool <python:bool>`
        """
        return self._shared

    @shared.setter
    def shared(self, value):
        self._shared = bool(value)

    @property
    def snap(self) -> Optional[int | float | Decimal]:
        """Proximity snap for graphs or single points. If :obj:`None <python:None>`, it
        defaults to ``10`` pixels for mouse-powered devices and ``25`` for touch devices.

        Defaults to :obj:`None <python:None>`.

        .. note::

          In most cases, the whole plot area captures the mouse movement, and in these
          cases :meth:`Tooltip.snap` doesn't make sense. This applies when
          :meth:`Tooltip.sticky_tracking` is ``True`` (default) and when the tooltip is
          :meth:`shared <Tooltip.shared>` or :meth:`split <Tooltip.split>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._snap

    @snap.setter
    def snap(self, value):
        self._snap = validators.numeric(value,
                                        allow_empty = True,
                                        minimum = 0)

    @property
    def split(self) -> bool:
        """If ``True``, splits the tooltip into one label per series, with the header
        close to the axis. Defaults to ``False``.

        .. hint::

          This is recommended over :meth:`shared <Tooltip.shared>` tooltips for charts
          with multiple line series, generally making them easier to read.

        .. note::

          This option takes precedence over :meth:`Tooltip.shared`.

        :rtype: :class:`bool <python:bool>`
        """
        return self._split

    @split.setter
    def split(self, value):
        self._split = bool(value)

    @property
    def stick_on_contact(self) -> bool:
        """If ``True``, prevents the tooltip from switching or closing when touched or
        pointed. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._stick_on_contact

    @stick_on_contact.setter
    def stick_on_contact(self, value):
        self._stick_on_contact = bool(value)

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the tooltip.

        .. note::

          The tooltip can also be styled through the CSS class ``.highcharts-tooltip``.

        .. warning::

          The default ``pointerEvents`` style makes the tooltip ignore mouse events, so in
          order to use clickable tooltips, this value must be set to ``auto``.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @property
    def use_html(self) -> bool:
        """If ``True``, will use HTML to render the tooltip. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        .. hint::

          Using HTML allows advanced formatting like tables and images in the tooltip. It
          is also recommended for RTL languages as it works around RTL bugs in early
          Firefox.

        :returns: Flag indicating whether to render tooltips using HTML.
        :rtype: :class:`bool <python:bool>`
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        self._use_html = bool(value)

    @property
    def value_decimals(self) -> Optional[int]:
        """How many decimals to show in each series' y value. Defaults to
        :obj:`None <python:None>`, which perserves all decimals.

        .. note::

          This is overridable in each series' tooltip options object.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._value_decimals

    @value_decimals.setter
    def value_decimals(self, value):
        self._value_decimals = validators.integer(value, allow_empty = True)

    @property
    def value_prefix(self) -> Optional[str]:
        """A string to prepend to each series' y value. Overridable in each series'
        tooltip options object. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value_prefix

    @value_prefix.setter
    def value_prefix(self, value):
        self._value_prefix = validators.string(value, allow_empty = True)

    @property
    def value_suffix(self) -> Optional[str]:
        """A string to append to each series' y value. Overridable in each series' tooltip
        options object. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value_suffix

    @value_suffix.setter
    def value_suffix(self, value):
        self._value_suffix = validators.string(value, allow_empty = True)

    @property
    def x_date_format(self) -> Optional[str]:
        """The format for the date in the tooltip header if the X axis is a datetime axis.
        Defaults to :obj:`None <python:None>`, which produces a best-guess based on the
        smallest distance between points in the chart.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._x_date_format

    @x_date_format.setter
    def x_date_format(self, value):
        self._x_date_format = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.pop('animation', True),
            'background_color': as_dict.pop('backgroundColor', None),
            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius',
                                         constants.DEFAULT_TOOLTIP.get('border_radius')),
            'border_width': as_dict.pop('borderWidth',
                                        constants.DEFAULT_TOOLTIP.get('border_width')),
            'class_name': as_dict.pop('className', None),
            'cluster_format': as_dict.pop('clusterFormat', None),
            'date_time_label_formats': as_dict.pop('dateTimeLabelFormats', None),
            'distance': as_dict.pop('distance',
                                    constants.DEFAULT_TOOLTIP.get('distance')),
            'enabled': as_dict.pop('enabled', True),
            'follow_pointer': as_dict.pop('followPointer', False),
            'follow_touch_move': as_dict.pop('followTouchMove', True),
            'footer_format': as_dict.pop('footerFormat',
                                         constants.DEFAULT_TOOLTIP.get('footer_format')),
            'formatter': as_dict.pop('formatter', None),
            'header_format': as_dict.pop('headerFormat', None),
            'header_shape': as_dict.pop('headerShape',
                                        constants.DEFAULT_TOOLTIP.get('header_shape')),
            'hide_delay': as_dict.pop('hideDelay',
                                      constants.DEFAULT_TOOLTIP.get('hide_delay')),
            'null_format': as_dict.pop('nullFormat', None),
            'null_formatter': as_dict.pop('nullFormatter', None),
            'outside': as_dict.pop('outside', None),
            'padding': as_dict.pop('padding', constants.DEFAULT_TOOLTIP.get('padding')),
            'point_format': as_dict.pop('pointFormat', None),
            'point_formatter': as_dict.pop('pointFormatter', None),
            'positioner': as_dict.pop('positioner', None),
            'shadow': as_dict.pop('shadow', True),
            'shape': as_dict.pop('shape', constants.DEFAULT_TOOLTIP.get('shape')),
            'shared': as_dict.pop('shared', False),
            'snap': as_dict.pop('snap', constants.DEFAULT_TOOLTIP.get('snap')),
            'split': as_dict.pop('split', False),
            'stick_on_contact': as_dict.pop('stickOnContact', False),
            'style': as_dict.pop('style', None),
            'use_html': as_dict.pop('useHTML', False),
            'value_decimals': as_dict.pop('valueDecimals', None),
            'value_prefix': as_dict.pop('valuePrefix', None),
            'value_suffix': as_dict.pop('valueSuffix', None),
            'x_date_format': as_dict.pop('xDateFormat', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'animation': self.animation,
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'clusterFormat': self.cluster_format,
            'dateTimeLabelFormats': self.date_time_label_formats,
            'distance': self.distance,
            'enabled': self.enabled,
            'followPointer': self.follow_pointer,
            'followTouchMove': self.follow_touch_move,
            'footerFormat': self.footer_format,
            'formatter': self.formatter,
            'headerFormat': self.header_format,
            'headerShape': self.header_shape,
            'hideDelay': self.hide_delay,
            'nullFormat': self.null_format,
            'nullFormatter': self.null_formatter,
            'outside': self.outside,
            'padding': self.padding,
            'pointFormat': self.point_format,
            'pointFormatter': self.point_formatter,
            'positioner': self.positioner,
            'shadow': self.shadow,
            'shape': self.shape,
            'shared': self.shared,
            'snap': self.snap,
            'split': self.split,
            'stickOnContact': self.stick_on_contact,
            'style': self.style,
            'useHTML': self.use_html,
            'valueDecimals': self.value_decimals,
            'valuePrefix': self.value_prefix,
            'valueSuffix': self.value_suffix,
            'xDateFormat': self.x_date_format
        }

        return self.trim_dict(untrimmed)
