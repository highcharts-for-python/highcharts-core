from typing import Optional

import json

from validator_collection import validators, checkers

from highcharts import errors

from highcharts.options.series.base import SeriesBase
from highcharts.options.series.arcdiagram import ArcDiagramSeries
from highcharts.options.series.area import AreaSeries
from highcharts.options.series.area import AreaRangeSeries
from highcharts.options.series.area import AreaSplineSeries
from highcharts.options.series.area import AreaSplineRangeSeries
from highcharts.options.series.area import LineSeries
from highcharts.options.series.area import StreamGraphSeries
from highcharts.options.series.bar import BarSeries
from highcharts.options.series.bar import ColumnSeries
from highcharts.options.series.bar import ColumnPyramidSeries
from highcharts.options.series.bar import ColumnRangeSeries
from highcharts.options.series.bar import CylinderSeries
from highcharts.options.series.bar import VariwideSeries
from highcharts.options.series.bar import WaterfallSeries
from highcharts.options.series.bar import WindBarbSeries
from highcharts.options.series.bar import XRangeSeries
from highcharts.options.series.bellcurve import BellCurveSeries
from highcharts.options.series.boxplot import BoxPlotSeries
from highcharts.options.series.boxplot import ErrorBarSeries
from highcharts.options.series.bubble import BubbleSeries
from highcharts.options.series.bullet import BulletSeries
from highcharts.options.series.dependencywheel import DependencyWheelSeries
from highcharts.options.series.dumbbell import DumbbellSeries
from highcharts.options.series.dumbbell import LollipopSeries
from highcharts.options.series.funnel import FunnelSeries
from highcharts.options.series.funnel import Funnel3DSeries
from highcharts.options.series.gauge import GaugeSeries
from highcharts.options.series.gauge import SolidGaugeSeries
from highcharts.options.series.heatmap import HeatmapSeries
from highcharts.options.series.heatmap import TilemapSeries
from highcharts.options.series.histogram import HistogramSeries
from highcharts.options.series.item import ItemSeries
from highcharts.options.series.networkgraph import NetworkGraphSeries
from highcharts.options.series.organization import OrganizationSeries
from highcharts.options.series.packedbubble import PackedBubbleSeries
from highcharts.options.series.pareto import ParetoSeries
from highcharts.options.series.pie import PieSeries
from highcharts.options.series.pie import VariablePieSeries
from highcharts.options.series.polygon import PolygonSeries
from highcharts.options.series.pyramid import PyramidSeries
from highcharts.options.series.pyramid import Pyramid3DSeries
from highcharts.options.series.sankey import SankeySeries
from highcharts.options.series.scatter import ScatterSeries
from highcharts.options.series.scatter import Scatter3DSeries
from highcharts.options.series.spline import SplineSeries
from highcharts.options.series.sunburst import SunburstSeries
from highcharts.options.series.timeline import TimelineSeries
from highcharts.options.series.treemap import TreemapSeries
from highcharts.options.series.vector import VectorSeries
from highcharts.options.series.venn import VennSeries
from highcharts.options.series.wordcloud import WordcloudSeries


SERIES_CLASSES = {
    'arcdiagram': ArcDiagramSeries,
    'areaseries': AreaSeries,
    'arearange': AreaRangeSeries,
    'areaspline': AreaSplineSeries,
    'areasplinerange': AreaSplineRangeSeries,
    'line': LineSeries,
    'streamgraph': StreamGraphSeries,
    'bar': BarSeries,
    'column': ColumnSeries,
    'columnpyramid': ColumnPyramidSeries,
    'columnrange': ColumnRangeSeries,
    'cylinder': CylinderSeries,
    'variwide': VariwideSeries,
    'waterfall': WaterfallSeries,
    'windbarb': WindBarbSeries,
    'xrange': XRangeSeries,
    'bellcurve': BellCurveSeries,
    'boxplot': BoxPlotSeries,
    'errorbar': ErrorBarSeries,
    'bubble': BubbleSeries,
    'bullet': BulletSeries,
    'dependencywheel': DependencyWheelSeries,
    'dumbbell': DumbbellSeries,
    'lollipop': LollipopSeries,
    'funnel': FunnelSeries,
    'funnel3d': Funnel3DSeries,
    'gauge': GaugeSeries,
    'solidgauge': SolidGaugeSeries,
    'heatmap': HeatmapSeries,
    'tilemap': TilemapSeries,
    'histogram': HistogramSeries,
    'item': ItemSeries,
    'networkgraph': NetworkGraphSeries,
    'organization': OrganizationSeries,
    'packedbubble': PackedBubbleSeries,
    'pareto': ParetoSeries,
    'pie': PieSeries,
    'variablepie': VariablePieSeries,
    'polygon': PolygonSeries,
    'pyramid': PyramidSeries,
    'pyramid3d': Pyramid3DSeries,
    'sankey': SankeySeries,
    'scatter': ScatterSeries,
    'scatter3d': Scatter3DSeries,
    'spline': SplineSeries,
    'sunburst': SunburstSeries,
    'timeline': TimelineSeries,
    'treemap': TreemapSeries,
    'vector': VectorSeries,
    'venn': VennSeries,
    'wordcloud': WordcloudSeries,
}


def create_series_obj(value, default_type = None) -> Optional[SeriesBase]:
    """Create an instance descended from :class:`SeriesBase`.

    :param value: The input that should be de-serialized to a :class:`SeriesBase`
      instance. Expected to be either a :class:`SeriesBase` instance, a
      :class:`dict <python:dict>`, or a JSON :class:`str <python:str>`

    :param default_type: The default series type to apply if not specified in
      ``value``. Defaults to :obj:`None <python:None>`
    :type default_type: :class:`str <python:str>` or :obj:`None <python:None>`

    :returns: A :class:`SeriesBase` (descendant) instance
    :rtype: :class:`SeriesBase` or :obj:`None <python:None>`
    """
    if not value:
        return None

    if isinstance(value, SeriesBase):
        return value

    if isinstance(value, dict):
        type_ = value.get('type', default_type)
        if not type_:
            raise errors.HighchartsValueError('To instantiate a Series, the "type" must '
                                              'be provided. No "type" key was found.')
        cls = SERIES_CLASSES.get(type_, default_type)
        if not cls:
            raise errors.HighchartsValueError(f'create_series_obj expects a value with '
                                              f'a recognized "type". However, received a '
                                              f'"type" value that was not recognized: '
                                              f'{type_}')

        instance = cls.from_dict(value)
    elif isinstance(value, str):
        try:
            preliminary = SeriesBase.from_js_literal(value)
            type_ = preliminary.type
        except errors.HighchartsParseError:
            preliminary_as_dict = json.loads(value)

            type_ = preliminary_as_dict.get('type', default_type)

        if not type_:
            raise errors.HighchartsValueError('To instantiate a Series, the "type" must '
                                              'be provided. No "type" key was found.')
        cls = SERIES_CLASSES.get(type_, default_type)
        if not cls:
            raise errors.HighchartsValueError(f'create_series_obj expects a value with '
                                              f'a recognized "type". However, received a '
                                              f'"type" value that was not recognized: '
                                              f'{type_}')

        try:
            instance = cls.from_js_literal(value)
        except errors.HighchartsParseError:
            instance = cls.from_json(value)

    return instance
