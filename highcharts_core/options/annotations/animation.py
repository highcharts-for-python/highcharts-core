from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class AnnotationAnimation(HighchartsMeta):
    """Configuraiton settings that apply to the animation of an annotation."""

    def __init__(self, **kwargs):
        self._defer = None

        self.defer = kwargs.get('defer', None)

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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'defer': as_dict.get('defer', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'defer': self.defer
        }

        return untrimmed
