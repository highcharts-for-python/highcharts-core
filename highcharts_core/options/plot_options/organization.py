from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.options.plot_options.bar import BarOptions
from highcharts_core.options.plot_options.levels import LevelOptions
from highcharts_core.utility_classes.data_labels import OrganizationDataLabel


class OrganizationOptions(BarOptions):
    """General options to apply to all Organization series types.

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

        self.hanging_indent = kwargs.get('hanging_indent', None)
        self.hanging_indent_translation = kwargs.get('hanging_indent_translation', None)
        self.levels = kwargs.get('levels', None)
        self.link_color = kwargs.get('link_color', None)
        self.link_line_width = kwargs.get('link_line_width', None)
        self.link_opacity = kwargs.get('link_opacity', None)
        self.link_radius = kwargs.get('link_radius', None)
        self.min_link_width = kwargs.get('min_link_width', None)
        self.min_node_length = kwargs.get('min_node_length', None)
        self.node_padding = kwargs.get('node_padding', None)
        self.node_width = kwargs.get('node_width', None)

        super().__init__(**kwargs)

    @property
    def data_labels(self) -> Optional[OrganizationDataLabel | List[OrganizationDataLabel]]:
        """Options for the series data labels, appearing next to each data point.

        .. note::

          To have multiple data labels per data point, you can also supply a collection of
          :class:`DataLabel` configuration settings.

        :rtype: :class:`OrganizationDataLabel <highcharts_core.utility_classes.data_labels.OrganizationDataLabel>`, 
          :class:`list <python:list>` of 
            :class:`OrganizationDataLabel <highcharts_core.utility_classes.data_labels.OrganizationDataLabel>` or
            :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    def data_labels(self, value):
        if not value:
            self._data_labels = None
        else:
            if checkers.is_iterable(value):
                self._data_labels = validate_types(value,
                                                   types = OrganizationDataLabel,
                                                   allow_none = False,
                                                   force_iterable = True)
            else:
                self._data_labels = validate_types(value,
                                                   types = OrganizationDataLabel,
                                                   allow_none = False)

    @property
    def hanging_indent(self) -> Optional[int | float | Decimal]:
        """The indentation in pixels of hanging nodes (nodes whose parent has
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
        """The color of the links between nodes. Defaults to ``'#666666'``.

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
            'node_width': as_dict.get('nodeWidth', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
