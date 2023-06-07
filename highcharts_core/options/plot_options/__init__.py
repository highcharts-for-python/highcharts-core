from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.plot_options.arcdiagram import ArcDiagramOptions
from highcharts_core.options.plot_options.area import AreaOptions
from highcharts_core.options.plot_options.area import AreaRangeOptions
from highcharts_core.options.plot_options.area import AreaSplineOptions
from highcharts_core.options.plot_options.area import AreaSplineRangeOptions
from highcharts_core.options.plot_options.bar import BarOptions
from highcharts_core.options.plot_options.bellcurve import BellCurveOptions
from highcharts_core.options.plot_options.boxplot import BoxPlotOptions
from highcharts_core.options.plot_options.bubble import BubbleOptions
from highcharts_core.options.plot_options.bullet import BulletOptions
from highcharts_core.options.plot_options.bar import ColumnOptions
from highcharts_core.options.plot_options.bar import ColumnPyramidOptions
from highcharts_core.options.plot_options.bar import ColumnRangeOptions
from highcharts_core.options.plot_options.bar import CylinderOptions
from highcharts_core.options.plot_options.dependencywheel import DependencyWheelOptions
from highcharts_core.options.plot_options.dumbbell import DumbbellOptions
from highcharts_core.options.plot_options.boxplot import ErrorBarOptions
from highcharts_core.options.plot_options.funnel import FunnelOptions
from highcharts_core.options.plot_options.funnel import Funnel3DOptions
from highcharts_core.options.plot_options.gauge import GaugeOptions
from highcharts_core.options.plot_options.heatmap import HeatmapOptions
from highcharts_core.options.plot_options.histogram import HistogramOptions
from highcharts_core.options.plot_options.item import ItemOptions
from highcharts_core.options.plot_options.area import LineOptions
from highcharts_core.options.plot_options.dumbbell import LollipopOptions
from highcharts_core.options.plot_options.networkgraph import NetworkGraphOptions
from highcharts_core.options.plot_options.organization import OrganizationOptions
from highcharts_core.options.plot_options.packedbubble import PackedBubbleOptions
from highcharts_core.options.plot_options.pareto import ParetoOptions
from highcharts_core.options.plot_options.pictorial import PictorialOptions
from highcharts_core.options.plot_options.pie import PieOptions
from highcharts_core.options.plot_options.polygon import PolygonOptions
from highcharts_core.options.plot_options.pyramid import PyramidOptions
from highcharts_core.options.plot_options.pyramid import Pyramid3DOptions
from highcharts_core.options.plot_options.sankey import SankeyOptions
from highcharts_core.options.plot_options.scatter import ScatterOptions
from highcharts_core.options.plot_options.scatter import Scatter3DOptions
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.options.plot_options.gauge import SolidGaugeOptions
from highcharts_core.options.plot_options.spline import SplineOptions
from highcharts_core.options.plot_options.area import StreamGraphOptions
from highcharts_core.options.plot_options.sunburst import SunburstOptions
from highcharts_core.options.plot_options.heatmap import TilemapOptions
from highcharts_core.options.plot_options.timeline import TimelineOptions
from highcharts_core.options.plot_options.treegraph import TreegraphOptions
from highcharts_core.options.plot_options.treemap import TreemapOptions
from highcharts_core.options.plot_options.pie import VariablePieOptions
from highcharts_core.options.plot_options.bar import VariwideOptions
from highcharts_core.options.plot_options.vector import VectorOptions
from highcharts_core.options.plot_options.venn import VennOptions
from highcharts_core.options.plot_options.bar import WaterfallOptions
from highcharts_core.options.plot_options.bar import WindBarbOptions
from highcharts_core.options.plot_options.wordcloud import WordcloudOptions
from highcharts_core.options.plot_options.bar import XRangeOptions


class PlotOptions(HighchartsMeta):
    """A wrapper object for configurations applied to each series type.

    The config objects for each series can also be overridden for each series item as
    given in the series array.

    Configuration options for the series are given in three levels:

      * Options for all series in a chart are given in the
        :meth:`series <PlotOptions.series>` property.
      * Options for all series of a specific type are given in the corresponding
        property for that type, for example
        :meth:`plot_options.line <PlotOptions.line>`.
      * Finally, options for one single series are given in the
        :meth:`Options.series <Options.series>` array.

    """

    def __init__(self, **kwargs):
        self._arcdiagram = None
        self._area = None
        self._arearange = None
        self._areaspline = None
        self._areasplinerange = None
        self._bar = None
        self._bellcurve = None
        self._boxplot = None
        self._bubble = None
        self._bullet = None
        self._column = None
        self._columnpyramid = None
        self._columnrange = None
        self._cylinder = None
        self._dependencywheel = None
        self._dumbbell = None
        self._errorbar = None
        self._funnel = None
        self._funnel_3d = None
        self._gauge = None
        self._heatmap = None
        self._histogram = None
        self._item = None
        self._line = None
        self._lollipop = None
        self._networkgraph = None
        self._organization = None
        self._packedbubble = None
        self._pareto = None
        self._pictorial = None
        self._pie = None
        self._polygon = None
        self._pyramid = None
        self._pyramid_3d = None
        self._sankey = None
        self._scatter = None
        self._scatter_3d = None
        self._series = None
        self._solidgauge = None
        self._spline = None
        self._streamgraph = None
        self._sunburst = None
        self._tilemap = None
        self._timeline = None
        self._treegraph = None
        self._treemap = None
        self._variablepie = None
        self._variwide = None
        self._vector = None
        self._venn = None
        self._waterfall = None
        self._windbarb = None
        self._wordcloud = None
        self._xrange = None

        for attribute in dir(self):
            if attribute.startswith('_') and not attribute.startswith('__'):
                non_private_name = attribute[1:]
                setattr(self, non_private_name, kwargs.get(non_private_name, None))

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions'

    @property
    def arcdiagram(self) -> Optional[ArcDiagramOptions]:
        """Arc diagram series is a chart drawing style in which the vertices of the chart
        are positioned along a line on the Euclidean plane and the edges are drawn as a
        semicircle in one of the two half-planes delimited by the line, or as smooth
        curves formed by sequences of semicircles.

        .. figure:: ../../../_static/arcdiagram-example.png
          :alt: Arc Diagram Example Chart
          :align: center

        :rtype: :class:`ArcDiagramOptions` or :obj:`None <python:None>`
        """
        return self._arcdiagram

    @arcdiagram.setter
    @class_sensitive(ArcDiagramOptions)
    def arcdiagram(self, value):
        self._arcdiagram = value

    @property
    def area(self) -> Optional[AreaOptions]:
        """General options to apply to all Area series types.

        .. figure:: ../../../_static/area-example.png
          :alt: Area Example Chart
          :align: center

        :rtype: :class:`AreaOptions` or :obj:`None <python:None>`
        """
        return self._area

    @area.setter
    @class_sensitive(AreaOptions)
    def area(self, value):
        self._area = value

    @property
    def arearange(self) -> Optional[AreaRangeOptions]:
        """General options to apply to all AreaRange series types. The area range series
        is a carteseian series with higher and lower values for each point along an X
        axis, where the area between the values is shaded.

        .. figure:: ../../../_static/arearange-example.png
          :alt: AreaRange Example Chart
          :align: center

        :rtype: :class:`AreaRangeOptions` or :obj:`None <python:None>`
        """
        return self._arearange

    @arearange.setter
    @class_sensitive(AreaRangeOptions)
    def arearange(self, value):
        self._arearange = value

    @property
    def areaspline(self) -> Optional[AreaSplineOptions]:
        """General options to apply to all AreaSpline series types. The area spline series
        is an area series where the graph between the points is smoothed into a spline.

        .. figure:: ../../../_static/areaspline-example.png
          :alt: AreaSpline Example Chart
          :align: center

        :rtype: :class:`AreaSplineOptions` or :obj:`None <python:None>`
        """
        return self._areaspline

    @areaspline.setter
    @class_sensitive(AreaSplineOptions)
    def areaspline(self, value):
        self._areaspline = value

    @property
    def areasplinerange(self) -> Optional[AreaSplineRangeOptions]:
        """General options to apply to all AreaSplineRange series types. The area spline
        range series is a carteseian series type with higher and lower Y values along an X
        axis. The area inside the range is colored, and the graph outlining the area is a
        smoothed spline.

        :rtype: :class:`AreaSplineRangeOptions` or :obj:`None <python:None>`
        """
        return self._areasplinerange

    @areasplinerange.setter
    @class_sensitive(AreaSplineRangeOptions)
    def areasplinerange(self, value):
        self._areasplinerange = value

    @property
    def bar(self) -> Optional[BarOptions]:
        """General options to apply to all Bar series types. A bar series is a special
        type of column series where the columns are horizontal.

        .. figure:: ../../../_static/bar-example.png
          :alt: Bar Example Chart
          :align: center

        :rtype: :class:`BarOptions` or :obj:`None <python:None>`
        """
        return self._bar

    @bar.setter
    @class_sensitive(BarOptions)
    def bar(self, value):
        self._bar = value

    @property
    def bellcurve(self) -> Optional[BellCurveOptions]:
        """General options to apply to all Bell Curve series types.

        A bell curve is an areaspline series which represents the probability density
        function of the normal distribution. It calculates mean and standard deviation of
        the base series data and plots the curve according to the calculated parameters.

        .. figure:: ../../../_static/bellcurve-example.png
          :alt: Bell Curve Example Chart
          :align: center

        :rtype: :class:`BellCurveOptions` or :obj:`None <python:None>`
        """
        return self._bellcurve

    @bellcurve.setter
    @class_sensitive(BellCurveOptions)
    def bellcurve(self, value):
        self._bellcurve = value

    @property
    def boxplot(self) -> Optional[BoxPlotOptions]:
        """General options to apply to all Box Plot series types.

        A box plot is a convenient way of depicting groups of data through their
        five-number summaries:

          * the smallest observation (sample minimum),
          * lower quartile (Q1),
          * median (Q2),
          * upper quartile (Q3), and
          * largest observation (sample maximum).

        .. figure:: ../../../_static/boxplot-example.png
          :alt: Box Plot Example Chart
          :align: center

        :rtype: :class:`BoxPlotOptions` or :obj:`None <python:None>`
        """
        return self._boxplot

    @boxplot.setter
    @class_sensitive(BoxPlotOptions)
    def boxplot(self, value):
        self._boxplot = value

    @property
    def bubble(self) -> Optional[BubbleOptions]:
        """General options to apply to all Bubble series types.

        A bubble series is a three dimensional series type where each point renders an X,
        Y, and Z value. Each points is drawn as a bubble where the position along the X
        and Y axes mark the X and Y values, and the size of the bubble relates to the Z
        value.

        .. figure:: ../../../_static/bubble-example.png
          :alt: Bubble Example Chart
          :align: center

        :rtype: :class:`BubbleOptions` or :obj:`None <python:None>`
        """
        return self._bubble

    @bubble.setter
    @class_sensitive(BubbleOptions)
    def bubble(self, value):
        self._bubble = value

    @property
    def bullet(self) -> Optional[BulletOptions]:
        """General options to apply to all Bullet series types.

        A bullet graph is a variation of a bar graph. The bullet graph features a single
        measure, compares it to a target, and displays it in the context of qualitative
        ranges of performance that could be set using :meth:`YAxis.plot_bands`.

        .. figure:: ../../../_static/bullet-example.png
          :alt: Bullet Example Chart
          :align: center

        :rtype: :class:`BulletOptions` or :obj:`None <python:None>`
        """
        return self._bullet

    @bullet.setter
    @class_sensitive(BulletOptions)
    def bullet(self, value):
        self._bullet = value

    @property
    def column(self) -> Optional[ColumnOptions]:
        """General options to apply to all Column series types.

        Column series display one column per value along an X axis.

        .. figure:: ../../../_static/column-example.png
          :alt: Column Example Chart
          :align: center

        :rtype: :class:`ColumnOptions` or :obj:`None <python:None>`
        """
        return self._column

    @column.setter
    @class_sensitive(ColumnOptions)
    def column(self, value):
        self._column = value

    @property
    def columnpyramid(self) -> Optional[ColumnPyramidOptions]:
        """General options to apply to all Column Pyramid series types.

        Column Pyramid series display one pyramid per value along an X axis.

        .. hint::

          To display horizontal pyramids, set :meth:`Chart.inverted` to ``True``.

        .. tabs::

          .. tab:: Standard

            .. figure:: ../../../_static/columnpyramid-example.png
              :alt: ColumnPyramid Example Chart
              :align: center

          .. tab:: Stacked

            .. figure:: ../../../_static/columnpyramid-example-stacked.png
              :alt: Stacked Column Pyramid Example Chart
              :align: center

          .. tab:: Stacked + Inverted

            .. figure:: ../../../_static/columnpyramid-example-stacked-horizontal.png
              :alt: Stacked and Inverted Column Pyramid Example Chart
              :align: center

        :rtype: :class:`ColumnPyramidOptions` or :obj:`None <python:None>`
        """
        return self._columnpyramid

    @columnpyramid.setter
    @class_sensitive(ColumnPyramidOptions)
    def columnpyramid(self, value):
        self._columnpyramid = value

    @property
    def columnrange(self) -> Optional[ColumnRangeOptions]:
        """General options to apply to all Column Range series types.

        The column range is a cartesian series type with higher and lower Y values along
        an X axis.

        .. hint::

          To display horizontal bars, set :meth:`Chart.inverted` to ``True``.

        .. tabs::

          .. tab:: Standard

            .. figure:: ../../../_static/columnrange-example.png
              :alt: ColumnRange Example Chart
              :align: center

          .. tab:: Horizontal

            .. figure:: ../../../_static/columnrange-example-horizontal.png
              :alt: Inverted Column Range Example Chart
              :align: center

        :rtype: :class:`ColumnRangeOptions` or :obj:`None <python:None>`
        """
        return self._columnrange

    @columnrange.setter
    @class_sensitive(ColumnRangeOptions)
    def columnrange(self, value):
        self._columnrange = value

    @property
    def cylinder(self) -> Optional[CylinderOptions]:
        """General options to apply to all Cylinder series types.

        A cylinder graph is a variation of a 3d column graph. The cylinder graph features
        cylindrical points.

        .. figure:: ../../../_static/cylinder-example.png
          :alt: Cylinder Example Chart
          :align: center

        :rtype: :class:`CylinderOptions` or :obj:`None <python:None>`
        """
        return self._cylinder

    @cylinder.setter
    @class_sensitive(CylinderOptions)
    def cylinder(self, value):
        self._cylinder = value

    @property
    def dependencywheel(self) -> Optional[DependencyWheelOptions]:
        """General options to apply to all Dependency Wheel series types.

        A dependency wheel chart is a type of flow diagram, where all nodes are laid out
        in a circle, and the flow between the are drawn as link bands.

        .. figure:: ../../../_static/dependencywheel-example.png
          :alt: Dependency Wheel Example Chart
          :align: center

        :rtype: :class:`DependencyWheelOptions` or :obj:`None <python:None>`
        """
        return self._dependencywheel

    @dependencywheel.setter
    @class_sensitive(DependencyWheelOptions)
    def dependencywheel(self, value):
        self._dependencywheel = value

    @property
    def dumbbell(self) -> Optional[DumbbellOptions]:
        """General options to apply to all Dumbbell series types.

        The dumbbell series is a cartesian series with higher and lower values for each
        point along an X axis, connected with a line between the values.

        .. figure:: ../../../_static/dumbbell-example.png
          :alt: Dumbbell Example Chart
          :align: center

        .. warning::

          Requires ``highcharts-more.js`` and ``modules/dumbbell.js`` be loaded
          client-side.

        :rtype: :class:`DumbbellOptions` or :obj:`None <python:None>`
        """
        return self._dumbbell

    @dumbbell.setter
    @class_sensitive(DumbbellOptions)
    def dumbbell(self, value):
        self._dumbbell = value

    @property
    def errorbar(self) -> Optional[ErrorBarOptions]:
        """General options to apply to all Error Bar series types.

        Error bars are a graphical representation of the variability of data and are used
        on graphs to indicate the error, or uncertainty in a reported measurement.

        .. figure:: ../../../_static/errorbar-example.png
          :alt: Error Bar Example Chart
          :align: center

        :rtype: :class:`ErrorBarOptions` or :obj:`None <python:None>`
        """
        return self._errorbar

    @errorbar.setter
    @class_sensitive(ErrorBarOptions)
    def errorbar(self, value):
        self._errorbar = value

    @property
    def funnel(self) -> Optional[FunnelOptions]:
        """General options to apply to all Funnel series types.

        Funnel charts are a type of chart often used to visualize stages in a sales
        project, where the top are the initial stages with the most clients.

        .. warning::

          Funnel charts require that the ``modules/funnel.js`` file is loaded client-side.

        .. figure:: ../../../_static/funnel-example.png
          :alt: Funnel Example Chart
          :align: center

        :rtype: :class:`FunnelOptions` or :obj:`None <python:None>`
        """
        return self._funnel

    @funnel.setter
    @class_sensitive(FunnelOptions)
    def funnel(self, value):
        self._funnel = value

    @property
    def funnel_3d(self) -> Optional[Funnel3DOptions]:
        """General options to apply to all Funnel 3D series types.

        A Funnel 3D chart is a three-dimensional version of funnel series type. Funnel
        charts are a type of chart often used to visualize stages in a sales project,
        where the top are the initial stages with the most clients.

        .. warning::

          Funnel 3D charts require that the following files are all loaded client-side:

            * ``highcharts-3d.js``,
            * ``cylinder.js`` and
            * ``funnel3d.js``

        .. figure:: ../../../_static/funnel_3d-example.png
          :alt: Funnel 3D Example Chart
          :align: center

        :rtype: :class:`FunnelOptions` or :obj:`None <python:None>`
        """
        return self._funnel_3d

    @funnel_3d.setter
    @class_sensitive(Funnel3DOptions)
    def funnel_3d(self, value):
        self._funnel_3d = value

    @property
    def gauge(self) -> Optional[GaugeOptions]:
        """General options to apply to all Gauge series types.

        Gauges are circular plots displaying one or more values with a dial pointing to
        values along the perimeter.

        .. figure:: ../../../_static/gauge-example.png
          :alt: Gauge Example Chart
          :align: center

        :rtype: :class:`GaugeOptions` or :obj:`None <python:None>`
        """
        return self._gauge

    @gauge.setter
    @class_sensitive(GaugeOptions)
    def gauge(self, value):
        self._gauge = value

    @property
    def heatmap(self) -> Optional[HeatmapOptions]:
        """General options to apply to all Heatmap series types.

        A heatmap is a graphical representation of data where the individual values
        contained in a matrix are represented as colors.

        .. warning::

          Heatmaps require that ``modules/heatmap`` is loaded client-side.

        .. figure:: ../../../_static/heatmap-example.png
          :alt: Heatmap Example Chart
          :align: center

        :rtype: :class:`HeatmapOptions` or :obj:`None <python:None>`
        """
        return self._heatmap

    @heatmap.setter
    @class_sensitive(HeatmapOptions)
    def heatmap(self, value):
        self._heatmap = value

    @property
    def histogram(self) -> Optional[HistogramOptions]:
        """General options to apply to all Histogram series types.

        A histogram is a column series which represents the distribution of the data set
        in the base series. Histogram splits data into bins and shows their frequencies.

        .. figure:: ../../../_static/histogram-example.png
          :alt: Histogram Example Chart
          :align: center

        :rtype: :class:`HistogramOptions` or :obj:`None <python:None>`
        """
        return self._histogram

    @histogram.setter
    @class_sensitive(HistogramOptions)
    def histogram(self, value):
        self._histogram = value

    @property
    def item(self) -> Optional[ItemOptions]:
        """General options to apply to all Item series types.

        An item chart is an infographic chart where a number of items are laid out in
        either a rectangular or circular pattern. It can be used to visualize counts
        within a group, or for the circular pattern, typically a parliament.

        The circular layout has much in common with a pie chart. Many of the item series
        options, like ``center``, ``size`` and data label positioning, are inherited from
        the :meth:`PlotOptions.pie` series and don't apply for rectangular layouts.

        .. tabs::

          .. tab:: Circular Item Chart

            .. figure:: ../../../_static/item-example-circular.png
              :alt: Circular Item Example Chart
              :align: center

          .. tab:: Rectangular Item Chart

            .. figure:: ../../../_static/item-example-rectangular.png
              :alt: Rectangular Item Example Chart
              :align: center

          .. tab:: Item Chart with Symbols

            .. figure:: ../../../_static/item-example-symbols.png
              :alt: Item Example Chart with Symbols
              :align: center

        :rtype: :class:`ItemOptions` or :obj:`None <python:None>`
        """
        return self._item

    @item.setter
    @class_sensitive(ItemOptions)
    def item(self, value):
        self._item = value

    @property
    def line(self) -> Optional[LineOptions]:
        """General options to apply to all Line series types.

        A line series displays information as a series of data points connected by
        straight line segments.

        .. figure:: ../../../_static/line-example.png
          :alt: Line Example Chart
          :align: center

        :rtype: :class:`LineOptions` or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    @class_sensitive(LineOptions)
    def line(self, value):
        self._line = value

    @property
    def lollipop(self) -> Optional[LollipopOptions]:
        """General options to apply to all Lollipop series types.

        The lollipop series is a carteseian series with a line anchored from the x axis
        and a dot at the end to mark the value.

        .. warning::

          Requires ``highcharts-more.js``, ``modules/dumbbell.js``, and
          ``modules/lollipop.js`` to be loaded client-side.

        .. figure:: ../../../_static/lollipop-example.png
          :alt: Lollipop Example Chart
          :align: center

        :rtype: :class:`LollipopOptions` or :obj:`None <python:None>`
        """
        return self._lollipop

    @lollipop.setter
    @class_sensitive(LollipopOptions)
    def lollipop(self, value):
        self._lollipop = value

    @property
    def networkgraph(self) -> Optional[NetworkGraphOptions]:
        """General options to apply to all Network Graph series types.

        A network graph is a type of relationship chart, where connnections (links)
        attract nodes (points) and other nodes repulse each other.

        .. figure:: ../../../_static/networkgraph-example.png
          :alt: NetworkGraph Example Chart
          :align: center

        :rtype: :class:`NetworkGraphOptions` or :obj:`None <python:None>`
        """
        return self._networkgraph

    @networkgraph.setter
    @class_sensitive(NetworkGraphOptions)
    def networkgraph(self, value):
        self._networkgraph = value

    @property
    def organization(self) -> Optional[OrganizationOptions]:
        """General options to apply to all Organization series types.

        An organization chart is a diagram that shows the structure of an organization and
        the relationships and relative ranks of its parts and positions.

        .. tabs::

          .. tab:: Standard Organization Chart

            .. figure:: ../../../_static/organization-example.png
              :alt: Organization Example Chart
              :align: center

          .. tab:: Horizontal Organization Chart

            .. figure:: ../../../_static/organization-example-horizontal.png
              :alt: Horizontal Organization Example Chart
              :align: center

        :rtype: :class:`OrganizationOptions` or :obj:`None <python:None>`
        """
        return self._organization

    @organization.setter
    @class_sensitive(OrganizationOptions)
    def organization(self, value):
        self._organization = value

    @property
    def packedbubble(self) -> Optional[PackedBubbleOptions]:
        """General options to apply to all Packed Bubble series types.

        A packed bubble series is a two dimensional series type, where each point renders
        a value in X, Y position. Each point is drawn as a bubble where the bubbles don't
        overlap with each other and the radius of the bubble relates to the value.

        .. tabs::

          .. tab:: Standard Packed Bubble

            .. figure:: ../../../_static/packedbubble-example.png
              :alt: Split Packed Bubble Example Chart
              :align: center

          .. tab:: Split Packed Bubble

            .. figure:: ../../../_static/packedbubble-example-split.png
              :alt: Split Packed Bubble Example Chart
              :align: center

        :rtype: :class:`PackedBubbleOptions` or :obj:`None <python:None>`
        """
        return self._packedbubble

    @packedbubble.setter
    @class_sensitive(PackedBubbleOptions)
    def packedbubble(self, value):
        self._packedbubble = value

    @property
    def pareto(self) -> Optional[ParetoOptions]:
        """General options to apply to all Pareto series types.

        A pareto diagram is a type of chart that contains both bars and a line graph,
        where individual values are represented in descending order by bars, and the
        cumulative total is represented by the line.

        .. figure:: ../../../_static/pareto-example.png
          :alt: Pareto Example Chart
          :align: center

        :rtype: :class:`ParetoOptions` or :obj:`None <python:None>`
        """
        return self._pareto

    @pareto.setter
    @class_sensitive(ParetoOptions)
    def pareto(self, value):
        self._pareto = value

    @property
    def pictorial(self) -> Optional[PictorialOptions]:
        """General options to apply to all Pictorial series types.

        A pictorial series uses vector images to represent the data, with the data's shape
        determined by the ``path`` parameter.

        .. figure:: ../../../_static/pictorial-example.png
          :alt: Pictorial Example Chart
          :align: center


        :rtype: :class:`PictorialOptions <highcharts_core.options.plot_options.pictorial.PictorialOptions>` or
          :obj:`None <python:None>`
        """
        return self._pictorial

    @pictorial.setter
    @class_sensitive(PictorialOptions)
    def pictorial(self, value):
        self._pictorial = value

    @property
    def pie(self) -> Optional[PieOptions]:
        """General options to apply to all Pie series types.

        A pie chart is a circular graphic which is divided into slices to illustrate
        numerical proportion.

        .. tabs::

          .. tab:: Pie Chart

            .. figure:: ../../../_static/pie-example.png
              :alt: Pie Example Chart
              :align: center

          .. tab:: Donut Chart

            .. figure:: ../../../_static/pie-example-donut.png
              :alt: Donut Example Chart
              :align: center

        :rtype: :class:`PieOptions` or :obj:`None <python:None>`
        """
        return self._pie

    @pie.setter
    @class_sensitive(PieOptions)
    def pie(self, value):
        self._pie = value

    @property
    def polygon(self) -> Optional[PolygonOptions]:
        """General options to apply to all Polygon series types.

        A polygon series can be used to draw any freeform shape in the cartesian
        coordinate system. A fill is applied with the :meth:`PolygonOptions.color`
        setting, and stroke is applied through :meth:`PolygonOptions.line_width` and
        :meth:`PolygonOptions.line_color`.

        .. figure:: ../../../_static/polygon-example.png
          :alt: Polygon Example Chart
          :align: center

        :rtype: :class:`PolygonOptions` or :obj:`None <python:None>`
        """
        return self._polygon

    @polygon.setter
    @class_sensitive(PolygonOptions)
    def polygon(self, value):
        self._polygon = value

    @property
    def pyramid(self) -> Optional[PyramidOptions]:
        """General options to apply to all Pyramid series types.

        A pyramid series is a special type of funnel, without neck and reversed by
        default.

        .. figure:: ../../../_static/pyramid-example.png
          :alt: Pyramid Example Chart
          :align: center

        :rtype: :class:`PyramidOptions` or :obj:`None <python:None>`
        """
        return self._pyramid

    @pyramid.setter
    @class_sensitive(PyramidOptions)
    def pyramid(self, value):
        self._pyramid = value

    @property
    def pyramid_3d(self) -> Optional[Pyramid3DOptions]:
        """General options to apply to all Pyramid 3D series types.

        A pyramid 3d series is a special type of funnel, without neck and reversed by
        default.

        .. figure:: ../../../_static/pyramid_3d-example.png
          :alt: Pyramid 3D Example Chart
          :align: center

        :rtype: :class:`Pyramid3DOptions` or :obj:`None <python:None>`
        """
        return self._pyramid_3d

    @pyramid_3d.setter
    @class_sensitive(Pyramid3DOptions)
    def pyramid_3d(self, value):
        self._pyramid_3d = value

    @property
    def sankey(self) -> Optional[SankeyOptions]:
        """General options to apply to all Sankey series types.

        A sankey diagram is a type of flow diagram, in which the width of the link between
        two nodes is shown proportionally to the flow quantity.

        .. tabs::

          .. tab:: Standard Sankey

            .. figure:: ../../../_static/sankey-example.png
              :alt: Sankey Example Chart
              :align: center

          .. tab:: Inverted Sankey

            .. figure:: ../../../_static/sankey-example-inverted.png
              :alt: Inverted Sankey Example Chart
              :align: center

          .. tab:: Sankey with Outgoing Links

            .. figure:: ../../../_static/sankey-example-outgoing.png
              :alt: Sankey Example Chart with Outgoing Links
              :align: center

        :rtype: :class:`SankeyOptions` or :obj:`None <python:None>`
        """
        return self._sankey

    @sankey.setter
    @class_sensitive(SankeyOptions)
    def sankey(self, value):
        self._sankey = value

    @property
    def scatter(self) -> Optional[ScatterOptions]:
        """General options to apply to all Scatter series types.

        A scatter plot uses cartesian coordinates to display values for two variables for
        a set of data.

        .. figure:: ../../../_static/scatter-example.png
          :alt: Scatter Example Chart
          :align: center

        :rtype: :class:`ScatterOptions` or :obj:`None <python:None>`
        """
        return self._scatter

    @scatter.setter
    @class_sensitive(ScatterOptions)
    def scatter(self, value):
        self._scatter = value

    @property
    def scatter_3d(self) -> Optional[Scatter3DOptions]:
        """General options to apply to all Scatter 3D series types.

        A 3D scatter plot uses x, y and z coordinates to display values for three
        variables for a set of data.

        .. figure:: ../../../_static/scatter_3d-example.png
          :alt: Scatter 3D Example Chart
          :align: center

        :rtype: :class:`Scatter3DOptions` or :obj:`None <python:None>`
        """
        return self._scatter_3d

    @scatter_3d.setter
    @class_sensitive(Scatter3DOptions)
    def scatter_3d(self, value):
        self._scatter_3d = value

    @property
    def series(self) -> Optional[SeriesOptions]:
        """General options to apply to all series types.

        :rtype: :class:`ScatterOptions` or :obj:`None <python:None>`
        """
        return self._series

    @series.setter
    @class_sensitive(SeriesOptions)
    def series(self, value):
        self._series = value

    @property
    def solidgauge(self) -> Optional[SolidGaugeOptions]:
        """General options to apply to all Solid Gauge series types.

        A solid gauge is a circular gauge where the value is indicated by a filled arc,
        and the color of the arc may variate with the value.

        .. figure:: ../../../_static/solidgauge-example.png
          :alt: SolidGauge Example Chart
          :align: center

        :rtype: :class:`SolidGaugeOptions` or :obj:`None <python:None>`
        """
        return self._solidgauge

    @solidgauge.setter
    @class_sensitive(SolidGaugeOptions)
    def solidgauge(self, value):
        self._solidgauge = value

    @property
    def spline(self) -> Optional[SplineOptions]:
        """General options to apply to all Spline series types.

        A spline series is a special type of line series, where the segments between the
        data points are smoothed.

        .. figure:: ../../../_static/spline-example.png
          :alt: Spline Example Chart
          :align: center

        :rtype: :class:`SplineOptions` or :obj:`None <python:None>`
        """
        return self._spline

    @spline.setter
    @class_sensitive(SplineOptions)
    def spline(self, value):
        self._spline = value

    @property
    def streamgraph(self) -> Optional[StreamGraphOptions]:
        """General options to apply to all Stream Graph series types.

        A streamgraph is a type of stacked area graph which is displaced around a central
        axis, resulting in a flowing, organic shape.

        .. figure:: ../../../_static/streamgraph-example.png
          :alt: StreamGraph Example Chart
          :align: center

        :rtype: :class:`StreamGraphOptions` or :obj:`None <python:None>`
        """
        return self._streamgraph

    @streamgraph.setter
    @class_sensitive(StreamGraphOptions)
    def streamgraph(self, value):
        self._streamgraph = value

    @property
    def sunburst(self) -> Optional[SunburstOptions]:
        """General options to apply to all Sunburst series types.

        A Sunburst displays hierarchical data, where a level in the hierarchy is
        represented by a circle. The center represents the root node of the tree. The
        visualization bears a resemblance to both treemap and pie charts.

        .. figure:: ../../../_static/sunburst-example.png
          :alt: Sunburst Example Chart
          :align: center

        :rtype: :class:`SunburstOptions` or :obj:`None <python:None>`
        """
        return self._sunburst

    @sunburst.setter
    @class_sensitive(SunburstOptions)
    def sunburst(self, value):
        self._sunburst = value

    @property
    def tilemap(self) -> Optional[TilemapOptions]:
        """General options to apply to all Tilemap series types.

        A tilemap series is a type of heatmap where the tile shapes are configurable.

        .. tabs::

          .. tab:: Honeycomb Tilemap

            .. figure:: ../../../_static/tilemap-example.png
              :alt: Honeycomb Tilemap Example Chart
              :align: center

          .. tab:: Circle Tilemap

            .. figure:: ../../../_static/tilemap-example-circle.png
              :alt: Tilemap Example Chart
              :align: center

          .. tab:: Diamond Tilemap

            .. figure:: ../../../_static/tilemap-example-diamond.png
              :alt: Tilemap Example Chart
              :align: center

        :rtype: :class:`TilemapOptions` or :obj:`None <python:None>`
        """
        return self._tilemap

    @tilemap.setter
    @class_sensitive(TilemapOptions)
    def tilemap(self, value):
        self._tilemap = value

    @property
    def timeline(self) -> Optional[TimelineOptions]:
        """General options to apply to all Timeline series types.

        The timeline series presents given events along a drawn line.

        .. tabs::

          .. tab:: Standard Timeline

            .. figure:: ../../../_static/timeline-example.png
              :alt: Timeline Example Chart
              :align: center

          .. tab:: Inverted Timeline

            .. figure:: ../../../_static/timeline-example-inverted.png
              :alt: Inverted Timeline Example Chart
              :align: center

          .. tab:: With True Datetime Axis

            .. figure:: ../../../_static/timeline-example-datetime.png
              :alt: Timeline Example Chart with Datetime Axis
              :align: center

        :rtype: :class:`TimelineOptions` or :obj:`None <python:None>`
        """
        return self._timeline

    @timeline.setter
    @class_sensitive(TimelineOptions)
    def timeline(self, value):
        self._timeline = value

    @property
    def treegraph(self) -> Optional[TreegraphOptions]:
        """General options to apply to all :term:`Treegraph` series types.
        
        A treegraph visualizes a relationship between ancestors and descendants with a clear parent-child relationship,
        e.g. a family tree or a directory structure.
        
        .. figure:: ../../../_static/treegraph-example.png
          :alt: Treegraph Example Chart
          :align: center
        
        :rtype: :class:`TreegraphOptions <highcharts_core.options.plot_options.treegraph.TreegraphOptions>` or 
          :obj:`None <python:None>`
        """
        return self._treegraph
    
    @treegraph.setter
    @class_sensitive(TreegraphOptions)
    def treegraph(self, value):
        self._treegraph = value

    @property
    def treemap(self) -> Optional[TreemapOptions]:
        """General options to apply to all Treemap series types.

        A treemap displays hierarchical data using nested rectangles. The data can be laid
        out in varying ways depending on options.

        .. figure:: ../../../_static/treemap-example.png
          :alt: Treemap Example Chart
          :align: center

        :rtype: :class:`TreemapOptions` or :obj:`None <python:None>`
        """
        return self._treemap

    @treemap.setter
    @class_sensitive(TreemapOptions)
    def treemap(self, value):
        self._treemap = value

    @property
    def variablepie(self) -> Optional[VariablePieOptions]:
        """General options to apply to all Variable Pie series types.

        A variable pie series is a two dimensional series type, where each point renders
        an Y and Z value. Each point is drawn as a pie slice where the size (arc) of the
        slice relates to the Y value and the radius of pie slice relates to the Z value.

        .. figure:: ../../../_static/variablepie-example.png
          :alt: Variable Pie Example Chart
          :align: center

        :rtype: :class:`VariablePieOptions` or :obj:`None <python:None>`
        """
        return self._variablepie

    @variablepie.setter
    @class_sensitive(VariablePieOptions)
    def variablepie(self, value):
        self._variablepie = value

    @property
    def variwide(self) -> Optional[VariwideOptions]:
        """General options to apply to all Variwide series types.

        A variwide chart (related to marimekko chart) is a column chart with a variable
        width expressing a third dimension.

        .. tabs::

          .. tab:: Standard Variwide

            .. figure:: ../../../_static/variwide-example.png
              :alt: Variwide Example Chart
              :align: center

          .. tab:: Inverted Variwide

            .. figure:: ../../../_static/variwide-example-inverted.png
              :alt: Variwide Example Chart
              :align: center

          .. tab:: with Datetime Axis

            .. figure:: ../../../_static/variwide-example-datetime.png
              :alt: Variwide Example Chart
              :align: center

        :rtype: :class:`VariwideOptions` or :obj:`None <python:None>`
        """
        return self._variwide

    @variwide.setter
    @class_sensitive(VariwideOptions)
    def variwide(self, value):
        self._variwide = value

    @property
    def vector(self) -> Optional[VectorOptions]:
        """General options to apply to all Vector series types.

        A vector plot is a type of cartesian chart where each point has an X and Y
        position, a length and a direction. Vectors are drawn as arrows.

        .. figure:: ../../../_static/vector-example.png
          :alt: Vector Example Chart
          :align: center

        :rtype: :class:`VectorOptions` or :obj:`None <python:None>`
        """
        return self._vector

    @vector.setter
    @class_sensitive(VectorOptions)
    def vector(self, value):
        self._vector = value

    @property
    def venn(self) -> Optional[VennOptions]:
        """General options to apply to all Venn series types.

        A Venn diagram displays all possible logical relations between a collection of
        different sets. The sets are represented by circles, and the relation between the
        sets are displayed by the overlap or lack of overlap between them. The venn
        diagram is a special case of Euler diagrams, which can also be displayed by this
        series type.

        .. tabs::

          .. tab:: Venn Diagram

            .. figure:: ../../../_static/venn-example.png
              :alt: Venn Example Chart
              :align: center

          .. tab:: Euler Diagram

            .. figure:: ../../../_static/venn-example-euler.png
              :alt: Euler Example Chart
              :align: center

        :rtype: :class:`VennOptions` or :obj:`None <python:None>`
        """
        return self._venn

    @venn.setter
    @class_sensitive(VennOptions)
    def venn(self, value):
        self._venn = value

    @property
    def waterfall(self) -> Optional[WaterfallOptions]:
        """General options to apply to all Waterfall series types.

        A waterfall chart displays sequentially introduced positive or negative values in
        cumulative columns.

        .. tabs::

          .. tab:: Standard Waterfall

            .. figure:: ../../../_static/waterfall-example.png
              :alt: Waterfall Example Chart
              :align: center

          .. tab:: Horizontal (Inverted) Waterfall

            .. figure:: ../../../_static/waterfall-example-inverted.png
              :alt: Waterfall Example Chart
              :align: center

          .. tab:: Stacked Waterfall

            .. figure:: ../../../_static/waterfall-example-stacked.png
              :alt: Waterfall Example Chart
              :align: center

        :rtype: :class:`WaterfallOptions` or :obj:`None <python:None>`
        """
        return self._waterfall

    @waterfall.setter
    @class_sensitive(WaterfallOptions)
    def waterfall(self, value):
        self._waterfall = value

    @property
    def windbarb(self) -> Optional[WindBarbOptions]:
        """General options to apply to all Wind Barb series types.

        Wind barbs are a convenient way to represent wind speed and direction in one
        graphical form. Wind direction is given by the stem direction, and wind speed by
        the number and shape of barbs.

        .. figure:: ../../../_static/windbarb-example.png
          :alt: Wind Barb Example Chart
          :align: center

        :rtype: :class:`WindBarbOptions` or :obj:`None <python:None>`
        """
        return self._windbarb

    @windbarb.setter
    @class_sensitive(WindBarbOptions)
    def windbarb(self, value):
        self._windbarb = value

    @property
    def wordcloud(self) -> Optional[WordcloudOptions]:
        """General options to apply to all Wordcloud series types.

        A word cloud is a visualization of a set of words, where the size and placement of
        a word is determined by how it is weighted.

        .. figure:: ../../../_static/wordcloud-example.png
          :alt: Wordcloud Example Chart
          :align: center

        :rtype: :class:`WordcloudOptions` or :obj:`None <python:None>`
        """
        return self._wordcloud

    @wordcloud.setter
    @class_sensitive(WordcloudOptions)
    def wordcloud(self, value):
        self._wordcloud = value

    @property
    def xrange(self) -> Optional[XRangeOptions]:
        """General options to apply to all X-Range series types.

        The X-range series displays ranges on the X axis, typically time intervals with a
        start and end date.

        .. tabs::

          .. tab:: Standard X-Range

            .. figure:: ../../../_static/xrange-example.png
              :alt: X-Range Example Chart
              :align: center

          .. tab:: Inverted X-Range

            .. figure:: ../../../_static/xrange-example-inverted.png
              :alt: Inverted X-Range Example Chart
              :align: center

        :rtype: :class:`XRangeOptions` or :obj:`None <python:None>`
        """
        return self._xrange

    @xrange.setter
    @class_sensitive(XRangeOptions)
    def xrange(self, value):
        self._xrange = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'arcdiagram': as_dict.get('arcdiagram', None),
            'area': as_dict.get('area', None),
            'arearange': as_dict.get('arearange', None),
            'areaspline': as_dict.get('areaspline', None),
            'areasplinerange': as_dict.get('areasplinerange', None),
            'bar': as_dict.get('bar', None),
            'bellcurve': as_dict.get('bellcurve', None),
            'boxplot': as_dict.get('boxplot', None),
            'bubble': as_dict.get('bubble', None),
            'bullet': as_dict.get('bullet', None),
            'column': as_dict.get('column', None),
            'columnpyramid': as_dict.get('columnpyramid', None),
            'columnrange': as_dict.get('columnrange', None),
            'cylinder': as_dict.get('cylinder', None),
            'dependencywheel': as_dict.get('dependencywheel', None),
            'dumbbell': as_dict.get('dumbbell', None),
            'errorbar': as_dict.get('errorbar', None),
            'funnel': as_dict.get('funnel', None),
            'funnel_3d': as_dict.get('funnel3d', None),
            'gauge': as_dict.get('gauge', None),
            'heatmap': as_dict.get('heatmap', None),
            'histogram': as_dict.get('histogram', None),
            'item': as_dict.get('item', None),
            'line': as_dict.get('line', None),
            'lollipop': as_dict.get('lollipop', None),
            'networkgraph': as_dict.get('networkgraph', None),
            'organization': as_dict.get('organization', None),
            'packedbubble': as_dict.get('packedbubble', None),
            'pareto': as_dict.get('pareto', None),
            'pictorial': as_dict.get('pictorial', None),
            'pie': as_dict.get('pie', None),
            'polygon': as_dict.get('polygon', None),
            'pyramid': as_dict.get('pyramid', None),
            'pyramid_3d': as_dict.get('pyramid3d', None),
            'sankey': as_dict.get('sankey', None),
            'scatter': as_dict.get('scatter', None),
            'scatter_3d': as_dict.get('scatter3d', None),
            'series': as_dict.get('series', None),
            'solidgauge': as_dict.get('solidgauge', None),
            'spline': as_dict.get('spline', None),
            'streamgraph': as_dict.get('streamgraph', None),
            'sunburst': as_dict.get('sunburst', None),
            'tilemap': as_dict.get('tilemap', None),
            'timeline': as_dict.get('timeline', None),
            'treegraph': as_dict.get('treegraph', None),
            'treemap': as_dict.get('treemap', None),
            'variablepie': as_dict.get('variablepie', None),
            'variwide': as_dict.get('variwide', None),
            'vector': as_dict.get('vector', None),
            'venn': as_dict.get('venn', None),
            'waterfall': as_dict.get('waterfall', None),
            'windbarb': as_dict.get('windbarb', None),
            'wordcloud': as_dict.get('wordcloud', None),
            'xrange': as_dict.get('xrange', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'arcdiagram': self.arcdiagram,
            'area': self.area,
            'arearange': self.arearange,
            'areaspline': self.areaspline,
            'areasplinerange': self.areasplinerange,
            'bar': self.bar,
            'bellcurve': self.bellcurve,
            'boxplot': self.boxplot,
            'bubble': self.bubble,
            'bullet': self.bullet,
            'column': self.column,
            'columnpyramid': self.columnpyramid,
            'columnrange': self.columnrange,
            'cylinder': self.cylinder,
            'dependencywheel': self.dependencywheel,
            'dumbbell': self.dumbbell,
            'errorbar': self.errorbar,
            'funnel': self.funnel,
            'funnel3d': self.funnel_3d,
            'gauge': self.gauge,
            'heatmap': self.heatmap,
            'histogram': self.histogram,
            'item': self.item,
            'line': self.line,
            'lollipop': self.lollipop,
            'networkgraph': self.networkgraph,
            'organization': self.organization,
            'packedbubble': self.packedbubble,
            'pareto': self.pareto,
            'pictorial': self.pictorial,
            'pie': self.pie,
            'polygon': self.polygon,
            'pyramid': self.pyramid,
            'pyramid3d': self.pyramid_3d,
            'sankey': self.sankey,
            'scatter': self.scatter,
            'scatter3d': self.scatter_3d,
            'series': self.series,
            'solidgauge': self.solidgauge,
            'spline': self.spline,
            'streamgraph': self.streamgraph,
            'sunburst': self.sunburst,
            'tilemap': self.tilemap,
            'timeline': self.timeline,
            'treegraph': self.treegraph,
            'treemap': self.treemap,
            'variablepie': self.variablepie,
            'variwide': self.variwide,
            'vector': self.vector,
            'venn': self.venn,
            'waterfall': self.waterfall,
            'windbarb': self.windbarb,
            'wordcloud': self.wordcloud,
            'xrange': self.xrange
        }

        return untrimmed
