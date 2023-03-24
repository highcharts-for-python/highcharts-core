###############################################
Toolkit Components and Product Roadmap
###############################################

****************************
The Toolkit's Contents
****************************

The **Highcharts for Python Toolkit** features a number of separate Python
libraries which extend the core **Highcharts Core for Python** 
(``highcharts-core``) library. This pattern maps quite naturally to the 
Highcharts (JS) suite's JavaScript design, where multiple other modules 
extend the Highcharts Core JavaScript library.

The **Highcharts for Python Toolkit** includes two categories of tools:

.. tabs::

  .. tab:: Core Visualization Libraries

    These libraries correspond to each of the major Highcharts
    `products <https://www.highcharts.com/products/>`__:

    * **Highcharts Core for Python**: This is the foundational Python library, and is required
      by all other components in the toolkit. It provides the fundamental Python classes
      that are used throughout the toolkit, and importantly provides 100% coverage for the
      functionality in the
      `Highcharts Core <https://www.highcharts.com/products/highcharts>`__ JavaScript
      library.
    * **Highcharts Stock for Python**: This is the Python wrapper for the
      `Highcharts Stock <https://www.highcharts.com/products/stock>`__
      JavaScript library, which provides extensive visualizations for time series and
      stock price visualizations. For more details, please see the relevant
      `Highcharts Stock for Python documentation <https://stock-docs.highchartspython.com>`__
    * **Highcharts Maps for Python**: This is the Python wrapper for the
      `Highcharts Maps <https://www.highcharts.com/products/maps>`__
      JavaScript library, which provides rich geographic data visualization options
      with rich interactive maps. For more details, please see the relevant
      `Highcharts Maps for Python documentation <https://maps-docs.highchartspython.com>`__
    * **Highcharts Gantt for Python**: This is the Python wrapper for the
      `Highcharts Gantt <https://www.highcharts.com/products/gantt>`__
      JavaScript library, which provides rich Gantt charting capabilities to better visualize
      resource allocation and project sequences over time. For more details, please see the relevant
      `Highcharts Gantt for Python documentation <https://gantt-docs.highchartspython.com>`__


  .. tab:: Extensions

    These libraries serve as extensions to the core visualization libraries, providing
    specialized functionality to simplify usage of the **Highcharts for Python Toolkit** in various
    applications:

    .. note::

      A number of extension libraries are in progress, but have not yet been released. Watch this space for news soon!

    .. note::

      All extensions to the **Highcharts for Python Toolkit** support visualizations produced in any
      of the core libraries. For more information, please see :doc:`Supported Visualizations <visualizations>`.

------------

********************************
The Toolkit's Roadmap
********************************

There are a number of features (and in some cases complete components) slated for
development. While detailed write-ups of each feature can be found in the respective
project repositories, the lists below provides some high-level information.

.. tabs::

  .. tab:: Core Visualization Libraries

    * Needed Script Tags ( :issue:`12` ). It would be helpful for **Highcharts for Python**
      to support the production of the relevant ``<script/>`` tags needed to include the
      Highcharts JS modules that are needed to render a specific chart (and to *not*
      include the modules that are not needed).

      In addition, this functionality should support the specification of:

        * *custom* script locations for the relevant Highcharts (JS) modules as needed
        * version-locking the Highcharts (JS) script versions to load

    * Support for Explicit Defaults ( :issue:`13` ). Currently, Highcharts default values
      are always presented as :obj:`None <python:None>` in outputs within Python, and are
      stripped from the serialized JSON or JS literal representation of all objects
      (because that way the Highcharts JS library applies its default). While this is
      valuable to minimize irrelevant data and shrink content passed along the wire, it
      does force developers to track / remember / understand the Highcharts defaults
      (which are called out in the docs, obviously - but still...it's a pain). So in the
      Zen of Python spirit that "explicit is better than implicit", there needs to be a
      mechanism for users to *explicitly* request that default values are accessible in 
      Python and shown when serializing the chart configuration.
    * Styled Mode Configuration ( :issue:`14` ). While :term:`styled mode` can currently be
      enabled in **Highcharts for Python**, the library does not provide for the actual
      definition or configuration of Highcharts CSS. It would be good if it did, so that
      all Highcharts-related configuration could be handled within the library.

  .. tab:: Extensions

    * Watch this space...we'll be announcing some new extensions soon.

********************************
Additional Tools Needed?
********************************

Are you looking for additional tools that are not already part of the
**Highcharts for Python Toolkit**? Drop us a note with a feature request in our
`Github Issues Page <https://github.com/highcharts-for-python/highcharts-core/issues>`_.
