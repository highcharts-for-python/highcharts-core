from typing import Optional, List
from collections import UserDict

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from validator_collection import checkers, validators, errors as validator_errors

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
        self._array = None
        self._ndarray = None
        self._data_points = None
        
        self.array = kwargs.get('array', None)
        self.ndarray = kwargs.get('ndarray', None)
        self.data_points = kwargs.get('data_points', None)

    def __getattr__(self, name):
        """Facilitates the retrieval of a 1D array of values from the collection.
        
        The basic logic is as follows:
        
        1. This method is automatically called when an attribute is not found in the 
           instance.
        2. It checks to see whether the attribute is a valid property of the data point
           class.
        3. If it is, and NumPy is installed, it assembles the array and returns the
           dimension indicated by the attribute name. If NumPy is not installed, it
           returns a simple list with values as per the attribute name.
        4. If ``name`` is not a valid property of the data point class, then it
           calls the ``super().__getattribute__()`` method to handle the attribute.
           
        :param name: The name of the attribute to retrieve.
        :type name: :class:`str <python:str>`
        
        :returns: The value of the attribute.
        
        :raises AttributeError: If ``name`` is not a valid attribute of the data point
          class or the instance.
        """
        data_point_properties = self._get_props_from_array()
        data_point_class = self._get_data_point_class()

        if name in ['_array',
                    'array',
                    '_ndarray',
                    'ndarray',
                    '_data_points',
                    'data_points']:
            return super().__getattr__(name)

        if name in data_point_properties and (
            self.ndarray is not None or self.array is not None
        ):
            if HAS_NUMPY and self.ndarray is not None and name in self.ndarray:
                return self.ndarray[name]

            position = data_point_properties.index(name)
            
            try:
                return [x[position] for x in self.array]
            except (TypeError, IndexError):
                raise AttributeError(name)

        data_points = self._assemble_data_points()
        as_list = [getattr(x, name, None) for x in data_points]
        
        if HAS_NUMPY:
            return np.asarray(as_list)
        
        return as_list

    def __setattr__(self, name, value):
        """Updates the collected data values if ``name`` is a valid property of the 
        data point.
        
        The basic logic is as follows:
        
          1. Check if ``name`` is a valid property of the data point class.
          2. If it is not, then call the ``super().__setattr__()`` method to handle
             the attribute. End the method.
          3. If it is, then check whether the call requires merging into existing
             data (as opposed to wholesale overwrite).
          4. If merging is required, check whether ``value`` is of the same length
             as other existing data. If it is shorter, then pad it with empty values.
             If it is longer, then raise an error.
          5. If NumPy is supported, then convert ``value`` to a NumPy array. Otherwise,
             leave it as is.
          6. If NumPy is supported and an array is present, replace the corresponding 
             slice with the new value.Otherwise, reconstitute the resulting array with 
             new values.
          7. If no array is supported, then set the corresponding property on the data
             points.

        """
        if name.startswith('_'):
            super().__setattr__(name, value)
            return
        elif name in ['array', 'ndarray', 'data_points']:
            super().__setattr__(name, value)
            return

        data_point_properties = self._get_props_from_array()

        try:
            has_ndarray = self.ndarray is not None
            has_array = self.array is not None
            has_data_points = self.data_points is not None
        except AttributeError:
            has_ndarray = False
            has_array = False
            has_data_points = False

        if name in data_point_properties and has_ndarray and name != 'name':
            index = data_point_properties.index(name)
            is_arraylike = utility_functions.is_arraylike(value)
            
            array_dict = self.ndarray.copy()

            # if value is not an array
            if not is_arraylike:
                value = np.full((self.ndarray_length, 1), value)

            extend_ndarray = len(value) > self.ndarray_length
            extend_value = len(value) < self.ndarray_length
            
            # if value has more members (values) than the existing ndarray
            if extend_ndarray:
                for key in self.ndarray:
                    if key == name:
                        continue
                    array_dict[key] = utility_functions.lengthen_array(array_dict[key],
                                                                       members = len(value))
                array_dict[name] = value
            # if value has fewer members (values) than the existing ndarray
            elif extend_value:
                value = utility_functions.lengthen_array(value,
                                                         members = self.ndarray_length)
            array_dict[name] = value

            self._ndarray = array_dict
        elif name in data_point_properties and has_array and name != 'name':
            index = data_point_properties.index(name)
            is_arraylike = utility_functions.is_arraylike(value)
            
            # if value is not an array
            if not is_arraylike:
                value = [value for x in range(len(self.array))]

            if len(value) > len(self.array):
                self.array.extend([[] for x in range(len(value) - len(self.array))])
            elif len(value) < len(self.array):
                value.extend([None for x in range(len(self.array) - len(value))])

            array = []
            for row_index, inner_array in enumerate(self.array):
                revised_array = [x for x in inner_array]
                revised_array = utility_functions.extend_columns(revised_array,
                                                                 index + 1)
                row_value = value[row_index]
                if utility_functions.is_iterable(row_value):
                    revised_array[index] = row_value[index]
                else:
                    revised_array[index] = row_value
                
                array.append(revised_array)
            
            self.array = array
        elif name in data_point_properties and has_data_points:
            is_arraylike = utility_functions.is_arraylike(value)
            if not is_arraylike:
                value = np.full((len(self.data_points), 1), value)
            
            if len(self.data_points) < len(value):
                missing = len(value) - len(self.data_points)
                for i in range(missing):
                    data_point_cls = self._get_data_point_class()
                    empty_data_point = data_point_cls()
                    self.data_points.append(empty_data_point)
                    
            if len(value) < len(self.data_points):
                value = utility_functions.lengthen_array(value,
                                                         members = len(self.data_points))

            for i in range(len(self.data_points)):
                if hasattr(value[i], 'item'):
                    checked_value = value[i].item()
                else:
                    checked_value = value[i]
                try:
                    setattr(self.data_points[i], name, checked_value)
                except validator_errors.CannotCoerceError as error:
                    if isinstance(checked_value, str) and ',' in checked_value:
                        checked_value = checked_value.replace(',', '')
                        setattr(self.data_points[i], name, checked_value)
                    elif checkers.is_numeric(checked_value):
                        checked_value = str(checked_value)
                        setattr(self.data_points[i], name, checked_value)
                    else:
                        raise error

        elif name in data_point_properties and name == 'name':
            index = data_point_properties.index(name)
            
            is_iterable = not isinstance(value,
                                         (str, bytes, dict, UserDict)) and hasattr(value, 
                                                                                   '__iter__')
            if is_iterable:
                as_list = []
                for i in range(len(value)):
                    if HAS_NUMPY:
                        if name != 'name' and data_point_properties[-1] == 'name':
                            inner_list = [np.nan for x in data_point_properties[:-1]]
                        else:
                            inner_list = [np.nan for x in data_point_properties]
                    else:
                        if name != 'name' and data_point_properties[-1] == 'name':
                            inner_list = [None for x in data_point_properties[:-1]]
                        else:
                            inner_list = [None for x in data_point_properties]
                    if index < len(inner_list):
                        inner_list[index] = value[i]
                    as_list.append(inner_list)
            else:
                if name != 'name' and data_point_properties[-1] == 'name':
                    as_list = [None for x in data_point_properties[:-1]]
                else:
                    as_list = [None for x in data_point_properties]
                as_list[index] = value

            if HAS_NUMPY:
                self.ndarray = as_list
            else:
                self.array = as_list
        elif utility_functions.is_arraylike(value):
            if not has_data_points:
                data_point_cls = self._get_data_point_class()
                data_points = [data_point_cls() for x in value]
                for index in range(len(data_points)):
                    try:
                        setattr(data_points[index], name, value[index])
                    except validator_errors.CannotCoerceError:
                        if isinstance(value[index], str) and ',' in value[index]:
                            coerced_value = value[index].replace(',', '')
                            setattr(data_points[index], name, coerced_value)
                        elif checkers.is_numeric(value[index]) or (
                            HAS_NUMPY and isinstance(value[index], np.number)
                        ):
                            coerced_value = str(value[index])
                            setattr(data_points[index], name, coerced_value)
                        else:
                            raise errors.HighchartsValueError(
                                f'Unable to set {name} to {value[index]}. '
                                f'If using a helper method, this is likely '
                                f'due to mismatched columns. Please review '
                                f'your input data.')
                super().__setattr__('data_points', [x for x in data_points])
            elif len(value) <= len(self.data_points):
                for index in range(len(value)):
                    setattr(self.data_points[index], name, value[index])
            else:
                cut_off = len(self.data_points)
                data_point_cls = self._get_data_point_class()
                for index in range(cut_off):
                    setattr(self.data_points[index], name, value[index])
                for index in range(len(value[cut_off:])):
                    data_point = data_point_cls()
                    setattr(data_point, name, value[index])
                    self.data_points.append(data_point)
        elif name == 'name':
            if not has_data_points:
                data_point_cls = self._get_data_point_class()
                if has_ndarray:
                    length = self.ndarray_length
                elif has_array:
                    length = len(self.array)
                else:
                    length = 1
                    
                data_points = [data_point_cls() for x in range(length)]

                for index in range(len(data_points)):
                    setattr(data_points[index], name, value)

                super().__setattr__('data_points', [x for x in data_points])
            else:
                for index in range(len(value)):
                    setattr(self.data_points[index], name, value[index])
        else:
            super().__setattr__(name, value)

    def __len__(self):
        """Returns the number of data points in the collection.
        
        :rtype: :class:`int <python:int>`
        """
        if self.ndarray is not None:
            result = self.ndarray_length
        elif self.array:
            result = len(self.array)
        elif self.data_points:
            result = len(self.data_points)
        else:
            result = 0
            
        return result

    def __iter__(self):
        self._current_index = 0
        return iter(self.to_array(force_object = True))
    
    def __next__(self):
        if self._current_index < len(self):
            x = self.to_array(force_object = True)[self._current_index]
            self._current_index += 1
            return x
        raise StopIteration

    def __bool__(self):
        return len(self) > 0

    @property
    def array(self) -> Optional[List]:
        """Primitive collection of values for data points in the collection. Used if
        `NumPy <https://www.numpy.org>`__ is not available. Defaults to 
        :obj:`None <python:None>`.
        
        .. note::
        
          If `NumPy <https://www.numpy.org>`__ is availalbe, will instead behave as
          an alias for
          :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollection.ndarray>`
        
        :rtype: :class:`list <python:list>` or :obj:`None <python:None>`
        """
        return self._array
    
    @array.setter
    def array(self, value):
        if not value:
            self._array = None
        elif utility_functions.is_iterable(value):
            self._array = [x for x in value]
        else:
            raise errors.HighchartsValueError(f'.array requires an iterable value. '
                                              f'Received: {value}')

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
            if not checkers.is_iterable(validated, forbid_literals = (str,
                                                                      bytes,
                                                                      dict,
                                                                      UserDict)):
                validated = [validated]

            super().__setattr__('_data_points', validated)

    @property
    def ndarray(self):
        """A :class:`dict <python:dict>` whose keys correspond to data point properties, 
        and whose values are :class:`numpy.ndarray <numpy:numpy.ndarray>` instances that 
        contain the data point collection's values.
        
        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._ndarray

    @ndarray.setter
    def ndarray(self, value):
        def raise_unsupported_dimension_error(length):
            supported_dimensions = self._get_supported_dimensions()
            
            supported_as_str = ', '.join([str(x) for x in supported_dimensions[:-1]])
            supported_as_str += f', or {str(supported_dimensions[-1])}'
            
            raise errors.HighchartsValueError(f'{self.__name__} supports arrays with '
                                                f'{supported_as_str} dimensions. Received'
                                                f' a value with: {length}')
            
        is_iterable = not isinstance(value, 
                                     (str, bytes, dict, UserDict)) and hasattr(value, 
                                                                               '__iter__')
        if value is None:
            self._ndarray = None
            as_array = False
        elif HAS_NUMPY and not isinstance(value, np.ndarray) and is_iterable:
            length = len(value[0])
            for item in value:
                if len(item) not in self._get_supported_dimensions():
                    raise_unsupported_dimension_error(len(item))
            props_from_array = self._get_props_from_array(length = length)
            as_dict = {}
            for index, prop in enumerate(props_from_array):
                prop_value = [x[index] for x in value]
                as_dict[prop] = utility_functions.to_ndarray(prop_value)

            as_array = utility_functions.to_ndarray(value)
        else:
            as_array = value

        if HAS_NUMPY and isinstance(as_array, np.ndarray):
            dimensions = as_array.ndim
            supported_dimensions = self._get_supported_dimensions()
            if dimensions not in supported_dimensions:
                dimensions = as_array.ndim + 1
                if dimensions not in supported_dimensions:
                    raise_unsupported_dimension_error(dimensions)
            props_from_array = self._get_props_from_array(length = dimensions)
            if props_from_array and props_from_array[-1] != 'name':
                props_from_array.append('name')
            as_dict = {}
            for index, prop in enumerate(props_from_array):
                try:
                    as_dict[prop] = as_array[:, index]
                except IndexError as error:
                    if index == len(props_from_array) - 1 and prop == 'name':
                        pass
                    else:
                        raise error
            self._ndarray = as_dict
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
        dimensions = cls._get_data_point_class()._get_supported_dimensions()
        last_dimension = dimensions[-1]
        data_point_properties = cls._get_props_from_array()
        if 'name' not in data_point_properties or len(data_point_properties) > last_dimension:
            dimensions.append(last_dimension + 1)
        
        return dimensions

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
        data_point_cls = cls._get_data_point_class()
        
        return data_point_cls._get_props_from_array(length)

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
        if HAS_NUMPY and isinstance(value, np.ndarray) and value.dtype != np.dtype('O'):
            return cls.from_ndarray(value)
        elif HAS_NUMPY and isinstance(value, np.ndarray):
            as_list = value.tolist()
        else:
            as_list = value

        data_points = cls._get_data_point_class().from_array(as_list)

        return cls(data_points = data_points)

    @classmethod
    def from_ndarray(cls, value):
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

    @property
    def ndarray_length(self) -> int:
        """The length of the array stored in 
        :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollection.ndarray>`.
        
        :rtype: :class:`int <python:int>`
        """
        if not self.ndarray:
            return 0

        return len(self.ndarray[list(self.ndarray.keys())[0]])

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
        if self.data_points is not None:
            data_points = [x for x in self.data_points]
        else:
            data_points = []

        if self.ndarray is None and not self.array:
            return data_points
        
        for index, data_point in enumerate(data_points):
            for prop in self._get_props_from_array():
                if getattr(data_point, prop) is not None:
                    setattr(data_points[index], prop, None)

        if HAS_NUMPY and self.ndarray is not None:
            if len(data_points) < self.ndarray_length:
                missing = self.ndarray_length - len(data_points)
                for i in range(missing):
                    data_points.append(self._get_data_point_class()())

            for index in range(self.ndarray_length):
                inner_list = [self.ndarray[key][index] for key in self.ndarray]
                data_points[index].populate_from_array(inner_list)
        else:
            if len(data_points) < len(self.array):
                missing = len(self.array) - len(data_points)
                for i in range(missing):
                    data_points.append(self._get_data_point_class()())
                    
            for index in range(len(self.array)):
                array = self.array[index]
                data_points[index].populate_from_array(array)

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
        
        props = self._get_props_from_array()
        if props and props[-1] == 'name':
            props = props[:-1]

        as_list = [[getattr(data_point, x, constants.EnforcedNull)
                    for x in props]
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

        if self.ndarray is None and not self.array and not self.data_points:
            return []
        
        if force_object and self.data_points and not self.array:
            return [x for x in self.data_points]
        elif force_object and self.ndarray is not None:
            return [x for x in self._assemble_data_points()]
        elif force_object and self.array is not None:
            return [x for x in self._assemble_data_points()]

        if force_ndarray and not HAS_NUMPY:
            raise errors.HighchartsDependencyError('Cannot force ndarray if NumPy is '
                                                   'not available in the runtime '
                                                   'environment. Please install using '
                                                   '"pip install numpy" or similar.')
        elif force_ndarray and self.ndarray is not None:
            return utility_functions.from_ndarray(self.ndarray)
        elif force_ndarray and self.data_points:
            as_ndarray = self._assemble_ndarray()
            return utility_functions.from_ndarray(as_ndarray)

        if self.ndarray is not None and not self.requires_js_object:
            as_list = []
            columns = []
            for key in self.ndarray:
                value = self.ndarray[key]
                if utility_functions.is_ndarray(value):
                    columns.append(utility_functions.from_ndarray(value))
                else:
                    columns.append(value)
            as_list = [list(x) for x in zip(*columns)]
            
            return as_list
        elif self.array is not None and not self.requires_js_object:
            return [x for x in self.array]
        
        if not self.array and self.data_points:
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
            'array': as_dict.get('array', None),
            'ndarray': as_dict.get('ndarray', None),
            'data_points': as_dict.get('dataPoints', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'array': self.array,
            'ndarray': self.ndarray,
            'dataPoints': self.data_points,
        }

        return untrimmed

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8',
                      careful_validation = False) -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :param careful_validation: if ``True``, will carefully validate JavaScript values
        along the way using the
        `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
        to ``False``.
        
        .. warning::
        
            Setting this value to ``True`` will significantly degrade serialization
            performance, though it may prove useful for debugging purposes.

        :type careful_validation: :class:`bool <python:bool>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self.to_array()
        is_ndarray = all([isinstance(x, list) for x in untrimmed])
        if not is_ndarray:
            as_str = '['
            as_str += ','.join([x.to_js_literal(encoding = encoding,
                                                careful_validation = careful_validation)
                                for x in untrimmed])
            as_str += ']'
        else:
            serialized = serialize_to_js_literal(untrimmed,
                                                 encoding = encoding,
                                                 careful_validation = careful_validation)
            as_str = serialized

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str
