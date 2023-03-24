.. code-block:: python

  # Given a LineSeries named "my_series", and a PySpark DataFrame variable named "df"
  my_series.load_from_pyspark(df,
                              property_map = {
                                  'x': 'date',
                                  'y': 'value',
                                  'id': 'id'
                              })

.. collapse:: Method Signature

  .. method:: .load_from_pyspark(self, df, property_map)
    :noindex:

    Replaces the contents of the
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
