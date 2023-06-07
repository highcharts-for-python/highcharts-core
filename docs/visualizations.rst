################################
Supported Visualizations
################################

.. contents::
  :depth: 3
  :backlinks: entry

--------------

As the tables below make clear, the **Highcharts for Python Toolkit** and the
`Highcharts <https://www.highcharts.com/>`__ suite of JavaScript libraries are likely the
single most comprehensive suite of data visualization tools available in the market. With
over 70 (seventy!) distinct data visualizations and 50 (fifty!)
:term:`technical indicators <technical indicator>`, you will be able to construct a
beautiful and interactive portrayal of your data.

.. _series_with_data:

******************************************
Series with Data
******************************************

The following are the series types that have ``.data`` properties and which can be used
to visualize your data.

.. seealso::

  * :doc:`Using Highcharts for Python <using>` > :ref:`Working with Data <working_with_data>`
  * :doc:`Using Highcharts for Python <using>` > :ref:`Adding Series to Charts <adding_series_to_charts>`
  * :doc:`Using Highcharts for Python <using>` > :ref:`Populating Series Data <populating_series_data>`

.. tabs::

  .. tab:: Core

    .. note::

      The visualizations below are provided by **Highcharts Core for Python** and
      `Highcharts Core (JS) <https://www.highcharts.com/products/highcharts/>`__. They are also
      available in the other libraries within the toolkit.

    .. list-table::
      :widths: 10 90
      :header-rows: 1

      * - Series Type
        - Screenshot + Class Links
      * - **Arc Diagram**
        - .. figure:: _static/arcdiagram-example.png
            :alt: Arc Diagram Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.arcdiagram.ArcDiagramOptions`

          :class:`highcharts_core.options.series.arcdiagram.ArcDiagramSeries`
      * - **Area**
        - .. figure:: _static/area-example.png
            :alt: Area Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.area.AreaOptions`

          :class:`highcharts_core.options.series.area.AreaSeries`
      * - **Area Range**
        - .. figure:: _static/arearange-example.png
            :alt: Area Range Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.area.AreaRangeOptions`

          :class:`highcharts_core.options.series.area.AreaRangeSeries`
      * - **Area Spline**
        - .. figure:: _static/areaspline-example.png
            :alt: Area Spline Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.area.AreaSplineOptions`

          :class:`highcharts_core.options.series.area.AreaSplineSeries`
      * - **Area Spline Range**
        - .. figure:: _static/areasplinerange-example.png
            :alt: Area Spline Range Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.area.AreaSplineRangeOptions`

          :class:`highcharts_core.options.series.area.AreaSplineRangeSeries`
      * - **Bar**
        - .. figure:: _static/bar-example.png
            :alt: Bar Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.bar.BarOptions`

          :class:`highcharts_core.options.series.bar.BarSeries`
      * - **Bell Curve**
        - .. figure:: _static/bellcurve-example.png
            :alt: BellCurve Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.bellcurve.BellCurveOptions`

          :class:`highcharts_core.options.series.bellcurve.BellCurveSeries`
      * - **Box Plot**
        - .. figure:: _static/boxplot-example.png
            :alt: BoxPlot Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.boxplot.BoxPlotOptions`

          :class:`highcharts_core.options.series.boxplot.BoxPlotSeries`
      * - **Bubble**
        - .. figure:: _static/bubble-example.png
            :alt: Bubble Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.bubble.BubbleOptions`

          :class:`highcharts_core.options.series.bubble.BubbleSeries`
      * - **Bullet**
        - .. figure:: _static/bullet-example.png
            :alt: Bullet Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.bullet.BulletOptions`

          :class:`highcharts_core.options.series.bullet.BulletSeries`
      * - **Column**
        - .. figure:: _static/column-example.png
            :alt: Column Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.bar.ColumnOptions`

          :class:`highcharts_core.options.series.bar.ColumnSeries`
      * - **Column Pyramid**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/columnpyramid-example.png
                :alt: ColumnPyramid Example Chart
                :width: 100%

            .. tab:: Stacked

              .. figure:: _static/columnpyramid-example-stacked.png
                :alt: Stacked Column Pyramid Example Chart
                :width: 100%

            .. tab:: Stacked + Inverted

              .. figure:: _static/columnpyramid-example-stacked-horizontal.png
                :alt: Stacked and Inverted Column Pyramid Example Chart
                :width: 100%

          :class:`highcharts_core.options.plot_options.bar.ColumnPyramidOptions`

          :class:`highcharts_core.options.series.bar.ColumnPyramidSeries`
      * - **Column Range**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/columnrange-example.png
                :alt: ColumnRange Example Chart
                :width: 100%

            .. tab:: Horizontal

              .. figure:: _static/columnrange-example-horizontal.png
                :alt: Inverted Column Range Example Chart
                :width: 100%

          :class:`highcharts_core.options.plot_options.bar.ColumnRangeOptions`

          :class:`highcharts_core.options.series.bar.ColumnRangeSeries`
      * - **Dependency Wheel**
        - .. figure:: _static/dependencywheel-example.png
            :alt: DependencyWheel Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.dependencywheel.DependencyWheelOptions`

          :class:`highcharts_core.options.series.dependencywheel.DependencyWheelSeries`
      * - **Dumbbell**
        - .. figure:: _static/dumbbell-example.png
            :alt: Dumbbell Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.dumbbell.DumbbellOptions`

          :class:`highcharts_core.options.series.dumbbell.DumbbellSeries`
      * - **Error Bar**
        - .. figure:: _static/errorbar-example.png
            :alt: ErrorBar Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.boxplot.ErrorBarOptions`

          :class:`highcharts_core.options.series.boxplot.ErrorBarSeries`
      * - **Funnel**
        - .. figure:: _static/funnel-example.png
            :alt: Funnel Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.funnel.FunnelOptions`

          :class:`highcharts_core.options.series.funnel.FunnelSeries`
      * - **Funnel 3D**
        - .. figure:: _static/funnel_3d-example.png
            :alt: Funnel3D Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.funnel.Funnel3DOptions`

          :class:`highcharts_core.options.series.funnel.Funnel3DSeries`
      * - **Gauge**
        - .. figure:: _static/gauge-example.png
            :alt: Gauge Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.gauge.GaugeOptions`

          :class:`highcharts_core.options.series.gauge.GaugeSeries`
      * - **Heatmap**
        - .. figure:: _static/heatmap-example.png
            :alt: Heatmap Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.heatmap.HeatmapOptions`

          :class:`highcharts_core.options.series.heatmap.HeatmapSeries`
      * - **Histogram**
        - .. figure:: _static/histogram-example.png
            :alt: Histogram Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.histogram.HistogramOptions`

          :class:`highcharts_core.options.series.histogram.HistogramSeries`
      * - **Item**
        - .. tabs::

            .. tab:: Circular

              .. figure:: _static/item-example-circular.png
                :alt: Circular Item Example Chart
                :width: 100%

            .. tab:: Rectangular

              .. figure:: _static/item-example-rectangular.png
                :alt: Rectangular Item Example Chart
                :width: 100%

            .. tab:: Symbols

              .. figure:: _static/item-example-symbols.png
                :alt: Item Example Chart with Symbols
                :width: 100%

          :class:`highcharts_core.options.plot_options.item.ItemOptions`

          :class:`highcharts_core.options.series.item.ItemSeries`
      * - **Line**
        - .. figure:: _static/line-example.png
            :alt: Line Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.area.LineOptions`

          :class:`highcharts_core.options.series.area.LineSeries`
      * - **Lollipop**
        - .. figure:: _static/lollipop-example.png
            :alt: Lollipop Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.dumbbell.LollipopOptions`

          :class:`highcharts_core.options.series.dumbbell.LollipopSeries`
      * - **Network Graph**
        - .. figure:: _static/networkgraph-example.png
            :alt: Network Graph Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.networkgraph.NetworkGraphOptions`

          :class:`highcharts_core.options.series.networkgraph.NetworkGraphSeries`
      * - **Organization**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/organization-example.png
                :alt: Organization Example Chart
                :width: 100%

            .. tab:: Horizontal

              .. figure:: _static/organization-example-horizontal.png
                :alt: Horizontal Organization Example Chart
                :width: 100%

          :class:`highcharts_core.options.plot_options.organization.OrganizationOptions`

          :class:`highcharts_core.options.series.organization.OrganizationSeries`
      * - **Packed Bubble**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/packedbubble-example.png
                :alt: Split Packed Bubble Example Chart
                :width: 100%

            .. tab:: Split

              .. figure:: _static/packedbubble-example-split.png
                :alt: Split Packed Bubble Example Chart
                :width: 100%

          :class:`highcharts_core.options.plot_options.packedbubble.PackedBubbleOptions`

          :class:`highcharts_core.options.series.packedbubble.PackedBubbleSeries`
      * - **Pareto**
        - .. figure:: _static/pareto-example.png
            :alt: Pareto Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.pareto.ParetoOptions`

          :class:`highcharts_core.options.series.pareto.ParetoSeries`
      * - **Pictorial**
        - .. figure:: _static/pictorial-example.png
            :alt: Pictorial Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.pictorial.PictorialOptions`

          :class:`highcharts_core.options.series.pictorial.PictorialSeries`
      * - **Pie**
        - .. tabs::

            .. tab:: Pie

              .. figure:: _static/pie-example.png
                :alt: Pie Example Chart
                :align: center

            .. tab:: Donut

              .. figure:: _static/pie-example-donut.png
                :alt: Donut Example Chart
                :align: center

          :class:`highcharts_core.options.plot_options.pie.PieOptions`

          :class:`highcharts_core.options.series.pie.PieSeries`
      * - **Polygon**
        - .. figure:: _static/polygon-example.png
            :alt: Polygon Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.polygon.PolygonOptions`

          :class:`highcharts_core.options.series.polygon.PolygonSeries`
      * - **Pyramid**
        - .. figure:: _static/pyramid-example.png
            :alt: Pyramid Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.pyramid.PyramidOptions`

          :class:`highcharts_core.options.series.pyramid.PyramidSeries`
      * - **Pyramid 3D**
        - .. figure:: _static/pyramid_3d-example.png
            :alt: Pyramid 3D Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.pyramid.Pyramid3DOptions`

          :class:`highcharts_core.options.series.pyramid.Pyramid3DSeries`
      * - **Sankey**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/sankey-example.png
                :alt: Sankey Example Chart
                :align: center

            .. tab:: Inverted

              .. figure:: _static/sankey-example-inverted.png
                :alt: Inverted Sankey Example Chart
                :align: center

            .. tab:: w/Outgoing Links

              .. figure:: _static/sankey-example-outgoing.png
                :alt: Sankey Example Chart with Outgoing Links
                :align: center

          :class:`highcharts_core.options.plot_options.sankey.SankeyOptions`

          :class:`highcharts_core.options.series.sankey.SankeySeries`
      * - **Scatter**
        - .. figure:: _static/scatter-example.png
            :alt: Scatter Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.scatter.ScatterOptions`

          :class:`highcharts_core.options.series.scatter.ScatterSeries`
      * - **Scatter 3D**
        - .. figure:: _static/scatter_3d-example.png
            :alt: Scatter 3D Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.scatter.Scatter3DOptions`

          :class:`highcharts_core.options.series.scatter.Scatter3DSeries`
      * - **Solid Gauge**
        - .. figure:: _static/solidgauge-example.png
            :alt: SolidGauge Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.gauge.SolidGaugeOptions`

          :class:`highcharts_core.options.series.gauge.SolidGaugeSeries`
      * - **Spline**
        - .. figure:: _static/spline-example.png
            :alt: Spline Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.spline.SplineOptions`

          :class:`highcharts_core.options.series.spline.SplineSeries`
      * - **Stream Graph**
        - .. figure:: _static/streamgraph-example.png
            :alt: StreamGraph Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.area.StreamGraphOptions`

          :class:`highcharts_core.options.series.area.StreamGraphSeries`
      * - **Sunburst**
        - .. figure:: _static/sunburst-example.png
            :alt: Sunburst Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.sunburst.SunburstOptions`

          :class:`highcharts_core.options.series.sunburst.SunburstSeries`
      * - **Tilemap**
        - .. figure:: _static/tilemap-example.png
            :alt: Tilemap Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.heatmap.TilemapOptions`

          :class:`highcharts_core.options.series.heatmap.TilemapSeries`
      * - **Timeline**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/timeline-example.png
                :alt: Timeline Example Chart
                :align: center

            .. tab:: Inverted

              .. figure:: _static/timeline-example-inverted.png
                :alt: Inverted Timeline Example Chart
                :align: center

            .. tab:: w/True Datetime Axis

              .. figure:: _static/timeline-example-datetime.png
                :alt: Timeline Example Chart with Datetime Axis
                :align: center

          :class:`highcharts_core.options.plot_options.timeline.TimelineOptions`

          :class:`highcharts_core.options.series.timeline.TimelineSeries`
      * - **Treegraph**
        - .. figure:: _static/treegraph-example.png
            :alt: Treegraph Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.treegraph.TreegraphOptions`

          :class:`highcharts_core.options.series.treegraph.TreegraphSeries`
      * - **Treemap**
        - .. figure:: _static/treemap-example.png
            :alt: Treemap Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.treemap.TreemapOptions`

          :class:`highcharts_core.options.series.treemap.TreemapSeries`
      * - **Variable Pie**
        - .. figure:: _static/variablepie-example.png
            :alt: VariablePie Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.pie.VariablePieOptions`

          :class:`highcharts_core.options.series.pie.VariablePieSeries`
      * - **Vector**
        - .. figure:: _static/vector-example.png
            :alt: Vector Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.vector.VectorOptions`

          :class:`highcharts_core.options.series.vector.VectorSeries`
      * - **Venn**
        - .. tabs::

            .. tab:: Venn Diagram

              .. figure:: _static/venn-example.png
                :alt: Venn Example Chart
                :align: center

            .. tab:: Euler Diagram

              .. figure:: _static/venn-example-euler.png
                :alt: Euler Example Chart
                :align: center

          :class:`highcharts_core.options.plot_options.venn.VennOptions`

          :class:`highcharts_core.options.series.venn.VennSeries`
      * - **Waterfall**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/waterfall-example.png
                :alt: Waterfall Example Chart
                :width: 100%

            .. tab:: Horizontal (Inverted)

              .. figure:: _static/waterfall-example-inverted.png
                :alt: Waterfall Example Chart
                :width: 100%

            .. tab:: Stacked

              .. figure:: _static/waterfall-example-stacked.png
                :alt: Waterfall Example Chart
                :width: 100%

          :class:`highcharts_core.options.plot_options.bar.WaterfallOptions`

          :class:`highcharts_core.options.series.bar.WaterfallSeries`
      * - **Wind Barb**
        - .. figure:: _static/windbarb-example.png
            :alt: WindBarb Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.bar.WindBarbOptions`

          :class:`highcharts_core.options.series.bar.WindBarbSeries`
      * - **Wordcloud**
        - .. figure:: _static/wordcloud-example.png
            :alt: Wordcloud Example Chart
            :width: 100%

          :class:`highcharts_core.options.plot_options.wordcloud.WordcloudOptions`

          :class:`highcharts_core.options.series.wordcloud.WordcloudSeries`
      * - **X-Range**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/xrange-example.png
                :alt: X-Range Example Chart
                :width: 100%

            .. tab:: Inverted

              .. figure:: _static/xrange-example-inverted.png
                :alt: Inverted X-Range Example Chart
                :width: 100%

          :class:`highcharts_core.options.plot_options.bar.XRangeOptions`

          :class:`highcharts_core.options.series.bar.XRangeSeries`

  .. tab:: Stock

    .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Series Type
        - Screenshot + Class Links
      * - **Candlestick**
        - .. figure:: _static/candlestick-example.png
            :alt: Candlestick Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.candlestick.CandlestickOptions`

          :class:`highcharts_stock.options.series.candlestick.CandlestickSeries`
      * - **HLC (High-Low-Close)**
        - .. figure:: _static/hlc-example.png
            :alt: HLC Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.hlc.HLCOptions`

          :class:`highcharts_stock.options.series.hlc.HLCSeries`
      * - **Hollow Candlestick**
        - .. figure:: _static/hollow-candlestick-example.png
            :alt: HollowCandlestick Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.candlestick.HollowCandlestickOptions`

          :class:`highcharts_stock.options.series.candlestick.HollowCandlestickSeries`
      * - **Heikin Ashi**
        - .. figure:: _static/heikin-ashi-example.png
            :alt: HeikinAshi Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.candlestick.HeikinAshiOptions`

          :class:`highcharts_stock.options.series.candlestick.HeikinAshiSeries`
      * - **OHLC (Open-High-Low-Close)**
        - .. figure:: _static/ohlc-example.png
            :alt: OHLC Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.hlc.OHLCOptions`

          :class:`highcharts_stock.options.series.hlc.OHLCSeries`

  .. tab:: Maps

    .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Series Type
        - Screenshot + Class Links
      * - **Flowmap**
        - .. figure:: _static/flowmap-example.png
            :alt: Flowmap Example Chart
            :width: 100%

          :class:`highcharts_maps.options.plot_options.flowmap.FlowmapOptions`

          :class:`highcharts_maps.options.series.flowmap.FlowmapSeries`
      * - **GeoHeatmap**
        - .. figure:: _static/geoheatmap-example.png
            :alt: GeoHeatmap Example Chart
            :width: 100%

          :class:`highcharts_maps.options.plot_options.flowmap.GeoHeatmapOptions`

          :class:`highcharts_maps.options.series.flowmap.GeoHeatmapSeries`
      * - **Map**
        - .. figure:: _static/map-example.png
            :alt: Map Example Chart
            :width: 100%

          :class:`highcharts_maps.options.plot_options.map.MapOptions`

          :class:`highcharts_maps.options.series.map.MapSeries`
      * - **Map Bubble**
        - .. figure:: _static/mapbubble-example.png
            :alt: Map Bubble Example Chart
            :width: 100%

          :class:`highcharts_maps.options.plot_options.mapbubble.MapBubbleOptions`

          :class:`highcharts_maps.options.series.mapbubble.MapBubbleSeries`
      * - **Map Line**
        - .. figure:: _static/mapline-example.png
            :alt: Map Line Example Chart
            :width: 100%

          :class:`highcharts_maps.options.plot_options.mapline.MapLineOptions`

          :class:`highcharts_maps.options.series.mapline.MapLineSeries`
      * - **Map Point**
        - .. figure:: _static/mappoint-example.png
            :alt: Map Point Example Chart
            :width: 100%

          :class:`highcharts_maps.options.plot_options.mappoint.MapPointOptions`

          :class:`highcharts_maps.options.series.mappoint.MapPointSeries`
      * - **Tiled Web Map**
        - .. figure:: _static/tiledwebmap-example.png
            :alt: Tiled Web Map Example Chart
            :width: 100%

          :class:`highcharts_maps.options.plot_options.tiledwebmap.TiledWebMapOptions`

          :class:`highcharts_maps.options.series.tiledwebmap.TiledWebMapSeries`

  .. tab:: Gantt

    .. list-table::
      :widths: 10 90
      :header-rows: 1

      * - Series Type
        - Screenshot + Class Links
      * - **Gantt Chart**
        - .. figure:: _static/gantt-example.png
            :alt: Gantt Chart Example
            :width: 100%

          :class:`highcharts_gantt.options.plot_options.gantt.GanttOptions`

          :class:`highcharts_gantt.options.series.gantt.GanttSeries`
      * - **X-Range**
        - .. tabs::

            .. tab:: Standard

              .. figure:: _static/xrange-example.png
                :alt: X-Range Example Chart
                :width: 100%

            .. tab:: Inverted

              .. figure:: _static/xrange-example-inverted.png
                :alt: Inverted X-Range Example Chart
                :width: 100%

          :class:`highcharts_gantt.options.plot_options.bar.XRangeOptions`

          :class:`highcharts_gantt.options.series.bar.XRangeSeries`

--------------

.. _technical_indicators:

*****************************
Technical Indicators
*****************************

The following visualizations are supported as
:term:`technical indicators <technical indicator>`, which are calculated dynamically from
the data contained in :ref:`series with data <series_with_data>` and overlaid onto your
visualizations.

.. tabs::

  .. tab:: Core

    .. error::

      The **Highcharts Core for Python** library and the related
      `Highcharts Core <https://www.highcharts.com/products/highcharts/>`__ JavaScript
      library do not support :term:`technical indicators <technical indicator>`.

      Only **Highcharts Stock for Python** and
      `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ support
      technical indicators.

  .. tab:: Stock

    .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Series Type
        - Screenshot + Class Links
      * - **Absolute Price Oscillator**

          **(APO)**
        - .. figure:: _static/apo-example.png
            :alt: APO Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.APOOptions`

          :class:`highcharts_stock.options.series.oscillators.APOSeries`
      * - **Acceleration Bands**

          **(ABANDS)**
        - .. figure:: _static/abands-example.png
            :alt: Acceleration Bands Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.abands.AbandsOptions`

          :class:`highcharts_stock.options.series.abands.AbandsSeries`
      * - **Accumulation/Distribution**
        - .. figure:: _static/ad-example.png
            :alt: Accumulation/Distribution Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.ad.ADOptions`

          :class:`highcharts_stock.options.series.ad.ADSeries`
      * - **Aroon**
        - .. figure:: _static/aroon-example.png
            :alt: Aroon Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.aroon.AroonOptions`

          :class:`highcharts_stock.options.series.aroon.AroonSeries`
      * - **Aroon Oscillator**
        - .. figure:: _static/aroon-oscillator-example.png
            :alt: Aroon Oscillator Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.AroonOscillatorOptions`

          :class:`highcharts_stock.options.series.oscillators.AroonOscillatorSeries`
      * - **Average True Range**

          **(ATR)**
        - .. figure:: _static/atr-example.png
            :alt: ATR Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.atr.ATROptions`

          :class:`highcharts_stock.options.series.atr.ATRSeries`
      * - **Awesome Oscillator**

          **(AO)**
        - .. figure:: _static/awesome-oscillator-example.png
            :alt: AO Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.ao.AOOptions`

          :class:`highcharts_stock.options.series.oscillators.ao.AOSeries`
      * - **Bollinger Bands**

          **(BB)**
        - .. figure:: _static/bollinger-bands-example.png
            :alt: Bollinger Bands Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.abands.BBOptions`

          :class:`highcharts_stock.options.series.abands.BBSeries`
      * - **Chaikin Money Flow**

          **(CMF)**
        - .. figure:: _static/cmf-example.png
            :alt: CMF Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.money_flow.CMFOptions`

          :class:`highcharts_stock.options.series.oscillators.money_flow.CMFSeries`
      * - **Chaikin Oscillator**
        - .. figure:: _static/chaikin-example.png
            :alt: Chaikin Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.ChaikinOptions`

          :class:`highcharts_stock.options.series.oscillators.ChaikinSeries`
      * - **Chande Momentum Oscillator**

          **(CMO)**
        - .. figure:: _static/cmo-example.png
            :alt: CMO Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.CMOOptions`

          :class:`highcharts_stock.options.series.oscillators.CMOSeries`
      * - **Commodity Channel Index**

          **(CCI)**
        - .. figure:: _static/cci-example.png
            :alt: CCI Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.CCIOptions`

          :class:`highcharts_stock.options.series.oscillators.CCISeries`
      * - **Detrended Price Oscillator**

          **(DPO)**
        - .. figure:: _static/dpo-example.png
            :alt: DPO Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.DPOOptions`

          :class:`highcharts_stock.options.series.oscillators.DPOSeries`
      * - **Directional Movement Index**

          **(DMI)**
        - .. figure:: _static/dmi-example.png
            :alt: DMI Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.dmi.DMIOptions`

          :class:`highcharts_stock.options.series.dmi.DMISeries`
      * - **Disparity Index**
        - .. figure:: _static/disparity-index-example.png
            :alt: Disparity Index Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.disparity_index.DisparityIndexOptions`

          :class:`highcharts_stock.options.series.disparity_index.DisparityIndexSeries`
      * - **Double Exponential**

          **Moving Average**

          **(DEMA)**
        - .. figure:: _static/dema-example.png
            :alt: DEMA Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.averages.DEMAOptions`

          :class:`highcharts_stock.options.series.averages.DEMASeries`
      * - **Exponential Moving**

          **Average**

          **(EMA)**
        - .. figure:: _static/ema-example.png
            :alt: EMA Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.averages.EMAOptions`

          :class:`highcharts_stock.options.series.averages.EMASeries`
      * - **Flags**
        - .. figure:: _static/flags-example.png
            :alt: Flags Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.flags.FlagsOptions`

          :class:`highcharts_stock.options.series.flags.FlagsSeries`
      * - **Ichimoku Kinko Hyo**

          **(IKH)**
        - .. figure:: _static/ikh-example.png
            :alt: IKH Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.momentum.ikh.IKHOptions`

          :class:`highcharts_stock.options.series.momentum.ikh.IKHSeries`
      * - **Keltner Channels**
        - .. figure:: _static/keltner-channels-example.png
            :alt: Keltner Channels Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.abands.KeltnerChannelsOptions`

          :class:`highcharts_stock.options.series.abands.KeltnerChannelsSeries`
      * - **Klinger Oscillator**
        - .. figure:: _static/klinger-example.png
            :alt: Klinger Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.klinger.KlingerOptions`

          :class:`highcharts_stock.options.series.oscillators.klinger.KlingerSeries`
      * - **Linear Regression**
        - .. figure:: _static/linear-regression-example.png
            :alt: Linear Regression Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.linear_regressions.LinearRegressionOptions`

          :class:`highcharts_stock.options.series.linear_regressions.LinearRegressionSeries`
      * - **Linear Regression**

          **Angle**
        - .. figure:: _static/linear-regression-angle-example.png
            :alt: Linear Regression Angle Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.linear_regressions.LinearRegressionAngleOptions`

          :class:`highcharts_stock.options.series.linear_regressions.LinearRegressionAngleSeries`
      * - **Linear Regression**

          **Intercept**
        - .. figure:: _static/linear-regression-intercept-example.png
            :alt: Linear Regression Intercept Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.linear_regressions.LinearRegressionInterceptOptions`

          :class:`highcharts_stock.options.series.linear_regressions.LinearRegressionInterceptSeries`
      * - **Linear Regression**

          **Slope**
        - .. figure:: _static/linear-regression-slope-example.png
            :alt: Linear Regression Slope Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.linear_regressions.LinearRegressionSlopeOptions`

          :class:`highcharts_stock.options.series.linear_regressions.LinearRegressionSlopeSeries`
      * - **Momentum**
        - .. figure:: _static/momentum-example.png
            :alt: Momentum Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.momentum.MomentumOptions`

          :class:`highcharts_stock.options.series.momentum.MomentumSeries`
      * - **Money Flow Index**

          **(MFI)**
        - .. figure:: _static/mfi-example.png
            :alt: MFI Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.mfi.MFIOptions`

          :class:`highcharts_stock.options.series.oscillators.mfi.MFISeries`
      * - **Moving Average**

          **Convergence/Divergence**

          **(MACD)**
        - .. figure:: _static/macd-example.png
            :alt: MACD Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.momentum.macd.MACDOptions`

          :class:`highcharts_stock.options.series.momentum.macd.MACDSeries`
      * - **Normalized Average True Range**

          **(NATR)**
        - .. figure:: _static/natr-example.png
            :alt: NATR Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.atr.NATROptions`

          :class:`highcharts_stock.options.series.atr.NATRSeries`
      * - **On-Balance Volume**

          **(OBV)**
        - .. figure:: _static/obv-example.png
            :alt: OBV Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.momentum.OBVOptions`

          :class:`highcharts_stock.options.series.momentum.OBVSeries`
      * - **Percentage Price Oscillator**

          **(PPO)**
        - .. figure:: _static/ppo-example.png
            :alt: PPO Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.ppo.PPOOptions`

          :class:`highcharts_stock.options.series.oscillators.ppo.PPOSeries`
      * - **Pivot Points**
        - .. figure:: _static/pivot-points-example.png
            :alt: Pivot Points Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.pivot_points.PivotPointsOptions`

          :class:`highcharts_stock.options.series.pivot_points.PivotPointsSeries`
      * - **Price Channel**
        - .. figure:: _static/price-channel-example.png
            :alt: PC Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.abands.PCOptions`

          :class:`highcharts_stock.options.series.abands.PCSeries`
      * - **Price Envelopes**
        - .. figure:: _static/price-envelopes-example.png
            :alt: Price Envelopes Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.price_envelopes.PriceEnvelopesOptions`

          :class:`highcharts_stock.options.series.price_envelopes.PriceEnvelopesSeries`
      * - **Parabolic SAR**

          **(PSAR)**
        - .. figure:: _static/psar-example.png
            :alt: PSAR Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.psar.PSAROptions`

          :class:`highcharts_stock.options.series.psar.PSARSeries`
      * - **Rate of Change**

          **(ROC)**
        - .. figure:: _static/roc-example.png
            :alt: ROC Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.momentum.ROCOptions`

          :class:`highcharts_stock.options.series.momentum.ROCSeries`
      * - **Relative Strength Index**

          **(RSI)**
        - .. figure:: _static/rsi-example.png
            :alt: RSI Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.momentum.RSIOptions`

          :class:`highcharts_stock.options.series.momentum.RSISeries`
      * - **Simple Moving**

          **Average**

          **(SMA)**
        - .. figure:: _static/sma-example.png
            :alt: SMA Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.averages.SMAOptions`

          :class:`highcharts_stock.options.series.averages.SMASeries`
      * - **Slow Stochastic**

          **Oscillator**
        - .. figure:: _static/slow-stochastic-example.png
            :alt: Slow Stochastic Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.stochastic.SlowStochasticOptions`

          :class:`highcharts_stock.options.series.oscillators.stochastic.SlowStochasticSeries`
      * - **Stochastic Oscillator**
        - .. figure:: _static/stochastic-example.png
            :alt: Stochastic Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.stochastic.StochasticOptions`

          :class:`highcharts_stock.options.series.oscillators.stochastic.StochasticSeries`
      * - **Supertrend**
        - .. figure:: _static/supertrend-example.png
            :alt: Supertrend Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.momentum.supertrend.SupertrendOptions`

          :class:`highcharts_stock.options.series.momentum.supertrend.SupertrendSeries`
      * - **Triple Exponential**

          **Moving Average**

          **(TEMA)**
        - .. figure:: _static/tema-example.png
            :alt: TEMA Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.averages.TEMAOptions`

          :class:`highcharts_stock.options.series.averages.TEMASeries`
      * - **Trendline**
        - .. figure:: _static/trendline-example.png
            :alt: Trendline Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.linear_regressions.TrendlineOptions`

          :class:`highcharts_stock.options.series.linear_regressions.TrendlineSeries`
      * - **Triple Exponential**

          **Average Oscillator**

          **(TRIX)**
        - .. figure:: _static/trix-example.png
            :alt: TRIX Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.TRIXOptions`

          :class:`highcharts_stock.options.series.oscillators.TRIXSeries`
      * - **Volume-by-Price**

          **(VBP)**
        - .. figure:: _static/vbp-example.png
            :alt: VBP Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.vbp.VBPOptions`

          :class:`highcharts_stock.options.series.vbp.VBPSeries`
      * - **Volume Weighted**

          **Average Price**

          **(VWAP)**
        - .. figure:: _static/vwap-example.png
            :alt: VWAP Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.averages.VWAPOptions`

          :class:`highcharts_stock.options.series.averages.VWAPSeries`
      * - **Weighted Moving**

          **Average**

          **(WMA)**
        - .. figure:: _static/wma-example.png
            :alt: WMA Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.averages.WMAOptions`

          :class:`highcharts_stock.options.series.averages.WMASeries`
      * - **Williams %R**
        - .. figure:: _static/williamsr-example.png
            :alt: Williams %R Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.oscillators.WilliamsROptions`

          :class:`highcharts_stock.options.series.oscillators.WilliamsRSeries`
      * - **ZigZag**
        - .. figure:: _static/zigzag-example.png
            :alt: ZigZag Example Chart
            :width: 100%

          :class:`highcharts_stock.options.plot_options.zigzag.ZigZagOptions`

          :class:`highcharts_stock.options.series.zigzag.ZigZagSeries`


  .. tab:: Maps

    .. error::

      The **Highcharts Maps for Python** extension and the related
      `Highcharts Maps <https://www.highcharts.com/products/maps/>`__ JavaScript
      library do not support :term:`technical indicators <technical indicator>`.

      Only **Highcharts Stock for Python** and
      `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ support
      technical indicators. For more information, please see
      `here <https://stock-docs.highchartspython.com/>`__.

  .. tab:: Gantt

    .. seealso::

      As an extension of the **Highcharts Stock for Python** library, for reasons of
      convenience the **Highcharts Gantt for Python** extension provides full support
      for all :term:`technical indicators <technical indicator>` supported by the
      **Highcharts Stock for Python** library.

      For more information, please see `here <https://stock-docs.highchartspython.com/>`__.
