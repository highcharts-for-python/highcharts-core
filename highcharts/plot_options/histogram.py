from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts.plot_options.bar import BarOptions


class HistogramOptions(BarOptions):
    """General options to apply to all Histogram series types.

    A histogram is a column series which represents the distribution of the data set
    in the base series. Histogram splits data into bins and shows their frequencies.

    .. figure:: _static/histogram-example.png
      :alt: Histogram Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._bins_number = None
        self._bin_width = None

        self.bins_number = kwargs.pop('bins_number', None)
        self.bin_width = kwargs.pop('bin_width', None)

        super().__init__(**kwargs)

    @property
    def bins_number(self) -> Optional[str | int]:
        """A preferable number of bins. Defaults to ``'square-root'``.

        .. warning::

          This setting is a suggestion, so a histogram may have a different number of
          bins.

        By default, it is set to the square root of the base series' data length.

        Available options are:

          * ``'square-root'``
          * ``'sturges'``
          * ``'rice'``

        You can also provie a JavaScript function which takes a ``baseSeries`` as a
        parameter and returns a positive integer.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._bins_number

    @bins_number.setter
    def bins_number(self, value):
        if value is None:
            self._bins_number = None
        else:
            try:
                value = validators.string(value)
            except ValueError:
                value = validators.integer(value, minimum = 0)

            self._bins_number = value

    @property
    def bin_width(self) -> Optional[int | float | Decimal]:
        """Width of each bin. If :obj:`None <python:None>`, the default behavior is to
        calculate the width as ``(max - min) / number of bins``.

        .. note::

          This option takes precedence over :meth:`HistogramOptions.bins_number`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._bin_width

    @bin_width.setter
    def bin_width(self, value):
        self._bin_width = validators.numeric(value,
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
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'bins_number': as_dict.pop('binsNumber', None),
            'bin_width': as_dict.pop('binWidth', None)
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'binsNumber': self.bins_number,
            'binWidth': self.bin_width
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
