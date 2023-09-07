from typing import Optional, List

from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.bar import BarSeries
from highcharts_core.options.series.data.connections import (OutgoingWeightedConnectionData,
                                                             OutgoingWeightedConnectionDataCollection)
from highcharts_core.options.plot_options.organization import OrganizationOptions
from highcharts_core.utility_classes.nodes import OrganizationNodeOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict, is_ndarray


class OrganizationSeries(BarSeries, OrganizationOptions):
    """Options to configure an Organization series.

    An organization chart is a diagram that shows the structure of an organization and
    the relationships and relative ranks of its parts and positions.

    .. tabs::

      .. tab:: Standard Organization Chart

        .. figure:: ../../../_static/organization-example.png
          :alt: Organization Example Chart
          :align: center

      .. tab:: Horizontal Organization Chart

        .. figure:: ../../../_static/organization-example-horizontal.png
          :alt: Horizontal Organization Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._nodes = None

        self.nodes = kwargs.get('nodes', None)

        super().__init__(**kwargs)

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return OutgoingWeightedConnectionDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return OutgoingWeightedConnectionData

    @property
    def data(self) -> Optional[List[OutgoingWeightedConnectionData] | OutgoingWeightedConnectionDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`OrganizationData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = BarSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`BarSeries.point_start` is :obj:`None <python:None>`, ``x`` values
            will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`BarSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              series = BarSeries()
              # Category X-axis
              series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              series.data = [
                  [9, 0],
                  [1, 5],
                  [2, 3],
                  [7, 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``x`` and ``y`` pair. The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`OutgoingWeightedConnectionData` 
            objects.

        :rtype: :class:`list <python:list>` of :class:`OutgoingWeightedConnectionData` or
          :class:`OutgoingWeightedConnectionData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = OutgoingWeightedConnectionData.from_array(value)

    @property
    def nodes(self) -> Optional[List[OrganizationNodeOptions]]:
        """Collection of nodes for an Organization Chart that are associated with a
        specific :class:`OrganizationSeries` by the :meth:`OrganizationSeries.id`.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`OrganizationNodeOptions` or
          :obj:`None <python:None>`
        """
        return self._nodes

    @nodes.setter
    @class_sensitive(OrganizationNodeOptions, force_iterable = True)
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
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'track_by_area': as_dict.get('trackByArea', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'grouping': as_dict.get('grouping', None),
            'group_padding': as_dict.get('groupPadding', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'point_padding': as_dict.get('pointPadding', None),
            'point_range': as_dict.get('pointRange', None),
            'point_width': as_dict.get('pointWidth', None),

            'depth': as_dict.get('depth', None),
            'edge_color': as_dict.get('edgeColor', None),
            'edge_width': as_dict.get('edgeWidth', None),
            'group_z_padding': as_dict.get('groupZPadding', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'hanging_indent': as_dict.get('hangingIndent', None),
            'hanging_indent_translation': as_dict.get('hangingIndentTranslation', None),
            'levels': as_dict.get('levels', None),
            'link_color': as_dict.get('linkColor', None),
            'link_line_width': as_dict.get('linkLineWidth', None),
            'link_opacity': as_dict.get('linkOpacity', None),
            'link_radius': as_dict.get('linkRadius', None),
            'min_link_width': as_dict.get('minLinkWidth', None),
            'min_node_length': as_dict.get('minNodeLength', None),
            'node_padding': as_dict.get('nodePadding', None),
            'node_width': as_dict.get('nodeWidth', None),

            'nodes': as_dict.get('nodes', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'data': self.data,
            'nodes': self.nodes
        }

        parents_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}
        for key in parents_as_dict:
            untrimmed[key] = parents_as_dict[key]

        return untrimmed
