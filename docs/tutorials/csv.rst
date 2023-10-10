########################################################
Using Highcharts Core for Python with CSVs
########################################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

CSV (Comma-Separated Value) is one of the most common formats for exchanging
data files - both large and small. Because of its popularity, the 
**Highcharts for Python Toolkit** is designed to work seamlessly with it.

.. sidebar:: What Can Highcharts for Python do with CSVs?

  The **Highcharts for Python Toolkit** is a *visualization* library. It is
  not used to perform *arithmetical*, *algebraic*, *statistical*, or *matrix* 
  calculations. It is exclusively concerned with visualizing data - and that
  data is typically the product of calculations that are performed up-stream.

  So given that focus, **Highcharts for Python** is designed to *read* data
  that is contained in CSV files and load the data they contain into
  appropriate **Highcharts for Python** classes, which can then be rendered
  using Highcharts (JS).

*********************************
General Approach
*********************************

The **Highcharts for Python Toolkit** provides a number of standard methods
that are used to interact with CSV files. These methods generally take the form:

  * ``.from_csv(as_string_or_file)`` This is always a class method which produces one or more
    instances, with data pulled from the CSV content found in ``as_string_or_file``.
  * ``.from_csv_in_rows(as_string_or_file)`` This is always a class method which produces one
    instance for every *row* in the CSV (``as_string_or_file``).
  * ``.load_from_csv(as_string_or_file)`` This is an instance method which updates an instance
    with data read from the ``as_string_or_file`` argument.

.. tip::

  All three of these standard methods are packaged to have batteries included.
  This means that for simple use cases, you can simply pass a 
  CSV to the method, and the method wlil attempt to determine the best way to 
  deserialize the CSV into the appropriate  **Highcharts for Python** objects.

  However, if you find that you need more fine-grained control, the methods
  provide powerful tools to give you the control you need when you need it.

These standard methods - with near-identical syntax - are available:

  * On all :term:`series` classes (descended from 
    :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`)
  * On the :class:`Chart <highcharts_core.chart.Chart>` class

-------------------------------

*****************************
Preparing Your CSV Data
*****************************

So let's try a real-world example. Let's say you've got some annual population
counts stored in a CSV file named ``'census-time-series.csv'`` that looks like this:

  .. image:: /_static/tutorials/census-time-series-csv-01.png
     :width: 100%
     :alt: Rendering of the data contained in 'census-time-series.csv'

The first column contains the names of geographic regions, while each of the subsequent
columns contains the population counts for a given year. Now, let's say we wanted
to visualize this data in various ways.

------------------------------

*********************************************
Creating the Chart: ``Chart.from_csv()``
*********************************************

Relying on the Defaults
===========================

The simplest way to create a chart from a CSV file is to call 
:class:`Chart.from_csv() <highcharts_core.chart.Chart.from_csv>` like
so:

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            wrapper_character = '"')
  my_chart.display()

.. image:: /_static/tutorials/census-time-series-03.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv')

As you can see, we haven't provided any more instructions besides telling it to
generate a chart from the file ``'census-time-series.csv'``, and to interpret a single 
quotation mark as a wrapper character. The result is a line chart, with one series for 
each year, and one point for each region. 

  .. tip::

    Unless instructed otherwise, **Highcharts for Python** will default to using a
    line chart. 

Setting the Series Type
==============================

Why don't we switch it to a bar chart?

.. code-block:: python
        
  my_chart = Chart.from_csv('census-time-series.csv', 
                            series_type = 'bar',
                            wrapper_character = '"')

.. image:: /_static/tutorials/census-time-series-04.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv', series_type = 'bar')

Now the result is a little more readable, but still not great: After all, there are more than
fifty geographic regions represented for each year, which makes the chart super crowded. 
Besides, maybe we're only interested in a specific year: 2019. 

Let's try focusing our chart.

Basic Property Mapping
==========================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'bar',
                            property_column_map = {
                                'x': 'Geographic Area',
                                'y': '2019'
                            })

.. image:: /_static/tutorials/census-time-series-05.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv', series_type = 'bar', property_column_map = {'x': 'Geographic Area', 'y': '2019'})

Much better! We've now added a ``property_column_map`` argument to the ``.from_csv()`` method call. 
This argument tells Highcharts for Python how to map columns in your data to properties in the 
resulting chart. In this case, the keys ``'x'`` and ``'y'`` tell **Highcharts for Python** that you want to map the ``'Geographic Area'`` column to the resulting series' data points' 
:meth:`.x <highcharts_core.options.series.data.bar.BarData.x>`,
and to map the ``'2019'`` column to the :meth:`.y <highcharts_core.options.series.data.bar.BarData.y>` 
properties, respectively.

The net result is that ``my_chart`` contains one 
:class:`BarSeries <highcharts_core.options.series.bar.BarSeries>` whose 
:meth:`.data <highcharts_core.options.series.bar.BarSeries.data>` property contains a 
:class:`BarDataCollection <highcharts_core.options.series.data.bar.BarDataCollection>` instance populated
with the data from the ``'Geographic Area'`` and ``'2019'`` columns in ``census-time-series.csv``.

But maybe we actually want to compare a couple different years? Let's try that.

  .. tip::

    Not all CSV data contains a header row. If your CSV data does not contain a header row,
    ``property_column_map`` accepts :class:`int <python:int>` values, which indicate the
    index of the column that you want to map. So the method call above would be equivalent to:

      .. code-block:: python

        my_chart = Chart.from_csv('census-time-series.csv',
                                  series_type = 'bar',
                                  property_column_map = {
                                      'x': 0,
                                      'y': 10
                                  })

Property Mapping with Multiple Series
========================================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'column',
                            property_column_map = {
                                'x': 'Geographic Area',
                                'y': ['2017', '2018', '2019']
                            })

.. image:: /_static/tutorials/census-time-series-06.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv', series_type = 'bar', property_column_map = {'x': 'Geographic Area', 'y': ['2017', '2018', '2019']})

Now we're getting somewhere! We've added a list of column names to the ``'y'`` key in the ``property_column_map`` 
argument. Each of those columns has now produced a *separate* 
:class:`BarSeries <highcharts_core.options.series.bar.BarSeries>` instance - but they're 
all still sharing the ``'Geographic Area'`` column as their 
:meth:`.x <highcharts_core.options.series.data.bar.BarData.x>` value.

  .. note::

    You can supply multiple values to any property in the ``property_column_map``. The example
    provided above is equivalent to:

      .. code-block:: python

        my_chart = Chart.from_csv('census-time-series.csv',
                                     series_type = 'column',
                                     property_column_map = {
                                         'x': ['Geographic Area', 'Geographic Area', 'Geographic Area'],
                                         'y': ['2017', '2018', '2019']
                                     })

    The only catch is that the ultimate number of values for each key must match. If there's
    only one value, then it will get repeated for all of the others. But if there's a mismatch,
    then **Highcharts for Python** will throw a 
    :exc:`HighchartsCSVDeserializationError <highcharts_core.errors.HighchartsCSVDeserializationError>`.

But so far, we've only been using the ``'x'`` and ``'y'`` keys in our ``property_column_map``. What if we wanted to
configure additional properties? Easy!

Configuring Additional Properties
=====================================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'bar',
                            property_column_map = {
                                'x': 'Geographic Area',
                                'y': ['2017', '2018', '2019'],
                                'id': 'some other column'
                            })

Now, our CSV is pretty simple does not contain a column named ``'some other column'`. But *if* it did,
then it would use that column to set the :meth:`.id <highcharts_core.options.series.data.bar.BarData.id>` property of each data point.

  .. note::

    You can supply any property you want to the ``property_map``. If the property is not
    supported by the series type you've selected, then it will be ignored.

But our chart is still looking a little basic - why don't we tweak some series configuration options?

Configuring Series Options
===============================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'bar',
                            property_column_map = {
                                'x': 'Geographic Area',
                                'y': ['2017', '2018', '2019'],
                            },
                            series_kwargs = {
                                'point_padding': 5
                            })

.. image:: /_static/tutorials/census-time-series-07.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv', series_type = 'bar', property_column_map = {'x': 'Geographic Area', 'y': ['2017', '2018', '2019'], 'id': 'Geographic Area'}, series_kwargs = {'point_padding': 0.25})

As you can see, we supplied a new ``series_kwargs`` argument to the ``.from_csv()`` method call. This
argument receives a :class:`dict <python:dict>` with keys that correspond to properties on the series. In
this case, by supplying ``'point_padding'`` we have set the resulting 
:meth:`BarSeries.point_padding <highcharts_core.options.series.bar.BarSeries.point_padding>` property to a
value of ``0.25`` - leading to a bit more spacing between the bars.

But our chart is *still* a little basic - why don't we give it a reasonable title?

Configuring Options
=============================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'bar',
                            wrapper_character = '"',
                            property_column_map = {
                                'x': 'Geographic Area',
                                'y': ['2017', '2018', '2019']
                            },
                            series_kwargs = {
                                'point_padding': 5
                            },
                            options_kwargs = {
                                'title': {
                                  'text': 'This Is My Chart Title'
                                }
                            })

.. image:: /_static/tutorials/census-time-series-08.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv', series_type = 'bar', property_column_map = {'x': 'Geographic Area', 'y': ['2017', '2018', '2019'], 'id': 'Geographic Area'}, series_kwargs = {'point_padding': 0.25}, options_kwargs = {'title': {'text': 'This Is My Chart Title'}})

As you can see, we've now given our chart a title. We did this by adding a new ``options_kwargs`` argument,
which likewise takes a :class:`dict <python:dict>` with keys that correspond to properties on the chart's
:class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` configuration.`

Now let's say we wanted our chart to render in an HTML ``<div>`` with an ``id`` of ``'my_target_div`` - 
we can configure that in the same method call.

Configuring Chart Settings
==============================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'bar',
                            wrapper_character = '"',
                            property_column_map = {
                                'x': 'Geographic Area',
                                'y': ['2017', '2018', '2019'],
                            },
                            series_kwargs = {
                                'point_padding': 0.25
                            },
                            options_kwargs = {
                                'title': {
                                  'text': 'This Is My Chart Title'
                                }
                            },
                            chart_kwargs = {
                                'container': 'my_target_div'
                            })

While you can't really *see* the difference here, by adding the ``chart_kwargs`` argument to
the method call, we now set the :meth:`.container <highcharts_core.chart.Chart.container>` property
on ``my_chart``.

But maybe we want to do something a little different - like compare the change in population over time.
Well, we can do that easily by visualizing each *row* of ``census-time-series.csv`` rather than each *column*.`

Visualizing Data in Rows
==============================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'line',
                            series_in_rows = True,
                            wrapper_character = '"')

.. image:: /_static/tutorials/census-time-series-09.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv', series_type = 'line', series_in_rows = True)

Okay, so here we removed some of the other arguments we'd been using to simplify the example. You'll see we've now
added the ``series_in_rows`` argument, and set it to ``True``. This tells **Highcharts for Python** that we expect
to produce one series for every *row* in ``census-time-series.csv``. 

Because we have not specified a ``property_column_map``, the series 
:meth:`.name <highcharts_core.options.series.bar.BarSeries.name>` values are populated from the ``'Geographic Area'``
column, while the data point :meth:`.x <highcharts_core.options.series.data.bar.BarData.y>` values come from each additional column (e.g. ``'2010'``, ``'2011'``, ``'2012'``, etc.)

  .. tip::

    To simplify the code further, any class that supports the ``.from_csv()`` method also
    supports the ``.from_csv_in_rows()`` method. The latter method is equivalent to passing
    ``series_in_rows = True`` to ``.from_csv()``.

    For more information, please see:

      * :class:`Chart.from_csv_in_rows() <highcharts_core.chart.Chart.from_csv_in_rows>`
      * :class:`SeriesBase.from_csv_in_rows() <highcharts_core.options.series.base.SeriesBase.from_csv_in_rows>`

But maybe we don't want *all* geographic areas shown on the chart - maybe we only want to compare a few.

Filtering Rows
=======================

.. code-block:: python

  my_chart = Chart.from_csv('census-time-series.csv',
                            series_type = 'line',
                            series_in_rows = True,
                            wrapper_character = '"',
                            series_index = slice(7, 10))

.. image:: /_static/tutorials/census-time-series-10.png
  :width: 100%
  :alt: Rendering of the chart produced by Chart.from_csv('census-time-series.csv', series_type = 'line', series_in_rows = True, series_index = slice(7, 10))

What we did here is we added a ``series_index`` argument, which tells **Highcharts for Python** to only
include the series found at that index in the resulting chart. In this case, we supplied a :func:`slice <python:slice>`
object, which operates just like ``list_of_series[7:10]``. The result only returns those series between index 7 and 10.

------------------------

**********************************************************************
Creating Series: ``.from_csv()`` and ``.from_csv_in_rows()``
**********************************************************************

All **Highcharts for Python** :term:`series` descend from the 
:class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>` class. And they all
therefore support the ``.from_csv()`` class method. 

When called on a series class, it produces one or more series from the CSV supplied. 
The method supports all of the same options
as :class:`Chart.from_csv() <highcharts_core.chart.Chart.from_csv>` *except for* ``options_kwargs`` and
``chart_kwargs``. This is because the ``.from_csv()`` method on a series class is only responsible for
creating series instances - not the chart itself.

Creating Series from Columns
==================================

So let's say we wanted to create one series for each of the years in ``census-time-series.csv``. 
We could do that like so:

  .. code-block:: python

    my_series = BarSeries.from_csv('census-time-series.csv')

Unlike when calling :meth:`Chart.from_csv() <highcharts_core.chart.Chart.from_csv>`, we
did not have to specify a ``series_type`` - that's because the ``.from_csv()`` class method on a
series class already knows the series type.

In this case, ``my_series`` now contains ten separate :class:`BarSeries <highcharts_core.options.series.bar.BarSeries>`
instances, each corresponding to one of the year columns in ``census-time-series.csv``.

But maybe we wanted to create our series from rows instead?

Creating Series from Rows
=================================

.. code-block:: python

  my_series = LineSeries.from_csv_in_rows('census-time-series.csv')

This will produce one :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`
instance for each row in ``census-time-series.csv``, ultimately producing a 
:class:`list <python:list>` of 57 
:class:`LineSeries <highcharts_core.options.series.area.LineSeries>` instances.

Now what if we don't need all 57, but instead only want the first five?

Filtering Series Created from Rows
======================================

.. code-block:: python

  my_series = LineSeries.from_csv_in_rows('census-time-series.csv', series_index = slice(0, 5))

This will return the first five series in the list of 57.
--------------------------

***********************************************************
Updating an Existing Series: ``.load_from_csv()``
***********************************************************

So far, we've only been creating new series and charts. But what if we want to update
the data within an existing series? That's easy to do using the 
:meth:`.load_from_csv() <highcharts_core.options.series.base.SeriesBase.load_from_csv>` method.

Let's say we take the first series returned in ``my_series`` up above, and we want to replace
its data with the data from the *10th* series. We can do that by:

  .. code-block:: python

    my_series[0].load_from_csv('census-time-series.csv', 
                               series_in_rows = True,
                               series_index = 9)

The ``series_in_rows`` argument tells the method to generate series per row, and then
the ``series_index`` argument tells it to only use the 10th series generated.

  .. caution::

    While the :meth:`.load_from_csv() <highcharts_core.options.series.base.SeriesBase.load_from_csv>`
    method supports the same arguments as 
    :meth:`.from_csv() <highcharts_core.options.series.base.SeriesBase.from_csv>`, it expects that
    the arguments supplied lead to an unambiguous *single* series. If they are ambiguous - meaning they
    lead to multiple series generated from the CSV - then the method will throw a 
    :exc:`HighchartsCSVDeserializationError <highcharts_core.errors.HighchartsCSVDeserializationError>`