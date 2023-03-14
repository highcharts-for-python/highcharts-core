.. code-block:: python

  from highcharts_core.chart import Chart
  from highcharts_core.options.series.area import LineSeries
  from highcharts_core.options.series.bar import BarSeries

  # Create a Chart instance called "my_chart" with an empty set of options
  my_chart = Chart(options = {})

  # Create a couple Series instances
  my_series1 = LineSeries()
  my_series2 = BarSeries()

  # Populate the options series list with the series you created.
  my_chart.options.series = [my_series1, my_series2]

  # Make a new one, and append it.
  my_series3 = LineSeries()
  my_chart.options.series.append(my_series3)
