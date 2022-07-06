from typing import Optional

from validator_collection import validators

from highcharts import errors
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
        """The horizontal alignment of the button. Defaults to ``'right'``.

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
        """The vertical alignment of the button. Defaults to ``'top'``.

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
