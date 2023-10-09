from typing import Optional, List, Dict
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.options.series.data.cartesian import CartesianData
from highcharts_core.options.series.data.collections import DataPointCollection


class BoxPlotData(CartesianData):
    """Variant of :class:`CartesianData` which is used for data points in a boxplot."""

    def __init__(self, **kwargs):
        self._box_dash_style = None
        self._high = None
        self._low = None
        self._median = None
        self._median_dash_style = None
        self._q1 = None
        self._q3 = None
        self._stem_dash_style = None
        self._whisker_dash_style = None

        self.box_dash_style = kwargs.get('box_dash_style', None)
        self.high = kwargs.get('high', None)
        self.low = kwargs.get('low', None)
        self.median = kwargs.get('median', None)
        self.median_dash_style = kwargs.get('median_dash_style', None)
        self.q1 = kwargs.get('q1', None)
        self.q3 = kwargs.get('q3', None)
        self.stem_dash_style = kwargs.get('stem_dash_style', None)
        self.whisker_dash_style = kwargs.get('whisker_dash_style', None)

        super().__init__(**kwargs)

    @property
    def box_dash_style(self) -> Optional[str]:
        """The dash style of the box.

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
        return self._box_dash_style

    @box_dash_style.setter
    def box_dash_style(self, value):
        if not value:
            self._box_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'box_dash_style expects a recognized '
                                                  f'value, but received: {value}')
            self._box_dash_style = value

    @property
    def high(self) -> Optional[int | float | Decimal]:
        """The highest value in the sample set. The top whisker is drawn here. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._high

    @high.setter
    def high(self, value):
        self._high = validators.numeric(value, allow_empty = True)

    @property
    def low(self) -> Optional[int | float | Decimal]:
        """The lowest value in the sample set. The bottom whisker is drawn here. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._low

    @low.setter
    def low(self, value):
        self._low = validators.numeric(value, allow_empty = True)

    @property
    def median(self) -> Optional[int | float | Decimal]:
        """The median value in the sample set. This is drawn as a line through the middle
        of the box. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._median

    @median.setter
    def median(self, value):
        self._median = validators.numeric(value, allow_empty = True)

    @property
    def median_dash_style(self) -> Optional[str]:
        """The dash style of the median. Defaults to ``'Solid'``.

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
        return self._median_dash_style

    @median_dash_style.setter
    def median_dash_style(self, value):
        if not value:
            self._median_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'median_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._median_dash_style = value

    @property
    def q1(self) -> Optional[int | float | Decimal]:
        """The lower quartile in the sample set. This is the bottom of the box. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._q1

    @q1.setter
    def q1(self, value):
        self._q1 = validators.numeric(value, allow_empty = True)

    @property
    def q3(self) -> Optional[int | float | Decimal]:
        """The higher quartile in the sample set. This is the top of the box. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._q3

    @q3.setter
    def q3(self, value):
        self._q3 = validators.numeric(value, allow_empty = True)

    @property
    def stem_dash_style(self) -> Optional[str]:
        """The dash style of the :term:`stem`, the vertical line extending from the box to
        the whiskers. Defaults to ``'Solid'``.

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
        return self._stem_dash_style

    @stem_dash_style.setter
    def stem_dash_style(self, value):
        if not value:
            self._stem_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'stem_dash_style expects a recognized'
                                                  f' value, but received: {value}')
            self._stem_dash_style = value

    @property
    def whisker_dash_style(self) -> Optional[str]:
        """The dash style of the whiskers. Defaults to ``'Solid'``.

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
        return self._whisker_dash_style

    @whisker_dash_style.setter
    def whisker_dash_style(self, value):
        if not value:
            self._whisker_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'whisker_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._whisker_dash_style = value

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
            if checkers.is_type(item, 'BoxPlotData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            elif checkers.is_iterable(item):
                if len(item) == 6:
                    as_dict = {
                        'x': item[0],
                        'low': item[1],
                        'q1': item[2],
                        'median': item[3],
                        'q3': item[4],
                        'high': item[5]
                    }
                elif len(item) == 5:
                    as_dict = {
                        'x': None,
                        'low': item[0],
                        'q1': item[1],
                        'median': item[2],
                        'q3': item[3],
                        'high': item[4]
                    }
                else:
                    raise errors.HighchartsValueError(f'data expects either a 6D or 5D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')

                as_obj = cls.from_dict(as_dict)
                if checkers.is_string(as_obj.x) and not as_obj.name:
                    as_obj.name = as_obj.x
                    as_obj.x = None
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a BoxPlot Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [1, 5, 6]

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return BoxPlotDataCollection.from_ndarray(value)
    
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
            None: ['x', 'low', 'q1', 'median', 'q3', 'high', 'name'],
            6: ['x', 'low', 'q1', 'median', 'q3', 'high'],
            5: ['low', 'q1', 'median', 'q3', 'high'],
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
            
        if self.q1 is not None:
            q1 = self.q1
        else:
            q1 = constants.EnforcedNull
            
        if self.median is not None:
            median = self.median
        else:
            median = constants.EnforcedNull
            
        if self.q3 is not None:
            q3 = self.q3
        else:
            q3 = constants.EnforcedNull
            
        if self.high is not None:
            high = self.high
        else:
            high = constants.EnforcedNull

        if self.x is None and self.name is None:
            return [low, q1, median, q3, high]

        return [x, low, q1, median, q3, high]

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
            'drilldown': as_dict.get('drilldown', None),
            'marker': as_dict.get('marker', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),

            'box_dash_style': as_dict.get('boxDashStyle', None),
            'high': as_dict.get('high', None),
            'low': as_dict.get('low', None),
            'median': as_dict.get('median', None),
            'median_dash_style': as_dict.get('medianDashStyle', None),
            'q1': as_dict.get('q1', None),
            'q3': as_dict.get('q3', None),
            'stem_dash_style': as_dict.get('stemDashStyle', None),
            'whisker_dash_style': as_dict.get('whiskerDashStyle', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'boxDashStyle': self.box_dash_style,
            'high': self.high,
            'low': self.low,
            'median': self.median,
            'medianDashStyle': self.median_dash_style,
            'q1': self.q1,
            'q3': self.q3,
            'stemDashStyle': self.stem_dash_style,
            'whiskerDashStyle': self.whisker_dash_style,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class BoxPlotDataCollection(DataPointCollection):
    """A collection of :class:`BoxPlotData` objects.

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
        return BoxPlotData
