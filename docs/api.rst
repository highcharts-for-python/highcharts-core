########################################
Highcharts for Python API Reference
########################################

.. contents::
  :local:
  :depth: 3
  :backlinks: entry

------------------------

*****************************
API Design Patterns
*****************************

Code Style: Python vs JavaScript Naming Conventions
=======================================================

.. include:: using/_code_style_naming_conventions.rst

Standard Methods
=======================================

Every single object supported by the Highcharts JS API corresponds to a Python class in
**Highcharts for Python**. These classes generally inherit from the
:class:`HighchartsMeta <highcharts_python.metaclasses.HighchartsMeta>` metaclass, which
provides each class with a number of standard methods.

These methods are the "workhorses" of **Highcharts for Python** and you will be relying
heavily on them when using the library. Thankfully, their signatures and behavior is
generally consistent - even if what happens "under the hood" is class-specific at times.

.. _deserialization_methods:

Deserialization Methods
---------------------------

.. include:: api/_deserialization_methods.rst

.. _serialization_methods:

Serialization Methods
--------------------------

.. include:: api/_serialization_methods.rst

.. _other_methods:

Other Convenience Methods
------------------------------

.. include:: api/_other_convenience_methods.rst

Module Structure
=====================

.. include:: api/_module_structure.rst

Class Structures and Inheritance
====================================

.. include:: api/_class_structures.rst

.. _class_hierarchy:

Class Hierarchies
---------------------

.. todo::

  Prepare a series of class hierarchy diagrams.

--------------------------

.. _module_toc:

********************************
Core Components
********************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.chart <highcharts_python.chart>`
    - :class:`Chart <highcharts_python.chart.Chart>`
  * - :mod:`.global_options <highcharts_python.global_options>`
    -
  * - :mod:`.global_options.language <highcharts_python.global_options.language>`
    - :class:`Language <highcharts_python.global_options.language.Language>`
  * - :mod:`.global_options.language.accessibility <highcharts_python.global_options.language.accessibility>`
    - :class:`AccessibilityLanguageOptions <highcharts_python.global_options.language.accessibility.AccessibilityLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.announce_new_data <highcharts_python.global_options.language.accessibility.announce_new_data>`
    - :class:`AnnounceNewDataLanguageOptions <highcharts_python.global_options.language.accessibility.announce_new_data.AnnounceNewDataLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.axis <highcharts_python.global_options.language.accessibility.axis>`
    - :class:`AxisLanguageOptions <highcharts_python.global_options.language.accessibility.axis.AxisLanguageOptions>`
  * - :mod:`.chart_types <highcharts_python.global_options.language.accessibility.chart_types>`
    - :class:`ChartTypesLanguageOptions <highcharts_python.global_options.language.accessibility.chart_types.ChartTypesLanguageOptions>`
  * - :mod:`.exporting <highcharts_python.global_options.language.accessibility.exporting>`
    - :class:`ExportingLanguageOptions <highcharts_python.global_options.language.accessibility.exporting.ExportingLanguageOptions>`
  * - :mod:`.legend <highcharts_python.global_options.language.accessibility.legend>`
    - :class:`LegendLanguageOptions <highcharts_python.global_options.language.accessibility.legend.LegendLanguageOptions>`
  * - :mod:`.range_selector <highcharts_python.global_options.language.accessibility.range_selector>`
    - :class:`RangeSelectorLanguageOptions <highcharts_python.global_options.language.accessibility.range_selector.RangeSelectorLanguageOptions>`
  * - :mod:`.screen_reader_section <highcharts_python.global_options.language.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSectionLanguageOptions <highcharts_python.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionLanguageOptions>`
      :class:`ScreenReaderSectionAnnotationLanguage <highcharts_python.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionAnnotationLanguage>`
  * - :mod:`.series <highcharts_python.global_options.language.accessibility.series>`
    - :class:`SeriesLanguageOptions <highcharts_python.global_options.language.accessibility.series.SeriesLanguageOptions>`
      :class:`SeriesSummaryLanguageOptions <highcharts_python.global_options.language.accessibility.series.SeriesSummaryLanguageOptions>`
      :class:`SeriesTypeDescriptions <highcharts_python.global_options.language.accessibility.series.SeriesTypeDescriptions>`
  * - :mod:`.sonification <highcharts_python.global_options.language.accessibility.sonification>`
    - :class:`SonificationLanguageOptions <highcharts_python.global_options.language.accessibility.sonification.SonificationLanguageOptions>`
  * - :mod:`.table <highcharts_python.global_options.language.accessibility.table>`
    - :class:`TableLanguageOptions <highcharts_python.global_options.language.accessibility.table.TableLanguageOptions>`
  * - :mod:`.zoom <highcharts_python.global_options.language.accessibility.zoom>`
    - :class:`ZoomLanguageOptions <highcharts_python.global_options.language.accessibility.zoom.ZoomLanguageOptions>`
  * - :mod:`.global_options.language.export_data <highcharts_python.global_options.language.export_data>`
    - :class:`ExportDataLanguageOptions <highcharts_python.global_options.language.export_data.ExportDataLanguageOptions>`
  * - :mod:`.global_options.language.navigation <highcharts_python.global_options.language.navigation>`
    - :class:`NavigationLanguageOptions <highcharts_python.global_options.language.navigation.NavigationLanguageOptions>`
      :class:`PopupLanguageOptions <highcharts_python.global_options.language.navigation.PopupLanguageOptions>`
  * - :mod:`.global_options.shared_options <highcharts_python.global_options.shared_options>`
    - :class:`SharedOptions <highcharts_python.global_options.shared_options.SharedOptions>`
  * - :mod:`.headless_export <highcharts_python.headless_export>`
    - :class:`ExportServer <highcharts_python.headless_export.ExportServer>`
  * - :mod:`.options <highcharts_python.options>`
    - :class:`HighchartsOptions <highcharts_python.options.HighchartsOptions>`
      :class:`Options <highcharts_python.options.Options>`
  * - :mod:`.options.accessibility <highcharts_python.options.accessibility>`
    - :class:`Accessibility <highcharts_python.options.accessibility.Accessibility>`
      :class:`CustomAccessibilityComponents <highcharts_python.options.accessibility.CustomAccessibilityComponents>`
  * - :mod:`.options.accessibility.announce_new_data <highcharts_python.options.accessibility.announce_new_data>`
    - :class:`AnnounceNewData <highcharts_python.options.accessibility.announce_new_data.AnnounceNewData>`
  * - :mod:`.options.accessibility.keyboard_navigation <highcharts_python.options.accessibility.keyboard_navigation>`
    - :class:`KeyboardNavigation <highcharts_python.options.accessibility.keyboard_navigation.KeyboardNavigation>`
  * - :mod:`.options.accessibility.keyboard_navigation.focus_border <highcharts_python.options.accessibility.keyboard_navigation.focus_border>`
    - :class:`FocusBorder <highcharts_python.options.accessibility.keyboard_navigation.focus_border.FocusBorder>`
      :class:`FocusBorderStyle <highcharts_python.options.accessibility.keyboard_navigation.focus_border.FocusBorderStyle>`
  * - :mod:`.options.accessibility.keyboard_navigation.series_navigation <highcharts_python.options.accessibility.keyboard_navigation.series_navigation>`
    - :class:`SeriesNavigation <highcharts_python.options.accessibility.keyboard_navigation.series_navigation.SeriesNavigation>`
  * - :mod:`options.accessibility.point <highcharts_python.options.accessibility.point>`
    - :class:`AccessibilityPoint <highcharts_python.options.accessibility.point.AccessibilityPoint>`
  * - :mod:`options.accessibility.screen_reader_section <highcharts_python.options.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSection <highcharts_python.options.accessibility.screen_reader_section.ScreenReaderSection>`
  * - :mod:`options.accessibility.series <highcharts_python.options.accessibility.series>`
    - :class:`SeriesAccessibility <highcharts_python.options.accessibility.series.SeriesAccessibility>`
  * - :mod:`.options.annotations <highcharts_python.options.annotations>`
    -
  * - :mod:`.options.axes <highcharts_python.options.axes>`
    -
  * - :mod:`.options.boost <highcharts_python.options.boost>`
    -
  * - :mod:`.caption <highcharts_python.options.caption>`
    -
  * - :mod:`.options.chart <highcharts_python.options.chart>`
    -
  * - :mod:`.options.credits <highcharts_python.options.credits>`
    -
  * - :mod:`.options.data <highcharts_python.options.data>`
    -
  * - :mod:`.options.defs <highcharts_python.options.defs>`
    -
  * - :mod:`.options.drilldown <highcharts_python.options.drilldown>`
    -
  * - :mod:`.options.exporting <highcharts_python.options.exporting>`
    -
  * - :mod:`.options.legend <highcharts_python.options.legend>`
    -
  * - :mod:`.options.loading <highcharts_python.options.loading>`
    -
  * - :mod:`.options.navigation <highcharts_python.options.navigation>`
    -
  * - :mod:`.options.no_data <highcharts_python.options.no_data>`
    -
  * - :mod:`.options.pane <highcharts_python.options.pane>`
    -
  * - :mod:`.options.plot_options <highcharts_python.options.plot_options>`
    -
  * - :mod:`.options.responsive <highcharts_python.options.responsive>`
    -
  * - :mod:`.options.series <highcharts_python.options.series>`
    -
  * - :mod:`.options.subtitle <highcharts_python.options.subtitle>`
    -
  * - :mod:`.options.time <highcharts_python.options.time>`
    -
  * - :mod:`.options.title <highcharts_python.options.title>`
    -
  * - :mod:`.options.tooltips <highcharts_python.options.tooltips>`
    -
  * - :mod:`.utility_classes <highcharts_python.utility_classes>`
    -

.. toctree::
  :hidden:
  :titlesonly:

  api/chart
  api/global_options/index
  api/headless_export
  api/options/index
  api/utility_classes/index

*********************
Library Internals
*********************

.. todo::

  Add navigation for library internals.
