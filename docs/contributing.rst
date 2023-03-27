##############################################
Contributing to Highcharts for Python
##############################################

.. note::

  As a general rule of thumb, the **Highcharts for Python Toolkit** applies 
  :pep:`PEP 8 <8>` styling, with some important differences.

.. include:: _unit_tests_code_coverage.rst

.. sidebar:: What makes an API idiomatic?

  One of our favorite ways of thinking about idiomatic design comes from a `talk
  given by Luciano Ramalho at Pycon 2016`_ where he listed traits of a Pythonic
  API as being:

  * don't force [the user] to write boilerplate code
  * provide ready to use functions and objects
  * don't force [the user] to subclass unless there's a *very good* reason
  * include the batteries: make easy tasks easy
  * are simple to use but not simplistic: make hard tasks possible
  * leverage the Python data model to:

    * provide objects that behave as you expect
    * avoid boilerplate through introspection (reflection) and metaprogramming.


.. contents:: Contents:
  :local:
  :depth: 3

*************************
Design Philosophy
*************************

**Highcharts for Python** is meant to be a "beautiful" and "usable" library. That means
that it should offer an idiomatic API that:

* works out of the box as intended,
* minimizes "bootstrapping" to produce meaningful output, and
* does not force users to understand how it does what it does.

In other words:

.. pull-quote::

  Users should simply be able to drive the car without looking at the engine.

The good news is that `Highcharts (JS) <https://www.highcharts.com>`__ applies a very similar philosophy, and so that
makes the job for **Highcharts for Python** that much simpler.

*************************
Style Guide
*************************

Basic Conventions
======================

* Do not terminate lines with semicolons.
* Line length should have a maximum of *approximately* 90 characters. If in doubt,
  make a longer line or break the line between clear concepts.
* Each class should be contained in its own file.
* If a file runs longer than 2,000 lines...it should probably be refactored and
  split.
* All imports should occur at the top of the file - except where they *have* to occur
  inside a function/method to avoid circular imports or over-zealous soft dependency
  handling.

* Do not use single-line conditions:

  .. code-block:: python

    # GOOD
    if x:
      do_something()

    # BAD
    if x: do_something()

* When testing if an object has a value, be sure to use ``if x is None:`` or
  ``if x is not None``. Do **not** confuse this with ``if x:`` and ``if not x:``.
* Use the ``if x:`` construction for testing truthiness, and ``if not x:`` for
  testing falsiness. This is **different** from testing:

    * ``if x is True:``
    * ``if x is False:``
    * ``if x is None:``

* As of right now, we are using type annotations for function/method returns, but are not
  using type annotation for arguments consistently. This is because that would
  have a negative impact (we believe) on readability.

Naming Conventions
=======================

* ``variable_name`` and not ``variableName`` or ``VariableName``. Should be a
  noun that describes what information is contained in the variable. If a ``bool``,
  preface with ``is_`` or ``has_`` or similar question-word that can be answered
  with a yes-or-no.
* ``function_name`` and not ``function_name`` or ``functionName``. Should be an
  imperative that describes what the function does (e.g. ``get_next_page``).
* ``CONSTANT_NAME`` and not ``constant_name`` or ``ConstantName``.
* ``ClassName`` and not ``class_name`` or ``Class_Name``.

Basic Design Conventions
=============================

* Functions at the module level can only be aware of objects either at a higher
  scope or singletons (which effectively have a higher scope).
* Generally, functions and methods can use **one** positional argument (other than
  ``self`` or ``cls``) without a default value. Any other arguments must be keyword
  arguments with default value given.

  .. code-block:: python

    def do_some_function(argument):
      # rest of function...

    def do_some_function(first_arg,
                         second_arg = None,
                         third_arg = True):
      # rest of function ...

* Functions and methods that accept values should start by validating their
  input, throwing exceptions as appropriate.
* When defining a class, define all attributes in ``__init__``.
* When defining a class, start by defining its attributes and methods as private
  using a single-underscore prefix. Then, only once they're implemented, decide
  if they should be public.
* Don't be afraid of the private attribute/public property/public setter pattern:

  .. code-block:: python

    class SomeClass(object):
      def __init__(*args, **kwargs):
        self._private_attribute = None

      @property
      def private_attribute(self):
        # custom logic which  may override the default return

        return self._private_attribute

      @setter.private_attribute
      def private_attribute(self, value):
        # custom logic that creates modified_value

        self._private_attribute = modified_value

* Separate a function or method's final (or default) ``return`` from the rest of
  the code with a blank line (except for single-line functions/methods).
* Because `Highcharts JS <https://www.highcharts.com>`__ repeats many of the same properties and groups of properties,
  be sure to practice :iabbr:`DRY (Do Not Repeat Yourself)`. Use inheritance to your
  advantage, and don't be afraid of the :term:`diamond of death` inheritance problem.

  .. seealso::

    * :ref:`Multiple Inheritance in Highcharts for Python <multiple_inheritance>`

Documentation Conventions
==============================

We are very big believers in documentation (maybe you can tell). To document
**Highcharts for Python** we rely on several tools:

Sphinx
---------------

`Sphinx <https://www.sphinx-doc.org/>`__ is used to organize the library's documentation
into this lovely readable format (which is also published to `ReadTheDocs`_). This
documentation is written in `reStructuredText`_ files which are stored in
``<project>/docs``.

  .. tip::
    As a general rule of thumb, we try to apply the `ReadTheDocs`_ own
    `Documentation Style Guide`_ to our `RST <reStructuredText>`_ documentation.

.. hint::

  To build the HTML documentation locally:

  #. In a terminal, navigate to ``<project>/docs``.
  #. Execute ``make html``.

     .. caution::

       The **Highcharts for Python** documentation relies on
       `Graphviz <https://graphviz.org/>`_ to render class inheritance diagrams. While in
       most Linux environments this should just work assuming it is installed, on Windows
       you will likley to have to use a more robust command to generate the full docs
       locally:

         .. code-block:: bash

           $ sphinx-build -b html -D graphviz_dot="c:\Program Files\Graphviz\bin\dot.exe" . _build/html

       (and if necessary, adjust the location of ``dot.exe`` in your command)

  When built locally, the HTML output of the documentation will be available at
  ``./docs/_build/index.html``.


Docstrings
----------------

* Docstrings are used to document the actual source code itself. When
  writing docstrings we adhere to the conventions outlined in :pep:`257`.

.. _design_patterns:

***************************************************
Design Patterns and Standards
***************************************************

`Highcharts <https://www.highcharts.com>`__ is a large, robust, and complicated suite of 
JavaScript libraries. If in doubt, take a look at the extensive 
`documentation <https://www.highcharts.com/docs/index>`_ and in particular the 
`API reference <https://api.highcharts.com/highcharts>`_.  Because 
**Highcharts for Python** wraps the Highcharts Core API, its design is heavily shaped by 
Highcharts JS' own design - as one should expect.

However, one of the main goals of **Highcharts for Python** is to make the Highcharts JS
library a little more Pythonic to make it easier for Python developers to leverage it. 
Here are the notable design patterns that have been adopted that you should be aware of:

Code Style: Python vs JavaScript Naming Conventions
=======================================================

.. include:: using/_code_style_naming_conventions.rst

Standard Methods: :class:`HighchartsMeta <highcharts_core.metaclasses.HighchartsMeta>`
============================================================================================

Every single object supported by the Highcharts JS API corresponds to a Python class in
**Highcharts for Python**. You can find the complete list in our comprehensive
:doc:`Highcharts for Python API Reference <api>`.

These classes generally inherit from the :class:`HighchartsMeta` metaclass, which provides
each class with a number of standard methods. These methods are the "workhorses" of
**Highcharts for Python** and you will be relying heavily on them when using the library.
Thankfully, their signatures and behavior is generally consistent - even if what happens
"under the hood" is class-specific at times.

The standard methods exposed by the classes are:

Deserialization Methods
---------------------------

.. include:: api/_deserialization_methods.rst

Serialization Methods
--------------------------

.. include:: api/_serialization_methods.rst

Other Convenience Methods
------------------------------

.. include:: api/_other_convenience_methods.rst

Module Structure
=====================

.. include:: api/_module_structure.rst

Class Structures and Inheritance
====================================

.. include:: api/_class_structures.rst

.. _multiple_inheritance:

Multiple Inheritance, DRY and the Diamond of Death
------------------------------------------------------

  *Everything in moderation, including moderation.*
  -- Oscar Wilde

When contributing code to the **Highcharts for Python Toolkit**, it is important to
understand how we handle multiple inheritance and the :term:`diamond of death` problem.

First, obviously, multiple inheritance is generally considered an anti-pattern. That's
because it makes debugging code much, much harder - particuarly in Python, which uses a
bit of a "magic" secret sauce called the MRO (Method Resolution Order) to determine which
parent class' methods to execute and when.

However, `Highcharts <https://www.highcharts.com>`__ - and by consequence, 
**Highcharts for Python** - is very verbose. We estimate that the full set of 
objects across the full Python toolkit has about 15,000 properties in total. A great many 
of these properties are identical in terms of their syntax, and their meaning (in context). 
So this is a classic example of where we can apply the principle of 
:iabbr:`DRY (Don't Repeat Yourself)` to good effect. By using class inheritance, we can 
reduce the number of properties from about 15,000 to about 1,900. Not bad!

However, this significant reduction *does* require us to use multiple inheritance in some
cases, paritcularly in the :mod:`.options.series <highcharts_core.options.series>`
classes (which inherit from both the corresponding type-specific options in
:mod:`.options.plot_options <highcharts_core.options.plot_options>`) *and* from the
generic :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>` class).

To solve the :term:`diamond of death` problem, we implemented a number of private
helper methods to assist in navigating the MRO:

.. list-table::
  :widths: 30 70
  :header-rows: 1

  * - Method / Function
    - Purpose
  * - :func:`.utility_functions.get_remaining_mro() <highcharts_core.utility_functions.get_remaining_mro>`
    - Retrieve the class objects that are still to be traversed for a given class' MRO.
  * - :func:`.utility_functions.mro__to_untrimmed_dict() <highcharts_core.utility_functions.mro__to_untrimmed_dict>`
    - Retrieve a consolidated :term:`untrimmed` :class:`dict <python:dict>` representation
      from all ancestors of a given class.
  * - :meth:`HighchartsMeta._untrimmed_mro_ancestors() <highcharts_core.metaclasses.HighchartsMeta._untrimmed_mro_ancestors>`
    - Method which consolidates the results of
      :meth:`_to_untrimmed_dict() <highcharts_core.metaclasses.HighchartsMeta._to_untrimmed_dict>`
      from a given instance's parent class into a single :class:`dict <python:dict>`.
  * - :meth:`HighchartsMeta._to_untrimmed_dict() <highcharts_core.metaclasses.HighchartsMeta._to_untrimmed_dict>`
    - Generates an :term:`untrimmed` :class:`dict <python:dict>` representation of the
      instance at its lowest level in the class hierarchy. Think of this as the
      "bottom of the ladder", with other methods (notably
      :meth:`_untrimmed_mro_ancestors() <highcharts_core.metaclasses.HighchartsMeta._untrimmed_mro_ancestors>`)
      being used to generate corresponding :class:`dict <python:dict>` from other rungs on
      the ladder.

When working on classes in the library:

  #. First, check whether the class has multiple inheritance. The easiest way to do this
     is to check the class inheritance diagram in the
     :doc:`Highcharts Core for Python API Reference <api>`.
  #. Second, if a class you're working on has mulitple inheritance, be sure to use the
     special functions and methods above as appropriate.

     .. tip::

       **Best practice!**

       Look at how we've implemented the standard methods for other classes with
       multiple inheritance. That will give you a good pattern to follow.

--------------------------

.. _dependencies:

********************
Dependencies
********************

.. include:: _dependencies.rst

.. _preparing-development-environment:

**************************************************
Preparing Your Development Environment
**************************************************

In order to prepare your local development environment, you should:

#. Fork the `Git repository <https://github.com/highcharts-for-python/highcharts-core>`_.
#. Clone your forked repository.
#. Set up a virtual environment (optional).
#. Install development dependencies:

  .. code-block:: bash

    highcharts-core/ $ pip install -r requirements.dev.txt

And you should be good to go!

Ideas and Feature Requests
============================

Check for open `issues <https://github.com/highcharts-for-python/highcharts-core/issues>`_
or create a new issue to start a discussion around a bug or feature idea.

Testing
=========

If you've added a new feature, we recommend you:

  * create local unit tests to verify that your feature works as expected, and
  * run local unit tests before you submit the pull request to make sure nothing
    else got broken by accident.

.. seealso::

  For more information about the **Highcharts for Python** testing approach please
  see: :doc:`Testing Highcharts for Python <testing>`

Submitting Pull Requests
===========================

After you have made changes that you think are ready to be included in the main
library, submit a pull request on Github and one of our developers will review
your changes. If they're ready (meaning they're well documented, pass unit tests,
etc.) then they'll be merged back into the main repository and slated for inclusion
in the next release.

Building Documentation
=========================

In order to build documentation locally, you can do so from the command line using:

.. code-block:: bash

  highcharts-core/ $ cd docs
  highcharts-core/docs $ make html

.. caution::

  The **Highcharts for Python** documentation relies on
  `Graphviz <https://graphviz.org/>`_ to render class inheritance diagrams. While in
  most Linux environments this should just work assuming it is installed, on Windows
  you will likley to have to use a more robust command to generate the full docs
  locally:

    .. code-block:: bash

      $ sphinx-build -b html -D graphviz_dot="c:\Program Files\Graphviz\bin\dot.exe" . _build/html

  (and if necessary, adjust the location of ``dot.exe`` in your command)


When the build process has finished, the HTML documentation will be locally
available at:

  .. code-block:: bash

    highcharts-core/docs/_build/html/index.html

.. note::

  Built documentation (the HTML) is **not** included in the project's Git
  repository. If you need local documentation, you'll need to build it.

Contributors
================

Thanks to everyone who helps make **Highcharts for Python** useful:

.. include:: _contributors.rst


References
=============

.. target-notes::

.. _ReadTheDocs: https://readthedocs.org
.. _reStructuredText: http://www.sphinx-doc.org/en/stable/rest.html
.. _`Documentation Style Guide`: http://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html
.. _`talk given by Luciano Ramalho at PyCon 2016`: https://www.youtube.com/watch?v=k55d3ZUF3ZQ
