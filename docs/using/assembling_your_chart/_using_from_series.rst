  .. note::

    ``.from_series()`` is supported by both the
    :class:`Chart <highcharts_core.chart.Chart>` and
    :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
    classes

.. code-block:: python

  my_series1 = LineSeries()
  my_series2 = BarSeries()

  my_chart = Chart.from_series(my_series1, my_series2, options = None)

.. collapse:: Method Signature

  .. method:: .from_series(cls, *series, kwargs = None)
    :noindex:

    Creates a new :class:`Chart <highcharts_core.chart.Chart>` instance populated
    with ``series``.

    :param series: One or more :term:`series` instances (descended from
      :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
      instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
      coercable to one
    :type series: :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
      or coercable

    :param kwargs: Other properties to use as keyword arguments for the instance to be
      created.

      .. warning::

        If ``kwargs`` sets the
        :meth:`options.series <highcharts_core.options.HighchartsOptions.series>`
        property, that setting will be *overridden* by the contents of ``series``.

    :type kwargs: :class:`dict <python:dict>`

    :returns: A new :class:`Chart <highcharts_core.chart.Chart>` instance
    :rtype: :class:`Chart <highcharts_core.chart.Chart>`
