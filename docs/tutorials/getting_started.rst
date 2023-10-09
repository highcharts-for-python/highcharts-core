##############################################
Highcharts Core for Python: Getting Started
##############################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

We're so glad you want to use **Highcharts Core for Python**! This tutorial will help
you get started, and give you a jumping off point to dive into all the great features
of the Highcharts visualization suite. Before you really get going, we suggest you take
a look at all of the great :doc:`visualization types <../visualizations>` you can create
using **Highcharts for Python** and `Highcharts (JS) <https://www.highcharts.com>`__.

***************************
Installation
***************************

First things first, to use **Highcharts for Python** the first step is to install the
library (likely to a virtual environment). That's pretty straightforward:

.. include:: ../_installation.rst

-------------------

******************************************
Importing Highcharts Core for Python
******************************************

Once you've installed **Highcharts Core for Python**, you can import it into your project
in two different ways:

.. include:: ../using/_importing.rst

-------------------

******************************************
Wrangle Your Data
******************************************

Since you want to use **Highcharts Core for Python** to visualize some data, first
you're going to have to wrangle the data into a form you can work with. How you do
this really depends on the data you are working with and the other tools you are
using in your tech stack.

The **Highcharts for Python** toolkit works with most of the "usual suspects" in the
Python ecosystem, including:

  * `Pandas <https://pandas.pydata.org/>`__
  * `Numpy <https://www.numpy.org/>`__
  * `PySpark <https://spark.apache.org/docs/latest/api/python/index.html>`__
  * CSV files
  * JSON files
  * Python :class:`dict <python:dict>` instances
  * Python iterables (e.g. :class:`list <python:list>`, :class:`tuple <python:tuple>`, etc.)

For the sake of simplicity, we'll work with Python iterables to show how you
can quickly get started. Let's say we have a simple 2-dimensional set of x/y values 
that we want to plot:

  .. code-block:: python

    my_iterable = [
        [0, 123],
        [1, 456],
        [2, 789],
        [3, 987],
        [4, 654],
        [5, 321]
    ]

That's all I need to wrangle my data! **Highcharts for Python** can work with 
``my_iterable`` directly and easily, wherever data is referenced.

.. tip::

  Different Highcharts :term:`series` types support different structures of
  iterable.

  Please review the detailed :ref:`series documentation <series_documentation>` for
  series type-specific details of relevant iterable/array structures.

Alternatively, we can convert ``my_iterable`` into a 
:class:`pandas.DataFrame <pandas:pandas.DataFrame>`, :class:`numpy.ndarray <numpy:numpy.ndarray>`,
or Python :class:`dict <python:dict>`:

  .. code-block:: python

    # As a Pandas DataFrame
    df = pandas.DataFrame(my_iterable, columns=['x', 'y'])

    # As a Numpy ndarray
    as_ndarray = numpy.as_ndarray(my_iterable)

    # As a Python dict
    as_dict = {'x': x[0], 'y': x[1] for x in my_iterable}

Now, we can consider our data "wrangled" and ready for visualization.

--------------------

******************************************
Assembling a Chart
******************************************

With our data wrangled, we can construct a chart with one line of code:

.. include:: _assembling_a_chart.rst

**********************************
Configuring the Chart
**********************************

`Highcharts (JS) <https://www.highcharts.com>`__ sets the standard for
data visualization because it supports a huge number of easy-to-understand
configuration options. **Highcharts for Python** makes it easy to configure
any of those options directly within Python.

To do that, we can use the :meth:`Chart.options <highcharts_core.chart.Chart.options>`
property. Having assembled our chart following the instructions above, ``my_chart``
already contains a :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
instance in the :meth:`Chart.options <highcharts_core.chart.Chart.options>` property.
You can access the :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`
we created at :meth:`Chart.options.series <highcharts_core.options.HighchartsOptions.series>`,
and you can set any other options you need on 
:meth:`Chart.options <highcharts_core.chart.Chart.options>`.

For example, let's say we want to set the chart's title to "My First Chart". To do that,
we can configure the 
:meth:`Chart.options.title <highcharts_core.options.HighchartsOptions.title>` property
using either a :class:`Title <highcharts_core.options.title.Title>` instance, or a
:class:`dict <python:dict>`:

  .. code-block:: python

    # as a Title instance

    from highcharts_core.options.title import Title

    my_chart.options.title = Title(text = 'My First Chart')

    # as a dict

    my_chart.options.title = {'text': 'My First Chart'}

Either way, the chart's title will now be set to "My First Chart".

  .. seealso::

    * :doc:`Templating and Shared Options <templating>`
    * :doc:`Creating JavaScript Callback Functions <callbacks>`

----------------

******************************************
Rendering the Chart
******************************************

Once we've assembled and configured our chart, we can render it. How we want
to render it depends on our exact needs. We can:

  * Display the chart in a `Jupyter Notebook <https://www.jupyter.org>`__
  * Save the chart as a static image
  * Generate the JavaScript that will render the chart in your users'
    web browser.

Displaying in Jupyter Notebook / Jupyter Lab
===============================================

If you're using **Highcharts Core for Python** in a Jupyter Notebook or Jupyter Lab,
you can display the chart right in your notebook. Doing so is super simple - just
call the :meth:`.display() <highcharts_core.chart.Chart.display>` method on 
``my_chart``:

  .. code-block:: python

    my_chart.display()

That's it! The chart will now render in the output of the cell.

  .. seealso::

    * :doc:`Using Highcharts Core for Python with Jupyter <jupyter>`

Saving the Chart as a Static Image
=======================================

If you want to save the chart as a static image, you can do so by calling the
:meth:`.download_chart() <highcharts_core.chart.Chart.download_chart>` method:

  .. code-block:: python

    my_chart.download_chart(filename = 'my_chart.png')

If you need it in a different format, you can specify the format using the
``format`` parameter. Highcharts for Python supports PNG (the default),
JPEG, PDF, and SVG. For example, to save the chart as a PDF, you can do:

  .. code-block:: python

    my_chart.download_chart(filename = 'my_chart.pdf', format = 'pdf')

And that's it!

  .. seealso::

    * :doc:`Exporting Static Charts <exporting>`

Rendering in the Web Browser
================================

If you want to render your chart in your user's web browser, then you can
use **Highcharts for Python** to automatically generate the JavaScript code
you will need. The best way to do this is to call the 
:meth:`.to_js_literal() <highcharts_core.chart.Chart.to_js_literal>` method
on ``my_chart``.

This will produce a string (or write to a file) containing the 
:term:`JS literal <JavaScript Object Literal Notation>` form of your chart and
its configuration. If the code contained in this string gets executed in your
user's browser (within a set of ``<script></script>`` tags), it will render
your chart.

So the way to get the JS literal is very straightforward:

  .. code-block:: python

    # EXAMPLE 1. 
    # Storing the JS literal in a string.

    my_js_literal = my_chart.to_js_literal()

    # EXAMPLE 2.
    # Saving the JS literal to a file named
    # "my-js-literal.js"

    my_chart.to_js_literal('my-js-literal.js')

Now the way to render this chart will ultimately depend on how your application
is architected. We see three - typical - patterns employed:

  #. If your Python code is responsible for preparing the client-side 
     HTML + JavaScript, then you can include ``my_js_literal`` in your
     template file. This pattern works for practically every Python web
     framework, including `Django <https://www.djangoproject.com>`__,
     and `Flask <https://flask.palletsprojects.com/en/3.0.x/>`__.
  #. If your Python code exposes RESTful or GraphQL APIs that are 
     consumed by your client-side application, then you can return the JS
     literal object as a string via your API. This can then be evaluated
     in your client-side application using JavaScript's ``new Function()``
     feature.

       .. caution::

         **DO NOT USE JAVASCRIPT'S eval() FUNCTION**.
         
         It is deprecated, and for good reason:
         
         It represents a major security risk. When using ``new Function()``,
         we recommend balancing the need for simplicity against the need for 
         security. You can secure your code by applying whitelisting techniques,
         sandboxing the scope of your ``new Function()`` context, adding 
         additional layers of M2M signed encryption, or employing sanitization
         techniques on the content of the JS literal returned by your API.

         Which specific techniques make sense will depend on your application 
         and your use case.

  #. If the data in your front-end application is generated on a periodic / batch
     basis, then you can save your JS literal to a static file (saved where 
     consumable by your front-end application) and have your front-end application
     simply load it as-needed.