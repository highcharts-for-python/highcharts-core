  .. note::

    The ``.from_pyspark()`` method is available on all :term:`series` classes and on the
    :class:`Chart <highcharts_core.chart.Chart>` class, allowing you to either assemble
    a series or an entire chart from Pandas
    :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` with only one method call.

.. code-block:: python

  # Given a PySpark DataFrame instance named "df"

  from highcharts_core.chart import Chart
  from highcharts_core.options.series.area import LineSeries

  # Create a LineSeries from the PySpark DataFrame "df"
  my_series = LineSeries.from_pyspark(df,
                                      property_map = {
                                          'x': 'date',
                                          'y': 'value',
                                          'id': 'id'
                                      })

  # Create a new Chart witha LineSeries from the DataFrame "df"
  my_chart = Chart.from_pyspark(df,
                                property_map = {
                                    'x': 'date',
                                    'y': 'value',
                                    'id': 'id'
                                },
                                series_type = 'line')

.. collapse:: Method Signature

  .. seealso::

    * :meth:`Chart.from_pyspark() <highcharts_core.chart.Chart.from_pyspark>`

  .. method:: .from_pyspark(cls, df, property_map, series_kwargs = None)
    :noindex:
    :classmethod:

    Create a :term:`series` instance whose
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
