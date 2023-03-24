.. code-block:: python

  # Given a LineSeries named "my_series", and a CSV file named "updated-data.csv"
  my_series.load_from_csv('updated-data.csv',
                          property_column_map = {
                              'x': 0,
                              'y': 3,
                              'id': 'id'
                          })

.. collapse:: Method Signature

  .. method:: .load_from_csv(self, as_string_or_file, property_column_map, has_header_row = True, delimiter = ',', null_text = 'None', wrapper_character = "'", line_terminator = '\r\n', wrap_all_strings = False, double_wrapper_character_when_nested = False, escape_character = '\\')
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
            my_series.load_from_csv('some-csv-file.csv',
                                    property_column_map = {
                                        'x': 0,
                                        'y': 3,
                                        'id': 'id'
                                    })

        As the example above shows, data is loaded into the ``my_series`` instance from
        the CSV file with a filename ``some-csv-file.csv``. The
        :meth:`x <CartesianData.x>`
        values for each data point will be taken from the first (index 0) column in the
        CSV file. The :meth:`y <CartesianData.y>` values will be taken from the fourth
        (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>` values
        will be taken from a column whose header row is labeled ``'id'`` (regardless of
        its index).

    :param as_string_or_file: The CSV data to load, either as a :class:`str <python:str>`
      or as the name of a file in the runtime envirnoment. If a file, data will be read
      from the file.

      .. tip::

        Unwrapped empty column values are automatically interpreted as null
        (:obj:`None <python:None>`).

    :type as_string_or_file: :class:`str <python:str>` or Path-like

    :param property_column_map: A :class:`dict <python:dict>` used to indicate which
      data point property should be set to which CSV column. The keys in the
      :class:`dict <python:dict>` should correspond to properties in the data point class,
      while the value can either be a numerical index (starting with 0) or a
      :class:`str <python:str>` indicating the label for the CSV column.

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

    :returns: A collection of data points descended from
      :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` as
      appropriate for the series class.
    :rtype: :class:`list <python:list>` of instances descended from
      :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`

    :raises HighchartsDeserializationError: if unable to parse the CSV data correctly
