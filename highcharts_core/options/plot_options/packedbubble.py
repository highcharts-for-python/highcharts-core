from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.plot_options.networkgraph import NetworkGraphOptions


class ParentNodeOptions(HighchartsMeta):
    """Series options for parent nodes."""

    def __init__(self, **kwargs):
        self._allow_point_select = None

        self.allow_point_select = kwargs.get('allow_point_select', None)

    @property
    def allow_point_select(self) -> Optional[bool]:
        """Allow this series' parent nodes to be selected by clicking on the graph.
        Defaults to ``False``.

        :rtype: :class:`bool <python:None>` or :obj:`None <python:None>`
        """
        return self._allow_point_select

    @allow_point_select.setter
    def allow_point_select(self, value):
        if value is None:
            self._allow_point_select = None
        else:
            self._allow_point_select = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return {
            'allow_point_select': as_dict.get('allowPointSelect', None)
        }

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'allowPointSelect': self.allow_point_select
        }


class PackedBubbleOptions(NetworkGraphOptions):
    """General options to apply to all Packed Bubble series types.

    A packed bubble series is a two dimensional series type, where each point renders
    a value in X, Y position. Each point is drawn as a bubble where the bubbles don't
    overlap with each other and the radius of the bubble relates to the value.

    .. tabs::

      .. tab:: Standard Packed Bubble

        .. figure:: ../../../_static/packedbubble-example.png
          :alt: Split Packed Bubble Example Chart
          :align: center

      .. tab:: Split Packed Bubble

        .. figure:: ../../../_static/packedbubble-example-split.png
          :alt: Split Packed Bubble Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._display_negative = None
        self._max_size = None
        self._min_size = None
        self._parent_node = None
        self._size_by = None
        self._use_simulation = None
        self._z_threshold = None

        self.display_negative = kwargs.get('display_negative', None)
        self.max_size = kwargs.get('max_size', None)
        self.min_size = kwargs.get('min_size', None)
        self.parent_node = kwargs.get('parent_node', None)
        self.size_by = kwargs.get('size_by', None)
        self.use_simulation = kwargs.get('use_simulation', None)
        self.z_threshold = kwargs.get('z_threshold', None)

        super().__init__(**kwargs)

    @property
    def display_negative(self) -> Optional[bool]:
        """If ``True``, display negative sized bubbles.

        The threshold is given by the :meth:`z_threshold <BubbleOptions.z_threshold>`
        setting, and negative bubbles can be visualized by setting
        :meth:`negative_color <BubbleOptions.negative_color>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._display_negative

    @display_negative.setter
    def display_negative(self, value):
        if value is None:
            self._display_negative = None
        else:
            self._display_negative = bool(value)

    @property
    def max_size(self) -> Optional[str | int | float | Decimal]:
        """Maximum bubble size. Defaults to ``'20%'``.

        If :obj:`None <python:None>`, bubbles will automatically size between the
        :meth:`min_size <BubbleOptions.min_size>` and ``max_size``, to reflect the z value
        of each bubble. Can be either pixels (when no unit is given), or a percentage of
        the smallest one of the plot width and height.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if value is None:
            self._max_size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('max_size expects either a number '
                                                      'or a % string. No "%" found.')
            except TypeError:
                self._max_size = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def min_size(self) -> Optional[str | int | float | Decimal]:
        """Minimum bubble size. Defaults to ``8``.

        If :obj:`None <python:None>`, bubbles will automatically size between the
        :meth:`max_size <BubbleOptions.max_size>` and ``min_size``, to reflect the z value
        of each bubble. Can be either pixels (when no unit is given), or a percentage of
        the smallest one of the plot width and height.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value):
        if value is None:
            self._min_size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('min_size expects either a number '
                                                      'or a % string. No "%" found.')
            except TypeError:
                self._min_size = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def parent_node(self) -> Optional[ParentNodeOptions]:
        """Series options for parent nodes.

        :rtype: :class:`ParentNodeOptions` or :obj:`None <python:None>`
        """
        return self._parent_node

    @parent_node.setter
    @class_sensitive(ParentNodeOptions)
    def parent_node(self, value):
        self._parent_node = value

    @property
    def size_by(self) -> Optional[str]:
        """Whether the bubble's value should be represented by the ``'area'`` or the
        ``'width'`` of the bubble. The default, ``'area'``, corresponds best to the human
        perception of the size of each bubble.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._size_by

    @size_by.setter
    def size_by(self, value):
        if not value:
            self._size_by = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['area', 'width']:
                raise errors.HighchartsValueError(f'size_by expects either "area", '
                                                  f'or "width". Received: {value}')
            self._size_by = value

    @property
    def use_simulation(self) -> Optional[bool]:
        """If ``True``, simulation is used to calculate bubble positions. Defaults to
        ``True``.

        Simulation also adds options to the series graph based on used layout. In case of
        big data sets, with any performance issues, it is possible to disable animation
        and pack bubble in a simple circular way.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_simulation

    @use_simulation.setter
    def use_simulation(self, value):
        if value is None:
            self._use_simulation = None
        else:
            self._use_simulation = bool(value)

    @property
    def z_threshold(self) -> Optional[int | float | Decimal]:
        """When :meth:`display_negative <BubbleOptions.display_negative>` is ``False``,
        then bubbles with a Z value lower than ``z_threshold`` are not rendered. When
        :meth:`display_negative <BubbleOptions.display_negative>` is ``True`` and
        :meth:`negative_color <BubbleOptions.negative_color>` is set, then points
        with a Z value lower than ``z_threshold`` are rendered with the negative coloring.

        Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_threshold

    @z_threshold.setter
    def z_threshold(self, value):
        self._z_threshold = validators.numeric(value, allow_empty = True)

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
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_color': as_dict.get('lineColor', None),
            'negative_color': as_dict.get('negativeColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'track_by_area': as_dict.get('trackByArea', None),
            'zone_axis': as_dict.get('zoneAxis', None),

            'color_index': as_dict.get('colorIndex', None),
            'crisp': as_dict.get('crisp', None),
            'draggable': as_dict.get('draggable', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'layout_algorithm': as_dict.get('layoutAlgorithm', None),
            'line_width': as_dict.get('lineWidth', None),
            'link': as_dict.get('link', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'zones': as_dict.get('zones', None),

            'display_negative': as_dict.get('displayNegative', None),
            'max_size': as_dict.get('maxSize', None),
            'min_size': as_dict.get('minSize', None),
            'parent_node': as_dict.get('parentNode', None),
            'size_by': as_dict.get('sizeBy', None),
            'use_simulation': as_dict.get('useSimulation', None),
            'z_threshold': as_dict.get('zThreshold', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'displayNegative': self.display_negative,
            'maxSize': self.max_size,
            'minSize': self.min_size,
            'parentNode': self.parent_node,
            'sizeBy': self.size_by,
            'useSimulation': self.use_simulation,
            'zThreshold': self.z_threshold
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
