from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.data.base import DataBase
from highcharts_core.options.series.data.collections import DataPointCollection
from highcharts_core.options.plot_options.drag_drop import DragDropOptions
from highcharts_core.utility_classes.data_labels import DataLabel


class WordcloudData(DataBase):
    """Data point that features a single and ``y`` value."""

    def __init__(self, **kwargs):
        self._data_labels = None
        self._drag_drop = None
        self._weight = None

        self.data_labels = kwargs.get('data_labels', None)
        self.drag_drop = kwargs.get('drag_drop', None)
        self.weight = kwargs.get('weight', None)

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
    def weight(self) -> Optional[int | float | Decimal]:
        """The weighting of a word. Defaults to :obj:`None <python:None>`.

        .. note::

          The weight decides the relative size of a word compared to the rest of the
          collection.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_list(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'WordcloudData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Wordcloud Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [1]

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return WordcloudData.from_ndarray(value)
    
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
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelrank', None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),

            'weight': as_dict.get('weight', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,

            'weight': self.weight,

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


        }

        return untrimmed


class WordcloudDataCollection(DataPointCollection):
    """A collection of :class:`WordcloudData` objects.

    .. note::
    
      When serializing to JS literals, if possible, the collection is serialized to a primitive
      array to boost performance within Python *and* JavaScript. However, this may not always be
      possible if data points have non-array-compliant properties configured (e.g. adjusting their 
      style, names, identifiers, etc.). If serializing to a primitive array is not possible, the
      results are serialized as JS literal objects.

    """

    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return WordcloudData


