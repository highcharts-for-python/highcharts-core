
Release 1.5.1
=========================================

* **BUGFIX:** Fixed bug in JS literal serialization that would misinterpret strings that 
  start with ``{``, end with ``}``, and contain a colon (``:``) as an object literal rather
  than as a string. (#130)

--------------------

Release 1.5.0
=========================================

* **ENHANCEMENT:** Align the API to **Highcharts (JS) v.11.2** (#127). In particular, this includes:

  * Added ``AxisEvents.point_break_out`` property.
  * Added ``.node_alignment`` property to ``SankeyOptions`` and ``SankeySeries``.
  * Added ``.link_color_mode`` property to ``SankeyOptions`` and ``SankeySeries``.
  * Added ``.inactive_other_points`` property to multiple series types.
  * Added ``.grouping`` property to Lollipop series type.
  * Added ``.low_marker`` property Area Range and Dumbell series types.
  * Added ``.show_export_in_progress`` and ``.export_in_progress`` support.
  * Added ``.drag`` annotation event support.
  
* **BUGFIX:** Fixed missing ``.levels`` support in ``TreegraphOptions`` and ``TreegraphSeries``.


--------------------

Release 1.4.3
=========================================

* **BUGFIX:** Fixed edge case error when deserializing ``ChartOptions`` using ``.from_dict()``
  with a ``dict`` that had been serialized using ``.to_dict()`` which errored on ``.margin`` 
  and ``.spacing`` (#124).

--------------------

Release 1.4.2
=========================================

* **BUGFIX:** Fixed location of the ``histogram.js`` module and ``bellcurve.js`` module to reflect
  latest changes in Highcharts (JS).

--------------------

Release 1.4.1
=========================================

* **BUGFIX:** Fixed handling of ``numpy.datetime64`` values in ``DataPointCollection``. (#118)

---------------------

Release 1.4.0
=========================================

* **MAJOR** performance gains in the ``.to_js_literal()`` method. Implementation seems to
  improve performance by 50 - 90%. (#51)
* *SIGNIFICANT* performance gains in the ``.to_json()`` method. Implementation seems to 
  improve performance by 30 - 90%.
* **ENHANCEMENT:** Significantly simplified use of the ``.from_pandas()`` method to support:

  * creation of multiple series from one DataFrame in one method call
  * creation of series without needing to specify a full property map
  * support for creating series by DataFrame row, rather than just by DataFrame column

* **ENHANCEMENT:** Added the ``.from_pandas_in_rows()`` method to support creation of
  charts and series from simple two-dimensional DataFrames laid out in rows.
* **ENHANCEMENT:** Added one-shot chart creation and rendering from Series objects (#89).
* **ENHANCEMENT:** Added one-shot chart creation using ``series`` and ``data``/``series_type`` keywords. (#90).
* **ENHANCEMENT:** Added ``.convert_to()`` convenience method to Series objects (#107).
* **ENHANCEMENT:** Added ``CallbackFunction.from_python()`` method which converts a Python function
  to its JavaScript equivalent using generative AI, with support for both OpenAI and Anthropic (#109).
* **BUGFIX:** Fixed instability issues in Jupyter Notebooks, both when operating as a Notebook (outside of 
  Jupyter Lab) and when saved to a static HTML file (#66).

--------------------

Release 1.3.7
=========================================

* **BUGFIX:** Fixed bug in ``HighchartsMeta.copy()`` (#98).
* **BUGFIX:** Fixed bug in data point serialization to primitive array.

---------------------

Release 1.3.6
=========================================

* **BUGFIX:** Adding missing ``menu...Style`` properties to `Navigation` class (#95).

---------------------

Release 1.3.5
=========================================

* **BUGFIX:** Fixed validation of style properties in the ``Legend`` class (#93).

---------------------


Release 1.3.4
=========================================

* **ENHANCEMENT:** Converted `ButtonTheme` into an extensible descendent of `JavaScriptDict` (#86).

---------------------

Release 1.3.3
=========================================

* **BUGFIX:** Added in a missing class extension for ``NavigationButtonConfiguration`` (#86).

---------------------

Release 1.3.2
=========================================

* **BUGFIX:** Fixed incorrect handling when defining a new ``Exporting.buttons`` context button under a different key name than ``contextButton``. (#84).

---------------------

Release 1.3.1
=========================================

* **BUGFIX:** Fixed incorrect ``style`` property deserialization in certain places (#82).

---------------------

Release 1.3.0
=========================================

* **ENHANCEMENT:** Modified the way that data points are serialized to JavaScript literal objects. Now, they are serialized to a JavaScript array if their configured properties are those that Highcharts (JS) supports in JavaScript array notation. Otherwise, the code falls back to serialize the data point as a JavaScript object literal. This change is intended to improve performance and reduce the size of the serialized data. (#77)
* **ENHANCEMENT:** Added ``__repr__()`` method for Highcharts Core for Python classes (#76).
* **ENHANCEMENT:** Added ``__str__()`` method with special handling for difficult-to-read classes (#76).
* **ENHANCEMENT:** Added ``Chart.get_script_tags()`` to retrieve Javascript ``<script>`` tags (#78).
* **ENHANCEMENT:** Added ``utility_functions.to_snake_case()`` function.
* **BUGFIX:** Fixed incorrect serialization of datetime and Pandas ``Timestamp`` objects in ``.to_dict()`` and ``.to_json()`` (#74).
* **BUGFIX:** Fixed incorrect serialization of ``EnforcedNull`` in ``.to_dict()`` and ``.to_json()`` (#75).

------------------

Release 1.2.6
=========================================

* **BUGFIX:** Fixed incorrect handling of an empty string in ``Annotation.draggable`` property (#71).

------------------

Release 1.2.5
=========================================

* **BUGFIX:** Fixed ``ExportServer`` handling of data relying on Pandas ``Timestamp`` instances.

------------------

Release 1.2.4
=========================================

* **BUGFIX:** Fixed ``.from_array()`` de-serialization to support propagation of string-type ``x`` values to ``name``(#67).

------------------

Release 1.2.3
=========================================

* **BUGFIX:** Fixed error when loading certain Highcharts (JS) scripts in Jupyter context.
* **ENHANCEMENT:** Increased the default timeout for ``Chart.download_chart()`` and related.

------------------

Release 1.2.2
=========================================

* **BUGFIX:** Fixed behavior where ``Chart.download_chart(format = 'svg')`` was incorrectly returning a PNG rather than an SVG ( #63 ).

------------------

Release 1.2.1
=========================================

* **ENHANCEMENT:** Added autoconversion of ``plotLine.value`` from ``datetime.datetime`` to POSIX timestamp (#58).
* **BUGFIX:** Fixed incorrect ``datetime`` serialization to SECONDS from Unix epoch. Now serializing to JS-compatible MILLISECONDS from Unix epoch (#61).

------------------

Release 1.2.0
=========================================

* **ENHANCEMENT:** Align the API to **Highcharts (JS) v.11.1** (#52). In particular, this includes:

  * Added ``AccessibilityPoint.description_format`` property.
  * Added support for ``.legend_symbol`` to plot options and series options.
  * Added ``.border_radius`` support to ``FunnelOptions`` and ``FunnelSeries``.
  * Added ``.interpolation`` support to ``HeatmapOptions`` and descendents.
  * Added ``.point_description_format`` support to ``SeriesOptions`` and descendents.
  * Added ``.fill_space`` support to ``TreegraphOptions`` and descendents.
  * Added ``.crossing`` support to axes.
  * Added ``.format`` support to ``Tooltip``.

* **ENHANCEMENT:** Added support for the inclusion of scripts based on features used in the chart (#12).
* **ENHANCEMENT:** Added ``dict`` support to ``.style`` property on labels and titles.
* **DOCS:** Various documentation updates and fixes.
* **DEPENDENCY:** Bumped ``requests`` version for security patch.

------------------

Release 1.1.1
=========================================

* **FIXED:** Problem when producing a JS literal, with the JS code inserting an unnecessary ``new`` (#42 and #43).
* **ENHANCEMENT:** Added more elegant error handling when something goes wrong displaying a chart in Jupyter (#43).

-------------

Release 1.1.0
=========================================

* Align the API to **Highcharts (JS) v.11**. In particular, this includes:

  * Updating documentation for ``options.chart.ChartOptions.styled_mode`` to align
    to new v11 design changes.
  * Updated documentation for ``options.series.data.base.DataBase.color_index`` to align to
    new v11 design changes.
  * Added new ``utility_classes.data_labels.SunburstDataLabel`` class to patch missing
    data label ``.rotation_mode`` property.
  * Updated ``options.plot_options.SunburstOptions.data_labels`` to accept ``SunburstDataLabel``
    values.
  * Updated documentation of ``options.axes.labels.AxisLabelOptions.distance`` to reflect new (or 
    newly-documented) behavior.
  * Added new ``utility_classes.data_labels.OrganizationDataLabel`` class to patch misisng data label ``.
    link_text_path`` property.
  * Updated ``options.plot_options.organization.OrganizationOptions.data_labels`` to accept ``OrganizationDataLabel``
    values.
  * Added ``.description_format`` property to ``options.plot_options.accessibility.TypeOptionsAccessibility``.
  * Added ``PictorialOptions`` / ``PictorialSeries`` series type with related classes.
  * Added ``.minor_ticks_per_major`` to ``options.axes.x_axis.XAxisOptions``.
  * Added ``.stack_shadow`` to ``options.axes.y_axis.YAxisOptions``.
  * Added ``.border_radius`` to ``ColumnRangeOptions`` / ``ColumnRangeSeries``.
  * Added ``.play_as_sand`` and ``.download_midi`` to ``global_options.language.Language``.
  * Added ``.border_radius`` to ``PieOptions`` / ``PieSeries``.
  * Added ``.style`` to ``utility_classes.buttons.CollapseButtonConfiguration``.
  * Added ``utility_classes.events.SimulationEvents`` and modified ``NetworkGraphOptions`` to support.
  * Added ``options.sonification`` and all related classes.
  * Added series-level ``SeriesSonification`` to all series.

* **FIXED:** Broken heatmap and tilemap documentation links.
* **FIXED:** Fixed missing ``TreegraphOptions`` / ``TreegraphSeries`` series type.

-------------------------------

Release 1.0.2
=========================================

* **DOCUMENTATION:** Added documentation of hard dependencies to the README (issue #37).

-----------------------

Release 1.0.1
=========================================

* **BUGFIX**: Fixed a bug encountered when parsing CSV data (issue #32).
* **ENHANCEMENT**: Added a catch for when trying to set ``Chart.options`` to a ``SharedOptions`` instance (issue #34).
* Fixed a broken link in the documentation.

---------------

Release 1.0.0
=========================================

* **First official release!**

---------------

Release 1.0.0-rc9
=========================================

* Added demos to documentation.

---------------

Release 1.0.0-rc8
=========================================

* **BUG:** #25. Fixed the edge case where if multiple notebooks are open in Jupyter Labs and
  different notebooks use the same container, the charts get rendered in *one* container.
* **BUG:** Fixed bug when serializing a string value equal to ``'Date'``.
* **BUG:** Fixed boolean handling in ``options.legend.LegendOptions.shadow``.
* **Enhancement:** Added ``.from_array()`` support to the ``decorators.validate_types()`` function.
* **BUG:** Fixed data valization in ``options.plot_options.pie.PieOptions.end_angle`` and ``.start_angle``.
* Added ``date`` and ``datetime`` support to axis min and max.
* Added iterable support to ``.from_dict()`` method.

---------------

Release 1.0.0-rc7
=========================================

* Further tweaks to documentation CSS for better accessibility.

---------------

Release 1.0.0-rc6
=========================================

* Added CSS overrides to documentation for better accessibility.
* Added jQuery to documentation to address issue in Sphinx 6.0 and Sphinx RTD Theme.

---------------

Release 1.0.0-rc5
=========================================

* Bug fixes to Jupyter Labs rendering.
* Bug fix for timestamp serialization of timezone-naive ``datetime`` objects.
* Bug fix: typo in Plot Bands serialization.
* Added null support to color validation.
* Bug fix in ``style`` deserialization.
* Bug fix in ``CartesianData.from_array()``.
* Fixed ``NaN`` handling in ``.load_from_pandas()``.
* Fixed JSON deserialization in ``.from_array()``.
* Added support for stylesheet links in Jupyter Labs context.
* Several bug fixes in JS literal serialization.
* Major improvements to JavaScript module inclusion.

---------------

Release 1.0.0-rc4
=========================================

* Revised the documentation.

---------------

Release 1.0.0-rc3
=========================================

* Revised the documentation.

---------------

Release 1.0.0-rc2
=========================================

* Closed #18. Fixed bug where loading data from a Pandas Dataframe could produce data points with None values.
* Added ``HighchartsPandasDeserializationError`` and ``HighchartsPySparkDeserializationError``.

---------------

Release 1.0.0-rc1
=========================================

* First public release: **Release Candidate 1**
