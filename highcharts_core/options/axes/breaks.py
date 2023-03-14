from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class AxisBreak(HighchartsMeta):
    """The definition of a break (non-continuous section, typically indicating a "jump")
    in the axis.

    .. note::

      The sections defined as breaks will be left out and all the points shifted
      closer to each other.

    """

    def __init__(self, **kwargs):
        self._break_size = None
        self._from_ = None
        self._repeat = None
        self._to = None

        self.break_size = kwargs.get('break_size', None)
        self.from_ = kwargs.get('from_', None)
        self.repeat = kwargs.get('repeat', None)
        self.to = kwargs.get('to', None)

    @property
    def break_size(self) -> Optional[int | float | Decimal]:
        """A number indicating how much space should be left between the start and the end
        of the break. Defaults to ``0``.

        .. note::

          The break size is given in axis units, so for instance on a datetime axis, a
          break size of ``3600000`` would indicate the equivalent of an hour.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._break_size

    @break_size.setter
    def break_size(self, value):
        self._break_size = validators.numeric(value, allow_empty = True)

    @property
    def from_(self) -> Optional[int | float | Decimal]:
        """The point where the break starts. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        self._from_ = validators.numeric(value, allow_empty = True)

    @property
    def repeat(self) -> Optional[int | float | Decimal]:
        """Defines an interval after which the break appears again. Defaults to ``0``.

        .. note::

          If ``0`` or :obj:`None <python:None>`, the breaks do not repeat.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._repeat

    @repeat.setter
    def repeat(self, value):
        self._repeat = validators.numeric(value,
                                          allow_empty = True,
                                          minimum = 0)

    @property
    def to(self) -> Optional[int | float | Decimal]:
        """The point where the break ends. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'break_size': as_dict.get('breakSize', None),
            'from_': as_dict.get('from', None),
            'repeat': as_dict.get('repeat', None),
            'to': as_dict.get('to', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'breakSize': self.break_size,
            'from': self.from_,
            'repeat': self.repeat,
            'to': self.to
        }

        return untrimmed
