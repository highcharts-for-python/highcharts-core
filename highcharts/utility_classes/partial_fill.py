from typing import Optional

from validator_collection import validators

from highcharts import errors
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class PartialFillOptions(HighchartsMeta):
    """A partial fill for each point, typically used to visualize how much of a task is
    performed.

    .. note::

      The partial fill object can be set either on series or point level.

    """

    def __init__(self, **kwargs):
        self._fill = None

        self.fill = kwargs.pop('fill', None)

    @property
    def fill(self) -> Optional[str | Gradient | Pattern]:
        """The fill color to be used for partial fills. Defaults to
        :obj:`None <python:None>`, which applies a darker shade of the point color.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        if not value:
            self._fill = None
        elif isinstance(value, (Gradient, Pattern)):
            self._fill = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._fill = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill = Gradient.from_dict(value)
                else:
                    self._fill = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._fill = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._fill = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill = Pattern.from_dict(value)
                else:
                    self._fill = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._fill = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @classmethod
    def from_dict(cls, as_dict):
        return cls(**{
            'fill': as_dict.pop('fill', None)
        })

    def _to_untrimmed_dict(self) -> dict:
        return {
            'fill': self.fill
        }
