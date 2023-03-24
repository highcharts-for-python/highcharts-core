
The structure of the **Highcharts Core for Python** library closely matches the structure
of the `Highcharts Core <https://api.highcharts.com/highcharts/>`_ options object (see the 
relevant `reference documentation <https://api.highcharts.com/highcharts/>`_).

At the root of the library - importable from ``highcharts_core`` you will find the
:mod:`highcharts_core.highcharts` module. This module is a catch-all importable module,
which allows you to easily access the most-commonly-used Highcharts for Python classes and
modules.

.. note::

  Whlie you can access all of the **Highcharts Core for Python** classes from
  ``highcharts_core.highcharts``, if you want to more precisely navigate to specific
  class definitions you can do fairly easily using the folder organization and naming
  conventions used in the library.

  *This is the recommended best practice to maximize performance*.

  In the root of the ``highcharts_core`` library you can find universally-shared
  class definitions, like :mod:`.metaclasses <highcharts_core.metaclasses>` which
  contains the :class:`HighchartsMeta`  definition and the :class:`JavaScriptDict`
  definition or :mod:`.decorators <highcharts_core.decorators>` which define
  method/property decorators that are used throughout the library.

  The :mod:`.utility_classes <highcharts_core.utility_classes>` folder contains class
  definitions for classes that are referenced or used throughout the other class
  definitions.

  And you can find the Highcharts Core ``options`` object and all of its
  properties defined in the :mod:`.options <highcharts_core.options>` module, with
  specific (complicated or extensive) sub-folders providing property-specific classes
  (e.g. the :mod:`.options.plot_options <highcharts_core.options.plot_options>`
  module defines all of the different configuration options for different series types,
  while the :mod:`.options.series <highcharts_core.options.series>` module defines all
  of the classes that represent :term:`series` of data in a given chart).
