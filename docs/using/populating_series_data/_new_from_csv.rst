  .. note::

    The ``.from_csv()`` method is available on all :term:`series` classes and on the
    :class:`Chart <highcharts_core.chart.Chart>` class, allowing you to either assemble
    a series or an entire chart from a CSV file with only one method call.

.. code-block:: python

  from highcharts_core.chart import Chart
  from highcharts_core.options.series.area import LineSeries

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

  # Create a chart with one or more LineSeries instances from 
  # the CSV file "some-csv-file.csv".

  # EXAMPLE 1: The minimum code:

  my_chart = Chart.from_csv('some-csv-file.csv', series_type = 'line')
  
  # EXAMPLE 2: For more precise configuration and *one* series:

  my_chart = Chart.from_csv('some-csv-file.csv',
                            property_column_map = {
                                'x': 0,
                                'y': 3,
                                'id': 'id'
                            },
                            series_type = 'line')
  
  # EXAMPLE 3: For more precise configuration and *multiple* series:

  my_chart = Chart.from_csv('some-csv-file.csv',
                            property_column_map = {
                                'x': 0,
                                'y': [3, 5, 8],
                                'id': 'id'
                            },
                            series_type = 'line')

.. collapse:: Method Signature

  .. seealso::

    * :meth:`Chart.from_csv() <highcharts_core.chart.Chart.from_csv>`
    * :meth:`SeriesBase.from_csv_in_rows() <highcharts_core.options.series.base.SeriesBase.from_csv_in_rows>`

  .. method:: .from_csv(cls, as_string_or_file, property_column_map = None, series_kwargs = None, has_header_row = True, delimiter = ',', null_text = 'None', wrapper_character = "'", line_terminator = '\r\n', wrap_all_strings = False, double_wrapper_character_when_nested = False, escape_character = '\\', series_in_rows = False, series_index = None, **kwargs)
    :noindex:
    :classmethod:

    Create one or more :term:`series` instances with
    :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` populated from data in a CSV string 
    or file.

      .. note::

        To produce one or more
        :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` instances, the
        minimum code required would be:

          .. code-block:: python

            # EXAMPLE 1. The minimum code:
            my_series = LineSeries.from_csv('some-csv-file.csv')

            # EXAMPLE 2. For more precise configuration and ONE series:
            my_series = LineSeries.from_csv('some-csv-file.csv',
                                            property_column_map = {
                                                'x': 0,
                                                'y': 3,
                                                'id': 'id'
                                            })

            # EXAMPLE 3. For more precise configuration and MULTIPLE series:
            my_series = LineSeries.from_csv('some-csv-file.csv',
                                            property_column_map = {
                                                'x': 0,
                                                'y': [3, 5, 8],
                                                'id': 'id'
                                            })

        As the example above shows, data is loaded into the ``my_series`` instance
        from the CSV file with a filename ``some-csv-file.csv``. 
        
        In EXAMPLE 1, the method will return one or more series where each series 
        will default to having its :meth:`.x <CartesianData.x>` values taken from 
        the first (index 0) column in the CSV, and one 
        :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` 
        instance will be created for each subsequent column (which will populate 
        that series' :meth:`.y <CartesianData.y>` values.
        
        In EXAMPLE 2, the chart will contain one series, where the
        :meth:`.x <CartesianData.x>`
        values for each data point will be taken from the first (index 0) column in
        the CSV file. The :meth:`.y <CartesianData.y>` values will be taken from the
        fourth (index 3) column in the CSV file. And the :meth:`.id <CartesianData.id>`
        values will be taken from a column whose header row is labeled ``'id'``
        (regardless of its index).
        
        In EXAMPLE 3, the chart will contain three series, all of which will have
        :meth:`.x <CartesianData.x>` values taken from the first (index 0) column,
        :meth:`.id <CartesianData.id>` values from the column whose header row is 
        labeled ``'id'``, and whose :meth:`.y <CartesianData.y>` will be taken
        from the fourth (index 3) column for the first series, the sixth (index 5)
        column for the second series, and the ninth (index 8) column for the third
        series.

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

    :type property_column_map: :class:`dict <python:dict>`

    :param series_type: Indicates the series type that should be created from the CSV
      data. Defaults to ``'line'``.

      .. warning::

        This argument is *not supported* when calling 
        :meth:`.from_csv() <highcharts_core.options.series.base.SeriesBase.from_csv>` on 
        a :term:`series` instance. It is only supported when calling 
        :meth:`Chart.from_csv() <highcharts_core.chart.Chart.from_csv>`.

    :type series_type: :class:`str <python:str>`

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
      the CSV data. Defaults to ``'\r\n'``.
    :type line_terminator: :class:`str <python:str>`

    :param line_terminator: The string used to indicate the end of a line/record in the
      CSV data. Defaults to ``'\r\n'``.

      .. note::

        The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
        parameter and always applies ``'\r\n'``, by design. The Python docs say this may
        change in the future, so for future backwards compatibility we are including it
        here.

    :type line_terminator: :class:`str <python:str>`

    :param wrap_all_strings: If ``True``, indicates that the CSV file has all string data
      values wrapped in quotation marks. Defaults to ``False``.

      .. warning::

        If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce any
        value that is *not* wrapped in quotation marks to a :class:`float <python:float>`.
        This can cause unexpected behavior, and typically we recommend leaving this as
        ``False`` and then re-casting values after they have been parsed.

    :type wrap_all_strings: :class:`bool <python:bool>`

    :param double_wrapper_character_when_nested: If ``True``, quote character is doubled
      when appearing within a string value. If ``False``, the ``escape_character`` is used
      to prefix quotation marks. Defaults to ``False``.
    :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

    :param escape_character: A one-character string that indicates the character used to
      escape quotation marks if they appear within a string value that is already wrapped
      in quotation marks. Defaults to ``\\`` (which is Python for ``'\'``, which is
      Python's native escape character).
    :type escape_character: :class:`str <python:str>`

    :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
      with x-values taken from column names, y-values taken from row values, and
      the series name taken from the row index. Defaults to ``False``.
    :type series_in_rows: :class:`bool <python:bool>`

    :param series_index: if :obj:`None <python:None>`, will attempt to populate
      the chart with multiple series from the CSV data. If an :class:`int <python:int>`
      is supplied, will populate the chart only with the series found at 
      ``series_index``.

    :type series_index: :class:`int <python:int>`, slice, or 
      :obj:`None <python:None>`

    :param **kwargs: Remaining keyword arguments will be attempted on the resulting
      :term:`series` instance and the data points it contains.

    :returns: One or more :term:`series` instances (descended from
      :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) with its
      :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
      populated from the CSV data in ``as_string_or_file``.
    :rtype: :class:`list <python:list>` of series instances (descended from
      :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or
      :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>` instance

    :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
      CSV columns by their label, but the CSV data does not contain a header row
