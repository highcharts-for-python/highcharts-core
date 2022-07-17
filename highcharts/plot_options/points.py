from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.position import Position
from highcharts.utility_classes.events import PointEvents


class ConnectorOptions(HighchartsMeta):
    """Options for the connector in the Series on point feature."""

    def __init__(self, **kwargs):
        self._dashstyle = None
        self._stroke = None
        self._width = 1

        self.dashstyle = kwargs.pop('dashstyle', None)
        self.stroke = kwargs.pop('stroke', None)
        self.width = kwargs.pop('width', 1)

    @property
    def dashstyle(self) -> Optional[str]:
        """Name of the dash style to use for the connector.

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
        return self._dashstyle

    @dashstyle.setter
    def dashstyle(self, value):
        if not value:
            self._dashstyle = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'dashstyle expects a recognized value'
                                                  f', but received: {value}')
            self._dashstyle = value

    @property
    def stroke(self) -> Optional[str]:
        """The color of the collector line.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        self._stroke = validators.string(value, allow_empty = True)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the connector line. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'dashstyle': as_dict.pop('dashstyle', None) or as_dict.pop('dashStyle', None),
            'stroke': as_dict.pop('stroke', None),
            'width': as_dict.pop('width', 1)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'dashstyle': self.dashstyle,
            'stroke': self.stroke,
            'width': self.width
        }

        return self.trim_dict(untrimmed)


class OnPointOptions(HighchartsMeta):
    """Options for the Series on point feature, which is currently only supported by
    ``pie`` and ``sunburst`` chargs."""

    def __init__(self, **kwargs):
        self._connector_options = None
        self._id = None
        self._position = None

        self.connector_options = kwargs.pop('connector_options', None)
        self.id = kwargs.pop('id', None)
        self.position = kwargs.pop('position', None)

    @property
    def connector_options(self) -> Optional[ConnectorOptions]:
        """Options for the connector in the Series on point feature.

        :rtype: :class:`ConnectorOptions` or :obj:`None <python:None>`
        """
        return self._connector_options

    @connector_options.setter
    @class_sensitive(ConnectorOptions)
    def connector_options(self, value):
        self._connector_options = value

    @property
    def id(self) -> Optional[str]:
        """The ``id`` of the point that we connect the series to.

        .. note::

          Only points with a given ``plot_x`` and ``plot_y`` values and map points are
          valid.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def position(self) -> Optional[Position]:
        """Options allowing to set a position and an offset of the series in the Series
        on point feature.

        :rtype: :class:`Position` or :obj:`None <python:None>`
        """
        return self._position

    @position.setter
    @class_sensitive(Position)
    def position(self, value):
        self._position = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'connector_options': as_dict.pop('connector_options', None),
            'id': as_dict.pop('id', None),
            'position': as_dict.pop('position', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'connectorOptions': self.connector_options,
            'id': self.id,
            'position': self.position
        }

        return self.trim_dict(untrimmed)


class Point(HighchartsMeta):
    """Properties for each single point."""

    def __init__(self, **kwargs):
        self._events = None

        self.events = kwargs.pop('events', None)

    @property
    def events(self) -> Optional[PointEvents]:
        """Events for each single point.

        :rtype: :class:`PointEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(PointEvents)
    def events(self, value):
        self._events = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'events': as_dict.pop('events', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'events': self.events
        }

        return self.trim_dict(untrimmed)
