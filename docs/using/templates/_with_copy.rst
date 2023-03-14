If you have an existing **Highcharts for Python** instance, you can copy its
properties to another object using the ``.copy()`` method. You can therefore set up
one chart, and then copy its properties to other chart objects with one method call.

  .. code-block:: python

    type_1_chart = Chart.from_js_literal('../../project_resources/highcharts_config/line-template-01.js')
    other_chart = type_1_chart.copy(other_chart, overwrite = True)

  .. tip::

    The :meth:`Chart.copy() <highcharts_core.chart.Chart.copy>` method supports a
    special keyword argument, ``preverse_data`` which if set to ``True`` will copy
    properties (unless ``overwrite = False``) but will *not* overwrite any data. This
    can be very useful to replicating the configuration of your chart across multiple
    charts that have different series and data.

      .. code-block:: python

        other_chart = Chart()
        other_chart.add_series(
          LineSeries.from_csv('../../project_resources/data_files/data-file-02.csv')
        )

        other_chart = type_1_chart.copy(other_chart,
                                        preserve_data = True)
