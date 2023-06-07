from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.utility_classes.jitter import Jitter


class ScatterOptions(SeriesOptions):
    """General options to apply to all Scatter series types.

    A scatter plot uses cartesian coordinates to display values for two variables for
    a set of data.

    .. figure:: ../../../_static/scatter-example.png
      :alt: Scatter Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._jitter = None

        self.jitter = kwargs.get('jitter', None)

        super().__init__(**kwargs)

    @property
    def jitter(self) -> Optional[Jitter]:
        """Apply a jitter effect for the rendered markers.

        When plotting discrete values, a little random noise may help telling the points
        apart. The jitter setting applies a random displacement of up to n axis units in
        either direction.

        So for example on a horizontal X axis, setting the ``jitter.x`` to ``0.24`` will
        render the point in a random position between 0.24 units to the left and 0.24
        units to the right of the true axis position. On a category axis, setting it to
        ``0.5`` will fill up the bin and make the data appear continuous.

        When rendered on top of a box plot or a column series, a jitter value of 0.24 will
        correspond to the underlying series' default ``group_padding`` and
        ``point_padding`` settings.

        :rtype: :class:`Jitter` or :obj:`None <python:None>`
        """
        return self._jitter

    @jitter.setter
    @class_sensitive(Jitter)
    def jitter(self, value):
        self._jitter = value

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
            'line_color': as_dict.get('lineColor', None),
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

            'jitter': as_dict.get('jitter', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'jitter': self.jitter
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class Scatter3DOptions(ScatterOptions):
    """General options to apply to all Scatter 3D series types.

    A 3D scatter plot uses x, y and z coordinates to display values for three
    variables for a set of data.

    .. figure:: ../../../_static/scatter_3d-example.png
      :alt: Scatter 3D Example Chart
      :align: center

    """
    pass
