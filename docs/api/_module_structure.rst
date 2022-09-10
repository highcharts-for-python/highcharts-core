
The structure of the **Highcharts for Python** library closely matches the structure
of the `Highcharts JS`_ options object (see the relevant
`reference documentation <https://api.highcharts.com/highcharts/>`_).

At the root of the library - importable from ``highcharts_python`` you will find the
``highcharts`` module. This module is a catch-all importable module, which allows you to
easily access all of the Highcharts for Python classes defined.

.. note::

  Whlie you can access all of the **Highcharts for Python** classes from
  ``highcharts_python.highcharts``, if you want to more precisely navigate to specific
  class definitions you can do fairly easily using the folder organization and naming
  conventions used in the library.

  In the root of the ``highcharts_python`` library you can find universally-shared
  class definitions, like ``metaclasses`` which contains the :class:`HighchartsMeta`
  definition and the :class:`JavaScriptDict` definition or ``decorators`` which define
  method/property decorators that are used throughout the library.

  The ``utility_classes`` folder contains class definitions for classes that are
  referenced or used throughout the other class definitions.

  And you can find the Highcharts JS options object and all of its
  properties defined in the ``options`` folder, with specific (complicated or extensive)
  sub-folders providing property-specific classes (e.g. the ``options/plot_options``
  folder defines all of the different configuration options for different series types,
  while the ``options/series`` folder defines all of the classes that represent
  :term:`series` of data in a given chart).

.. tip::

  To keep things simple, we recommend importing classes you need directly from the
  ``highcharts_python.highcharts`` module. There are two paths to do so easily:

  .. code-block:: python

    # APPROACH #1: Import the highcharts module, and access its child classes directly.
    #              for example by now calling highcharts.Chart().
    from highcharts_python import highcharts

    my_chart = highcharts.Chart()
    my_shared_options = highcharts.SharedOptions()

    my_line_series = highcharts.options.series.area.LineSeries()

    # APPROACH #2: Import a specific class or module by name from the "highcharts" module.
    from highcharts_python.highcharts import Chart, SharedOptions, options

    my_chart = Chart()
    my_shared_options = SharedOptions()
    my_line_series = options.series.area.LineSeries()
