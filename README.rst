####################################################
Highcharts for Python
####################################################

**Python Wrapper for Highcharts JS**

**Highcharts for Python** is a Python wrapper for the
`Highcharts <https://highcharts.com>`_ JS data visualization library. It is designed to
simplify management of `Highcharts <https://highcharts.com>`_ visualizations in Python
by providing a Python object representation of the Highcharts ``options`` configuration
and native integration with Pandas and PySpark.

**COMPLETE DOCUMENTATION:** http://highcharts-python.readthedocs.org/en/latest/index.html

.. contents::
 :depth: 3
 :backlinks: entry

--------------------

***************
Installation
***************

To install **Highcharts for Python**, just execute:

.. code:: bash

 $ pip install highcharts-python


Dependencies
==============

 * `Validator-Collection v1.5.0 <https://github.com/insightindustry/validator-collection>`_ or higher

-------------

************************************
Why Highcharts for Python?
************************************

When building professional-grade analytical applications, I've found
`Highcharts <https://highcharts.com>`_ to be one of the best visualization libraries out
there, providing excellent performance and extensive high-end animated, interactive data
visualization capabilities. However, `Highcharts <https://highcharts.com>`_ is
a pure JavaScript library that is primarily configured using a single JavaScript object
which can be inconvenient to manage within Python.

Lacking a Pythonic object representation of the Highcharts ``options`` configuration
object, developers are forced to manage Python `dict <python:dict>` objects that then
get serialized to JSON. This can be a pain, since it makes interaction across the
Python / JavaScript border (serializing to JSON, de-serializing from JSON) harder and
can make it less intuitive to manage the object's state.

This library is meant to fix that by providing a simple class representation of the
Highcharts ``options`` configuration object.
