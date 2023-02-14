from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.metaclasses import HighchartsMeta


class Position(HighchartsMeta):
    """The position of the Reset Zoom Button."""

    def __init__(self, **kwargs):
        self._align = None
        self._vertical_align = None
        self._x = None
        self._y = None

        self.align = kwargs.get('align', None)
        self.vertical_align = kwargs.get('vertical_align', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def align(self) -> Optional[str]:
        """The horizontal alignment of the button. Defaults to ``'right'``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :returns: The horizontal alignment of the button.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
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
        if not value:
            self._vertical_align = None
        else:
            value = validators.string(value, allow_empty = True)
            value = value.lower()
            if value not in ['bottom', 'middle', 'top']:
                raise errors.HighchartsValueError(f'vertical_align expects either "top", '
                                                  f'"middle", or "bottom". Was: {value}')
            self._vertical_align = value

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x position offset of the button. Defaults to ``-10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y position offset of the button. Defaults to ``10``.

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
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'align': self.align,
            'verticalAlign': self.vertical_align,
            'x': self.x,
            'y': self.y
        }
