#############################
Using Highcharts for Python
#############################

.. contents::
  :depth: 2
  :backlinks: entry

--------------

***************************************************************
An Introduction to Highcharts JS and Highcharts for Python
***************************************************************

`Highcharts JS <https://www.highcharts.com>`_  is the gold-standard in JavaScript data
visualization libraries, enabling you to design rich, beautiful, and highly interactive
data visualizations of (almost) every kind imaginable, and to render those visualizations
in your web or mobile applications. Take a look at some of their
`customer showcases <https://www.highcharts.com/blog/posts/use-cases/>`_ and their own
`demo gallery <https://www.highcharts.com/demo>`_
to see what you can do with Highcharts.

**Highcharts for Python** is a Python wrapper for the
`Highcharts JS <https://www.highcharts.com>`_ JavaScript library, which means that it is
designed to give developers working in Python a simple and Pythonic way of interacting
with Highcharts JS. Highcharts for Python will *not* render data visualizations itself -
that's what Highcharts JS does - but it *will* allow you to:

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

`Highcharts JS <https://www.highcharts.com/>`_ is a large, robust, and complicated
JavaScript library. If in doubt, take a look at their extensive
`documentation <https://www.highcharts.com/docs/index>`_ and in particular their
`API reference <https://api.highcharts.com/highcharts>`_. Because
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
conventions is that variables, objects, and object properties (keys) are typically written
in ``camelCase``.

A lot of (digital) ink has been spilled writing about the pros and cons of ``camelCase``
vs ``snake_case``. While I have a scientific evidence-based opinion on the matter, in
practice it is simply a convention that developers adopt in a particular programming
language. The issue, however, is that while JavaScript has adopted the ``camelCase``
convention, Python generally skews towards the ``snake_case`` convention.

For most Python developers, using ``snake_case`` is the "default" mindset. Most of their
Python code will use ``snake_case``. So having to switch to ``camelcase`` to interact with
Highcharts JS would force us to context switch, increases cognitive load, and is an easy
place for a developer to overlook things and make a mistake that can be quite annoying to
track down and fix later.

Therefore, when designing **Highcharts for Python**, we made several carefully considered
design choices when it comes to naming conventions:

  #. All **Highcharts for Python** classes follow the Pythonic ``ClassName`` (PascalCase)
     convention.
  #. All **Highcharts for Python** properties and methods follow the Pythonic
     ``snake_case`` convention.
  #. All *inputs* to properties and methods support *both* ``snake_case`` and
     ``camelCase`` (aka ``mixedCase``) convention by default. This means that you can take
     something directly from Highcharts JS' JavaScript code and supply it to
     **Highcharts for Python** without having to convert case or conventions. But if you
     are constructing and configuring something directly in Python, you can use
     ``snake_case`` if you prefer (and most Python developers will prefer).

     For example, if you supply a JSON file to a ``from_json()`` method, that file can
     leverage Highcharts JS natural ``camelCase`` convention OR Highcharts for Python's
     ``snake_case`` convention.
  #. All *outputs* from serialization methods (e.g. ``to_dict()`` or ``to_js_literal()``)
     will produce outputs that are Highcharts JS-compatible, meaning that they apply the
     ``camelCase`` convention.

.. tip::

  **Best Practice**

  If you are using external files to provide templates or themes for your Highcharts
  data visualizations, produce those external files using Highcharts JS' natural
  ``camelCase`` convention. That will make it easier to re-use them elsewhere within a
  JavaScript context if you need to in the future.

Classes and Standard Methods
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

.. method:: from_js_literal(cls, as_string_or_file: str, allow_snake_case: bool = True)
  :classmethod:

  Convert a JavaScript object defined using :term:`JavaScript literal notation` into a
  **Highcharts for Python** Python object, typically descended from
  :class:`HighchartsMeta`.

  :param cls: The class (:class:`type <python:type>`) object itself.
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

  :returns: A **Highcharts for Python** Python object corresponding to the JavaScript
    object supplied in ``as_string_or_file``.
  :rtype: Descendent of :class:`HighchartsMeta`


.. method:: from_dict(cls, as_dict: dict, allow_snake_case: bool = True)
  :classmethod:

  Convert a :class:`dict <python:dict>` representation of a Highcharts JS object into a
  Python object representation, typically descended from :class:`HighchartsMeta`.

  :param cls: The class (:class:`type <python:type>`) object itself.
  :type cls: :class:`type <python:type>`

  :param as_dict: The :class:`dict <python:dict>` representation of the object.
  :type as_dict: :class:`dict <python:dict>`

  :param allow_snake_case: If ``True``, allows keys in ``as_dict`` to apply the
    ``snake_case`` convention. If ``False``, will ignore keys that apply the
    ``snake_case`` convention and only process keys that use the ``camelCase`` convention.
    Defaults to ``True``.
  :type allow_snake_case: :class:`bool <python:bool>`

--------------------------

*************************************************
Organizing Your Highcharts for Python Project
*************************************************

.. todo::

  Add section for organizing your project.

-----------------

********************************************
Managing Your Configurations
********************************************

.. todo::

  Add a section for how to manage your chart (or global) configuration.

-----------------------

**************************************
Working with Data
**************************************

.. todo::

  Add a section explaining how to supply data to Highcharts for Python.

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
