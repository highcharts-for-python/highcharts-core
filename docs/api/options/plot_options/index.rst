################################################################
:mod:`.plot_options <highcharts_core.options.plot_options>`
################################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  accessibility
  arcdiagram
  area
  bar
  bellcurve
  boxplot
  bubble
  bullet
  data_sorting
  dependencywheel
  drag_drop
  dumbbell
  funnel
  gauge
  generic
  heatmap
  histogram
  item
  levels
  link
  networkgraph
  organization
  packedbubble
  pareto
  pictorial
  pie
  points
  polygon
  pyramid
  sankey
  scatter
  series
  sonification
  spline
  sunburst
  timeline
  treegraph
  treemap
  vector
  venn
  wordcloud

-------------------------

.. module:: highcharts_core.options.plot_options

********************************************************************************************************************
class: :class:`PlotOptions <highcharts_core.options.plot_options.PlotOptions>`
********************************************************************************************************************

.. autoclass:: PlotOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: PlotOptions
      :top-classes: highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

  |

--------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
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
  * - :mod:`.options.series.treegraph <highcharts_core.options.series.treegraph>`
    - :class:`TreegraphSeries <highcharts_core.options.series.treegraph.TreegraphSeries>`
  * - :mod:`.options.plot_options.treemap <highcharts_core.options.plot_options.treemap>`
    - :class:`TreemapOptions <highcharts_core.options.plot_options.treemap.TreemapOptions>`
  * - :mod:`.options.plot_options.vector <highcharts_core.options.plot_options.vector>`
    - :class:`VectorOptions <highcharts_core.options.plot_options.vector.VectorOptions>`
  * - :mod:`.options.plot_options.venn <highcharts_core.options.plot_options.venn>`
    - :class:`VennOptions <highcharts_core.options.plot_options.venn.VennOptions>`
  * - :mod:`.options.plot_options.wordcloud <highcharts_core.options.plot_options.wordcloud>`
    - :class:`WordcloudOptions <highcharts_core.options.plot_options.wordcloud.WordcloudOptions>`
      :class:`RotationOptions <highcharts_core.options.plot_options.wordcloud.RotationOptions>`
