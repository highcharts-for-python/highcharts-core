from typing import Optional

from highcharts.decorators import class_sensitive
from highcharts.plot_options.series import SeriesOptions
from highcharts.utility_classes.jitter import Jitter


class ScatterOptions(SeriesOptions):
    """General options to apply to all Scatter series types.

    A scatter plot uses cartesian coordinates to display values for two variables for
    a set of data.

    .. figure:: _static/scatter-example.png
      :alt: Scatter Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._jitter = None

        self.jitter = kwargs.pop('jitter', None)

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
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'jitter': as_dict.pop('jitter', None)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'jitter': self.jitter
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class Scatter3DOptions(ScatterOptions):
    """General options to apply to all Scatter 3D series types.

    A 3D scatter plot uses x, y and z coordinates to display values for three
    variables for a set of data.

    .. figure:: _static/scatter_3d-example.png
      :alt: Scatter 3D Example Chart
      :align: center

    """
    pass
