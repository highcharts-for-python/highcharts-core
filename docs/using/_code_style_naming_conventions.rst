  *There are only two hard things in Computer Science: cache invalidation and naming
  things.* -- Phil Karlton

Highcharts Core is a JavaScript library, and as such it adheres to the code conventions
that are popular (practically standard) when working in JavaScript. Chief among these
conventions is that variables and object properties (keys) are typically written in
``camelCase``.

A lot of (digital) ink has been spilled writing about the pros and cons of ``camelCase``
vs ``snake_case``. While I have a scientific evidence-based opinion on the matter, in
practice it is simply a convention that developers adopt in a particular programming
language. The issue, however, is that while JavaScript has adopted the ``camelCase``
convention, Python generally skews towards the ``snake_case`` convention.

For most Python developers, using ``snake_case`` is the "default" mindset. Most of your
Python code will use ``snake_case``. So having to switch into ``camelcase`` to interact
with Highcharts Core forces us to context switch, increases cognitive load, and is an
easy place for us to overlook things and make a mistake that can be quite annoying to
track down and fix later.

Therefore, when designing the **Highcharts for Python Toolkit**, we made several carefully
considered design choices when it comes to naming conventions:

#. All **Highcharts for Python** classes follow the Pythonic ``PascalCase`` class-naming
   convention.
#. All **Highcharts for Python** properties and methods follow the Pythonic
   ``snake_case`` property/method/variable/function-naming convention.
#. All *inputs* to properties and methods support *both* ``snake_case`` and
   ``camelCase`` (aka ``mixedCase``) convention by default. 
   
   This means that you can take something directly from Highcharts JavaScript code and 
   supply it to the **Highcharts for Python Toolkit** without having to convert case or 
   conventions. But if you are constructing and configuring something directly in Python 
   using explicit :ref:`deserialization methods <deserialization_methods>`, you can use 
   ``snake_case`` if you prefer (and most Python developers will prefer).

   For example, if you supply a JSON file to a ``from_json()`` method, that file can
   leverage Highcharts (JS) natural ``camelCase`` convention OR Highcharts for Python's
   ``snake_case`` convention.

   .. warning::

     Note that this dual-convention support only applies to
     :ref:`deserialization methods` and does *not* apply to the
     **Highcharts for Python** ``__init__()`` class constructors. All ``__init__()``
     methods expect ``snake_case`` properties to be supplied as keywords.

#. All *outputs* from serialization methods (e.g. ``to_dict()`` or ``to_js_literal()``)
   will produce outputs that are Highcharts (JS)-compatible, meaning that they apply the
   ``camelCase`` convention.

.. tip::

  **Best Practice**

  If you are using external files to provide templates or themes for your Highcharts
  data visualizations, produce those external files using Highcharts JS' natural
  ``camelCase`` convention. That will make it easier to re-use them elsewhere within a
  JavaScript context if you need to in the future.
