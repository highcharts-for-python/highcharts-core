from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class SeriesTypeDescriptions(HighchartsMeta):
    """Descriptions of lesser known series types. The relevant description is added to
    the screen reader information region when these series types are used."""

    def __init__(self, **kwargs):
        self._arearange = None
        self._areasplinerange = None
        self._boxplot = None
        self._bubble = None
        self._columnrange = None
        self._errorbar = None
        self._funnel = None
        self._pyramid = None
        self._waterfall = None

        self.arearange = kwargs.get('arearange', None)
        self.areasplinerange = kwargs.get('areasplinerange', None)
        self.boxplot = kwargs.get('boxplot', None)
        self.bubble = kwargs.get('bubble', None)
        self.columnrange = kwargs.get('columnrange', None)
        self.errorbar = kwargs.get('errorbar', None)
        self.funnel = kwargs.get('funnel', None)
        self.pyramid = kwargs.get('pyramid', None)
        self.waterfall = kwargs.get('waterfall', None)

    @property
    def arearange(self) -> Optional[str]:
        """Defaults to ``'Arearange charts are line charts displaying a range between a lower and higher value for each point.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._arearange

    @arearange.setter
    def arearange(self, value):
        self._arearange = validators.string(value, allow_empty = True)

    @property
    def areasplinerange(self) -> Optional[str]:
        """Defaults to
        ``'These charts are line charts displaying a range between a lower and higher value for each point.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._areasplinerange

    @areasplinerange.setter
    def areasplinerange(self, value):
        self._areasplinerange = validators.string(value, allow_empty = True)

    @property
    def boxplot(self) -> Optional[str]:
        """Defaults to ``'Box plot charts are typically used to display groups of statistical data. Each data point in the chart can have up to 5 values: minimum, lower quartile, median, upper quartile, and maximum.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boxplot

    @boxplot.setter
    def boxplot(self, value):
        self._boxplot = validators.string(value, allow_empty = True)

    @property
    def bubble(self) -> Optional[str]:
        """Defaults to ``'Bubble charts are scatter charts where each data point also has a size value.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bubble

    @bubble.setter
    def bubble(self, value):
        self._bubble = validators.string(value, allow_empty = True)

    @property
    def columnrange(self) -> Optional[str]:
        """Defaults to
        ``'Columnrange charts are column charts displaying a range between a lower and higher value for each point.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._columnrange

    @columnrange.setter
    def columnrange(self, value):
        self._columnrange = validators.string(value, allow_empty = True)

    @property
    def errorbar(self) -> Optional[str]:
        """Defaults to ``'Errorbar series are used to display the variability of the data.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._errorbar

    @errorbar.setter
    def errorbar(self, value):
        self._errorbar = validators.string(value, allow_empty = True)

    @property
    def funnel(self) -> Optional[str]:
        """Defaults to ``'Funnel charts are used to display reduction of data in stages.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._funnel

    @funnel.setter
    def funnel(self, value):
        self._funnel = validators.string(value, allow_empty = True)

    @property
    def pyramid(self) -> Optional[str]:
        """Defaults to ``'Pyramid charts consist of a single pyramid with item heights corresponding to each point value.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pyramid

    @pyramid.setter
    def pyramid(self, value):
        self._pyramid = validators.string(value, allow_empty = True)

    @property
    def waterfall(self) -> Optional[str]:
        """Defaults to ``'A waterfall chart is a column chart where each column contributes towards a total end value.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._waterfall

    @waterfall.setter
    def waterfall(self, value):
        self._waterfall = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'arearange': as_dict.get('arearange', None),
            'areasplinerange': as_dict.get('areasplinerange', None),
            'boxplot': as_dict.get('boxplot', None),
            'bubble': as_dict.get('bubble', None),
            'columnrange': as_dict.get('columnrange', None),
            'errorbar': as_dict.get('errorbar', None),
            'funnel': as_dict.get('funnel', None),
            'pyramid': as_dict.get('pyramid', None),
            'waterfall': as_dict.get('waterfall', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'arearange': self.arearange,
            'areasplinerange': self.areasplinerange,
            'boxplot': self.boxplot,
            'bubble': self.bubble,
            'columnrange': self.columnrange,
            'errorbar': self.errorbar,
            'funnel': self.funnel,
            'pyramid': self.pyramid,
            'waterfall': self.waterfall
        }

        return untrimmed


class SeriesSummaryLanguageOptions(HighchartsMeta):
    """Language configuration for the series main summary.

    Each series type has two modes:

      #. This series type is the only series type used in the chart
      #. This is a combination chart with multiple series types

    .. note::

      If a definition does not exist for the specific series type and mode, the
      ``'default'`` language definitions are used.

      Chart and its subproperties can be accessed with the ``{chart}`` variable. The
      series and its subproperties can be accessed with the ``{series}`` variable.

      The series index (starting from 1) can be accessed with the ``{seriesNumber}``
      variable.

    """

    def __init__(self, **kwargs):
        self._bar = None
        self._bar_combination = None
        self._boxplot = None
        self._boxplot_combination = None
        self._bubble = None
        self._bubble_combination = None
        self._column = None
        self._column_combination = None
        self._default = None
        self._default_combination = None
        self._line = None
        self._line_combination = None
        self._map = None
        self._map_combination = None
        self._mapbubble = None
        self._mapbubble_combination = None
        self._mapline = None
        self._mapline_combination = None
        self._pie = None
        self._pie_combination = None
        self._scatter = None
        self._scatter_combination = None
        self._spline = None
        self._spline_combination = None

        self.bar = kwargs.get('bar',
                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar'))
        self.bar_combination = kwargs.get('bar_combination',
                                          constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar_combination'))
        self.boxplot = kwargs.get('boxplot',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot'))
        self.boxplot_combination = kwargs.get('boxplot_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot_combination'))
        self.bubble = kwargs.get('bubble',
                                 constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble'))
        self.bubble_combination = kwargs.get('bubble_combination',
                                             constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble_combination'))
        self.column = kwargs.get('column',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column'))
        self.column_combination = kwargs.get('column_combination',
                                             constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column_combination'))
        self.default = kwargs.get('default',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default'))
        self.default_combination = kwargs.get('default_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default_combination'))
        self.line = kwargs.get('line',
                                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line'))
        self.line_combination = kwargs.get('line_combination',
                                           constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line_combination'))
        self.map = kwargs.get('map',
                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map'))
        self.map_combination = kwargs.get('map_combination',
                                          constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map_combination'))
        self.mapbubble = kwargs.get('mapbubble',
                                     constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble'))
        self.mapbubble_combination = kwargs.get('mapbubble_combination',
                                                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble_combination'))
        self.mapline = kwargs.get('mapline',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline'))
        self.mapline_combination = kwargs.get('mapline_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline_combination'))
        self.pie = kwargs.get('pie',
                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie'))
        self.pie_combination = kwargs.get('pie_combination',
                                          constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie_combination'))
        self.scatter = kwargs.get('scatter',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter'))
        self.scatter_combination = kwargs.get('scatter_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter_combination'))
        self.spline = kwargs.get('spline',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline'))
        self.spline_combination = kwargs.get('spline_combination',
                                             constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline_combination'))

    @property
    def bar(self) -> Optional[str]:
        """Defaults to ``'{series.name}, bar series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bars, bar)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = validators.string(value, allow_empty = True)

    @property
    def bar_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Bar series with {series.points.length} {#plural(series.points.length, bars, bar)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bar_combination

    @bar_combination.setter
    def bar_combination(self, value):
        self._bar_combination = validators.string(value, allow_empty = True)

    @property
    def boxplot(self) -> Optional[str]:
        """Defaults to ``'{series.name}, boxplot {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, boxes, box)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boxplot

    @boxplot.setter
    def boxplot(self, value):
        self._boxplot = validators.string(value, allow_empty = True)

    @property
    def boxplot_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Boxplot with {series.points.length} {#plural(series.points.length, boxes, box)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boxplot_combination

    @boxplot_combination.setter
    def boxplot_combination(self, value):
        self._boxplot_combination = validators.string(value, allow_empty = True)

    @property
    def bubble(self) -> Optional[str]:
        """Defaults to ``'{series.name}, bubble series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bubble

    @bubble.setter
    def bubble(self, value):
        self._bubble = validators.string(value, allow_empty = True)

    @property
    def bubble_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Bubble series with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bubble_combination

    @bubble_combination.setter
    def bubble_combination(self, value):
        self._bubble_combination = validators.string(value, allow_empty = True)

    @property
    def column(self) -> Optional[str]:
        """Defaults to ``'{series.name}, bar series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bars, bar)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._column

    @column.setter
    def column(self, value):
        self._column = validators.string(value, allow_empty = True)

    @property
    def column_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Bar series with {series.points.length} {#plural(series.points.length, bars, bar)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._column_combination

    @column_combination.setter
    def column_combination(self, value):
        self._column_combination = validators.string(value, allow_empty = True)

    @property
    def default(self) -> Optional[str]:
        """Defaults to ``'{series.name}, series {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._default

    @default.setter
    def default(self, value):
        self._default = validators.string(value, allow_empty = True)

    @property
    def default_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._default_combination

    @default_combination.setter
    def default_combination(self, value):
        self._default_combination = validators.string(value, allow_empty = True)

    @property
    def line(self) -> Optional[str]:
        """Defaults to ``'{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    def line(self, value):
        self._line = validators.string(value, allow_empty = True)

    @property
    def line_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_combination

    @line_combination.setter
    def line_combination(self, value):
        self._line_combination = validators.string(value, allow_empty = True)

    @property
    def map(self) -> Optional[str]:
        """Defaults to ``'{series.name}, map {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, areas, area)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map

    @map.setter
    def map(self, value):
        self._map = validators.string(value, allow_empty = True)

    @property
    def map_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Map with {series.points.length} {#plural(series.points.length, areas, area)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map_combination

    @map_combination.setter
    def map_combination(self, value):
        self._map_combination = validators.string(value, allow_empty = True)

    @property
    def mapbubble(self) -> Optional[str]:
        """Defaults to ``'{series.name}, bubble series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mapbubble

    @mapbubble.setter
    def mapbubble(self, value):
        self._mapbubble = validators.string(value, allow_empty = True)

    @property
    def mapbubble_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Bubble series with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mapbubble_combination

    @mapbubble_combination.setter
    def mapbubble_combination(self, value):
        self._mapbubble_combination = validators.string(value, allow_empty = True)

    @property
    def mapline(self) -> Optional[str]:
        """Defaults to ``'{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mapline

    @mapline.setter
    def mapline(self, value):
        self._mapline = validators.string(value, allow_empty = True)

    @property
    def mapline_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mapline_combination

    @mapline_combination.setter
    def mapline_combination(self, value):
        self._mapline_combination = validators.string(value, allow_empty = True)

    @property
    def pie(self) -> Optional[str]:
        """Defaults to ``'{series.name}, pie {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, slices, slice)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pie

    @pie.setter
    def pie(self, value):
        self._pie = validators.string(value, allow_empty = True)

    @property
    def pie_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Pie with {series.points.length} {#plural(series.points.length, slices, slice)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pie_combination

    @pie_combination.setter
    def pie_combination(self, value):
        self._pie_combination = validators.string(value, allow_empty = True)

    @property
    def scatter(self) -> Optional[str]:
        """Defaults to ``'{series.name}, scatter plot {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._scatter

    @scatter.setter
    def scatter(self, value):
        self._scatter = validators.string(value, allow_empty = True)

    @property
    def scatter_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}, scatter plot with {series.points.length} {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._scatter_combination

    @scatter_combination.setter
    def scatter_combination(self, value):
        self._scatter_combination = validators.string(value, allow_empty = True)

    @property
    def spline(self) -> Optional[str]:
        """Defaults to ``'{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._spline

    @spline.setter
    def spline(self, value):
        self._spline = validators.string(value, allow_empty = True)

    @property
    def spline_combination(self) -> Optional[str]:
        """Defaults to
        ``'{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#plural(series.points.length, points, point)}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._spline_combination

    @spline_combination.setter
    def spline_combination(self, value):
        self._spline_combination = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'bar': as_dict.get('bar', None),
            'bar_combination': as_dict.get('barCombination', None),
            'boxplot': as_dict.get('boxplot', None),
            'boxplot_combination': as_dict.get('boxplotCombination', None),
            'bubble': as_dict.get('bubble', None),
            'bubble_combination': as_dict.get('bubbleCombination', None),
            'column': as_dict.get('column', None),
            'column_combination': as_dict.get('columnCombination', None),
            'default': as_dict.get('default', None),
            'default_combination': as_dict.get('defaultCombination', None),
            'line': as_dict.get('line', None),
            'line_combination': as_dict.get('lineCombination', None),
            'map': as_dict.get('map', None),
            'map_combination': as_dict.get('mapCombination', None),
            'mapbubble': as_dict.get('mapbubble', None),
            'mapbubble_combination': as_dict.get('mapbubbleCombination', None),
            'mapline': as_dict.get('mapline', None),
            'mapline_combination': as_dict.get('maplineCombination', None),
            'pie': as_dict.get('pie', None),
            'pie_combination': as_dict.get('pieCombination', None),
            'scatter': as_dict.get('scatter', None),
            'scatter_combination': as_dict.get('scatterCombination', None),
            'spline': as_dict.get('spline', None),
            'spline_combination': as_dict.get('splineCombination', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'bar': self.bar,
            'barCombination': self.bar_combination,
            'boxplot': self.boxplot,
            'boxplotCombination': self.boxplot_combination,
            'bubble': self.bubble,
            'bubbleCombination': self.bubble_combination,
            'column': self.column,
            'columnCombination': self.column_combination,
            'default': self.default,
            'defaultCombination': self.default_combination,
            'line': self.line,
            'lineCombination': self.line_combination,
            'map': self.map,
            'mapCombination': self.map_combination,
            'mapbubble': self.mapbubble,
            'mapbubbleCombination': self.mapbubble_combination,
            'mapline': self.mapline,
            'maplineCombination': self.mapline_combination,
            'pie': self.pie,
            'pieCombination': self.pie_combination,
            'scatter': self.scatter,
            'scatterCombination': self.scatter_combination,
            'spline': self.spline,
            'splineCombination': self.spline_combination
        }

        return untrimmed


class SeriesLanguageOptions(HighchartsMeta):
    """Language configuration for different series types.

    .. hint::

      For more dynamic control over the series element descriptions, see
      :meth:`Accessibility.series_description_formatter`.

    """

    def __init__(self, **kwargs):
        self._description = None
        self._null_point_value = None
        self._point_annotations_description = None
        self._summary = None
        self._x_axis_description = None
        self._y_axis_description = None

        self.description = kwargs.get('description', None)
        self.null_point_value = kwargs.get('null_point_value', None)
        self.point_annotations_description = kwargs.get('point_annotations_description',
                                                        None)
        self.summary = kwargs.get('summary', None)
        self.x_axis_description = kwargs.get('x_axis_description', None)
        self.y_axis_description = kwargs.get('y_axis_description', None)

    @property
    def description(self) -> Optional[str]:
        """User supplied description text. Defaults to:
        ``''``.

        .. note::

          This is added in the point comment description by default if present.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def null_point_value(self) -> Optional[str]:
        """Description for the value of null points. Defaults to:
        ``''``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._null_point_value

    @null_point_value.setter
    def null_point_value(self, value):
        self._null_point_value = validators.string(value, allow_empty = True)

    @property
    def point_annotations_description(self) -> Optional[str]:
        """Description for annotations on a point, as it is made available to assistive
        technology. Defaults to:
        ``''``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_annotations_description

    @point_annotations_description.setter
    def point_annotations_description(self, value):
        self._point_annotations_description = validators.string(value, allow_empty = True)

    @property
    def summary(self) -> Optional[SeriesSummaryLanguageOptions]:
        """Language configuration for the series main summary.

        Each series type has two modes:

          #. This series type is the only series type used in the chart
          #. This is a combination chart with multiple series types

        .. note::

          If a definition does not exist for the specific series type and mode, the
          ``'default'`` language definitions are used.

          Chart and its subproperties can be accessed with the ``{chart}`` variable. The
          series and its subproperties can be accessed with the ``{series}`` variable.

          The series index (starting from 1) can be accessed with the ``{seriesNumber}``
          variable.

        :rtype: :class:`SeriesSummaryLanguageOptions` or :obj:`None <python:None>`
        """
        return self._summary

    @summary.setter
    @class_sensitive(SeriesSummaryLanguageOptions)
    def summary(self, value):
        self._summary = value

    @property
    def x_axis_description(self) -> Optional[str]:
        """xAxis description for series if there are multiple xAxes in the chart. Defaults
        to: ``''``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._x_axis_description

    @x_axis_description.setter
    def x_axis_description(self, value):
        self._x_axis_description = validators.string(value, allow_empty = True)

    @property
    def y_axis_description(self) -> Optional[str]:
        """yAxis description for series if there are multiple yAxes in the chart. Defaults
        to: ``''``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._y_axis_description

    @y_axis_description.setter
    def y_axis_description(self, value):
        self._y_axis_description = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.get('description', None),
            'null_point_value': as_dict.get('nullPointValue', None),
            'point_annotations_description': as_dict.get('pointAnnotationsDescription',
                                                         None),
            'summary': as_dict.get('summary', None),
            'x_axis_description': as_dict.get('xAxisDescription', None),
            'y_axis_description': as_dict.get('yAxisDescription', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'description': self.description,
            'nullPointValue': self.null_point_value,
            'pointAnnotationsDescription': self.point_annotations_description,
            'summary': self.summary,
            'xAxisDescription': self.x_axis_description,
            'yAxisDescription': self.y_axis_description
        }

        return untrimmed
