from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors, constants
from highcharts_core.metaclasses import HighchartsMeta


class AxisTitle(HighchartsMeta):
    """The axis title, shown next to the axis line."""

    def __init__(self, **kwargs):
        self._align = None
        self._margin = None
        self._offset = None
        self._position_3d = None
        self._reserve_space = None
        self._rotation = None
        self._skew_3d = None
        self._style = None
        self._text = None
        self._text_align = None
        self._use_html = False
        self._x = None
        self._y = None

        self.align = kwargs.get('align', None)
        self.margin = kwargs.get('margin', None)
        self.offset = kwargs.get('offset', None)
        self.position_3d = kwargs.get('position_3d', None)
        self.reserve_space = kwargs.get('reserve_space', None)
        self.rotation = kwargs.get('rotation', None)
        self.skew_3d = kwargs.get('skew_3d', None)
        self.style = kwargs.get('style', None)
        self.text = kwargs.get('text', None)
        self.text_align = kwargs.get('text_align', None)
        self.use_html = kwargs.get('use_html', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'xAxis.title'

    @property
    def align(self) -> Optional[str]:
        """Alignment of the title relative to the axis values. Defaults to ``middle``.

        Accepts:

          * ``'low'``
          * ``'middle'``
          * ``'high'``

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
            if value not in ['low', 'middle', 'high']:
                raise errors.HighchartsValueError(f'align must be either "low", "middle"'
                                                  f', or "high". Was: {value}')

            self._align = value

    @property
    def margin(self) -> Optional[int | float | Decimal]:
        """The distance (in pixels) between the axis labels or line and the title.
        Defaults to :obj:`None <python:None>`, which applies ``0`` for horizontal axes and
        ``10`` for vertical axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = validators.numeric(value, allow_empty = True)

    @property
    def offset(self) -> Optional[int | float | Decimal]:
        """The explicitly-provided distance of the axis title from the axis line. Defaults
        to :obj:`None <python:None>`.

        When :obj:`None <python:None>`, this distance is computed from the offset width of
        the labels, the labels' distance from the axis, and the title's
        :meth:`margin <AxisTitle.margin>`. However when the ``offset`` option is set, all
        this gets overridden.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = validators.numeric(value, allow_empty = True)

    @property
    def position_3d(self) -> Optional[str]:
        """Defines how the title is to be repositioned according to the 3D chart
        orientation. Defaults to :obj:`None <python:None>` which applies the setting from
        :meth:`AxisLabeLOptions.position_3d`.

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
        """If ``True``, reserve space for the title. Defaults to ``True``.

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
        """Rotation of the title in degrees, where ``0`` is horizontal and ``270`` is
        vertical reading from bottom to top. Defaults to ``0``.

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
        """If ``True``, the title will skewed to follow the perspective. Defaults to
        :obj:`None <python:None>`, which applies the same setting as set for
        :meth:`AxisLabeLOptions.skew_3d`.

        .. note::

          Setting this to ``True`` will fix overlapping labels and titles, but texts
          become less legible due to the distortion. The final appearance depends heavily
          on :meth:`position_3d <AxisTitle.position_3d>`.

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
    def style(self) -> Optional[str]:
        """CSS styling to apply to the title. Defaults to :obj:`None <python:None>`.

        .. hint::

          If the title length is longer than the axis length, the title will wrap by
          default. The following three methods can all prevent the title from wrapping in
          such a situation:

            * Setting ``"textOverflow: 'ellipsis'"`` in the ``style``
            * Setting ``"whiteSpace: 'nowrap'"`` in the ``style``
            * Setting an explicit :meth:`AxisTitle.width`

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True, coerce_value = True)

    @property
    def text(self) -> Optional[str | constants.EnforcedNullType]:
        """The actual text of the title.

        .. note::

          A subset of HTML is supported, e.g. ``<b>``, ``<i>``, ``<span>`` (with in-line
          styles), etc.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._text = constants.EnforcedNull
        else:
            self._text = validators.string(value, allow_empty = True)

    @property
    def text_align(self) -> Optional[str]:
        """The text alignment for the title. Defaults to :obj:`None <python:None>`, which
        applies behavior based on the :meth:`AxisTitle.align` setting and the axis
        orientation:

          * For Horizontal Axes:

            * when ``align == 'low'``, defaults to ``'left'``
            * when ``align == 'middle'``, defaults to ``'center'``
            * when ``align == 'high'``, defaults to ``'right'``

          * For Vertical Axes:

            * when ``align == 'low'`` and :meth:`NumericAxis.opposite` is ``True``,
              defaults to ``'right'``
            * when ``align == 'low'`` and :meth:`NumericAxis.opposite` is ``False``,
              defaults to ``'left'``
            * when ``align == 'middle'``, defaults to ``'center'``
            * when ``align == 'high'`` and :meth:`NumericAxis.opposite` is ``True``,
              defaults to ``'left'``
            * when ``align == 'high'`` and :meth:`NumericAxis.opposite` is ``True``,
              defaults to ``'right'``

        Possible values are:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
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
        """If ``True``, will use HTML to render the title. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render the title using HTML.
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
        """The x position offset of the title. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y position offset of the title. Defaults to ``0``.

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
            'margin': as_dict.get('margin', None),
            'offset': as_dict.get('offset', None),
            'position_3d': as_dict.get('position3d', None),
            'reserve_space': as_dict.get('reserveSpace', None),
            'rotation': as_dict.get('rotation', None),
            'skew_3d': as_dict.get('skew3d', None),
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None),
            'text_align': as_dict.get('textAlign', None),
            'use_html': as_dict.get('useHTML', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'margin': self.margin,
            'offset': self.offset,
            'position3d': self.position_3d,
            'reserveSpace': self.reserve_space,
            'rotation': self.rotation,
            'skew3d': self.skew_3d,
            'style': self.style,
            'text': self.text,
            'textAlign': self.text_align,
            'useHTML': self.use_html,
            'x': self.x,
            'y': self.y
        }

        return untrimmed
