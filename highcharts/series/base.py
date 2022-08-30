from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts.decorators import class_sensitive
from highcharts.plot_options.series import SeriesOptions
from highcharts.series.data.base import DataBase


class SeriesBase(SeriesOptions):
    """Generic base class for specific series configurations."""

    def __init__(self, **kwargs):
        self._data = None
        self._id = None
        self._index = None
        self._legend_index = None
        self._name = None
        self._stack = None
        self._x_axis = None
        self._y_axis = None
        self._z_index = None

        self.data = kwargs.get('data', None)
        self.id = kwargs.get('id', None)
        self.index = kwargs.get('index', None)
        self.legend_index = kwargs.get('legend_index', None)
        self.name = kwargs.get('name', None)
        self.stack = kwargs.get('stack', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def data(self) -> Optional[List[DataBase]]:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`DataBase` or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    @class_sensitive(DataBase, force_iterable = True)
    def data(self, value):
        self._data = value

    @property
    def id(self) -> Optional[str]:
        """An id for the series. Defaults to :obj:`None <python:None>`.

        .. hint::

          This can be used (in JavaScript) after render time to get a pointer to the
          series object through ``chart.get()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def index(self) -> Optional[int]:
        """The index for the series in the chart, affecting the internal index in the
        (JavaScript) ``chart.series`` array, the visible Z-index, and the order of the
        series in the legend. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._index

    @index.setter
    def index(self, value):
        self._index = validators.integer(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def legend_index(self) -> Optional[int]:
        """The sequential index for the series in the legend. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._legend_index

    @legend_index.setter
    def legend_index(self, value):
        self._legend_index = validators.integer(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def name(self) -> Optional[str]:
        """The name of the series as shown in the legend, tooltip, etc. Defaults to
        :obj:`None <python:None>.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        `"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def stack(self) -> Optional[str]:
        """Indicates the "stack" into which the series should be grouped, if the chart
        groups series into stacks. Defaults to :obj:`None <python:None>`.

        .. note::

          The value can be a string or a numeric value, provided that series in the same
          stack all have the same value when converted to a string. For ease of ues,
          Highcharts for Python will attempt to force the conversion of the relevant value
          to a string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stack

    @stack.setter
    def stack(self, value):
        if not value:
            self._stack = None
        else:
            self._stack = validators.string(value,
                                            coerce_value = True)

    @property
    def x_axis(self) -> Optional[str | int]:
        """When using multiple X-axes, this setting determines on which axis the series
        should be drawn. Its value should be either a numerical index position in the
        :meth:`Options.x_axis` array (starting at 0), or a :class:`str <python:str>`
        indicating the :meth:`id <XAxis.id>` of the axis to which the series should be
        connected. Defaults to :obj:`None <python:None>`, which behaves as if the value
        were set to ``0``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if value is None:
            self._x_axis = None
        else:
            try:
                value = validators.integer(value, minimum = 0)
            except ValueError:
                value = validators.string(value)

            self._x_axis = value

    @property
    def y_axis(self) -> Optional[str | int]:
        """When using multiple Y-axes, this setting determines on which axis the series
        should be drawn. Its value should be either a numerical index position in the
        :meth:`Options.y_axis` array (starting at 0), or a :class:`str <python:str>`
        indicating the :meth:`id <YAxis.id>` of the axis to which the series should be
        connected. Defaults to :obj:`None <python:None>`, which behaves as if the value
        were set to ``0``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if value is None:
            self._y_axis = None
        else:
            try:
                value = validators.integer(value, minimum = 0)
            except ValueError:
                value = validators.string(value)

            self._y_axis = value

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The visual z-index of the series. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        if value is None:
            self._z_index = None
        else:
            self._z_index = validators.numeric(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.get('getExtremesForAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'data': self.data,
            'id': self.id,
            'index': self.index,
            'legendIndex': self.legend_index,
            'name': self.name,
            'stack': self.stack,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
            'zIndex': self.z_index,
        }
        parent_as_dict = super()._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
