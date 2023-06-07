from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.metaclasses import HighchartsMeta


class Subtitle(HighchartsMeta):
    """The chart's subtitle.

    .. note::

      This can be used both to display a subtitle below the main title, and to display
      random text anywhere in the chart.

    """

    def __init__(self, **kwargs):
        self._align = None
        self._floating = None
        self._style = None
        self._text = None
        self._use_html = None
        self._vertical_align = None
        self._width_adjust = None
        self._x = None
        self._y = None

        self.align = kwargs.get('align', None)
        self.floating = kwargs.get('floating', None)
        self.style = kwargs.get('style', None)
        self.text = kwargs.get('text', None)
        self.use_html = kwargs.get('use_html', None)
        self.vertical_align = kwargs.get('vertical_align', None)
        self.width_adjust = kwargs.get('width_adjust', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'subtitle'

    @property
    def align(self) -> Optional[str]:
        """The horizontal alignment of the subtitle. Defaults to
        ``'center'``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :returns: The alignment of the subtitle.
        :rtype: :class:`str <python:str>`
        """
        return self._align

    @align.setter
    def align(self, value):
        value = validators.string(value, allow_empty = True)
        if value:
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'align must be either "left", "center"'
                                                  f', or "right". Was: {value}')

        self._align = value

    @property
    def floating(self) -> Optional[bool]:
        """If ``True`, sets the subtitle to floating. When the subtitle is floating, the
        plot area will not move to make space for it. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._floating

    @floating.setter
    def floating(self, value):
        if value is None:
            self._floating = None
        else:
            self._floating = bool(value)

    @property
    def style(self) -> Optional[str | dict]:
        """CSS styling to apply to the subtitle. Defaults to
        ``{"color": "#666666", "fontSize": "0.8em"}``.

        :rtype: :class:`dict <python:dict>` or :class:`str <python:str>` or :obj:`None <python:None>`
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
    def text(self) -> Optional[str]:
        """The text of the subtitle. Defaults to an empty string (``''``).

        :rtype: :class:`str <python:str>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the subtitle. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render the subtitle using HTML.
        :rtype: :class:`bool <python:bool>`
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
        """The vertical alignment of the subtitle. Defaults to
        :obj:`None <python:None>`.

        Accepts:

          * ``'bottom'``
          * ``'middle'``
          * ``'top'``

        .. note::

          When set to ``'middle'``, the subtitle behaves as if :meth:`Subtitle.floating`
          were set to ``True``.

        :rtype: :class:`str <python:str>`
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
    def width_adjust(self) -> Optional[int | float | Decimal]:
        """Adjustment made to the subtitle width, normally to reserve space for the export
        hamburger menu. Defaults to ``-44``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width_adjust

    @width_adjust.setter
    def width_adjust(self, value):
        self._width_adjust = validators.numeric(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x position of the subtitle relative to the alignment within
        :meth:`Options.chart.spacing_left` and :meth:`Option.chart.spacing_right`.
        Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y position of the subtitle relative to the alignment within
        :meth:`Options.chart.spacing_top` and :meth:`Option.chart.spacing_bottom`.
        Defaults to :obj:`None <python:None>`, which positions the subtitle below the
        title (unless the title is floating).

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
            'floating': as_dict.get('floating', None),
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'width_adjust': as_dict.get('widthAdjust', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'floating': self.floating,
            'style': self.style,
            'text': self.text,
            'useHTML': self.use_html,
            'verticalAlign': self.vertical_align,
            'widthAdjust': self.width_adjust,
            'x': self.x,
            'y': self.y
        }

        return untrimmed
