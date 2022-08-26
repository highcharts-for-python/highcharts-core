from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.plot_options.networkgraph import NetworkGraphOptions


class ParentNodeOptions(HighchartsMeta):
    """Series options for parent nodes."""

    def __init__(self, **kwargs):
        self._allow_point_select = None

        self.allow_point_select = kwargs.pop('allow_point_select', None)

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
    def from_dict(cls, as_dict):
        return cls({
            'allow_point_select': as_dict.pop('allowPointSelect', None)
        })

    def _to_untrimmed_dict(self) -> dict:
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

        .. figure:: _static/packedbubble-example.png
          :alt: Split Packed Bubble Example Chart
          :align: center

      .. tab:: Split Packed Bubble

        .. figure:: _static/packedbubble-example-split.png
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

        self.display_negative = kwargs.pop('display_negative', None)
        self.max_size = kwargs.pop('max_size', None)
        self.min_size = kwargs.pop('min_size', None)
        self.parent_node = kwargs.pop('parent_node', None)
        self.size_by = kwargs.pop('size_by', None)
        self.use_simulation = kwargs.pop('use_simulation', None)
        self.z_threshold = kwargs.pop('z_threshold', None)

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
                    raise ValueError
            except ValueError:
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
                    raise ValueError
            except ValueError:
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

            'display_negative': as_dict.pop('displayNegative', None),
            'max_size': as_dict.pop('maxSize', None),
            'min_size': as_dict.pop('minSize', None),
            'parent_node': as_dict.pop('parentNode', None),
            'size_by': as_dict.pop('sizeBy', None),
            'use_simulation': as_dict.pop('useSimulation', None),
            'z_threshold': as_dict.pop('zThreshold', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'displayNegative': self.display_negative,
            'maxSize': self.max_size,
            'minSize': self.min_size,
            'parentNode': self.parent_node,
            'sizeBy': self.size_by,
            'useSimulation': self.use_simulation,
            'zThreshold': self.z_threshold
        }
        parent_as_dict = super()._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
