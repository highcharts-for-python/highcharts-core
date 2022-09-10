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
