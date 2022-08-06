from typing import Optional
from decimal import Decimal

import datetime

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.series.data.base import DataBase
from highcharts.plot_options.drag_drop import DragDropOptions
from highcharts.utility_classes.data_labels import DataLabel
from highcharts.utility_classes.markers import Marker


class CartesianData(DataBase):
    """Data point that can be represented on a :term:`Cartesian` graph, featuring an ``x``
    and ``y`` value."""

    def __init__(self, **kwargs):
        self._data_labels = None
        self._drag_drop = None
        self._drilldown = None
        self._marker = None
        self._x = None
        self._y = None

        self.data_labels = kwargs.pop('data_labels', None)
        self.drag_drop = kwargs.pop('drag_drop', None)
        self.drilldown = kwargs.pop('drilldown', None)
        self.marker = kwargs.pop('marker', None)
        self.x = kwargs.pop('x', None)
        self.y = kwargs.pop('y', None)

        super().__init__(**kwargs)

    @property
    def data_labels(self) -> Optional[DataLabel]:
        """Individual data label for the data point.

        :rtype: :class:`DataLabel` or :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    @class_sensitive(DataLabel)
    def data_labels(self, value):
        self._data_labels = value

    @property
    def drag_drop(self) -> Optional[DragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(DragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def drilldown(self) -> Optional[str]:
        """The :meth:`id <SeriesBase.id>` of a series in the ``drilldown.series`` array
        to use as a drilldown destination for this point. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drilldown

    @drilldown.setter
    def drilldown(self, value):
        self._drilldown = validators.string(value, allow_empty = True)

    @property
    def marker(self) -> Optional[Marker]:
        """Options for the point markers of line-like series.

        :rtype: :class:`Marker` or :obj:`None <python:None>`
        """
        return self._marker

    @marker.setter
    @class_sensitive(Marker)
    def marker(self, value):
        self._marker = value

    @property
    def x(self) -> Optional[str | datetime.date | datetime.datetime | int | float | Decimal]:
        """The point's location on the x-axis. Defaults to :obj:`None <python:None>`.

        If :obj:`None <python:None>`, the point's position on the x-axis will be
        automatically determined based on its position in the series'
        :meth:`data <SeriesBase.data>` array. The first point will be given an ``x`` value
        of ``0``, or the series' :meth:`point_start <SeriesBase.point_start>` value.
        Each subsequent point will be incremented either by ``1`` or the value of
        :meth:`point_interval <SeriesBase.point_interval>`.

        :rtype: numeric or :class:`str <python:str>` or
          :class:`date <python:datetime.date>` or
          :class:`datetime <python:datetime.datetime>` or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        if value is None:
            self._x = None
        else:
            if checkers.is_datetime(value):
                value = validators.datetime(value)
            elif checkers.is_date(value):
                value = validators.date(value)
            elif checkers.is_numeric(value):
                value = validators.numeric(value)
            else:
                value = validators.string(value)

            self._x = value

    @property
    def y(self) -> Optional[int | float | Decimal | type(None) | constants.EnforcedNullType]:
        """The position of the data point on the Y-axis. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        if value is None or isinstance(value, constants.EnforcedNullType):
            self._y = None
        else:
            self._y = validators.numeric(value)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`CartesianData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`CartesianData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'CartesianData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType) or \
                 checkers.is_numeric(item):
                as_obj = cls(y = item)
            elif checkers.is_iterable(item):
                if len(item) != 2:
                    raise errors.HighchartsValueError(f'data expects either a 1D or 2D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
                as_dict = {
                    'x': item[0],
                    'y': item[1]
                }
                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Cartesian Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,

            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'marker': self.marker,
            'x': self.x,
            'y': self.y,
        }

        return untrimmed


class Cartesian3DData(CartesianData):
    """Variant of :class:`CartesianData` which supports three dimensions (an x, y, and
    z-axis)."""

    def __init__(self, **kwargs):
        self._z = None

        self.z = kwargs.pop('z', None)

        super().__init__(**kwargs)

    @property
    def z(self) -> Optional[int | float | Decimal | type(None) | constants.EnforcedNullType]:
        """The position of the data point on the z-axis. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._z

    @z.setter
    def z(self, value):
        if value is None or isinstance(value, constants.EnforcedNullType):
            self._z = None
        else:
            self._z = validators.numeric(value)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`Cartesian3DData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`Cartesian3DData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'Cartesian3DData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls(x = None,
                             y = None,
                             z = None)
            elif checkers.is_iterable(item):
                if len(item) == 3:
                    as_dict = {
                        'x': item[0],
                        'y': item[1],
                        'z': item[2]
                    }
                elif len(item) == 2:
                    as_dict = {
                        'x': None,
                        'y': item[0],
                        'z': item[1]
                    }
                else:
                    raise errors.HighchartsValueError(f'data expects either a 3D or 3D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Cartesian 3D Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')

            collection.append(as_obj)

        return collection

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'z': as_dict.pop('z', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,

            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'marker': self.marker,
            'x': self.x,
            'y': self.y,

            'z': self.z,
        }

        return untrimmed


class CartesianValueData(CartesianData):
    """Variant of :class:`CartesianData` which supports three values (an ``x``, ``y``, and
    ``value``)."""

    def __init__(self, **kwargs):
        self._point_padding = None
        self._value = None

        self.point_padding = kwargs.pop('point_padding', None)
        self.value = kwargs.pop('value', None)

        super().__init__(**kwargs)

    @property
    def point_padding(self) -> Optional[int | float | Decimal]:
        """Point padding for the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_padding

    @point_padding.setter
    def point_padding(self, value):
        self._point_padding = validators.numeric(value, allow_empty = True)

    @property
    def value(self) -> Optional[int | float | Decimal | type(None) | constants.EnforcedNullType]:
        """The ``value`` of the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        if value_ is None or isinstance(value_, constants.EnforcedNullType):
            self._value = None
        else:
            self._value = validators.numeric(value_)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`CartesianValueData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`CartesianValueData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'CartesianValueData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls(x = None,
                             y = None,
                             value = None)
            elif checkers.is_iterable(item):
                if len(item) == 3:
                    as_dict = {
                        'x': item[0],
                        'y': item[1],
                        'value': item[2]
                    }
                elif len(item) == 2:
                    as_dict = {
                        'x': None,
                        'y': item[0],
                        'value': item[1]
                    }
                else:
                    raise errors.HighchartsValueError(f'data expects either a 3D or 3D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Cartesian Value Data Point or be'
                                                  f' coercable to one. Could not coerce: '
                                                  f'{item}')

            collection.append(as_obj)

        return collection

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'point_padding': as_dict.pop('pointPadding', None),
            'value': as_dict.pop('value', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,

            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'marker': self.marker,
            'x': self.x,
            'y': self.y,

            'pointPadding': self.point_padding,
            'value': self.value,
        }

        return untrimmed
