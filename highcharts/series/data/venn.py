from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.series.data.base import DataBase
from highcharts.plot_options.drag_drop import DragDropOptions
from highcharts.utility_classes.data_labels import DataLabel


class VennData(DataBase):
    """Data point used to render an area within a Venn Diagram."""

    def __init__(self, **kwargs):
        self._data_labels = None
        self._drag_drop = None
        self._drilldown = None
        self._sets = None
        self._value = None

        self.data_labels = kwargs.pop('data_labels', None)
        self.drag_drop = kwargs.pop('drag_drop', None)
        self.drilldown = kwargs.pop('drilldown', None)
        self.sets = kwargs.pop('sets', None)
        self.value = kwargs.pop('value', None)

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
    def sets(self) -> Optional[List[str]]:
        """The set or sets the options will be applied to. Defaults to
        :obj:`None <python:None>`.

        If a single entry is defined, then it will create a new set. If more than one
        entry is defined, then it will define the overlap between the sets in the array.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return self._sets

    @sets.setter
    def sets(self, value):
        if not value:
            self._sets = None
        else:
            if checkers.is_iterable(value):
                self._sets = [validators.string(x) for x in value]
            else:
                self._sets = [validators.string(value)]

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The value of the point, resulting in a relative area of the circle, or area of
        overlap between two sets in the venn or euler diagram. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        self._value = validators.numeric(value_, allow_empty = True)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`VennData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`VennData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'VennData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Venn Data Point or be '
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

            'sets': as_dict.pop('sets', None),
            'value': as_dict.pop('value', None),

        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
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

            'sets': self.sets,
            'value': self.value,
        }

        return self.trim_dict(untrimmed)
