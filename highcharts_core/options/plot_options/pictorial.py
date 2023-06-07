from decimal import Decimal
from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.options.plot_options.series import SeriesOptions


class PictorialOptions(SeriesOptions):
    """General options to apply to all Pictorial series types.

    A pictorial series uses vector images to represent the data, with the data's shape
    determined by the ``path`` parameter.

    .. figure:: ../../../_static/pictorial-example.png
      :alt: Pictorial Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._depth = None
        self._edge_color = None
        self._edge_width = None
        self._grouping = None
        self._group_padding = None
        self._group_z_padding = None
        self._max_point_width = None
        self._min_point_length = None
        self._point_range = None
        
        self.depth = kwargs.get('depth', None)
        self.edge_color = kwargs.get('edge_color', None)
        self.edge_width = kwargs.get('edge_width', None)
        self.grouping = kwargs.get('grouping', None)
        self.group_padding = kwargs.get('group_padding', None)
        self.group_z_padding = kwargs.get('group_z_padding', None)
        self.max_point_width = kwargs.get('max_point_width', None)
        self.min_point_length = kwargs.get('min_point_length', None)
        self.point_padding = kwargs.get('point_padding', None)
        self.point_range = kwargs.get('point_range', None)
        self.point_width = kwargs.get('point_width', None)

        super().__init__(**kwargs)

    @property
    def depth(self) -> Optional[int | float | Decimal]:
        """Depth of the columns in a 3D column chart. Defaults to ``25``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = validators.numeric(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def edge_color(self) -> Optional[str]:
        """The color of the edges when rendering 3D columns. Defaults to
        :obj:`None <python:None>`.

        Similar to :meth:`border_color <BarOptions.border_color>`, except it defaults to
        the same color as the column if set to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._edge_color

    @edge_color.setter
    def edge_color(self, value):
        self._edge_color = validators.string(value, allow_empty = True)

    @property
    def edge_width(self) -> Optional[int | float | Decimal]:
        """The width of the colored edges applied to a 3D column. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._edge_width

    @edge_width.setter
    def edge_width(self, value):
        self._edge_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def grouping(self) -> Optional[bool]:
        """If ``True``, groups non-stacked columns. If ``False``, renders them
        independent of each other. Non-grouped columns will be laid out individually and
        overlap each other.

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._grouping

    @grouping.setter
    def grouping(self, value):
        if value is None:
            self._grouping = None
        else:
            self._grouping = bool(value)

    @property
    def group_padding(self) -> Optional[int | float | Decimal]:
        """Padding between each value group, in x axis units. Defaults to ``0.2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_padding

    @group_padding.setter
    def group_padding(self, value):
        self._group_padding = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def group_z_padding(self) -> Optional[int | float | Decimal]:
        """Spacing between columns along the Z axis in a 3D chart. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_z_padding

    @group_z_padding.setter
    def group_z_padding(self, value):
        self._group_z_padding = validators.numeric(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def max_point_width(self) -> Optional[int | float | Decimal]:
        """The maximum allowed pixel width for a column. This prevents the image from 
        becoming too wide when there is a small number of points in the chart. Defaults 
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_point_width

    @max_point_width.setter
    def max_point_width(self, value):
        self._max_point_width = validators.numeric(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def min_point_length(self) -> Optional[int | float | Decimal]:
        """The minimal height for a column or width for a data point. Defaults to 
        :obj:`None <python:None>`.

        By default, ``0`` values are not shown. To visualize a ``0`` (or close to zero)
        point, set the minimal point length to a pixel value like ``3``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_point_length

    @min_point_length.setter
    def min_point_length(self, value):
        self._min_point_length = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def point_padding(self) -> Optional[int | float | Decimal]:
        """Padding between each column or bar, in x axis units. Defaults to ``0.1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_padding

    @point_padding.setter
    def point_padding(self, value):
        self._point_padding = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def point_range(self) -> Optional[constants.EnforcedNullType | int | float | Decimal]:
        """The X axis range that each point is valid for, which determines the width of
        the column. Defaults to ``EnforcedNull``, which computes the range automatically.

        On a categorized axis, the range will be ``1`` by default (one category unit). On
        linear and datetime axes, the range will be computed as the distance between the
        two closest data points.

        The default ``EnforcedNull`` means it is computed automatically, but the setting
        can be used to override the default value.

        .. note::

          If :meth:`data_sorting <BarOptions.data_sorting>` is enabled, the default value
          is implicitly adjusted to ``1``.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._point_range

    @point_range.setter
    def point_range(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._point_range = constants.EnforcedNull
        else:
            self._point_range = validators.numeric(value, allow_empty = True)

    @property
    def point_width(self) -> Optional[int | float | Decimal]:
        """A pixel value specifying a fixed width for each point. When set
        to :obj:`None <python:None>`, the width is calculated from the
        :meth:`point_padding <PictorialOptions.point_padding>` and
        :meth:`group_padding <PictorialOptions.group_padding>`. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_width

    @point_width.setter
    def point_width(self, value):
        self._point_width = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0)
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
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'color_axis': as_dict.get('colorAxis', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'stacking': as_dict.get('stacking', None),
            
            'depth': as_dict.get('depth', None),
            'edge_color': as_dict.get('edgeColor', None),
            'edge_width': as_dict.get('edgeWidth', None),
            'grouping': as_dict.get('grouping', None),
            'group_padding': as_dict.get('groupPadding', None),
            'group_z_padding': as_dict.get('groupZPadding', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'point_padding': as_dict.get('pointPadding', None),
            'point_range': as_dict.get('pointRange', None),
            'point_width': as_dict.get('pointWidth', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'depth': self.depth,
            'edgeColor': self.edge_color,
            'edgeWidth': self.edge_width,
            'grouping': self.grouping,
            'groupPadding': self.group_padding,
            'groupZPadding': self.group_z_padding,
            'maxPointWidth': self.max_point_width,
            'minPointLength': self.min_point_length,
            'pointPadding': self.point_padding,
            'pointRange': self.point_range,
            'pointWidth': self.point_width,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
