################################################################
:mod:`.plot_options <highcharts_python.options.plot_options>`
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
  pie
  points
  polygon
  pyramid
  sankey
  scatter
  series
  spline
  sunburst
  timeline
  treemap
  vector
  venn
  wordcloud

-------------------------

.. module:: highcharts_python.options.plot_options

********************************************************************************************************************
class: :class:`PlotOptions <highcharts_python.options.plot_options.PlotOptions>`
********************************************************************************************************************

.. autoclass:: PlotOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: PlotOptions
      :top-classes: highcharts_python.metaclasses.HighchartsMeta
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
  * - :mod:`.plot_options.heatmap <highcharts_python.options.plot_options.heatmap>`
    - :class:`HeatmapOptions <highcharts_python.options.plot_options.heatmap.HeatmapOptions>`
      :class:`TilemapOptions <highcharts_python.options.plot_options.heatmap.TilemapOptions>`
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
