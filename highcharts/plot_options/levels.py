from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors, constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.data_labels import DataLabel
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.states import States


class BaseLevelOptions(HighchartsMeta):
    """Base class from which other Level Options classes inherit."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._data_labels = None
        self._level = None

        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.data_labels = kwargs.pop('data_labels', None)
        self.level = kwargs.pop('level', None)

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

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'level': as_dict.pop('level', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'dataLabels': self.data_labels,
            'level': self.level
        }
        parent_as_dict = super().to_dict()
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class LevelOptions(BaseLevelOptions):
    """Set options on specific levels. Takes precedence over series options, but not
    node and link options."""

    def __init__(self, **kwargs):
        self._color_by_point = None
        self._link_opacity = 0.5
        self._states = None

        self.color_by_point = kwargs.pop('color_by_point', True)
        self.link_opacity = kwargs.pop('link_opacity', 0.5)
        self.states = kwargs.pop('states', None)

        super().__init__(**kwargs)

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
            'data_labels': as_dict.pop('dataLabels', None),
            'level': as_dict.pop('level', None),

            'color_by_point': as_dict.pop('colorByPoint', True),
            'link_opacity': as_dict.pop('linkOpacity', 0.5),
            'states': as_dict.pop('states', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'colorByPoint': self.color_by_point,
            'dataLabels': self.data_labels,
            'linkOpacity': self.link_opacity,
            'states': self.states
        }
        parent_as_dict = super().to_dict()
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class ColorVariation(HighchartsMeta):
    """Configuration for a color variation to apply to all points on a level."""

    def __init__(self, **kwargs):
        self._key = None
        self._to = None

        self.key = kwargs.pop('key', None)
        self.to = kwargs.pop('to', None)

    @property
    def key(self) -> Optional[str]:
        """The key of a color variation. Currently only supports ``'brightness'``.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._key

    @key.setter
    def key(self, value):
        self._key = validators.string(value, allow_empty = True)

    @property
    def to(self) -> Optional[int | float | Decimal]:
        """The ending value of a color variation. The last sibling will receive this
        value. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'key': as_dict.pop('key', None),
            'to': as_dict.pop('to', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'key': self.key,
            'to': self.to
        }

        return self.trim_dict(untrimmed)


class LevelSize(HighchartsMeta):
    """Determines the width of the ring per level."""

    def __init__(self, **kwargs):
        self._unit = None
        self._value = None

        self.unit = kwargs.pop('unit', None)
        self.value = kwargs.pop('value', None)

    @property
    def unit(self) -> Optional[str]:
        """Indication of how to interpret :meth:`LevelSize.value`. Defaults to
        ``'weight'``.

        Accepts the following options:

          * ``'percentage'`` - gives a width relative to result of outer radius minus
            inner radius
          * ``'pixels'`` - gives the ring a fixed width in pixels
          * ``'weight'`` - takes the remaining width after percentage and pixels, and
            distributes it accross all "weighted" levels. The value relative to the sum of
            all weights determines the width.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._unit

    @unit.setter
    def unit(self, value):
        if not value:
            self._unit = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['percentage', 'pixels', 'weight']:
                raise errors.HighchartsValueError(f'unit expects "weight", "pixels", or '
                                                  f'"percentage". Received: {value}')
            self._unit = value

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The value used for calculating the width of the ring. Defaults to ``1``.

        .. note::

          The interpretation of this value is determined by :meth:`LevelSize.unit`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        self._value = validators.numeric(value_, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'unit': as_dict.pop('unit', None),
            'value': as_dict.pop('value', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'unit': self.unit,
            'value': self.value
        }

        return self.trim_dict(untrimmed)


class SunburstLevelOptions(BaseLevelOptions):
    """Set options on specific levels for Sunburst Charts. Takes precedence over series
    options, but not node and link options."""

    def __init__(self, **kwargs):
        self._border_dash_style = None
        self._color = None
        self._color_variation = None
        self._level_size = None

        self.border_dash_style = kwargs.pop('border_dash_style', None)
        self.color = kwargs.pop('color', None)
        self.color_variation = kwargs.pop('color_variation', None)
        self.level_size = kwargs.pop('level_size', None)

        super().__init__(**kwargs)

    @property
    def border_dash_style(self) -> Optional[str]:
        """The dash style applied to all points which lie on the same level. Defaults to
        :obj:`None <python:None>`.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_dash_style

    @border_dash_style.setter
    def border_dash_style(self, value):
        if not value:
            self._border_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'border_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._border_dash_style = value

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """Set a color on all points which lies on the same level. Defaults to
        :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def color_variation(self) -> Optional[ColorVariation]:
        """Set a color variation on all points which lie on the same level. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`ColorVariation` or :obj:`None <python:None>`
        """
        return self._color_variation

    @color_variation.setter
    @class_sensitive(ColorVariation)
    def color_variation(self, value):
        self._color_variation = value

    @property
    def level_size(self) -> Optional[LevelSize]:
        """Set the width of the ring for all points which lie on the same level. Defaults
        to :obj:`None <python:None>`.

        :rtype: :class:`LevelSize` or :obj:`None <python:None>`
        """
        return self._level_size

    @level_size.setter
    @class_sensitive(LevelSize)
    def level_size(self, value):
        self._level_size = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'level': as_dict.pop('level', None),

            'border_dash_style': as_dict.pop('borderDashStyle', None),
            'color': as_dict.pop('color', None),
            'color_variation': as_dict.pop('colorVariation', None),
            'level_size': as_dict.pop('levelSize', None)
         }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'borderDashStyle': self.border_dash_style,
            'color': self.color,
            'colorVariation': self.color_variation,
            'levelSize': self.level_size
        }

        parent_as_dict = super().to_dict()
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
