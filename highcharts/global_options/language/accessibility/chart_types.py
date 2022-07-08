from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class ChartTypesLanguageOptions(HighchartsMeta):
    """Chart type description strings.

    .. note::

      This is added to the chart information region.

      If there is only a single series type used in the chart, we use the format
      string for the series type, or default if missing. There is one format string
      for cases where there is only a single series in the chart, and one for multiple
      series of the same type.

    """

    def __init__(self, **kwargs):
        self._bar_multiple = None
        self._bar_single = None
        self._boxplot_multiple = None
        self._boxplot_single = None
        self._bubble_multiple = None
        self._bubble_single = None
        self._column_multiple = None
        self._column_single = None
        self._combination_chart = None
        self._default_multiple = None
        self._default_single = None
        self._empty_chart = None
        self._line_multiple = None
        self._line_single = None
        self._map_type_description = None
        self._pie_multiple = None
        self._pie_single = None
        self._scatter_multiple = None
        self._scatter_single = None
        self._spline_multiple = None
        self._spline_single = None
        self._unknown_map = None

        self.bar_multiple = kwargs.pop('bar_multiple',
                                       constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_MULTIPLE)
        self.bar_single = kwargs.pop('bar_single',
                                     constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_SINGLE)
        self.boxplot_multiple = kwargs.pop('boxplot_multiple',
                                           constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_MULTIPLE)
        self.boxplot_single = kwargs.pop('boxplot_single',
                                         constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_SINGLE)
        self.bubble_multiple = kwargs.pop('bubble_multiple',
                                          constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_MULTIPLE)
        self.bubble_single = kwargs.pop('bubble_single',
                                        constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_SINGLE)
        self.column_multiple = kwargs.pop('column_multiple',
                                          constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_MULTIPLE)
        self.column_single = kwargs.pop('column_single',
                                        constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_SINGLE)
        self.combination_chart = kwargs.pop('combination_chart',
                                               constants.DEFAULT_LANG_ACS_CHART_TYPES_COMBO)
        self.default_multiple = kwargs.pop('default_multiple',
                                           constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_MULTIPLE)
        self.default_single = kwargs.pop('default_single',
                                         constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_SINGLE)
        self.empty_chart = kwargs.pop('empty_chart',
                                      constants.DEFAULT_LANG_ACS_CHART_TYPES_EMPTY_CHART)
        self.line_multiple = kwargs.pop('line_multiple',
                                        constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_MULTIPLE)
        self.line_single = kwargs.pop('line_single',
                                      constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_SINGLE)
        self.map_type_description = kwargs.pop('map_type_description',
                                               constants.DEFAULT_LANG_ACS_CHART_TYPES_MAP_TYPE_DESCRIPTION)
        self.pie_multiple = kwargs.pop('pie_multiple',
                                       constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_MULTIPLE)
        self.pie_single = kwargs.pop('pie_single',
                                     constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_SINGLE)
        self.scatter_multiple = kwargs.pop('scatter_multiple',
                                           constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_MULTIPLE)
        self.scatter_single = kwargs.pop('scatter_single',
                                         constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_SINGLE)
        self.spline_multiple = kwargs.pop('spline_multiple',
                                          constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_MULTIPLE)
        self.spline_single = kwargs.pop('spline_single',
                                        constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_SINGLE)
        self.unknown_map = kwargs.pop('unknown_map',
                                      constants.DEFAULT_LANG_ACS_CHART_TYPES_UNKNOWN_MAP)

    @property
    def bar_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bar_multiple

    @bar_multiple.setter
    def bar_multiple(self, value):
        if value == '':
            self._bar_multiple = ''
        else:
            self._bar_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_MULTIPLE

    @property
    def bar_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bar_single

    @bar_single.setter
    def bar_single(self, value):
        if value == '':
            self._bar_single = ''
        else:
            self._bar_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_SINGLE

    @property
    def boxplot_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._boxplot_multiple

    @boxplot_multiple.setter
    def boxplot_multiple(self, value):
        if value == '':
            self._boxplot_multiple = ''
        else:
            self._boxplot_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_MULTIPLE

    @property
    def boxplot_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._boxplot_single

    @boxplot_single.setter
    def boxplot_single(self, value):
        if value == '':
            self._boxplot_single = ''
        else:
            self._boxplot_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_SINGLE

    @property
    def bubble_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bubble_multiple

    @bubble_multiple.setter
    def bubble_multiple(self, value):
        if value == '':
            self._bubble_multiple = ''
        else:
            self._bubble_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_MULTIPLE

    @property
    def bubble_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bubble_single

    @bubble_single.setter
    def bubble_single(self, value):
        if value == '':
            self._bubble_single = ''
        else:
            self._bubble_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_SINGLE

    @property
    def column_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._column_multiple

    @column_multiple.setter
    def column_multiple(self, value):
        if value == '':
            self._column_multiple = ''
        else:
            self._column_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_MULTIPLE

    @property
    def column_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._column_single

    @column_single.setter
    def column_single(self, value):
        if value == '':
            self._column_single = ''
        else:
            self._column_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_SINGLE

    @property
    def combination_chart(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_COMBO}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._combination_chart

    @combination_chart.setter
    def combination_chart(self, value):
        if value == '':
            self._combination_chart = ''
        else:
            self._combination_chart = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_COMBO

    @property
    def default_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._default_multiple

    @default_multiple.setter
    def default_multiple(self, value):
        if value == '':
            self._default_multiple = ''
        else:
            self._default_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_MULTIPLE

    @property
    def default_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._default_single

    @default_single.setter
    def default_single(self, value):
        if value == '':
            self._default_single = ''
        else:
            self._default_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_SINGLE

    @property
    def empty_chart(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_EMPTY_CHART}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._empty_chart

    @empty_chart.setter
    def empty_chart(self, value):
        if value == '':
            self._empty_chart = ''
        else:
            self._empty_chart = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_EMPTY_CHART

    @property
    def line_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._line_multiple

    @line_multiple.setter
    def line_multiple(self, value):
        if value == '':
            self._line_multiple = ''
        else:
            self._line_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_MULTIPLE

    @property
    def line_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._line_single

    @line_single.setter
    def line_single(self, value):
        if value == '':
            self._line_single = ''
        else:
            self._line_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_SINGLE

    @property
    def map_type_description(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_MAP_TYPE_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._map_type_description

    @map_type_description.setter
    def map_type_description(self, value):
        if value == '':
            self._map_type_description = ''
        else:
            self._map_type_description = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_MAP_TYPE_DESCRIPTION

    @property
    def pie_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._pie_multiple

    @pie_multiple.setter
    def pie_multiple(self, value):
        if value == '':
            self._pie_multiple = ''
        else:
            self._pie_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_MULTIPLE

    @property
    def pie_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._pie_single

    @pie_single.setter
    def pie_single(self, value):
        if value == '':
            self._pie_single = ''
        else:
            self._pie_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_SINGLE

    @property
    def scatter_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._scatter_multiple

    @scatter_multiple.setter
    def scatter_multiple(self, value):
        if value == '':
            self._scatter_multiple = ''
        else:
            self._scatter_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_MULTIPLE

    @property
    def scatter_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._scatter_single

    @scatter_single.setter
    def scatter_single(self, value):
        if value == '':
            self._scatter_single = ''
        else:
            self._scatter_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_SINGLE

    @property
    def spline_multiple(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._spline_multiple

    @spline_multiple.setter
    def spline_multiple(self, value):
        if value == '':
            self._spline_multiple = ''
        else:
            self._spline_multiple = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_MULTIPLE

    @property
    def spline_single(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_SINGLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._spline_single

    @spline_single.setter
    def spline_single(self, value):
        if value == '':
            self._spline_single = ''
        else:
            self._spline_single = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_SINGLE

    @property
    def unknown_map(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_UNKNOWN_MAP}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._unknown_map

    @unknown_map.setter
    def unknown_map(self, value):
        if value == '':
            self._unknown_map = ''
        else:
            self._unknown_map = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_CHART_TYPES_UNKNOWN_MAP

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'bar_multiple': as_dict.pop('barMultiple',
                                        constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_MULTIPLE),
            'bar_single': as_dict.pop('barSingle',
                                      constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_SINGLE),
            'boxplot_multiple': as_dict.pop('boxplotMultiple',
                                            constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_MULTIPLE),
            'boxplot_single': as_dict.pop('boxplotSingle',
                                          constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_SINGLE),
            'bubble_multiple': as_dict.pop('bubbleMultiple',
                                           constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_MULTIPLE),
            'bubble_single': as_dict.pop('bubbleSingle',
                                         constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_SINGLE),
            'column_multiple': as_dict.pop('columnMultiple',
                                           constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_MULTIPLE),
            'column_single': as_dict.pop('columnSingle',
                                         constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_SINGLE),
            'combination_multiple': as_dict.pop('combinationMultiple',
                                                constants.DEFAULT_LANG_ACS_CHART_TYPES_COMBO_MULTIPLE),
            'combination_single': as_dict.pop('combinationSingle',
                                              constants.DEFAULT_LANG_ACS_CHART_TYPES_COMBO_SINGLE),
            'default_multiple': as_dict.pop('defaultMultiple',
                                            constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_MULTIPLE),
            'default_single': as_dict.pop('defaultSingle',
                                          constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_SINGLE),
            'empty_chart': as_dict.pop('emptyChart',
                                       constants.DEFAULT_LANG_ACS_CHART_TYPES_EMPTY_CHART),
            'line_multiple': as_dict.pop('lineMultiple',
                                         constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_MULTIPLE),
            'line_single': as_dict.pop('lineSingle',
                                       constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_SINGLE),
            'map_type_description': as_dict.pop('map_type_description',
                                                constants.DEFAULT_LANG_ACS_CHART_TYPES_MAP_TYPE_DESCRIPTION),
            'pie_multiple': as_dict.pop('pieMultiple',
                                        constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_MULTIPLE),
            'pie_single': as_dict.pop('pieSingle',
                                      constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_SINGLE),
            'scatter_multiple': as_dict.pop('scatterMultiple',
                                            constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_MULTIPLE),
            'scatter_single': as_dict.pop('scatterSingle',
                                          constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_SINGLE),
            'spline_multiple': as_dict.pop('splineMultiple',
                                           constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_MULTIPLE),
            'spline_single': as_dict.pop('splineSingle',
                                         constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_SINGLE),
            'unknown_map': as_dict.pop('unknownMap',
                                       constants.DEFAULT_LANG_ACS_CHART_TYPES_UNKNOWN_MAP)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'barMultiple': self.bar_multiple,
            'barSingle': self.bar_single,
            'boxplotMultiple': self.boxplot_multiple,
            'boxplotSingle': self.boxplot_single,
            'bubbleMultiple': self.bubble_multiple,
            'bubbleSingle': self.bubble_single,
            'columnMultiple': self.column_multiple,
            'columnSingle': self.column_single,
            'combinationMultiple': self.combination_multiple,
            'combinationSingle': self.combination_single,
            'defaultMultiple': self.default_multiple,
            'defaultSingle': self.default_single,
            'emptyChart': self.empty_chart,
            'lineMultiple': self.line_multiple,
            'lineSingle': self.line_single,
            'map_type_description': self.map_type_description,
            'pieMultiple': self.pie_multiple,
            'pieSingle': self.pie_single,
            'scatterMultiple': self.scatter_multiple,
            'scatterSingle': self.scatter_single,
            'splineMultiple': self.spline_multiple,
            'splineSingle': self.spline_single,
            'unknownMap': self.unknown_map
        }

        return self.trim_dict(untrimmed)
