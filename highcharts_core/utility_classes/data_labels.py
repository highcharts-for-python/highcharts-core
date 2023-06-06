from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_core.utility_classes.animation import AnimationOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.shadows import ShadowOptions
from highcharts_core.utility_classes.ast import TextPath
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class Filter(HighchartsMeta):
    """A declarative filter to control of which data labels to display.

    The declarative filter is designed for use when JavaScript callback functions are
    not available, like when the chart options require a pure JSON structure or for
    use with graphical editors. For programmatic control, use the
    :meth:`DataLabel.formatter` instead, and return ``undefined`` to disable a single
    data label."""

    def __init__(self, **kwargs):
        self._operator = None
        self._property = None
        self._value = None

        self.operator = kwargs.get('operator', None)
        self.property_ = kwargs.get('property_', None)
        self.value = kwargs.get('value', None)

    @property
    def operator(self) -> Optional[str]:
        """The operator to compare by. Defaults to :obj:`None <python:None>`.

        Accepts:

          * ``'>'``
          * ``'<'``
          * ``'>='``
          * ``'<='``
          * ``'=='``
          * ``'==='``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = validators.string(value, allow_empty = True)

    @property
    def property_(self) -> Optional[str]:
        """The point property to filter by. Defaults to :obj:`None <python:None>`.

        Point options are passed directly to properties, additionally there are ``y``
        value, ``percentage``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._property

    @property_.setter
    def property_(self, value):
        self._property = validators.string(value, allow_empty = True)

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The value to compare against. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        self._value = validators.numeric(value_, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'operator': as_dict.get('operator', None),
            'property_': as_dict.get('property', None),
            'value': as_dict.get('value', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'operator': self.operator,
            'property': self.property_,
            'value': self.value
        }


class DataLabel(HighchartsMeta):
    """Options for the series data labels, appearing next to each data point."""

    def __init__(self, **kwargs):
        self._align = None
        self._allow_overlap = None
        self._animation = None
        self._background_color = None
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._class_name = None
        self._color = None
        self._crop = None
        self._defer = None
        self._enabled = None
        self._filter = None
        self._format = None
        self._formatter = None
        self._inside = None
        self._null_format = None
        self._null_formatter = None
        self._overflow = None
        self._padding = None
        self._position = None
        self._rotation = None
        self._shadow = None
        self._shape = None
        self._style = None
        self._text_path = None
        self._use_html = None
        self._vertical_align = None
        self._x = None
        self._y = None
        self._z = None

        self.align = kwargs.get('align', None)
        self.allow_overlap = kwargs.get('allow_overlap', None)
        self.animation = kwargs.get('animation', None)
        self.background_color = kwargs.get('background_color', None)
        self.border_color = kwargs.get('border_color', None)
        self.border_radius = kwargs.get('border_radius', None)
        self.border_width = kwargs.get('border_width', None)
        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.crop = kwargs.get('crop', None)
        self.defer = kwargs.get('defer', None)
        self.enabled = kwargs.get('enabled', None)
        self.filter = kwargs.get('filter', None)
        self.format = kwargs.get('format', None)
        self.formatter = kwargs.get('formatter', None)
        self.inside = kwargs.get('inside', None)
        self.null_format = kwargs.get('null_format', None)
        self.null_formatter = kwargs.get('null_formatter', None)
        self.overflow = kwargs.get('overflow', None)
        self.padding = kwargs.get('padding', None)
        self.position = kwargs.get('position', None)
        self.rotation = kwargs.get('rotation', None)
        self.shadow = kwargs.get('shadow', None)
        self.shape = kwargs.get('shape', None)
        self.style = kwargs.get('style', None)
        self.text_path = kwargs.get('text_path', None)
        self.use_html = kwargs.get('use_html', None)
        self.vertical_align = kwargs.get('vertical_align', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
        self.z = kwargs.get('z', None)

    @property
    def align(self) -> Optional[str]:
        """The alignment of the data label compared to the point. Defaults to
        ``None``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        .. hint::

          If right, the right side of the label should be touching the point.

        :returns: The alignment of the annotation's label.
        :rtype: :class:`str <python:str>`
        """
        return self._align

    @align.setter
    def align(self, value):
        if not value:
            self._align = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'align must be either "left", '
                                                  f'"center", or "right". Was: {value}')

        self._align = value

    @property
    def allow_overlap(self) -> Optional[bool]:
        """If ``True``, data labels are allowed to overlap each other.

        Defaults to ``False``.

        .. hint::

          To make the labels less sensitive for overlapping, the :meth:`DataLabel.padding`
          can be set to ``0``.

        :returns: Flag indicating whether to allow data labels to overlap.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_overlap

    @allow_overlap.setter
    def allow_overlap(self, value):
        if value is None:
            self._allow_overlap = None
        else:
            self._allow_overlap = bool(value)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Enable or disable the initial animation for the data labels when a series is
        displayed.

        The animation can also be set as a configuration object. Please note that this
        option only applies to the initial animation of the series itself. For other
        animations, see :class:`Chart.animation` and the ``animation`` parameter under the
        (JavaScript) API methods. The following properties are supported:

          * ``defer``: The animation delay time in milliseconds.

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
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or gradient for the data label. Defaults to
        :obj:`None <python:None>`.

        :returns: The backgorund color for the data label.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        from highcharts_core import utility_functions
        self._background_color = utility_functions.validate_color(value)

    @property
    def border_color(self) -> Optional[str]:
        """The border color for the data label. Defaults to
        :obj:`None <python:None>`

        :returns: The border color for the data label.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = validators.string(value, allow_empty = True)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The border radius (in pixels) applied to the data label. Defaults to
        ``0``.

        :returns: The border radius to apply to the data label.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width (in pixels) applied to the data label. Defaults to
        ``0``.

        :returns: The border width to apply to the data label.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS. Defaults to
        ``'highcharts-no-tooltip'``.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str]:
        """The text color for the data labels. Defaults to :obj:`None <python:None>`.

        .. note::

          For certain series types, like column or map, the data labels can be drawn
          inside the points. In this case the data label will be drawn with maximum
          contrast by default. Additionally, it will be given a ``text-outline`` style
          with the opposite color, to further increase the contrast. This can be
          overridden by setting the ``text-outline`` style to ``none`` in the
          :meth:`DataLabel.style` setting.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def crop(self) -> Optional[bool]:
        """If ``True``, hide part of the data label that falls outside the plot
        area. Defaults to ``False``.

        .. note::

          By default, the data label is moved inside the plot area as per the
          :meth:`DataLabel.overflow` setting.

        :returns: Flag indicating whether to clip a data label that extends beyond
          the plot area.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crop

    @crop.setter
    def crop(self, value):
        if value is None:
            self._crop = None
        else:
            self._crop = bool(value)

    @property
    def defer(self) -> Optional[bool | int]:
        """Whether to defer displaying the data labels until the initial series animation
        has finished. If :obj:`None <python:None>`, behaves as if set to ``True``.

        Setting to ``False`` renders the data label immediately.

        If set to ``True`` inherits the defer time set in
        :meth:`PlotOptions.series.animation`.

        If set to a number, defers the animation by that number of milliseconds.

        :rtype: :class:`bool <python:bool>` or :class:`int <python:int>` or
          :obj:`None <python:None>`
        """
        return self._defer

    @defer.setter
    def defer(self, value):
        if value is None:
            self._defer = None
        else:
            if value is True or value is False:
                self._defer = value
            else:
                self._defer = validators.integer(value)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable or disable the data labels. Setting to :obj:`None <python:None>` behaves
        as if set to ``False``.

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
    def filter(self) -> Optional[Filter]:
        """A declarative filter to control of which data labels to display.

        The declarative filter is designed for use when JavaScript callback functions are
        not available, like when the chart options require a pure JSON structure or for
        use with graphical editors. For programmatic control, use the
        :meth:`DataLabel.formatter` instead, and return ``undefined`` to disable a single
        data label.

        :rtype: :class:`Filter` or :obj:`None <python:None>`
        """
        return self._filter

    @filter.setter
    @class_sensitive(Filter)
    def filter(self, value):
        self._filter = value

    @property
    def format(self) -> Optional[str]:
        """A format string to apply to the label. Defaults to
        ``'point.value'``.


        :returns: The format string to apply to the labels.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format

    @format.setter
    def format(self, value):
        self._format = validators.string(value, allow_empty = True)

    @property
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format the data label. Defaults to
        :obj:`None <python:None>`.

        .. note::

          If a :meth:`DataLabel.format` is specified, the formatter will be ignored.

        :returns: A JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @property
    def inside(self) -> Optional[bool]:
        """For points with an extent, like columns or map areas, whether to align the data
        label inside the box or to the actual value point. Defaults to
        ``:obj:`None <python:None>`, which behaves like ``False`` in most cases but
        ``True`` in stacked columns.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._inside

    @inside.setter
    def inside(self, value):
        if value is None:
            self._inside = None
        else:
            self._inside = bool(value)

    @property
    def null_format(self) -> Optional[str]:
        """Format for points with the value of ``null``. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Works analogously to :meth:`DataLabel.format`.

        .. warning::

          Can only be applied only to series which support displaying null points.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._null_format

    @null_format.setter
    def null_format(self, value):
        self._null_format = validators.string(value, allow_empty = True)

    @property
    def null_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format the text of the data label for visible
        null points.

        .. note::

          Works analogously to :meth:`DataLabel.formatter`.

        .. warning::

          Can only be applied only to series which support displaying null points.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._null_formatter

    @null_formatter.setter
    @class_sensitive(CallbackFunction)
    def null_formatter(self, value):
        self._null_formatter = value

    @property
    def overflow(self) -> Optional[str]:
        """Configuration on how to handle a data label that overflows outside of
        the plot area.  Defaults to ``'justify'``,
        which aligns them inside the plot area. For columns and bars, this means the data
        label will be moved inside the bar.

        .. hint::

          To display data labels outside the plot area, set ``overflow`` to ``'allow'``
          and :meth:`DataLabel.crop` to ``False``.

        Accepts:

          * ``'justify'`` - which forces the label back into the plot area
          * ``'allow'`` - which allows data labels to overflow outside of the plot area

        .. note::

          The overflow treatment is also affected by the :meth:`DataLabel.crop`
          setting.

        :returns: Configuration of overflow setting.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._overflow

    @overflow.setter
    def overflow(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._overflow = None
        else:
            value = value.lower()
            if value not in ['justify', 'none']:
                raise errors.HighchartsValueError(f'overflow accepts "justify" or "none".'
                                                  f' Was: {value}')
            self._overflow = value

    @property
    def padding(self) -> Optional[int]:
        """The padding within the border box when either
        :meth:`DataLabel.border_width` or :meth:`DataLabel.background_color` is set.

        Defaults to ``5``.

        :returns: The padding to apply to the data label.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validators.numeric(value, allow_empty = True)

    @property
    def position(self) -> Optional[str]:
        """Aligns data labels relative to points. Defaults to
        ``'center'``.

        Accepts the following values:

          * ``'center'`` (the default)
          * ``'left'``
          * ``'right'``

        .. note::

          If ``center`` is not possible, aligns to ``right``.

        :rtype: :class:`str <python:str>`
        """
        return self._position

    @position.setter
    def position(self, value):
        if not value:
            self._position = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['center', 'left', 'right']:
                raise errors.HighchartsValueError(f'position expects a value of "center",'
                                                  f' "left", or "right". Was: {value}')
            self._position = value

    @property
    def rotation(self) -> Optional[int | float | Decimal]:
        """Text rotation in degrees. Defaults to
        ``0``

        .. warning::

          Due to a more complex structure, backgrounds, borders and padding will be lost
          on a rotated data label.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = validators.numeric(value, allow_empty = True)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
        """Configuration for the shadow to apply to the data label box. Defaults to
        ``False``.

        If ``False``, no shadow is applied.

        :returns: The shadow configuration to apply or ``False``.
        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions` or
          :obj:`None <python:None>`
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
                                   types = ShadowOptions)
            self._shadow = value

    @property
    def shape(self) -> Optional[str]:
        """The name of the symbol to use for the border around the label. Defaults to
        ``'square'``.

        Accepts:

          * ``'rect'``
          * ``'square'``
          * ``'circle'``
          * ``'diamond'``
          * ``'triangle'``
          * ``'callout'``

        :returns: The shape to use for the border around the label.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._shape

    @shape.setter
    def shape(self, value):
        if not value:
            self._shape = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['callout',
                             'connector',
                             'rect',
                             'circle',
                             'diamond',
                             'triangle']:
                raise errors.HighchartsValueError(f'shape expects a supported annotation '
                                                  f'label shape. Was: {value}')
            self._shape = value

    @property
    def style(self) -> Optional[dict | str]:
        """CSS styling to apply to the annotation's label.

        The default color setting is ``"contrast"``, which is a pseudo color that
        Highcharts picks up and applies the maximum contrast to the underlying point item,
        for example the bar in a bar chart.

        ``textOutline`` is a pseudo property that applies an outline of the given width
        with the given color, which by default is the maximum contrast to the text. So a
        bright text color will result in a black text outline for maximum readability on
        a mixed background. In some cases, especially with grayscale text, the text
        outline doesn't work well, in which cases it can be disabled by setting it to
        ``"none"``. When :meth:`DataLabel.use_html` is ``True``, the ``textOutline`` will
        not be picked up. In this, case, the same effect can be acheived through the
        ``text-shadow`` CSS property.

        For some series types, where each point has an extent, like for example tree maps,
        the data label may overflow the point. There are two strategies for handling
        overflow. By default, the text will wrap to multiple lines. The other strategy is
        to set ``textOverflow`` to ellipsis, which will keep the text on one line plus it
        will break inside long words.

        :rtype: :class:`dict <python:dict>` or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        try:
            self._style = validators.dict(value, allow_empty = True)
        except (ValueError, TypeError):
            self._style = validators.string(value, allow_empty = True)

    @property
    def text_path(self) -> Optional[TextPath]:
        """Options for a label text which should follow marker's shape.

        .. note::

          Border and background are disabled for a label that follows a path.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text_path

    @text_path.setter
    @class_sensitive(TextPath)
    def text_path(self, value):
        self._text_path = value

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the data label. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render data labels using HTML.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        if value is None:
            self._use_html = None
        else:
            self._use_html = bool(value)

    @property
    def vertical_align(self) -> Optional[str]:
        """The vertical alignment of the annotation's label. Defaults to
        :obj:`None <python:None>`.

        If :obj:`None <python:None>`, the alignment will depend on the data. For example,
        in a column chart, the label would be above positive values and below negative
        values.

        Accepts:

          * ``'bottom'``
          * ``'middle'``
          * ``'top'``
          * :obj:`None <python:None>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._vertical_align = None
        else:
            value = value.lower()
            if value not in ['bottom', 'middle', 'top']:
                raise errors.HighchartsValueError(f'vertical_align expects either "top", '
                                                  f'"middle", or "bottom". Was: {value}')
            self._vertical_align = value

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x position offset of the label relative to the point. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y position offset of the label relative to the point. Defaults to
        ``None``.

        :rtype: numeric
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @property
    def z(self) -> Optional[int]:
        """The Z index of the data labels. Defaults to
        ``6``.

        If :obj:`None <python:None>`, will be placed above the series.

        .. hint::

          Use a Z index of ``2`` to display it behind the series.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z

    @z.setter
    def z(self, value):
        self._z = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'animation': as_dict.get('animation', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'crop': as_dict.get('crop', None),
            'defer': as_dict.get('defer', None),
            'enabled': as_dict.get('enabled', None),
            'filter': as_dict.get('filter', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'inside': as_dict.get('inside', None),
            'null_format': as_dict.get('nullFormat', None),
            'null_formatter': as_dict.get('nullFormatter', None),
            'overflow': as_dict.get('overflow', None),
            'padding': as_dict.get('padding', None),
            'position': as_dict.get('position', None),
            'rotation': as_dict.get('rotation', None),
            'shadow': as_dict.get('shadow', None),
            'shape': as_dict.get('shape', None),
            'style': as_dict.get('style', None),
            'text_path': as_dict.get('textPath', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
            'z': as_dict.get('z', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'allowOverlap': self.allow_overlap,
            'animation': self.animation,
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'color': self.color,
            'crop': self.crop,
            'defer': self.defer,
            'enabled': self.enabled,
            'filter': self.filter,
            'format': self.format,
            'formatter': self.formatter,
            'inside': self.inside,
            'nullFormat': self.null_format,
            'nullFormatter': self.null_formatter,
            'overflow': self.overflow,
            'padding': self.padding,
            'position': self.position,
            'rotation': self.rotation,
            'shadow': self.shadow,
            'shape': self.shape,
            'style': self.style,
            'textPath': self.text_path,
            'useHTML': self.use_html,
            'verticalAlign': self.vertical_align,
            'x': self.x,
            'y': self.y,
            'z': self.z
        }

        return untrimmed


class SunburstDataLabel(DataLabel):
    """Variant of :class:`DataLabel` used for :term:`sunburst` series."""
    
    def __init__(self, **kwargs):
        self._rotation_mode = None
        
        self.rotation_mode = kwargs.get('rotation_mode', None)
        
        super().__init__(**kwargs)
        
    @property
    def rotation_mode(self) -> Optional[str]:
        """Determines how the data label will be rotated relative to the perimeter of the sunburst. 
        
        Valid values are:
        
          * ``'circular'``
          * ``'auto'``
          * ``'parallel'`` 
          * ``'perpendicular'``. 
          
        Defaults to ``'circular'``.
        
        .. note::

          When ``'circular'``, the best fit will be computed for the point, so that the label is curved around the 
          center when there is room for it, otherwise perpendicular. 
        
          The legacy ``'auto'`` option works similiarly to ``'circular'``, but instead of curving the labels, they are 
          tangented to the perimiter.
        
        .. warning::
        
          The :meth:`.rotation <highcharts_core.utility_classes.data_labels.SunburstDataLabel.rotation>` property 
          takes precedence over ``.rotation_mode``.
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._rotation_mode
    
    @rotation_mode.setter
    def rotation_mode(self, value):
        if not value:
            self._rotation_mode = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['circular', 'auto', 'parallel', 'perpendicular']:
                raise errors.HighchartsValueError(f'if not empty, rotation_mode expects a value of either '
                                                  f'"circular", "auto", "parallel", or "perpendicular", '
                                                  f' but received "{str}".')

            self._rotation_mode = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'animation': as_dict.get('animation', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'crop': as_dict.get('crop', None),
            'defer': as_dict.get('defer', None),
            'enabled': as_dict.get('enabled', None),
            'filter': as_dict.get('filter', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'inside': as_dict.get('inside', None),
            'null_format': as_dict.get('nullFormat', None),
            'null_formatter': as_dict.get('nullFormatter', None),
            'overflow': as_dict.get('overflow', None),
            'padding': as_dict.get('padding', None),
            'position': as_dict.get('position', None),
            'rotation': as_dict.get('rotation', None),
            'shadow': as_dict.get('shadow', None),
            'shape': as_dict.get('shape', None),
            'style': as_dict.get('style', None),
            'text_path': as_dict.get('textPath', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
            'z': as_dict.get('z', None),
            
            'rotation_mode': as_dict.get('rotationMode', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'rotationMode': self.rotation_mode,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class OrganizationDataLabel(DataLabel):
    """Variant of :class:`DataLabel` used for :term:`organization` series."""
    
    def __init__(self, **kwargs):
        self._link_format = None
        self._link_formatter = None
        self._link_text_path = None
        
        self.link_format = kwargs.get('link_format', None)
        self.link_formatter = kwargs.get('link_formatter', None)
        self.link_text_path = kwargs.get('link_text_path', None)
        
        super().__init__(**kwargs)

    @property
    def link_format(self) -> Optional[str]:
        """The format string specifying what to show for links in the\rorganization chart.
        
        .. tip::
        
          Best to use with 
          :meth:`.link_text_path <highcharts_core.utility_classes.data_labels.OrganizationDataLabel.link_text_path>`
          enabled.
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._link_format
    
    @link_format.setter
    def link_format(self, value):
        self._link_format = validators.string(value, allow_empty = True)

    @property
    def link_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format data labels for links in the organization chart. 

        .. note::

          The :meth:`.link_format <highcharts_core.utility_classes.data_labels.OrganizationDataLabel.link_format>`
          property takes precedence over the ``link_formatter``.

        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._link_formatter

    @link_formatter.setter
    @class_sensitive(CallbackFunction)
    def link_formatter(self, value):
        self._link_formatter = value

    @property
    def link_text_path(self) -> Optional[TextPath]:
        """Options for a label text which should follow the link's shape.

        .. note::

          Border and background are disabled for a label that follows a path.

        :rtype: :class:`TextPath <highcharts_core.utility_classes.ast.TextPath>` or :obj:`None <python:None>`
        """
        return self._link_text_path

    @link_text_path.setter
    @class_sensitive(TextPath)
    def link_text_path(self, value):
        self._link_text_path = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'animation': as_dict.get('animation', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'crop': as_dict.get('crop', None),
            'defer': as_dict.get('defer', None),
            'enabled': as_dict.get('enabled', None),
            'filter': as_dict.get('filter', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'inside': as_dict.get('inside', None),
            'null_format': as_dict.get('nullFormat', None),
            'null_formatter': as_dict.get('nullFormatter', None),
            'overflow': as_dict.get('overflow', None),
            'padding': as_dict.get('padding', None),
            'position': as_dict.get('position', None),
            'rotation': as_dict.get('rotation', None),
            'shadow': as_dict.get('shadow', None),
            'shape': as_dict.get('shape', None),
            'style': as_dict.get('style', None),
            'text_path': as_dict.get('textPath', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
            'z': as_dict.get('z', None),
            
            'link_format': as_dict.get('linkFormat', None),
            'link_formatter': as_dict.get('linkFormatter', None),
            'link_text_path': as_dict.get('linkTextPath', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'linkFormat': self.link_format,
            'linkFormatter': self.link_formatter,
            'linkTextPath': self.link_text_path,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class NodeDataLabel(DataLabel):
    """Variant of :class:`DataLabel` used for node-based charts/diagrams."""

    def __init__(self, **kwargs):
        self._node_format = None
        self._node_formatter = None

        self.node_format = kwargs.get('node_format', None)
        self.node_formatter = kwargs.get('node_formatter', None)

        super().__init__(**kwargs)

    @property
    def node_format(self) -> Optional[str]:
        """The format string which determines what to render for nodes in a sankey,
        organization, or similar diagram. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._node_format

    @node_format.setter
    def node_format(self, value):
        self._node_format = validators.string(value, allow_empty = True)

    @property
    def node_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format data labels for nodes in a sankey or
        organization diagram. Defaults to :obj:`None <python:None>`.

        .. note::

          The :meth:`node_format <NodeDataLabel.node_format>` takes precedence over the
          ``node_formatter``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._node_formatter

    @node_formatter.setter
    @class_sensitive(CallbackFunction)
    def node_formatter(self, value):
        self._node_formatter = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'animation': as_dict.get('animation', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'crop': as_dict.get('crop', None),
            'defer': as_dict.get('defer', None),
            'enabled': as_dict.get('enabled', None),
            'filter': as_dict.get('filter', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'inside': as_dict.get('inside', None),
            'null_format': as_dict.get('nullFormat', None),
            'null_formatter': as_dict.get('nullFormatter', None),
            'overflow': as_dict.get('overflow', None),
            'padding': as_dict.get('padding', None),
            'position': as_dict.get('position', None),
            'rotation': as_dict.get('rotation', None),
            'shadow': as_dict.get('shadow', None),
            'shape': as_dict.get('shape', None),
            'style': as_dict.get('style', None),
            'text_path': as_dict.get('textPath', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
            'z': as_dict.get('z', None),

            'node_format': as_dict.get('nodeFormat', None),
            'node_formatter': as_dict.get('nodeFormatter', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'nodeFormat': self.node_format,
            'nodeFormatter': self.node_formatter,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
