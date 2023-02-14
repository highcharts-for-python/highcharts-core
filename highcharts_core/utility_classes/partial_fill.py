from typing import Optional

from validator_collection import validators

from highcharts_core import errors, utility_functions
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class PartialFillOptions(HighchartsMeta):
    """A partial fill for each point, typically used to visualize how much of a task is
    performed.

    .. note::

      The partial fill object can be set either on series or point level.

    """

    def __init__(self, **kwargs):
        self._fill = None

        self.fill = kwargs.get('fill', None)

    @property
    def fill(self) -> Optional[str | Gradient | Pattern]:
        """The fill color to be used for partial fills. Defaults to
        :obj:`None <python:None>`, which applies a darker shade of the point color.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = utility_functions.validate_color(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return {
            'fill': as_dict.get('fill', None)
        }

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'fill': self.fill
        }
