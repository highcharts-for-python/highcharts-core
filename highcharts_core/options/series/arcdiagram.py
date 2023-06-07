from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.base import SeriesBase
from highcharts_core.options.series.data.arcdiagram import ArcDiagramData
from highcharts_core.options.plot_options.arcdiagram import ArcDiagramOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict
from highcharts_core.utility_classes.nodes import NodeOptions


class ArcDiagramSeries(SeriesBase, ArcDiagramOptions):
    """Arc diagram series is a chart drawing style in which the vertices of the chart
    are positioned along a line on the Euclidean plane and the edges are drawn as a
    semicircle in one of the two half-planes delimited by the line, or as smooth
    curves formed by sequences of semicircles.

    .. figure:: ../../../_static/arcdiagram-example.png
      :alt: Arc Diagram Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._link_weight = None
        self._nodes = None
        self._offset = None

        self.link_weight = kwargs.get('link_weight', None)
        self.nodes = kwargs.get('nodes', None)
        self.offset = kwargs.get('offset', None)

        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[ArcDiagramData]]:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`ArcDiagramData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    @class_sensitive(ArcDiagramData, force_iterable = True)
    def data(self, value):
        self._data = value

    @property
    def link_weight(self) -> Optional[int | float | Decimal]:
        """The global link weight. Defaults to :obj:`None <python:None>`.

        If :obj:`None <python:None>`, width is calculated per link, depending on the
        weight value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._link_weight

    @link_weight.setter
    def link_weight(self, value):
        if value is None:
            self._link_weight = None
        else:
            self._link_weight = validators.numeric(value,
                                                   minimum = 0)

    @property
    def nodes(self) -> Optional[List[NodeOptions]]:
        """A collection of options for configuring individual nodes. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`NodeOptions` or
          :obj:`None <python:None>`
        """
        return self._nodes

    @nodes.setter
    @class_sensitive(NodeOptions, force_iterable = True)
    def nodes(self, value):
        self._nodes = value

    @property
    def offset(self) -> Optional[str]:
        """The offset of an arc diagram nodes column in relation to the plot area,
        expressed as a percentage of the plot area. If :obj:`None <python:None>`, the
        series is placed so that the biggest node is touching the bottom border of the
        plot area (equivalent to ``'100%'``). Defaults to :obj:`None <python:None>`.

        .. hint::

          For example, setting the offset to ``'50%'`` will place the nodes in the center
          of the chart.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._offset

    @offset.setter
    def offset(self, value):
        if not value:
            self._offset = None
        else:
            value = validators.string(value)
            value = value.lower()
            if '%' not in value:
                raise errors.HighchartsValueError(f'offset expects a percentage string. '
                                                  f'No "%" character found in: {value}')
            self._offset = value

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

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'centered_links': as_dict.get('centeredLinks', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'color_index': as_dict.get('colorIndex', None),
            'colors': as_dict.get('colors', None),
            'equal_nodes': as_dict.get('equalNodes', None),
            'levels': as_dict.get('levels', None),
            'link_opacity': as_dict.get('linkOpacity', None),
            'min_link_width': as_dict.get('minLinkWidth', None),
            'node_width': as_dict.get('nodeWidth', None),
            'reversed': as_dict.get('reversed', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'link_weight': as_dict.get('linkWeight', None),
            'nodes': as_dict.get('nodes', None),
            'offset': as_dict.get('offset', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'data': self.data,
            'linkWeight': self.link_weight,
            'nodes': self.nodes,
            'offset': self.offset
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
