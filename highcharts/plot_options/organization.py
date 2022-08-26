from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.plot_options.bar import BarOptions
from highcharts.plot_options.levels import LevelOptions


class OrganizationOptions(BarOptions):
    """General options to apply to all Organization series types.

    An organization chart is a diagram that shows the structure of an organization and
    the relationships and relative ranks of its parts and positions.

    .. tabs::

      .. tab:: Standard Organization Chart

        .. figure:: _static/organization-example.png
          :alt: Organization Example Chart
          :align: center

      .. tab:: Horizontal Organization Chart

        .. figure:: _static/organization-example-horizontal.png
          :alt: Horizontal Organization Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._hanging_indent = None
        self._hanging_indent_translation = None
        self._levels = None
        self._link_color = None
        self._link_line_width = None
        self._link_opacity = None
        self._link_radius = None
        self._min_link_width = None
        self._min_node_length = None
        self._node_padding = None
        self._node_width = None

        self.hanging_indent = kwargs.pop('hanging_indent', None)
        self.hanging_indent_translation = kwargs.pop('hanging_indent_translation', None)
        self.levels = kwargs.pop('levels', None)
        self.link_color = kwargs.pop('link_color', None)
        self.link_line_width = kwargs.pop('link_line_width', None)
        self.link_opacity = kwargs.pop('link_opacity', None)
        self.link_radius = kwargs.pop('link_radius', None)
        self.min_link_width = kwargs.pop('min_link_width', None)
        self.min_node_length = kwargs.pop('min_node_length', None)
        self.node_padding = kwargs.pop('node_padding', None)
        self.node_width = kwargs.pop('node_width', None)

        super().__init__(**kwargs)

    @property
    def hanging_indent(self) -> Optional[int | float | Decimal]:
        """The indentation in pixels of :term:`hanging nodes` (nodes whose parent has
        ``layout`` set to ``'hanging'``). Defaults to ``20``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._hanging_indent

    @hanging_indent.setter
    def hanging_indent(self, value):
        self._hanging_indent = validators.numeric(value, allow_empty = True)

    @property
    def hanging_indent_translation(self) -> Optional[str]:
        """Defines the indentation of a ``'hanging'`` layout parent's children. Defaults
        to ``'inherit'``.

        Possible options are:

          * ``'inherit'`` - Only the first child adds the indentation, children of a child
            with indentation inherit the indentation
          * ``'cumulative'`` - All children of a child with indentation add its own
            indent. If this option causes overlapping of nodes, then use the ``'shrink'``
            setting.
          * ``'shrink'`` - Nodes shrink by the
            :meth:`hanging_indent <OrganizationOptions.hanging_indent>` value until they
            reach the :meth:`min_node_length <OrganizationOptions.min_node_length>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._hanging_indent_translation

    @hanging_indent_translation.setter
    def hanging_indent_translation(self, value):
        if not value:
            self._hanging_indent_translation = None
        else:
            value = validators.string(value, allow_empty = True)
            value = value.lower()
            if value not in ['inherit', 'cumulative', 'shrink']:
                raise errors.HighchartsValueError(f'hanging_indent_translation expects '
                                                  f'a value of "inherit", "cumulative", '
                                                  f'"shrink", or None. Received: {value}')

            self._hanging_indent_translation = value

    @property
    def levels(self) -> Optional[List[LevelOptions]]:
        """Set options on specific levels. Takes precedence over series options, but not
        node and link options.

        :rtype: :obj:`None <python:None>`, or :class:`list <python:list>` of
          :class:`LevelOptions`
        """
        return self._levels

    @levels.setter
    @class_sensitive(LevelOptions, force_iterable = True)
    def levels(self, value):
        self._levels = value

    @property
    def link_color(self) -> Optional[str]:
        """The color of the links between nodes. Defaults to ``'#666666'.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._link_color

    @link_color.setter
    def link_color(self, value):
        self._link_color = validators.string(value, allow_empty = True)

    @property
    def link_line_width(self) -> Optional[int | float | Decimal]:
        """The line width of the links connecting nodes, in pixels. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._link_line_width

    @link_line_width.setter
    def link_line_width(self, value):
        self._link_line_width = validators.numeric(value, allow_empty = True)

    @property
    def link_opacity(self) -> Optional[int | float | Decimal]:
        """Opacity for the links between nodes in sankey or similar diagrams. Defaults to
        ``0.5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._link_opacity

    @link_opacity.setter
    def link_opacity(self, value):
        self._link_opacity = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def link_radius(self) -> Optional[int | float | Decimal]:
        """Radius for the rounded corners of the links between nodes. Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._link_radius

    @link_radius.setter
    def link_radius(self, value):
        self._link_radius = validators.numeric(value, allow_empty = True)

    @property
    def min_link_width(self) -> Optional[int | float | Decimal]:
        """The minimal width for a line of a sankey. By default, 0 values are not shown.
        Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_link_width

    @min_link_width.setter
    def min_link_width(self, value):
        self._min_link_width = validators.numeric(value, allow_empty = True)

    @property
    def min_node_length(self) -> Optional[int | float | Decimal]:
        """In a horizontal chart, the minimum width of the hanging nodes only, expressed
        in pixels. In a vertical chart, the minimum height of the hanging nodes only,
        expressed in pixels. Defaults to ``10``.

        .. warning::

          Only applied when
          :meth:`hanging_indent_translation <OrganizationOptions.hanging_indent_translation>`
          is set to ``'shrink'``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_node_length

    @min_node_length.setter
    def min_node_length(self, value):
        self._min_node_length = validators.numeric(value, allow_empty = True)

    @property
    def node_padding(self) -> Optional[int | float | Decimal]:
        """The padding between nodes in a sankey diagram or dependency wheel, in pixels.
        Defaults to ``10``.

        If the number of nodes is so great that it is possible to lay them out within the
        plot area with the given ``node_padding``, they will be rendered with a smaller
        padding as a strategy to avoid overflow.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._node_padding

    @node_padding.setter
    def node_padding(self, value):
        self._node_padding = validators.numeric(value, allow_empty = True)

    @property
    def node_width(self) -> Optional[int | float | Decimal]:
        """In a horizontal chart, the width of the nodes in pixels. Defaults to ``50``.

        .. note::

          Most organization charts are vertical, so the name of this option is
          counterintuitive.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._node_width

    @node_width.setter
    def node_width(self, value):
        self._node_width = validators.numeric(value, allow_empty = True)

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
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'group_z_padding': as_dict.pop('groupZPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'hanging_indent': as_dict.pop('hangingIndent', None),
            'hanging_indent_translation': as_dict.pop('hangingIndentTranslation', None),
            'levels': as_dict.pop('levels', None),
            'link_color': as_dict.pop('linkColor', None),
            'link_line_width': as_dict.pop('linkLineWidth', None),
            'link_opacity': as_dict.pop('linkOpacity', None),
            'link_radius': as_dict.pop('linkRadius', None),
            'min_link_width': as_dict.pop('minLinkWidth', None),
            'min_node_length': as_dict.pop('minNodeLength', None),
            'node_padding': as_dict.pop('nodePadding', None),
            'node_width': as_dict.pop('nodeWidth', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'hangingIndent': self.hanging_indent,
            'hangingIndentTranslation': self.hanging_indent_translation,
            'levels': self.levels,
            'linkColor': self.link_color,
            'linkLineWidth': self.link_line_width,
            'linkOpacity': self.link_opacity,
            'linkRadius': self.link_radius,
            'minLinkWidth': self.min_link_width,
            'minNodeLength': self.min_node_length,
            'nodePadding': self.node_padding,
            'nodeWidth': self.node_width
        }
        parent_as_dict = super()._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
