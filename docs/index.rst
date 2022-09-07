.. image:: _static/highcharts-python-logo.png
  :alt: Highcharts for Python - High-end Data Visualization for the Python Ecosystem
  :align: right
  :width: 200
  :height: 100

|

###################################################
Highcharts for Python Toolkit
###################################################

**High-end data visualization for the Python ecosystem**

.. sidebar:: Version Compatibility

  **Highcharts for Python** is designed to be compatible with:

    * Python 3.9 or higher,
    * Highcharts JS 10.2 or higher,
    * Jupyter Notebook 6.4 or higher,
    * Pandas 1.3 or higher
    * PySpark 3.3 or higher

.. include:: _unit_tests_code_coverage.rst

.. toctree::
  :hidden:
  :maxdepth: 3
  :caption: Contents

  Home <self>
  Quickstart: Patterns and Best Practices <quickstart>
  FAQ <faq>
  Toolkit Components and Roadmap <toolkit>
  Using Highcharts for Python <using>
  API Reference <api>
  Error Reference <errors>
  Contributor Guide <contributing>
  Testing Reference <testing>
  Release History <history>
  Glossary <glossary>
  Licensing <license>

The **Highcharts for Python Toolkit** is a Python library that provides a Python wrapper
for the fantastic `Highcharts JS <https://www.highcharts.com/>`_ suite of JavaScript data
visualization libraries, with full integration into the robust Python ecosystem. The full
toolkit includes support for:

  * **Highcharts JS** - the core Highcharts data visualization library
  * **Highcharts Stock** - the robust time series visualization extension to Highcharts JS
  * **Highcharts Maps** - the rich map visualization extension to Highcharts JS
  * **Highcharts Gantt** - the :term:`Gantt charting <Gantt Chart>` extension to
    Highcharts JS
  * The **Highcharts Export Server** - enabling the programmatic creation of static
    (downloadable) data visualizations

In order to integrate **Highcharts for Python** into the Python ecosystem, the library
features native integration with:

  * **Jupyter Notebook**. You can now produce high-end and interactive plots and renders
    using the full suite of Highcharts visualization capabilities.
  * **Pandas**. Automatically produce data visualizations from your Pandas dataframes
  * **PySpark**. Automatically produce data visualizations from data in a PySpark
    dataframe.

.. contents::
  :depth: 3
  :backlinks: entry

---------------------

*********************************
Installation
*********************************

.. include:: _installation.rst

Dependencies
===============

.. include:: _dependencies.rst

*********************************
Why Highcharts for Python?
*********************************

Odds are you are aware of `Highcharts JS <https://www.highcharts.com/>`_. If not, why not?
It is the world's most popular, most powerful, category-defining JavaScript data
visualization library. If you are building a web or mobile app/dashboard that will be
visualizing data in some fashion, you should absolutely take a look at the Highcharts
suite of solutions. Just take a look at some of their fantastic
`demo visualizations <https://www.highcharts.com/demo>`_.

As the library name suggests, Highcharts JS is a JavaScript library. It is written in
JavaScript, and is specifically used to configure and render data visualizations in a
web browser (or other JavaScript-executing, like mobile app) environment. As a JavaScript
library, its audience is JavaScript developers. But what about the broader ecosystem of
Python developers and data scientists?

Python is increasingly used as the technology of choice for data scientists and for
creating the back-end of leading enterprise-grade applications. As such, it often provides
the backend services that drive web and mobile applications - in other words, Python is
often the backend that delivers data and content to the front-end...which then renders it
using JavaScript and HTML.

There are numerous Python frameworks (Django, Flask, Tornado, etc.) with specific
capabilities to simplify integration with Javascript frontend frameworks (React, Angular,
VueJS, etc.). But facilitating that with Highcharts has historically been very difficult.
Part of this difficulty is because Highcharts JS - while supporting JSON as a
serialization/deserialization format - leverages JavaScript object literals to expose the
full power and interactivity of its data visualizations. And while it's easy to serialize
JSON from Python, serializing and deserializing to/from JavaScript object literal notation
is much more complicated. This means that Python developers looking to integrate with
Highcharts typically had to either invest a lot of effort, or were only able to access
a small portion of Highcharts rich functionality.

So I wrote the **Highcharts for Python** toolkit to bridge that gap.

**Highcharts for Python** provides Python object representation for *all* of the
JavaScript objects defined in the Highcharts API. It provides automatic data validation,
and exposes simple and standardized methods for serializing those Python objects
back-and-forth to JavaScript object literal notation.

Key Highcharts for Python Features
======================================

* **Clean and consistent API**. No reliance on "hacky" code, :class:`dict <python:dict>`
  and JSON serialization, or impossible to maintain / copy-pasted "spaghetti code".
* **Comprehensive Highcharts support**. Every single Highcharts chart type and every
  single configuration option is supported in **Highcharts for Python**. This includes the
  use of Highcharts' rich JavaScript formatter (JS callback function) capabilities that
  are often needed to get the most out of Highcharts' visualization and interaction
  capabilities.
* **Simple JavaScript Code Generation**. With one method call, produce production-ready
  JavaScript code to render your interactive visualizations using Highcharts' rich
  capabilities.
* **Easy and Robust Chart Download**. With one method call, produce high-end static
  visualizations that can be downloaded or shared as files with your audience. Produce
  static charts using the Highsoft-provided :term:`Highcharts Export Server`, or using
  your own private export server as needed.
* **Integration with Pandas and PySpark**. With two lines of code, produce a high-end
  interactive visualization of your Pandas or PySpark dataframe.
* Leverage Highcharts visualization templates in your Python code to eliminate "fiddly"
  configuration tweaks.
* **Consistent code style**. For Python developers, switching between Pythonic code
  conventions and JavaScript code conventions can be...annoying. So
  **Highcharts for Python** applies Pythonic syntax with automatic conversion between
  Pythonic ``snake_case`` notation and JavaScript ``camelCase`` styles.

|

**Highcharts for Python** vs Alternatives
==============================================

.. include:: _versus_alternatives.rst

---------------------

********************************
Hello World, and Basic Usage
********************************

1. Import Highcharts for Python
=====================================

  .. code-block:: python

    from highcharts_python import highcharts

  .. seealso::

    * :ref:`Importing Your Configuration Objects <importing_config_objects>`

2. Create Your Chart
================================

  .. code-block:: python

    # from a JavaScript file
    my_chart = highcharts.Chart.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_chart = highcharts.Chart.from_json('my_json.json')

    # from a Python dict
    my_chart = highcharts.Chart.from_dict(my_dict_obj)

    # from a Pandas dataframe
    my_chart = highcharts.Chart.from_pandas(df)

    # from a PySpark dataframe
    my_chart = highcharts.Chart.from_pyspark(df)

    # from a CSV
    my_chart = highcharts.Chart.from_csv('/some_file_location/filename.csv')

    # from a HighchartsOptions configuration object
    my_chart = highcharts.Chart.from_options(my_options)

    # from a Series configuration
    my_chart = highcharts.Chart.from_series(my_series)


  .. seealso::

    * :ref:`Instantiating Your Highcharts for Python Objects <instantiating>`

3. Configure Global Settings (optional)
=============================================

  .. code-block:: python

    # Import SharedOptions
    from highcharts.global_options.shared_options import SharedOptions

    # from a JavaScript file
    my_global_settings = SharedOptions.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_global_settings = SharedOptions.from_json('my_json.json')

    # from a Python dict
    my_global_settings = SharedOptions.from_dict(my_dict_obj)

    # from a HighchartsOptions configuration object
    my_global_settings = SharedOptions.from_options(my_options)

  .. seealso::

    * :ref:`Configuring Global Settings for Your Charts <global_settings>`


4. Configure Your Chart / Global Settings
================================================

  .. code-block:: python

    from highcharts.options.title import Title
    from highcharts.options.credits import Credits

    # Using dicts
    my_chart.title = {
        'align': 'center'
        'floating': True,
        'text': 'The Title for My Chart',
        'use_html': False,
    }

    my_chart.credits = {
        'enabled': True,
        'href': 'https://www.highcharts.com/',
        'position': {
            'align': 'center',
            'vertical_align': 'bottom',
            'x': 123,
            'y': 456
        },
        'style': {
            'color': '#cccccc',
            'cursor': 'pointer',
            'font_size': '9px'
        },
        'text': 'Chris Modzelewski'
    }

    # Using direct objects
    from highcharts.options.title import Title
    from highcharts.options.credits import Credits

    my_title = Title(text = 'The Title for My Chart', floating = True, align = 'center')
    my_chart.options.title = my_title

    my_credits = Credits(text = 'Chris Modzelewski', enabled = True, href = 'https://www.highcharts.com')
    my_chart.options.credits = my_credits

  .. seealso::

    * :ref:`Configuring Your Charts <configuring>`

5. Generate the JavaScript Code for Your Chart
=================================================

Now having configured your chart in full, you can easily generate the JavaScript code
that will render the chart wherever it is you want it to go:

  .. code-block:: python

    # as a string
    js_as_str = my_chart.to_js_literal()

    # to a file (and as a string)
    js_as_str = my_chart.to_js_literal(filename = 'my_target_file.js')

  .. seealso::

    * :ref:`Rendering Your Charts <rendering>`
    * :ref:`Using Highcharts for Python with Flask`
    * :ref:`Using Highcharts for Python with Django`

6. Generate the JavaScript Code for Your Global Settings (optional)
=========================================================================

  .. code-block:: python

    # as a string
    global_settings_js = my_global_settings.to_js_literal()

    # to a file (and as a string)
    global_settings_js = my_global_settings.to_js_literal('my_target_file.js')

  .. seealso::

    * :ref:`Rendering Your Charts <rendering>`
    * :ref:`Using Highcharts for Python with Flask <flask>`
    * :ref:`Using Highcharts for Python with Django <django>`

7. Generate a Static Version of Your Chart
==============================================

  .. code-block:: python

    # as in-memory bytes
    my_image_bytes = my_chart.download_chart(format = 'png')

    # to an image file (and as in-memory bytes)
    my_image_bytes = my_chart.download_chart(filename = 'my_target_file.png',
                                             format = 'png')

  .. seealso::

    * :ref:`Exporting Your Chart <exporting>`

--------------

*********************
Questions and Issues
*********************

You can ask questions and report issues on the project's
`Github Issues Page <https://github.com/hcpllc/highcharts-python/issues>`_

-----------------

*********************
Contributing
*********************

We welcome contributions and pull requests! For more information, please see the
:doc:`Contributor Guide <contributing>`. And thanks to all those who've already
contributed:

.. include:: _contributors.rst

-------------------

*********************
Testing
*********************

We use `TravisCI <http://travisci.org>`_ for our build automation and
`ReadTheDocs <https://readthedocs.org>`_ for our documentation.

Detailed information about our test suite and how to run tests locally can be
found in our :doc:`Testing Reference <testing>`.

--------------------

********************
Indices and tables
********************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
