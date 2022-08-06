from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.plot_options.pie import PieOptions


class ItemOptions(PieOptions):
    """General options to apply to all Item series types.

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
        self._item_padding = None
        self._layout = None
        self._rows = None

        self.item_padding = kwargs.pop('item_padding', None)
        self.layout = kwargs.pop('layout', None)
        self.rows = kwargs.pop('rows', None)

    @property
    def inner_size(self) -> Optional[str | int]:
        """In circular view, the size of the inner diameter of the circle. Defaults to
        ``40%``. Can be a percentage or pixel value.

        .. note::

          Percentages are relative to the outer perimeter. Pixel values are given as
          integers.

        .. warning::

          If :meth:`ItemOptions.rows` is set, this value will be overridden by the
          ``rows`` setting.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._inner_size

    @inner_size.setter
    def inner_size(self, value):
        if value is None:
            self._inner_size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.integer(value, minimum = 0)

            self._inner_size = value

    @property
    def item_padding(self) -> Optional[int | float | Decimal]:
        """The padding between the items, given in relative size where the size of the
        item itself is 1. Defaults to ``0.1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._item_padding

    @item_padding.setter
    def item_padding(self, value):
        self._item_padding = validators.numeric(value, allow_empty = True)

    @property
    def layout(self) -> Optional[str]:
        """The layout of the items in rectangular view. Defaults to ``'vertical'``.

        Accepts:

          * ``'horizontal'``
          * ``'vertical'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._layout

    @layout.setter
    def layout(self, value):
        if not value:
            self._layout = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['horizontal', 'vertical']:
                raise errors.HighchartsValueError(f'layout expects "horizontal" or '
                                                  f'"vertical", but was: {value}')

            self._layout = value

    @property
    def rows(self) -> Optional[int]:
        """The number of rows to display in the rectangular or circular view. Defaults to
        :obj:`None <python:None>`.

        .. note::

          If the :meth:`ItemOptions.inner_size` is set, it will be overridden by the
          ``rows`` setting.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = validators.integer(value, allow_empty = True)

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
            'rows': as_dict.pop('rows', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'item_padding': self.item_padding,
            'layout': self.layout,
            'rows': self.rows
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
