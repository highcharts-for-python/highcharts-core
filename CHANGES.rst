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
