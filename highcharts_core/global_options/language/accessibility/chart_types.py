from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


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

        self.bar_multiple = kwargs.get('bar_multiple', None)
        self.bar_single = kwargs.get('bar_single', None)
        self.boxplot_multiple = kwargs.get('boxplot_multiple', None)
        self.boxplot_single = kwargs.get('boxplot_single', None)
        self.bubble_multiple = kwargs.get('bubble_multiple', None)
        self.bubble_single = kwargs.get('bubble_single', None)
        self.column_multiple = kwargs.get('column_multiple', None)
        self.column_single = kwargs.get('column_single', None)
        self.combination_chart = kwargs.get('combination_chart', None)
        self.default_multiple = kwargs.get('default_multiple', None)
        self.default_single = kwargs.get('default_single', None)
        self.empty_chart = kwargs.get('empty_chart', None)
        self.line_multiple = kwargs.get('line_multiple', None)
        self.line_single = kwargs.get('line_single', None)
        self.map_type_description = kwargs.get('map_type_description', None)
        self.pie_multiple = kwargs.get('pie_multiple', None)
        self.pie_single = kwargs.get('pie_single', None)
        self.scatter_multiple = kwargs.get('scatter_multiple', None)
        self.scatter_single = kwargs.get('scatter_single', None)
        self.spline_multiple = kwargs.get('spline_multiple', None)
        self.spline_single = kwargs.get('spline_single', None)
        self.unknown_map = kwargs.get('unknown_map', None)

    @property
    def bar_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
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
    def bar_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BAR_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bar_single

    @bar_single.setter
    def bar_single(self, value):
        self._bar_single = validators.string(value, allow_empty = True)

    @property
    def boxplot_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boxplot_multiple

    @boxplot_multiple.setter
    def boxplot_multiple(self, value):
        self._boxplot_multiple = validators.string(value, allow_empty = True)

    @property
    def boxplot_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boxplot_single

    @boxplot_single.setter
    def boxplot_single(self, value):
        self._boxplot_single = validators.string(value, allow_empty = True)

    @property
    def bubble_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bubble_multiple

    @bubble_multiple.setter
    def bubble_multiple(self, value):
        self._bubble_multiple = validators.string(value, allow_empty = True)

    @property
    def bubble_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bubble_single

    @bubble_single.setter
    def bubble_single(self, value):
        self._bubble_single = validators.string(value, allow_empty = True)

    @property
    def column_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._column_multiple

    @column_multiple.setter
    def column_multiple(self, value):
        self._column_multiple = validators.string(value, allow_empty = True)

    @property
    def column_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._column_single

    @column_single.setter
    def column_single(self, value):
        self._column_single = validators.string(value, allow_empty = True)

    @property
    def combination_chart(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_COMBO}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._combination_chart

    @combination_chart.setter
    def combination_chart(self, value):
        self._combination_chart = validators.string(value, allow_empty = True)

    @property
    def default_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._default_multiple

    @default_multiple.setter
    def default_multiple(self, value):
        self._default_multiple = validators.string(value, allow_empty = True)

    @property
    def default_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._default_single

    @default_single.setter
    def default_single(self, value):
        self._default_single = validators.string(value, allow_empty = True)

    @property
    def empty_chart(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_EMPTY_CHART}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._empty_chart

    @empty_chart.setter
    def empty_chart(self, value):
        self._empty_chart = validators.string(value, allow_empty = True)

    @property
    def line_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_multiple

    @line_multiple.setter
    def line_multiple(self, value):
        self._line_multiple = validators.string(value, allow_empty = True)

    @property
    def line_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_LINE_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_single

    @line_single.setter
    def line_single(self, value):
        self._line_single = validators.string(value, allow_empty = True)

    @property
    def map_type_description(self) -> Optional[str]:
        """Defaults to
        ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_MAP_TYPE_DESCRIPTION}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map_type_description

    @map_type_description.setter
    def map_type_description(self, value):
        self._map_type_description = validators.string(value, allow_empty = True)

    @property
    def pie_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pie_multiple

    @pie_multiple.setter
    def pie_multiple(self, value):
        self._pie_multiple = validators.string(value, allow_empty = True)

    @property
    def pie_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_PIE_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pie_single

    @pie_single.setter
    def pie_single(self, value):
        self._pie_single = validators.string(value, allow_empty = True)

    @property
    def scatter_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._scatter_multiple

    @scatter_multiple.setter
    def scatter_multiple(self, value):
        self._scatter_multiple = validators.string(value, allow_empty = True)

    @property
    def scatter_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._scatter_single

    @scatter_single.setter
    def scatter_single(self, value):
        self._scatter_single = validators.string(value, allow_empty = True)

    @property
    def spline_multiple(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._spline_multiple

    @spline_multiple.setter
    def spline_multiple(self, value):
        self._spline_multiple = validators.string(value, allow_empty = True)

    @property
    def spline_single(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._spline_single

    @spline_single.setter
    def spline_single(self, value):
        self._spline_single = validators.string(value, allow_empty = True)

    @property
    def unknown_map(self) -> Optional[str]:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_CHART_TYPES_UNKNOWN_MAP}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._unknown_map

    @unknown_map.setter
    def unknown_map(self, value):
        self._unknown_map = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'bar_multiple': as_dict.get('barMultiple', None),
            'bar_single': as_dict.get('barSingle', None),
            'boxplot_multiple': as_dict.get('boxplotMultiple', None),
            'boxplot_single': as_dict.get('boxplotSingle', None),
            'bubble_multiple': as_dict.get('bubbleMultiple', None),
            'bubble_single': as_dict.get('bubbleSingle', None),
            'column_multiple': as_dict.get('columnMultiple', None),
            'column_single': as_dict.get('columnSingle', None),
            'combination_chart': as_dict.get('combinationChart', None),
            'default_multiple': as_dict.get('defaultMultiple', None),
            'default_single': as_dict.get('defaultSingle', None),
            'empty_chart': as_dict.get('emptyChart', None),
            'line_multiple': as_dict.get('lineMultiple', None),
            'line_single': as_dict.get('lineSingle', None),
            'map_type_description': as_dict.get('mapTypeDescription', None),
            'pie_multiple': as_dict.get('pieMultiple', None),
            'pie_single': as_dict.get('pieSingle', None),
            'scatter_multiple': as_dict.get('scatterMultiple', None),
            'scatter_single': as_dict.get('scatterSingle', None),
            'spline_multiple': as_dict.get('splineMultiple', None),
            'spline_single': as_dict.get('splineSingle', None),
            'unknown_map': as_dict.get('unknownMap', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'barMultiple': self.bar_multiple,
            'barSingle': self.bar_single,
            'boxplotMultiple': self.boxplot_multiple,
            'boxplotSingle': self.boxplot_single,
            'bubbleMultiple': self.bubble_multiple,
            'bubbleSingle': self.bubble_single,
            'columnMultiple': self.column_multiple,
            'columnSingle': self.column_single,
            'combinationChart': self.combination_chart,
            'defaultMultiple': self.default_multiple,
            'defaultSingle': self.default_single,
            'emptyChart': self.empty_chart,
            'lineMultiple': self.line_multiple,
            'lineSingle': self.line_single,
            'mapTypeDescription': self.map_type_description,
            'pieMultiple': self.pie_multiple,
            'pieSingle': self.pie_single,
            'scatterMultiple': self.scatter_multiple,
            'scatterSingle': self.scatter_single,
            'splineMultiple': self.spline_multiple,
            'splineSingle': self.spline_single,
            'unknownMap': self.unknown_map
        }

        return untrimmed
