  .. note::

    The ``.from_pandas()`` method is available on all :term:`series` classes and on the
    :class:`Chart <highcharts_core.chart.Chart>` class, allowing you to either assemble
    a series or an entire chart from Pandas :class:`DataFrame <pandas:DataFrame>`
    with only one method call.

.. code-block:: python

  # Given a Pandas DataFrame instance named "df"
  from highcharts_core.chart import Chart
  from highcharts_core.options.series.area import LineSeries

  # Creating a Series from the DataFrame
  my_series = LineSeries.from_pandas(df,
                                     property_map = {
                                         'x': 'date',
                                         'y': 'value',
                                         'id': 'id'
                                     })

  # Creating a Chart with a lineSeries from the DataFrame.
  my_chart = Chart.from_pandas(df,
                               property_map = {
                                   'x': 'date',
                                   'y': 'value',
                                   'id': 'id'
                               },
                               series_type = 'line')


.. collapse:: Method Signature

  .. seealso::

    * :meth:`Chart.from_pandas() <highcharts_core.chart.Chart.from_pandas>`

  .. method:: .from_pandas(cls, df, property_map, series_kwargs = None)
    :noindex:
    :classmethod:

    Create a :term:`series` instance whose
    :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
    is populated from a `pandas <https://pandas.pydata.org/>`__
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
    :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org>`__ is
      not available in the runtime environment
