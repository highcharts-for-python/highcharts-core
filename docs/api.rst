###########################################
Highcharts Core for Python API Reference
###########################################

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

Every single object supported by the
`Highcharts Core JavaScript API <https://api.highcharts.com/highcharts/>`__ corresponds to a Python
class in **Highcharts Core for Python**. These classes generally inherit from the
:class:`HighchartsMeta <highcharts_core.metaclasses.HighchartsMeta>` metaclass, which
provides each class with a number of standard methods.

These methods are the "workhorses" of the **Highcharts for Python Toolkit** and you will be relying
heavily on them when using the library. Thankfully, their signatures and behavior is
generally consistent - even if what happens "under the hood" is class-specific at times.

Deserialization Methods
---------------------------

.. include:: api/_deserialization_methods.rst

Serialization Methods
--------------------------

.. include:: api/_serialization_methods.rst

Other Convenience Methods
------------------------------

.. include:: api/_other_convenience_methods.rst

Handling Default Values
===============================

.. include:: api/_handling_defaults.rst


Module Structure
=====================

.. include:: api/_module_structure.rst

Class Structures and Inheritance
====================================

.. include:: api/_class_structures.rst

.. warning::

  Certain sections of the **Highcharts for Python Toolkit** - in particular the
  :mod:`options.series <highcharts_core.options.series>` classes - rely heavily on
  multiple inheritance. This is a known anti-pattern in Python development as it runs the
  risk of encountering the :term:`diamond of death` inheritance problem. This complicates
  the process of inheriting methods or properties from parent classes when properties or
  methods share names across multiple parents.

  We know this the diamond of death is an anti-pattern, but it was a necessary one to 
  minimize code duplication and maximize consistency. For that reason, we implemented it 
  properly *despite* the anti-pattern, using some advanced Python concepts to navigate the 
  Python MRO (Method Resolution Order) system cleanly. However, an awareness of the pattern 
  used may prove helpful if your code inherits from the Highcharts for Python classes.

  .. seealso::

    For a more in-depth discussion of how the anti-pattern was implemented safely and
    reliably, please review the :doc:`Contributor Guidelines <contributing>`.

--------------------------

.. _core_components:

********************************
Core Components
********************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.chart <highcharts_core.chart>`
    - :class:`Chart <highcharts_core.chart.Chart>`
  * - :mod:`.global_options <highcharts_core.global_options>`
    -
  * - :mod:`.global_options.language <highcharts_core.global_options.language>`
    - :class:`Language <highcharts_core.global_options.language.Language>`
  * - :mod:`.global_options.language.accessibility <highcharts_core.global_options.language.accessibility>`
    - :class:`AccessibilityLanguageOptions <highcharts_core.global_options.language.accessibility.AccessibilityLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.announce_new_data <highcharts_core.global_options.language.accessibility.announce_new_data>`
    - :class:`AnnounceNewDataLanguageOptions <highcharts_core.global_options.language.accessibility.announce_new_data.AnnounceNewDataLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.axis <highcharts_core.global_options.language.accessibility.axis>`
    - :class:`AxisLanguageOptions <highcharts_core.global_options.language.accessibility.axis.AxisLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.chart_types <highcharts_core.global_options.language.accessibility.chart_types>`
    - :class:`ChartTypesLanguageOptions <highcharts_core.global_options.language.accessibility.chart_types.ChartTypesLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.exporting <highcharts_core.global_options.language.accessibility.exporting>`
    - :class:`ExportingLanguageOptions <highcharts_core.global_options.language.accessibility.exporting.ExportingLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.legend <highcharts_core.global_options.language.accessibility.legend>`
    - :class:`LegendLanguageOptions <highcharts_core.global_options.language.accessibility.legend.LegendLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.range_selector <highcharts_core.global_options.language.accessibility.range_selector>`
    - :class:`RangeSelectorLanguageOptions <highcharts_core.global_options.language.accessibility.range_selector.RangeSelectorLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.screen_reader_section <highcharts_core.global_options.language.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSectionLanguageOptions <highcharts_core.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionLanguageOptions>`
      :class:`ScreenReaderSectionAnnotationLanguage <highcharts_core.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionAnnotationLanguage>`
  * - :mod:`.global_options.language.accessibility.series <highcharts_core.global_options.language.accessibility.series>`
    - :class:`SeriesLanguageOptions <highcharts_core.global_options.language.accessibility.series.SeriesLanguageOptions>`
      :class:`SeriesSummaryLanguageOptions <highcharts_core.global_options.language.accessibility.series.SeriesSummaryLanguageOptions>`
      :class:`SeriesTypeDescriptions <highcharts_core.global_options.language.accessibility.series.SeriesTypeDescriptions>`
  * - :mod:`.global_options.language.accessibility.sonification <highcharts_core.global_options.language.accessibility.sonification>`
    - :class:`SonificationLanguageOptions <highcharts_core.global_options.language.accessibility.sonification.SonificationLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.table <highcharts_core.global_options.language.accessibility.table>`
    - :class:`TableLanguageOptions <highcharts_core.global_options.language.accessibility.table.TableLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.zoom <highcharts_core.global_options.language.accessibility.zoom>`
    - :class:`ZoomLanguageOptions <highcharts_core.global_options.language.accessibility.zoom.ZoomLanguageOptions>`
  * - :mod:`.global_options.language.export_data <highcharts_core.global_options.language.export_data>`
    - :class:`ExportDataLanguageOptions <highcharts_core.global_options.language.export_data.ExportDataLanguageOptions>`
  * - :mod:`.global_options.language.navigation <highcharts_core.global_options.language.navigation>`
    - :class:`NavigationLanguageOptions <highcharts_core.global_options.language.navigation.NavigationLanguageOptions>`
      :class:`PopupLanguageOptions <highcharts_core.global_options.language.navigation.PopupLanguageOptions>`
  * - :mod:`.global_options.shared_options <highcharts_core.global_options.shared_options>`
    - :class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`
  * - :mod:`.headless_export <highcharts_core.headless_export>`
    - :class:`ExportServer <highcharts_core.headless_export.ExportServer>`
  * - :mod:`.highcharts <highcharts_core.highcharts>`
    - (most classes from across the rest of the API)
  * - :mod:`.options <highcharts_core.options>`
    - :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
      :class:`Options <highcharts_core.options.Options>`
  * - :mod:`.options.accessibility <highcharts_core.options.accessibility>`
    - :class:`Accessibility <highcharts_core.options.accessibility.Accessibility>`
      :class:`CustomAccessibilityComponents <highcharts_core.options.accessibility.CustomAccessibilityComponents>`
  * - :mod:`.options.accessibility.announce_new_data <highcharts_core.options.accessibility.announce_new_data>`
    - :class:`AnnounceNewData <highcharts_core.options.accessibility.announce_new_data.AnnounceNewData>`
  * - :mod:`.options.accessibility.keyboard_navigation <highcharts_core.options.accessibility.keyboard_navigation>`
    - :class:`KeyboardNavigation <highcharts_core.options.accessibility.keyboard_navigation.KeyboardNavigation>`
  * - :mod:`.options.accessibility.keyboard_navigation.focus_border <highcharts_core.options.accessibility.keyboard_navigation.focus_border>`
    - :class:`FocusBorder <highcharts_core.options.accessibility.keyboard_navigation.focus_border.FocusBorder>`
      :class:`FocusBorderStyle <highcharts_core.options.accessibility.keyboard_navigation.focus_border.FocusBorderStyle>`
  * - :mod:`.options.accessibility.keyboard_navigation.series_navigation <highcharts_core.options.accessibility.keyboard_navigation.series_navigation>`
    - :class:`SeriesNavigation <highcharts_core.options.accessibility.keyboard_navigation.series_navigation.SeriesNavigation>`
  * - :mod:`options.accessibility.point <highcharts_core.options.accessibility.point>`
    - :class:`AccessibilityPoint <highcharts_core.options.accessibility.point.AccessibilityPoint>`
  * - :mod:`options.accessibility.screen_reader_section <highcharts_core.options.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSection <highcharts_core.options.accessibility.screen_reader_section.ScreenReaderSection>`
  * - :mod:`options.accessibility.series <highcharts_core.options.accessibility.series>`
    - :class:`SeriesAccessibility <highcharts_core.options.accessibility.series.SeriesAccessibility>`
  * - :mod:`.options.annotations <highcharts_core.options.annotations>`
    - :class:`Annotation <highcharts_core.options.annotations.Annotation>`
  * - :mod:`.options.annotations.animation <highcharts_core.options.annotations.animation>`
    - :class:`AnnotationAnimation <highcharts_core.options.annotations.animation.AnnotationAnimation>`
  * - :mod:`.options.annotations.control_point_options <highcharts_core.options.annotations.control_point_options>`
    - :class:`AnnotationControlPointOption <highcharts_core.options.annotations.control_point_options.AnnotationControlPointOption>`
  * - :mod:`.options.annotations.events <highcharts_core.options.annotations.events>`
    - :class:`AnnotationEvent <highcharts_core.options.annotations.events.AnnotationEvent>`
  * - :mod:`.options.annotations.label_options <highcharts_core.options.annotations.label_options>`
    - :class:`AnnotationLabel <highcharts_core.options.annotations.label_options.AnnotationLabel>`
      :class:`AnnotationLabelOptionAccessibility <highcharts_core.options.annotations.label_options.AnnotationLabelOptionAccessibility>`
      :class:`LabelOptions <highcharts_core.options.annotations.label_options.LabelOptions>`
  * - :mod:`.options.annotations.options.annotations.points <highcharts_core.options.annotations.points>`
    - :class:`AnnotationPoint <highcharts_core.options.annotations.points.AnnotationPoint>`
  * - :mod:`.options.annotations.shape_options <highcharts_core.options.annotations.shape_options>`
    - :class:`AnnotationShape <highcharts_core.options.annotations.shape_options.AnnotationShape>`
      :class:`ShapeOptions <highcharts_core.options.annotations.shape_options.ShapeOptions>`
  * - :mod:`.options.axes <highcharts_core.options.axes>`
    -
  * - :mod:`.options.axes.accessibility <highcharts_core.options.axes.accessibility>`
    - :class:`AxisAccessibility <highcharts_core.options.axes.accessibility.AxisAccessibility>`
  * - :mod:`.options.axes.breaks <highcharts_core.options.axes.breaks>`
    - :class:`AxisBreak <highcharts_core.options.axes.breaks.AxisBreak>`
  * - :mod:`.options.axes.color_axis <highcharts_core.options.axes.color_axis>`
    - :class:`ColorAxis <highcharts_core.options.axes.color_axis.ColorAxis>`
  * - :mod:`.options.axes.crosshair <highcharts_core.options.axes.crosshair>`
    - :class:`CrosshairOptions <highcharts_core.options.axes.crosshair.CrosshairOptions>`
  * - :mod:`.options.axes.data_classes <highcharts_core.options.axes.data_classes>`
    - :class:`DataClass <highcharts_core.options.axes.data_classes.DataClass>`
  * - :mod:`.options.axes.generic <highcharts_core.options.axes.generic>`
    - :class:`GenericAxis <highcharts_core.options.axes.generic.GenericAxis>`
  * - :mod:`.options.axes.labels <highcharts_core.options.axes.labels>`
    - :class:`AxisLabelOptions <highcharts_core.options.axes.labels.AxisLabelOptions>`
      :class:`PlotBandLabel <highcharts_core.options.axes.labels.PlotBandLabel>`
      :class:`PlotLineLabel <highcharts_core.options.axes.labels.PlotLineLabel>`
  * - :mod:`.options.axes.markers <highcharts_core.options.axes.markers>`
    - :class:`AxisMarker <highcharts_core.options.axes.markers.AxisMarker>`
  * - :mod:`.options.axes.numeric <highcharts_core.options.axes.numeric>`
    - :class:`NumericAxis <highcharts_core.options.axes.numeric.NumericAxis>`
  * - :mod:`.options.axes.parallel_axes <highcharts_core.options.axes.parallel_axes>`
    - :class:`ParallelAxesOptions <highcharts_core.options.axes.parallel_axes.ParallelAxesOptions>`
  * - :mod:`.options.axes.plot_bands <highcharts_core.options.axes.plot_bands>`
    - :class:`PlotBand <highcharts_core.options.axes.plot_bands.PlotBand>`
      :class:`PlotLine <highcharts_core.options.axes.plot_bands.PlotLine>`
  * - :mod:`.options.axes.title <highcharts_core.options.axes.title>`
    - :class:`AxisTitle <highcharts_core.options.axes.title.AxisTitle>`
  * - :mod:`.options.axes.x_axis <highcharts_core.options.axes.x_axis>`
    - :class:`XAxis <highcharts_core.options.axes.x_axis.XAxis>`
  * - :mod:`.options.axes.y_axis <highcharts_core.options.axes.y_axis>`
    - :class:`YAxis <highcharts_core.options.axes.y_axis.YAxis>`
      :class:`StackShadow <highcharts_core.options.axes.y_axis.StackShadow>`
  * - :mod:`.options.axes.z_axis <highcharts_core.options.axes.z_axis>`
    - :class:`ZAxis <highcharts_core.options.axes.z_axis.ZAxis>`
  * - :mod:`.options.boost <highcharts_core.options.boost>`
    - :class:`Boost <highcharts_core.options.boost.Boost>`
      :class:`BoostDebug <highcharts_core.options.boost.BoostDebug>`
  * - :mod:`.options.caption <highcharts_core.options.caption>`
    - :class:`Caption <highcharts_core.options.caption.Caption>`
  * - :mod:`.options.chart <highcharts_core.options.chart>`
    - :class:`ChartOptions <highcharts_core.options.chart.ChartOptions>`
      :class:`PanningOptions <highcharts_core.options.chart.PanningOptions>`
  * - :mod:`.options.chart.options_3d <highcharts_core.options.chart.options_3d>`
    - :class:`Options3D <highcharts_core.options.chart.options_3d.Options3D>`
      :class:`Frame <highcharts_core.options.chart.options_3d.Frame>`
      :class:`PanelOptions <highcharts_core.options.chart.options_3d.PanelOptions>`
  * - :mod:`.options.chart.reset_zoom_button <highcharts_core.options.chart.reset_zoom_button>`
    - :class:`ResetZoomButtonOptions <highcharts_core.options.chart.reset_zoom_button.ResetZoomButtonOptions>`
  * - :mod:`.options.chart.scrollable_plot_area <highcharts_core.options.chart.scrollable_plot_area>`
    - :class:`ScrollablePlotArea <highcharts_core.options.chart.scrollable_plot_area.ScrollablePlotArea>`
  * - :mod:`.options.chart.zooming <highcharts_core.options.chart.zooming>`
    - :class:`ZoomingOptions <highcharts_core.options.chart.zooming.ZoomingOptions>`
      :class:`MouseWheelOptions <highcharts_core.options.chart.zooming.MouseWheelOptions>`
  * - :mod:`.options.credits <highcharts_core.options.credits>`
    - :class:`Credits <highcharts_core.options.credits.Credits>`
      :class:`CreditStyleOptions <highcharts_core.options.credits.CreditStyleOptions>`
  * - :mod:`.options.data <highcharts_core.options.data>`
    - :class:`Data <highcharts_core.options.data.Data>`
  * - :mod:`.options.defs <highcharts_core.options.defs>`
    - :class:`MarkerDefinition <highcharts_core.options.defs.MarkerDefinition>`
      :class:`MarkerASTNode <highcharts_core.options.defs.MarkerASTNode>`
      :class:`MarkerAttributeObject <highcharts_core.options.defs.MarkerAttributeObject>`
  * - :mod:`.options.drilldown <highcharts_core.options.drilldown>`
    - :class:`Drilldown <highcharts_core.options.drilldown.Drilldown>`
  * - :mod:`.options.exporting <highcharts_core.options.exporting>`
    - :class:`Exporting <highcharts_core.options.exporting.Exporting>`
      :class:`ExportingAccessibilityOptions <highcharts_core.options.exporting.ExportingAccessibilityOptions>`
  * - :mod:`.options.exporting.csv <highcharts_core.options.exporting.csv>`
    - :class:`ExportingCSV <highcharts_core.options.exporting.csv.ExportingCSV>`
      :class:`CSVAnnotationOptions <highcharts_core.options.exporting.csv.CSVAnnotationOptions>`
  * - :mod:`.options.exporting.exporting.pdf_font <highcharts_core.options.exporting.pdf_font>`
    - :class:`PDFFontOptions <highcharts_core.options.exporting.pdf_font.PDFFontOptions>`
  * - :mod:`.options.legend <highcharts_core.options.legend>`
    - :class:`Legend <highcharts_core.options.legend.Legend>`
  * - :mod:`.options.legend.accessibility <highcharts_core.options.legend.accessibility>`
    - :class:`LegendAccessibilityOptions <highcharts_core.options.legend.accessibility.LegendAccessibilityOptions>`
      :class:`LegendKeyboardNavigation <highcharts_core.options.legend.accessibility.LegendKeyboardNavigation>`
  * - :mod:`.options.legend.bubble_legend <highcharts_core.options.legend.bubble_legend>`
    - :class:`BubbleLegend <highcharts_core.options.legend.bubble_legend.BubbleLegend>`
      :class:`BubbleLegendRange <highcharts_core.options.legend.bubble_legend.BubbleLegendRange>`
      :class:`BubbleLegendLabelOptions <highcharts_core.options.legend.bubble_legend.BubbleLegendLabelOptions>`
  * - :mod:`.options.legend.navigation <highcharts_core.options.legend.navigation>`
    - :class:`LegendNavigation <highcharts_core.options.legend.navigation.LegendNavigation>`
  * - :mod:`.options.legend.title <highcharts_core.options.legend.title>`
    - :class:`LegendTitle <highcharts_core.options.legend.title.LegendTitle>`
  * - :mod:`.options.loading <highcharts_core.options.loading>`
    - :class:`Loading <highcharts_core.options.loading.Loading>`
  * - :mod:`.options.navigation <highcharts_core.options.navigation>`
    - :class:`Navigation <highcharts_core.options.navigation.Navigation>`
  * - :mod:`.options.navigation.bindings <highcharts_core.options.navigation.bindings>`
    - :class:`Bindings <highcharts_core.options.navigation.bindings.Bindings>`
      :class:`RectangleAnnotationBinding <highcharts_core.options.navigation.bindings.RectangleAnnotationBinding>`
      :class:`LabelAnnotationBinding <highcharts_core.options.navigation.bindings.LabelAnnotationBinding>`
      :class:`EllipseAnnotationBinding <highcharts_core.options.navigation.bindings.EllipseAnnotationBinding>`
      :class:`CircleAnnotationBinding <highcharts_core.options.navigation.bindings.CircleAnnotationBinding>`
      :class:`Binding <highcharts_core.options.navigation.bindings.Binding>`
  * - :mod:`.options.no_data <highcharts_core.options.no_data>`
    - :class:`NoData <highcharts_core.options.no_data.NoData>`
  * - :mod:`.options.pane <highcharts_core.options.pane>`
    - :class:`Pane <highcharts_core.options.pane.Pane>`
      :class:`PaneBackground <highcharts_core.options.pane.PaneBackground>`
  * - :mod:`.options.plot_options <highcharts_core.options.plot_options>`
    - :class:`PlotOptions <highcharts_core.options.plot_options.PlotOptions>`
  * - :mod:`.options.plot_options.accessibility <highcharts_core.options.plot_options.accessibility>`
    - :class:`TypeOptionsAccessibility <highcharts_core.options.plot_options.accessibility.TypeOptionsAccessibility>`
      :class:`SeriesKeyboardNavigation <highcharts_core.options.plot_options.accessibility.SeriesKeyboardNavigation>`
  * - :mod:`.options.plot_options.arcdiagram <highcharts_core.options.plot_options.arcdiagram>`
    - :class:`ArcDiagramOptions <highcharts_core.options.plot_options.arcdiagram.ArcDiagramOptions>`
  * - :mod:`.options.plot_options.area <highcharts_core.options.plot_options.area>`
    - :class:`AreaOptions <highcharts_core.options.plot_options.area.AreaOptions>`
      :class:`AreaRangeOptions <highcharts_core.options.plot_options.area.AreaRangeOptions>`
      :class:`AreaSplineOptions <highcharts_core.options.plot_options.area.AreaSplineOptions>`
      :class:`AreaSplineRangeOptions <highcharts_core.options.plot_options.area.AreaSplineRangeOptions>`
      :class:`LineOptions <highcharts_core.options.plot_options.area.LineOptions>`
      :class:`StreamGraphOptions <highcharts_core.options.plot_options.area.StreamGraphOptions>`
  * - :mod:`.options.plot_options.bar <highcharts_core.options.plot_options.bar>`
    - :class:`BarOptions <highcharts_core.options.plot_options.bar.BarOptions>`
      :class:`ColumnOptions <highcharts_core.options.plot_options.bar.ColumnOptions>`
      :class:`ColumnPyramidOptions <highcharts_core.options.plot_options.bar.ColumnPyramidOptions>`
      :class:`ColumnRangeOptions <highcharts_core.options.plot_options.bar.ColumnRangeOptions>`
      :class:`CylinderOptions <highcharts_core.options.plot_options.bar.CylinderOptions>`
      :class:`VariwideOptions <highcharts_core.options.plot_options.bar.VariwideOptions>`
      :class:`WaterfallOptions <highcharts_core.options.plot_options.bar.WaterfallOptions>`
      :class:`WindBarbOptions <highcharts_core.options.plot_options.bar.WindBarbOptions>`
      :class:`XRangeOptions <highcharts_core.options.plot_options.bar.XRangeOptions>`
      :class:`BaseBarOptions <highcharts_core.options.plot_options.bar.BaseBarOptions>`
  * - :mod:`.options.plot_options.bellcurve <highcharts_core.options.plot_options.bellcurve>`
    - :class:`BellCurveOptions <highcharts_core.options.plot_options.bellcurve.BellCurveOptions>`
  * - :mod:`.options.plot_options.boxplot <highcharts_core.options.plot_options.boxplot>`
    - :class:`BoxPlotOptions <highcharts_core.options.plot_options.boxplot.BoxPlotOptions>`
      :class:`ErrorBarOptions <highcharts_core.options.plot_options.boxplot.ErrorBarOptions>`
  * - :mod:`.options.plot_options.bubble <highcharts_core.options.plot_options.bubble>`
    - :class:`BubbleOptions <highcharts_core.options.plot_options.bubble.BubbleOptions>`
  * - :mod:`.options.plot_options.bullet <highcharts_core.options.plot_options.bullet>`
    - :class:`BulletOptions <highcharts_core.options.plot_options.bullet.BulletOptions>`
      :class:`TargetOptions <highcharts_core.options.plot_options.bullet.TargetOptions>`
  * - :mod:`.options.plot_options.data_sorting <highcharts_core.options.plot_options.data_sorting>`
    - :class:`DataSorting <highcharts_core.options.plot_options.data_sorting.DataSorting>`
  * - :mod:`.options.plot_options.dependencywheel <highcharts_core.options.plot_options.dependencywheel>`
    - :class:`DependencyWheelOptions <highcharts_core.options.plot_options.dependencywheel.DependencyWheelOptions>`
  * - :mod:`.options.plot_options.drag_drop <highcharts_core.options.plot_options.drag_drop>`
    - :class:`DragDropOptions <highcharts_core.options.plot_options.drag_drop.DragDropOptions>`
      :class:`HighLowDragDropOptions <highcharts_core.options.plot_options.drag_drop.HighLowDragDropOptions>`
      :class:`BoxPlotDragDropOptions <highcharts_core.options.plot_options.drag_drop.BoxPlotDragDropOptions>`
      :class:`BulletDragDropOptions <highcharts_core.options.plot_options.drag_drop.BulletDragDropOptions>`
      :class:`GuideBox <highcharts_core.options.plot_options.drag_drop.GuideBox>`
      :class:`GuideBoxOptions <highcharts_core.options.plot_options.drag_drop.GuideBoxOptions>`
      :class:`DragHandle <highcharts_core.options.plot_options.drag_drop.DragHandle>`
  * - :mod:`.options.plot_options.dumbbell <highcharts_core.options.plot_options.dumbbell>`
    - :class:`DumbbellOptions <highcharts_core.options.plot_options.dumbbell.DumbbellOptions>`
      :class:`LollipopOptions <highcharts_core.options.plot_options.dumbbell.LollipopOptions>`
  * - :mod:`.options.plot_options.funnel <highcharts_core.options.plot_options.funnel>`
    - :class:`FunnelOptions <highcharts_core.options.plot_options.funnel.FunnelOptions>`
      :class:`Funnel3DOptions <highcharts_core.options.plot_options.funnel.Funnel3DOptions>`
  * - :mod:`.options.plot_options.gauge <highcharts_core.options.plot_options.gauge>`
    - :class:`GaugeOptions <highcharts_core.options.plot_options.gauge.GaugeOptions>`
      :class:`SolidGaugeOptions <highcharts_core.options.plot_options.gauge.SolidGaugeOptions>`
  * - :mod:`.options.plot_options.generic <highcharts_core.options.plot_options.generic>`
    - :class:`GenericTypeOptions <highcharts_core.options.plot_options.generic.GenericTypeOptions>`
  * - :mod:`.options.plot_options.heatmap <highcharts_core.options.plot_options.heatmap>`
    - :class:`HeatmapOptions <highcharts_core.options.plot_options.heatmap.HeatmapOptions>`
      :class:`TilemapOptions <highcharts_core.options.plot_options.heatmap.TilemapOptions>`
  * - :mod:`.options.plot_options.histogram <highcharts_core.options.plot_options.histogram>`
    - :class:`HistogramOptions <highcharts_core.options.plot_options.histogram.HistogramOptions>`
  * - :mod:`.options.plot_options.item <highcharts_core.options.plot_options.item>`
    - :class:`ItemOptions <highcharts_core.options.plot_options.item.ItemOptions>`
  * - :mod:`.options.plot_options.levels <highcharts_core.options.plot_options.levels>`
    - :class:`LevelOptions <highcharts_core.options.plot_options.levels.LevelOptions>`
      :class:`SunburstLevelOptions <highcharts_core.options.plot_options.levels.SunburstLevelOptions>`
      :class:`TreemapLevelOptions <highcharts_core.options.plot_options.levels.TreemapLevelOptions>`
      :class:`LevelSize <highcharts_core.options.plot_options.levels.LevelSize>`
      :class:`ColorVariation <highcharts_core.options.plot_options.levels.ColorVariation>`
      :class:`BaseLevelOptions <highcharts_core.options.plot_options.levels.BaseLevelOptions>`
  * - :mod:`.options.plot_options.link <highcharts_core.options.plot_options.link>`
    - :class:`LinkOptions <highcharts_core.options.plot_options.link.LinkOptions>`
  * - :mod:`.options.plot_options.networkgraph <highcharts_core.options.plot_options.networkgraph>`
    - :class:`NetworkGraphOptions <highcharts_core.options.plot_options.networkgraph.NetworkGraphOptions>`
      :class:`LayoutAlgorithm <highcharts_core.options.plot_options.networkgraph.LayoutAlgorithm>`
  * - :mod:`.options.plot_options.organization <highcharts_core.options.plot_options.organization>`
    - :class:`OrganizationOptions <highcharts_core.options.plot_options.organization.OrganizationOptions>`
  * - :mod:`.options.plot_options.packedbubble <highcharts_core.options.plot_options.packedbubble>`
    - :class:`PackedBubbleOptions <highcharts_core.options.plot_options.packedbubble.PackedBubbleOptions>`
      :class:`ParentNodeOptions <highcharts_core.options.plot_options.packedbubble.ParentNodeOptions>`
  * - :mod:`.options.plot_options.pareto <highcharts_core.options.plot_options.pareto>`
    - :class:`ParetoOptions <highcharts_core.options.plot_options.pareto.ParetoOptions>`
  * - :mod:`.options.plot_options.pictorial <highcharts_core.options.plot_options.pictorial>`
    - :class:`PictorialOptions <highcharts_core.options.plot_options.pictorial.PictorialOptions>`
  * - :mod:`.options.plot_options.pie <highcharts_core.options.plot_options.pie>`
    - :class:`PieOptions <highcharts_core.options.plot_options.pie.PieOptions>`
      :class:`VariablePieOptions <highcharts_core.options.plot_options.pie.VariablePieOptions>`
  * - :mod:`.options.plot_options.points <highcharts_core.options.plot_options.points>`
    - :class:`Point <highcharts_core.options.plot_options.points.Point>`
      :class:`OnPointOptions <highcharts_core.options.plot_options.points.OnPointOptions>`
      :class:`ConnectorOptions <highcharts_core.options.plot_options.points.ConnectorOptions>`
  * - :mod:`.options.plot_options.polygon <highcharts_core.options.plot_options.polygon>`
    - :class:`PolygonOptions <highcharts_core.options.plot_options.polygon.PolygonOptions>`
  * - :mod:`.options.plot_options.pyramid <highcharts_core.options.plot_options.pyramid>`
    - :class:`PyramidOptions <highcharts_core.options.plot_options.pyramid.PyramidOptions>`
      :class:`Pyramid3DOptions <highcharts_core.options.plot_options.pyramid.Pyramid3DOptions>`
  * - :mod:`.options.plot_options.sankey <highcharts_core.options.plot_options.sankey>`
    - :class:`SankeyOptions <highcharts_core.options.plot_options.sankey.SankeyOptions>`
  * - :mod:`.options.plot_options.scatter <highcharts_core.options.plot_options.scatter>`
    - :class:`ScatterOptions <highcharts_core.options.plot_options.scatter.ScatterOptions>`
      :class:`Scatter3DOptions <highcharts_core.options.plot_options.scatter.Scatter3DOptions>`
  * - :mod:`.options.plot_options.series <highcharts_core.options.plot_options.series>`
    - :class:`SeriesOptions <highcharts_core.options.plot_options.series.SeriesOptions>`
  * - :mod:`.options.plot_options.sonification <highcharts_core.options.plot_options.sonification>`
    - :class:`SeriesSonification <highcharts_core.options.plot_options.sonification.SeriesSonification>`
  * - :mod:`.options.plot_options.spline <highcharts_core.options.plot_options.spline>`
    - :class:`SplineOptions <highcharts_core.options.plot_options.spline.SplineOptions>`
  * - :mod:`.options.plot_options.sunburst <highcharts_core.options.plot_options.sunburst>`
    - :class:`SunburstOptions <highcharts_core.options.plot_options.sunburst.SunburstOptions>`
  * - :mod:`.options.plot_options.timeline <highcharts_core.options.plot_options.timeline>`
    - :class:`TimelineOptions <highcharts_core.options.plot_options.timeline.TimelineOptions>`
  * - :mod:`.options.plot_options.treegraph <highcharts_core.options.plot_options.treegraph>`
    - :class:`TreegraphOptions <highcharts_core.options.plot_options.treegraph.TreegraphOptions>`
      :class:`TreegraphEvents <highcharts_core.options.plot_options.treegraph.TreegraphEvents>`
  * - :mod:`.options.plot_options.treemap <highcharts_core.options.plot_options.treemap>`
    - :class:`TreemapOptions <highcharts_core.options.plot_options.treemap.TreemapOptions>`
  * - :mod:`.options.plot_options.vector <highcharts_core.options.plot_options.vector>`
    - :class:`VectorOptions <highcharts_core.options.plot_options.vector.VectorOptions>`
  * - :mod:`.options.plot_options.venn <highcharts_core.options.plot_options.venn>`
    - :class:`VennOptions <highcharts_core.options.plot_options.venn.VennOptions>`
  * - :mod:`.options.plot_options.wordcloud <highcharts_core.options.plot_options.wordcloud>`
    - :class:`WordcloudOptions <highcharts_core.options.plot_options.wordcloud.WordcloudOptions>`
      :class:`RotationOptions <highcharts_core.options.plot_options.wordcloud.RotationOptions>`
  * - :mod:`.options.responsive <highcharts_core.options.responsive>`
    - :class:`Responsive <highcharts_core.options.responsive.Responsive>`
      :class:`ResponsiveRules <highcharts_core.options.responsive.ResponsiveRules>`
      :class:`Condition <highcharts_core.options.responsive.Condition>`
  * - :mod:`.options.series <highcharts_core.options.series>`
    -
  * - :mod:`.options.series.arcdiagram <highcharts_core.options.series.arcdiagram>`
    - :class:`ArcDiagramSeries <highcharts_core.options.series.arcdiagram.ArcDiagramSeries>`
  * - :mod:`.options.series.area <highcharts_core.options.series.area>`
    - :class:`AreaSeries <highcharts_core.options.series.area.AreaSeries>`
      :class:`AreaRangeSeries <highcharts_core.options.series.area.AreaRangeSeries>`
      :class:`AreaSplineSeries <highcharts_core.options.series.area.AreaSplineSeries>`
      :class:`AreaSplineRangeSeries <highcharts_core.options.series.area.AreaSplineRangeSeries>`
      :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`
      :class:`StreamGraphSeries <highcharts_core.options.series.area.StreamGraphSeries>`
  * - :mod:`.options.series.bar <highcharts_core.options.series.bar>`
    - :class:`BarSeries <highcharts_core.options.series.bar.BarSeries>`
      :class:`ColumnSeries <highcharts_core.options.series.bar.ColumnSeries>`
      :class:`ColumnPyramidSeries <highcharts_core.options.series.bar.ColumnPyramidSeries>`
      :class:`ColumnRangeSeries <highcharts_core.options.series.bar.ColumnRangeSeries>`
      :class:`CylinderSeries <highcharts_core.options.series.bar.CylinderSeries>`
      :class:`VariwideSeries <highcharts_core.options.series.bar.VariwideSeries>`
      :class:`WaterfallSeries <highcharts_core.options.series.bar.WaterfallSeries>`
      :class:`WindBarbSeries <highcharts_core.options.series.bar.WindBarbSeries>`
      :class:`XRangeSeries <highcharts_core.options.series.bar.XRangeSeries>`
      :class:`BaseBarSeries <highcharts_core.options.series.bar.BaseBarSeries>`
  * - :mod:`.options.series.base <highcharts_core.options.series.base>`
    - :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
  * - :mod:`.options.series.bellcurve <highcharts_core.options.series.bellcurve>`
    - :class:`BellCurveSeries <highcharts_core.options.series.bellcurve.BellCurveSeries>`
  * - :mod:`.options.series.boxplot <highcharts_core.options.series.boxplot>`
    - :class:`BoxPlotSeries <highcharts_core.options.series.boxplot.BoxPlotSeries>`
      :class:`ErrorBarSeries <highcharts_core.options.series.boxplot.ErrorBarSeries>`
  * - :mod:`.options.series.bubble <highcharts_core.options.series.bubble>`
    - :class:`BubbleSeries <highcharts_core.options.series.bubble.BubbleSeries>`
  * - :mod:`.options.series.bullet <highcharts_core.options.series.bullet>`
    - :class:`BulletSeries <highcharts_core.options.series.bullet.BulletSeries>`
  * - :mod:`.options.series.data <highcharts_core.options.series.data>`
    -
  * - :mod:`.options.series.data.accessibility <highcharts_core.options.series.data.accessibility>`
    - :class:`DataPointAccessibility <highcharts_core.options.series.data.accessibility.DataPointAccessibility>`
  * - :mod:`.options.series.data.arcdiagram <highcharts_core.options.series.data.arcdiagram>`
    - :class:`ArcDiagramData <highcharts_core.options.series.data.arcdiagram.ArcDiagramData>`
  * - :mod:`.options.series.data.bar <highcharts_core.options.series.data.bar>`
    - :class:`BarData <highcharts_core.options.series.data.bar.BarData>`
      :class:`WaterfallData <highcharts_core.options.series.data.bar.WaterfallData>`
      :class:`WindBarbData <highcharts_core.options.series.data.bar.WindBarbData>`
      :class:`XRangeData <highcharts_core.options.series.data.bar.XRangeData>`
  * - :mod:`.options.series.data.base <highcharts_core.options.series.data.base>`
    - :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`
  * - :mod:`.options.series.data.boxplot <highcharts_core.options.series.data.boxplot>`
    - :class:`BoxPlotData <highcharts_core.options.series.data.boxplot.BoxPlotData>`
  * - :mod:`.options.series.data.bullet <highcharts_core.options.series.data.bullet>`
    - :class:`BulletData <highcharts_core.options.series.data.bullet.BulletData>`
  * - :mod:`.options.series.data.cartesian <highcharts_core.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_core.options.series.data.cartesian.CartesianData>`
      :class:`Cartesian3DData <highcharts_core.options.series.data.cartesian.Cartesian3DData>`
      :class:`CartesianValueData <highcharts_core.options.series.data.cartesian.CartesianValueData>`
  * - :mod:`.options.series.data.connections <highcharts_core.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_core.options.series.data.connections.ConnectionData>`
      :class:`WeightedConnectionData <highcharts_core.options.series.data.connections.WeightedConnectionData>`
      :class:`OutgoingWeightedConnectionData <highcharts_core.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`ConnectionBase <highcharts_core.options.series.data.connections.ConnectionBase>`
  * - :mod:`.options.series.data.pie <highcharts_core.options.series.data.pie>`
    - :class:`PieData <highcharts_core.options.series.data.pie.PieData>`
      :class:`VariablePieData <highcharts_core.options.series.data.pie.VariablePieData>`
  * - :mod:`.options.series.data.range <highcharts_core.options.series.data.range>`
    - :class:`RangeData <highcharts_core.options.series.data.range.RangeData>`
      :class:`ConnectedRangeData <highcharts_core.options.series.data.range.ConnectedRangeData>`
  * - :mod:`.options.series.data.single_point <highcharts_core.options.series.data.single_point>`
    - :class:`SinglePointData <highcharts_core.options.series.data.single_point.SinglePointData>`
      :class:`SingleValueData <highcharts_core.options.series.data.single_point.SingleValueData>`
      :class:`SingleXData <highcharts_core.options.series.data.single_point.SingleXData>`
      :class:`LabeledSingleXData <highcharts_core.options.series.data.single_point.LabeledSingleXData>`
      :class:`ConnectedSingleXData <highcharts_core.options.series.data.single_point.ConnectedSingleXData>`
      :class:`SinglePointBase <highcharts_core.options.series.data.single_point.SinglePointBase>`
  * - :mod:`.options.series.data.sunburst <highcharts_core.options.series.data.sunburst>`
    - :class:`SunburstData <highcharts_core.options.series.data.sunburst.SunburstData>`
  * - :mod:`.options.series.data.treegraph <highcharts_core.options.series.data.treegraph>`
    - :class:`TreegraphData <highcharts_core.options.series.data.treegraph.TreegraphData>`
  * - :mod:`.options.series.data.treemap <highcharts_core.options.series.data.treemap>`
    - :class:`TreemapData <highcharts_core.options.series.data.treemap.TreemapData>`
  * - :mod:`.options.series.data.vector <highcharts_core.options.series.data.vector>`
    - :class:`VectorData <highcharts_core.options.series.data.vector.VectorData>`
  * - :mod:`.options.series.data.venn <highcharts_core.options.series.data.venn>`
    - :class:`VennData <highcharts_core.options.series.data.venn.VennData>`
  * - :mod:`.options.series.data.wordcloud <highcharts_core.options.series.data.wordcloud>`
    - :class:`WordcloudData <highcharts_core.options.series.data.wordcloud.WordcloudData>`
  * - :mod:`.options.series.dependencywheel <highcharts_core.options.series.dependencywheel>`
    - :class:`DependencyWheelSeries <highcharts_core.options.series.dependencywheel.DependencyWheelSeries>`
  * - :mod:`.options.series.dumbbell <highcharts_core.options.series.dumbbell>`
    - :class:`DumbbellSeries <highcharts_core.options.series.dumbbell.DumbbellSeries>`
      :class:`LollipopSeries <highcharts_core.options.series.dumbbell.LollipopSeries>`
  * - :mod:`.options.series.funnel <highcharts_core.options.series.funnel>`
    - :class:`FunnelSeries <highcharts_core.options.series.funnel.FunnelSeries>`
      :class:`Funnel3DSeries <highcharts_core.options.series.funnel.Funnel3DSeries>`
  * - :mod:`.options.series.gauge <highcharts_core.options.series.gauge>`
    - :class:`GaugeSeries <highcharts_core.options.series.gauge.GaugeSeries>`
      :class:`SolidGaugeSeries <highcharts_core.options.series.gauge.SolidGaugeSeries>`
  * - :mod:`.options.series.heatmap <highcharts_core.options.series.heatmap>`
    - :class:`HeatmapSeries <highcharts_core.options.series.heatmap.HeatmapSeries>`
      :class:`TilemapSeries <highcharts_core.options.series.heatmap.TilemapSeries>`
  * - :mod:`.options.series.histogram <highcharts_core.options.series.histogram>`
    - :class:`HistogramSeries <highcharts_core.options.series.histogram.HistogramSeries>`
  * - :mod:`.options.series.item <highcharts_core.options.series.item>`
    - :class:`ItemSeries <highcharts_core.options.series.item.ItemSeries>`
  * - :mod:`.options.series.labels <highcharts_core.options.series.labels>`
    - :class:`SeriesLabel <highcharts_core.options.series.labels.SeriesLabel>`
      :class:`Box <highcharts_core.options.series.labels.Box>`
  * - :mod:`.options.series.networkgraph <highcharts_core.options.series.networkgraph>`
    - :class:`NetworkGraphSeries <highcharts_core.options.series.networkgraph.NetworkGraphSeries>`
  * - :mod:`.options.series.organization <highcharts_core.options.series.organization>`
    - :class:`OrganizationSeries <highcharts_core.options.series.organization.OrganizationSeries>`
  * - :mod:`.options.series.packedbubble <highcharts_core.options.series.packedbubble>`
    - :class:`PackedBubbleSeries <highcharts_core.options.series.packedbubble.PackedBubbleSeries>`
  * - :mod:`.options.series.pareto <highcharts_core.options.series.pareto>`
    - :class:`ParetoSeries <highcharts_core.options.series.pareto.ParetoSeries>`
  * - :mod:`.options.series.pictorial <highcharts_core.options.series.pictorial>`
    - :class:`PictorialSeries <highcharts_core.options.series.pictorial.PictorialSeries>`
      :class:`PictorialPaths <highcharts_core.options.series.pictorial.PictorialPaths>`
  * - :mod:`.options.series.pie <highcharts_core.options.series.pie>`
    - :class:`PieSeries <highcharts_core.options.series.pie.PieSeries>`
      :class:`VariablePieSeries <highcharts_core.options.series.pie.VariablePieSeries>`
  * - :mod:`.options.series.polygon <highcharts_core.options.series.polygon>`
    - :class:`PolygonSeries <highcharts_core.options.series.polygon.PolygonSeries>`
  * - :mod:`.options.series.pyramid <highcharts_core.options.series.pyramid>`
    - :class:`PyramidSeries <highcharts_core.options.series.pyramid.PyramidSeries>`
      :class:`Pyramid3DSeries <highcharts_core.options.series.pyramid.Pyramid3DSeries>`
  * - :mod:`.options.series.sankey <highcharts_core.options.series.sankey>`
    - :class:`SankeySeries <highcharts_core.options.series.sankey.SankeySeries>`
  * - :mod:`.options.series.scatter <highcharts_core.options.series.scatter>`
    - :class:`ScatterSeries <highcharts_core.options.series.scatter.ScatterSeries>`
      :class:`Scatter3DSeries <highcharts_core.options.series.scatter.Scatter3DSeries>`
  * - :mod:`.options.series.series_generator <highcharts_core.options.series.series_generator>`
    - :func:`create_series_obj() <highcharts_core.options.series.series_generator.create_series_obj>`
  * - :mod:`.options.series.spline <highcharts_core.options.series.spline>`
    - :class:`SplineSeries <highcharts_core.options.series.spline.SplineSeries>`
  * - :mod:`.options.series.sunburst <highcharts_core.options.series.sunburst>`
    - :class:`SunburstSeries <highcharts_core.options.series.sunburst.SunburstSeries>`
  * - :mod:`.options.series.timeline <highcharts_core.options.series.timeline>`
    - :class:`TimelineSeries <highcharts_core.options.series.timeline.TimelineSeries>`
  * - :mod:`.options.series.treegraph <highcharts_core.options.series.treegraph>`
    - :class:`TreegraphSeries <highcharts_core.options.series.treegraph.TreegraphSeries>`
  * - :mod:`.options.series.treemap <highcharts_core.options.series.treemap>`
    - :class:`TreemapSeries <highcharts_core.options.series.treemap.TreemapSeries>`
  * - :mod:`.options.series.vector <highcharts_core.options.series.vector>`
    - :class:`VectorSeries <highcharts_core.options.series.vector.VectorSeries>`
  * - :mod:`.options.series.venn <highcharts_core.options.series.venn>`
    - :class:`VennSeries <highcharts_core.options.series.venn.VennSeries>`
  * - :mod:`.options.series.wordcloud <highcharts_core.options.series.wordcloud>`
    - :class:`WordcloudSeries <highcharts_core.options.series.wordcloud.WordcloudSeries>`
  * - :mod:`.options.sonification <highcharts_core.options.sonification>`
    - :class:`SonificationOptions <highcharts_core.options.sonification.SonificationOptions>`
  * - :mod:`.options.sonification.grouping <highcharts_core.options.sonification.grouping>`
    - :class:`PointGrouping <highcharts_core.options.sonification.grouping.SonificationGrouping>`
  * - :mod:`.options.sonification.mapping <highcharts_core.options.sonification.mapping>`
    - :class:`SonificationMapping <highcharts_core.options.sonification.mapping.SonificationMapping>`
      :class:`AudioParameter <highcahrts_core.options.sonification.mapping.AudioParameter>`
      :class:`AudioFilter <highcharts_core.options.sonification.mapping.AudioFilter>`
      :class:`PitchParameter <highcharts_core.options.sonification.mapping.PitchParameter>`
      :class:`TremoloEffect <highcahrts_core.options.sonification.mapping.TremoloEffect>`
  * - :mod:`.options.sonification.track_configurations <highcharts_core.options.sonification.track_configurations>`
    - :class:`InstrumentTrackConfiguration <highcharts_core.options.sonification.track_configurations.InstrumentTrackConfiguration>`
      :class:`SpeechTrackConfiguration <highcharts_core.options.sonification.track_configurations.SpeechTrackConfiguration>`
      :class:`ContextTrackConfiguration <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration>`
      :class:`TrackConfigurationBase <highcharts_core.options.sonification.track_configurations.TrackConfigurationBase>`
      :class:`ActiveWhen <highcharts_core.options.sonification.track_configurations.ActiveWhen>`
  * - :mod:`.options.subtitle <highcharts_core.options.subtitle>`
    - :class:`Subtitle <highcharts_core.options.subtitle.Subtitle>`
  * - :mod:`.options.time <highcharts_core.options.time>`
    - :class:`Time <highcharts_core.options.time.Time>`
  * - :mod:`.options.title <highcharts_core.options.title>`
    - :class:`Title <highcharts_core.options.title.Title>`
  * - :mod:`.options.tooltips <highcharts_core.options.tooltips>`
    - :class:`Tooltip <highcharts_core.options.tooltips.Tooltip>`
  * - :mod:`.utility_classes <highcharts_core.utility_classes>`
    -
  * - :mod:`.utility_classes.animation <highcharts_core.utility_classes.animation>`
    - :class:`AnimationOptions <highcharts_core.utility_classes.animation.AnimationOptions>`
  * - :mod:`.utility_classes.ast <highcharts_core.utility_classes.ast>`
    - :class:`ASTMap <highcharts_core.utility_classes.ast.ASTMap>`
      :class:`ASTNode <highcharts_core.utility_classes.ast.ASTNode>`
      :class:`TextPath <highcharts_core.utility_classes.ast.TextPath>`
      :class:`AttributeObject <highcharts_core.utility_classes.ast.AttributeObject>`
  * - :mod:`.utility_classes.breadcrumbs <highcharts_core.utility_classes.breadcrumbs>`
    - :class:`BreadcrumbOptions <highcharts_core.utility_classes.breadcrumbs.BreadcrumbOptions>`
      :class:`Separator <highcharts_core.utility_classes.breadcrumbs.Separator>`
  * - :mod:`.utility_classes.buttons <highcharts_core.utility_classes.buttons>`
    - :class:`ExportingButtons <highcharts_core.utility_classes.buttons.ExportingButtons>`
      :class:`CollapseButtonConfiguration <highcharts_core.utility_classes.buttons.CollapseButtonConfiguration>`
      :class:`ContextButtonConfiguration <highcharts_core.utility_classes.buttons.ContextButtonConfiguration>`
      :class:`ButtonConfiguration <highcharts_core.utility_classes.buttons.ButtonConfiguration>`
      :class:`ButtonTheme <highcharts_core.utility_classes.buttons.ButtonTheme>`
  * - :mod:`.utility_classes.clusters <highcharts_core.utility_classes.clusters>`
    - :class:`ClusterOptions <highcharts_core.utility_classes.clusters.ClusterOptions>`
      :class:`VectorLayoutAlgorithm <highcharts_core.utility_classes.clusters.VectorLayoutAlgorithm>`
  * - :mod:`.utility_classes.data_grouping <highcharts_core.utility_classes.data_grouping>`
    - :class:`DataGroupingOptions <highcharts_core.utility_classes.data_grouping.DataGroupingOptions>`
  * - :mod:`.utility_classes.data_labels <highcharts_core.utility_classes.data_labels>`
    - :class:`DataLabel <highcharts_core.utility_classes.data_labels.DataLabel>`
      :class:`SunburstDataLabel <highcharts_core.utility_classes.data_labels.SunburstDataLabel>`
      :class:`OrganizationDataLabel <highcharts_core.utility_classes.data_labels.OrganizationDataLabel>`
      :class:`NodeDataLabel <highcharts_core.utility_classes.data_labels.NodeDataLabel>`
      :class:`Filter <highcharts_core.utility_classes.data_labels.Filter>`
  * - :mod:`.utility_classes.date_time_label_formats <highcharts_core.utility_classes.date_time_label_formats>`
    - :class:`DateTimeLabelFormats <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelFormats>`
  * - :mod:`.utility_classes.events <highcharts_core.utility_classes.events>`
    - :class:`ChartEvents <highcharts_core.utility_classes.events.ChartEvents>`
      :class:`BreadcrumbEvents <highcharts_core.utility_classes.events.BreadcrumbEvents>`
      :class:`NavigationEvents <highcharts_core.utility_classes.events.NavigationEvents>`
      :class:`PointEvents <highcharts_core.utility_classes.events.PointEvents>`
      :class:`SeriesEvents <highcharts_core.utility_classes.events.SeriesEvents>`
      :class:`SimulationEvents <highcharts_core.utility_classes.events.SimulationEvents>`
      :class:`ClusterEvents <highcharts_core.utility_classes.events.ClusterEvents>`
      :class:`AxisEvents <highcharts_core.utility_classes.events.AxisEvents>`
      :class:`MouseEvents <highcharts_core.utility_classes.events.MouseEvents>`
  * - :mod:`.utility_classes.gradients <highcharts_core.utility_classes.gradients>`
    - :class:`Gradient <highcharts_core.utility_classes.gradients.Gradient>`
      :class:`LinearGradient <highcharts_core.utility_classes.gradients.LinearGradient>`
      :class:`RadialGradient <highcharts_core.utility_classes.gradients.RadialGradient>`
  * - :mod:`.utility_classes.javascript_functions <highcharts_core.utility_classes.javascript_functions>`
    - :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
      :class:`JavaScriptClass <highcharts_core.utility_classes.javascript_functions.JavaScriptClass>`
      :class:`VariableName <highcharts_core.utility_classes.javascript_functions.VariableName>`
  * - :mod:`.utility_classes.jitter <highcharts_core.utility_classes.jitter>`
    - :class:`Jitter <highcharts_core.utility_classes.jitter.Jitter>`
  * - :mod:`.utility_classes.markers <highcharts_core.utility_classes.markers>`
    - :class:`Marker <highcharts_core.utility_classes.markers.Marker>`
  * - :mod:`.utility_classes.menus <highcharts_core.utility_classes.menus>`
    - :class:`MenuObject <highcharts_core.utility_classes.menus.MenuObject>`
      :class:`MenuItem <highcharts_core.utility_classes.menus.MenuItem>`
  * - :mod:`.utility_classes.nodes <highcharts_core.utility_classes.nodes>`
    - :class:`NodeOptions <highcharts_core.utility_classes.nodes.NodeOptions>`
      :class:`DependencyWheelNodeOptions <highcharts_core.utility_classes.nodes.DependencyWheelNodeOptions>`
      :class:`OrganizationNodeOptions <highcharts_core.utility_classes.nodes.OrganizationNodeOptions>`
  * - :mod:`.utility_classes.partial_fill <highcharts_core.utility_classes.partial_fill>`
    - :class:`PartialFillOptions <highcharts_core.utility_classes.partial_fill.PartialFillOptions>`
  * - :mod:`.utility_classes.patterns <highcharts_core.utility_classes.patterns>`
    - :class:`Pattern <highcharts_core.utility_classes.patterns.Pattern>`
      :class:`PatternOptions <highcharts_core.utility_classes.patterns.PatternOptions>`
  * - :mod:`.utility_classes.position <highcharts_core.utility_classes.position>`
    - :class:`Position <highcharts_core.utility_classes.position.Position>`
  * - :mod:`.utility_classes.shadows <highcharts_core.utility_classes.shadows>`
    - :class:`ShadowOptions <highcharts_core.utility_classes.shadows.ShadowOptions>`
  * - :mod:`.utility_classes.states <highcharts_core.utility_classes.states>`
    - :class:`States <highcharts_core.utility_classes.states.States>`
      :class:`HoverState <highcharts_core.utility_classes.states.HoverState>`
      :class:`InactiveState <highcharts_core.utility_classes.states.InactiveState>`
      :class:`NormalState <highcharts_core.utility_classes.states.NormalState>`
      :class:`SelectState <highcharts_core.utility_classes.states.SelectState>`
  * - :mod:`.utility_classes.zones <highcharts_core.utility_classes.zones>`
    - :class:`Zone <highcharts_core.utility_classes.zones.Zone>`
      :class:`ClusterZone <highcharts_core.utility_classes.zones.ClusterZone>`

.. toctree::
  :hidden:
  :titlesonly:

  api/chart
  api/global_options/index
  api/headless_export
  api/highcharts
  api/options/index
  api/utility_classes/index

*********************
Library Internals
*********************

.. toctree::
  :hidden:

  Internal Reference <api/internals>

While most users will be interacting with the :ref:`Core Components <core_components>` of
**Highcharts for Python**, you may need (or choose to) work with various internals of the
library. If you're :doc:`contributing` to the library, then you will definitely need to
familiarize yourself with these internals.

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.metaclasses <highcharts_core.metaclasses>`
    - :class:`HighchartsMeta <highcharts_core.metaclasses.HighchartsMeta>`
      :class:`JavaScriptDict <highcharts_core.metaclasses.JavaScriptDict>`
  * - :mod:`.decorators <highcharts_core.decorators>`
    - :deco:`@class_sensitive() <highcharts_core.decorators.class_sensitive>`
      :func:`validate_types() <highcharts_core.decorators.validate_types>`
  * - :mod:`.js_literal_functions <highcharts_core.js_literal_functions>`
    - :func:`serialize_to_js_literal() <highcharts_core.js_literal_functions.serialize_to_js_literal>`
      :func:`attempt_variable_declaration() <highcharts_core.js_literal_functions.attempt_variable_declaration>`
      :func:`is_js_function_or_class() <highcharts_core.js_literal_functions.is_js_function_or_class>`
      :func:`get_js_literal() <highcharts_core.js_literal_functions.get_js_literal>`
      :func:`assemble_js_literal() <highcharts_core.js_literal_functions.assemble_js_literal>`
      :func:`convert_js_literal_to_python() <highcharts_core.js_literal_functions.convert_js_literal_to_python>`
      :func:`convert_js_property_to_python() <highcharts_core.js_literal_functions.convert_js_property_to_python>`
      :func:`convert_js_to_python() <highcharts_core.js_literal_functions.convert_js_to_python>`
      :func:`get_key_value_pairs() <highcharts_core.js_literal_functions.get_key_value_pairs>`
  * - :mod:`.utility_functions <highcharts_core.utility_functions>`
    - :func:`mro_to_dict() <highcharts_core.utility_functions.mro_to_dict>`
      :func:`get_remaining_mro() <highcharts_core.utility_functions.get_remaining_mro>`
      :func:`mro__to_untrimmed_dict() <highcharts_core.utility_functions.mro__to_untrimmed_dict>`
      :func:`validate_color() <highcharts_core.utility_functions.validate_color>`
      :func:`to_camelCase() <highcharts_core.utility_functions.to_camelCase>`
      :func:`parse_csv() <highcharts_core.utility_functions.parse_csv>`

.. target-notes::

.. include:: links.txt
