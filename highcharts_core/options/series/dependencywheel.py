from typing import Optional, List

from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.base import SeriesBase
from highcharts_core.options.series.data.connections import WeightedConnectionData
from highcharts_core.options.plot_options.dependencywheel import DependencyWheelOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict
from highcharts_core.utility_classes.nodes import DependencyWheelNodeOptions


class DependencyWheelSeries(SeriesBase, DependencyWheelOptions):
    """Options to configure a Dependency Wheel series.

    A dependency wheel chart is a type of flow diagram, where all nodes are laid out
    in a circle, and the flow between the are drawn as link bands.

    .. figure:: ../../../_static/dependencywheel-example.png
      :alt: Dependency Wheel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._nodes = None

        self.nodes = kwargs.get('nodes', None)

        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[WeightedConnectionData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`WeightedConnectionData`
        instances, it accepts as input:

        .. tabs::

          .. tab:: Object Collection

            A one-dimensional collection of :class:`WeightedConnectionData` objects or
            :class:`dict <python:dict>` that are coercable to
            :class:`WeightedConnectionData` instances.

        :rtype: :class:`list <python:list>` of :class:`WeightedConnectionData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = WeightedConnectionData.from_array(value)

    @property
    def nodes(self) -> Optional[List[DependencyWheelNodeOptions]]:
        """Collection of nodes for a Dependency Wheel that are associated with a
        specific :class:`DependencyWheelSeries` by the :meth:`DependencyWheelSeries.id`.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`DependencyWheelNodeOptions` or
          :obj:`None <python:None>`
        """
        return self._nodes

    @nodes.setter
    @class_sensitive(DependencyWheelNodeOptions, force_iterable = True)
    def nodes(self, value):
        self._nodes = value

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
            'legend_symbol': as_dict.get('legendSymbol', None),
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
            'sonification': as_dict.get('sonification', None),
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
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
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

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'center': as_dict.get('center', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'curve_factor': as_dict.get('curveFactor', None),
            'levels': as_dict.get('levels', None),
            'link_opacity': as_dict.get('linkOpacity', None),
            'min_link_width': as_dict.get('minLinkWidth', None),
            'node_padding': as_dict.get('nodePadding', None),
            'node_width': as_dict.get('nodeWidth', None),
            'start_angle': as_dict.get('startAngle', None),

            'nodes': as_dict.get('nodes', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        untrimmed['nodes'] = self.nodes

        return untrimmed
