########################################################
Using Highcharts Core for Python with Pandas
########################################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

The **Highcharts for Python Toolkit** is a data *visualizaiton* library.
That means that it is designed to let you visualize the data that you
or your users are analyzing, rather than to do the analysis itself. But
while there are better tools to actually crunch the numbers, 
**Highcharts for Python** still has to work closely with your data in
order to visualize it.

When working with **Highcharts for Python**, it can be useful to
understand:

  #. How **Highcharts for Python** represents your data
  #. How to load your data into a **Highcharts for Python** object
  #. How to adjust your data in **Highcharts for Python**
  #. How **Highcharts for Python** serializes your data for 
     Highcharts (JS). 

-------------------

*************************************
Highcharts for Python Data Model
*************************************

In broad brushstrokes, you can think of your **Highcharts for Python**
chart as a tree. 

.. list-table::
  :widths: 30 70

  * - .. image:: /_static/highcharts-chart-anatomy.png
        :width: 100%
        :alt: Diagram of chart structure: Chart > Options > Series Collection > Series > Data Collection > Data Point

At the root of the tree is a 
:class:`Chart <highcharts_core.chart.Chart>`, and that chart contains 
options (:class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`). 
Those options in turn contain a collection of :term:`series`,
each of which can be thought of as one "line" of data in your visualization.

Each series instance (descended from 
:class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`)
contains a :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>`
property, which contains a set of :term:`data points <data point>`.

Depending on your data and your configuration, this set of data points may 
be represented as:

  * a :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
    instance (or a descendent of it) which in turn contains your data values and related
    configuration options
  * an iterable of 
    :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`-descended instances,
    each of which contains the data value and configuration of an invidual :term:`data point`

This model is relatively straightforward, but there is one important complexity: the 
relationship between 
:class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
instances and :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` instances.

:class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>` vs :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`
=======================================================================================================================================================================================

The :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>` 
class stores your individual data points in a combination of three different list-like structures:

  * as a :class:`numpy.ndarray <numpy:numpy.ndarray>` in the 
    :meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollections.ndarray>` property
  * as a :class:`list <python:list>` of 
    :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` instances in the 
    :meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollections.data_points>`
    property
  * as a :class:`list <python:list>` of primitives (e.g. numbers, strings, etc.) in the 
    :meth:`.array <highcharts_core.options.series.data.collections.DataPointCollections.array>`
    property

Why split it up like this? The purpose is to maximize performance within both
**Highcharts for Python** and Highcharts (JS), while still minimizing outside dependencies.

Highcharts (JS) supports data organized in primitive arrays. So it can easily visualize something
like the following:

  .. code-block:: python

    [
        [0, 12],
        [1, 34],
        [2, 56],
        [3, 78],
        [4, 90]
    ]

This way of representing your data gives you the fastest performance in Highcharts (JS),
leading to lightening-fast rendering of your chart. And since it's just a simple list of
numbers, **Highcharts for Python** doesn't have to apply any fancy logic to serialize it to
:term:`JS literal notation <JavaScript Object Literal Notation>` - leading to fast 
performance in Python as well.

This is why the 
:class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
separates the data that can be represented as a primitive array (stored in either 
:meth:`.ndarray <highcharts_core.options.series.data.collections.DataPointCollections.ndarray>` or
:meth:`.array <highcharts_core.options.series.data.collections.DataPointCollections.array>`), from 
data point properties that need to be represented as a full Highcharts (JS) data point object
(stored in 
:meth:`.data_points <highcharts_core.options.series.data.collections.DataPointCollections.data_points>`).

And if you're familiar with `NumPy <https://www.numpy.org>`__, that looks *just* like
a :class:`ndarray <numpy:numpy.ndarray>` - and for good reason! If you have 
`NumPy <https://www.numpy.org>` installed, **Highcharts for Python** will leave your 
:class:`ndarray <numpy:numpy.ndarray>` objects as-is to benefit from its vectorization 
and performance.

Internally, 
:class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
instances will intelligently combine the information stored in these three different properties
to serialize your data points. This is done as-appropriately, generating a list of renderable
data points represented either as a primitive array, or as full objects, depending on the
properties that have been configured.

So do you have to worry to about this complexity? Not really! All of this happens under the
hood in the **Highcharts for Python** code. You can simply load your data using the
convenience methods available on your series instances
:class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>` 
or its descendents, or simply pass your data to the series 
:class:`.data <highcharts_core.options.series.base.SeriesBase.data>` property.

Let's see how this works in practice.

------------------------

*****************************************
Loading Data into Highcharts for Python
*****************************************

Preparing Your Data
===========================

So let's try a real-world example. Let's say you've got some annual population
counts stored in a CSV file named ``'census-time-series.csv'``. There are four
different ways you can represent this data:

  #. As-is in the CSV file. Meaning you don't do anything, just leave it
     in the file as-is.
  #. Loaded into a Python iterable (i.e. a :class:`list <python:list>` of
     :class:`list <python:list>`, where each inner list represents a row from
     the CSV). This might look something like this:

       .. code-block:: python

        raw_data = [
            ['United States', 309321666, 311556874, 313830990, 315993715, 318301008, 320635163, 322941311, 324985539, 326687501, 328239523],
            ['Northeast',  55380134, 55604223, 55775216, 55901806, 56006011, 56034684, 56042330, 56059240, 56046620, 55982803],
            ['Midwest', 66974416, 67157800, 67336743, 67560379, 67745167, 67860583, 67987540, 68126781, 68236628, 68329004],
            ...
        ]

  #. As a :class:`numpy.ndarray <numpy:numpy.ndarray>`, which might look like this:

      .. list-table::
        :widths: 30 70

          - .. image:: /_static/tutorials/raw-data-as-numpy.png
              :width: 100%
              :alt: Rendering of the numpy.ndarray produced by np.genfromtext('census-time-series.csv', delimiter = ',', names = True)

  #. As a :class:`pandas.DataFrame <pandas:pandas.DataFrame>`, which might look like this:

      .. list-table::
        :widths: 30 70

        * - .. code-block:: python
      
              raw_data = pandas.read_csv('census-time-series.csv',
                                         index_col = 0,
                                         thousands = ',', 
                                         delimiter = ',')

        * - .. image:: /_static/tutorials/census-time-series-02.png
              :width: 100%
              :alt: Rendering of the Pandas DataFrame loaded from "census-time-series.csv"

Now that we've got our data prepared, let's add it to a series or chart.

Creating a Series/Chart with Data
======================================

.. note::

  In this tutorial, we'll focus on assembling one or more :term:`series` of data, rather than
  a complete chart. This is because chart's have many more configuration options, but 
  fundamentally the data that they contain is stored within one or more series instances,
  which themselves contain data points in a 
  :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>` 
  or an iterable of 
  :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` instances.

So now that we have ``raw_data`` prepared, we can now load it into a series. There are four ways to do 
this:

  #. By passing it to the :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
     of our series when instantiating the series:

     .. code-block:: python

      from highcharts_core.options.series.area import LineSeries

      my_series = LineSeries(data = raw_data)

  #. By calling one of the "helper" methods:

    .. code-block:: python

      from highcharts_core.options.series.area import LineSeries

      # If my data is either a numpy.ndarray or Python iterable
      my_series = LineSeries.from_array(raw_data)

      # If my data is in a Pandas DataFrame
      my_series = LineSeries.from_pandas(raw_data)

      # If my data is in a CSV file
      my_series = LineSeries.from_csv('census-time-series.csv')

    .. seealso::

      Depending on the arguments you supply to the helper methods, they
      may produce *multiple* series for inclusion on your chart. For more
      information, please see:

        * :doc:`Using Highcharts for Python with Pandas <pandas>`
        * :doc:`Using Highcharts for Python with CSVs <csv>`

  #. By instantiating your *set* of data directly, and passing it to the
     :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
     of our series:

       .. code-block:: python

         from highcharts_core.options.series.area import LineSeries
         from highcharts_core.options.series.data.cartesian import CartesianData

         my_data = CartesianData.from_array(raw_data)

         my_series = LineSeries(data = my_data)

       .. seealso::

       Depending on the arguments you supply to the helper methods, they
       may produce *multiple* series for inclusion on your chart. For more
       information, please see:

         * :doc:`Using Highcharts for Python with Pandas <pandas>`
         * :doc:`Using Highcharts for Python with CSVs <csv>`

    #. By instantiating *individual* data points directly, and passing it to
       the :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property
       of our series:

       .. code-block:: python

         from highcharts_core.options.series.area import LineSeries
         from highcharts_core.options.series.data.cartesian import CartesianData

         my_data = [CartesianData(x = record[0], y = record[1] for record in raw_data]

         my_series = LineSeries(data = my_data)


In all cases, the result is the same: a 
:class:`LineSeries <highcharts_core.options.series.area.LineSeries>` instance (or a 
:class:`list <python:list>` of 
:class:`LineSeries <highcharts_core.options.series.area.LineSeries>` that contain your data.

Now that your data has been loaded into your series, you can configure it as needed. 

Configuring Your Data
=========================================

In most cases, you shouldn't have to worry about the internals of how **Highcharts for Python**
stores your data. Depending on whether you supplied a primitive array, a 
:class:`numpy.ndarray <numpy:numpy.ndarray>`, or data from a Pandas 
:class:`DataFrame <pandas:pandas.DataFrame>`, your series' data will either be represented as
a :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
or as a :class:`list <python:list>` of data point objects (descended from 
:class:`DataBase <highcharts_core.options.series.data.base.DataBase>`).

In all cases, you can easily set properties on your data via your series object itself. For
example, let's say we wanted to configure the 
:meth:`.target <highcharts_core.options.series.bullet.BulletSeries>` values on data points
in a :class:`BulletSeries <highcharts_core.options.series.bullet.BulletSeries>` instance. We
can do that easily by working at the *series* level:

  .. code-block:: python

    # EXAMPLE 1.
    # Supplying one value per data point.

    my_series.target = [1, 2, 3, 4, 5, 6]

    # EXAMPLE 2.
    # Supplying one value, which will be applied to ALL data points.

    my_series.target = 2

This propagation of data point properties extends to *all* data point properties. If a
property of the same name exists on the series, it will be set on the *series*. But if
it only exists on the data point, it will be propagated to the relevant data points.

In some circumstances, you may want to set data point properties that have identically-named
properties on the series. For example, data points and series both support the ``.id`` property.
But you can set this property at the data point level in two ways:

  #. If your data point is represented as a 
     :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`,
     you can simply set it as a sub-property of the series 
     :meth:`.data <highcharts_core.options.series.base.SeriesBase.data>` property:

     .. code-block:: python

       # EXAMPLE 1.
       # Supplying one value per data point.
       my_series.data.id = ['id1', 'id2', 'id3', 'id4', 'id5', 'id6']

       # EXAMPLE 2.
       # Supplying one value, which will be applied to ALL data points.

       my_series.data.id = 'id2'

    The :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
    will worry about proagating the relevant property / value to the individual data points as needed.

  #. If you data points are represented as a :class:`list <python:list>` of 
     :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`-descended objects, then you can
     adjust them the same way you would adjust any member of a list:

     .. code-block::
    
       id_list = ['id1', 'id2', 'id3', 'id4', 'id5', 'id6']
       for index in range(len(series.data)):
           series.data[index].id = id_list[index]

    In this case, you are adjusting the data points directly, so you do need to make sure you are 
    adjusting the exact properties you need to adjust in the exact right location.

Updating Your Data
========================

You can also update your data after it has been loaded into your series. This is done by calling one
of the ``.load_from_*`` series helper methods, which makes it possible to update your series' data
just like when creating the series:

  .. code-block:: python

    # EXAMPLE 1.
    # Updating the .data property

    my_series.data = updated_data

    # EXAMPLE 2.
    # If my data is either a numpy.ndarray or Python iterable

    my_series.load_from_array(updated_data)

    # EXAMPLE 3.
    # If my data is in a Pandas DataFrame

    my_series.load_from_pandas(updated_data)

    # EXAMPLE 4.
    # If my data is in a CSV file

    my_series.load_from_csv('updated-data.csv')

---------------------------

***************************************
Serializing Your Data for Rendering
***************************************

While you shouldn't have to serialize your data directly using **Highcharts for Python**, it
may be useful to understand how this process works.

First, it's important to understand that Highcharts (JS) supports data represented in two different
forms:

  * as :term:`JavaScript literal objects <JavaScript Object Literal Notation>`, and
  * as primitive arrays, which are basically collections of strings and numbers

JS literal objects are the most flexible, because they allow you to take advantage of all of the
different data point configuration options supported by Highcharts. However, primitive arrays
perform much faster: Highcharts for Python generates them faster, there's less data to transfer on the wire, and Highcharts (JS) can render them faster.

For this reason, **Highcharts for Python** will always try to serialize your data points to a 
primitive array first. If the series type supports a primitive array, and there is no information configured
on the data points that prevents it from being serialized as a primitive array, Highcharts for Python
will default to that form of serialization.

However, if there are special properties (not supported by primitive arrays) set on the data points, or if
the series type is one that does not support primitive arrays, then Highcharts for Python will generate
a JavaScript literal object instead.

This logic all happens automatically whenever you call 
:class:`.to_js_literal() <highcharts_core.options.series.base.SeriesBase.to_js_literal>` on your series.
