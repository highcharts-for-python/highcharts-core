from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.plot_options.generic import GenericTypeOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.plot_options.levels import LevelOptions


class ArcDiagramOptions(GenericTypeOptions):
    """Arc diagram series is a chart drawing style in which the vertices of the chart
    are positioned along a line on the Euclidean plane and the edges are drawn as a
    semicircle in one of the two half-planes delimited by the line, or as smooth
    curves formed by sequences of semicircles.

    .. figure:: _static/arcdiagram-example.png
      :alt: Arc Diagram Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._centered_links = False
        self._color_by_point = True
        self._color_index = None
        self._colors = None
        self._equal_nodes = False
        self._levels = None
        self._link_opacity = 0.5
        self._min_link_width = 0
        self._node_width = 20
        self._reversed = False
        self._sticky_tracking = True

        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.centered_links = kwargs.pop('centered_links', False)
        self.color_by_point = kwargs.pop('color_by_point', True)
        self.color_index = kwargs.pop('color_index', None)
        self.colors = kwargs.pop('colors', None)
        self.equal_nodes = kwargs.pop('equal_nodes', False)
        self.levels = kwargs.pop('levels', None)
        self.link_opacity = kwargs.pop('link_opacity', 0.5)
        self.min_link_width = kwargs.pop('min_link_width', 0)
        self.node_width = kwargs.pop('node_width', 20)
        self.reversed = kwargs.pop('reversed', False)
        self.sticky_tracking = kwargs.pop('sticky_tracking', None)

        super(self).__init__(**kwargs)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each column or bar. Defaults to
        ``'#ffffff'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding each column or bar. If
        :obj:`None <python:None>`, defaults to ``1`` when there is room for a border, but
        to ``0`` when the columns are so dense that a border would cover the next column.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def centered_links(self) -> bool:
        """The option to center links rather than position them one after another.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._centered_links

    @centered_links.setter
    def centered_links(self, value):
        self._centered_links = bool(value)

    @property
    def color_by_point(self) -> bool:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        self._color_by_point = bool(value)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def colors(self) -> Optional[List[str | Gradient | Pattern]]:
        """A series-specific or series type-specific color set to apply instead of the
        global colors when :meth:`ArcDiagramOptions.color_by_point` is ``True``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`,
          :class:`Gradient`, or :class:`Pattern` OR :obj:`None <python:None>`
        """
        return self._colors

    @colors.setter
    def colors(self, value):
        if not value:
            self._colors = None
        else:
            value = validators.iterable(value)
            checked_values = []
            for item in value:
                if isinstance(value, str):
                    checked_values.append(item)
                else:
                    processed_item = validate_types(item,
                                                    types = (Gradient, Pattern))
                    checked_values.append(processed_item)

            self._colors = checked_values

    @property
    def equal_nodes(self) -> bool:
        """Whether nodes with different values should have the same size. Defaults to
        ``False``.

        If ``True``, all nodes are calculated based on the ``nodePadding`` and current
        plot area. It is possible to override it using the :meth:`Marker.radius` setting.

        :rtype: :class:`bool <python:bool>`
        """
        return self._equal_nodes

    @equal_nodes.setter
    def equal_nodes(self, value):
        self._equal_nodes = bool(value)

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
    def min_link_width(self) -> Optional[int | float | Decimal]:
        """The minimal width for a line of a sankey or similar diagram. By default,
        ``0`` values are not shown. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_link_width

    @min_link_width.setter
    def min_link_width(self, value):
        self._min_link_width = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def node_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of each node in a sankey diagram or dependency wheel, or the
        height in case the chart is inverted. Defaults to ``20``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._node_width

    @node_width.setter
    def node_width(self, value):
        self._node_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def reversed(self) -> bool:
        """If ``True``, places the series on the other side of the plot area. Defaults to
        ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._reversed

    @reversed.setter
    def reversed(self, value):
        self._reversed = bool(value)

    @property
    def sticky_tracking(self) -> Optional[bool]:
        """Enable (``True``) or disable (``False``) :term:`sticky tracking` of mouse
        events. Defaults to :obj:`None <python:None>`.

        When ``True``, the mouse out event on a series isn't triggered until the mouse
        moves over another series, or out of the plot area.

        When ``False``, the mouse out event on a series is triggered when the mouse leaves
        the area around the series' graph or markers. This also implies the tooltip when
        not shared.

        When ``sticky_tracking`` is ``False`` and `:meth:Tooltip.shared` is ``False``, the
        tooltip will be hidden when moving the mouse between series.

        If :obj:`None <python:None>`, will defaults to ``True`` for line and area type
        series, but ``False`` for columns, pies, etc.

        .. note::

          The boost module will force this option because of technical limitations.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._sticky_tracking

    @sticky_tracking.setter
    def sticky_tracking(self, value):
        if value is None:
            self._sticky_tracking = None
        else:
            self._sticky_tracking = bool(value)

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
            'centered_links': as_dict.pop('centeredLinks', False),
            'color_by_point': as_dict.pop('colorByPoint', True),
            'color_index': as_dict.pop('colorIndex', None),
            'colors': as_dict.pop('colors', None),
            'equal_nodes': as_dict.pop('equalNodes', False),
            'levels': as_dict.pop('levels', None),
            'link_opacity': as_dict.pop('linkOpacity', 0.5),
            'min_link_width': as_dict.pop('minLinkWidth', 0),
            'node_width': as_dict.pop('nodeWidth', 20),
            'reversed': as_dict.pop('reversed', False),
            'sticky_tracking': as_dict.pop('stickyTracking', None)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'centeredLinks': self.centered_links,
            'colorByPoint': self.color_by_point,
            'colorIndex': self.color_index,
            'colors': self.colors,
            'equalNodes': self.equal_nodes,
            'levels': self.levels,
            'linkOpacity': self.link_opacity,
            'minLinkWidth': self.min_link_width,
            'nodeWidth': self.node_width,
            'reversed': self.reversed,
            'stickyTracking': self.sticky_tracking
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
