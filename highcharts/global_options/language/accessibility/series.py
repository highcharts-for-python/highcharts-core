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

        self.arearange = kwargs.pop('arearange',
                                    constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('arearange'))
        self.areasplinerange = kwargs.pop('areasplinerange',
                                          constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('areasplinerange'))
        self.boxplot = kwargs.pop('boxplot',
                                  constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('boxplot'))
        self.bubble = kwargs.pop('bubble',
                                 constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('bubble'))
        self.columnrange = kwargs.pop('columnrange',
                                      constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('columnrange'))
        self.errorbar = kwargs.pop('errorbar',
                                   constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('errorbar'))
        self.funnel = kwargs.pop('funnel',
                                 constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('funnel'))
        self.pyramid = kwargs.pop('pyramid',
                                  constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('pyramid'))
        self.waterfall = kwargs.pop('waterfall',
                                    constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('waterfall'))

    @property
    def arearange(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('arearange')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._arearange

    @arearange.setter
    def arearange(self, value):
        if value == '':
            self._arearange = ''
        else:
            self._arearange = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('arearange')

    @property
    def areasplinerange(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('areasplinerange')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._areasplinerange

    @areasplinerange.setter
    def areasplinerange(self, value):
        if value == '':
            self._areasplinerange = ''
        else:
            self._areasplinerange = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('areasplinerange')

    @property
    def boxplot(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('boxplot')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._boxplot

    @boxplot.setter
    def boxplot(self, value):
        if value == '':
            self._boxplot = ''
        else:
            self._boxplot = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('boxplot')

    @property
    def bubble(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('bubble')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bubble

    @bubble.setter
    def bubble(self, value):
        if value == '':
            self._bubble = ''
        else:
            self._bubble = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('bubble')

    @property
    def columnrange(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('columnrange')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._columnrange

    @columnrange.setter
    def columnrange(self, value):
        if value == '':
            self._columnrange = ''
        else:
            self._columnrange = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('columnrange')

    @property
    def errorbar(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('errorbar')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._errorbar

    @errorbar.setter
    def errorbar(self, value):
        if value == '':
            self._errorbar = ''
        else:
            self._errorbar = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('errorbar')

    @property
    def funnel(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('funnel')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._funnel

    @funnel.setter
    def funnel(self, value):
        if value == '':
            self._funnel = ''
        else:
            self._funnel = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('funnel')

    @property
    def pyramid(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('pyramid')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._pyramid

    @pyramid.setter
    def pyramid(self, value):
        if value == '':
            self._pyramid = ''
        else:
            self._pyramid = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('pyramid')

    @property
    def waterfall(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('waterfall')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._waterfall

    @waterfall.setter
    def waterfall(self, value):
        if value == '':
            self._waterfall = ''
        else:
            self._waterfall = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('waterfall')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'arearange': as_dict.pop('arearange',
                                     constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('arearange')),
            'areasplinerange': as_dict.pop('areasplinerange',
                                           constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('areasplinerange')),
            'boxplot': as_dict.pop('boxplot',
                                   constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('boxplot')),
            'bubble': as_dict.pop('bubble',
                                  constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('bubble')),
            'columnrange': as_dict.pop('columnrange',
                                       constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('columnrange')),
            'errorbar': as_dict.pop('errorbar',
                                    constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('errorbar')),
            'funnel': as_dict.pop('funnel',
                                  constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('funnel')),
            'pyramid': as_dict.pop('pyramid',
                                   constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('pyramid')),
            'waterfall': as_dict.pop('waterfall',
                                     constants.DEFAULT_LANG_ACS_SERIES_TYPES.get('waterfall')),
        }

        return cls(**kwargs)

    def to_dict(self):
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

        return self.trim_dict(untrimmed)


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
    def bar(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bar

    @bar.setter
    def bar(self, value):
        if value == '':
            self._bar = ''
        else:
            self._bar = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar')

    @property
    def bar_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bar_combination

    @bar_combination.setter
    def bar_combination(self, value):
        if value == '':
            self._bar_combination = ''
        else:
            self._bar_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar_combination')

    @property
    def boxplot(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._boxplot

    @boxplot.setter
    def boxplot(self, value):
        if value == '':
            self._boxplot = ''
        else:
            self._boxplot = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot')

    @property
    def boxplot_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._boxplot_combination

    @boxplot_combination.setter
    def boxplot_combination(self, value):
        if value == '':
            self._boxplot_combination = ''
        else:
            self._boxplot_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot_combination')

    @property
    def bubble(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bubble

    @bubble.setter
    def bubble(self, value):
        if value == '':
            self._bubble = ''
        else:
            self._bubble = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble')

    @property
    def bubble_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bubble_combination

    @bubble_combination.setter
    def bubble_combination(self, value):
        if value == '':
            self._bubble_combination = ''
        else:
            self._bubble_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble_combination')

    @property
    def column(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._column

    @column.setter
    def column(self, value):
        if value == '':
            self._column = ''
        else:
            self._column = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column')

    @property
    def column_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._column_combination

    @column_combination.setter
    def column_combination(self, value):
        if value == '':
            self._column_combination = ''
        else:
            self._column_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column_combination')

    @property
    def default(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._default

    @default.setter
    def default(self, value):
        if value == '':
            self._default = ''
        else:
            self._default = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default')

    @property
    def default_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._default_combination

    @default_combination.setter
    def default_combination(self, value):
        if value == '':
            self._default_combination = ''
        else:
            self._default_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default_combination')

    @property
    def line(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._line

    @line.setter
    def line(self, value):
        if value == '':
            self._line = ''
        else:
            self._line = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line')

    @property
    def line_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._line_combination

    @line_combination.setter
    def line_combination(self, value):
        if value == '':
            self._line_combination = ''
        else:
            self._line_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line_combination')

    @property
    def map(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._map

    @map.setter
    def map(self, value):
        if value == '':
            self._map = ''
        else:
            self._map = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map')

    @property
    def map_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._map_combination

    @map_combination.setter
    def map_combination(self, value):
        if value == '':
            self._map_combination = ''
        else:
            self._map_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map_combination')

    @property
    def mapbubble(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._mapbubble

    @mapbubble.setter
    def mapbubble(self, value):
        if value == '':
            self._mapbubble = ''
        else:
            self._mapbubble = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble')

    @property
    def mapbubble_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._mapbubble_combination

    @mapbubble_combination.setter
    def mapbubble_combination(self, value):
        if value == '':
            self._mapbubble_combination = ''
        else:
            self._mapbubble_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble_combination')

    @property
    def mapline(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._mapline

    @mapline.setter
    def mapline(self, value):
        if value == '':
            self._mapline = ''
        else:
            self._mapline = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline')

    @property
    def mapline_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._mapline_combination

    @mapline_combination.setter
    def mapline_combination(self, value):
        if value == '':
            self._mapline_combination = ''
        else:
            self._mapline_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline_combination')

    @property
    def pie(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._pie

    @pie.setter
    def pie(self, value):
        if value == '':
            self._pie = ''
        else:
            self._pie = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie')

    @property
    def pie_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._pie_combination

    @pie_combination.setter
    def pie_combination(self, value):
        if value == '':
            self._pie_combination = ''
        else:
            self._pie_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie_combination')

    @property
    def scatter(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._scatter

    @scatter.setter
    def scatter(self, value):
        if value == '':
            self._scatter = ''
        else:
            self._scatter = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter')

    @property
    def scatter_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._scatter_combination

    @scatter_combination.setter
    def scatter_combination(self, value):
        if value == '':
            self._scatter_combination = ''
        else:
            self._scatter_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter_combination')

    @property
    def spline(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._spline

    @spline.setter
    def spline(self, value):
        if value == '':
            self._spline = ''
        else:
            self._spline = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline')

    @property
    def spline_combination(self) -> str:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline_combination')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._spline_combination

    @spline_combination.setter
    def spline_combination(self, value):
        if value == '':
            self._spline_combination = ''
        else:
            self._spline_combination = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline_combination')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'bar': as_dict.pop('bar',
                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar')),
            'bar_combination': as_dict.pop('barCombination',
                                           constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bar_combination')),
            'boxplot': as_dict.pop('boxplot',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot')),
            'boxplot_combination': as_dict.pop('boxplotCombination',
                                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('boxplot_combination')),
            'bubble': as_dict.pop('bubble',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble')),
            'bubble_combination': as_dict.pop('bubbleCombination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('bubble_combination')),
            'column': as_dict.pop('column',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column')),
            'column_combination': as_dict.pop('columnCombination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('column_combination')),
            'default': as_dict.pop('default',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default')),
            'default_combination': as_dict.pop('defaultCombination',
                                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('default_combination')),
            'line': as_dict.pop('line',
                                constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line')),
            'line_combination': as_dict.pop('lineCombination',
                                            constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('line_combination')),
            'map': as_dict.pop('map',
                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map')),
            'map_combination': as_dict.pop('mapCombination',
                                           constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('map_combination')),
            'mapbubble': as_dict.pop('mapbubble',
                                     constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble')),
            'mapbubble_combination': as_dict.pop('mapbubbleCombination',
                                                 constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapbubble_combination')),
            'mapline': as_dict.pop('mapline',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline')),
            'mapline_combination': as_dict.pop('maplineCombination',
                                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('mapline_combination')),
            'pie': as_dict.pop('pie',
                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie')),
            'pie_combination': as_dict.pop('pieCombination',
                                           constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('pie_combination')),
            'scatter': as_dict.pop('scatter',
                                   constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter')),
            'scatter_combination': as_dict.pop('scatterCombination',
                                               constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('scatter_combination')),
            'spline': as_dict.pop('spline',
                                  constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline')),
            'spline_combination': as_dict.pop('splineCombination',
                                              constants.DEFAULT_LANG_ACS_SERIES_SUMMARY.get('spline_combination')),
        }

        return cls(**kwargs)

    def to_dict(self):
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

        return self.trim_dict(untrimmed)


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

        self.description = kwargs.pop('description',
                                      constants.DEFAULT_LANG_ACS_SERIES_DESCRIPTION)
        self.null_point_value = kwargs.pop('null_point_value',
                                           constants.DEFAULT_LANG_ACS_SERIES_NULL_PT_VALUE)
        self.point_annotations_description = kwargs.pop('point_annotations_description',
                                                        constants.DEFAULT_LANG_ACS_SERIES_PT_ANNOTATIONS_DESCRIPTION)
        self.summary = kwargs.pop('summary', None)
        self.x_axis_description = kwargs.pop('x_axis_description',
                                             constants.DEFAULT_LANG_ACS_SERIES_XAXIS_DESCRIPTION)
        self.y_axis_description = kwargs.pop('y_axis_description',
                                             constants.DEFAULT_LANG_ACS_SERIES_YAXIS_DESCRIPTION)

    @property
    def description(self) -> str:
        """User supplied description text. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_SERIES_DESCRIPTION}'``.

        .. note::

          This is added in the point comment description by default if present.

        :rtype: :class:`str <python:str>`
        """
        return self._description

    @description.setter
    def description(self, value):
        if value == '':
            self._description = ''
        else:
            self._description = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_DESCRIPTION

    @property
    def null_point_value(self) -> str:
        """Description for the value of null points. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_SERIES_NULL_PT_VALUE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._null_point_value

    @null_point_value.setter
    def null_point_value(self, value):
        if value == '':
            self._null_point_value = ''
        else:
            self._null_point_value = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_NULL_PT_VALUE

    @property
    def point_annotations_description(self) -> str:
        """Description for annotations on a point, as it is made available to assistive
        technology. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_SERIES_PT_ANNOTATIONS_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._point_annotations_description

    @point_annotations_description.setter
    def point_annotations_description(self, value):
        if value == '':
            self._point_annotations_description = ''
        else:
            self._point_annotations_description = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_PT_ANNOTATIONS_DESCRIPTION

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

          The series index (starting from 1) can be accessed with the ``{seriesNumber}`` variable.

        :rtype: :class:`SeriesSummaryLanguageOptions` or :obj:`None <python:None>`
        """
        return self._summary

    @summary.setter
    @class_sensitive(SeriesSummaryLanguageOptions)
    def summary(self, value):
        self._summary = value

    @property
    def x_axis_description(self) -> str:
        """xAxis description for series if there are multiple xAxes in the chart. Defaults
        to: ``'{constants.DEFAULT_LANG_ACS_SERIES_XAXIS_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._x_axis_description

    @x_axis_description.setter
    def x_axis_description(self, value):
        if value == '':
            self._x_axis_description = ''
        else:
            self._x_axis_description = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_XAXIS_DESCRIPTION

    @property
    def y_axis_description(self) -> str:
        """yAxis description for series if there are multiple yAxes in the chart. Defaults
        to: ``'{constants.DEFAULT_LANG_ACS_SERIES_YAXIS_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._y_axis_description

    @y_axis_description.setter
    def y_axis_description(self, value):
        if value == '':
            self._y_axis_description = ''
        else:
            self._y_axis_description = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_SERIES_YAXIS_DESCRIPTION

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.pop('description',
                                       constants.DEFAULT_LANG_ACS_SERIES_DESCRIPTION),
            'null_point_value': as_dict.pop('nullPointValue',
                                            constants.DEFAULT_LANG_ACS_SERIES_NULL_PT_VALUE),
            'point_annotations_description': as_dict.pop('pointAnnotationsDescription',
                                                         constants.DEFAULT_LANG_ACS_SERIES_PT_ANNOTATIONS_DESCRIPTION),
            'summary': as_dict.pop('summary', None),
            'x_axis_description': as_dict.pop('xAxisDescription',
                                              constants.DEFAULT_LANG_ACS_SERIES_XAXIS_DESCRIPTION),
            'y_axis_description': as_dict.pop('yAxisDescription',
                                              constants.DEFAULT_LANG_ACS_SERIES_YAXIS_DESCRIPTION)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'description': self.description,
            'nullPointValue': self.null_point_value,
            'pointAnnotationsDescription': self.point_annotations_description,
            'summary': self.summary,
            'xAxisDescription': self.x_axis_description,
            'yAxisDescription': self.y_axis_description
        }

        return self.trim_dict(untrimmed)
