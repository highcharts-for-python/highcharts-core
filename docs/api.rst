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

.. _core_components:

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
  * - :mod:`global_options.language.accessibility.chart_types <highcharts_python.global_options.language.accessibility.chart_types>`
    - :class:`ChartTypesLanguageOptions <highcharts_python.global_options.language.accessibility.chart_types.ChartTypesLanguageOptions>`
  * - :mod:`global_options.language.accessibility.exporting <highcharts_python.global_options.language.accessibility.exporting>`
    - :class:`ExportingLanguageOptions <highcharts_python.global_options.language.accessibility.exporting.ExportingLanguageOptions>`
  * - :mod:`global_options.language.accessibility.legend <highcharts_python.global_options.language.accessibility.legend>`
    - :class:`LegendLanguageOptions <highcharts_python.global_options.language.accessibility.legend.LegendLanguageOptions>`
  * - :mod:`global_options.language.accessibility.range_selector <highcharts_python.global_options.language.accessibility.range_selector>`
    - :class:`RangeSelectorLanguageOptions <highcharts_python.global_options.language.accessibility.range_selector.RangeSelectorLanguageOptions>`
  * - :mod:`global_options.language.accessibility.screen_reader_section <highcharts_python.global_options.language.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSectionLanguageOptions <highcharts_python.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionLanguageOptions>`
      :class:`ScreenReaderSectionAnnotationLanguage <highcharts_python.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionAnnotationLanguage>`
  * - :mod:`global_options.language.accessibility.series <highcharts_python.global_options.language.accessibility.series>`
    - :class:`SeriesLanguageOptions <highcharts_python.global_options.language.accessibility.series.SeriesLanguageOptions>`
      :class:`SeriesSummaryLanguageOptions <highcharts_python.global_options.language.accessibility.series.SeriesSummaryLanguageOptions>`
      :class:`SeriesTypeDescriptions <highcharts_python.global_options.language.accessibility.series.SeriesTypeDescriptions>`
  * - :mod:`global_options.language.accessibility.sonification <highcharts_python.global_options.language.accessibility.sonification>`
    - :class:`SonificationLanguageOptions <highcharts_python.global_options.language.accessibility.sonification.SonificationLanguageOptions>`
  * - :mod:`global_options.language.accessibility.table <highcharts_python.global_options.language.accessibility.table>`
    - :class:`TableLanguageOptions <highcharts_python.global_options.language.accessibility.table.TableLanguageOptions>`
  * - :mod:`global_options.language.accessibility.zoom <highcharts_python.global_options.language.accessibility.zoom>`
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
  * - :mod:`.chart.options_3d <highcharts_python.options.chart.options_3d>`
    - :class:`Options3D <highcharts_python.options.chart.options_3d.Options3D>`
      :class:`Frame <highcharts_python.options.chart.options_3d.Frame>`
      :class:`PanelOptions <highcharts_python.options.chart.options_3d.PanelOptions>`
  * - :mod:`.chart.reset_zoom_button <highcharts_python.options.chart.reset_zoom_button>`
    - :class:`ResetZoomButtonOptions <highcharts_python.options.chart.reset_zoom_button.ResetZoomButtonOptions>`
  * - :mod:`.chart.scrollable_plot_area <highcharts_python.options.chart.scrollable_plot_area>`
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
  * - :mod:`.options.navigation.bindings <highcharts_python.options.navigation.bindings>`
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
    - :class:`PlotOptions <highcharts_python.options.plot_options.PlotOptions>`
  * - :mod:`.plot_options.accessibility <highcharts_python.options.plot_options.accessibility>`
    - :class:`TypeOptionsAccessibility <highcharts_python.options.plot_options.accessibility.TypeOptionsAccessibility>`
      :class:`SeriesKeyboardNavigation <highcharts_python.options.plot_options.accessibility.SeriesKeyboardNavigation>`
  * - :mod:`.plot_options.arcdiagram <highcharts_python.options.plot_options.arcdiagram>`
    - :class:`ArcDiagramOptions <highcharts_python.options.plot_options.arcdiagram.ArcDiagramOptions>`
  * - :mod:`.plot_options.area <highcharts_python.options.plot_options.area>`
    - :class:`AreaOptions <highcharts_python.options.plot_options.area.AreaOptions>`
      :class:`AreaRangeOptions <highcharts_python.options.plot_options.area.AreaRangeOptions>`
      :class:`AreaSplineOptions <highcharts_python.options.plot_options.area.AreaSplineOptions>`
      :class:`AreaSplineRangeOptions <highcharts_python.options.plot_options.area.AreaSplineRangeOptions>`
      :class:`LineOptions <highcharts_python.options.plot_options.area.LineOptions>`
      :class:`StreamGraphOptions <highcharts_python.options.plot_options.area.StreamGraphOptions>`
  * - :mod:`.plot_options.bar <highcharts_python.options.plot_options.bar>`
    - :class:`BarOptions <highcharts_python.options.plot_options.bar.BarOptions>`
      :class:`ColumnOptions <highcharts_python.options.plot_options.bar.ColumnOptions>`
      :class:`ColumnPyramidOptions <highcharts_python.options.plot_options.bar.ColumnPyramidOptions>`
      :class:`ColumnRangeOptions <highcharts_python.options.plot_options.bar.ColumnRangeOptions>`
      :class:`CylinderOptions <highcharts_python.options.plot_options.bar.CylinderOptions>`
      :class:`VariwideOptions <highcharts_python.options.plot_options.bar.VariwideOptions>`
      :class:`WaterfallOptions <highcharts_python.options.plot_options.bar.WaterfallOptions>`
      :class:`WindBarbOptions <highcharts_python.options.plot_options.bar.WindBarbOptions>`
      :class:`XRangeOptions <highcharts_python.options.plot_options.bar.XRangeOptions>`
      :class:`BaseBarOptions <highcharts_python.options.plot_options.bar.BaseBarOptions>`
  * - :mod:`.plot_options.bellcurve <highcharts_python.options.plot_options.bellcurve>`
    - :class:`BellCurveOptions <highcharts_python.options.plot_options.bellcurve.BellCurveOptions>`
  * - :mod:`.plot_options.boxplot <highcharts_python.options.plot_options.boxplot>`
    - :class:`BoxPlotOptions <highcharts_python.options.plot_options.boxplot.BoxPlotOptions>`
      :class:`ErrorBarOptions <highcharts_python.options.plot_options.boxplot.ErrorBarOptions>`
  * - :mod:`.plot_options.bubble <highcharts_python.options.plot_options.bubble>`
    - :class:`BubbleOptions <highcharts_python.options.plot_options.bubble.BubbleOptions>`
  * - :mod:`.plot_options.bullet <highcharts_python.options.plot_options.bullet>`
    - :class:`BulletOptions <highcharts_python.options.plot_options.bullet.BulletOptions>`
      :class:`TargetOptions <highcharts_python.options.plot_options.bullet.TargetOptions>`
  * - :mod:`.plot_options.data_sorting <highcharts_python.options.plot_options.data_sorting>`
    - :class:`DataSorting <highcharts_python.options.plot_options.data_sorting.DataSorting>`
  * - :mod:`.plot_options.dependencywheel <highcharts_python.options.plot_options.dependencywheel>`
    - :class:`DependencyWheelOptions <highcharts_python.options.plot_options.dependencywheel.DependencyWheelOptions>`
  * - :mod:`.plot_options.drag_drop <highcharts_python.options.plot_options.drag_drop>`
    - :class:`DragDropOptions <highcharts_python.options.plot_options.drag_drop.DragDropOptions>`
      :class:`HighLowDragDropOptions <highcharts_python.options.plot_options.drag_drop.HighLowDragDropOptions>`
      :class:`BoxPlotDragDropOptions <highcharts_python.options.plot_options.drag_drop.BoxPlotDragDropOptions>`
      :class:`BulletDragDropOptions <highcharts_python.options.plot_options.drag_drop.BulletDragDropOptions>`
      :class:`GuideBox <highcharts_python.options.plot_options.drag_drop.GuideBox>`
      :class:`GuideBoxOptions <highcharts_python.options.plot_options.drag_drop.GuideBoxOptions>`
      :class:`DragHandle <highcharts_python.options.plot_options.drag_drop.DragHandle>`
  * - :mod:`.plot_options.dumbbell <highcharts_python.options.plot_options.dumbbell>`
    - :class:`DumbbellOptions <highcharts_python.options.plot_options.dumbbell.DumbbellOptions>`
      :class:`LollipopOptions <highcharts_python.options.plot_options.dumbbell.LollipopOptions>`
  * - :mod:`.plot_options.funnel <highcharts_python.options.plot_options.funnel>`
    - :class:`FunnelOptions <highcharts_python.options.plot_options.funnel.FunnelOptions>`
      :class:`Funnel3DOptions <highcharts_python.options.plot_options.funnel.Funnel3DOptions>`
  * - :mod:`.plot_options.gauge <highcharts_python.options.plot_options.gauge>`
    - :class:`GaugeOptions <highcharts_python.options.plot_options.gauge.GaugeOptions>`
      :class:`SolidGaugeOptions <highcharts_python.options.plot_options.gauge.SolidGaugeOptions>`
  * - :mod:`.plot_options.generic <highcharts_python.options.plot_options.generic>`
    - :class:`GenericTypeOptions <highcharts_python.options.plot_options.generic.GenericTypeOptions>`
  * - :mod:`.plot_options.Heatmap <highcharts_python.options.plot_options.Heatmap>`
    - :class:`HeatmapOptions <highcharts_python.options.plot_options.Heatmap.HeatmapOptions>`
      :class:`TilemapOptions <highcharts_python.options.plot_options.Tilemap.TilemapOptions>`
  * - :mod:`.plot_options.histogram <highcharts_python.options.plot_options.histogram>`
    - :class:`HistogramOptions <highcharts_python.options.plot_options.histogram.HistogramOptions>`
  * - :mod:`.plot_options.item <highcharts_python.options.plot_options.item>`
    - :class:`ItemOptions <highcharts_python.options.plot_options.item.ItemOptions>`
  * - :mod:`.plot_options.levels <highcharts_python.options.plot_options.levels>`
    - :class:`LevelOptions <highcharts_python.options.plot_options.levels.LevelOptions>`
      :class:`SunburstLevelOptions <highcharts_python.options.plot_options.levels.SunburstLevelOptions>`
      :class:`TreemapLevelOptions <highcharts_python.options.plot_options.levels.TreemapLevelOptions>`
      :class:`LevelSize <highcharts_python.options.plot_options.levels.LevelSize>`
      :class:`ColorVariation <highcharts_python.options.plot_options.levels.ColorVariation>`
      :class:`BaseLevelOptions <highcharts_python.options.plot_options.levels.BaseLevelOptions>`
  * - :mod:`.plot_options.link <highcharts_python.options.plot_options.link>`
    - :class:`LinkOptions <highcharts_python.options.plot_options.link.LinkOptions>`
  * - :mod:`.plot_options.networkgraph <highcharts_python.options.plot_options.networkgraph>`
    - :class:`NetworkGraphOptions <highcharts_python.options.plot_options.networkgraph.NetworkGraphOptions>`
      :class:`LayoutAlgorithm <highcharts_python.options.plot_options.networkgraph.LayoutAlgorithm>`
  * - :mod:`.plot_options.organization <highcharts_python.options.plot_options.organization>`
    - :class:`OrganizationOptions <highcharts_python.options.plot_options.organization.OrganizationOptions>`
  * - :mod:`.plot_options.packedbubble <highcharts_python.options.plot_options.packedbubble>`
    - :class:`PackedBubbleOptions <highcharts_python.options.plot_options.packedbubble.PackedBubbleOptions>`
      :class:`ParentNodeOptions <highcharts_python.options.plot_options.packedbubble.ParentNodeOptions>`
  * - :mod:`.plot_options.pareto <highcharts_python.options.plot_options.pareto>`
    - :class:`ParetoOptions <highcharts_python.options.plot_options.pareto.ParetoOptions>`
  * - :mod:`.plot_options.pie <highcharts_python.options.plot_options.pie>`
    - :class:`PieOptions <highcharts_python.options.plot_options.pie.PieOptions>`
      :class:`VariablePieOptions <highcharts_python.options.plot_options.pie.VariablePieOptions>`
  * - :mod:`.plot_options.points <highcharts_python.options.plot_options.points>`
    - :class:`Point <highcharts_python.options.plot_options.points.Point>`
      :class:`OnPointOptions <highcharts_python.options.plot_options.points.OnPointOptions>`
      :class:`ConnectorOptions <highcharts_python.options.plot_options.points.ConnectorOptions>`
  * - :mod:`.plot_options.polygon <highcharts_python.options.plot_options.polygon>`
    - :class:`PolygonOptions <highcharts_python.options.plot_options.polygon.PolygonOptions>`
  * - :mod:`.plot_options.pyramid <highcharts_python.options.plot_options.pyramid>`
    - :class:`PyramidOptions <highcharts_python.options.plot_options.pyramid.PyramidOptions>`
      :class:`Pyramid3DOptions <highcharts_python.options.plot_options.pyramid.Pyramid3DOptions>`
  * - :mod:`.plot_options.sankey <highcharts_python.options.plot_options.sankey>`
    - :class:`SankeyOptions <highcharts_python.options.plot_options.sankey.SankeyOptions>`
  * - :mod:`.plot_options.scatter <highcharts_python.options.plot_options.scatter>`
    - :class:`ScatterOptions <highcharts_python.options.plot_options.scatter.ScatterOptions>`
      :class:`Scatter3DOptions <highcharts_python.options.plot_options.scatter.Scatter3DOptions>`
  * - :mod:`.plot_options.series <highcharts_python.options.plot_options.series>`
    - :class:`SeriesOptions <highcharts_python.options.plot_options.series.SeriesOptions>`
  * - :mod:`.plot_options.spline <highcharts_python.options.plot_options.spline>`
    - :class:`SplineOptions <highcharts_python.options.plot_options.spline.SplineOptions>`
  * - :mod:`.plot_options.sunburst <highcharts_python.options.plot_options.sunburst>`
    - :class:`SunburstOptions <highcharts_python.options.plot_options.sunburst.SunburstOptions>`
  * - :mod:`.plot_options.timeline <highcharts_python.options.plot_options.timeline>`
    - :class:`TimelineOptions <highcharts_python.options.plot_options.timeline.TimelineOptions>`
  * - :mod:`.plot_options.treemap <highcharts_python.options.plot_options.treemap>`
    - :class:`TreemapOptions <highcharts_python.options.plot_options.treemap.TreemapOptions>`
  * - :mod:`.plot_options.vector <highcharts_python.options.plot_options.vector>`
    - :class:`VectorOptions <highcharts_python.options.plot_options.vector.VectorOptions>`
  * - :mod:`.plot_options.venn <highcharts_python.options.plot_options.venn>`
    - :class:`VennOptions <highcharts_python.options.plot_options.venn.VennOptions>`
  * - :mod:`.plot_options.wordcloud <highcharts_python.options.plot_options.wordcloud>`
    - :class:`WordcloudOptions <highcharts_python.options.plot_options.wordcloud.WordcloudOptions>`
      :class:`RotationOptions <highcharts_python.options.plot_options.wordcloud.RotationOptions>`
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
    - :class:`Title <highcharts_python.options.title.Title>`
  * - :mod:`.options.tooltips <highcharts_python.options.tooltips>`
    - :class:`Tooltip <highcharts_python.options.tooltips.Tooltip>`
  * - :mod:`.options.series <highcharts_python.options.series>`
    -
  * - :mod:`.options.series.arcdiagram <highcharts_python.options.series.arcdiagram>`
    - :class:`ArcDiagramSeries <highcharts_python.options.series.arcdiagram.ArcDiagramSeries>`
  * - :mod:`.options.series.area <highcharts_python.options.series.area>`
    - :class:`AreaSeries <highcharts_python.options.series.area.AreaSeries>`
      :class:`AreaRangeSeries <highcharts_python.options.series.area.AreaRangeSeries>`
      :class:`AreaSplineSeries <highcharts_python.options.series.area.AreaSplineSeries>`
      :class:`AreaSplineRangeSeries <highcharts_python.options.series.area.AreaSplineRangeSeries>`
      :class:`LineSeries <highcharts_python.options.series.area.LineSeries>`
      :class:`StreamGraphSeries <highcharts_python.options.series.area.StreamGraphSeries>`
  * - :mod:`.options.series.bar <highcharts_python.options.series.bar>`
    - :class:`BarSeries <highcharts_python.options.series.bar.BarSeries>`
      :class:`ColumnSeries <highcharts_python.options.series.bar.ColumnSeries>`
      :class:`ColumnPyramidSeries <highcharts_python.options.series.bar.ColumnPyramidSeries>`
      :class:`ColumnRangeSeries <highcharts_python.options.series.bar.ColumnRangeSeries>`
      :class:`CylinderSeries <highcharts_python.options.series.bar.CylinderSeries>`
      :class:`VariwideSeries <highcharts_python.options.series.bar.VariwideSeries>`
      :class:`WaterfallSeries <highcharts_python.options.series.bar.WaterfallSeries>`
      :class:`WindBarbSeries <highcharts_python.options.series.bar.WindBarbSeries>`
      :class:`XRangeSeries <highcharts_python.options.series.bar.XRangeSeries>`
      :class:`BaseBarSeries <highcharts_python.options.series.bar.BaseBarSeries>`
  * - :mod:`.options.series.base <highcharts_python.options.series.base>`
    - :class:`SeriesBase <highcharts_python.options.series.base.SeriesBase>`
  * - :mod:`.options.series.bellcurve <highcharts_python.options.series.bellcurve>`
    - :class:`BellCurveSeries <highcharts_python.options.series.bellcurve.BellCurveSeries>`
  * - :mod:`.options.series.boxplot <highcharts_python.options.series.boxplot>`
    - :class:`BoxPlotSeries <highcharts_python.options.series.boxplot.BoxPlotSeries>`
      :class:`ErrorBarSeries <highcharts_python.options.series.boxplot.ErrorBarSeries>`
  * - :mod:`.options.series.bubble <highcharts_python.options.series.bubble>`
    - :class:`BubbleSeries <highcharts_python.options.series.bubble.BubbleSeries>`
  * - :mod:`.options.series.bullet <highcharts_python.options.series.bullet>`
    - :class:`BulletSeries <highcharts_python.options.series.bullet.BulletSeries>`
  * - :mod:`.options.series.data <highcharts_python.options.series.data>`
    -
  * - :mod:`.options.series.data.accessibility <highcharts_python.options.series.data.accessibility>`
    - :class:`DataPointAccessibility <highcharts_python.options.series.data.accessibility.DataPointAccessibility>`
  * - :mod:`.options.series.data.arcdiagram <highcharts_python.options.series.data.arcdiagram>`
    - :class:`ArcDiagramData <highcharts_python.options.series.data.arcdiagram.ArcDiagramData>`
  * - :mod:`.options.series.data.bar <highcharts_python.options.series.data.bar>`
    - :class:`BarData <highcharts_python.options.series.data.bar.BarData>`
      :class:`WaterfallData <highcharts_python.options.series.data.bar.WaterfallData>`
      :class:`WindBarbData <highcharts_python.options.series.data.bar.WindBarbData>`
      :class:`XRangeData <highcharts_python.options.series.data.bar.XRangeData>`
  * - :mod:`.options.series.data.base <highcharts_python.options.series.data.base>`
    - :class:`DataBase <highcharts_python.options.series.data.base.DataBase>`
  * - :mod:`.options.series.data.boxplot <highcharts_python.options.series.data.boxplot>`
    - :class:`BoxPlotData <highcharts_python.options.series.data.boxplot.BoxPlotData>`
  * - :mod:`.options.series.data.bullet <highcharts_python.options.series.data.bullet>`
    - :class:`BulletData <highcharts_python.options.series.data.bullet.BulletData>`
  * - :mod:`.options.series.data.cartesian <highcharts_python.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_python.options.series.data.cartesian.CartesianData>`
      :class:`Cartesian3DData <highcharts_python.options.series.data.cartesian.Cartesian3DData>`
      :class:`CartesianValueData <highcharts_python.options.series.data.cartesian.CartesianValueData>`
  * - :mod:`.options.series.data.connections <highcharts_python.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_python.options.series.data.connections.ConnectionData>`
      :class:`WeightedConnectionData <highcharts_python.options.series.data.connections.WeightedConnectionData>`
      :class:`OutgoingWeightedConnectionData <highcharts_python.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`ConnectionBase <highcharts_python.options.series.data.connections.ConnectionBase>`
  * - :mod:`.options.series.data.pie <highcharts_python.options.series.data.pie>`
    - :class:`PieData <highcharts_python.options.series.data.pie.PieData>`
      :class:`VariablePieData <highcharts_python.options.series.data.pie.VariablePieData>`
  * - :mod:`.options.series.data.range <highcharts_python.options.series.data.range>`
    - :class:`RangeData <highcharts_python.options.series.data.range.RangeData>`
      :class:`ConnectedRangeData <highcharts_python.options.series.data.range.ConnectedRangeData>`
  * - :mod:`.options.series.data.single_point <highcharts_python.options.series.data.single_point>`
    - :class:`SinglePointData <highcharts_python.options.series.data.single_point.SinglePointData>`
      :class:`SingleValueData <highcharts_python.options.series.data.single_point.SingleValueData>`
      :class:`SingleXData <highcharts_python.options.series.data.single_point.SingleXData>`
      :class:`LabeledSingleXData <highcharts_python.options.series.data.single_point.LabeledSingleXData>`
      :class:`ConnectedSingleXData <highcharts_python.options.series.data.single_point.ConnectedSingleXData>`
      :class:`SinglePointBase <highcharts_python.options.series.data.single_point.SinglePointBase>`
  * - :mod:`.options.series.data.sunburst <highcharts_python.options.series.data.sunburst>`
    - :class:`SunburstData <highcharts_python.options.series.data.sunburst.SunburstData>`
  * - :mod:`.options.series.data.treemap <highcharts_python.options.series.data.treemap>`
    - :class:`TreemapData <highcharts_python.options.series.data.treemap.TreemapData>`
  * - :mod:`.options.series.data.vector <highcharts_python.options.series.data.vector>`
    - :class:`VectorData <highcharts_python.options.series.data.vector.VectorData>`
  * - :mod:`.options.series.data.venn <highcharts_python.options.series.data.venn>`
    - :class:`VennData <highcharts_python.options.series.data.venn.VennData>`
  * - :mod:`.options.series.data.wordcloud <highcharts_python.options.series.data.wordcloud>`
    - :class:`WordcloudData <highcharts_python.options.series.data.wordcloud.WordcloudData>`
  * - :mod:`.options.series.dependencywheel <highcharts_python.options.series.dependencywheel>`
    - :class:`DependencyWheelSeries <highcharts_python.options.series.dependencywheel.DependencyWheelSeries>`
  * - :mod:`.options.series.dumbbell <highcharts_python.options.series.dumbbell>`
    - :class:`DumbbellSeries <highcharts_python.options.series.dumbbell.DumbbellSeries>`
      :class:`LollipopSeries <highcharts_python.options.series.dumbbell.LollipopSeries>`
  * - :mod:`.options.series.funnel <highcharts_python.options.series.funnel>`
    - :class:`FunnelSeries <highcharts_python.options.series.funnel.FunnelSeries>`
      :class:`Funnel3DSeries <highcharts_python.options.series.funnel.Funnel3DSeries>`
  * - :mod:`.options.series.gauge <highcharts_python.options.series.gauge>`
    - :class:`GaugeSeries <highcharts_python.options.series.gauge.GaugeSeries>`
      :class:`SolidGaugeSeries <highcharts_python.options.series.gauge.SolidGaugeSeries>`
  * - :mod:`.options.series.Heatmap <highcharts_python.options.series.Heatmap>`
    - :class:`HeatmapSeries <highcharts_python.options.series.Heatmap.HeatmapSeries>`
      :class:`TilemapSeries <highcharts_python.options.series.Tilemap.TilemapSeries>`
  * - :mod:`.options.series.histogram <highcharts_python.options.series.histogram>`
    - :class:`HistogramSeries <highcharts_python.options.series.histogram.HistogramSeries>`
  * - :mod:`.options.series.item <highcharts_python.options.series.item>`
    - :class:`ItemSeries <highcharts_python.options.series.item.ItemSeries>`
  * - :mod:`.options.series.labels <highcharts_python.options.series.labels>`
    - :class:`SeriesLabel <highcharts_python.options.series.labels.SeriesLabel>`
      :class:`Box <highcharts_python.options.series.labels.Box>`
  * - :mod:`.options.series.networkgraph <highcharts_python.options.series.networkgraph>`
    - :class:`NetworkGraphSeries <highcharts_python.options.series.networkgraph.NetworkGraphSeries>`
  * - :mod:`.options.series.organization <highcharts_python.options.series.organization>`
    - :class:`OrganizationSeries <highcharts_python.options.series.organization.OrganizationSeries>`
  * - :mod:`.options.series.packedbubble <highcharts_python.options.series.packedbubble>`
    - :class:`PackedBubbleSeries <highcharts_python.options.series.packedbubble.PackedBubbleSeries>`
  * - :mod:`.options.series.pareto <highcharts_python.options.series.pareto>`
    - :class:`ParetoSeries <highcharts_python.options.series.pareto.ParetoSeries>`
  * - :mod:`.options.series.pie <highcharts_python.options.series.pie>`
    - :class:`PieSeries <highcharts_python.options.series.pie.PieSeries>`
      :class:`VariablePieSeries <highcharts_python.options.series.pie.VariablePieSeries>`
  * - :mod:`.options.series.polygon <highcharts_python.options.series.polygon>`
    - :class:`PolygonSeries <highcharts_python.options.series.polygon.PolygonSeries>`
  * - :mod:`.options.series.pyramid <highcharts_python.options.series.pyramid>`
    - :class:`PyramidSeries <highcharts_python.options.series.pyramid.PyramidSeries>`
      :class:`Pyramid3DSeries <highcharts_python.options.series.pyramid.Pyramid3DSeries>`
  * - :mod:`.options.series.sankey <highcharts_python.options.series.sankey>`
    - :class:`SankeySeries <highcharts_python.options.series.sankey.SankeySeries>`
  * - :mod:`.options.series.scatter <highcharts_python.options.series.scatter>`
    - :class:`ScatterSeries <highcharts_python.options.series.scatter.ScatterSeries>`
      :class:`Scatter3DSeries <highcharts_python.options.series.scatter.Scatter3DSeries>`
  * - :mod:`.options.series.series_generator <highcharts_python.options.series.series_generator>`
    - :func:`create_series_obj() <highcharts_python.options.series.series_generator.create_series_obj>`
  * - :mod:`.options.series.spline <highcharts_python.options.series.spline>`
    - :class:`SplineSeries <highcharts_python.options.series.spline.SplineSeries>`
  * - :mod:`.options.series.sunburst <highcharts_python.options.series.sunburst>`
    - :class:`SunburstSeries <highcharts_python.options.series.sunburst.SunburstSeries>`
  * - :mod:`.options.series.timeline <highcharts_python.options.series.timeline>`
    - :class:`TimelineSeries <highcharts_python.options.series.timeline.TimelineSeries>`
  * - :mod:`.options.series.treemap <highcharts_python.options.series.treemap>`
    - :class:`TreemapSeries <highcharts_python.options.series.treemap.TreemapSeries>`
  * - :mod:`.options.series.vector <highcharts_python.options.series.vector>`
    - :class:`VectorSeries <highcharts_python.options.series.vector.VectorSeries>`
  * - :mod:`.options.series.venn <highcharts_python.options.series.venn>`
    - :class:`VennSeries <highcharts_python.options.series.venn.VennSeries>`
  * - :mod:`.options.series.wordcloud <highcharts_python.options.series.wordcloud>`
    - :class:`WordcloudSeries <highcharts_python.options.series.wordcloud.WordcloudSeries>`
  * - :mod:`.utility_classes <highcharts_python.utility_classes>`
    -
  * - :mod:`.utility_classes.animation <highcharts_python.utility_classes.animation>`
    - :class:`AnimationOptions <highcharts_python.utility_classes.animation.AnimationOptions>`
  * - :mod:`.utility_classes.ast <highcharts_python.utility_classes.ast>`
    - :class:`ASTMap <highcharts_python.utility_classes.ast.ASTMap>`
      :class:`ASTNode <highcharts_python.utility_classes.ast.ASTNode>`
      :class:`TextPath <highcharts_python.utility_classes.ast.TextPath>`
      :class:`AttributeObject <highcharts_python.utility_classes.ast.AttributeObject>`
  * - :mod:`.utility_classes.breadcrumbs <highcharts_python.utility_classes.breadcrumbs>`
    - :class:`BreadcrumbOptions <highcharts_python.utility_classes.breadcrumbs.BreadcrumbOptions>`
      :class:`Separator <highcharts_python.utility_classes.breadcrumbs.Separator>`
  * - :mod:`.utility_classes.buttons <highcharts_python.utility_classes.buttons>`
    - :class:`ExportingButtons <highcharts_python.utility_classes.buttons.ExportingButtons>`
      :class:`ContextButtonConfiguration <highcharts_python.utility_classes.buttons.ContextButtonConfiguration>`
      :class:`ButtonConfiguration <highcharts_python.utility_classes.buttons.ButtonConfiguration>`
      :class:`ButtonTheme <highcharts_python.utility_classes.buttons.ButtonTheme>`
  * - :mod:`.utility_classes.clusters <highcharts_python.utility_classes.clusters>`
    - :class:`ClusterOptions <highcharts_python.utility_classes.clusters.ClusterOptions>`
      :class:`VectorLayoutAlgorithm <highcharts_python.utility_classes.clusters.VectorLayoutAlgorithm>`
  * - :mod:`.utility_classes.data_grouping <highcharts_python.utility_classes.data_grouping>`
    - :class:`DataGroupingOptions <highcharts_python.utility_classes.data_grouping.DataGroupingOptions>`
  * - :mod:`.utility_classes.data_labels <highcharts_python.utility_classes.data_labels>`
    - :class:`DataLabel <highcharts_python.utility_classes.data_labels.DataLabel>`
      :class:`NodeDataLabel <highcharts_python.utility_classes.data_labels.NodeDataLabel>`
      :class:`Filter <highcharts_python.utility_classes.data_labels.Filter>`
  * - :mod:`.utility_classes.date_time_label_formats <highcharts_python.utility_classes.date_time_label_formats>`
    - :class:`DateTimeLabelFormats <highcharts_python.utility_classes.date_time_label_formats.DateTimeLabelFormats>`
  * - :mod:`.utility_classes.events <highcharts_python.utility_classes.events>`
    - :class:`ChartEvents <highcharts_python.utility_classes.events.ChartEvents>`
      :class:`BreadcrumbEvents <highcharts_python.utility_classes.events.BreadcrumbEvents>`
      :class:`NavigationEvents <highcharts_python.utility_classes.events.NavigationEvents>`
      :class:`PointEvents <highcharts_python.utility_classes.events.PointEvents>`
      :class:`SeriesEvents <highcharts_python.utility_classes.events.SeriesEvents>`
      :class:`ClusterEvents <highcharts_python.utility_classes.events.ClusterEvents>`
      :class:`AxisEvents <highcharts_python.utility_classes.events.AxisEvents>`
      :class:`MouseEvents <highcharts_python.utility_classes.events.MouseEvents>`
  * - :mod:`.utility_classes.gradients <highcharts_python.utility_classes.gradients>`
    - :class:`Gradient <highcharts_python.utility_classes.gradients.Gradient>`
      :class:`LinearGradient <highcharts_python.utility_classes.gradients.LinearGradient>`
      :class:`RadialGradient <highcharts_python.utility_classes.gradients.RadialGradient>`
  * - :mod:`.utility_classes.javascript_functions <highcharts_python.utility_classes.javascript_functions>`
    - :class:`CallbackFunction <highcharts_python.utility_classes.javascript_functions.CallbackFunction>`
      :class:`JavaScriptClass <highcharts_python.utility_classes.javascript_functions.JavaScriptClass>`
  * - :mod:`.utility_classes.jitter <highcharts_python.utility_classes.jitter>`
    - :class:`Jitter <highcharts_python.utility_classes.jitter.Jitter>`
  * - :mod:`.utility_classes.markers <highcharts_python.utility_classes.markers>`
    - :class:`Marker <highcharts_python.utility_classes.markers.Marker>`
  * - :mod:`.utility_classes.menus <highcharts_python.utility_classes.menus>`
    - :class:`MenuObject <highcharts_python.utility_classes.menus.MenuObject>`
      :class:`MenuItem <highcharts_python.utility_classes.menus.MenuItem>`
  * - :mod:`.utility_classes.nodes <highcharts_python.utility_classes.nodes>`
    - :class:`NodeOptions <highcharts_python.utility_classes.nodes.NodeOptions>`
      :class:`DependencyWheelNodeOptions <highcharts_python.utility_classes.nodes.DependencyWheelNodeOptions>`
      :class:`OrganizationNodeOptions <highcharts_python.utility_classes.nodes.OrganizationNodeOptions>`
  * - :mod:`.utility_classes.partial_fill <highcharts_python.utility_classes.partial_fill>`
    - :class:`PartialFillOptions <highcharts_python.utility_classes.partial_fill.PartialFillOptions>`
  * - :mod:`.utility_classes.patterns <highcharts_python.utility_classes.patterns>`
    - :class:`Pattern <highcharts_python.utility_classes.patterns.Pattern>`
      :class:`PatternOptions <highcharts_python.utility_classes.patterns.PatternOptions>`
  * - :mod:`.utility_classes.position <highcharts_python.utility_classes.position>`
    - :class:`Position <highcharts_python.utility_classes.position.Position>`
  * - :mod:`.utility_classes.shadows <highcharts_python.utility_classes.shadows>`
    - :class:`ShadowOptions <highcharts_python.utility_classes.shadows.ShadowOptions>`
  * - :mod:`.utility_classes.states <highcharts_python.utility_classes.states>`
    - :class:`States <highcharts_python.utility_classes.states.States>`
      :class:`HoverState <highcharts_python.utility_classes.states.HoverState>`
      :class:`InactiveState <highcharts_python.utility_classes.states.InactiveState>`
      :class:`NormalState <highcharts_python.utility_classes.states.NormalState>`
      :class:`SelectState <highcharts_python.utility_classes.states.SelectState>`
  * - :mod:`.utility_classes.zones <highcharts_python.utility_classes.zones>`
    - :class:`Zone <highcharts_python.utility_classes.zones.Zone>`
      :class:`ClusterZone <highcharts_python.utility_classes.zones.ClusterZone>`

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

.. toctree::
  :hidden:

  Internal Reference <api/internals>

While most users will be interacting with the :doc:`Core Components <core_components>` of
**Highcharts for Python**, you may need (or choose to) work with various internals of the
library. If you're :doc:`contributing` to the library, then you will definitely need to
familiarize yourself with these internals.

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.metaclasses <highcharts_python.metaclasses>`
    - :class:`HighchartsMeta <highcharts_python.metaclasses.HighchartsMeta>`
      :class:`JavaScriptDict <highcharts_python.metaclasses.JavaScriptDict>`
  * - :mod:`.decorators <highcharts_python.decorators>`
    - :deco:`@class_sensitive() <highcharts_python.decorators.class_sensitive>`
      :func:`validate_types() <highcharts_python.decorators.validate_types>`
  * - :mod:`.js_literal_functions <highcharts_python.js_literal_functions>`
    - :func:`serialize_to_js_literal() <highcharts_python.js_literal_functions.serialize_to_js_literal>`
      :func:`attempt_variable_declaration() <highcharts_python.js_literal_functions.attempt_variable_declaration>`
      :func:`is_js_function_or_class() <highcharts_python.js_literal_functions.is_js_function_or_class>`
      :func:`get_js_literal() <highcharts_python.js_literal_functions.get_js_literal>`
      :func:`assemble_js_literal() <highcharts_python.js_literal_functions.assemble_js_literal>`
      :func:`convert_js_literal_to_python() <highcharts_python.js_literal_functions.convert_js_literal_to_python>`
      :func:`convert_js_property_to_python() <highcharts_python.js_literal_functions.convert_js_property_to_python>`
      :func:`convert_js_to_python() <highcharts_python.js_literal_functions.convert_js_to_python>`
      :func:`get_key_value_pairs() <highcharts_python.js_literal_functions.get_key_value_pairs>`
  * - :mod:`.utility_functions <highcharts_python.utility_functions>`
    - :func:`mro_to_dict() <highcharts_python.utility_functions.mro_to_dict>`
      :func:`get_remaining_mro() <highcharts_python.utility_functions.get_remaining_mro>`
      :func:`mro__to_untrimmed_dict() <highcharts_python.utility_functions.mro__to_untrimmed_dict>`
      :func:`validate_color() <highcharts_python.utility_functions.validate_color>`
      :func:`to_camelCase() <highcharts_python.utility_functions.to_camelCase>`
      :func:`parse_csv() <highcharts_python.utility_functions.parse_csv>`
