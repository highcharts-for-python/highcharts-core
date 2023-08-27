from typing import Optional, List
from collections import UserDict

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from validator_collection import checkers, validators

from highcharts_core import constants, errors, utility_functions
from highcharts_core.decorators import validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.js_literal_functions import serialize_to_js_literal, assemble_js_literal
from highcharts_core.options.series.data.base import DataBase


class DataPointCollection(HighchartsMeta):
    """Collection of data points.
    
    This class stores numerical values that Highcharts can interpret 
    from a primitive array in a :class:`numpy.ndarray <numpy:numpy.ndarray>`
    (in the 
    :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollection.ndarray>`
    property) and non-numerical data point properties as Highcharts for Python 
    :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`-descended 
    objects (in the 
    :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollection.data_points>`
    property).
    
    .. note::
    
      When serializing to JS literals, if possible, the collection is serialized to a primitive
      array to boost performance within Python *and* JavaScript. However, this may not always be
      possible if data points have non-array-compliant properties configured (e.g. adjusting their 
      style, names, identifiers, etc.). If serializing to a primitive array is not possible, the
      results are serialized as JS literal objects.

    """
    
    def __init__(self, **kwargs):
        self._data_points = None
        self._ndarray = None
        
        self.data_points = kwargs.get('data_points', None)
        self.ndarray = kwargs.get('ndarray', None)
        
    @property
    def data_points(self) -> Optional[List[DataBase]]:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`DataBase` or 
          :obj:`None <python:None>`
        """
        return self._data_points
    
    @data_points.setter
    def data_points(self, value):
        if not value:
            self._data_points = None
        else:
            validated = validate_types(value,
                                       types = self._get_data_point_class(),
                                       force_iterable = True)
            self._data_points = validated

    @property
    def ndarray(self) -> Optional[np.ndarray]:
        """The :class:`numpy.ndarray <numpy:numpy.ndarray>` instance that contains the
        data point collection's numerical values.
        
        :rtype: :class:`numpy.ndarray <numpy:numpy.ndarray>` or
          :obj:`None <python:None>`
        """
        return self._ndarray

    @ndarray.setter
    def ndarray(self, value):
        if value is None:
            self._ndarray = None
            as_array = False
        elif not isinstance(value, 
                            np.ndarray) and checkers.is_iterable(value,
                                                                 forbid_literals = (str, bytes, dict, UserDict)):
            as_array = utility_functions.to_ndarray(value)
        else:
            as_array = value

        if isinstance(as_array, np.ndarray):
            if as_array.ndim not in self._get_supported_dimensions():
                supported_dimensions = self._get_supported_dimensions()
                supported_as_str = ', '.join([str(x) for x in supported_dimensions[:-1]])
                supported_as_str += f', or {str(supported_dimensions[-1])}'
                
                raise errors.HighchartsValueError(f'{self.__name__} supports arrays with '
                                                f'{supported_as_str} dimensions. Received'
                                                f' a value with: {as_array.ndim}')

            self._ndarray = as_array
        elif value is not None:
            raise errors.HighchartsValueError(f'.ndarray expects a numpy.ndarray '
                                              f'or an iterable that can easily be '
                                              f'coerced to one. Received: '
                                              f'{value.__class__.__name__}')

    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return DataBase

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """The number of dimensions supported by the collection.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return cls._get_data_point_class()._get_supported_dimensions()

    @classmethod
    def _get_props_from_array(cls) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`
        method.
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        data_point_cls = cls._get_data_point_class()
        
        return data_point_cls._get_props_from_array()

    @classmethod
    def from_array(cls, value):
        """Creates a 
        :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>` 
        instance from an array of values.
        
        :param value: The value that should contain the data which will be converted into
          data point instances.
        :type value: iterable or :class:`numpy.ndarray <numpy:numpy.ndarray>`
       
        :returns: A single-object collection of data points.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          or :obj:`None <python:None>`
          
        :raises HighchartsDependencyError: if `NumPy <https://numpy.org>`__ is not installed
        """
        if not HAS_NUMPY:
            raise errors.HighchartsDependencyError('DataPointCollection requires NumPy '
                                                   'be installed. The runtime '
                                                   'environment does not currently have '
                                                   'NumPy installed. Please use the data '
                                                   'point pattern instead, or install NumPy'
                                                   ' using "pip install numpy" or similar.')
        
        if isinstance(value, np.ndarray) and value.dtype != np.dtype('O'):
            return cls.from_ndarray(value)
        elif isinstance(value, np.ndarray):
            as_list = value.tolist()
        else:
            as_list = value

        data_points = cls._get_data_point_class().from_array(as_list)

        return cls(data_points = data_points)

    @classmethod
    def from_ndarray(cls, value: np.ndarray):
        """Creates a 
        :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>` 
        instance from an array of values.
        
        :param value: The value that should contain the data which will be converted into
          data point instances.
        :type value: :class:`numpy.ndarray <numpy:numpy.ndarray>`
       
        :returns: A single-object collection of data points.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          or :obj:`None <python:None>`
          
        :raises HighchartsDependencyError: if `NumPy <https://numpy.org>`__ is not installed
        """
        if not HAS_NUMPY:
            raise errors.HighchartsDependencyError('DataPointCollection requires NumPy '
                                                   'be installed. The runtime '
                                                   'environment does not currently have '
                                                   'NumPy installed. Please use the data '
                                                   'point pattern instead, or install NumPy'
                                                   ' using "pip install numpy" or similar.')
        
        if not isinstance(value, np.ndarray):
            raise errors.HighchartsValueError(f'Expected a NumPy ndarray instance, but '
                                              f'received: {value.__class__.__name__}')

        if value.dtype == np.dtype('O'):
            return cls.from_array(value.tolist())

        return cls(ndarray = value)
    
    @property
    def requires_js_object(self) -> bool:
        """Indicates whether or not the data point *must* be serialized to a JS literal 
        object or whether it can be serialized to a primitive array.
        
        :returns: ``True`` if the data point *must* be serialized to a JS literal object.
          ``False`` if it can be serialized to an array.
        :rtype: :class:`bool <python:bool>`
        """
        if not self.data_points:
            return False

        from_array_props = [utility_functions.to_camelCase(x)
                            for x in self._get_props_from_array()]
        
        data_points_as_dict = [x.to_dict() for x in self.data_points]
        for data_point in data_points_as_dict:
            for prop in from_array_props:
                if prop in data_point:
                    del data_point[prop]
                    
        data_points = sum([1 for x in data_points_as_dict if x])
        
        if data_points:
            return True
        
        return False

    def _assemble_data_points(self):
        """Assemble a collection of 
        :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`-descended
        objects from the provided data. The algorithm should be as follows:
        
        1. Take any data points provided in the 
          :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollection.data_points>` property.
        
        2. If the 
          :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointcollection.data_points>`
          is empty, return the data points as-is.
        
        3. Strip the data points of properties from the 
          :meth:`._get_props_from_array() <highcharts_core.options.series.data.collections.DataPointCollection._get_props_from_array>`
          method.
          
        4. Populate the data points with property values from
          :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointcollection.data_points>`.
          
        5. Return the re-hydrated data points.
        
        :rtype: :class:`list <python:list>` of 
          :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`
          instances.

        """
        data_points = [x for x in self.data_points]
        if self.ndarray is None:
            return data_points
        
        for data_point in data_points:
            for prop in self._get_props_from_array():
                if getattr(data_point, prop) is not None:
                    data_point.prop = None
                    
        if len(data_points) < len(self.ndarray):
            missing = len(self.ndarray) - len(data_points)
            for i in range(missing):
                data_points.append(self._data_point_class())
                    
        for index in range(len(self.ndarray)):
            data_points[index].populate_from_array(self.ndarray[index])

        return data_points

    def _assemble_ndarray(self):
        """Assemble a :class:`numpy.ndarray <numpy:numpy.ndarray>` from the contents
        of
        :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollection.data_points>`.
        
        .. warning::
        
          This method will *ignore* properties that Highcharts (JS) cannot support in a 
          primitive nested array structure.
        
        :returns: A :class:`numpy.ndarray <numpy:numpy.ndarray>` of the data points.
        :rtype: :class:`numpy.ndarray <numpy:numpy.ndarray>`
        
        """
        if not self.data_points:
            return np.ndarray.empty()

        as_list = [[getattr(data_point, x, constants.EnforcedNull)
                    for x in self._get_props_from_array()]
                   for data_point in self.data_points]
        
        return utility_functions.to_ndarray(as_list)

    def to_array(self, force_object = False, force_ndarray = False) -> List:
        """Generate the array representation of the data points (the inversion 
        of 
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`).
        
        .. warning::
        
          If any data points *cannot* be serialized to a JavaScript array,
          this method will instead return the untrimmed :class:`dict <python:dict>`
          representation of the data points as a fallback.

        :param force_object: if ``True``, forces the return of the instance's
          untrimmed :class:`dict <python:dict>` representation. Defaults to ``False``.

          .. warning::
          
            Values in
            :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollection.ndarray>`
            are *ignored* within this operation in favor of data points stored in
            :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollection.data_points>`.
            
            However, if there are no data points in
            :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollection.data_points>`
            then data point objects will be assembled based on
            :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollection.ndarray>`.
            
        :type force_object: :class:`bool <python:bool>`
        
        :param force_ndarray: if ``True``, forces the return of the instance's
          data points as a :class:`numpy.ndarray <numpy:numpy.ndarray>`. Defaults to 
          ``False``.
          
          .. warning::
          
            Properties of any 
            :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollection.data_points>`
            are *ignored* within this operation if
            :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollection.ndarray>`
            is populated.
            
            However, if
            :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollection.ndarray>`
            is not populated, then a :class:`numpy.ndarray <numpy:numpy.ndarray>` will 
            be assembled from values in 
            :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollection.data_points>`
            (ignoring properties that Highcharts (JS) cannot interpret as a primitive array).
            
        :type force_ndarray: :class:`bool <python:bool>`
        
        :raises HighchartsValueError: if both `force_object` and `force_ndarray` are
          ``True``

        :returns: The array representation of the data point collection.
        :rtype: :class:`list <python:list>`
        """
        if force_object and force_ndarray:
            raise errors.HighchartsValueError('force_object and force_ndarray cannot '
                                              'both be True')

        if self.ndarray is None and not self.data_points:
            return []
        
        if force_object and self.data_points:
            return [x for x in self.data_points]
        elif force_object and self.ndarray is not None:
            return [x for x in self._assemble_data_points()]
            
        if force_ndarray and self.ndarray is not None:
            return utility_functions.from_ndarray(self.ndarray)
        elif force_ndarray and self.data_points:
            as_ndarray = self._assemble_ndarray()
            return utility_functions.from_ndarray(as_ndarray)
        
        if self.ndarray is not None and not self.requires_js_object:
            return utility_functions.from_ndarray(self.ndarray)
        
        if self.data_points:
            return [x for x in self.data_points]

        return [x for x in self._assemble_data_points()]

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
            'ndarray': as_dict.get('ndarray', None),
            'data_points': as_dict.get('dataPoints', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'ndarray': self.ndarray,
            'dataPoints': self.data_points,
        }

        return untrimmed

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self.to_array()
        is_ndarray = all([isinstance(x, list) for x in untrimmed])
        if not is_ndarray:
            as_str = '['
            as_str += ','.join([x.to_js_literal() for x in untrimmed])
            as_str += ']'
        else:
            serialized = serialize_to_js_literal(untrimmed)
            as_str = serialized

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

