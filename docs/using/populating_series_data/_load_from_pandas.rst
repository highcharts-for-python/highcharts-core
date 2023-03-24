.. code-block:: python

  # Given a LineSeries named "my_series", and a Pandas DataFrame variable named "df"
  my_series.load_from_pandas(df,
                             property_map = {
                                 'x': 'date',
                                 'y': 'value',
                                 'id': 'id'
                             })

.. collapse:: Method Signature

  .. method:: .load_from_pandas(self, df, property_map)
    :noindex:

    Replace the contents of the
    :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
    with data points populated from a `pandas <https://pandas.pydata.org/>`__
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
    :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`__ is
      not available in the runtime environment
