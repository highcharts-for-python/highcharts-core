**Highcharts for Python** objects re-use many of the same properties. This is one of the 
strengths of the Highcharts API, in that it is internally consistent and that behavior 
configured on one object should be readily transferrable to a second object provided it 
shares the same properties. However, Highcharts has a *lot* of properties. We estimate 
that the ``options.plotOptions`` objects and their sub-properties have close to 3,000
properties. But because they are heavily repeated, those 3,000 or so properties can be
reduced to only 421 unique property names. That's almost an 85% reduction.

:iabbr:`DRY (Don't Repeat Yourself)` is an important principle in software development.
Can you imagine propagating changes in seven places (on average) in your code? That would
be a maintenance nightmare! And it is exactly the kind of maintenance nightmare that class
inheritance was designed to fix.

For that reason, the **Highcharts for Python Toolkit** classes have a deeply nested
inheritance structure. This is important to understand both for evaluating
:func:`isinstance() <python:isinstance>` checks in your code, or for understanding how to
further subclass Highcharts for Python components.

  .. seealso::

    For more details, please review the :doc:`API documentation <../api>`, in particular
    the class inheritance diagrams included for each documented class.
