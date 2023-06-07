from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import validate_types
from highcharts_core.options.plot_options.bar import BarOptions
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class HistogramOptions(BarOptions):
    """General options to apply to all Histogram series types.

    A histogram is a column series which represents the distribution of the data set
    in the base series. Histogram splits data into bins and shows their frequencies.

    .. figure:: ../../../_static/histogram-example.png
      :alt: Histogram Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._bins_number = None
        self._bin_width = None

        self.bins_number = kwargs.get('bins_number', None)
        self.bin_width = kwargs.get('bin_width', None)

        super().__init__(**kwargs)

    @property
    def bins_number(self) -> Optional[CallbackFunction | str | int]:
        """A preferable number of bins. Defaults to ``'square-root'``.

        .. warning::

          This setting is a suggestion, so a histogram may have a different number of
          bins.

        By default, it is set to the square root of the base series' data length.

        Available options are:

          * ``'square-root'``
          * ``'sturges'``
          * ``'rice'``

        You can also provide a JavaScript function which takes a ``baseSeries`` as a
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
                value = validate_types(value,
                                       types = CallbackFunction,
                                       allow_none = False)
            except (TypeError, ValueError):
                try:
                    value = validators.string(value)
                    value = value.lower()
                    if value not in ['square-root', 'sturges', 'rice']:
                        raise errors.HighchartsValueError(f'bins_number expects a number,'
                                                          f' a JavaScript callback '
                                                          f'function, or a string value '
                                                          f'of "square-root", "sturges", '
                                                          f'or "rice". Received: '
                                                          f'{value}')
                except TypeError:
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
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'track_by_area': as_dict.get('trackByArea', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'grouping': as_dict.get('grouping', None),
            'group_padding': as_dict.get('groupPadding', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'point_padding': as_dict.get('pointPadding', None),
            'point_range': as_dict.get('pointRange', None),
            'point_width': as_dict.get('pointWidth', None),

            'depth': as_dict.get('depth', None),
            'edge_color': as_dict.get('edgeColor', None),
            'edge_width': as_dict.get('edgeWidth', None),
            'group_z_padding': as_dict.get('groupZPadding', None),

            'bins_number': as_dict.get('binsNumber', None),
            'bin_width': as_dict.get('binWidth', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'binsNumber': self.bins_number,
            'binWidth': self.bin_width
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
