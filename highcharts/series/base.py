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

        self.data = kwargs.pop('data', None)
        self.id = kwargs.pop('id', None)
        self.index = kwargs.pop('index', None)
        self.legend_index = kwargs.pop('legend_index', None)
        self.name = kwargs.pop('name', None)
        self.stack = kwargs.pop('stack', None)
        self.x_axis = kwargs.pop('x_axis', None)
        self.y_axis = kwargs.pop('y_axis', None)
        self.z_index = kwargs.pop('z_index', None)

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
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def to_dict(self) -> dict:
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
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
