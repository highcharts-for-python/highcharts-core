  .. code-block:: python

    my_chart = Chart(data = my_iterable, series_type = 'line')

This will create a :class:`Chart <highcharts_core.chart.Chart>` instance
with one :term:`series` of type ``line`` (represented as a 
:class:`LineSeries <highcharts_core.options.series.area.LineSeries>` instance).

Depending on how we've wrangled our data, we can similarly produce a chart
from a :class:`pandas.DataFrame <pandas:pandas.DataFrame>`, 
:class:`numpy.ndarray <numpy:numpy.ndarray>`, or Python :class:`dict <python:dict>`:

  .. code-block:: python

    # From a Pandas DataFrame

    my_chart = Chart.from_pandas(df, series_type = 'line')

    # From a Numpy ndarray

    my_chart = Chart.from_array(data = as_ndarray, series_type = 'line')

    # From a Python dict

    my_chart = Chart(data = as_dict, series_type = 'line')

All of these lines of code are equivalent, and should produce an identical
``my_chart``.

  .. seealso::
  
    * :doc:`Using Highcharts Core for Python with Pandas <pandas>`
    * :doc:`Using Highcharts Core for Python with CSVs <csv>`
    * :doc:`Working with Highcharts for Python Series Instances <series>`
    * :doc:`Working with Data in the Highcharts for Python Toolkit <data>`
