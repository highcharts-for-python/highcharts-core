from typing import Optional, List

from highcharts.series.base import SeriesBase
from highcharts.series.data.pie import PieData, VariablePieData
from highcharts.plot_options.pie import PieOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class PieSeries(SeriesBase, PieOptions):
    """Options to configure a Pie series.

    A pie chart is a circular graphic which is divided into slices to illustrate
    numerical proportion.

    .. tabs::

      .. tab:: Pie Chart

        .. figure:: _static/pie-example.png
          :alt: Pie Example Chart
          :align: center

      .. tab:: Donut Chart

        .. figure:: _static/pie-example-donut.png
          :alt: Donut Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self.__mro_init__(kwargs)

    @property
    def data(self) -> Optional[List[PieData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`PieData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = PieSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a :meth:`y <PieData.y>` value

          .. tab:: Object Collection

            A one-dimensional collection of :class:`PieData` objects.

        :rtype: :class:`list <python:list>` of :class:`PieData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = PieData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
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
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
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

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center': as_dict.pop('center', None),
            'colors': as_dict.pop('colors', None),
            'depth': as_dict.pop('depth', None),
            'end_angle': as_dict.pop('endAngle', None),
            'fill_color': as_dict.pop('fillColor', None),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', None),
            'inner_size': as_dict.pop('innerSize', None),
            'min_size': as_dict.pop('minSize', None),
            'size': as_dict.pop('size', None),
            'sliced_offset': as_dict.pop('slicedOffset', None),
            'start_angle': as_dict.pop('startAngle', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = mro_to_dict(self)

        return untrimmed


class VariablePieSeries(PieSeries):
    """Options to apply to a Variable Pie series.

    A variable pie series is a two dimensional series type, where each point renders
    an Y and Z value. Each point is drawn as a pie slice where the size (arc) of the
    slice relates to the Y value and the radius of pie slice relates to the Z value.

    .. figure:: _static/variablepie-example.png
      :alt: Variable Pie Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._max_point_size = None
        self._min_point_size = None
        self._size_by = None
        self._z_max = None
        self._z_min = None

        self.max_point_size = kwargs.pop('max_point_size', None)
        self.min_point_size = kwargs.pop('min_point_size', None)
        self.size_by = kwargs.pop('size_by', None)
        self.z_max = kwargs.pop('z_max', None)
        self.z_min = kwargs.pop('z_min', None)

        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[VariablePieData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`VariablePieData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 2D Collection

            .. code-block::

              series = VariablePieSeries()
              series.data = [
                  [40, 75],
                  [50, 50],
                  [60, 40]
              ]

            A two-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a :meth:`y <VariablePieData.y>` and
            :meth:`z <VariablePieData.z>` respectively.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`VariablePieData` objects.

        :rtype: :class:`list <python:list>` of :class:`VariablePieData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = VariablePieData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
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
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center': as_dict.pop('center', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'colors': as_dict.pop('colors', None),
            'depth': as_dict.pop('depth', None),
            'end_angle': as_dict.pop('endAngle', None),
            'fill_color': as_dict.pop('fillColor', None),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', None),
            'inner_size': as_dict.pop('innerSize', None),
            'linecap': as_dict.pop('linecap', None),
            'min_size': as_dict.pop('minSize', None),
            'size': as_dict.pop('size', None),
            'sliced_offset': as_dict.pop('slicedOffset', None),
            'start_angle': as_dict.pop('startAngle', None),

            'max_point_size': as_dict.pop('maxPointSize', None),
            'min_point_size': as_dict.pop('minPointSize', None),
            'size_by': as_dict.pop('sizeBy', None),
            'z_max': as_dict.pop('zMax', None),
            'z_min': as_dict.pop('zMin', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'max_point_size': self.max_point_size,
            'min_point_size': self.min_point_size,
            'size_by': self.size_by,
            'z_max': self.z_max,
            'z_min': self.z_min
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
