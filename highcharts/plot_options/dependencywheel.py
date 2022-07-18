from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.plot_options.generic import GenericTypeOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.plot_options.levels import LevelOptions


class DependencyWheelOptions(GenericTypeOptions):
    """General options to apply to all Dependency Wheel series types.

    A dependency wheel chart is a type of flow diagram, where all nodes are laid out
    in a circle, and the flow between the are drawn as link bands.

    .. figure:: _static/dependencywheel-example.png
      :alt: Dependency Wheel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._center = None
        self._center_in_category = False
        self._color_by_point = True
        self._color_index = None
        self._colors = None
        self._curve_factor = None
        self._levels = None
        self._link_opacity = 0.5
        self._min_link_width = 0
        self._node_padding = 10
        self._node_width = 20
        self._start_angle = 0

        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.center = kwargs.pop('center', [constants.EnforcedNull,
                                            constants.EnforcedNull])
        self.center_in_category = kwargs.pop('center_in_category', False)
        self.color_by_point = kwargs.pop('color_by_point', True)
        self.color_index = kwargs.pop('color_index', None)
        self.colors = kwargs.pop('colors', None)
        self.curve_factor = kwargs.pop('curve_factor', 0.6)
        self.levels = kwargs.pop('levels', None)
        self.link_opacity = kwargs.pop('link_opacity', 0.5)
        self.min_link_width = kwargs.pop('min_link_width', 0)
        self.node_padding = kwargs.pop('node_padding', 10)
        self.node_width = kwargs.pop('node_width', 20)
        self.start_angle = kwargs.pop('start_angle', 0)

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
                                                  f'Received a {len(value)}-member array.')
            processed_values = []
            for item in value:
                try:
                    item = validators.string(value)
                    if '%' not in item:
                        raise ValueError
                except ValueError:
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
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', True),
            'color_index': as_dict.pop('colorIndex', None),
            'colors': as_dict.pop('colors', None),
            'curve_factor': as_dict.pop('curveFactor', 0.6),
            'levels': as_dict.pop('levels', None),
            'link_opacity': as_dict.pop('linkOpacity', 0.5),
            'min_link_width': as_dict.pop('minLinkWidth', 0),
            'node_padding': as_dict.pop('nodePadding', 10),
            'node_width': as_dict.pop('nodeWidth', 20),
            'start_angle': as_dict.pop('startAngle', 0)
        }

        return kwargs

    def to_dict(self) -> dict:
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
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
