#############################
Using Highcharts for Python
#############################

.. contents::
  :depth: 2
  :backlinks: entry

--------------

***************************************************************
Introduction to Highcharts JS and Highcharts for Python
***************************************************************

`Highcharts JS`_  is the gold-standard in JavaScript data visualization libraries,
enabling you to design rich, beautiful, and highly interactive data visualizations of
(almost) any kind imaginable, and to render those visualizations in your web or mobile
applications. Take a look at some of their
`customer showcases <https://www.highcharts.com/blog/posts/use-cases/>`_ and their own
`demo gallery <https://www.highcharts.com/demo>`_ to see what you can do with Highcharts.

**Highcharts for Python** is a Python wrapper for the
`Highcharts JS`_ JavaScript library, which means that it is designed to give developers
working in Python a simple and Pythonic way of interacting with Highcharts JS. Highcharts
for Python will *not* render data visualizations itself - that's what Highcharts JS does -
but it *will* allow you to:

  #. Configure your data visualizations in Python.
  #. Supply data you have in Python to your data visualizations.
  #. Programmatically produce the Highcharts JS JavaScript code that will actually render
     your data visualization.
  #. Programmatically download a static version of your visualization (as needed) within
     Python.

.. tip::

  Think of **Highcharts for Python** as a translator to bridge your data visualization
  needs between Python and JavaScript.

-------------------

*************************************************
Key Design Patterns in Highcharts for Python
*************************************************

`Highcharts JS`_ is a large, robust, and complicated JavaScript library. If in doubt, take
a look at their extensive `documentation <https://www.highcharts.com/docs/index>`_ and in
particular their `API reference <https://api.highcharts.com/highcharts>`_. Because
**Highcharts for Python** wraps the Highcharts JS API, its design is heavily shaped by
Highcharts JS' own design - as one should expect.

However, one of the main goals of **Highcharts for Python** is to make the Highcharts JS
library a little more Pythonic in terms of its design to make it easier for Python
developers to leverage it. Here are the notable design patterns that have been adopted
that you should be aware of:

Code Style: Python vs JavaScript Naming Conventions
=======================================================

  *There are only two hard things in Computer Science: cache invalidation and naming
  things.* -- Phil Karlton

Highcharts JS is a JavaScript library, and as such it adheres to the code conventions that
are popular (practically standard) when working in JavaScript. Chief among these
conventions is that variables and object properties (keys) are typically written in
``camelCase``.

A lot of (digital) ink has been spilled writing about the pros and cons of ``camelCase``
vs ``snake_case``. While I have a scientific evidence-based opinion on the matter, in
practice it is simply a convention that developers adopt in a particular programming
language. The issue, however, is that while JavaScript has adopted the ``camelCase``
convention, Python generally skews towards the ``snake_case`` convention.

For most Python developers, using ``snake_case`` is the "default" mindset. Most of their
Python code will use ``snake_case``. So having to switch into ``camelcase`` to interact
with Highcharts JS forces us to context switch, increases cognitive load, and is an easy
place for us to overlook things and make a mistake that can be quite annoying to
track down and fix later.

Therefore, when designing **Highcharts for Python**, we made several carefully considered
design choices when it comes to naming conventions:

  #. All **Highcharts for Python** classes follow the Pythonic ``PascalCase`` class-naming
     convention.
  #. All **Highcharts for Python** properties and methods follow the Pythonic
     ``snake_case`` property/method/variable/function-naming convention.
  #. All *inputs* to properties and methods support *both* ``snake_case`` and
     ``camelCase`` (aka ``mixedCase``) convention by default. This means that you can take
     something directly from Highcharts JS' JavaScript code and supply it to
     **Highcharts for Python** without having to convert case or conventions. But if you
     are constructing and configuring something directly in Python using explicit
     :ref:`deserialization methods <deserialization_methods>`, you can use ``snake_case``
     if you prefer (and most Python developers will prefer).

     For example, if you supply a JSON file to a ``from_json()`` method, that file can
     leverage Highcharts JS natural ``camelCase`` convention OR Highcharts for Python's
     ``snake_case`` convention.

     .. warning::

       Note that this dual-convention support only applies to
       :ref:`deserialization methods` and does *not* apply to the
       **Highcharts for Python** ``__init__()`` class constructors. All ``__init__()``
       methods expect ``snake_case`` properties to be supplied as keywords.

  #. All *outputs* from serialization methods (e.g. ``to_dict()`` or ``to_js_literal()``)
     will produce outputs that are Highcharts JS-compatible, meaning that they apply the
     ``camelCase`` convention.

.. tip::

  **Best Practice**

  If you are using external files to provide templates or themes for your Highcharts
  data visualizations, produce those external files using Highcharts JS' natural
  ``camelCase`` convention. That will make it easier to re-use them elsewhere within a
  JavaScript context if you need to in the future.

Standard Methods
=======================================

Every single object supported by the Highcharts JS API corresponds to a Python class in
**Highcharts for Python**. You can find the complete list in our comprehensive
:doc:`Highcharts for Python API Reference <api>`.

These classes generally inherit from the :class:`HighchartsMeta` metaclass, which provides
each class with a number of standard methods. These methods are the "workhorses" of
**Highcharts for Python** and you will be relying heavily on them when using the library.
Thankfully, their signatures and behavior is generally consistent - even if what happens
"under the hood" is class-specific at times.

The standard methods exposed by the classes are:

.. _deserialization_methods:

Deserialization Methods
---------------------------

  .. method:: from_js_literal(cls, as_string_or_file, allow_snake_case = True)
    :classmethod:

    Convert a JavaScript object defined using :term:`JavaScript literal notation` into a
    **Highcharts for Python** Python object, typically descended from
    :class:`HighchartsMeta`.

    :param cls: The class object itself.
    :type cls: :class:`type <python:type>`

    :param as_string_or_file: The JavaScript object you wish to convert. Expects either a
      :class:`str <python:str>` containing the JavaScript object, or a path to a file which
      consists of the object.
    :type as_string_or_file: :class:`str <python:str>`

    :param allow_snake_case: If ``True``, allows keys in ``as_string_or_file`` to apply the
      ``snake_case`` convention. If ``False``, will ignore keys that apply the
      ``snake_case`` convention and only process keys that use the ``camelCase`` convention.
      Defaults to ``True``.
    :type allow_snake_case: :class:`bool <python:bool>`

    :returns: A **Highcharts for Python** object corresponding to the JavaScript
      object supplied in ``as_string_or_file``.
    :rtype: Descendent of :class:`HighchartsMeta`


  .. method:: from_json(cls, as_json_or_file, allow_snake_case = True)
    :classmethod:

    Convert a Highcharts JS object represented as JSON (in either :class:`str <python:str>`
    or :class:`bytes <python:bytes>` form, or as a file name) into a
    **Highcharts for Python** object, typically descended from :class:`HighchartsMeta`.

    :param cls: The class object itself.
    :type cls: :class:`type <python:type>`

    :param as_json_or_file: The JSON object you wish to convert, or a filename that contains
      the JSON object that you wish to convert.
    :type as_json_or_file: :class:`str <python:str>` or :class:`bytes <python:bytes>`

    :param allow_snake_case: If ``True``, allows keys in ``as_json`` to apply the
      ``snake_case`` convention. If ``False``, will ignore keys that apply the
      ``snake_case`` convention and only process keys that use the ``camelCase`` convention.
      Defaults to ``True``.
    :type allow_snake_case: :class:`bool <python:bool>`

    :returns: A **Highcharts for Python** Python object corresponding to the JSON
      object supplied in ``as_json``.
    :rtype: Descendent of :class:`HighchartsMeta`


  .. method:: from_dict(cls, as_dict, allow_snake_case = True)
    :classmethod:

    Convert a :class:`dict <python:dict>` representation of a Highcharts JS object into a
    Python object representation, typically descended from :class:`HighchartsMeta`.

    :param cls: The class object itself.
    :type cls: :class:`type <python:type>`

    :param as_dict: The :class:`dict <python:dict>` representation of the object.
    :type as_dict: :class:`dict <python:dict>`

    :param allow_snake_case: If ``True``, allows keys in ``as_dict`` to apply the
      ``snake_case`` convention. If ``False``, will ignore keys that apply the
      ``snake_case`` convention and only process keys that use the ``camelCase`` convention.
      Defaults to ``True``.
    :type allow_snake_case: :class:`bool <python:bool>`


.. _serialization_methods:

Serialization Methods
--------------------------

  .. method:: to_js_literal(self, filename = None, encoding = 'utf-8')

    Convert the **Highcharts for Python** instance to Highcharts JS-compatible JavaScript
    code using :term:`JavaScript literal notation`.

    :param filename: If supplied, persists the JavaScript code to the file indicated.
      Defaults to :obj:`None <python:None>`.
    :type filename: Path-like or :obj:`None <python:None>`

    :param encoding: Indicates the character encoding to use when producing the JavaScript
      literal string. Defaults to ``'utf-8'``.
    :type encoding: :class:`str <python:str>`

    :returns: Highcharts JS-compatible JavaScript code using
      :term:`JavaScript literal notation`.
    :rtype: :class:`str <python:str>`


  .. method:: to_json(self, filename = None, encoding = 'utf-8')

    Convert the **Highcharts for Python** instance to Highcharts JS-compatible JSON.

    .. warning::

      While similar, JSON is inherently different from
      :term:`JavaScript object literal notation`. In particular, it cannot include
      JavaScript functions. This means if you try to convert a Highcharts for Python object
      to JSON, any properties that are :class:`CallbackFunction` instances will not be
      included. If you want to convert those functions, please use ``.to_js_literal()``
      instead.

    :param filename: If supplied, persists the JSON is persisted to the file indicated.
      Defaults to :obj:`None <python:None>`.
    :type filename: Path-like or :obj:`None <python:None>`

    :param encoding: Indicates the character encoding to use when producing the JSON.
      Defaults to ``'utf-8'``.
    :type encoding: :class:`str <python:str>`

    :returns: Highcharts JS-compatible JSON representation of the object.
    :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`

      .. note::

        **Highcharts for Python** works with different JSON encoders. If your environment
        has `orjson <https://github.com/ijl/orjson>`_, for example, the result will be
        returned as a :class:`bytes <python:bytes>` instance. Otherwise, the library will
        fallback to various other JSON encoders until finally falling back to the Python
        standard library's JSON encoder/decoder.


  .. method:: to_dict(self)

    Convert the **Highcharts for Python** object into a Highcharts JS-compatible
    :class:`dict <python:dict>` object.

    :returns: Highcharts JS-compatible :class:`dict <python:dict>` object
    :rtype: :class:`dict <python:dict>`


.. _other_methods:

Other Methods
--------------------------

  .. method:: copy(self, other, overwrite = True, **kwargs)

    Copy the properties from ``self`` to ``other``.

    :param other: The target instance to which the properties of this instance should
      be copied.
    :type other: :class:`HighchartsMeta`

    :param overwrite: if ``True``, properties in ``other`` that are already set will
      be overwritten by their counterparts in ``self``. Defaults to ``True``.
    :type overwrite: :class:`bool <python:bool>`

    :param kwargs: Additional keyword arguments. Some special descendents of
      :class:`HighchartsMeta` may have special implementations of this method which
      rely on additional keyword arguments.

    :returns: A mutated version of ``other`` with new property values

    :raises HighchartsValueError: if ``other`` is not the same class as (or subclass of)
      ``self``


Module Structure
=====================

The structure of the **Highcharts for Python** library closely matches the structure
of the `Highcharts JS`_ options object (see the relevant
`reference documentation <https://api.highcharts.com/highcharts/>`_).

At the root of the library - importable from ``highcharts_python`` you will find the
``highcharts`` module. This module is a catch-all importable module, which allows you to
easily access all of the Highcharts for Python classes defined.

.. note::

  Whlie you can access all of the **Highcharts for Python** classes from
  ``highcharts_python.highcharts``, if you want to more precisely navigate to sepcific
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

    # APPROACH #2: Import a specific class by name from the "highcharts" module.
    from highcharts_python.highcharts import Chart

Class Structures and Inheritance
====================================

`Highcharts JS`_ objects re-use many of the same properties. This is one of the strengths
of the Highcharts API, in that it is internally consistent and that behavior configured on
one object should be readily transferrable to a second object provided it shares the same
properties. However, Highcharts JS has a *lot* of properties. For example, I estimate that
the ``options.plotOptions`` objects and their sub-properties have close to 3,000
properties. But because they are heavily repeated, those 3,000 or so properties can be
reduced to only 421 unique property names. That's almost an 85% reduction.

:iabbr:`DRY (Don't Repeat Yourself)` is an important principle in software development.
Can you imagine propagating changes in seven places (on average) in your code? That would
be a maintenance nightmare! And it is exactly the kind of maintenance nightmare that class
inheritance was designed to fix.

For that reason, the **Highcharts for Python** classes have a deeply nested inheritance
structure. This is important to understand both for evaluating ``isinstance()`` checks
in your code, or for understanding how to further subclass Highcharts for Python
components.

  .. seealso::

    For a full diagram of Highcharts for Python class structure, please see the
    :ref:`Highcharts for Python API Reference: Class Hierarchy <class_hierarchy>`.

.. warning::

  Certain sections of the **Highcharts for Python** library - in particular the
  ``options.series`` classes - rely heavily on multiple inheritance. This is a known
  anti-pattern in Python development as it runs the risk of encountering the
  :term:`diamond of death` inheritance problem. This complicates the process of inheriting
  methods or properties from parent classes when properties or methods share names
  across multiple parents.

  I know this is an anti-pattern, but it was a necessary one to minimize code duplication
  and maximize consistency. For that reason, I implemented it properly *despite* the
  anti-pattern, using some advanced Python concepts to navigate the Python MRO
  (Method Resolution Order) system cleanly. However, an awareness of the pattern used
  may prove helpful if your code inherits from the Highcharts for Python classes.

  .. seealso::

    For a more in-depth discussion of how the anti-pattern was implemented safely and
    reliably, please review the :doc:`Contributor Guidelines <contributing.rst>`.

--------------------------

*************************************************
Organizing Your Highcharts for Python Project
*************************************************

**Highcharts for Python** is a utility that can integrate with - quite literally - any
frontend framework. Whether your Python application is relying on iPython (e.g.
`Jupyter Notebook <>`_ or `Jupyter Labs <>`_), `Flask <>`_, `Django <>`_, `FastAPI <>`_,
`Pyramid <>`_, `Tornado <>`_, or some completely home-grown solution all Highcharts for
Python needs is a place where `Highcharts JS`_ JavaScript code can be executed.

All of those frameworks I mentioned have their own best practices for organizing their
application structures, and those should *always* take priority. Even in a data-centric
application that will be relying heavily on **Highcharts for Python**, your application's
core business logic will be doing most of the heavy lifting and so your project's
organization should reflect that.

However, there are a number of best practices that we recommend for organizing your
files and code to work with **Highcharts for Python**:

  .. warning::

      *There are nine and sixty ways of constructing a tribal lay, and every single one of
      them is right!* -- Rudyard Kipling, *In the Neolithic Age*

    The organizational model described below is just a suggestion, and you can (and likely
    will) depart from its principles and practices as you gain more experience using
    **Highcharts for Python**. There's nothing wrong with that! It's just a set of best
    practices that we've found work for us and which we therefore recommend.

.. _shared_options:

Use Shared Options
========================

One of the most challenging aspects of `Highcharts JS`_ is its sheer breadth of
functionality and configurability. That's simultaneously the library's greatest strength,
and its greatest weakness. This is because it can be quite challenging to wrangle
thousands of properties - especially when one single visualization can use thousands
of properties!

This is a challenge that the developers of `Highcharts JS`_ are keenly aware of, and one
which we've given some thought to in the **Highcharts for Python** library. A core
principle you should use throughout your project is to practice
:iabbr:`DRY (Do Not Repeat Yourself)` programming. If your application will be generating
multiple visualizations, they will likely need some consistent configurations.

For example, you will want their title position to be consistent, their color schemes to
be consistent, their font sizing to be consistent, etc. In your code you want these
configuration settings to be defined *once* and then applied to all of the visualizations
you are producing.

This can be facilitated using the
:class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
class. It generates a single set of global options which - when serialized to JavaScript -
apply its configuration settings consistently across all data visualizations on the same
page.

As with all **Highcharts for Python** objects, you can instantiate them in several ways:

.. tabs::

  .. tab:: with JS Literal

    .. tip::

      **Best practice!**

      We really like to use JS literals written as separate files in our codebase. It
      makes it super simple to instantiate a
      :class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
      instance with one method call.

    Let's say you organize your files like so:

      .. line-block::

        my_repository/
        | --- docs/
        | --- my_project/
        | ------ project_resources/
        | --------- image_files/
        | --------- data_files/
        | ------------ data-file-01.csv
        | ------------ data-file-02.csv
        | ------------ data-file-03.csv
        | --------- **highcharts_config/**
        | ------------ **shared_options.js**
        | ------------ bar-template-01.js
        | ------------ bar-template-02.js
        | ------------ line-template.js
        | ------------ packed-bubble-template.js
        | ------ some_package/
        | --------- __init__.py
        | --------- package_module.py
        | --------- another_module.py
        | ------ __init__.py
        | ------ __version__.py
        | ------ some_module.py
        | --- tests/
        | --- .gitignore
        | --- requirements.txt

    You'll notice that the organization has a ``project_resources`` folder. This is where
    you would put the various files that your application wlil reference, like your static
    images, or the files that contain data you might be using in your application. It also
    contains a **highcharts_config** folder, which contains several files with a ``.js``
    extension. Of particular note is the file in bold, ``shared_options.js``. This file
    should contain a :term:`JavaScript object literal <JavaScript object literal>`
    version of the configuration settings you want to apply to *all* of your
    visualizations. This file might look something like this:

      .. literalinclude:: _static/shared_options.js
        :language: javascript

    Now with this file, you can easily create a
    :class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
    instance by executing:

      .. code-block:: python

        from highcharts_python.highcharts import SharedOptions

        my_shared_options = SharedOptions.from_js_literal('../../project_resources/highcharts_config/shared_options.js')

    And that's it! Now you have a
    :class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
    instance that can be used to apply your configuration standards to all of your charts.
    You can do that by delivering its JavaScript output to your front-end by calling:

      .. code-block:: python

        js_code_snippet = my_shared_options.to_js_literal()

    which will produce a string as follows:

      .. literalinclude:: _static/shared_options_output.js
        :language: javascript

    And now you can deliver ``js_code_snippet`` to your HTML template or wherever it will
    be rendered.

  .. tab:: with JSON

    You can use the same exact pattern as using a JS literal with a JSON file instead.
    We don't really think there's an advantage to this - but there might be one
    significant disadvantage: JSON files cannot be used to provide JavaScript functions
    to your Highcharts configuration. This means that formatters, event handlers, etc.
    will not be applied through your shared options if you use a JSON file.

    If your shared options don't require JavaScript functions? Then by all means, feel
    free to use a JSON file and the ``.from_json()`` method instead.

    With a file structure like:

      .. line-block::

        my_repository/
        | --- docs/
        | --- my_project/
        | ------ project_resources/
        | --------- image_files/
        | --------- data_files/
        | ------------ data-file-01.csv
        | ------------ data-file-02.csv
        | ------------ data-file-03.csv
        | --------- **highcharts_config/**
        | ------------ **shared_options.json**
        | ------------ bar-template.json
        | ------------ line-template.json
        | ------------ packed-bubble-template.json
        | ------ some_package/
        | --------- __init__.py
        | --------- package_module.py
        | --------- another_module.py
        | ------ __init__.py
        | ------ __version__.py
        | ------ some_module.py
        | --- tests/
        | --- .gitignore
        | --- requirements.txt

    You can leverage shared options that read from
    ``my_project/project_resources/highcharts_config/shared_options.json`` by executing:

      .. code-block:: python

        from highcharts_python.highcharts import SharedOptions

        my_shared_options = SharedOptions.from_js_literal(
            '../../project_resources/highcharts_config/shared_options.json'
        )

        json_code_snippet = my_shared_options.to_js_literal()

  .. tab:: with ``dict``

    If you are hoping to configure a simple set of options, one of the fastest ways to do
    so in your Python code is to instantiate your
    :class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
    instance from a simple :class:`dict <python:dict>`:

      .. code-block:: python

        as_dict = {
            'chart': {
                'backgroundColor': '#fff',
                'borderWidth': 2,
                'plotBackgroundColor': 'rgba(255, 255, 255, 0.9)',
                'plotBorderWidth': 1
            }
        }

        my_shared_options = SharedOptions.from_dict(as_dict)

        js_code_snippet = my_shared_options.to_js_literal()

      .. tip::

        This method is particularly helpful and easy to maintain if you are only using a
        *very* small subset of the `Highcharts JS`_ configuration options.

  .. tab:: with ``__init__()``

    You can also instantiate a
    :class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
    instance directly using keywords in the constructor:

      .. code-block:: python

        from highcharts_python.highcharts import ChartOptions, SharedOptions

        my_shared_options = SharedOptions(chart = ChartOptions(background_color = '#fff',
                                                               border_width = 2,
                                                               plot_background_color = 'rgba(255, 255, 255, 0.9)',
                                                               plot_border_width = 1))

        js_code_snippet = my_shared_options.to_js_literal()

      .. note::

        You can also supply :class:`dict <python:dict>` representations as keyword argument
        values in the object constructors.

      .. tip::

        **Best practice!**

        While you can create a
        :class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
        instance and then modify its properties after the fact, that's not exactly the best
        code style. It makes things a bit verbose, and a little harder to reason about.

        Instead, it's recommended that you instantiate your object with all of its
        properties in one go. If you need to change them later, you can do so using Python
        easily - but best to create it all at once.

Use Templates to Get Started
==================================

While :ref:`shared options <shared_options>` are applied to all charts that are rendered
on the same web page with the shared options JS code, certain types of visualizations
may need special treatment. Sure, you can use the
:meth:`plot_options <SharedOptions.plot_options>` settings to configure chart
type-specific options, but how can you efficiently use multiple charts of the same type
that have different settings?

For example, let's say you used :ref:`shared options <shared_options>` to set universal
bar chart settings. But what happens if you know you'll have different data shown in
different bar charts? You can use a similar templating pattern for different sub-types
of your charts.

.. tabs::

  .. tab:: with JS Literal

    .. tip::

      **Best practice!**

      We really like to use JS literals written as separate files in our codebase. It
      makes it super simple to instantiate a **Highcharts for Python** instance with one
      method call.

    Let's say you organize your files like so:

      .. line-block::

        my_repository/
        | --- docs/
        | --- my_project/
        | ------ project_resources/
        | --------- image_files/
        | --------- data_files/
        | ------------ data-file-01.csv
        | ------------ data-file-02.csv
        | ------------ data-file-03.csv
        | --------- **highcharts_config/**
        | ------------ shared_options.js
        | ------------ **bar-template-01.js**
        | ------------ **bar-template-02.js**
        | ------------ line-template.js
        | ------------ packed-bubble-template.js
        | ------ some_package/
        | --------- __init__.py
        | --------- package_module.py
        | --------- another_module.py
        | ------ __init__.py
        | ------ __version__.py
        | ------ some_module.py
        | --- tests/
        | --- .gitignore
        | --- requirements.txt

    As you can see, there are two JS literal files named ``bar-template-01.js`` and
    ``bar-template-02.js`` respectively. These template files can be used to significantly
    accelerate the configuration of our bar charts. Each template corresponds to one
    sub-type of bar chart that we know we will need. These sub-types may have different
    event functions, or more frequently use different formatting functions to make the
    data look the way we want it to look.

    Now with these template files, we can easily create a pair of
    :class:`Chart <highcharts_python.chart.Chart>` instances by executing:

      .. code-block:: python

        from highcharts_python.highcharts import Chart, BarSeries

        type_1_chart = Chart.from_js_literal(
            '../../project_resources/highcharts_config/bar-template-01.js'
        )
        type_2_chart = Chart.from_js_literal(
            '../../project_resources/highcharts_config/bar-template-02.js'
        )

    And that's it! Now you have two chart instances which you can further modify. For
    example, you can add data to them by calling:

      .. code-block:: python

        type_1_chart.container = 'chart1_div'
        type_2_chart.container = 'chart2_div'

        type_1_chart.add_series(BarSeries.from_csv('../../project_resources/data_files/data-file-01.csv'))
        type_2_chart.add_series(BarSeries.from_csv('../../project_resources/data_files/data-file-02.csv'))

    And then you can create the relevant JavaScript code to render the chart using:

      .. code-block:: python

        type_1_chart_js = type_1_chart.to_js_literal()
        type_2_chart_js = type_2_chart.to_js_literal()

    And now you can deliver ``type_1_chart_js`` and ``type_2_chart_js`` to your HTML
    template or wherever it will be rendered.

  .. tab:: with JSON

    You can use the same exact pattern as using a JS literal with a JSON file instead.
    We don't really think there's an advantage to this - but there might be one
    significant disadvantage: JSON files cannot be used to provide JavaScript functions
    to your Highcharts configuration. This means that formatters, event handlers, etc.
    will not be applied through your shared options if you use a JSON file.

    If your chart templates don't require JavaScript functions? Then by all means, feel
    free to use a JSON file and the ``.from_json()`` method instead of the
    ``.from_js_literal()`` method.

    .. tip::

      In practice, we find that most chart templates differ in their formatter functions
      and event handlers. This makes JSON a particularly weak tool for templating those
      charts. We strongly prefer the JS literal method described above.

  .. tab:: with ``dict``

    If you are hoping to configure a simple set of template settings, one of the fastest
    ways to do so in your Python code is to instantiate your
    :class:`Chart <highcharts_python.chart.Chart>` instance from a simple
    :class:`dict <python:dict>` using the ``.from_dict()`` method.

      .. tip::

        This method is particularly helpful and easy to maintain if you are only using a
        *very* small subset of the `Highcharts JS`_ configuration options.

  .. tab:: with ``.copy()``

    If you have an existing **Highcharts for Python** instance, you can copy its
    properties to another object using the ``.copy()`` method. You can therefore set up
    one chart, and then copy its properties to other chart objects with one method call.

      .. code-block:: python

        type_1_chart = Chart.from_js_literal('../../project_resources/highcharts_config/bar-template-01.js')
        other_chart = type_1_chart.copy(other_chart, overwrite = True)

      .. tip::

        The :meth:`Chart.copy() <highcharts_python.chart.Chart.copy>` method supports a
        special keyword argument, ``preverse_data`` which if set to ``True`` will copy
        properties (unless ``overwrite = True``) but will *not* overwrite any data. This
        can be very useful to replicating the configuration of your chart across multiple
        charts that have different series and data.

          .. code-block:: python

            other_chart = Chart()
            other_chart.add_series(
              BarSeries.from_csv('../../project_resources/data_files/data-file-02.csv')
            )

            other_chart = type_1_chart.copy(other_chart,
                                            preserve_data = True)

-----------------

**************************************
Working with Data
**************************************

Obviously, if you are going to use **Highcharts for Python** and `Highcharts JS`_ you will
need to have data to visualize. Python is rapidly becoming the *lingua franca* in the
world of data manipulation, transformation, and analysis and **Highcharts for Python**
is specifically designed to play well within that ecosystem to make it easy to visualize
data from CSV files, from `pandas <>`_ dataframes, or `PySpark <>`_ dataframes.

How Highcharts JS Represents Data
==================================

`Highcharts JS`_ supports two differen tways of representing data: as an individual
:term:`series` comprised of individual data points, and as a set of instructions to read
data dynamically from a CSV file or an HTML table.

  .. seealso::

    * :class:`DataBase <highcharts_python.options.series.data.base.DataBase>` class
    * :class:`options.Data <highcharts_python.options.data.Data>` class

`Highcharts JS`_ organizes data into :term:`series`. You can think of a series as a single
line on a graph that shows a set of values. The set of values that make up the series are
data points, which are defined by a set of properties that indicate the data point's
position on one or more axes. As a result, `Highcharts JS`_ and **Highcharts for Python**
both represent the data points in series as a list of data point objects in the ``data``
property within the series:

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - Highcharts JS
    - Highcharts for Python
  * - .. code-block:: javascript

        // Example Series Object
        // (for a Line series type):
        {
          data: [
            {
              id: 'first-data-point',
              x: 1,
              y: 123,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            },
            {
              id: 'second-data-point',
              x: 2,
              y: 456,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            },
            {
              id: 'third-data-point',
              x: 3,
              y: 789,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            }
          ],
          // ...
          // other Series properties go here
          // to configure styling/behavior
        }
    - .. code-block:: python

        # Corresponding LineSeries object
        my_series = Series(data = [
            CartesianData(id = 'first-data-point1',
                          x = 1,
                          y = 123),
            CartesianData(id = 'second-data-point1',
                          x = 2,
                          y = 456),
            CartesianData(id = 'third-data-point1',
                          x = 3,
                          y = 789),
        ])

As you can see, **Highcharts for Python** represents its data the same way that
`Highcharts JS`_ does. That should be expected. However, constructing tens, hundreds, or
possibly thousands of data points individually in your code would be a nightmare. For that
reason, **Highcharts for Python** provides a number of convenience methods to make it
easier to populate your series.

Every single :term:`Series` class in **Highcharts for Python** features several different
methods to either load data (to an existing series instance) or to create a new series
instance with data already loaded.

.. _loading_data_to_existing_series:

Loading to an Existing Series
-------------------------------

  .. method:: .load_from_csv(self, as_string_or_file, column_property_map, has_header_row = True, delimiter = ',', null_text = 'None', wrapper_character = "'", line_terminator = '\r\n')

    Updates the series instance with a collection of data points (descending from
    :class:`DataBase <highcharts_python.options.series.data.base.DataBase>`) from
    ``as_string_or_file`` by traversing the rows of data and extracting the values from
    the columns indicated in ``column_property_map``.

      .. warning::

        This method will overwrite the contents of the series instance's
        :meth:`data <highcharts_python.options.series.base.SeriesBase>` property.

      .. note::

        For an example
        :class:`LineSeries <highcharts_python.options.series.area.LineSeries>`, the
        minimum code required would be:

          .. code-block:: python

            my_series = LineSeries()
            my_series.load_from_csv('some-csv-file.csv',
                                    column_property_map = {
                                        'x': 0,
                                        'y': 3,
                                        'id': 'id'
                                    })

        As the example above shows, data is loaded into the ``my_series`` instance from
        the CSV file with a filename ``some-csv-file.csv``. The
        :meth:`x <CartesianData.x>`
        values for each data point will be taken from the first (index 0) column in the
        CSV file. The :meth:`y <CartesianData.y>` values will be taken from the fourth
        (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>` values
        will be taken from a column whose header row is labeled ``'id'`` (regardless of
        its index).

    :param as_string_or_file: The CSV data to load, either as a :class:`str <python:str>`
      or as the name of a file in the runtime enviroment. If a file, data will be read
      from the file.

      .. tip::

        Unwrapped empty column values are automatically interpreted as null
        (:obj:`None <python:None>`).

    :type as_string_or_file: :class:`str <python:str>` or Path-like

    :param column_property_map: A :class:`dict <python:dict>` used to indicate which
      data point property should be set to which CSV column. The keys in the
      :class:`dict <python:dict>` should correspond to properties in the data point class,
      while the value can either be a numerical index (starting with 0) or a
      :class:`str <python:str>` indicating the label for the CSV column.

      .. warning::

        If the ``column_property_map`` uses :class:`str <python:str>` values, the CSV file
        *must* have a header row (this is expected, by default). If there is no header row
        and a :class:`str <python:str>` value is found, a
        :exc:`HighchartsDeserializationError` will be raised.

    :type column_property_map: :class:`dict <python:dict>`

    :param has_header_row: If ``True``, indicates that the first row of
      ``as_string_or_file`` contains column labels, rather than actual data. Defaults to
      ``True``.
    :type has_header_row: :class:`bool <python:bool>`

    :param delimiter: The delimiter used between columns. Defaults to ``,``.
    :type delimiter: :class:`str <python:str>`

    :param wrapper_character: The string used to wrap string values when
      wrapping is applied. Defaults to ``'``.
    :type wrapper_character: :class:`str <python:str>`

    :param null_text: The string used to indicate an empty value if empty
      values are wrapped. Defaults to `None`.
    :type null_text: :class:`str <python:str>`

    :param line_terminator: The string used to indicate the end of a line/record in the
      CSV data. Defaults to ``'\r\n'``.
    :type line_terminator: :class:`str <python:str>`

    :returns: A collection of data points descended from
      :class:`DataBase <highcharts_python.options.series.data.base.DataBase>` as
      appropriate for the series class.
    :rtype: :class:`list <python:list>` of instances descended from
      :class:`DataBase <highcharts_python.options.series.data.base.DataBase>`

    :raises HighchartsDeserializationError: if unable to parse the CSV data correctly

--------------------

**************************************
Rendering Your Visualizations
**************************************

.. todo::

  Add a section for how to render your data visualization.

---------------------------

********************************************
Downloading Your Visualizations
********************************************

.. todo::

  Add a section for how to export your charts.

-----------------------------


.. _Highcharts JS: https://www.highcharts.com
