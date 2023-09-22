from typing import Optional

from validator_collection import checkers, validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.data.treemap import TreemapData
from highcharts_core.options.series.data.collections import DataPointCollection
from highcharts_core.utility_classes.markers import Marker


class SunburstData(TreemapData):
    """Data point that can features a ``parent``, a ``value``, and can be sliced."""

    def __init__(self, **kwargs):
        self._marker = None
        self._sliced = None

        self.marker = kwargs.get('marker', None)
        self.sliced = kwargs.get('sliced', None)

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
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return SunburstDataCollection.from_ndarray(value)

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

            'color_value': as_dict.get('colorValue', None),
            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'parent': as_dict.get('parent', None),
            'value': as_dict.get('value', None),

            'marker': as_dict.get('marker', None),
            'sliced': as_dict.get('sliced', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'marker': self.marker,
            'sliced': self.sliced,

            'colorValue': self.color_value,
            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'parent': self.parent,
            'value': self.value,

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
            'selected': self.selected
        }

        return untrimmed


class SunburstDataCollection(DataPointCollection):
    """A collection of :class:`SunburstData` objects.

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
        return SunburstData
