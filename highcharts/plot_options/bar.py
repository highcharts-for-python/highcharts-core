from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.plot_options.series import SeriesOptions
from highcharts.utility_classes.gradients import Gradient
from higcharts.utility_classes.patterns import Pattern


class BarOptions(SeriesOptions):
    """General options to apply to all Bar series types. A bar series is a special
    type of column series where the columns are horizontal.

    .. figure:: _static/bar-example.png
      :alt: Bar Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._center_in_category = None
        self._color_by_point = None
        self._depth = None
        self._edge_color = None
        self._edge_width = None
        self._grouping = None
        self._group_padding = None
        self._group_z_padding = None
        self._max_point_width = None
        self._min_point_length = None
        self._point_padding = None
        self._point_range = None
        self._point_width = None

        self.border_color = kwargs.pop('border_color', '#ffffff')
        self.border_radius = kwargs.pop('border_radius', 0)
        self.border_width = kwargs.pop('border_width', None)
        self.center_in_category = kwargs.pop('center_in_category', False)
        self.color_by_point = kwargs.pop('color_by_point', False)
        self.depth = kwargs.pop('depth', 25)
        self.edge_color = kwargs.pop('edge_color', None)
        self.edge_width = kwargs.pop('edge_width', 1)
        self.grouping = kwargs.pop('grouping', True)
        self.group_padding = kwargs.pop('group_padding', 0.2)
        self.group_z_padding = kwargs.pop('group_z_padding', 1)
        self.max_point_width = kwargs.pop('max_point_width', None)
        self.min_point_length = kwargs.pop('min_point_length', 0)
        self.point_padding = kwargs.pop('point_padding', 0.1)
        self.point_range = kwargs.pop('point_range', constants.EnforcedNull)
        self.point_width = kwargs.pop('point_width', None)

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
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The corner radius of the border surrounding each column or bar. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

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
        """The maximum allowed pixel width for a column, translated to the height of a bar
        in a bar chart. This prevents the columns from becoming too wide when there is a
        small number of points in the chart. Defaults to :obj:`None <python:None>`.

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
        """The minimal height for a column or width for a bar. Defaults to ``0``.

        By default, ``0`` values are not shown. To visualize a ``0`` (or close to zero)
        point, set the minimal point length to a pixel value like ``3``.

        .. warning::

          In stacked column charts, ``min_point_length`` might not be respected for
          tightly packed values.

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
    def point_range(self) -> constants.EnforcedNullType | int | float | Decimal:
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

        :rtype: numeric or :class:`EnforcedNullType`
        """
        return self._point_range

    @point_range.setter
    def point_range(self, value):
        if not value and value != 0:
            self._point_range = constants.EnforcedNull
        else:
            self._point_range = validators.numeric(value)

    @property
    def point_width(self) -> Optional[int | float | Decimal]:
        """A pixel value specifying a fixed width for each column or bar point. When set
        to :obj:`None <python:None>`, the width is calculated from the
        :meth:`point_padding <BarOptions.point_padding>` and
        :meth:`group_padding <BarOptions.group_padding>`. Defaults to
        :obj:`None <python:None>`.

        The width effects the dimension that is not based on the point value. For column
        series, this is the hoizontal length while for bar series it is the vertical
        length.

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

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', 0.75),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', False),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', '#ffffff'),
            'border_radius': as_dict.pop('borderRadius', 0),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', False),
            'color_by_point': as_dict.pop('colorByPoint', False),
            'depth': as_dict.pop('depth', 25),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', 1),
            'grouping': as_dict.pop('grouping', True),
            'group_padding': as_dict.pop('groupPadding', 0.2),
            'group_z_padding': as_dict.pop('groupZPadding', 1),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', 0),
            'point_padding': as_dict.pop('pointPadding', 0.1),
            'point_range': as_dict.pop('pointRange', constants.EnforcedNull),
            'point_width': as_dict.pop('pointWidth', None)
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'centerInCategory': self.center_in_category,
            'colorByPoint': self.color_by_point,
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
            'pointWidth': self.point_width
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class ColumnOptions(BarOptions):
    """General options to apply to all Column series types.

    Column series display one column per value along an X axis.

    .. figure:: _static/column-example.png
      :alt: Column Example Chart
      :align: center

    """
    pass


class ColumnPyramidOptions(ColumnOptions):
    """General options to apply to all Column Pyramid series types.

    Column Pyramid series display one pyramid per value along an X axis.

    .. hint::

      To display horizontal pyramids, set :meth:`Chart.inverted` to ``True``.

    .. tabs::

      .. tab:: Standard

        .. figure:: _static/columnpyramid-example.png
          :alt: ColumnPyramid Example Chart
          :align: center

      .. tab:: Stacked

        .. figure:: _static/columnpyramid-example-stacked.png
          :alt: Stacked Column Pyramid Example Chart
          :align: center

      .. tab:: Stacked + Inverted

        .. figure:: _static/columnpyramid-example-stacked-horizontal.png
          :alt: Stacked and Inverted Column Pyramid Example Chart
          :align: center

    """
    pass


class ColumnRangeOptions(ColumnOptions):
    """General options to apply to all Column Range series types.

    The column range is a cartesian series type with higher and lower Y values along
    an X axis.

    .. hint::

      To display horizontal bars, set :meth:`Chart.inverted` to ``True``.

    .. tabs::

      .. tab:: Standard

        .. figure:: _static/columnrange-example.png
          :alt: ColumnRange Example Chart
          :align: center

      .. tab:: Horizontal

        .. figure:: _static/columnrange-example-horizontal.png
          :alt: Inverted Column Range Example Chart
          :align: center

    """
    pass


class CylinderOptions(BarOptions):
    """General options to apply to all Cylinder series types.

    A cylinder graph is a variation of a 3d column graph. The cylinder graph features
    cylindrical points.

    .. figure:: _static/cylinder-example.png
      :alt: Cylinder Example Chart
      :align: center

    """
    pass
