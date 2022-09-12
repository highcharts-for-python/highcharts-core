###############################################
Toolkit Components and Product Roadmap
###############################################

****************************
The Toolkit's Contents
****************************

The **Highcharts for Python** toolkit features a number of separate Python
libraries which extend the core **Highcharts for Python** (``highcharts-python``) library.
This pattern actually maps quite naturally to the Highcharts JS design, where multiple
other modules extend the core Highcharts JS library.

The **Highcharts for Python** toolkit includes two categories of tools:

.. tabs::

  .. tab:: Core Visualization Libraries

    These libraries correspond to each of the major Highcharts
    `products <https://www.highcharts.com/blog/products/>`_:

    * **Highcharts for Python**: This is the foundational Python library, and is required
      by all other components in the toolkit. It provides the fundamental Python classes
      that are used throughout the toolkit, and importantly provides 100% coverage for the
      functionality in the
      `Highcharts JS <https://www.highcharts.com/blog/products/#highcharts>`_ JavaScript
      library.
    * **Highcharts Stock for Python**: This is the Python wrapper for the
      `Highcharts Stock <https://www.highcharts.com/blog/products/#highcharts-stock>`_
      JavaScript library, which provides extensive visualizations for time series and
      stock price visualizations. For more details, please see the relevant
      `Highcharts Stock for Python documentation <https://highcharts-stock-python.readthedocs.io>`_
    * **Highcharts Maps for Python**: This is the Python wrapper for the
      `Highcharts Maps <https://www.highcharts.com/blog/products/#highcharts-maps>`_
      JavaScript library, which provides extensive geographic data visualization options
      with rich interactive maps. For more details, please see the relevant
      `Highcharts Maps for Python documentation <https://highcharts-maps-python.readthedocs.io>`_

  .. tab:: Extensions

    These libraries serve as extensions to the core visualization libraries, providing
    specialized functionality to simplify usage of **Highcharts for Python** in various
    applications:

    .. note::

      The libraries below are in-progress, but have not yet been released.

    * **Highcharts Gantt for Python**: This is the Python wrapper for the
      `Highcharts Gantt <https://www.highcharts.com/blog/products/#highcharts>`_
      JavaScript library, which provides rich visualizations for resource allocation over
      time. For more details, please see the relevant
      `Highcharts Gantt for Python documentation <https://highcharts-gantt-python.readthedocs.io>`_
    * **Highcharts for Dash**: This is a set of components for the
      `Dash <https://dash.plotly.com/>`_ data visualization framework which makes it easy
      to use Highcharts visualizations in your Dash dashboards. For more details, please
      see the relevant `Highcharts for Dash documentation <https://highcharts-dash.readthedocs.io>`_.
    * **Flask-Highcharts**: This is an extension to the Flask microframework which makes
      integrating Highcharts visualizations into Flask views super simple. For more
      details, please see the relevant
      `Flask-Highcharts documentation <https://flask-highcharts.readthedocs.io>`_.
    * **Highcharts for Django**: This is an extension to the Django web framework which
      makes utilizing Highcharts visualizations in your Django application super simple.
      For more details, please see the
      `Highcharts for Django documentation <https://highcharts-django.readthedocs.io>`_.

    .. note::

      All extensions to **Highcharts for Python** support visualizations produced in any
      of the core libraries.

------------

********************************
The Toolkit's Roadmap
********************************

There are a number of features (and in some cases complete components) slated for
development. While detailed write-ups of each feature can be found in the respective
project project repo, the lists below provides some high-level information.

.. tabs::

  .. tab:: Core Visualization Libraries

    * Support for Explicit Defaults ( :issue:`1` ). Currently, Highcharts default values
      are always presented as :obj:`None <python:None>` in outputs within Python, and are
      stripped from the serialized JSON or JS literal representation of all objects
      (because that way the Highcharts JS library applies its default). While this is
      valuable to minimize irrelevant data and shrink content passed along the wire, it
      does force developers to track / remember / understand the Highcharts defaults
      (which are called out in the docs, obviously - but still...it's a pain). So in the
      Zen of Python spirit that "explicit is better than implicit", there needs to be a
      mechanism for users of the library to *explicitly* request that default values are
      accessible in Python and shown when serializing the chart configuration.
    * Needed Script Tags ( :issue:`2` ). It would be helpful for **Highcharts for Python**
      to support the production of the relevant ``<script/>`` tags needed to include the
      Highcharts JS modules that are needed to render a specific chart (and to *not*
      include the modules that are not needed).

  .. tab:: Extensions

    * Implement and release **Highcharts for Dash** ( :issue:`3` ).
    * Implement and release **Flask-Highcharts** ( :issue:`4` ).
    * Implement and release **Highcharts for Django** ( :issue:`5` ).

********************************
Additional Tools Needed?
********************************

Are you looking for additional tools that are not already part of the
**Highcharts for Python** toolkit? Drop us a note with a feature request in our
`Github Issues Page <https://github.com/hcpllc/highcharts-python/issues>`_.
