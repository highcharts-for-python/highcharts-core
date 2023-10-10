from typing import Optional, List, Dict
from decimal import Decimal

import datetime

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.data.base import DataBase
from highcharts_core.options.series.data.cartesian import CartesianData, CartesianDataCollection
from highcharts_core.options.plot_options.drag_drop import DragDropOptions
from highcharts_core.utility_classes.data_labels import DataLabel
from highcharts_core.utility_classes.markers import Marker
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class RangeData(DataBase):
    """Data point that consists of an ``x``, ``low``, and ``high`` value."""

    def __init__(self, **kwargs):
        self._data_labels = None
        self._drag_drop = None
        self._drilldown = None
        self._high = None
        self._low = None
        self._marker = None
        self._x = None

        self.data_labels = kwargs.get('data_labels', None)
        self.drag_drop = kwargs.get('drag_drop', None)
        self.drilldown = kwargs.get('drilldown', None)
        self.high = kwargs.get('high', None)
        self.low = kwargs.get('low', None)
        self.marker = kwargs.get('marker', None)
        self.x = kwargs.get('x', None)

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
    def high(self) -> Optional[int | float | Decimal]:
        """The high or maximum value for the data point. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._high

    @high.setter
    def high(self, value):
        self._high = validators.numeric(value, allow_empty = True)

    @property
    def low(self) -> Optional[int | float | Decimal]:
        """The low or minimum value for the data point. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._low

    @low.setter
    def low(self, value):
        self._low = validators.numeric(value, allow_empty = True)

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

    @classmethod
    def from_list(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass

        if not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'RangeData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls(x = None,
                             low = None,
                             high = None)
            elif checkers.is_iterable(item):
                if len(item) == 2:
                    as_dict = {
                        'low': item[0],
                        'high': item[1]
                    }
                elif len(item) == 3:
                    as_dict = {
                        'x': item[0],
                        'low': item[1],
                        'high': item[2]
                    }
                else:
                    raise errors.HighchartsValueError(f'data expects either a 3D or 2D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')

                as_obj = cls.from_dict(as_dict)
                if checkers.is_string(as_obj.x) and not as_obj.name:
                    as_obj.name = as_obj.x
                    as_obj.x = None
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be an AreaRangeData Point or be '
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
        return RangeDataCollection.from_ndarray(value)

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [1, 2, 3]

    @classmethod
    def _get_props_from_array(cls, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        prop_list = {
            None: ['x', 'low', 'high', 'name'],
            3: ['x', 'low', 'high'],
            2: ['low', 'high'],
        }
        return cls._get_props_from_array_helper(prop_list, length)

    def to_array(self, force_object = False) -> List | Dict:
        """Generate the array representation of the data point (the inversion 
        of 
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`).
        
        .. warning::
        
          If the data point *cannot* be serialized to a JavaScript array,
          this method will instead return the untrimmed :class:`dict <python:dict>`
          representation of the data point as a fallback.

        :param force_object: if ``True``, forces the return of the instance's
          untrimmed :class:`dict <python:dict>` representation. Defaults to ``False``.
        :type force_object: :class:`bool <python:bool>`

        :returns: The array representation of the data point.
        :rtype: :class:`list <python:list>` of values or :class:`dict <python:dict>`
        """
        if self.requires_js_object or force_object:
            return self._to_untrimmed_dict()
        
        if self.x is not None:
            x = self.x
        elif self.name is not None:
            x = self.name
        else:
            x = constants.EnforcedNull
            
        if self.low is not None:
            low = self.low
        else:
            low = constants.EnforcedNull
            
        if self.high is not None:
            high = self.high
        else:
            high = constants.EnforcedNull

        if self.x is None and self.name is None:
            return [low, high]
            
        return [x, low, high]

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
            'label_rank': as_dict.get('labelrank',
                                      None) or as_dict.get('labelRank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'high': as_dict.get('high', None),
            'low': as_dict.get('low', None),
            'marker': as_dict.get('marker', None),
            'x': as_dict.get('x', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'high': self.high,
            'low': self.low,
            'marker': self.marker,
            'x': self.x,

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


class RangeDataCollection(CartesianDataCollection):
    """A collection of :class:`RangeData` objects.

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
        return RangeData


class ConnectedRangeData(CartesianData):
    """Variant of :class:`CartesianData` which extends the class with connector
    attributes."""

    def __init__(self, **kwargs):
        self._connector_color = None
        self._connector_width = None
        self._low_color = None

        self.connector_color = kwargs.get('connector_color', None)
        self.connector_width = kwargs.get('connector_width', None)
        self.low_color = kwargs.get('low_color', None)

        super().__init__(**kwargs)

    @property
    def connector_color(self) -> Optional[str]:
        """Color of the line that connects the dumbbell point's values. If
        :obj:`None <python:None>`, applies the series' color. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._connector_color

    @connector_color.setter
    def connector_color(self, value):
        self._connector_color = validators.string(value, allow_empty = True)

    @property
    def connector_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the line that connects the dumbbell point's values. Defaults to
        ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._connector_width

    @connector_width.setter
    def connector_width(self, value):
        self._connector_width = validators.numeric(value, allow_empty = True)

    @property
    def low_color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the start markers in a dumbbell graph. Defaults to ``'#333333'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._low_color

    @low_color.setter
    def low_color(self, value):
        from highcharts_core import utility_functions
        self._low_color = utility_functions.validate_color(value)

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return ConnectedRangeDataCollection.from_ndarray(value)

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
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'marker': as_dict.get('marker', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),

            'connector_color': as_dict.get('connectorColor', None),
            'connector_width': as_dict.get('connectorWidth', None),
            'low_color': as_dict.get('lowColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'connectorColor': self.connector_color,
            'connectorWidth': self.connector_width,
            'lowColor': self.low_color
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class ConnectedRangeDataCollection(CartesianDataCollection):
    """A collection of :class:`ConnectedRangeData` objects.

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
        return ConnectedRangeData
