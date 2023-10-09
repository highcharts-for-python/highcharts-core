###################################################
Working with Series in Highcharts for Python
###################################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

**Highcharts for Python** (and Highcharts (JS), of course) are both built around
the concept of :term:`data series <series>`. A data series can be thought of as
a set of data points that describe the same "thing", and which represent how
the data can be organized. Think: 
  
  * a single line on a line chart
  * a set of columns all the same color on a column chart
  * all of a pie or donut chart

As a result, when you constructing your chart in **Highcharts for Python**,
what you are really doing is constructing one or more :term:`series` that
are then placed on a shared canvas, with shared axes, a shared legend, etc.

  .. image:: /_static/highcharts-chart-anatomy.png
    :width: 75
    :align: right
    :alt: Diagram showing the conceptual components of a Highcharts chart

This tutorial is designed to help you understand how to manage series in your
Highcharts visualizations using **Highcharts for Python**.

----------------------------------

*********************************
How Series are Organized
*********************************

As the diagram above shows, Highcharts visualizations are configured
within a :class:`Chart <highcharts_core.chart.Chart>` object, which has
the :meth:`.options <highcharts_core.chart.Chart.options>` property where
the chart's configuration "lives", represented as a 
:class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
instance.

The :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` 
configuration allows you to define *all* details of what gets displayed on
the chart, how that content behaves, etc. The configuration options available in 
:class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` can be
thought of as chart-level configurations: They configure or define things that apply to
everything shown on the chart: the axes to display, the legend, the title, the settings shared
across all of the series on the chart, etc.

But within the :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
you will find the :meth:`.series <highcharts_core.options.HighchartsOptions.series>`
property. This is where you define the *specific* :term:`series` to render on your chart.

This property gets one or more series instances, all of which are descended from
:class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`. They descend from
this single base series class because many of their properties are shared across all types
of series. For example, whether the series is to render as a line or as a bar, all series will
have an :meth:`.id <highcharts_core.options.series.base.SeriesBase.id>` option.

All visualizations supported by Highcharts have a corresponding series type, which means
they all have their corresponding series class. To see this mapping, take a look at our
:doc:`Supported Visualizations </visualizations>`.

Each series type has its set of shared properties that derive from 
:class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>, but specific series types 
may have their own type-specific settings. For example, a 
:class:`GaugeSeries <highcharts_core.options.series.gauge.GaugeSeries>` will have options to
configure the gauge's dial (:meth:`.dial <highcharts_core.options.series.gauge.GaugeSeries.dial>`),
overshot-handling (:meth:`.overshoot <highcharts_core.options.series.gauge.GaugeSeries.overshoot>`),
and pivot point (:meth:`.pivot <highcharts_core.options.series.gauge.GaugeSeries.pivot>`) - settings
which would be completely *irrelevant* for a 
:class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, which does not have a dial,
does not have a concept of overshooting the bounds of the dial, and does not have any pivot points.

.. list-table::
  :widths: 50 50
  
  * - .. figure:: ../../../_static/gauge-example.png
        :alt: Gauge Example Chart
        :align: center
    - .. figure:: ../../../_static/line-example.png
        :alt: Line Example Chart
        :align: center

And all series (technically, *almost* all) have a 
:meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property, which contains the
data that should be visualized in the series.

.. sidebar:: Exceptions without Data

  Certain types of visualiation - like 
  :class:`BellCurveSeries <highcharts_core.options.series.bellcurve.BellCurveSeries>`
  do not receive their own data, but instead are tied to an underlying 
  :meth:`.base_series <highcharts_core.options.series.bellcurve.BellCurveSeries.base_series>`
  whose data is used to shape their visualization.

    .. figure:: ../../../_static/bellcurve-example.png
      :alt: Bell Curve Example Chart
      :align: center
      :width: 35%

So as you can see, series are pretty fundamental to your Highcharts visualizations: They are
what actually gets visualized.

So how do we start creating series using **Highcharts for Python**?

---------------------------------------

***************************************************
Creating Series in Highcharts for Python
***************************************************


Of course, you can always construct your series using direct instantiation:

  .. code-block:: python

    from highcharts_core.chart import Chart
    from highcharts_core.options import HighchartsOptions
    from highcharts_core.options.series.area import LineSeries

    my_line_series = LineSeries(data = my_data, id = 'my_series_id123')
    my_options = HighchartsOptions(series = [my_line_series])
    my_chart = Chart(options = my_options)

And there may be situations where there is the best way for you to construct your
series, depending on how you are managing your full Highcharts for Python application.

But there are much simpler / faster ways to rapidly create your chart/series:

Assembling a Chart with Series at Once
=========================================

.. include:: _assembling_a_chart.rst

Assembling Series Alone
==========================

You can create series similarly:

  .. code-block:: python

    from highcharts_core.options.series.area import LineSeries

    my_line_series = LineSeries(data = my_iterable)

This will create a :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` 
instance.

Depending on how we've wrangled our data, we can similarly produce one or more
series from a :class:`pandas.DataFrame <pandas:pandas.DataFrame>`, 
:class:`numpy.ndarray <numpy:numpy.ndarray>`, or Python :class:`dict <python:dict>`:

  .. code-block:: python

    # From a Pandas DataFrame

    my_series = LineSeries.from_pandas(df)

    # From a Numpy ndarray

    my_series = LineSeries.from_array(data = as_ndarray)

    # From a CSV file

    my_series = LineSeries.from_csv('my-data.csv')

    # From a Python iterable

    my_series = LineSeries.from_array(data = as_iterable)

All of these lines of code are equivalent, and should produce an identical
``my_series``. Depending on the arguments you supply to the helper methods,
they may either produce *one* series instance or a :class:`list <python:list>`
of series instances.

Adding Series to a Chart
===========================

If you have created series on their own, you can add them to an existing
:class:`Chart <highcharts_core.chart.Chart>` very easily:

  .. code-block:: python

    # EXAMPLE 1.
    # Adding one series

    my_chart.add_series(my_series)

    # EXAMPLE 2.
    # Adding multiple series if they are in one iterable

    my_chart.add_series(my_list_of_series)

    # EXAMPLE 3.
    # Adding multiple individual series
    
    my_chart.add_series(series1, series2, series3)

Or you can also create a new chart *from* a list of series:

  .. code-block:: python

    # EXAMPLE 1.
    # With one series

    my_chart = Chart.from_series(my-series)

    # EXAMPLE 2.
    # With multiple series if they are in one iterable

    my_chart = Chart.from_series(my_list_of_series)

    # EXAMPLE 3.
    # Adding multiple individual series
    
    my_chart = Chart.from_series(series1, series2, series3)

.. tip::

  The same :meth:`.add_series <highcharts_core.chart.Chart.add_series>` and
  :meth:`.from_series <highcharts_core.chart.Chart.from_series>` helper methods
  are also available on the
  :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` class.

So now that we've created a chart and a bunch of series, what else can we do?

----------------------------

*********************************
Configuring Your Series
*********************************

You can configure the options available on each series very simply. Highcharts (JS) -
and so **Highcharts for Python** - have a very extensive API, with lots of configuration
options. 

.. tip::
    
  We recommend reviewing the :doc:`API Reference </api>` to really explore
  the options available for different series types.

Updating Data Points
=========================

However, the most important configuration you will do is to manage the data points
you wish to display in your series. You can do this by:

  #. Passing data directly to the 
     :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>`
     property:

     .. code-block:: python

        my_series.data = updated_data

  #. Using any of the helper methods provided on the series instance:

     .. code-block:: python

       # EXAMPLE 1.
       # Updating data points from a new Pandas DataFrame

       my_series.load_from_pandas(df)

       # EXAMPLE 2.
       # Updating data points from a new numpy.ndarray

       my_series.load_from_array(as_ndarray)

       # EXAMPLE 3.
       # Updating data points from a new iterable.

       my_series.load_from_array(as_iterable)

       # EXAMPLE 4.
       # Updating data points from a CSV file.

       my_series.load_from_csv('my-updated-csv-file.csv')

Updating Data Point Properties
==================================

In addition, all series instances make it easy to propagate information throughout your
underlying data. When you try to set a property on your series object, **Highcharts for Python**
will first see if it is a valid property on the series itself. But if it is not, then it will
check whether it is a supported property on that series' *data*.

So as an example, if we want to give our series an ID, we can simply call:

  .. code-block:: python

    my_series.id = 'my-updated-id-value'

However, if we want to set a :class:`BulletSeries <highcharts_core.options.series.bullet.BulletSeries>` data points' :meth:`.target <highcharts_core.options.series.data.bullet.BulletData>` value, we can simply reference it on the series.
For example, if our :class:`BulletSeries <highcharts_core.options.series.bullet.BulletSeries>` contains three data points, we can set their targets easily using the series:

  .. code-block:: python

    my_bullet_series.target = [1, 2, 3]

By passing an iterable (or a :class:`numpy.ndarray <numpy:numpy.ndarray>`), *all* of your data 
points will get updated with the appropriate value. This makes it very easy to execute your data point 
configurations by operating on the series, rather than working with *individual* data points - though if you want
to work with *individual* data points, you can do so as well.

.. seealso::

  * :doc:`Working with Data in Highcharts for Python <data>`

Converting Series Types
===========================

Every series type has its own type-specific set of configuration options. However, there may be
times when you want to change how your data is to be visualized / rendered. **Highcharts for Python**
provides a useful helper method for that, too. For example, if we want to convert our 
:class:`LineSeries <highcharts_core.options.series.area.LineSeries>` to a 
:class:`BarSeries <highcharts_core.options.series.bar.BarSeries>`, we can do that by calling the
:meth:`.convert_to <highcharts_core.options.series.base.SeriesBase.convert_to>` method:

  .. code-block:: python

    # EXAMPLE 1
    # Indicating the target type with a string label

    my_series.convert_to(series_type = 'bar')

    # EXAMPLE 2
    # Indicating the target type with a SeriesBase class

    my_series.convert_to(series_type = BarSeries)

So now that we've constructed, configured, and adjusted our series, we can also render them
easily.

-----------------------

***************************
Rendering Series
***************************

Series can be rendered within the chart that they are a part of, simply by following
the process to render the chart:

Rendering a Series within a Chart
=======================================

  #. When in Jupyter Notebook/Lab, just execute the :meth:`.display() <highcharts_core.chart.Chart.display>`
     method.

       .. code-block:: python

         my_chart.display()

  #. When rendering within a web application, or saving to a file for rendering in a separate application,
     you can serialize your chart to :term:`JavaScript object literal notation`:

       .. code-block:: python

         as_js_literal = my_chart.to_js_literal()

     which will produce the JavaScript code to render your complete chart.

Rendering a Series Alone
============================

The *exact same* helper methods are available on your series as well. So if you have assembled your
series as ``my_series``, you can take a shortcut to visualize it by calling:

  .. code-block:: python

    my_series.display()

which will assemble a generic :class:`Chart <highcharts_core.chart.Chart>` instance, include
your series, and render it in Jupyter Notebook/Lab. 

You can also produce a :class:`Chart <highcharts_core.chart.Chart>` instance containing your 
series in a single method call as well:

  .. code-block:: python

    my_chart = my_series.to_chart()

And similarly:

  .. code-block::

    series_as_js_literal = my_series.to_js_literal()

will produce the JS literal representation of your series, for use in a JavaScript application.

------------

Given all of this flexibliity, we hope you have a great time assembling 
high-end visualizations and exploring **Highcharts for Python**!