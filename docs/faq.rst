################################
Frequently Asked Questions
################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

***********************
Getting Help
***********************

**Where can I get help using Highcharts Core for Python?**

This documentation is a great place to start, but we're here to help!

.. include:: _support.rst

-----------------

.. _faq_licensing:

***********************
Licensing
***********************

**Is Highcharts Core for Python free?**

If you are evaluating the **Highcharts for Python Toolkit**, you are welcome 
to install this library and use it free of charge. 

However, if you are using it for professional purposes - either to use 
Highcharts for your work, or to build an application that integrates the library - 
then you have to pay for both Highcharts Core (JS) itself *and* for your right 
to use the **Highcharts for Python Toolkit**. 

You can purchase licenses for both from Highsoft A/S at: 
`https://shop.highcharts.com/ <https://shop.highcharts.com>`__.

**How much does Highcharts for Python cost?**

As a paid add-on to the Highcharts JavaScript libraries, the 
**Highcharts for Python Toolkit** toolkit is priced at 30% of the price you pay 
for your Highcharts JavaScript license/support contract.

**How do I license the Highcharts for Python Toolkit?**

Licensing is super easy! You can go to 
`https://shop.highcharts.com <https://shop.highcharts.com>`__ and fill out the 
form, and that's it!

----------------------

******************************
Open Source
******************************

**Is Highcharts for Python open source?**

Yes. The **Highcharts for Python Toolkit** toolkit is open source (but not free - 
see :ref:`licensing <faq_licensing>` above).

You are welcome to review the source code for any library in the toolkit on 
`Github <https://github.com/highcharts-for-python>`__, including for 
`Highcharts Core for Python <https://github.com/highcharts-for-python/highcharts-core>`__.

**Can I fork the toolkit or a library in the toolkit?**

.. warning::

  Remember that if you fork the library and make modifications to the source code, that means that we will *not* be able to provide support or technical assistance for you should you run into trouble. So you will ultimately depend on
  forks at your own risk!

Yes. You are welcome to fork any of our repositories from `Github <https://github.com/highcharts-for-python>`__, 
provided that you adhere to the terms of our :doc:`license`.

.. tip::

  Bear in mind that if you fork the repository, that does not mean you are allowed to use it for professional purposes. Even if forked, you still need a license to do so. You can purchase a license `here <https://shop.highcharts.com>`__.

**Can I contribute to the Highcharts for Python Toolkit?**

Absolutely! We encourage contributions to the toolkit from the community! For more information, please read our :doc:`Contributor Guide <contributing>`.

-----------

******************************
Running into Issues
******************************

**In Jupyter Notebook, I keep getting an error that says "Something went wrong with the Highcharts.js script." What gives?**

This is a known issue affecting Jupyter Notebook users, but it can be caused by multiple different things:

*Network Connectivity*. When calling :meth:`Chart.display() <highcharts_core.chart.Chart.display>`, 
**Highcharts for Python** will attempt to load the required Highcharts (JS) JavaScript libraries into the
environment where where Jupyter Notebook is running. By default, **Highcharts for Python** tries for 5 seconds.
But if the relevant scripts have not (yet) loaded in 5 seconds, it will display an error. You can tell Jupyter
to wait longer by adjusting the ``retries`` and ``interval`` properties on the ``.display()`` method. For example:

  .. code-block:: python

    # To wait for 7 seconds
    my_chart.display(retries = 7, interval = 1000)

    # To wait for 10 seconds
    my_chart.display(retries = 10)

*Incorrect IPython, Jupyter Notebook, or Jupyter Lab versions*. Please be sure to check the versions of
IPython, Jupyter Notebook, and Jupyter Lab that you are using in your runtime environment. You can do this
by running:

  .. code-block:: bash

    $ pip list

  and then finding the entries for ``ipython``, ``notebook``, and ``jupyterlab``. Please check those versions 
  against our (soft) dependencies:

    .. include:: _dependencies.rst

If you are using older versions, you can upgrade it by executing:

  .. code-block:: bash

    $ pip install --upgrade ipython notebook jupyterlab

*VSCode Extension Conflict*. This is the most pernicious cause of this behavior. When you are running
Jupyter Notebook within VSCode *and* have various Jupyter Notebook-related extensions installed/enabled,
those extensions can *sometimes* cause this error. Unfortunately, it is not consistent, and the same
extensions in two different environments may or may not produce this behavior. However, users report that 
disabling those extensions, restarting VSCode, and then re-enabling
those extensions seems to solve that problem. However, to reproduce this *very* inconsistent error, we'd
appreciate if you could comment in `the relevant Github issue <https://github.com/highcharts-for-python/highcharts-core/issues/46>`__ to let us know which extensions you have installed when this problem occurs.

**I'm getting a Highcharts error about boost/turbo mode - what does that mean?**

Highcharts (JS) supports two similar features called "boost mode" and "turbo mode" that 
accelerate rendering of the visualization in your users' browsers. However, these modes 
work best when your chart's data is represented as a primitive array instead of as a full
object:

  .. list-table::
    :widths: 50 50
    :header-rows: 1

    * - Primitive Array
      - Full Object
    * - .. code-block:: python

          [
              [1, 23],
              [2, 34],
              [3, 45]
          ]
      - .. code-block:: python

          [
              {'x': 1, 'y': 23},
              {'x': 2, 'y': 34},
              {'x': 3, 'y': 45}
          ]

When rendering a chart whose data is contained in full objects, by default Highcharts (JS) disables
boost/turbo mode if there are more data points than a configurable threshold. You can adjust the thresholds
using various options, including :meth:`.turbo_threshold <highcharts_core.options.series.base.SeriesBase.turbo_threshold>`, 
:meth:`.boost_threshold <highcharts_core.options.series.base.SeriesBase.boost_threshold>` and the
configuration of chart-level :class:`Boost <highcharts_core.options.boost.Boost>` options.

  .. seealso::

    * Highcharts (JS) Documentation: `Boost module <https://www.highcharts.com/docs/advanced-chart-features/boost-module>`__
    * :class:`Boost <highcharts_core.options.boost.Boost>` options
    * Plot Options: :meth:`.boost_threshold <highcharts_core.options.plot_options.generic.GenericTypeOptions.turbo_threshold>`
    * Series Configuration: :meth:`.boost_threshold <highcharts_core.options.series.base.SeriesBase.boost_threshold>`
    * Series Configuration: :meth:`.turbo_threshold <highcharts_core.options.series.base.SeriesBase.turbo_threshold>`
