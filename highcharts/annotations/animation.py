from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class AnnotationAnimation(HighchartsMeta):
    """Configuraiton settings that apply to the animation of an annotation."""

    def __init__(self, **kwargs):
        self._defer = None

        self.defer = kwargs.pop('defer', None)

    @property
    def defer(self) -> Optional[int | float | Decimal]:
        """The animation delay time in milliseconds. Defaults to
        :obj:`None <python:None>`.

        Set to ``0`` to render the annotation immediately.

        Set to :obj:`None <python:None>` to inherit the defer time from
        :meth:`Series.animation.defer`.

        :returns: The animation delay time in milliseconds.
        :rtype: numeric or :obj:`None <python:None>`

        :raises ValueError: if set to a negative number
        """
        return self._defer

    @defer.setter
    def defer(self, value):
        self._defer = validators.numeric(value,
                                         allow_empty = True,
                                         minimum = 0)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'defer': as_dict.pop('defer', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'defer': self.defer
        }

        as_dict = self.trim_dict(untrimmed)

        return as_dict
