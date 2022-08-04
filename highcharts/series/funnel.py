from typing import Optional, List

from highcharts.series.pie import PieSeries
from highcharts.plot_options.funnel import FunnelOptions, Funnel3DOptions
from highcharts.series.data.single_point import SinglePointData
from highcharts.utility_functions import mro_init, mro_to_dict


class FunnelSeries(PieSeries, FunnelOptions):
    """Options to configure a Funnel series.

    Funnel charts are a type of chart often used to visualize stages in a sales
    project, where the top are the initial stages with the most clients.

    .. warning::

      Funnel charts require that the ``modules/funnel.js`` file is loaded client-side.

    .. figure:: _static/funnel-example.png
      :alt: Funnel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[List[SinglePointData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`SinglePointData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = PieSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a :meth:`y <SinglePointData.y>` value

          .. tab:: Object Collection

            A one-dimensional collection of :class:`SinglePointData` objects.

        :rtype: :class:`list <python:list>` of :class:`SinglePointData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = SinglePointData.from_setter(value)

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
            'linecap': as_dict.pop('linecap', None),
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

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center': as_dict.pop('center', None),
            'colors': as_dict.pop('colors', None),
            'depth': as_dict.pop('depth', 0),
            'end_angle': as_dict.pop('endAngle', None),
            'fill_color': as_dict.pop('fillColor', None),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', True),
            'inner_size': as_dict.pop('innerSize', 0),
            'min_size': as_dict.pop('minSize', 80),
            'size': as_dict.pop('size', None),
            'sliced_offset': as_dict.pop('slicedOffset', 10),
            'start_angle': as_dict.pop('startAngle', 0),

            'height': as_dict.pop('height', None),
            'neck_height': as_dict.pop('neckHeight', None),
            'neck_width': as_dict.pop('neckWidth', None),
            'reversed': as_dict.pop('reversed', None),
            'width': as_dict.pop('width', None)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)


class Funnel3DSeries(FunnelSeries, Funnel3DOptions):
    """Options to apply to a Variable Pie series.

    A variable pie series is a two dimensional series type, where each point renders
    an Y and Z value. Each point is drawn as a pie slice where the size (arc) of the
    slice relates to the Y value and the radius of pie slice relates to the Z value.

    .. figure:: _static/variablepie-example.png
      :alt: Variable Pie Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

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

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center': as_dict.pop('center', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'colors': as_dict.pop('colors', None),
            'depth': as_dict.pop('depth', 0),
            'end_angle': as_dict.pop('endAngle', None),
            'fill_color': as_dict.pop('fillColor', None),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', True),
            'inner_size': as_dict.pop('innerSize', 0),
            'linecap': as_dict.pop('linecap', 'round'),
            'min_size': as_dict.pop('minSize', 80),
            'size': as_dict.pop('size', None),
            'sliced_offset': as_dict.pop('slicedOffset', 10),
            'start_angle': as_dict.pop('startAngle', 0),

            'height': as_dict.pop('height', None),
            'neck_height': as_dict.pop('neckHeight', None),
            'neck_width': as_dict.pop('neckWidth', None),
            'reversed': as_dict.pop('reversed', None),
            'width': as_dict.pop('width', None),

            'max_point_size': as_dict.pop('maxPointSize', None),
            'min_point_size': as_dict.pop('minPointSize', None),
            'size_by': as_dict.pop('sizeBy', None),
            'z_max': as_dict.pop('zMax', None),
            'z_min': as_dict.pop('zMin', None),
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)
