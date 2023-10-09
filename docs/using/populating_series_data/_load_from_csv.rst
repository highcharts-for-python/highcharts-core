.. code-block:: python

  # Given a LineSeries named "my_series", and a CSV file named "updated-data.csv"

  my_series.load_from_csv('updated-data.csv')

  # For more precise control over how the CSV data is parsed, 
  # you can supply a mapping of series properties to their CSV column
  # either by index position *or* by column header name.

  my_series.load_from_csv('updated-data.csv',
                          property_column_map = {
                              'x': 0,
                              'y': 3,
                              'id': 'id'
                          })

.. collapse:: Method Signature

  .. method:: .load_from_csv(self, as_string_or_file, property_column_map = None, has_header_row = True, delimiter = ',', null_text = 'None', wrapper_character = "'", line_terminator = '\r\n', wrap_all_strings = False, double_wrapper_character_when_nested = False, escape_character = '\\', series_in_rows = 'line', series_index = None, **kwargs)
    :noindex:

    Updates the series instance with a collection of data points (descending from
    :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`) from
    ``as_string_or_file`` by traversing the rows of data and extracting the values from
    the columns indicated in ``property_column_map``.

      .. warning::

        This method will overwrite the contents of the series instance's
        :meth:`data <highcharts_core.options.series.base.SeriesBase>` property.

      .. note::

        For an example
        :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
        minimum code required would be:

          .. code-block:: python

            my_series = LineSeries()
            
            # Minimal code - will attempt to update the line series
            # taking x-values from the first column, and y-values from
            # the second column. If there are too many columns in the CSV,
            # will throw an error.
            my_series = my_series.from_csv('some-csv-file.csv')
            
            # More precise code - will attempt to update the line series
            # mapping columns in the CSV file to properties on the series
            # instance.
            my_series = my_series.from_csv('some-csv-file.csv',
                                            property_column_map = {
                                                'x': 0,
                                                'y': 3,
                                                'id': 'id'
                                            })

        As the example above shows, data is loaded into the ``my_series`` instance
        from the CSV file with a filename ``some-csv-file.csv``. Unless otherwise
        specified, the :meth:`.x <CartesianData.x>` values for each data point will
        be taken from the first (index 0) column in the CSV file, while the 
        :meth:`.y <CartesianData.y>` values will be taken from the second column.
        
        If the CSV has more than 2 columns, then this will throw an
        :exc:`HighchartsCSVDeserializationError` because the function is not certain
        which columns to use to update the series. If this happens, you can precisely
        specify which columns to use by providing a ``property_column_map`` argument, 
        as shown in the second example. In that second example, the
        :meth:`.x <CartesianData.x>` values for each data point will be taken from 
        the first (index 0) column in the CSV file. The :meth:`.y <CartesianData.y>` 
        values will be taken from the fourth (index 3) column in the CSV file. And 
        the :meth:`.id <CartesianData.id>`
        values will be taken from a column whose header row is labeled ``'id'``
        (regardless of its index).

    :param as_string_or_file: The CSV data to load, either as a :class:`str <python:str>`
      or as the name of a file in the runtime envirnoment. If a file, data will be read
      from the file.

      .. tip::

        Unwrapped empty column values are automatically interpreted as null
        (:obj:`None <python:None>`).

    :type as_string_or_file: :class:`str <python:str>` or Path-like

    :param property_column_map: An optional :class:`dict <python:dict>` used to indicate 
      which data point property should be set to which CSV column. The keys in the
      :class:`dict <python:dict>` should correspond to properties in the data point class,
      while the value can either be a numerical index (starting with 0) or a
      :class:`str <python:str>` indicating the label for the CSV column. Defaults to 
      :obj:`None <python:None>`.

      .. warning::

        If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV file
        *must* have a header row (this is expected, by default). If there is no header row
        and a :class:`str <python:str>` value is found, a
        :exc:`HighchartsDeserializationError` will be raised.

    :type property_column_map: :class:`dict <python:dict>`

    :param has_header_row: If ``True``, indicates that the first row of
      ``as_string_or_file`` contains column labels, rather than actual data. Defaults to
      ``True``.
    :type has_header_row: :class:`bool <python:bool>`

    :param delimiter: The delimiter used between columns. Defaults to ``,``.
    :type delimiter: :class:`str <python:str>`

    :param wrapper_character: The string used to wrap string values when
      wrapping is applied. Defaults to ``'``.
    :type wrapper_character: :class:`str <python:str>`

    :param null_text: The string used to indicate an empty value if empty
      values are wrapped. Defaults to `None`.
    :type null_text: :class:`str <python:str>`

    :param line_terminator: The string used to indicate the end of a line/record in the
      CSV data. Defaults to ``'\r\n'``.

      .. warning::

        The Python :mod:`csv <python:csv>` module currently ignores the
        ``line_terminator`` parameter and always applies ``'\r\n'``, by design. The Python
        docs say this may change in the future, so for future backwards compatibility we
        are including it here.

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
      the series name taken from the row index. Defaults to 
      :obj:`False <python:False>`.
    :type series_in_rows: :class:`bool <python:bool>`

    :param series_index: if :obj:`None <python:None>`, will raise a 
      :exc:`HighchartsCSVDeserializationError <highcharts_core.errors.HighchartsCSVDeserializationError>`
      if the CSV data contains more than one series and no ``property_column_map`` 
      is provided. Otherwise, will update the instance with the series found 
      in the CSV at the ``series_index`` value. Defaults to 
      :obj:`None <python:None>`.

        .. tip::

          This argument is *ignored* if ``property_column_map`` is provided.

    :type series_index: :class:`int <python:int>` or :obj:`None <python:None>`

    :param **kwargs: Remaining keyword arguments will be attempted on the resulting
      :term:`series` instance and the data points it contains.

    :returns: A collection of data points descended from
      :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` as
      appropriate for the series class.
    :rtype: :class:`list <python:list>` of instances descended from
      :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`

    :raises HighchartsDeserializationError: if unable to parse the CSV data correctly
