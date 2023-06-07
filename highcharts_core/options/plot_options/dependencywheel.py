from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors, utility_functions
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.options.plot_options.generic import GenericTypeOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.options.plot_options.levels import LevelOptions


class DependencyWheelOptions(GenericTypeOptions):
    """General options to apply to all Dependency Wheel series types.

    A dependency wheel chart is a type of flow diagram, where all nodes are laid out
    in a circle, and the flow between the are drawn as link bands.

    .. figure:: ../../../_static/dependencywheel-example.png
      :alt: Dependency Wheel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._center = None
        self._center_in_category = None
        self._color_by_point = None
        self._color_index = None
        self._colors = None
        self._curve_factor = None
        self._levels = None
        self._link_opacity = None
        self._min_link_width = None
        self._node_padding = None
        self._node_width = None
        self._start_angle = None

        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.center = kwargs.get('center', None)
        self.center_in_category = kwargs.get('center_in_category', None)
        self.color_by_point = kwargs.get('color_by_point', None)
        self.color_index = kwargs.get('color_index', None)
        self.colors = kwargs.get('colors', None)
        self.curve_factor = kwargs.get('curve_factor', None)
        self.levels = kwargs.get('levels', None)
        self.link_opacity = kwargs.get('link_opacity', None)
        self.min_link_width = kwargs.get('min_link_width', None)
        self.node_padding = kwargs.get('node_padding', None)
        self.node_width = kwargs.get('node_width', None)
        self.start_angle = kwargs.get('start_angle', None)

        super().__init__(**kwargs)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each column or bar. Defaults to
        ``'#ffffff'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions
        self._border_color = utility_functions.validate_color(value)

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
    def center(self) -> Optional[List[str | int | float | Decimal | constants.EnforcedNullType]]:
        """The center of the wheel relative to the plot area. Expects a two-member array,
        indicating the x and y coordinates as percentages or pixel values. If
        :obj:`None <python:None>`, the default behaviour is to center the wheel inside the
        plot area.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of numeric or
          :class:`str <python:str>` values
        """
        return self._center

    @center.setter
    def center(self, value):
        if not value:
            self._center = None
        else:
            value = validators.iterable(value)
            if len(value) != 2:
                raise errors.HighchartsValueError(f'center expects a 2-member array. '
                                                  f'Received a {len(value)}-member '
                                                  f'array.')
            processed_values = []
            for item in value:
                try:
                    item = validators.string(item)
                    if '%' not in item:
                        raise errors.HighchartsValueError('center expects a 2-member '
                                                          'array of numbers or '
                                                          'percentage strings. No "%" '
                                                          'was found in the string.')
                except TypeError:
                    item = validators.numeric(value)

                processed_values.append(item)

            self._center = processed_values

    @property
    def center_in_category(self) -> Optional[bool]:
        """If ``True``, the columns will center in the category, ignoring null or missing
        points. When ``False``, space will be reserved for null or missing points.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._center_in_category

    @center_in_category.setter
    def center_in_category(self, value):
        if value is None:
            self._center_in_category = None
        else:
            self._center_in_category = bool(value)

    @property
    def color_by_point(self) -> Optional[bool]:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        if value is None:
            self._color_by_point = None
        else:
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
            self._colors = [utility_functions.validate_color(x) for x in value]

    @property
    def curve_factor(self) -> Optional[int | float | Decimal]:
        """The amount by which to curve the lines in a sankey diagram or dependency wheel.
        Higher numbers makes the links more curved, while a curveFactor of ``0`` makes the
        lines straight. Defaults to ``0.6``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._curve_factor

    @curve_factor.setter
    def curve_factor(self, value):
        self._curve_factor = validators.numeric(value, allow_empty = True)

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
    def node_padding(self) -> Optional[int | float | Decimal]:
        """The padding between nodes in a sankey diagram or dependency wheel, in pixels.
        Defaults to ``10``.

        .. note::

          If the number of nodes is so great that it is not possible to lay them out
          within the plot area with the given ``node_padding``, they will be rendered with
          a smaller padding as a strategy to avoid overflow.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._node_padding

    @node_padding.setter
    def node_padding(self, value):
        self._node_padding = validators.numeric(value,
                                                allow_empty = True)

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
    def start_angle(self) -> Optional[int | float | Decimal]:
        """The start angle of the dependency wheel, in degrees where ``0`` is up. Defaults
        to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._start_angle

    @start_angle.setter
    def start_angle(self, value):
        self._start_angle = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0,
                                               maximum = 360)

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
            'center': as_dict.get('center', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'color_index': as_dict.get('colorIndex', None),
            'colors': as_dict.get('colors', None),
            'curve_factor': as_dict.get('curveFactor', None),
            'levels': as_dict.get('levels', None),
            'link_opacity': as_dict.get('linkOpacity', None),
            'min_link_width': as_dict.get('minLinkWidth', None),
            'node_padding': as_dict.get('nodePadding', None),
            'node_width': as_dict.get('nodeWidth', None),
            'start_angle': as_dict.get('startAngle', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'center': self.center,
            'centerInCategory': self.center_in_category,
            'colorByPoint': self.color_by_point,
            'colorIndex': self.color_index,
            'colors': self.colors,
            'curveFactor': self.curve_factor,
            'levels': self.levels,
            'linkOpacity': self.link_opacity,
            'minLinkWidth': self.min_link_width,
            'nodePadding': self.node_padding,
            'nodeWidth': self.node_width,
            'startAngle': self.start_angle
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
