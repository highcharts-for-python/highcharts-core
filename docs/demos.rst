################################
Demos
################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

***********************************************
Trying the Highcharts for Python Toolkit
***********************************************

You are welcome to try the **Highcharts for Python** toolkit at your convenience and at no cost.
You can do so by installing the libraries you need very simple:

.. tabs::

  .. tab:: Highcharts Core for Python

    To install **Highcharts Core for Python**, just execute:

    .. code-block:: bash

      $ pip install highcharts-core

  .. tab:: Highcharts Stock for Python

    To install **Highcharts Stock for Python**, just execute:

    .. code-block:: bash

      $ pip install highcharts-stock

  .. tab:: Highcharts Maps for Python

    To install **Highcharts Maps for Python**, just execute:

    .. code-block:: bash

      $ pip install highcharts-maps

  .. tab:: Highcharts Gantt for Python

    To install **Highcharts Gantt for Python**, just execute:

    .. code-block:: bash

      $ pip install highcharts-gantt

If you are evaluating the **Highcharts for Python Toolkit**, you are welcome 
to install this library and use it free of charge. 

However, if you are using it for professional purposes - either to use 
Highcharts for your work, or to build an application that integrates the library - 
then you have to pay for both Highcharts Core (JS) itself *and* for your right 
to use the **Highcharts for Python Toolkit**. 

You can purchase licenses for both from Highsoft A/S at: 
`https://shop.highcharts.com/ <https://shop.highcharts.com>`__.

---------------

********************************************************
Demonstrating the Highcharts for Python Toolkit
********************************************************

We have prepared an extensive set of demos showcasing much of the code and
functionality of the **Highcharts for Python** toolkit. To see the demos in action,
we recommend that you click the following badge:

  .. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/highcharts-for-python/highcharts-for-python-demos/HEAD
    :alt: Binder: Highcharts for Python Demos

This will clone the `Highcharts for Python Demos <https://github.com/highcharts-for-python/highcharts-for-python-demos>`__
source repository within a Docker image, and launch `Jupyter Lab <https://jupyter.org>`__ within that
Docker container. This will then let you browse, edit, and run any of the Jupyter Notebooks contained
within the `Highcharts for Python Demos <https://github.com/highcharts-for-python/highcharts-for-python-demos>`__ repo.

How the Demos are Organized
==============================

.. sidebar::

  You should be aware that the demos use a variety of Highcharts for Python features, including various
  ways of de-serializing chart configurations. Some might load data from files, others might load them
  from ``snake_case`` :class:`dict <python:dict>`, others from ``camelCase`` Javascript Object Literal 
  Notation :class:`str <python:str>` values, and more.

  To see the full flexibility that the toolkit provides, we recommend reviewing several of the demos.

Once you have launched the Binder, you can browse the folders and Notebooks in the Jupyter Lab 
environment. You'll notice that the Jupyter Lab environment has one folder for each of the core
Highcharts for Python libraries, respectively: ``highcharts-core``, ``highcharts-stock``, 
``highcharts-maps``, and ``highcharts-gantt``. Within each of these folders, you will find sub-folders
labeled in a way to describe their contents. 

For example:

  * the sub-folder ``line-charts`` would contain various Notebooks that demonstrate the 
    generation of various Line Charts using the **Highcharts for Python** toolkit
  * the sub-folder ``python-features`` would contain various Notebooks that demonstrate
    the use of Python-specific features like the ``.from_pandas()`` convenience methods
  * etc.

Navigating the demos should be fairly intuitive - just pay attention to the folder names and the filenames of the Jupyter Notebooks.

Executing a Demo
===================

Once you are reviewing the demos, you can run a demo either by stepping through the cells in the Notebook, or 
by running all the cells in sequence.

------------------

*******************************
Running Demos Locally
*******************************

.. note::
  
  You can run the demos locally by following instructions in the 
  `Highcharts for Python Demos <https://github.com/highcharts-for-python/highcharts-for-python-demos>`__ Github repo's README.