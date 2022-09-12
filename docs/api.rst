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
    - :class:`Annotation <highcharts_python.options.annotations.Annotation>`
  * - :mod:`.options.annotations.animation <highcharts_python.options.annotations.animation>`
    - :class:`AnnotationAnimation <highcharts_python.options.annotations.animation.AnnotationAnimation>`
  * - :mod:`.options.annotations.control_point_options <highcharts_python.options.annotations.control_point_options>`
    - :class:`AnnotationControlPointOption <highcharts_python.options.annotations.control_point_options.AnnotationControlPointOption>`
  * - :mod:`.options.annotations.events <highcharts_python.options.annotations.events>`
    - :class:`AnnotationEvent <highcharts_python.options.annotations.events.AnnotationEvent>`
  * - :mod:`.options.annotations.label_options <highcharts_python.options.annotations.label_options>`
    - :class:`AnnotationLabel <highcharts_python.options.annotations.label_options.AnnotationLabel>`
      :class:`AnnotationLabelOptionAccessibility <highcharts_python.options.annotations.label_options.AnnotationLabelOptionAccessibility>`
      :class:`LabelOptions <highcharts_python.options.annotations.label_options.LabelOptions>`
  * - :mod:`.options.annotations.options.annotations.points <highcharts_python.options.annotations.points>`
    - :class:`AnnotationPoint <highcharts_python.options.annotations.points.AnnotationPoint>`
  * - :mod:`.options.annotations.shape_options <highcharts_python.options.annotations.shape_options>`
    - :class:`AnnotationShape <highcharts_python.options.annotations.shape_options.AnnotationShape>`
      :class:`ShapeOptions <highcharts_python.options.annotations.shape_options.ShapeOptions>`
  * - :mod:`.options.axes <highcharts_python.options.axes>`
    -
  * - :mod:`.options.axes.accessibility <highcharts_python.options.axes.accessibility>`
    - :class:`AxisAccessibility <highcharts_python.options.axes.accessibility.AxisAccessibility>`
  * - :mod:`.options.axes.breaks <highcharts_python.options.axes.breaks>`
    - :class:`AxisBreak <highcharts_python.options.axes.breaks.AxisBreak>`
  * - :mod:`.options.axes.color_axis <highcharts_python.options.axes.color_axis>`
    - :class:`ColorAxis <highcharts_python.options.axes.color_axis.ColorAxis>`
  * - :mod:`.options.axes.crosshair <highcharts_python.options.axes.crosshair>`
    - :class:`CrosshairOptions <highcharts_python.options.axes.crosshair.CrosshairOptions>`
  * - :mod:`.options.axes.data_classes <highcharts_python.options.axes.data_classes>`
    - :class:`DataClass <highcharts_python.options.axes.data_classes.DataClass>`
  * - :mod:`.options.axes.generic <highcharts_python.options.axes.generic>`
    - :class:`GenericAxis <highcharts_python.options.axes.generic.GenericAxis>`
  * - :mod:`.options.axes.labels <highcharts_python.options.axes.labels>`
    - :class:`AxisLabelOptions <highcharts_python.options.axes.labels.AxisLabelOptions>`
      :class:`PlotBandLabel <highcharts_python.options.axes.labels.PlotBandLabel>`
      :class:`PlotLineLabel <highcharts_python.options.axes.labels.PlotLineLabel>`
  * - :mod:`.options.axes.markers <highcharts_python.options.axes.markers>`
    - :class:`AxisMarker <highcharts_python.options.axes.markers.AxisMarker>`
  * - :mod:`.options.axes.numeric <highcharts_python.options.axes.numeric>`
    - :class:`NumericAxis <highcharts_python.options.axes.numeric.NumericAxis>`
  * - :mod:`.options.axes.parallel_axes <highcharts_python.options.axes.parallel_axes>`
    - :class:`ParallelAxesOptions <highcharts_python.options.axes.parallel_axes.ParallelAxesOptions>`
  * - :mod:`.options.axes.plot_bands <highcharts_python.options.axes.plot_bands>`
    - :class:`PlotBand <highcharts_python.options.axes.plot_bands.PlotBand>`
      :class:`PlotLine <highcharts_python.options.axes.plot_bands.PlotLine>`
  * - :mod:`.options.axes.title <highcharts_python.options.axes.title>`
    - :class:`AxisTitle <highcharts_python.options.axes.title.AxisTitle>`
  * - :mod:`.options.axes.x_axis <highcharts_python.options.axes.x_axis>`
    - :class:`XAxis <highcharts_python.options.axes.x_axis.XAxis>`
  * - :mod:`.options.axes.y_axis <highcharts_python.options.axes.y_axis>`
    - :class:`YAxis <highcharts_python.options.axes.y_axis.YAxis>`
  * - :mod:`.options.axes.z_axis <highcharts_python.options.axes.z_axis>`
    - :class:`ZAxis <highcharts_python.options.axes.z_axis.ZAxis>`
  * - :mod:`.options.boost <highcharts_python.options.boost>`
    - :class:`Boost <highcharts_python.options.boost.Boost>`
      :class:`BoostDebug <highcharts_python.options.boost.BoostDebug>`
  * - :mod:`.options.caption <highcharts_python.options.caption>`
    - :class:`Caption <highcharts_python.options.caption.Caption>`
  * - :mod:`.options.chart <highcharts_python.options.chart>`
    - :class:`ChartOptions <highcharts_python.options.chart.ChartOptions>`
      :class:`PanningOptions <highcharts_python.options.chart.PanningOptions>`
  * - :mod:`.options_3d <highcharts_python.options.chart.options_3d>`
    - :class:`Options3D <highcharts_python.options.chart.options_3d.Options3D>`
      :class:`Frame <highcharts_python.options.chart.options_3d.Frame>`
      :class:`PanelOptions <highcharts_python.options.chart.options_3d.PanelOptions>`
  * - :mod:`.reset_zoom_button <highcharts_python.options.chart.reset_zoom_button>`
    - :class:`ResetZoomButtonOptions <highcharts_python.options.chart.reset_zoom_button.ResetZoomButtonOptions>`
  * - :mod:`.scrollable_plot_area <highcharts_python.options.chart.scrollable_plot_area>`
    - :class:`ScrollablePlotArea <highcharts_python.options.chart.scrollable_plot_area.ScrollablePlotArea>`
  * - :mod:`.options.credits <highcharts_python.options.credits>`
    - :class:`Credits <highcharts_python.options.credits.Credits>`
      :class:`CreditStyleOptions <highcharts_python.options.credits.CreditStyleOptions>`
  * - :mod:`.options.data <highcharts_python.options.data>`
    - :class:`Data <highcharts_python.options.data.Data>`
  * - :mod:`.options.defs <highcharts_python.options.defs>`
    - :class:`MarkerDefinition <highcharts_python.options.defs.MarkerDefinition>`
      :class:`MarkerASTNode <highcharts_python.options.defs.MarkerASTNode>`
      :class:`MarkerAttributeObject <highcharts_python.options.defs.MarkerAttributeObject>`
  * - :mod:`.options.drilldown <highcharts_python.options.drilldown>`
    - :class:`Drilldown <highcharts_python.options.drilldown.Drilldown>`
  * - :mod:`.options.exporting <highcharts_python.options.exporting>`
    - :class:`Exporting <highcharts_python.options.exporting.Exporting>`
      :class:`ExportingAccessibilityOptions <highcharts_python.options.exporting.ExportingAccessibilityOptions>`
  * - :mod:`.options.exporting.csv <highcharts_python.options.exporting.csv>`
    - :class:`ExportingCSV <highcharts_python.options.exporting.csv.ExportingCSV>`
      :class:`CSVAnnotationOptions <highcharts_python.options.exporting.csv.CSVAnnotationOptions>`
  * - :mod:`.options.exporting.exporting.pdf_font <highcharts_python.options.exporting.pdf_font>`
    - :class:`PDFFontOptions <highcharts_python.options.exporting.pdf_font.PDFFontOptions>`
  * - :mod:`.options.legend <highcharts_python.options.legend>`
    - :class:`Legend <highcharts_python.options.legend.Legend>`
  * - :mod:`.options.legend.accessibility <highcharts_python.options.legend.accessibility>`
    - :class:`LegendAccessibilityOptions <highcharts_python.options.legend.accessibility.LegendAccessibilityOptions>`
      :class:`LegendKeyboardNavigation <highcharts_python.options.legend.accessibility.LegendKeyboardNavigation>`
  * - :mod:`.options.legend.bubble_legend <highcharts_python.options.legend.bubble_legend>`
    - :class:`BubbleLegend <highcharts_python.options.legend.bubble_legend.BubbleLegend>`
      :class:`BubbleLegendRange <highcharts_python.options.legend.bubble_legend.BubbleLegendRange>`
      :class:`BubbleLegendLabelOptions <highcharts_python.options.legend.bubble_legend.BubbleLegendLabelOptions>`
  * - :mod:`.options.legend.navigation <highcharts_python.options.legend.navigation>`
    - :class:`LegendNavigation <highcharts_python.options.legend.navigation.LegendNavigation>`
  * - :mod:`.options.legend.title <highcharts_python.options.legend.title>`
    - :class:`LegendTitle <highcharts_python.options.legend.title.LegendTitle>`
  * - :mod:`.options.loading <highcharts_python.options.loading>`
    - :class:`Loading <highcharts_python.options.loading.Loading>`
  * - :mod:`.options.navigation <highcharts_python.options.navigation>`
    - :class:`Navigation <highcharts_python.options.navigation.Navigation>`
  * - :mod:`.bindings <highcharts_python.options.navigation.bindings>`
    - :class:`Bindings <highcharts_python.options.navigation.bindings.Bindings>`
      :class:`RectangleAnnotationBinding <highcharts_python.options.navigation.bindings.RectangleAnnotationBinding>`
      :class:`LabelAnnotationBinding <highcharts_python.options.navigation.bindings.LabelAnnotationBinding>`
      :class:`EllipseAnnotationBinding <highcharts_python.options.navigation.bindings.EllipseAnnotationBinding>`
      :class:`CircleAnnotationBinding <highcharts_python.options.navigation.bindings.CircleAnnotationBinding>`
      :class:`Binding <highcharts_python.options.navigation.bindings.Binding>`
  * - :mod:`.options.no_data <highcharts_python.options.no_data>`
    - :class:`NoData <highcharts_python.options.no_data.NoData>`
  * - :mod:`.options.pane <highcharts_python.options.pane>`
    - :class:`Pane <highcharts_python.options.pane.Pane>`
      :class:`PaneBackground <highcharts_python.options.pane.PaneBackground>`
  * - :mod:`.options.plot_options <highcharts_python.options.plot_options>`
    -
  * - :mod:`.options.responsive <highcharts_python.options.responsive>`
    - :class:`Responsive <highcharts_python.options.responsive.Responsive>`
      :class:`ResponsiveRules <highcharts_python.options.responsive.ResponsiveRules>`
      :class:`Condition <highcharts_python.options.responsive.Condition>`
  * - :mod:`.options.series <highcharts_python.options.series>`
    -
  * - :mod:`.options.subtitle <highcharts_python.options.subtitle>`
    - :class:`Subtitle <highcharts_python.options.subtitle.Subtitle>`
  * - :mod:`.options.time <highcharts_python.options.time>`
    - :class:`Time <highcharts_python.options.time.Time>`
  * - :mod:`.options.title <highcharts_python.options.title>`
    -
  * - :mod:`.options.tooltips <highcharts_python.options.tooltips>`
    - :class:`Tooltip <highcharts_python.options.tooltips.Tooltip>`
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
