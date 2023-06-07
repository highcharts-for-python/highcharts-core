from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class HeatmapOptions(SeriesOptions):
    """General options to apply to all Heatmap series types.

    A heatmap is a graphical representation of data where the individual values
    contained in a matrix are represented as colors.

    .. warning::

      Heatmaps require that ``modules/heatmap`` is loaded client-side.

    .. figure:: ../../../_static/heatmap-example.png
      :alt: Heatmap Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_radius = None
        self._colsize = None
        self._interpolation = None
        self._null_color = None
        self._point_padding = None
        self._rowsize = None

        self.border_radius = kwargs.get('border_radius', None)
        self.colsize = kwargs.get('colsize', None)
        self.interpolation = kwargs.get('interpolation', None)
        self.null_color = kwargs.get('null_color', None)
        self.point_padding = kwargs.get('point_padding', None)
        self.rowsize = kwargs.get('rowsize', None)

        super().__init__(**kwargs)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The border radius for each heatmap item. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def colsize(self) -> Optional[int]:
        """The column size - how many X axis units each column in the heatmap should span.
        Defaults to ``1``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._colsize

    @colsize.setter
    def colsize(self, value):
        self._colsize = validators.integer(value,
                                           allow_empty = True,
                                           minimum = 1)

    @property
    def interpolation(self) -> Optional[bool]:
        """If ``True``, renders data points as an interpolated image.
        Defaults to ``False``.
        
        :rtype: :class:`bool <python:bool>`
        """
        return self._interpolation
    
    @interpolation.setter
    def interpolation(self, value):
        if value is None:
            self._interpolation = None
        else:
            self._interpolation = bool(value)

    @property
    def null_color(self) -> Optional[str | Gradient | Pattern]:
        """The color applied to null points. Defaults to ``'#f7f7f7'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._null_color

    @null_color.setter
    def null_color(self, value):
        from highcharts_core import utility_functions
        self._null_color = utility_functions.validate_color(value)

    @property
    def point_padding(self) -> Optional[int | float | Decimal]:
        """Padding between the points in the heatmap. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_padding

    @point_padding.setter
    def point_padding(self, value):
        self._point_padding = validators.numeric(value, allow_empty = True)

    @property
    def rowsize(self) -> Optional[int]:
        """The row size - how many Y axis units each heatmap row should span. Defaults to
        ``1``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._rowsize

    @rowsize.setter
    def rowsize(self, value):
        self._rowsize = validators.integer(value,
                                           allow_empty = True,
                                           minimum = 1)

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
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'border_radius': as_dict.get('borderRadius', None),
            'colsize': as_dict.get('colsize', None),
            'interpolation': as_dict.get('interpolation', None),
            'null_color': as_dict.get('nullColor', None),
            'point_padding': as_dict.get('pointPadding', None),
            'rowsize': as_dict.get('rowsize', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderRadius': self.border_radius,
            'colsize': self.colsize,
            'interpolation': self.interpolation,
            'nullColor': self.null_color,
            'pointPadding': self.point_padding,
            'rowsize': self.rowsize
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class TilemapOptions(HeatmapOptions):
    """General options to apply to all Tilemap series types.

    A tilemap series is a type of heatmap where the tile shapes are configurable.

    .. tabs::

      .. tab:: Honeycomb Tilemap

        .. figure:: ../../../_static/tilemap-example.png
          :alt: Honeycomb Tilemap Example Chart
          :align: center

      .. tab:: Circle Tilemap

        .. figure:: ../../../_static/tilemap-example-circle.png
          :alt: Tilemap Example Chart
          :align: center

      .. tab:: Diamond Tilemap

        .. figure:: ../../../_static/tilemap-example-diamond.png
          :alt: Tilemap Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._tile_shape = None

        self.tile_shape = kwargs.get('tile_shape', None)

        super().__init__(**kwargs)

    @property
    def tile_shape(self) -> Optional[str]:
        """The shape of the tiles in the tilemap. Defaults to ``'hexagon'``.

        Possible values are:

          * ``'hexagon'``
          * ``'circle'``
          * ``'diamond'``
          * ``'square'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._tile_shape

    @tile_shape.setter
    def tile_shape(self, value):
        if not value:
            self._tile_shape = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['hexagon', 'circle', 'diamond', 'square']:
                raise errors.HighchartsValueError(f'tile_shape expects "hexagon", '
                                                  f'"circle", "diamond", or "square". '
                                                  f'Received: {value}')
            self._tile_shape = value

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
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'border_radius': as_dict.get('borderRadius', None),
            'colsize': as_dict.get('colsize', None),
            'interpolation': as_dict.get('interpolation', None),
            'null_color': as_dict.get('nullColor', None),
            'point_padding': as_dict.get('pointPadding', None),
            'rowsize': as_dict.get('rowsize', None),

            'tile_shape': as_dict.get('tileShape', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'tileShape': self.tile_shape
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
