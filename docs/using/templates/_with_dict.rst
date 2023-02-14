If you are hoping to configure a simple set of template settings, one of the fastest
ways to do so in your Python code is to instantiate your
:class:`Chart <highcharts_core.chart.Chart>` instance from a simple
:class:`dict <python:dict>` using the ``.from_dict()`` method.

  .. tip::

    This method is particularly helpful and easy to maintain if you are only using a
    *very* small subset of the `Highcharts JS <https://www.highcharts.com>`__
    configuration options.
