from typing import Optional, List, Type
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class AxisLabelOptions(HighchartsMeta):
    """Settings for the axis labels, which show the number or category for each tick."""

    def __init__(self, **kwargs):
        self._align = None
        self._allow_overlap = None
        self._auto_rotation = None
        self._auto_rotation_limit = None
        self._distance = None
        self._enabled = None
        self._format = None
        self._formatter = None
        self._overflow = None
        self._padding = None
        self._position_3d = None
        self._reserve_space = None
        self._rotation = None
        self._skew_3d = None
        self._stagger_lines = None
        self._step = None
        self._style = None
        self._use_html = False
        self._x = None
        self._y = None
        self._z_index = None

        self.align = kwargs.get('align', None)
        self.allow_overlap = kwargs.get('allow_overlap', None)
        self.auto_rotation = kwargs.get('auto_rotation', None)
        self.auto_rotation_limit = kwargs.get('auto_rotation_limit', None)
        self.distance = kwargs.get('distance', None)
        self.enabled = kwargs.get('enabled', None)
        self.format = kwargs.get('format', None)
        self.formatter = kwargs.get('formatter', None)
        self.overflow = kwargs.get('overflow', None)
        self.padding = kwargs.get('padding', None)
        self.position_3d = kwargs.get('position_3d', None)
        self.reserve_space = kwargs.get('reserve_space', None)
        self.rotation = kwargs.get('rotation', None)
        self.skew_3d = kwargs.get('skew_3d', None)
        self.stagger_lines = kwargs.get('stagger_lines', None)
        self.step = kwargs.get('step', None)
        self.style = kwargs.get('style', None)
        self.use_html = kwargs.get('use_html', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'xAxis.labels'

    @property
    def align(self) -> Optional[str]:
        """The part of the string the given position is anchored to. If ``'left'``, the
        left side of the string is at the axis position. Defaults to
        :obj:`None <python:None>`, which leads Highcharts to determine the label alignment
        based on which side of the chart the axis is placed on and the rotation of the
        label.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

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
                raise errors.HighchartsValueError(f'align must be either "left", "center"'
                                                  f', or "right". Was: {value}')

            self._align = value

    @property
    def allow_overlap(self) -> Optional[bool]:
        """If ``True``, allows the axis labels to overlap. When ``False``, overlapping
        labels are hidden. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._allow_overlap

    @allow_overlap.setter
    def allow_overlap(self, value):
        if value is None:
            self._allow_overlap = None
        else:
            self._allow_overlap = bool(value)

    @property
    def auto_rotation(self) -> Optional[List[int | float | Decimal | Type[None]]]:
        """For horizontal axes, provides the allowed degrees of label rotation to prevent
        overlapping labels.

        If there is enough space, labels are not rotated. As the chart gets narrower, it
        will start rotating the labels by the measurements contained in ``auto_rotation``
        in sequence. If they still do not fit, then Highcharts will start removing every
        second label, and rotating through the sequence again, etc.

        Include :obj:`None <python:None>` in the collection to disable automatic rotation,
        at that step in the sequence - which will cause the labels to
        word-wrap if possible.

        If set to :obj:`None <python:None>`, defaults to ``[-45]``
        on bottom and top axes, and :obj:`None <python:None>` (word-wrapping) on left and
        right axes.

        :rtype: :obj:`None <python:None>`, or :class:`list <python:list>` of
          numeric/:obj:`None <python:None>` values
        """
        return self._auto_rotation

    @auto_rotation.setter
    def auto_rotation(self, value):
        if not value:
            self._auto_rotation = None
        else:
            value = validators.iterable(value)
            processed_value = []
            for item in value:
                if item is not None:
                    processed_item = validators.numeric(item)
                else:
                    processed_item = None

                processed_value.append(processed_item)

            self._auto_rotation = processed_value

    @property
    def auto_rotation_limit(self) -> Optional[int]:
        """The category width threshold at which auto rotation ceases to be applied.
        When each category width is more than this many pixels, auto rotation is not
        applied. Instead, the axis label is laid out with word wrapping. Defaults to
        ``80``.

        .. hint::

          A lower limit makes sense when the label contains multiple short words that
          don't extend the available horizontal space for each label.

        :rtype: :class:`int <python:int>`
        """
        return self._auto_rotation_limit

    @auto_rotation_limit.setter
    def auto_rotation_limit(self, value):
        self._auto_rotation_limit = validators.integer(value, allow_empty = True)

    @property
    def distance(self) -> Optional[int | float | Decimal | str]:
        """The label's pixel distance from the perimeter of the plot area.

        .. versionchanged:: Highcharts for Python v.1.2.0 + Highcharts Core (JS) v.11.1

          If not specified, defaults to ``8``.

          .. warning::

            On cartesian charts, this is overridden if the :meth:`.x <highcharts_core.options.axes.labels.x>` property 
            is set.
            
            On polar charts, if it's a percentage string, it is interpreted the same as 
            :meth:`SolidGaugeOptions.radius <plot_options.gauge.SolidGaugeOptions.radius>`, so that the label can be 
            aligned under the gauge's shape.

        :rtype: numeric, :class:`str <python:str>`, or :obj:`None <python:None>`
        """
        return self._distance

    @distance.setter
    def distance(self, value):
        if value is None:
            self._distance = None
        elif checkers.is_string(value) or not value:
            self._distance = validators.string(value)
        else:
            self._distance = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable or disable the axis labels. Setting to :obj:`None <python:None>` behaves
        as if set to ``True``.

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
    def format(self) -> Optional[str]:
        """Format string that is applied to the axis labels. Defaults to
        :obj:`None <python:None>`.

        Context is available as format string variables. For example, you can use
        ``'{text}'`` to insert the default formatted text. The recommended way of adding
        units for the label is using text, for example ``'{text} km'``.

        To add custom numeric or datetime formatting, use ``'{value}'`` with formatting,
        for example ``'{value:.1f}'`` or ``'{value:%Y-%m-%d}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format

    @format.setter
    def format(self, value):
        self._format = validators.string(value, allow_empty = True)

    @property
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format the axis label. Defaults to
        :obj:`None <python:None>`, which applies a built-in function which returns a
        formatted string depending on whether the axis is a category, datetime,
        linear/logarithmic, etc. axis type.

        .. note::

          The value is available in (JavaScript) ``this.value``. Additional properties for
          ``this`` are ``axis``, ``chart``, ``isFirst``, ``isLast``, and ``text`` which
          holds the value of the default formatter.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @property
    def overflow(self) -> Optional[str]:
        """Configuration on how to handle an axis label on the horizontal axis that
        overflows.  If set to ``'allow'``, it will not be aligned at all. Defaults to
        ``'justify'``, which attempts to align the label to the edge of the axis and
        on failure removes the label.

        Accepts:

          * ``'justify'`` - which attempts to fit the label to the edge of the axis
          * ``'allow'`` - which allows axis labels to overflow outside of the axis area

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
            if value not in ['justify', 'allow']:
                raise errors.HighchartsValueError(f'overflow accepts "justify" or "allow"'
                                                  f'. Was: {value}')
            self._overflow = value

    @property
    def padding(self) -> Optional[int | float | Decimal]:
        """The padding for axis labels, expressed in pixels (used to ensure white space
        between the labels). Defaults to ``5``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validators.numeric(value, allow_empty = True)

    @property
    def position_3d(self) -> Optional[str]:
        """Defines how the labels are to be repositioned according to the 3D chart
        orientation. Defaults to ``'offset'``.

        Accepts the following values:

          * ``'offset'`` (the default) - maintains a fixed horizontal/vertical distance
            from the tick marks, despite the chart orientation. This is
            backwards-compatible behavior, and causes skewing of X and Z axes.
          * ``'chart'`` - preserve the 3D position relative to the chart. This looks nice,
            but it is hard to read if the text isn't forward-facing.
          * ``'flap'`` - rotated text along the axis to compensate for the chart
            orientation. This tries to maintain text as legible as possible on all
            orientations.
          * ``'ortho'`` - rotates text along the axis direction so that the labels are
            orthogonal to the axis. This is very similar to ``'flap'``, but prevents
            skewing the labels (X and Y scaling are still present).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._position_3d

    @position_3d.setter
    def position_3d(self, value):
        if not value:
            self._position_3d = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['offset', 'chart', 'flap', 'ortho']:
                raise errors.HighchartsValueError(f'position expects a value of "offset",'
                                                  f' "chart", "flap", or "ortho". '
                                                  f'Was: {value}')
            self._position_3d = value

    @property
    def reserve_space(self) -> Optional[bool]:
        """If ``True``, reserve space for the labels. If :obj:`None <python:None>`, by
        default space is reserved for the labels in these cases:

          * On all horizontal axes.
          * On vertical axes if :meth:`AxisLabelOptions.align` is ``'right'`` on a
            left-side axis or ``'left'`` on a right-side axis.
          * On vertical axes if :meth:`AxisLabelOptions.align` is ``'center'``.

        This can be turned off (set to ``False``), for example, when the labels are
        rendered inside the plot area instead of outside.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._reserve_space

    @reserve_space.setter
    def reserve_space(self, value):
        if value is None:
            self._reserve_space = None
        else:
            self._reserve_space = bool(value)

    @property
    def rotation(self) -> Optional[int | float | Decimal]:
        """Rotation of the axis label in degrees. When :obj:`None <python:None>`, the
        :meth:`auto_rotation <AxisLabelOptions.auto_rotation>` setting takes precedence
        but otherwise defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = validators.numeric(value,
                                            allow_empty = True,
                                            minimum = 0)

    @property
    def skew_3d(self) -> Optional[bool]:
        """If ``True``, the axis labels will skewed to follow the perspective. Defaults to
        ``False``.

        .. note::

          Setting this to ``True`` will fix overlapping labels and titles, but texts
          become less legible due to the distortion. The final appearance depends heavily
          on :meth:`position_3d <AxisLabelOptions.position_3d>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._skew_3d

    @skew_3d.setter
    def skew_3d(self, value):
        if value is None:
            self._skew_3d = None
        else:
            self._skew_3d = bool(value)

    @property
    def stagger_lines(self) -> Optional[int]:
        """The number of lines to spread the labels over to make room or tighter labels.
        Defaults to ``0``.

        .. hint::

          Setting the value to ``0`` disables staggering.

        .. warning::

          Only applies to horizontal axes only.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._stagger_lines

    @stagger_lines.setter
    def stagger_lines(self, value):
        self._stagger_lines = validators.integer(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def step(self) -> Optional[int]:
        """To show only every *n* th label on the axis, set the step to *n*. For example,
        setting the step to ``2`` will render every other label. Defaults to ``0``.

        .. warning::

          When set to ``0``, the step is automatically calculated to avoid overlap. To
          prevent this behavior, set to ``1``. This usually only happens on a category
          axis, and is often a sign that you have chosen the wrong axis type.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._step

    @step.setter
    def step(self, value):
        self._step = validators.integer(value,
                                        allow_empty = True,
                                        minimum = 0)

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the axis label. Defaults to :obj:`None <python:None>`.

        .. hint::

          Use ``"whiteSpace: 'nowrap'"`` to prevent wrapping of category labels.

        .. hint::

          Use ``"textOverflow: 'one'"`` to prevent ellipsis (three dots).

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, 
                                        allow_empty = True,
                                        coerce_value = True)

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the axis label. If ``False``, will
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
    def x(self) -> Optional[int | float | Decimal]:
        """The x position offset of all labels relative to the tick positions on the axis.

        .. versionchanged:: Highcharts Core for Python v.2.0.0 / Highcharts Core (JS) v.11.

          .. note::
        
            If set, overrides the :meth:`.distance <highcharts_core.options.axes.labels.AxisLabelOptions.distance>`
            property.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y position offset of all labels relative to the tick positions on the axis.
        Defaults to :obj:`None <python:None>`, which makes it adapt to the font size of
        the bottom axis.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The Z index for the axis labels. Defaults to ``7``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'auto_rotation': as_dict.get('autoRotation', None),
            'auto_rotation_limit': as_dict.get('autoRotationLimit', None),
            'distance': as_dict.get('distance', None),
            'enabled': as_dict.get('enabled', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'overflow': as_dict.get('overflow', None),
            'padding': as_dict.get('padding', None),
            'position_3d': as_dict.get('position3d', None),
            'reserve_space': as_dict.get('reserveSpace', None),
            'rotation': as_dict.get('rotation', None),
            'skew_3d': as_dict.get('skew3d', None),
            'stagger_lines': as_dict.get('staggerLines', None),
            'step': as_dict.get('step', None),
            'style': as_dict.get('style', None),
            'use_html': as_dict.get('useHTML', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
            'z_index': as_dict.get('zIndex', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'allowOverlap': self.allow_overlap,
            'autoRotation': self.auto_rotation,
            'autoRotationLimit': self.auto_rotation_limit,
            'distance': self.distance,
            'enabled': self.enabled,
            'format': self.format,
            'formatter': self.formatter,
            'overflow': self.overflow,
            'padding': self.padding,
            'position3d': self.position_3d,
            'reserveSpace': self.reserve_space,
            'rotation': self.rotation,
            'skew3d': self.skew_3d,
            'staggerLines': self.stagger_lines,
            'step': self.step,
            'style': self.style,
            'useHTML': self.use_html,
            'x': self.x,
            'y': self.y,
            'zIndex': self.z_index
        }

        return untrimmed


class PlotBandLabel(HighchartsMeta):
    """Text label for a Plot Band."""

    def __init__(self, **kwargs):
        self._align = None
        self._rotation = None
        self._style = None
        self._text = None
        self._text_align = None
        self._use_html = None
        self._vertical_align = None
        self._x = None
        self._y = None

        self.align = kwargs.get('align', None)
        self.rotation = kwargs.get('rotation', None)
        self.style = kwargs.get('style', None)
        self.text = kwargs.get('text', None)
        self.text_align = kwargs.get('text_align', None)
        self.use_html = kwargs.get('use_html', None)
        self.vertical_align = kwargs.get('vertical_align', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def align(self) -> Optional[str]:
        """Horizontal alignment of the label.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

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
                raise errors.HighchartsValueError(f'align must be either "left", "center"'
                                                  f', or "right". Was: {value}')

            self._align = value

    @property
    def rotation(self) -> Optional[int | float | Decimal]:
        """Rotation of the label in degrees. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = validators.numeric(value,
                                            allow_empty = True,
                                            minimum = 0)

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the label. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, 
                                        allow_empty = True,
                                        coerce_value = True)

    @property
    def text(self) -> Optional[str]:
        """The string text itself.

        .. note::

          A subset of HTML is supported, e.g. ``<b>``, ``<i>``, etc.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @property
    def text_align(self) -> Optional[str]:
        """The text alignment for the label. Defaults to :obj:`None <python:None>`, which
        applies the same value as the :meth:`PlotBandLabel.align` setting.

        .. note::

          While :meth:`PlotBandLabel.align` determines where the text's anchor point is
          placed within the plot band, ``text_align`` determines how the text is aligned
          against its anchor point.

        Possible values are:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>`
        """
        return self._text_align

    @text_align.setter
    def text_align(self, value):
        if not value:
            self._text_align = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'text_align must be either "left", '
                                                  f'"center", or "right". Was: {value}')

            self._text_align = value

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the label. If ``False``, will
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
        """Vertical alignment of the label relative to the plot band. Defaults to
        ``'top'``.

        Accepts:

          * ``'top'``
          * ``'middle'``
          * ``'bottom'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, value):
        if not value:
            self._vertical_align = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['top', 'middle', 'bottom']:
                raise errors.HighchartsValueError(f'vertical_align expects either "top",'
                                                  f' "middle", or "bottom". Was: {value}')

            self._vertical_align = value

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The horizontal position offset relative to the alignment position. Defaults
        to :obj:`None <python:None>`, which adjusts the default based on the chart's
        orientation.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """Vertical position of the text baseline, relative to the vertical alignment.
        Defaults to :obj:`None <python:None>`, which adjusts the default behavior based
        on the chart's orientation.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'rotation': as_dict.get('rotation', None),
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None),
            'text_align': as_dict.get('textAlign', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'rotation': self.rotation,
            'style': self.style,
            'text': self.text,
            'textAlign': self.text_align,
            'useHTML': self.use_html,
            'verticalAlign': self.vertical_align,
            'x': self.x,
            'y': self.y
        }

        return untrimmed


class PlotLineLabel(PlotBandLabel):
    """Text label applied to a Plot Line."""

    def __init__(self, **kwargs):
        self._formatter = None

        self.formatter = kwargs.get('formatter', None)

        super().__init__(**kwargs)

    @property
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback  function to format the label. Defaults to
        :obj:`None <python:None>`.

        .. hint::

          Useful properties like the value of the plot line or the range of the plot band
          (:meth:`PlotBand.from` & :meth:`to <PlotBand.to>` properties) can be found in
          the (JavaScript) ``this.options`` object.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'formatter': as_dict.get('formatter', None),
            'rotation': as_dict.get('rotation', None),
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None),
            'text_align': as_dict.get('textAlign', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'formatter': self.formatter,
            'rotation': self.rotation,
            'style': self.style,
            'text': self.text,
            'textAlign': self.text_align,
            'useHTML': self.use_html,
            'verticalAlign': self.vertical_align,
            'x': self.x,
            'y': self.y
        }

        return untrimmed
