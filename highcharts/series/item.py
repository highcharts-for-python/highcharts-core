from typing import Optional, List

from highcharts.series.pie import PieSeries
from highcharts.plot_options.item import ItemOptions
from highcharts.series.data.single_point import SinglePointData
from highcharts.utility_functions import mro_init, mro_to_dict


class ItemSeries(PieSeries, ItemOptions):
    """Options to configure an Item series.

    An item chart is an infographic chart where a number of items are laid out in
    either a rectangular or circular pattern. It can be used to visualize counts
    within a group, or for the circular pattern, typically a parliament.

    The circular layout has much in common with a pie chart. Many of the item series
    options, like ``center``, ``size`` and data label positioning, are inherited from
    the :meth:`PlotOptions.pie` series and don't apply for rectangular layouts.

    .. tabs::

      .. tab:: Circular Item Chart

        .. figure:: _static/item-example-circular.png
          :alt: Circular Item Example Chart
          :align: center

      .. tab:: Rectangular Item Chart

        .. figure:: _static/item-example-rectangular.png
          :alt: Rectangular Item Example Chart
          :align: center

      .. tab:: Item Chart with Symbols

        .. figure:: _static/item-example-symbols.png
          :alt: Item Example Chart with Symbols
          :align: center

    """

    def __init__(self, **kwargs):
        self.__mro_init__(kwargs)

    @property
    def data(self) -> Optional[List[SinglePointData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`SinglePointData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = ItemSeries()
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
            self._data = SinglePointData.from_setter(value)

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

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center': as_dict.pop('center', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'colors': as_dict.pop('colors', None),
            'depth': as_dict.pop('depth', None),
            'end_angle': as_dict.pop('endAngle', None),
            'fill_color': as_dict.pop('fillColor', None),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', None),
            'inner_size': as_dict.pop('innerSize', None),
            'linecap': as_dict.pop('linecap', None),
            'min_size': as_dict.pop('minSize', None),
            'size': as_dict.pop('size', None),
            'sliced_offset': as_dict.pop('slicedOffset', None),
            'start_angle': as_dict.pop('startAngle', None),

            'item_padding': as_dict.pop('itemPadding', None),
            'layout': as_dict.pop('layout', None),
            'rows': as_dict.pop('rows', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro_to_dict(self)

        return untrimmed
