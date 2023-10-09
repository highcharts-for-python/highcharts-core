from typing import Optional, List
from decimal import Decimal
from collections import UserDict

try:
    import orjson as json
except ImportError:
    try:
        import rapidjson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            import json
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from validator_collection import validators, checkers

from highcharts_core import errors, utility_functions, constants
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.options.series.data.base import DataBase
from highcharts_core.options.series.data.collections import DataPointCollection


class SeriesBase(SeriesOptions):
    """Generic base class for specific series configurations."""

    def __init__(self, **kwargs):
        self._data = None
        self._id = None
        self._index = None
        self._legend_index = None
        self._name = None
        self._stack = None
        self._x_axis = None
        self._y_axis = None
        self._z_index = None

        self.data = kwargs.get('data', None)
        self.id = kwargs.get('id', None)
        self.index = kwargs.get('index', None)
        self.legend_index = kwargs.get('legend_index', None)
        self.name = kwargs.get('name', None)
        self.stack = kwargs.get('stack', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)
        self.z_index = kwargs.get('z_index', None)

        super().__init__(**kwargs)

    def __str__(self):
        """Return a human-readable :class:`str <python:str>` representation of the series.

        .. warning::
        
          To ensure that the result is human-readable, the string representation
          will be generated *without* its 
          :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` 
          property.
        
          .. tip::
        
            If you would like a *complete* and *unambiguous* :class:`str <python:str>` 
            representation, then you can:
            
            * use the :meth:`__repr__() <highcharts_core.options.series.base.SeriesBase.__repr__>` method,
            * call ``repr(my_series)``, or
            * serialize the series to JSON using ``my_series.to_json()``.
            
        :returns: A :class:`str <python:str>` representation of the chart.
        :rtype: :class:`str <python:str>`
        """
        as_dict = self.to_dict()

        kwargs = {utility_functions.to_snake_case(key): as_dict[key]
                  for key in as_dict if key != 'data'}
        kwargs_as_str = ', '.join([f'{key} = {repr(kwargs[key])}'
                                   for key in kwargs])

        return f'{self.__class__.__name__}({kwargs_as_str})'

    def __getattr__(self, name):
        """Facilitates the retrieval of properties from the series and its underlying data.
        
        The logic is:
        
          1. If the attribute exists on the series object, then return it.
          2. If ``.data`` is empty, then return :obj:`None <python:None>`.
          3. If ``.data`` contains a 
             :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`,
             then return the attribute from the collection.
          4. Since ``.data`` contains a list of data points, return an iterable
             containing the attribute from each data point. If NumPy is available,
             return this iterable as a NumPy :class:`ndarray <numpy:numpy.ndarray>`.

        :param name: The name of the attribute to retrieve.
        :type name: :class:`str <python:str>`
        
        :returns: The value of the attribute.
        
        :raises AttributeError: If ``name`` is not a valid attribute of the data point
          class or the instance.
        """
        try:
            return super().__getattribute__(name)
        except AttributeError as error:
            if name in ['__iter__', '__next__', 'requires_js_object']:
                raise error
            pass

        if not self.data:
            raise AttributeError(name)

        if isinstance(self.data, DataPointCollection):
            return getattr(self.data, name)

        results = [getattr(x, name) for x in self.data]

        if HAS_NUMPY:
            results = np.asarray(results)

        return results
    
    def __setattr__(self, name, value):
        """Updates the series attribute, or descendent attributes on the ``.data`` 
        properties.
        """
        try:
            super().__setattr__(name, value)
            return
        except AttributeError:
            pass
        
        collection_cls = self._data_collection_class()
        data_point_cls = self._data_point_class()
        
        if not utility_functions.is_ndarray(self.data) and not self.data:
            if HAS_NUMPY:
                collection = collection_cls()
                setattr(collection, name, value)
                self.data = collection
            elif checkers.is_iterable(value, forbid_literals = (str, 
                                                                bytes, 
                                                                dict, 
                                                                UserDict)):
                collection = collection_cls()
                setattr(collection, name, value)
                self.data = collection
            else:
                data_point = data_point_cls(name = value)
                self._data = [data_point]
        elif not self.data:
            collection = collection_cls()
            setattr(collection, name, value)
            self.data = collection
        elif checkers.is_type(self.data, 'DataPointCollection'):
            setattr(self.data, name, value)
        else:
            if not checkers.is_iterable(value, forbid_literals = (str,
                                                                  bytes,
                                                                  dict,
                                                                  UserDict)):
                value = [value for x in self.data]
            
            if len(self.data) > len(value):
                value = value + [None for x in range(len(self.data) - len(value))]
            elif len(self.data) < len(value):
                self.data = self.data + [data_point_cls() 
                                         for x in range(len(value) - len(self.data))]
            
            for index in range(len(self.data)):
                setattr(self.data[index], name, value[index])

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return DataPointCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return DataBase

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return f'series.{self.type}'

    @property
    def data(self) -> Optional[List[DataBase] | DataPointCollection]:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`DataBase` or 
          :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>` 
          or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not utility_functions.is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = self._data_point_class().from_array(value)
              
    @property
    def id(self) -> Optional[str]:
        """An id for the series. Defaults to :obj:`None <python:None>`.

        .. hint::

          This can be used (in JavaScript) after render time to get a pointer to the
          series object through ``chart.get()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def index(self) -> Optional[int]:
        """The index for the series in the chart, affecting the internal index in the
        (JavaScript) ``chart.series`` array, the visible Z-index, and the order of the
        series in the legend. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._index

    @index.setter
    def index(self, value):
        self._index = validators.integer(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def legend_index(self) -> Optional[int]:
        """The sequential index for the series in the legend. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._legend_index

    @legend_index.setter
    def legend_index(self, value):
        self._legend_index = validators.integer(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def name(self) -> Optional[str]:
        """The name of the series as shown in the legend, tooltip, etc. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def stack(self) -> Optional[str]:
        """Indicates the "stack" into which the series should be grouped, if the chart
        groups series into stacks. Defaults to :obj:`None <python:None>`.

        .. note::

          The value can be a string or a numeric value, provided that series in the same
          stack all have the same value when converted to a string. For ease of ues,
          Highcharts for Python will attempt to force the conversion of the relevant value
          to a string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stack

    @stack.setter
    def stack(self, value):
        if not value:
            self._stack = None
        else:
            self._stack = validators.string(value,
                                            coerce_value = True)

    @property
    def x_axis(self) -> Optional[str | int]:
        """When using multiple X-axes, this setting determines on which axis the series
        should be drawn. Its value should be either a numerical index position in the
        :meth:`Options.x_axis` array (starting at 0), or a :class:`str <python:str>`
        indicating the :meth:`id <XAxis.id>` of the axis to which the series should be
        connected. Defaults to :obj:`None <python:None>`, which behaves as if the value
        were set to ``0``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if value is None:
            self._x_axis = None
        else:
            try:
                value = validators.integer(value, minimum = 0)
            except (ValueError, TypeError):
                value = validators.string(value)

            self._x_axis = value

    @property
    def y_axis(self) -> Optional[str | int]:
        """When using multiple Y-axes, this setting determines on which axis the series
        should be drawn. Its value should be either a numerical index position in the
        :meth:`Options.y_axis` array (starting at 0), or a :class:`str <python:str>`
        indicating the :meth:`id <YAxis.id>` of the axis to which the series should be
        connected. Defaults to :obj:`None <python:None>`, which behaves as if the value
        were set to ``0``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if value is None:
            self._y_axis = None
        else:
            try:
                value = validators.integer(value, minimum = 0)
            except (ValueError, TypeError):
                value = validators.string(value)

            self._y_axis = value

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The visual z-index of the series. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        if value is None:
            self._z_index = None
        else:
            self._z_index = validators.numeric(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'data': self.data,
            'id': self.id,
            'index': self.index,
            'legendIndex': self.legend_index,
            'name': self.name,
            'stack': self.stack,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
            'zIndex': self.z_index,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

    def load_from_array(self, value):
        """Update the :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>`
        property with data loaded from an iterable in ``value``.

        :param value: The value that should contain the data which will be converted into data
          point instances.

          .. note::

            If ``value`` is not an iterable, it will be converted into an iterable to be
            further de-serialized correctly.

        :type value: iterable

        """
        data_point_cls = self._data_point_class()

        self.data = data_point_cls.from_array(value)

    @classmethod
    def from_array(cls, value, series_kwargs = None):
        """Create one instance of the series with ``data`` populated from ``value``.

        :param value: The value that should contain the data which will be converted into data
          point instances.

          .. note::

            If ``value`` is not an iterable, it will be converted into an iterable to be
            further de-serialized correctly.

        :type value: iterable
        
        :param series_kwargs: Optional keyword arguments to apply when instanting the 
          series. Defaults to :obj:`None <python:None>`.
        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`
        
        :returns: An instance of the series type with ``data`` populated from the value.
        :rtype: :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          descendent
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        data_point_cls = cls._data_point_class()
        data_points = data_point_cls.from_array(value)

        series_kwargs['data'] = data_points
        series = cls(**series_kwargs)

        return series

    def load_from_csv(self,
                      as_string_or_file,
                      property_column_map = None,
                      has_header_row = True,
                      delimiter = ',',
                      null_text = 'None',
                      wrapper_character = "'",
                      line_terminator = '\r\n',
                      wrap_all_strings = False,
                      double_wrapper_character_when_nested = False,
                      escape_character = "\\",
                      series_in_rows = False,
                      series_index = True,
                      **kwargs):
        """Replace the existing
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        with a new value populated from data in a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_series = LineSeries()
                
                # EXAMPLE 1. Minimal code - will attempt to update the line series
                # taking x-values from the first column, and y-values from
                # the second column. If there are too many columns in the CSV,
                # will throw an error.
                
                my_series = my_series.from_csv('some-csv-file.csv')
                
                # EXAMPLE 2. More precise code - will attempt to update the line series
                # mapping columns in the CSV file to properties on the series
                # instance.
                
                my_series = my_series.from_csv('some-csv-file.csv',
                                               property_column_map = {
                                                   'x': 0,
                                                   'y': 3,
                                                   'id': 'id'
                                               })
                
                # EXAMPLE 3. More precise code - will update the line series
                # using a specific series generated from the CSV file.
                
                my_series = my_series.from_csv('some-csv-file.csv', series_index = 2)

            As the example above shows, data is loaded into the ``my_series`` instance
            from the CSV file with a filename ``some-csv-file.csv``. As shown in
            EXAMPLE 1, unless otherwise specified, the :meth:`.x <CartesianData.x>` 
            values for each data point will be taken from the first (index 0) column
            in the CSV file, while the :meth:`.y <CartesianData.y>` values will be 
            taken from the second column.
            
            If the CSV has more than 2 columns, then this will throw an
            :exc:`HighchartsCSVDeserializationError` because the function is not certain
            which columns to use to update the series. If this happens, you can either:
            
              #. As shown in EXAMPLE 2, precisely specify which columns to use by 
                 providing a ``property_column_map`` argument. In EXAMPLE 2, the
                 :meth:`.x <CartesianData.x>` values for each data point will be taken
                 from the first (index 0) column in the CSV file. The 
                 :meth:`.y <CartesianData.y>` values will be taken from the fourth 
                 (index 3) column in the CSV file. And the 
                 :meth:`.id <CartesianData.id>` values will be taken from a column whose
                 header row is labeled ``'id'`` (regardless of its index).
              #. Supply a ``series_index`` argument, which indicates which of the series
                 generated from the CSV file should be used to update the instance.

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param property_column_map: An optional :class:`dict <python:dict>` used to 
          indicate which data point property should be set to which CSV column. The keys
          in the :class:`dict <python:dict>` should correspond to properties in the data 
          point class, while the value can either be a numerical index (starting with 0) 
          or a :class:`str <python:str>` indicating the label for the CSV column. 
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
            file *must* have a header row (this is expected, by default). If there is no
            header row and a :class:`str <python:str>` value is found, a
            :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.
        :type line_terminator: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce any
            value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\`` (which is Python for ``'\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to 
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`
        
        :param series_index: if :obj:`None <python:None>`, will raise a 
          :exc:`HighchartsCSVDeserializationError <highcharts_core.errors.HighchartsCSVDeserializationError>`
          if the CSV data contains more than one series and no ``property_column_map`` 
          is provided. Otherwise, will update the instance with the series found 
          in the CSV at the ``series_index`` value. Defaults to 
          :obj:`None <python:None>`.
        :type series_index: :class:`int <python:int>` or :obj:`None <python:None>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        cls = self.__class__
        new_instance = cls.from_csv(
            as_string_or_file,
            property_column_map = property_column_map,
            has_header_row = has_header_row,
            delimiter = delimiter,
            null_text = null_text,
            wrapper_character = wrapper_character,
            line_terminator = line_terminator,
            wrap_all_strings = wrap_all_strings,
            double_wrapper_character_when_nested = double_wrapper_character_when_nested,
            escape_character = escape_character,
            series_in_rows = series_in_rows,
            series_index = series_index,
            **kwargs
        )

        if series_index is None and isinstance(new_instance, list):
            raise errors.HighchartsCSVDeserializationError(
                f'Expected data for a single series, but got {len(new_instance)} when '
                f'loading from CSV. Please either modify the structure of your CSV '
                f'or provide more targeted instructions using the property_column_map '
                f'argument.'
            )
        elif isinstance(new_instance, list):
            new_instance = new_instance[series_index]

        self.data = new_instance.data

    @classmethod
    def _from_csv_multi_map(cls,
                            as_string_or_file,
                            property_column_map = None,
                            has_header_row = True,
                            series_kwargs = None,
                            delimiter = ',',
                            null_text = 'None',
                            wrapper_character = "'",
                            line_terminator = '\r\n',
                            wrap_all_strings = False,
                            double_wrapper_character_when_nested = False,
                            escape_character = "\\",
                            series_in_rows = False,
                            **kwargs):
        """Replace the existing
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        with a new value populated from data in a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_series = LineSeries()
                my_series = my_series.from_csv('some-csv-file.csv',
                                               property_column_map = {
                                                   'x': 0,
                                                   'y': 3,
                                                   'id': 'id'
                                               })

            As the example above shows, data is loaded into the ``my_series`` instance
            from the CSV file with a filename ``some-csv-file.csv``. The
            :meth:`x <CartesianData.x>`
            values for each data point will be taken from the first (index 0) column in
            the CSV file. The :meth:`y <CartesianData.y>` values will be taken from the
            fourth (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>`
            values will be taken from a column whose header row is labeled ``'id'``
            (regardless of its index).

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param property_column_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which CSV column. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value can either be a numerical index (starting with 0) or a
          :class:`str <python:str>` indicating the label for the CSV column. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
            file *must* have a header row (this is expected, by default). If there is no
            header row and a :class:`str <python:str>` value is found, a
            :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from the CSV file instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.
        :type line_terminator: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce any
            value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\`` (which is Python for ``'\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to 
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        try:
            as_string_or_file = as_string_or_file.strip()
        except AttributeError:
            pass

        property_column_map = validators.dict(property_column_map,
                                              allow_empty = True) or {}
        cleaned_column_map = {}
        for key in property_column_map:
            map_value = property_column_map.get(key, None)
            if map_value is None:
                continue
            if not isinstance(map_value, int) and not has_header_row:
                raise errors.HighchartsCSVDeserializationError(f'The supplied CSV '
                                                               f'data does not have a'
                                                               f'header row, but the '
                                                               f'property_column_map '
                                                               f'did not supply an '
                                                               f'index. Received: '
                                                               f'column name '
                                                               f'"{map_value}" '
                                                               f'instead.')
            cleaned_column_map[key] = map_value

        if not checkers.is_on_filesystem(as_string_or_file):
            as_str = as_string_or_file
            columns, csv_records = utility_functions.parse_csv(
                as_str,
                has_header_row = has_header_row,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = False,
                double_wrapper_character_when_nested = False,
                escape_character = "\\"
            )
        else:
            with open(as_string_or_file, 'r', newline = '') as file_:
                columns, csv_records = utility_functions.parse_csv(
                    file_,
                    has_header_row = has_header_row,
                    delimiter = delimiter,
                    null_text = null_text,
                    wrapper_character = wrapper_character,
                    line_terminator = line_terminator,
                    wrap_all_strings = False,
                    double_wrapper_character_when_nested = False,
                    escape_character = "\\"
                )

        fixed_values = {}
        iterable_values = {}
        number_of_series = 1
        mismatched_series = {}
        names = []
        for key in cleaned_column_map:
            map_value = cleaned_column_map[key]

            is_iterable = not isinstance(map_value, (str, bytes, dict, UserDict)) and \
                hasattr(map_value, '__iter__')

            if is_iterable:
                for item in map_value:
                    if item not in columns:
                        raise errors.HighchartsCSVDeserializationError(
                            f'property_column_map is looking for a column labeled '
                            f'"{item}", but no corresponding column was found.'
                        )

                implied_series = len(map_value)
                if number_of_series == 1 and implied_series > number_of_series:
                    number_of_series = implied_series
                elif implied_series != number_of_series:
                    mismatched_series[key] = implied_series
                
                iterable_values[key] = map_value
                if key == 'y':
                    name_list = [x if isinstance(x, str) else columns[x]
                                 for x in map_value]
                    names.extend(name_list)
            else:
                if isinstance(map_value, str) and map_value not in columns:
                    raise errors.HighchartsCSVDeserializationError(
                        f'property_column_map is looking for a column labeled '
                        f'"{map_value}", but no corresponding column was found.'
                    )
                elif map_value not in columns and checkers.is_integer(
                    map_value,
                    coerce_value = True
                ) and int(map_value) > len(columns):
                    raise errors.HighchartsCSVDeserializationError(
                        f'property_column_map is looking for a column at index '
                        f'{map_value}, but no corresponding column was found.'
                    )

                fixed_values[key] = map_value
                if key == 'y':
                    if isinstance(map_value, str):
                        names.append(map_value)
                    else:
                        names.append(columns[map_value])

        if mismatched_series:
            raise errors.HighchartsCSVDeserializationError(
                f'Unable to create series from CSV. The property map implied '
                f'multiple series were needed, but properties had mismatched '
                f'number of values:\n{mismatched_series}'
            )
        
        collections = []
        for index in range(number_of_series):
            collection_cls = cls._data_collection_class()
            collection_instance = collection_cls()
            for key in iterable_values:
                iterable_value = iterable_values[key][index]
                prop_array = [x.get(iterable_value, None) for x in csv_records]
                for i, value in enumerate(prop_array):
                    if value and isinstance(value, str) and ',' in value:
                        test_value = value.replace(',', '')
                        if checkers.is_numeric(test_value):
                            value = test_value
                    prop_array[i] = value

                setattr(collection_instance, key, prop_array)
            for key in fixed_values:
                fixed_value = fixed_values[key]
                prop_array = [x.get(fixed_value, None) for x in csv_records]
                for i, value in enumerate(prop_array):
                    if value and isinstance(value, str) and ',' in value:
                        test_value = value.replace(',', '')
                        if checkers.is_numeric(test_value):
                            value = test_value
                    prop_array[i] = value

                setattr(collection_instance, key, prop_array)
                getattr(collection_instance, key, None)

            collections.append(collection_instance)
        
        series_list = []
        for index in range(number_of_series):
            series_kwargs['data'] = collections[index]
            series_instance = cls(**series_kwargs)
            try:
                series_instance.name = names[index]
            except IndexError:
                pass
            for key in kwargs:
                if key not in series_kwargs and key not in cleaned_column_map:
                    setattr(series_instance, key, kwargs[key])

            series_list.append(series_instance)
        
        return series_list

    @classmethod
    def from_csv(cls,
                 as_string_or_file,
                 property_column_map = None,
                 has_header_row = True,
                 series_kwargs = None,
                 delimiter = ',',
                 null_text = 'None',
                 wrapper_character = "'",
                 line_terminator = '\r\n',
                 wrap_all_strings = False,
                 double_wrapper_character_when_nested = False,
                 escape_character = "\\",
                 series_in_rows = False,
                 series_index = None,
                 **kwargs):
        """Create one or more new :term:`series` instances with
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>`
        populated from data in a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                # Create one or more LineSeries instances from the CSV file "some-csv-file.csv".

                # EXAMPLE 1. The minimum code to produce one series for each
                # column in the CSV file (excluding the first column):

                my_series = LineSeries.from_csv('some-csv-file.csv')

                # EXAMPLE 2. Produces ONE series with more precise configuration:

                my_series = LineSeries.from_csv('some-csv-file.csv',
                                                property_column_map = {
                                                    'x': 0,
                                                    'y': 3,
                                                    'id': 'id'
                                                })

                # EXAMPLE 3. Produces THREE series instances with 
                # more precise configuration:

                my_series = LineSeries.from_csv('some-csv-file.csv',
                                                property_column_map = {
                                                    'x': 0,
                                                    'y': [3, 5, 8],
                                                    'id': 'id'
                                                })

            As the example above shows, data is loaded into the ``my_series`` instance
            from the CSV file with a filename ``some-csv-file.csv``. The
            :meth:`x <CartesianData.x>`
            values for each data point will be taken from the first (index 0) column in
            the CSV file. The :meth:`y <CartesianData.y>` values will be taken from the
            fourth (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>`
            values will be taken from a column whose header row is labeled ``'id'``
            (regardless of its index).

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param property_column_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which CSV column. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value can either be a numerical index (starting with 0) or a
          :class:`str <python:str>` indicating the label for the CSV column. Defaults to
          :obj:`None <python:None>`.

            .. note::
          
              If any of the values in ``property_column_map`` contain an iterable, then
              one series will be produced for each item in the iterable. For example,
              the following:
            
                .. code-block:: python
            
                  {
                      'x': 0,
                      'y': [3, 5, 8]
                  }
              
              will return *three* series, each of which will have its 
              :meth:`.x <CartesianData.x>` value populated from the first column 
              (index 0), and whose :meth:`.y <CartesianData.y>`
              values will be populated from the fourth, sixth, and ninth columns (indices 
              3, 5, and 8), respectively.

            .. warning::

              If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
              file *must* have a header row (this is expected, by default). If there is no
              header row and a :class:`str <python:str>` value is found, a
              :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from the CSV file instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.
        :type line_terminator: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce any
            value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\\\`` (which is Python for ``'\\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to ``False``.
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: If supplied, return the series that Highcharts for Python
          generated from the CSV at the ``series_index`` position. Defaults to 
          :obj:`None <python:None>`, which returns all series generated from the CSV.
        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :term:`series` instance (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) OR 
          :class:`list <python:list>` of series instances with its
          :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
          populated from the data in ``df``.
        :rtype: :class:`list <python:list>` of series instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descendent

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        if series_in_rows:
            return cls.from_csv_in_rows(
                as_string_or_file,
                has_header_row = has_header_row,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = wrap_all_strings,
                double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                escape_character = escape_character,
                series_index = series_index,
                **kwargs
            )

        # SCENARIO 1: Has Property Map
        if property_column_map:
            series_list = cls._from_csv_multi_map(
                as_string_or_file,
                property_column_map = property_column_map,
                has_header_row = has_header_row,
                series_kwargs = series_kwargs,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = wrap_all_strings,
                double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                escape_character = escape_character,
                **kwargs
            )
            if len(series_list) == 1:
                return series_list[0]
            
            return series_list

        # SCENARIO 2: Properties in KWARGS
        collection_cls = cls._data_collection_class()
        data_point_cls = cls._data_point_class()
        props_from_array = data_point_cls._get_props_from_array()
        if not props_from_array:
            props_from_array = ['x', 'y']

        property_map = {}
        for prop in props_from_array:
            if prop in kwargs:
                property_map[prop] = kwargs[prop]
        
        if property_map:
            series_list = cls._from_csv_multi_map(
                as_string_or_file,
                property_column_map = property_map,
                has_header_row = has_header_row,
                series_kwargs = series_kwargs,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = wrap_all_strings,
                double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                escape_character = escape_character,
                **kwargs
            )
            for index in range(len(series_list)):
                for key in kwargs:
                    if key not in props_from_array and key not in series_kwargs:
                        setattr(series_list[index], key, kwargs[key])
            
            if len(series_list) == 1:
                return series_list[0]

            if series_index is not None:
                return series_list[index]

            return series_list

        # SCENARIO 3: No Explicit Properties
        if not checkers.is_on_filesystem(as_string_or_file):
            as_str = as_string_or_file
            columns, csv_records = utility_functions.parse_csv(
                as_str,
                has_header_row = has_header_row,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = False,
                double_wrapper_character_when_nested = False,
                escape_character = "\\"
            )
        else:
            with open(as_string_or_file, 'r', newline = '') as file_:
                columns, csv_records = utility_functions.parse_csv(
                    file_,
                    has_header_row = has_header_row,
                    delimiter = delimiter,
                    null_text = null_text,
                    wrapper_character = wrapper_character,
                    line_terminator = line_terminator,
                    wrap_all_strings = False,
                    double_wrapper_character_when_nested = False,
                    escape_character = "\\"
                )

        try:
            series_idx = kwargs.get('index', columns[0])
        except IndexError:
            series_idx = kwargs.get('index', 0)

        column_count = len(columns)
        if not columns:
            column_count = len(csv_records[0])

        supported_dimensions = collection_cls._get_supported_dimensions()

        # SCENARIO 3a: Single Series, Data Frame Columns align exactly to Data Point Properties
        if column_count in supported_dimensions:
            property_map = {}
            props_from_array = data_point_cls._get_props_from_array(length = column_count)
            if not props_from_array:
                props_from_array = ['x', 'y']
            
            property_map[props_from_array[0]] = [x.get(series_idx, None) 
                                                 for x in csv_records]

            for index, prop in enumerate(props_from_array[1:]):
                if series_idx is not None:
                    prop_array = [x.get(columns[index + 1], index + 1)
                                  for x in csv_records]
                else:
                    prop_array = [x.get(columns[index], index)
                                  for x in csv_records]
                for i, value in enumerate(prop_array):
                    if value and isinstance(value, str) and ',' in value:
                        test_value = value.replace(',', '')
                        if checkers.is_numeric(test_value):
                            value = test_value
                    prop_array[i] = value

                property_map[prop] = prop_array
            
            collection = collection_cls()
            for key in property_map:
                setattr(collection, key, property_map[key])

            series_kwargs['data'] = collection
            series_instance = cls(**series_kwargs)
            for key in kwargs:
                if key not in series_kwargs and key not in property_map:
                    setattr(series_instance, key, kwargs[key])

            return series_instance

        # SCENARIO 3b: Multiple Series, Data Frame Columns correspond to multiples of Data Point Properties
        reversed_dimensions = sorted(supported_dimensions, reverse = True)

        columns_per_series = None
        if reversed_dimensions:
            for dimension in reversed_dimensions:
                if series_idx is not None and dimension > 1 and column_count % (dimension - 1) == 0:
                    if dimension > 2 and props_from_array[-1] == 'name':
                        columns_per_series = dimension - 2
                    else:
                        columns_per_series = dimension - 1
                    break
                if dimension > 1 and column_count % dimension == 0:
                    columns_per_series = dimension
                    break
                elif dimension == 1:
                    columns_per_series = 1
        
        if not columns_per_series:
            raise errors.HighchartsCSVDeserializationError(
                f'Could not determine how to deserialize CSV with {column_count}'
                f' columns into a {collection_cls.__name__} instance. Please supply '
                f'more precise instructions using property_column_map or '
                f'by explicitly specificying data property kwargs.'
            )

        series_count = column_count // columns_per_series
        if columns_per_series == 1 and series_idx:
            series_count -= 1

        series_list = []
        for index in range(series_count):
            start = 1 + (len(series_list) * columns_per_series)

            property_map = {}
            if series_idx is not None:
                expected_length = columns_per_series + 1
            else:
                expected_length = columns_per_series
                
            props_from_array = data_point_cls._get_props_from_array(length = expected_length)
            if not props_from_array:
                props_from_array = ['x', 'y']

            property_map[props_from_array[0]] = [x.get(series_idx, None) 
                                                 for x in csv_records]
            
            has_implicit_series_name = 'name' not in kwargs and 'name' not in series_kwargs
            if has_implicit_series_name:
                try:
                    series_name = columns[start]
                except (IndexError, TypeError):
                    series_name = None
            else:
                series_name = series_kwargs.get('name', None) or kwargs.get('name', None)

            props_from_array = props_from_array[1:]
            for idx, prop in enumerate(props_from_array):
                index = start + idx

                prop_array = [x.get(columns[index], idx) for x in csv_records]

                property_map[prop] = prop_array

            collection = collection_cls()
            for key in property_map:
                try:
                    setattr(collection, key, property_map[key])
                except ValueError as error:
                    if key not in ['x', 'name'] and 'name' not in property_map:
                        setattr(collection, 'name', property_map[key])
                    else:
                        raise error

            series_kwargs['data'] = collection
            series_instance = cls(**series_kwargs)
            for key in kwargs:
                if key not in series_kwargs and key not in property_map:
                    setattr(series_instance, key, kwargs[key])

            if 'name' not in series_kwargs and 'name' not in kwargs:
                series_instance.name = series_name

            series_list.append(series_instance)

        if series_index is not None:
            return series_list[series_index]

        return series_list

    @classmethod
    def from_csv_in_rows(cls,
                         as_string_or_file,
                         has_header_row = True,
                         series_kwargs = None,
                         delimiter = ',',
                         null_text = 'None',
                         wrapper_character = "'",
                         line_terminator = '\r\n',
                         wrap_all_strings = False,
                         double_wrapper_character_when_nested = False,
                         escape_character = "\\",
                         **kwargs):
        """Create a new :term:`series` instance with a
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        populated from data in a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_series = LineSeries.from_csv_in_rows('some-csv-file.csv')

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from the CSV file instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.
        :type line_terminator: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce any
            value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\\\`` (which is Python for ``'\\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :term:`series` instance (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) OR 
          :class:`list <python:list>` of series instances with its
          :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
          populated from the data in ``df``.
        :rtype: :class:`list <python:list>` of series instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descendent

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        if not checkers.is_on_filesystem(as_string_or_file):
            as_str = as_string_or_file
            columns, csv_records = utility_functions.parse_csv(
                as_str,
                has_header_row = has_header_row,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = False,
                double_wrapper_character_when_nested = False,
                escape_character = "\\"
            )
        else:
            with open(as_string_or_file, 'r', newline = '') as file_:
                columns, csv_records = utility_functions.parse_csv(
                    file_,
                    has_header_row = has_header_row,
                    delimiter = delimiter,
                    null_text = null_text,
                    wrapper_character = wrapper_character,
                    line_terminator = line_terminator,
                    wrap_all_strings = False,
                    double_wrapper_character_when_nested = False,
                    escape_character = "\\"
                )

        collection_cls = cls._data_collection_class()
        supported_dimensions = collection_cls._get_supported_dimensions()
        if 2 not in supported_dimensions:
            raise errors.HighchartsPandasDeserializationError(
                f'Unable to create a collection of {cls.__name__} instances '
                f'from CSV using a 2-dimensional array because {cls.__name__} does '
                f'not support 2-dimensional arrays as inputs. Please use a '
                f'different series type, or transpose the CSV to a columnar structure '
                f'and supply a column_property_map for greater precision.'
            )
        data_properties = collection_cls._get_props_from_array()
        
        if columns:
            x_values = columns[1:]
        else:
            x_values = [x for x in range(len(csv_records[0].keys()) - 1)]

        name_key = list(csv_records[0].keys())[0]
        name_values = [row[name_key] for row in csv_records]
        
        series_count = len(csv_records)
        series_list = []
        
        for row in range(series_count):
            series_name = name_values[row]
            y_values = [x for x in list(csv_records[row].values())[1:]]
            for i, value in enumerate(y_values):
                if value and isinstance(value, str) and ',' in value:
                    test_value = value.replace(',', '')
                    if checkers.is_numeric(test_value):
                        value = test_value
                y_values[i] = value
                
            as_array = zip(x_values, y_values)
            collection = collection_cls.from_array(as_array)
            series_instance_kwargs = series_kwargs.copy()
            series_instance_kwargs['data'] = collection
            series_instance_kwargs['name'] = series_name
            series_instance = cls(**series_instance_kwargs)
            for key in kwargs:
                if key not in series_instance_kwargs and key not in data_properties:
                    setattr(series_instance, key, kwargs[key])

            series_list.append(series_instance)

        return series_list

    def load_from_pandas(self,
                         df,
                         property_map = None,
                         series_in_rows = False,
                         series_index = None):
        """Replace the contents of the
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        with data points populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:pandas.DataFrame>`.

        :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:pandas.DataFrame>` column. Defaults to 
          :obj:`None <python:None>`.

        :type property_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to 
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: If supplied, return the series that Highcharts for Python
          generated from ``df`` at the ``series_index`` value. Defaults to 
          :obj:`None <python:None>`, which returns all series generated from ``df``.

          .. warning::

            If :obj:`None <python:None>` and Highcharts for Python generates multiple
            series, then a :exc:`HighchartsPandasDeserializationError` will be raised.

        :type series_index: :class:`int <python:int>`, or :obj:`None <python:None>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsPandasDeserializationError: if ``series_index`` is 
          :obj:`None <python:None>`, and it is ambiguous which series generated from
          the dataframe should be used
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        cls = self.__class__
        new_instance = cls.from_pandas(df,
                                       property_map = property_map,
                                       series_in_rows = series_in_rows)
        if series_index is None and isinstance(new_instance, list):
            raise errors.HighchartsPandasDeserializationError(
                f'Expected data for a single series, but got {len(new_instance)} when '
                f'loading from df. Please either modify the structure of df '
                f'or provide more targeted instructions using the property_map '
                f'argument.'
            )
        elif isinstance(new_instance, list):
            new_instance = new_instance[series_index]

        self.data = new_instance.data

    @classmethod
    def _from_pandas_multi_map(cls,
                               df,
                               property_map,
                               series_kwargs = None,
                               **kwargs):
        """Create one or more :term:`series` instances whose
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` properties
        are populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:pandas.DataFrame>`, when ``property_map`` suggests there are
        multiple series.

        :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:pandas.DataFrame>` column. Defaults to :obj:`None <python:None>`
        :type property_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`
        
        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :term:`series` instance (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) OR 
          :class:`list <python:list>` of series instances with its
          :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
          populated from the data in ``df``.
        :rtype: :class:`list <python:list>` of series instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descendent

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        fixed_values = {}
        iterable_values = {}
        number_of_series = 1
        mismatched_series = {}
        names = []
        for key in property_map:
            map_value = property_map[key]

            is_iterable = not isinstance(map_value, (str, bytes, dict, UserDict)) and \
                hasattr(map_value, '__iter__')

            if is_iterable:
                for item in map_value:
                    if item not in df.columns.values:
                        raise errors.HighchartsPandasDeserializationError(
                            f'Unable to find a column labeled "{item}" in df.'
                        )

                implied_series = len(map_value)
                if number_of_series == 1 and implied_series > number_of_series:
                    number_of_series = implied_series
                elif implied_series != number_of_series:
                    mismatched_series[key] = implied_series
                
                iterable_values[key] = map_value
                if key == 'y':
                    names.extend(map_value)
            else:
                if map_value not in df.columns.values:
                    if map_value != df.index.name:
                        raise errors.HighchartsPandasDeserializationError(
                            f'Unable to find a column labeled "{map_value}" in df.'
                        )

                fixed_values[key] = map_value
                if key == 'y':
                    names.append(map_value)
        
        if mismatched_series:
            raise errors.HighchartsPandasDeserializationError(
                f'Unable to create series from df. The property map implied '
                f'multiple series were needed, but properties had mismatched '
                f'number of values:\n{mismatched_series}'
            )
        
        collections = []
        for index in range(number_of_series):
            collection_cls = cls._data_collection_class()
            collection_instance = collection_cls()
            for key in iterable_values:
                iterable_value = iterable_values[key][index]
                prop_array = df[iterable_value].values
                setattr(collection_instance, key, prop_array)
            for key in fixed_values:
                fixed_value = fixed_values[key]
                try:
                    prop_array = df[fixed_value].values
                except KeyError:
                    prop_array = df.index.values
                setattr(collection_instance, key, prop_array)
            collections.append(collection_instance)
        
        series_list = []
        for index in range(number_of_series):
            series_kwargs['data'] = collections[index]
            series_instance = cls(**series_kwargs)
            try:
                series_instance.name = names[index]
            except IndexError:
                pass
            for key in kwargs:
                if key not in series_kwargs and property_map:
                    setattr(series_instance, key, kwargs[key])

            series_list.append(series_instance)
        
        return series_list

    @classmethod
    def from_pandas_in_rows(cls,
                            df,
                            series_kwargs = None,
                            series_index = None,
                            **kwargs):
        """Create a collection of :term:`series` instances, one for each
        row in ``df``.

        :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
          should be loaded.
        :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`
        
        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be 
            *overwritten*. The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param series_index: If supplied, return the series that Highcharts for Python
          generated from ``df`` at the ``series_index`` value. Defaults to 
          :obj:`None <python:None>`, which returns all series generated from ``df``.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.
        
        :returns: Collection of :term:`series` instances corresponding, with one series 
          per row in ``df``, and where:

            * the series x-values are populated from the column labels in ``df``
            * the series name is set to the row label from ``df``
            * the series y-values are populated from the values within that row in ``df``

        :rtype: :class:`list <python:list>` of 
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descendent
          instances

        """
        try:
            from pandas import DataFrame
        except ImportError:
            raise errors.HighchartsDependencyError('pandas is not available in the '
                                                   'runtime environment. Please install '
                                                   'using "pip install pandas"')

        if not checkers.is_type(df, ('DataFrame')):
            raise errors.HighchartsValueError(f'df is expected to be a Pandas DataFrame.'
                                              f'Was: {df.__class__.__name__}')
        
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        collection_cls = cls._data_collection_class()
        supported_dimensions = collection_cls._get_supported_dimensions()
        if 2 not in supported_dimensions:
            raise errors.HighchartsPandasDeserializationError(
                f'Unable to create a collection of {cls.__name__} instances '
                f'from df using a 2-dimensional array because {cls.__name__} does '
                f'not support 2-dimensional arrays as inputs. Please use a '
                f'different series type, or transpose df to a columnar structure '
                f'and supply a property_map for greater precision.'
            )
        data_properties = collection_cls._get_props_from_array()
        
        x_values = df.columns.values
        name_values = df.index.values
        
        series_count = len(df)
        series_list = []
        
        for row in range(series_count):
            series_name = name_values[row]
            y_values = df.iloc[[row]].values
            y_values = y_values.reshape(x_values.shape)

            as_array = np.column_stack((x_values, y_values))
            collection = collection_cls.from_array(as_array)
            series_instance_kwargs = series_kwargs.copy()
            series_instance_kwargs['data'] = collection
            series_instance_kwargs['name'] = series_name
            series_instance = cls(**series_instance_kwargs)
            for key in kwargs:
                if key not in series_instance_kwargs and key not in data_properties:
                    setattr(series_instance, key, kwargs[key])

            series_list.append(series_instance)

        if series_index is not None:
            return series_list[series_index]

        return series_list

    @classmethod
    def from_pandas(cls,
                    df,
                    property_map = None,
                    series_kwargs = None,
                    series_in_rows = False,
                    series_index = None,
                    **kwargs):
        """Create one or more :term:`series` instances whose
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` properties
        are populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:pandas.DataFrame>`.

          .. code-block:: python

            # Given a Pandas DataFrame instance named "df"
            from highcharts_core.chart import Chart
            from highcharts_core.options.series.area import LineSeries

            # Creating a Series from the DataFrame
        
            ## EXAMPLE 1. Minimum code required. Creates one or more series.

            my_series = LineSeries.from_pandas(df)

            ## EXAMPLE 2. More precise configuration. Creates ONE series.

            my_series = LineSeries.from_pandas(df, series_index = 2)

            ## EXAMPLE 3. More precise configuration. Creates ONE series.

            my_series = LineSeries.from_pandas(df,
                                               property_map = {
                                                  'x': 'date',
                                                  'y': 'value',
                                                  'id': 'id'
                                               })
        
            ## EXAMPLE 4. More precise configuration. Creates THREE series.

            my_series = LineSeries.from_pandas(df,
                                               property_map = {
                                                  'x': 'date',
                                                  'y': ['value1', 'value2', 'value3'],
                                                  'id': 'id'
                                               })

        :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:pandas.DataFrame>` column. Defaults to 
          :obj:`None <python:None>`.

            .. note::
          
              If any of the values in ``property_map`` contain an iterable, then
              one series will be produced for each item in the iterable. For example,
              the following:
            
                .. code-block:: python
            
                  {
                      'x': 'timestamp',
                      'y': ['value1', 'value2', 'value3']
                  }
              
              will return *three* series, each of which will have its 
              :meth:`.x <CartesianData.x>` value populated from the column
              labeled ``'timestamp'``, and whose :meth:`.y <CartesianData.y>`
              values will be populated from the columns labeled ``'value1'``,
              ``'value2'``, and ``'value3'``, respectively.

        :type property_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to ``False``.
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: If supplied, return the series that Highcharts for Python
          generated from ``df`` at the ``series_index`` value. Defaults to 
          :obj:`None <python:None>`, which returns all series generated from ``df``.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :term:`series` instance (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) OR 
          :class:`list <python:list>` of series instances with its
          :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
          populated from the data in ``df``.
        :rtype: :class:`list <python:list>` of series instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descendent

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        
        # SCENARIO 0: Series in Rows
        if series_in_rows:
            return cls.from_pandas_in_rows(df,
                                           series_kwargs,
                                           series_index = series_index,
                                           **kwargs)

        # SCENARIO 1: Has Property Map
        if property_map:
            series_list = cls._from_pandas_multi_map(df,
                                                     property_map,
                                                     series_kwargs,
                                                     **kwargs)
            if len(series_list) == 1:
                return series_list[0]

            if series_index is not None:
                return series_list[series_index]

            return series_list

        # SCENARIO 2: Properties in KWARGS
        collection_cls = cls._data_collection_class()
        data_point_cls = cls._data_point_class()
        props_from_array = data_point_cls._get_props_from_array()
        if not props_from_array:
            props_from_array = ['x', 'y']

        property_map = {}
        for prop in props_from_array:
            if prop in kwargs:
                property_map[prop] = kwargs[prop]
        
        if property_map:
            series_list = cls._from_pandas_multi_map(df,
                                                     property_map,
                                                     series_kwargs)
            for index in range(len(series_list)):
                for key in kwargs:
                    if key not in props_from_array and key not in series_kwargs:
                        setattr(series_list[index], key, kwargs[key])
            
            if len(series_list) == 1:
                return series_list[0]

            if series_index is not None:
                return series_list[series_index]

            return series_list

        # SCENARIO 3: No Explicit Properties
        series_idx = kwargs.get('index', df.index)
        column_count = len(df.columns)
        supported_dimensions = collection_cls._get_supported_dimensions()
        
        # SCENARIO 3a: Single Series, Data Frame Columns align exactly to Data Point Properties
        if column_count in supported_dimensions:
            property_map = {}
            props_from_array = data_point_cls._get_props_from_array(length = column_count)
            if not props_from_array:
                props_from_array = ['x', 'y']
            property_map[props_from_array[0]] = series_idx

            for index, prop in enumerate(props_from_array[1:]):
                prop_value = df.iloc[:, index + 1].values
                property_map[prop] = prop_value
                
            collection = collection_cls()
            for key in property_map:
                setattr(collection, key, property_map[key])

            series_kwargs['data'] = collection
            series_instance = cls(**series_kwargs)
            for key in kwargs:
                if key not in series_kwargs and key not in property_map:
                    setattr(series_instance, key, kwargs[key])

            return series_instance

        # SCENARIO 3b: Multiple Series, Data Frame Columns correspond to multiples of Data Point Properties
        reversed_dimensions = sorted(supported_dimensions, reverse = True)
        columns_per_series = None
        if reversed_dimensions:
            for dimension in reversed_dimensions:
                if series_idx is not None and dimension > 1 and column_count % (dimension - 1) == 0:
                    if dimension > 2 and props_from_array[-1] == 'name':
                        columns_per_series = dimension - 2
                    else:
                        columns_per_series = dimension - 1
                    break
                elif dimension > 1 and column_count % dimension == 0:
                    columns_per_series = dimension
                    break
                elif dimension == 1:
                    columns_per_series = 1
        if not columns_per_series:
            raise errors.HighchartsPandasDeserializationError(
                f'Could not determine how to deserialize data frame with {column_count}'
                f' columns into a {collection_cls.__name__} instance. Please supply '
                f'more precise instructions using property_map or '
                f'by explicitly specificying data property kwargs.'
            )

        series_count = column_count // columns_per_series
        series_list = []
        for index in range(series_count):
            start = len(series_list) * columns_per_series

            property_map = {}
            if series_idx is not None:
                expected_length = columns_per_series + 1
            else:
                expected_length = columns_per_series
            props_from_array = data_point_cls._get_props_from_array(length = expected_length)
            if not props_from_array:
                props_from_array = ['x', 'y']
                
            property_map[props_from_array[0]] = series_idx

            has_implicit_series_name = 'name' not in kwargs and 'name' not in series_kwargs
            if has_implicit_series_name:
                series_name = df.columns[start]
            else:
                series_name = series_kwargs.get('name', None) or kwargs.get('name', None)

            for index, prop in enumerate(props_from_array[1:]):
                index = start + index
                prop_value = df.iloc[:, index].values
                property_map[prop] = prop_value
            
            collection = collection_cls()
            for key in property_map:
                setattr(collection, key, property_map[key])

            series_kwargs['data'] = collection
            series_kwargs['name'] = series_name
            series_instance = cls(**series_kwargs)
            for key in kwargs:
                if key not in series_kwargs and key not in property_map:
                    setattr(series_instance, key, kwargs[key])

            series_list.append(series_instance)

        if series_index is not None:
            return series_list[index]
          


        return series_list

    def load_from_pyspark(self,
                          df,
                          property_map):
        """Replaces the contents of the
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        with values from a `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
        :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`.

        :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
          should be loaded.
        :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :raises HighchartsPySparkDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if
          `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
          in the runtime environment
        """
        try:
            from pyspark.sql import DataFrame
        except ImportError:
            raise errors.HighchartsDependencyError('pyspark is not available in the '
                                                   'runtime environment. Please install '
                                                   'using "pip install pyspark"')

        if not checkers.is_type(df, ('DataFrame')):
            raise errors.HighchartsValueError(f'df is expected to be a PySpark DataFrame.'
                                              f'Was: {df.__class__.__name__}')

        property_map = validators.dict(property_map)
        column_instances = []
        for key in property_map:
            map_value = property_map[key]
            if map_value not in df.columns:
                raise errors.HighchartsPySparkDeserializationError(
                    f'Unable to find a column labeled "{map_value}" in df.'
                )
            column_instance = getattr(df, map_value)
            column_instances.append(column_instance)

        narrower_df = df.select(*column_instances)
        rdd_as_jsons = narrower_df.toJSON()

        df_as_dicts = [json.loads(x) for x in rdd_as_jsons.toLocalIterator()]
        records_as_dicts = []
        for record in df_as_dicts:
            record_as_dict = {}
            for key in property_map:
                map_value = property_map[key]
                record_as_dict[key] = record.get(map_value, None)
            records_as_dicts.append(record_as_dict)

        self.data = records_as_dicts

    @classmethod
    def from_pyspark(cls,
                     df,
                     property_map,
                     series_kwargs = None):
        """Create a :term:`series` instance whose
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        is populated from a `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
        :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`.

        :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
          should be loaded.
        :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :returns: A :term:`series` instance (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) with its
          :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
          populated from the data in ``df``.
        :rtype: :class:`list <python:list>` of series instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`)

        :raises HighchartsPySparkDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if
          `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
          in the runtime environment
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        instance = cls(**series_kwargs)
        instance.load_from_pyspark(df, property_map)

        return instance

    def to_chart(self, chart_kwargs = None, options_kwargs = None):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance containing the
        series instance.
        
        :param chart_kwargs: Optional keyword arguments to use when constructing the 
          :class:`Chart <highcharts_core.chart.Chart>` instance. Defaults to
          :obj:`None <python:None>`.
        :type chart_kwargs: :class:`dict <python:dict>`
        
        :param options_kwargs: Optional keyword arguments to use when constructing the
          chart's :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
          object. Defaults to :obj:`None <python:None>`.
          
          .. warning:: 
          
            If your ``chart_kwargs`` contains an ``options`` key, its value
            will be overwritten if you supply ``options_kwargs``.

        :type options_kwargs: :class:`dict <python:dict>`
        
        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance containing the
          series instance.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        """
        from highcharts_core.chart import Chart
        
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}
        
        as_chart = Chart(**chart_kwargs)
        if options_kwargs:
            as_chart.options = options_kwargs
            
        as_chart.add_series(self)
        
        return as_chart
    
    def display(self,
                global_options = None,
                container = None,
                retries = 5,
                interval = 1000,
                chart_kwargs = None,
                options_kwargs = None):
        """Display the series in `Jupyter Labs <https://jupyter.org/>`_ or
        `Jupyter Notebooks <https://jupyter.org/>`_.

        :param global_options: The :term:`shared options` to use when rendering the chart.
          Defaults to :obj:`None <python:None>`
        :type global_options: :class:`SharedOptions <highcharts_stock.global_options.shared_options.SharedOptions>`
          or :obj:`None <python:None>`

        :param container: The ID to apply to the HTML container when rendered in Jupyter Labs. Defaults to
          :obj:`None <python:None>`, which applies the :meth:`.container <highcharts_core.chart.Chart.container>`
          property if set, and ``'highcharts_target_div'`` if not set.

          .. note::

            Highcharts for Python will append a 6-character random string to the value of ``container``
            to ensure uniqueness of the chart's container when rendering in a Jupyter Notebook/Labs context. The
            :class:`Chart <highcharts_core.chart.Chart>` instance will retain the mapping between container and the
            random string so long as the instance exists, thus allowing you to easily update the rendered chart by
            calling the :meth:`.display() <highcharts_core.chart.Chart.display>` method again.

            If you wish to create a new chart from the instance that does not update the existing chart, then you can do
            so by specifying a new ``container`` value.

        :type container: :class:`str <python:str>` or :obj:`None <python:None>`

        :param retries: The number of times to retry rendering the chart. Used to avoid race conditions with the 
          Highcharts script. Defaults to 5.
        :type retries: :class:`int <python:int>`

        :param interval: The number of milliseconds to wait between retrying rendering the chart. Defaults to 1000 (1
          seocnd).
        :type interval: :class:`int <python:int>`

        :param chart_kwargs: Optional keyword arguments to use when constructing the 
          :class:`Chart <highcharts_core.chart.Chart>` instance. Defaults to
          :obj:`None <python:None>`.
        :type chart_kwargs: :class:`dict <python:dict>`
        
        :param options_kwargs: Optional keyword arguments to use when constructing the
          chart's :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
          object. Defaults to :obj:`None <python:None>`.
          
          .. warning:: 
          
            If your ``chart_kwargs`` contains an ``options`` key, its value
            will be overwritten if you supply ``options_kwargs``.

        :type options_kwargs: :class:`dict <python:dict>`

        :raises HighchartsDependencyError: if
          `ipython <https://ipython.readthedocs.io/en/stable/>`_ is not available in the
          runtime environment
        """
        as_chart = self.to_chart(chart_kwargs = chart_kwargs, 
                                 options_kwargs = options_kwargs)
        as_chart.display(global_options = global_options,
                         container = container,
                         retries = retries,
                         interval = interval)

    def convert_to(self, series_type):
        """Creates a new series of ``series_type`` from the current series.
        
        :param series_type: The series type that should be returned.
        :type series_type: :class:`str <python:str>` or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descended
          
        .. warning::
        
          This operation is *not* guaranteed to work converting between all series 
          types. This is because some series types have different properties, different
          logic / functionality for their properties, and may have entirely different
          data requirements.
          
          In general, this method is expected to be *lossy* in nature, meaning that when
          the series can be converted "close enough" the series will be converted. 
          However, if the target ``series_type`` does not support certain properties set
          on the original instance, then those settings will *not* be propagated to the 
          new series.
          
          In certain cases, this method may raise an 
          :exc:`HighchartsSeriesConversionError <highcharts_core.errors.HighchartsSeriesConversionError>`
          if the method is unable to convert (even losing some data) the original into 
          ``series_type``.
        
        :returns: A new series of ``series_type``, maintaining relevant properties and
          data from the original instance.
        :rtype: ``series_type``
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>` descendant
          
        :raises HighchartsSeriesConversionError: if unable to convert (even after losing 
          some data) the original instance into an instance of ``series_type``.
        :raises HighchartsValueError: if ``series_type`` is not a recognized series type

        """
        from highcharts_core.options.series.series_generator import SERIES_CLASSES
        if isinstance(series_type, str):
            series_type = series_type.lower()
            if series_type not in SERIES_CLASSES:
                raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                                  f'series type. Received: {series_type}')
            series_type_name = series_type
            series_type = SERIES_CLASSES.get(series_type)
        elif not issubclass(series_type, SeriesBase):
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')
        else:
            series_type_name = series_type.__name__

        as_js_literal = self.to_js_literal()
        try:
            target = series_type.from_js_literal(as_js_literal)
        except (ValueError, TypeError):
            raise errors.HighchartsSeriesConversionError(f'Unable to convert '
                                                         f'{self.__class__.__name__} instance '
                                                         f'to {series_type_name}')
        
        return target