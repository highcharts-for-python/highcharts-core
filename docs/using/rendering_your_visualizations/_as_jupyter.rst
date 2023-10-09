.. code-block:: python

  from highcharts_core.chart import Chart
  from highcharts_core.global_options.shared_options import SharedOptions

  my_chart = Chart(data = [0, 5, 3, 5], series_type = 'line')

  # Now this will render the contents of "my_chart" in your Jupyter Notebook
  my_chart.display()

  # You can also supply shared options to display to make sure that they are applied:
  my_shared_options = SharedOptions()

  # Now this will render the contents of "my_chart" in your Jupyter Notebook, but applying
  # your shared options
  my_chart.display(global_options = my_shared_options)

.. collapse:: Method Signature

  .. method:: display(self, global_options = None, container = None, retries = 5, interval = 1000)
    :noindex:

    Display the chart in `Jupyter Labs <https://jupyter.org/>`__ or
    `Jupyter Notebooks <https://jupyter.org/>`__.

    :param global_options: The :term:`shared options` to use when rendering the chart.
      Defaults to :obj:`None <python:None>`
    :type global_options: :class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`
      or :obj:`None <python:None>`

    :param container: The ID to apply to the HTML container when rendered in Jupyter Labs. Defaults to
      :obj:`None <python:None>`, which applies the :meth:`.container <highcharts_core.chart.Chart.container>`
      property if set, and ``'highcharts_target_div'`` if not set.

      .. note::

        Highcharts for Python will append a 6-character random string to the value of ``container``
        to ensure uniqueness of the chart's container when rendering in a Jupyter Notebook/Labs context. The
        :class:`Chart <highcharts_core.chart.Chart>` instance will retain the mapping between container and the
        random string so long as the instance exists, thus allowing you to easily update the rendered chart by
        calling the :meth:`.display() <highcharts_core.chart.Chart.display>` method again.

        If you wish to create a new chart from the instance that does not update the existing chart, then you can do
        so by specifying a new ``container`` value.

    :type container: :class:`str <python:str>` or :obj:`None <python:None>`

    :param retries: The number of times to retry rendering the chart. Used to avoid race conditions with the 
      Highcharts script. Defaults to 5.
    :type retries: :class:`int <python:int>`

    :param interval: The number of milliseconds to wait between retrying rendering the chart. Defaults to 1000 (1
      second).
    :type interval: :class:`int <python:int>`

    :raises HighchartsDependencyError: if
      `ipython <https://ipython.readthedocs.io/en/stable/>`__ is not available in the
      runtime environment
