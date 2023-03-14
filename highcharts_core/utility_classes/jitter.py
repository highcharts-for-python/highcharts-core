from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class Jitter(HighchartsMeta):
    """Apply a jitter effect for the rendered markers.

    When plotting discrete values, a little random noise may help telling the points
    apart. The jitter setting applies a random displacement of up to n axis units in
    either direction.

    So for example on a horizontal X axis, setting the ``jitter.x`` to ``0.24`` will
    render the point in a random position between 0.24 units to the left and 0.24
    units to the right of the true axis position. On a category axis, setting it to
    ``0.5`` will fill up the bin and make the data appear continuous.

    When rendered on top of a box plot or a column series, a jitter value of 0.24 will
    correspond to the underlying series' default ``group_padding`` and
    ``point_padding`` settings.

    """

    def __init__(self, **kwargs):
        self._x = None
        self._y = None

        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The maximal X offset for the random jitter effect. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The maximal Y offset for the random jitter effect. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return {
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None)
        }

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'x': self.x,
            'y': self.y
        }
