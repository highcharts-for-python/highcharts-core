.. code-block:: python

  # Given a LineSeries named "my_series", and a Pandas DataFrame variable named "df"
  
  # EXAMPLE 1. The minimum code required to update the series:

  my_series.load_from_pandas(df)

  # EXAMPLE 2. For more precise control over how the ``df`` is parsed, 
  # you can supply a mapping of series properties to their dataframe column.

  my_series.load_from_pandas(df,
                             property_map = {
                                 'x': 'date',
                                 'y': 'value',
                                 'id': 'id'
                             })

  # EXAMPLE 3. For more precise control, specify the index of the
  # Highcharts for Python series instance to use in updating your series' data.

  my_series.load_from_pandas(df, series_index = 3)


.. collapse:: Method Signature

  .. method:: .load_from_pandas(self, df, property_map = None, series_in_rows = False, series_index = None)
    :noindex:

    Replace the contents of the
    :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
    with data points populated from a `pandas <https://pandas.pydata.org/>`__
    :class:`DataFrame <pandas:pandas.DataFrame>`.

    :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
      loaded.
    :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

    :param property_map: A :class:`dict <python:dict>` used to indicate which
      data point property should be set to which column in ``df``. The keys in the
      :class:`dict <python:dict>` should correspond to properties in the data point
      class, while the value should indicate the label for the
      :class:`DataFrame <pandas:pandas.DataFrame>` column.
    :type property_map: :class:`dict <python:dict>`

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

    :type series_index: :class:`int <python:int>`, slice, or 
      :obj:`None <python:None>`

    :raises HighchartsPandasDeserializationError: if ``property_map`` references
      a column that does not exist in the data frame
    :raises HighchartsPandasDeserializationError: if ``series_index`` is 
      :obj:`None <python:None>`, and it is ambiguous which series generated from
      the dataframe should be used
    :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`__ is
      not available in the runtime environment
