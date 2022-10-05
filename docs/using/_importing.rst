.. tabs::

  .. tab:: from Precise Location

    .. tip::

      **Best Practice!**

      This method of importing **Highcharts for Python** objects yields the fastest
      performance for the ``import`` statement. However, it is more verbose and requires
      you to navigate the extensive :doc:`Highcharts for Python API </api>`.

    .. code-block:: python

      # Import classes using precise module indications. For example:
      from highcharts_python.chart import Chart
      from highcharts_python.global_options.shared_options import SharedOptions
      from highcharts_python.options import HighchartsOptions
      from highcharts_python.options.plot_options.bar import BarOptions
      from highcharts_python.options.series.bar import BarSeries

  .. tab:: from ``.highcharts``

    .. caution::

      This method of importing **Highcharts for Python** classes has relatively slow
      performance because it imports hundreds of different classes from across the entire
      library. This performance impact may be acceptable to you in your use-case, but
      do use at your own risk.

    .. code-block:: python

      # Import objects from the catch-all ".highcharts" module.
      from highcharts_python import highcharts

      # You can now access specific classes without individual import statements.
      highcharts.Chart
      highcharts.SharedOptions
      highcharts.HighchartsOptions
      highcharts.BarOptions
      highcharts.BarSeries
