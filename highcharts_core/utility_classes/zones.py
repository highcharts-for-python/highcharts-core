from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.markers import Marker


class Zone(HighchartsMeta):
    """A zone defined within a series.

    Zones can be applied to the X axis, Y axis or Z axis for bubbles, according to the
    :meth:`zone_axis <AreaOptions.zone_axis>` option.

    """

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._dash_style = None
        self._fill_color = None
        self._value = None

        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.dash_style = kwargs.get('dash_style', None)
        self.fill_color = kwargs.get('fill_color', None)
        self.value = kwargs.get('value', None)

    @property
    def class_name(self) -> Optional[str]:
        """A custom class name for the zone.

        .. warning::

          Supported in :term:`styled mode` only.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """Defines the color of the series. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the graph, or for some series types the
        outline of each shape. Defaults to :obj:`None <python:None>`.

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
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        if not value:
            self._dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'dash_style expects a recognized value'
                                                  f', but received: {value}')
            self._dash_style = value

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """Fill color or gradient for the area.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        from highcharts_core import utility_functions
        self._fill_color = utility_functions.validate_color(value)

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The value up to where the zone extends. If :obj:`None <python:None>`, the zone
        stretches to the last value in the series. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        self._value = validators.numeric(value_, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'dash_style': as_dict.get('dashStyle', None),
            'fill_color': as_dict.get('fillColor', None),
            'value': as_dict.get('value', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'dashStyle': self.dash_style,
            'fillColor': self.fill_color,
            'value': self.value
        }

        return untrimmed


class ClusterZone(HighchartsMeta):
    """A zone defined for a group of Clusters."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._from = None
        self._marker = None
        self._to = None

        self.class_name = kwargs.get('class_name', None)
        self.from_ = kwargs.get('from_', None)
        self.marker = kwargs.get('marker', None)
        self.to = kwargs.get('to', None)

    @property
    def class_name(self) -> Optional[str]:
        """A custom class name for the zone.

        .. warning::

          Supported in :term:`styled mode` only.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def from_(self) -> Optional[int | float | Decimal]:
        """The value where the zone starts.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._from

    @from_.setter
    def from_(self, value):
        self._from = validators.numeric(value, allow_empty = True)

    @property
    def marker(self) -> Optional[Marker]:
        """Settings for the cluster marker belonging to the zone.

        :rtype: :class:`Marker` or :obj:`None <python:None>`
        """
        return self._marker

    @marker.setter
    @class_sensitive(Marker)
    def marker(self, value):
        self._marker = value

    @property
    def to(self) -> Optional[int | float | Decimal]:
        """The value where the zone ends.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'from_': as_dict.get('from', None),
            'marker': as_dict.get('marker', None),
            'to': as_dict.get('to', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'from': self.from_,
            'marker': self.marker,
            'to': self.to
        }

        return untrimmed
