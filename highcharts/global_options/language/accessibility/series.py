from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


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

        self.arearange = kwargs.pop('arearange', None)
        self.areasplinerange = kwargs.pop('areasplinerange', None)
        self.boxplot = kwargs.pop('boxplot', None)
        self.bubble = kwargs.pop('bubble', None)
        self.columnrange = kwargs.pop('columnrange', None)
        self.errorbar = kwargs.pop('errorbar', None)
        self.funnel = kwargs.pop('funnel', None)
        self.pyramid = kwargs.pop('pyramid', None)
        self.waterfall = kwargs.pop('waterfall', None)

    @property
    def arearange(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('arearange')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._arearange

    @arearange.setter
    def arearange(self, value):
        self._arearange = validators.string(value, allow_empty = True)

    @property
    def areasplinerange(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('areasplinerange')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._areasplinerange

    @areasplinerange.setter
    def areasplinerange(self, value):
        self._areasplinerange = validators.string(value, allow_empty = True)

    @property
    def boxplot(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('boxplot')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._boxplot

    @boxplot.setter
    def boxplot(self, value):
        self._boxplot = validators.string(value, allow_empty = True)

    @property
    def bubble(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('bubble')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._bubble

    @bubble.setter
    def bubble(self, value):
        self._bubble = validators.string(value, allow_empty = True)

    @property
    def columnrange(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('columnrange')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._columnrange

    @columnrange.setter
    def columnrange(self, value):
        self._columnrange = validators.string(value, allow_empty = True)

    @property
    def errorbar(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('errorbar')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._errorbar

    @errorbar.setter
    def errorbar(self, value):
        self._errorbar = validators.string(value, allow_empty = True)

    @property
    def funnel(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('funnel')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._funnel

    @funnel.setter
    def funnel(self, value):
        self._funnel = validators.string(value, allow_empty = True)

    @property
    def pyramid(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('pyramid')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._pyramid

    @pyramid.setter
    def pyramid(self, value):
        self._pyramid = validators.string(value, allow_empty = True)

    @property
    def waterfall(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('waterfall')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._waterfall

    @waterfall.setter
    def waterfall(self, value):
        self._waterfall = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'arearange': as_dict.pop('arearange', None),
            'areasplinerange': as_dict.pop('areasplinerange', None),
            'boxplot': as_dict.pop('boxplot', None),
            'bubble': as_dict.pop('bubble', None),
            'columnrange': as_dict.pop('columnrange', None),
            'errorbar': as_dict.pop('errorbar', None),
            'funnel': as_dict.pop('funnel', None),
            'pyramid': as_dict.pop('pyramid', None),
            'waterfall': as_dict.pop('waterfall', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
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

        self.bar = kwargs.pop('bar',
                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar'))
        self.bar_combination = kwargs.pop('bar_combination',
                                          constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar_combination'))
        self.boxplot = kwargs.pop('boxplot',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot'))
        self.boxplot_combination = kwargs.pop('boxplot_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot_combination'))
        self.bubble = kwargs.pop('bubble',
                                 constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble'))
        self.bubble_combination = kwargs.pop('bubble_combination',
                                             constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble_combination'))
        self.column = kwargs.pop('column',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column'))
        self.column_combination = kwargs.pop('column_combination',
                                             constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column_combination'))
        self.default = kwargs.pop('default',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default'))
        self.default_combination = kwargs.pop('default_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default_combination'))
        self.line = kwargs.pop('line',
                                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line'))
        self.line_combination = kwargs.pop('line_combination',
                                           constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line_combination'))
        self.map = kwargs.pop('map',
                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map'))
        self.map_combination = kwargs.pop('map_combination',
                                          constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map_combination'))
        self.mapbubble = kwargs.pop('mapbubble',
                                     constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble'))
        self.mapbubble_combination = kwargs.pop('mapbubble_combination',
                                                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble_combination'))
        self.mapline = kwargs.pop('mapline',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline'))
        self.mapline_combination = kwargs.pop('mapline_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline_combination'))
        self.pie = kwargs.pop('pie',
                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie'))
        self.pie_combination = kwargs.pop('pie_combination',
                                          constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie_combination'))
        self.scatter = kwargs.pop('scatter',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter'))
        self.scatter_combination = kwargs.pop('scatter_combination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter_combination'))
        self.spline = kwargs.pop('spline',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline'))
        self.spline_combination = kwargs.pop('spline_combination',
                                             constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline_combination'))

    @property
    def bar(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = validators.string(value, allow_empty = True)

    @property
    def bar_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._bar_combination

    @bar_combination.setter
    def bar_combination(self, value):
        self._bar_combination = validators.string(value, allow_empty = True)

    @property
    def boxplot(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._boxplot

    @boxplot.setter
    def boxplot(self, value):
        self._boxplot = validators.string(value, allow_empty = True)

    @property
    def boxplot_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._boxplot_combination

    @boxplot_combination.setter
    def boxplot_combination(self, value):
        self._boxplot_combination = validators.string(value, allow_empty = True)

    @property
    def bubble(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._bubble

    @bubble.setter
    def bubble(self, value):
        self._bubble = validators.string(value, allow_empty = True)

    @property
    def bubble_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._bubble_combination

    @bubble_combination.setter
    def bubble_combination(self, value):
        self._bubble_combination = validators.string(value, allow_empty = True)

    @property
    def column(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._column

    @column.setter
    def column(self, value):
        self._column = validators.string(value, allow_empty = True)

    @property
    def column_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._column_combination

    @column_combination.setter
    def column_combination(self, value):
        self._column_combination = validators.string(value, allow_empty = True)

    @property
    def default(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._default

    @default.setter
    def default(self, value):
        self._default = validators.string(value, allow_empty = True)

    @property
    def default_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._default_combination

    @default_combination.setter
    def default_combination(self, value):
        self._default_combination = validators.string(value, allow_empty = True)

    @property
    def line(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._line

    @line.setter
    def line(self, value):
        self._line = validators.string(value, allow_empty = True)

    @property
    def line_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._line_combination

    @line_combination.setter
    def line_combination(self, value):
        self._line_combination = validators.string(value, allow_empty = True)

    @property
    def map(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._map

    @map.setter
    def map(self, value):
        self._map = validators.string(value, allow_empty = True)

    @property
    def map_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._map_combination

    @map_combination.setter
    def map_combination(self, value):
        self._map_combination = validators.string(value, allow_empty = True)

    @property
    def mapbubble(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._mapbubble

    @mapbubble.setter
    def mapbubble(self, value):
        self._mapbubble = validators.string(value, allow_empty = True)

    @property
    def mapbubble_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._mapbubble_combination

    @mapbubble_combination.setter
    def mapbubble_combination(self, value):
        self._mapbubble_combination = validators.string(value, allow_empty = True)

    @property
    def mapline(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._mapline

    @mapline.setter
    def mapline(self, value):
        self._mapline = validators.string(value, allow_empty = True)

    @property
    def mapline_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._mapline_combination

    @mapline_combination.setter
    def mapline_combination(self, value):
        self._mapline_combination = validators.string(value, allow_empty = True)

    @property
    def pie(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._pie

    @pie.setter
    def pie(self, value):
        self._pie = validators.string(value, allow_empty = True)

    @property
    def pie_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._pie_combination

    @pie_combination.setter
    def pie_combination(self, value):
        self._pie_combination = validators.string(value, allow_empty = True)

    @property
    def scatter(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._scatter

    @scatter.setter
    def scatter(self, value):
        self._scatter = validators.string(value, allow_empty = True)

    @property
    def scatter_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._scatter_combination

    @scatter_combination.setter
    def scatter_combination(self, value):
        self._scatter_combination = validators.string(value, allow_empty = True)

    @property
    def spline(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._spline

    @spline.setter
    def spline(self, value):
        self._spline = validators.string(value, allow_empty = True)

    @property
    def spline_combination(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline_combination')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._spline_combination

    @spline_combination.setter
    def spline_combination(self, value):
        self._spline_combination = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'bar': as_dict.pop('bar', None),
            'bar_combination': as_dict.pop('barCombination', None),
            'boxplot': as_dict.pop('boxplot', None),
            'boxplot_combination': as_dict.pop('boxplotCombination', None),
            'bubble': as_dict.pop('bubble', None),
            'bubble_combination': as_dict.pop('bubbleCombination', None),
            'column': as_dict.pop('column', None),
            'column_combination': as_dict.pop('columnCombination', None),
            'default': as_dict.pop('default', None),
            'default_combination': as_dict.pop('defaultCombination', None),
            'line': as_dict.pop('line', None),
            'line_combination': as_dict.pop('lineCombination', None),
            'map': as_dict.pop('map', None),
            'map_combination': as_dict.pop('mapCombination', None),
            'mapbubble': as_dict.pop('mapbubble', None),
            'mapbubble_combination': as_dict.pop('mapbubbleCombination', None),
            'mapline': as_dict.pop('mapline', None),
            'mapline_combination': as_dict.pop('maplineCombination', None),
            'pie': as_dict.pop('pie', None),
            'pie_combination': as_dict.pop('pieCombination', None),
            'scatter': as_dict.pop('scatter', None),
            'scatter_combination': as_dict.pop('scatterCombination', None),
            'spline': as_dict.pop('spline', None),
            'spline_combination': as_dict.pop('splineCombination', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
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

        self.description = kwargs.pop('description', None)
        self.null_point_value = kwargs.pop('null_point_value', None)
        self.point_annotations_description = kwargs.pop('point_annotations_description',
                                                        None)
        self.summary = kwargs.pop('summary', None)
        self.x_axis_description = kwargs.pop('x_axis_description', None)
        self.y_axis_description = kwargs.pop('y_axis_description', None)

    @property
    def description(self) -> Optional[str]:
        """User supplied description text. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_SERIES_DESCRIPTION}'``.

        .. note::

          This is added in the point comment description by default if present.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def null_point_value(self) -> Optional[str]:
        """Description for the value of null points. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_SERIES_NULL_PT_VALUE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._null_point_value

    @null_point_value.setter
    def null_point_value(self, value):
        self._null_point_value = validators.string(value, allow_empty = True)

    @property
    def point_annotations_description(self) -> Optional[str]:
        """Description for annotations on a point, as it is made available to assistive
        technology. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_SERIES_PT_ANNOTATIONS_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
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
        to: ``'{constants.DEFAULT_LANG_ACS_SERIES_XAXIS_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._x_axis_description

    @x_axis_description.setter
    def x_axis_description(self, value):
        self._x_axis_description = validators.string(value, allow_empty = True)

    @property
    def y_axis_description(self) -> Optional[str]:
        """yAxis description for series if there are multiple yAxes in the chart. Defaults
        to: ``'{constants.DEFAULT_LANG_ACS_SERIES_YAXIS_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._y_axis_description

    @y_axis_description.setter
    def y_axis_description(self, value):
        self._y_axis_description = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.pop('description', None),
            'null_point_value': as_dict.pop('nullPointValue', None),
            'point_annotations_description': as_dict.pop('pointAnnotationsDescription',
                                                         None),
            'summary': as_dict.pop('summary', None),
            'x_axis_description': as_dict.pop('xAxisDescription', None),
            'y_axis_description': as_dict.pop('yAxisDescription', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'description': self.description,
            'nullPointValue': self.null_point_value,
            'pointAnnotationsDescription': self.point_annotations_description,
            'summary': self.summary,
            'xAxisDescription': self.x_axis_description,
            'yAxisDescription': self.y_axis_description
        }

        return untrimmed
