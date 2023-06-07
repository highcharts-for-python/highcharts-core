from typing import Optional, List
from highcharts_core.options.series.funnel import FunnelSeries
from highcharts_core.options.series.pie import PieSeries
from highcharts_core.options.plot_options.pyramid import PyramidOptions, Pyramid3DOptions
from highcharts_core.options.series.data.single_point import SinglePointData
from highcharts_core.utility_functions import mro__to_untrimmed_dict


class PyramidSeries(FunnelSeries, PyramidOptions):
    """Options to configure a Pyramid series.

    A pyramid series is a special type of funnel, without neck and reversed by
    default.

    .. figure:: ../../../_static/pyramid-example.png
      :alt: Pyramid Example Chart
      :align: center

    """
    pass


class Pyramid3DSeries(PyramidOptions, PieSeries):
    """Options to configure a Pyramid 3D series.

    A pyramid 3d series is a special type of funnel, without neck and reversed by
    default.

    .. figure:: ../../../_static/pyramid_3d-example.png
      :alt: Pyramid 3D Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._gradient_for_sides = None

        self.gradient_for_sides = kwargs.get('gradient_for_sides', None)

        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[SinglePointData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`SinglePointData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = FunnelSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a :meth:`y <SinglePointData.y>` value

          .. tab:: Object Collection

            A one-dimensional collection of :class:`SinglePointData` objects.

        :rtype: :class:`list <python:list>` of :class:`SinglePointData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = SinglePointData.from_array(value)

    @property
    def gradient_for_sides(self) -> Optional[bool]:
        """If ``True``, sides fill is set to a gradient. If ``False``, sides are rendered
        with a solid color. Defaults to :obj:`None <python:None>`, which is equivalent to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`.
        """
        return self._gradient_for_sides

    @gradient_for_sides.setter
    def gradient_for_sides(self, value):
        if value is None:
            self._gradient_for_sides = None
        else:
            self._gradient_for_sides = bool(value)

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

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'center': as_dict.get('center', None),
            'colors': as_dict.get('colors', None),
            'depth': as_dict.get('depth', None),
            'end_angle': as_dict.get('endAngle', None),
            'fill_color': as_dict.get('fillColor', None),
            'ignore_hidden_point': as_dict.get('ignoreHiddenPoint', None),
            'inner_size': as_dict.get('innerSize', None),
            'min_size': as_dict.get('minSize', None),
            'size': as_dict.get('size', None),
            'sliced_offset': as_dict.get('slicedOffset', None),
            'start_angle': as_dict.get('startAngle', None),
            'thickness': as_dict.get('thickness', None),

            'height': as_dict.get('height', None),
            'neck_height': as_dict.get('neckHeight', None),
            'neck_width': as_dict.get('neckWidth', None),
            'reversed': as_dict.get('reversed', None),
            'width': as_dict.get('width', None),

            'gradient_for_sides': as_dict.get('gradientForSides', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'data': self.data,
            'gradientForSides': self.gradient_for_sides,
            'colorAxis': self.color_axis,
            'colorIndex': self.color_index,
            'colorKey': self.color_key,
            'linecap': self.linecap
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
