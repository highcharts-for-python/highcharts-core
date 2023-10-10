##############################################################
:mod:`.options <highcharts_core.options>`
##############################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  accessibility/index
  annotations/index
  axes/index
  boost
  caption
  chart/index
  credits
  data
  defs
  drilldown
  exporting/index
  legend/index
  loading
  navigation/index
  no_data
  pane
  plot_options/index
  responsive
  series/color_index
  sonification/index
  subtitle
  time
  title
  tooltips

--------------

.. module:: highcharts_core.options

****************************************************************************************
class: :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`
****************************************************************************************

.. autoclass:: HighchartsOptions
  :members:
  :inherited-members:
  :special-members: __str__, __repr__

-----------------------

****************************************************************************************
class: :class:`Options <highcharts_core.options.Options>`
****************************************************************************************

.. autoclass:: Options
  :members:
  :inherited-members:
  :special-members: __str__, __repr__

-----------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
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
    - :class:`TreegraphSeries <highcharts_core.options.plot_options.treegraph.TreegraphSeries>`
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
      :class:`ArcDiagramDataCollection <highcharts_core.options.series.data.arcidagram.ArcDiagramDataCollection>`
  * - :mod:`.options.series.data.bar <highcharts_core.options.series.data.bar>`
    - :class:`BarData <highcharts_core.options.series.data.bar.BarData>`
      :class:`BarDataCollection <highcharts_core.options.series.data.bar.BarDataCollection>`
      :class:`WaterfallData <highcharts_core.options.series.data.bar.WaterfallData>`
      :class:`WaterfallDataCollection <highcharts_core.options.series.data.bar.WaterfallDataCollection>`
      :class:`WindBarbData <highcharts_core.options.series.data.bar.WindBarbData>`
      :class:`WindBarbDataCollection <highcharts_core.options.series.data.bar.WindBarbDataCollection>`
      :class:`XRangeData <highcharts_core.options.series.data.bar.XRangeData>`
      :class:`XRangeDataCollection <highcharts_core.options.series.data.bar.XRangeDataCollection>`
  * - :mod:`.options.series.data.base <highcharts_core.options.series.data.base>`
    - :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`
  * - :mod:`.options.series.data.boxplot <highcharts_core.options.series.data.boxplot>`
    - :class:`BoxPlotData <highcharts_core.options.series.data.boxplot.BoxPlotData>`
      :class:`BoxPlotDataCollection <highcharts_core.options.series.data.boxplot.BoxPlotDataCollection>`
  * - :mod:`.options.series.data.bullet <highcharts_core.options.series.data.bullet>`
    - :class:`BulletData <highcharts_core.options.series.data.bullet.BulletData>`
      :class:`BulletDataCollection <highcharts_core.options.series.data.bullet.BulletDataCollection>`
  * - :mod:`.options.series.data.cartesian <highcharts_core.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_core.options.series.data.cartesian.CartesianData>`
      :class:`CartesianDataCollection <highcharts_core.options.series.data.cartesian.CartesianDataCollection>`
      :class:`Cartesian3DData <highcharts_core.options.series.data.cartesian.Cartesian3DData>`
      :class:`Cartesian3DDataCollection <highcharts_core.options.series.data.cartesian.Cartesian3DDataCollection>`
      :class:`CartesianValueData <highcharts_core.options.series.data.cartesian.CartesianValueData>`
      :class:`CartesianValueDataCollection <highcharts_core.options.series.data.cartesian.CartesianValueDataCollection>`
  * - :mod:`.options.series.data.collections <highcharts_core.options.series.data.collections>`
    - :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
  * - :mod:`.options.series.data.connections <highcharts_core.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_core.options.series.data.connections.ConnectionData>`
      :class:`ConnectionDataCollection <highcharts_core.options.series.data.connections.ConnectionDataCollection>`
      :class:`WeightedConnectionData <highcharts_core.options.series.data.connections.WeightedConnectionData>`
      :class:`WeightedConnectionDataCollection <highcharts_core.options.series.data.connections.WeightedConnectionDataCollection>`
      :class:`OutgoingWeightedConnectionData <highcharts_core.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`OutgoingWeightedConnectionDataCollection <highcharts_core.options.series.data.connections.OutgoingWeightedConnectionDataCollection>`
      :class:`ConnectionBase <highcharts_core.options.series.data.connections.ConnectionBase>`
  * - :mod:`.options.series.data.pie <highcharts_core.options.series.data.pie>`
    - :class:`PieData <highcharts_core.options.series.data.pie.PieData>`
      :class:`PieDataCollection <highcharts_core.options.series.data.pie.PieDataCollection>`
      :class:`VariablePieData <highcharts_core.options.series.data.pie.VariablePieData>`
      :class:`VariablePieDataCollection <highcharts_core.options.series.data.pie.VariablePieDataCollection>`
  * - :mod:`.options.series.data.range <highcharts_core.options.series.data.range>`
    - :class:`RangeData <highcharts_core.options.series.data.range.RangeData>`
      :class:`RangeDataCollection <highcharts_core.options.series.data.range.RangeDataCollection>`
      :class:`ConnectedRangeData <highcharts_core.options.series.data.range.ConnectedRangeData>`
      :class:`ConnectedRangeDataCollection <highcharts_core.options.series.data.range.ConnectedRangeDataCollection>`
  * - :mod:`.options.series.data.single_point <highcharts_core.options.series.data.single_point>`
    - :class:`SinglePointData <highcharts_core.options.series.data.single_point.SinglePointData>`
      :class:`SinglePointDataCollection <highcharts_core.options.series.data.single_point.SinglePointDataCollection>`
      :class:`SingleValueData <highcharts_core.options.series.data.single_point.SingleValueData>`
      :class:`SingleValueDataCollection <highcharts_core.options.series.data.single_point.SingleValueDataCollection>`
      :class:`SingleXData <highcharts_core.options.series.data.single_point.SingleXData>`
      :class:`SingleXDataCollection <highcharts_core.options.series.data.single_point.SingleXDataCollection>`
      :class:`LabeledSingleXData <highcharts_core.options.series.data.single_point.LabeledSingleXData>`
      :class:`LabeledSingleXDataCollection <highcharts_core.options.series.data.single_point.LabeledSingleXDataCollection>`
      :class:`ConnectedSingleXData <highcharts_core.options.series.data.single_point.ConnectedSingleXData>`
      :class:`ConnectedSingleXDataCollection <highcharts_core.options.series.data.single_point.ConnectedSingleXDataCollection>`
      :class:`SinglePointBase <highcharts_core.options.series.data.single_point.SinglePointBase>`
  * - :mod:`.options.series.data.sunburst <highcharts_core.options.series.data.sunburst>`
    - :class:`SunburstData <highcharts_core.options.series.data.sunburst.SunburstData>`
      :class:`SunburstDataCollection <highcharts_core.options.series.data.sunburst.SunburstDataCollection>`
  * - :mod:`.options.series.data.treegraph <highcharts_core.options.series.data.treegraph>`
    - :class:`TreegraphData <highcharts_core.options.series.data.treegraph.TreegraphData>`
      :class:`TreegraphDataCollection <highcharts_core.options.series.data.treegraph.TreegraphDataCollection>`
  * - :mod:`.options.series.data.treemap <highcharts_core.options.series.data.treemap>`
    - :class:`TreemapData <highcharts_core.options.series.data.treemap.TreemapData>`
      :class:`TreemapDataCollection <highcharts_core.options.series.data.treemap.TreemapDataCollection>`
  * - :mod:`.options.series.data.vector <highcharts_core.options.series.data.vector>`
    - :class:`VectorData <highcharts_core.options.series.data.vector.VectorData>`
      :class:`VectorDataCollection <highcharts_core.options.series.data.vector.VectorDataCollection>`
  * - :mod:`.options.series.data.venn <highcharts_core.options.series.data.venn>`
    - :class:`VennData <highcharts_core.options.series.data.venn.VennData>`
      :class:`VennDataCollection <highcharts_core.options.series.data.venn.VennDataCollection>`
  * - :mod:`.options.series.data.wordcloud <highcharts_core.options.series.data.wordcloud>`
    - :class:`WordcloudData <highcharts_core.options.series.data.wordcloud.WordcloudData>`
      :class:`WordcloudDataCollection <highcharts_core.options.series.data.wordcloud.WordcloudDataCollection>`
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
      :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>`
      :class:`AudioFilter <highcharts_core.options.sonification.mapping.AudioFilter>`
      :class:`PitchParameter <highcharts_core.options.sonification.mapping.PitchParameter>`
      :class:`TremoloEffect <highcharts_core.options.sonification.mapping.TremoloEffect>`
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
