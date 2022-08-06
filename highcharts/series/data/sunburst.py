from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.series.data.base import DataBase
from highcharts.plot_options.drag_drop import DragDropOptions
from highcharts.utility_classes.data_labels import DataLabel
from highcharts.utility_classes.markers import Marker


class TreemapData(DataBase):
    """Data point that can features a ``parent`` and ``value``."""

    def __init__(self, **kwargs):
        self._color_value = None
        self._data_labels = None
        self._drag_drop = None
        self._drilldown = None
        self._parent = None
        self._value = None

        self.color_value = kwargs.pop('color_value', None)
        self.data_labels = kwargs.pop('data_labels', None)
        self.drag_drop = kwargs.pop('drag_drop', None)
        self.drilldown = kwargs.pop('drilldown', None)
        self.parent = kwargs.pop('parent', None)
        self.sliced = kwargs.pop('sliced', None)
        self.value = kwargs.pop('value', None)

        super().__init__(**kwargs)

    @property
    def color_value(self) -> Optional[int]:
        """If :meth:`SunburstOptions.color_axis` is set, this property determines which
        color should be applied to the data point from the scale of the color axis.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_value

    @color_value.setter
    def color_value(self, value):
        self._color_value = validators.integer(value, allow_empty = True)

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
    def parent(self) -> Optional[str]:
        """The :meth:`id <SunburstData.id>` of the parent data point. If no points match
        the value provided, or if set to :obj:`None <python:None>`, the parent will be set
        to the root. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = validators.string(value, allow_empty = True)

    @property
    def value(self) -> Optional[int | float | Decimal | type(None) | constants.EnforcedNullType]:
        """The value of the point, resulting in a relative area of the point in the
        sunburst. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
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
        """Generator method which produces a collection of :class:`TreemapData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`TreemapData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'TreemapData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Treemap Data Point or be '
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

            'color_value': as_dict.pop('colorValue', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'parent': as_dict.pop('parent', None),
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

            'colorValue': self.color_value,
            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'parent': self.parent,
            'value': self.value
        }

        return untrimmed


class SunburstData(DataBase):
    """Data point that can features a ``parent``, a ``value``, and can be sliced."""

    def __init__(self, **kwargs):
        self._marker = None
        self._sliced = None

        self.marker = kwargs.pop('marker', None)
        self.sliced = kwargs.pop('sliced', None)

        super().__init__(**kwargs)

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
    def sliced(self) -> Optional[bool]:
        """If ``True``, displays the data point as a slice offset from the center.
        Defaults to :obj:`None <python:None>`, which behaves as ``False``.

        .. note::

          If a data point is offste, its children are also offset.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._sliced

    @sliced.setter
    def sliced(self, value):
        if value is None:
            self._sliced = None
        else:
            self._sliced = bool(value)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`SunburstData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`SunburstData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'SunburstData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Sunburst Data Point or be '
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

            'color_value': as_dict.pop('colorValue', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'parent': as_dict.pop('parent', None),
            'value': as_dict.pop('value', None),

            'marker': as_dict.pop('marker', None),
            'sliced': as_dict.pop('sliced', None),
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

            'colorValue': self.color_value,
            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'parent': self.parent,
            'value': self.value,

            'marker': self.marker,
            'sliced': self.sliced,
        }

        return untrimmed
