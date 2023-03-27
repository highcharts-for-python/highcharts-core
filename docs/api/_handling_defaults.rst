  *Explicit is better than implicit.*
  -- The Zen of Python

`Highcharts <https://www.highcharts.com/>`_ has a *lot* of default values. These
default values are generally applied if a JavaScript property is ``undefined`` (missing or
otherwise not specified), which is different from the JavaScript value of ``null``.

While our Pythonic instinct is to:

  * indicate those default values explicitly in the **Highcharts for Python** code as
    keyword argument defaults, and
  * return those default values in the serialized form of any **Highcharts for Python**
    objects

doing so would introduce a massive problem: It would bloat data transferred on the wire
*unnecessarily*.

The way that `Highcharts (JS) <https://www.highcharts.com>`__ handles defaults is an elegant
compromise between explicitness and the practical reality of making your code readable.
Why make a property explicit in a configuration string if you don't care about it? Purity
is only valuable to a point. And with thousands of properties across the
`Highcharts (JS) <https://www.highcharts.com>`__ suite, *nobody* wants to transmit or
maintain thousands of property configurations if it can be avoided.

For that reason, the **Highcharts for Python Toolkit** explicitly breaks Pythonic
convention: when an object's property returns :obj:`None <python:None>`, that has the
equivalent meaning of "Highcharts (JS) will apply the Highcharts default for this
property". These properties will *not* be serialized, either to a JS literal, nor to a
:class:`dict <python:dict>`, nor to JSON. This has the advantage of maintaining consistent
behavior with the `Highcharts (JS) <https://www.highcharts.com/>`__ suite while
still providing an internally consistent logic to follow.

.. note::

  There's an item on the **Highcharts for Python** :doc:`roadmap <../toolkit>` (:issue:`12`)
  to *optionally* surface defaults when explicitly requested. Not sure when it will be
  implemented, but we'll get there at some point.
