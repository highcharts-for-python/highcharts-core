  .. note::

    The ``.from_pandas()`` method is available on all :term:`series` classes and on the
    :class:`Chart <highcharts_core.chart.Chart>` class, allowing you to either assemble
    a series or an entire chart from Pandas :class:`DataFrame <pandas:pandas.DataFrame>`
    with only one method call.

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

  ## EXAMPLE 5. Minimum code required. Creates one or more series
  ## from a dataframe where each row in the dataframe is a 
  ## Highcharts series. The two lines of code below are equivalent.

  my_series = LineSeries.from_pandas_in_rows(df)
  
  # Creating a Chart with a lineSeries from the DataFrame.

  ## EXAMPLE 1. Minimum code required. Populates the chart with
  ## one or more series.

  my_chart = Chart.from_pandas(df)

  ## EXAMPLE 2. More precise configuration. Populates the chart with
  ## one series.

  my_chart = Chart.from_pandas(df, series_index = 2)

  ## EXAMPLE 3. More precise configuration. Populates the chart with
  ## ONE series.

  my_chart = Chart.from_pandas(df,
                               property_map = {
                                   'x': 'date',
                                   'y': 'value',
                                   'id': 'id'
                               },
                               series_type = 'line')
  
  ## EXAMPLE 4. More precise configuration. Populates the chart with
  ## THREE series.

  my_chart = Chart.from_pandas(df,
                               property_map = {
                                   'x': 'date',
                                   'y': ['value1', 'value2', 'value3'],
                                   'id': 'id'
                               },
                               series_type = 'line')

  ## EXAMPLE 5. Minimum code required. Creates a Chart populated
  ## with series from a dataframe where each row in the dataframe
  ## becomes a series on the chart.

  my_chart = Chart.from_pandas_in_rows(df)


.. collapse:: Method Signature

  .. seealso::

    * :meth:`Chart.from_pandas() <highcharts_core.chart.Chart.from_pandas>`
    * :meth:`Chart.from_pandas_in_rows() <highcharts_core.chart.Chart.from_pandas_in_rows>`
    * :meth:`SeriesBase.from_pandas_in_rows() <highcharts_core.options.series.base.SeriesBase.from_pandas_in_rows>`

  .. method:: .from_pandas(cls, df, property_map = None, series_kwargs = None, series_in_rows = False, series_index = None, **kwargs)
    :noindex:
    :classmethod:

    Create one or more :term:`series` instances whose
    :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` properties
    are populated from a `pandas <https://pandas.pydata.org/>`_
    :class:`DataFrame <pandas:pandas.DataFrame>`.

    :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
      loaded.
    :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

    :param property_map: An optional :class:`dict <python:dict>` used to indicate which
      data point property should be set to which column in ``df``. The keys in the
      :class:`dict <python:dict>` should correspond to properties in the data point
      class, while the value should indicate the label for the
      :class:`DataFrame <pandas:pandas.DataFrame>` column.

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

    :type property_map: :class:`dict <python:dict>`

    :param series_type: Indicates the series type that should be created from the CSV
      data. Defaults to ``'line'``.

      .. warning::

        This argument is *not supported* when calling 
        :meth:`.from_pandas() <highcharts_core.options.series.base.SeriesBase.from_pandas>` on 
        a :term:`series`. It is only supported when calling 
        :meth:`Chart.from_csv() <highcharts_core.chart.Chart.from_pandas>`.

    :type series_type: :class:`str <python:str>`

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

    :returns: One or more :term:`series` instances (descended from
      :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) with the
      :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
      populated from the data in ``df``.
    :rtype: :class:`list <python:list>` of series instances (descended from
      :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`), or
      a :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descended
      instance

    :raises HighchartsPandasDeserializationError: if ``property_map`` references
      a column that does not exist in the data frame
    :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org>`__ is
      not available in the runtime environment
