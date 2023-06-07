from typing import Optional, List
from decimal import Decimal

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

from validator_collection import validators, checkers

from highcharts_core import errors, utility_functions, constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.options.series.data.base import DataBase


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

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return f'series.{self.type}'

    @property
    def data(self) -> Optional[List[DataBase]]:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`DataBase` or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    @class_sensitive(DataBase, force_iterable = True)
    def data(self, value):
        self._data = value

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

    def load_from_csv(self,
                      as_string_or_file,
                      property_column_map,
                      has_header_row = True,
                      delimiter = ',',
                      null_text = 'None',
                      wrapper_character = "'",
                      line_terminator = '\r\n',
                      wrap_all_strings = False,
                      double_wrapper_character_when_nested = False,
                      escape_character = "\\"):
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
          :class:`str <python:str>` indicating the label for the CSV column.

          .. warning::

            If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
            file *must* have a header row (this is expected, by default). If there is no
            header row and a :class:`str <python:str>` value is found, a
            :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>`

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

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        try:
            as_string_or_file = as_string_or_file.strip()
        except AttributeError:
            pass

        property_column_map = validators.dict(property_column_map, allow_empty = False)
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

        for key in cleaned_column_map:
            map_value = cleaned_column_map[key]
            if map_value not in columns:
                if isinstance(map_value, str):
                    raise errors.HighchartsCSVDeserializationError(
                        f'property_column_map is looking for a column labeled '
                        f'"{map_value}", but no corresponding column was found.'
                    )
                else:
                    raise errors.HighchartsCSVDeserializationError(
                        f'property_column_map is looking for a column indexed '
                        f'{map_value}, but no corresponding column was found.'
                    )

        data_point_dicts = []
        for record in csv_records:
            data_point_dict = {}
            for key in cleaned_column_map:
                map_value = cleaned_column_map[key]
                value = record.get(map_value, None)
                if value and isinstance(value, str) and ',' in value:
                    test_value = value.replace(delimiter, '')
                    if checkers.is_numeric(test_value):
                        value = test_value

                data_point_dict[key] = value
                
            data_point_dicts.append(data_point_dict)

        self.data = data_point_dicts

    @classmethod
    def from_csv(cls,
                 as_string_or_file,
                 property_column_map,
                 has_header_row = True,
                 series_kwargs = None,
                 delimiter = ',',
                 null_text = 'None',
                 wrapper_character = "'",
                 line_terminator = '\r\n',
                 wrap_all_strings = False,
                 double_wrapper_character_when_nested = False,
                 escape_character = "\\"):
        """Create a new :term:`series` instance with a
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        populated from data in a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_series = LineSeries.from_csv('some-csv-file.csv',
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
          :class:`str <python:str>` indicating the label for the CSV column.

          .. warning::

            If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
            file *must* have a header row (this is expected, by default). If there is no
            header row and a :class:`str <python:str>` value is found, a
            :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>`

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

        :returns: A :term:`series` instance (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) with its
          :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
          populated from the CSV data in ``as_string_or_file``.
        :rtype: :class:`list <python:list>` of series instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`)

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        instance = cls(**series_kwargs)
        instance.load_from_csv(as_string_or_file,
                               property_column_map,
                               has_header_row = has_header_row,
                               delimiter = delimiter,
                               null_text = null_text,
                               wrapper_character = wrapper_character,
                               line_terminator = line_terminator,
                               wrap_all_strings = wrap_all_strings,
                               double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                               escape_character = escape_character)

        return instance

    def load_from_pandas(self,
                         df,
                         property_map):
        """Replace the contents of the
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        with data points populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:DataFrame>`.

        :param df: The :class:`DataFrame <pandas:DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:DataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        try:
            from pandas import DataFrame, isna
        except ImportError:
            raise errors.HighchartsDependencyError('pandas is not available in the '
                                                   'runtime environment. Please install '
                                                   'using "pip install pandas"')

        if not checkers.is_type(df, ('DataFrame', 'Series')):
            raise errors.HighchartsValueError(f'df is expected to be a pandas DataFrame '
                                              f'or Series. Was: {df.__class__.__name__}')

        if not property_map:
            raise errors.HighchartsValueError('property_map cannot be None or empty')

        property_map = validators.dict(property_map)
        for key in property_map:
            map_value = property_map[key]
            if map_value not in df.columns:
                raise errors.HighchartsPandasDeserializationError(
                    f'Unable to find a column labeled "{map_value}" in df.'
                )
        narrower_df = df[[property_map[key] for key in property_map]]

        df_as_dicts = narrower_df.to_dict(orient = 'records')

        records_as_dicts = []
        for record in df_as_dicts:
            record_as_dict = {}
            for key in property_map:
                map_value = property_map[key]
                record_as_dict[key] = record.get(map_value, None)
                if isna(record_as_dict[key]):
                    record_as_dict[key] = constants.EnforcedNull
            records_as_dicts.append(record_as_dict)
            
        self.data = records_as_dicts

    @classmethod
    def from_pandas(cls,
                    df,
                    property_map,
                    series_kwargs = None):
        """Create a :term:`series` instance whose
        :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
        is populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:DataFrame>`.

        :param df: The :class:`DataFrame <pandas:DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:DataFrame>` column.
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

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        instance = cls(**series_kwargs)
        instance.load_from_pandas(df, property_map)

        return instance

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
