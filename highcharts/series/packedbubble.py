from typing import Optional, List

from highcharts.series.networkgraph import NetworkGraphSeries
from highcharts.series.data.single_point import SingleValueData
from highcharts.plot_options.packedbubble import PackedBubbleOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class PackedBubbleSeries(NetworkGraphSeries, PackedBubbleOptions):
    """Options to configure a Packed Bubble series.

    A packed bubble series is a two dimensional series type, where each point renders
    a value in X, Y position. Each point is drawn as a bubble where the bubbles don't
    overlap with each other and the radius of the bubble relates to the value.

    .. tabs::

      .. tab:: Standard Packed Bubble

        .. figure:: _static/packedbubble-example.png
          :alt: Split Packed Bubble Example Chart
          :align: center

      .. tab:: Split Packed Bubble

        .. figure:: _static/packedbubble-example-split.png
          :alt: Split Packed Bubble Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self.__mro_init__(kwargs)

    @property
    def data(self) -> Optional[List[SingleValueData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`SingleValueData` instances,
        it accepts as input either:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = PackedBubbleSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a :meth:`value <SingleValueData.value>`
            value.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`SingleValueData` objects.

        :rtype: :class:`list <python:list>` of :class:`SingleValueData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = SingleValueData.from_setter(value)

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

            'draggable': as_dict.pop('draggable', None),
            'layout_algorithm': as_dict.pop('layoutAlgorithm', None),
            'link': as_dict.pop('link', None),

            'display_negative': as_dict.pop('displayNegative', None),
            'max_size': as_dict.pop('maxSize', None),
            'min_size': as_dict.pop('minSize', None),
            'parent_node': as_dict.pop('parent_node', None),
            'size_by': as_dict.pop('sizeBy', None),
            'use_simulation': as_dict.pop('use_simulation', None),
            'z_threshold': as_dict.pop('zThreshold', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro_to_dict(self)

        return untrimmed
