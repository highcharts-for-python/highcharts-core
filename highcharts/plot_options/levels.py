from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.data_labels import DataLabel
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.states import States


class LevelOptions(HighchartsMeta):
    """Set options on specific levels. Takes precedence over series options, but not
    node and link options."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._color_by_point = None
        self._data_labels = None
        self._level = None
        self._link_opacity = 0.5
        self._states = None

        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.color_by_point = kwargs.pop('color_by_point', True)
        self.data_labels = kwargs.pop('data_labels', None)
        self.level = kwargs.pop('level', None)
        self.link_opacity = kwargs.pop('link_opacity', 0.5)
        self.states = kwargs.pop('states', None)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each column or bar. Defaults to
        ``'#ffffff'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding each column or bar. If
        :obj:`None <python:None>`, defaults to ``1`` when there is room for a border, but
        to ``0`` when the columns are so dense that a border would cover the next column.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def color_by_point(self) -> bool:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        self._color_by_point = bool(value)

    @property
    def data_labels(self) -> Optional[DataLabel]:
        """Options for the series data labels, appearing next to each data point.

        :rtype: :class:`DataLabel` or :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    @class_sensitive(DataLabel)
    def data_labels(self, value):
        self._data_labels = value

    @property
    def level(self) -> Optional[int]:
        """Decides which level takes effect from the options set in the levels object.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._level

    @level.setter
    def level(self, value):
        self._level = validators.integer(value, allow_empty = True)

    @property
    def link_opacity(self) -> Optional[int | float | Decimal]:
        """Opacity for the links between nodes in sankey or similar diagrams. Defaults to
        ``0.5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._link_opacity

    @link_opacity.setter
    def link_opacity(self, value):
        self._link_opacity = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def states(self) -> Optional[States]:
        """Configuration for state-specific configuration to apply to the data series.

        :rtype: :class:`States` or :obj:`None <python:None>`
        """
        return self._states

    @states.setter
    @class_sensitive(States)
    def states(self, value):
        self._states = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'color_by_point': as_dict.pop('colorByPoint', True),
            'data_labels': as_dict.pop('dataLabels', None),
            'level': as_dict.pop('level', None),
            'link_opacity': as_dict.pop('linkOpacity', 0.5),
            'states': as_dict.pop('states', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'border_color': self.border_color,
            'border_width': self.border_width,
            'color_by_point': self.color_by_point,
            'data_labels': self.data_labels,
            'level': self.level,
            'link_opacity': self.link_opacity,
            'states': self.states
        }

        return self.trim_dict(untrimmed)
