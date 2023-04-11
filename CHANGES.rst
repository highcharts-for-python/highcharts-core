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
