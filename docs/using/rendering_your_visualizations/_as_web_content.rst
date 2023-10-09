.. tabs::

  .. tab:: as a Highcharts JS Chart

    .. code-block:: python

      from highcharts_core.chart import Chart
      from highcharts_core.options.series.area import LineSeries

      my_chart = Chart(data = [0, 5, 3, 5], series_type = 'line')

      as_js_literal = my_chart.to_js_literal()

      # This will produce a string equivalent to:
      #
      # document.addEventListener('DOMContentLoaded', function() {
      #   const myChart = Highcharts.chart('target_div', {
      #      series: {
      #          type: 'line',
      #          data: [0, 5, 3, 5]
      #      }
      #   });
      # });
