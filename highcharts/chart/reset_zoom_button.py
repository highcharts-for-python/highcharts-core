from typing import Optional

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class Position(HighchartsMeta):
    """The position of the Reset Zoom Button."""

    def __init__(self, **kwargs):
        self._align = 'right'
        self._vertical_align = 'top'
        self._x = -10
        self._y = 10

        self.align = kwargs.pop('align', 'right')
        self.vertical_align = kwargs.pop('vertical_align', 'top')
        self.x = kwargs.pop('x', -10)
        self.y = kwargs.pop('y', 10)

    @property
    def align(self) -> str:
        f"""The horizontal alignment of the button. Defaults to ``'right'``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :returns: The horizontal alignment of the button.
        :rtype: :class:`str <python:str>`
        """
        return self._align

    @align.setter
    def align(self, value):
        value = validators.string(value, allow_empty = False)
        value = value.lower()
        if value not in ['left', 'center', 'right']:
            raise errors.HighchartsValueError(f'align must be either "left", "center", or '
                                              f'"right". Was: {value}')

        self._align = value

    @property
    def vertical_align(self) -> Optional[str]:
        f"""The vertical alignment of the button. Defaults to ``'top'``.

        Accepts:

          * ``'bottom'``
          * ``'middle'``
          * ``'top'``

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
    def x(self) -> int:
        """The x position offset of the button. Defaults to ``-10``.

        :rtype: numeric
        """
        return self._x

    @x.setter
    def x(self, value):
        value = validators.numeric(value, allow_empty = True)
        if value is None:
            self._x = 0
        else:
            self._x = value

    @property
    def y(self) -> int:
        """The y position offset of the button. Defaults to ``10``.

        :rtype: numeric
        """
        return self._y

    @y.setter
    def y(self, value):
        value = validators.numeric(value, allow_empty = True)
        if value is None:
            self._y = 0
        else:
            self._y = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.pop('align', 'right'),
            'vertical_align': as_dict.pop('verticalAlign', 'top'),
            'x': as_dict.pop('x', -10),
            'y': as_dict.pop('y', 10)
        }

        return cls(**kwargs)

    def to_dict(self):
        return {
            'align': self.align,
            'verticalAlign': self.vertical_align,
            'x': self.x,
            'y': self.y
        }


class ResetZoomButtonOptions(HighchartsMeta):
    """Configuration settings for the button that appears after a selection zoom,
    allowing the user to reset zoom."""

    def __init__(self, **kwargs):
        self._position = None
        self._relative_to = 'plot'
        self._theme = None

        self.position = kwargs.pop('position',
                                   constants.DEFAULT_RESET_ZOOM_BUTTON_POSITION)
        self.relative_to = kwargs.pop('relative_to', 'plot')
        self.theme = kwargs.pop('theme', constants.DEFAULT_RESET_ZOOM_BUTTON_THEME)

    @property
    def position(self) -> Position:
        """The position of the button.

        :rtype: :class:`Position`
        """
        return self._position

    @position.setter
    @class_sensitive(Position)
    def position(self, value):
        self._position = value

    @property
    def relative_to(self) -> str:
        """What frame the button placement should be related to. Defaults to ``'plot'``.

        Accepts:

          * ``'plot'``
          * ``'chart'``
          * ``'plotBox'``
          * ``'spacingBox'

        :rtype: :class:`str <python:str>`
        """
        return self._relative_to

    @relative_to.setter
    def relative_to(self, value):
        if not value:
            self._relative_to = 'plot'
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['plot', 'chart', 'plotBox', 'spacingBox']:
                raise errors.HighchartsValueError(f'relative_to accepts "plot", "chart", '
                                                  f'"plotBox", "spacingBox", or None. '
                                                  f'Received: {value}')
            self._relative_to = value

    @property
    def theme(self) -> Optional[dict]:
        """A collection of attributes for the button.

        The object takes SVG attributes like ``fill``, ``stroke``, ``stroke-width`` or
        ``r``, the border radius.

        The theme also supports ``style``, a collection of CSS properties for the text.
        Equivalent attributes for the hover state are given in JavaScript
        ``theme.states.hover``.

        :rtype: :class:`dict <python:dict>`
        """
        return self._theme

    @theme.setter
    def theme(self, value):
        self._theme = validators.dict(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'position': as_dict.pop('position',
                                    constants.DEFAULT_RESET_ZOOM_BUTTON_POSITION),
            'relative_to': as_dict.pop('relativeTo', 'plot'),
            'theme': as_dict.pop('theme', constants.DEFAULT_RESET_ZOOM_BUTTON_THEME)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'position': self.position,
            'relativeTo': self.relative_to,
            'theme': self.theme
        }

        return self.trim_dict(untrimmed)
