from typing import Optional

from validator_collection import validators

from highcharts.series.bar import BarSeries
from highcharts.plot_options.histogram import HistogramOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class HistogramSeries(BarSeries, HistogramOptions):
    """Options to configure a Histogram series.

    A histogram is a column series which represents the distribution of the data set
    in the base series. Histogram splits data into bins and shows their frequencies.

    .. figure:: _static/histogram-example.png
      :alt: Histogram Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._base_series = None

        self.base_series = kwargs.pop('base_series', None)

        self.__mro_init__(kwargs)

    @property
    def base_series(self) -> Optional[int | str]:
        """An integer identifying the index to use for the base series, or a string
        representing the id of the series. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._base_series

    @base_series.setter
    def base_series(self, value):
        if value is None:
            self._base_series = None
        else:
            try:
                value = validators.string(value)
            except ValueError:
                value = validators.integer(value)

            self._base_series = value

    @property
    def data(self) -> None:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          All Histogram Series by definition return :obj:`None <python:None>` for their
          data. They are a special series, drawn in relationship to the
          :meth:`base_series <HistogramSeries.base_series>` specified, and do not receive
          independent data points of their own.

        :rtype: :obj:`None <python:None>`
        """
        return None

    @data.setter
    def data(self, value):
        pass

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

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'group_z_padding': as_dict.pop('groupZPadding', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),

            'bins_number': as_dict.pop('binsNumber', None),
            'bin_width': as_dict.pop('binWidth', None),

            'base_series': as_dict.pop('baseSeries', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'baseSeries': self.base_series
        }

        parents_as_dict = mro_to_dict(self) or {}
        for key in parents_as_dict:
            untrimmed[key] = parents_as_dict[key]

        return untrimmed
