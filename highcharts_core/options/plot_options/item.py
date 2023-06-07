from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.options.plot_options.pie import PieOptions


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

        .. figure:: ../../../_static/item-example-circular.png
          :alt: Circular Item Example Chart
          :align: center

      .. tab:: Rectangular Item Chart

        .. figure:: ../../../_static/item-example-rectangular.png
          :alt: Rectangular Item Example Chart
          :align: center

      .. tab:: Item Chart with Symbols

        .. figure:: ../../../_static/item-example-symbols.png
          :alt: Item Example Chart with Symbols
          :align: center

    """

    def __init__(self, **kwargs):
        self._item_padding = None
        self._layout = None
        self._rows = None

        self.item_padding = kwargs.get('item_padding', None)
        self.layout = kwargs.get('layout', None)
        self.rows = kwargs.get('rows', None)

        super().__init__(**kwargs)

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
                    raise errors.HighchartsValueError('inner_size expects a number or '
                                                      'percentage ("%") string. No "%" '
                                                      'character found.')
            except TypeError:
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

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'center': as_dict.get('center', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'colors': as_dict.get('colors', None),
            'depth': as_dict.get('depth', None),
            'end_angle': as_dict.get('endAngle', None),
            'fill_color': as_dict.get('fillColor', None),
            'ignore_hidden_point': as_dict.get('ignoreHiddenPoint', None),
            'inner_size': as_dict.get('innerSize', None),
            'linecap': as_dict.get('linecap', None),
            'min_size': as_dict.get('minSize', None),
            'size': as_dict.get('size', None),
            'sliced_offset': as_dict.get('slicedOffset', None),
            'start_angle': as_dict.get('startAngle', None),
            'thickness': as_dict.get('thickness', None),

            'item_padding': as_dict.get('itemPadding', None),
            'layout': as_dict.get('layout', None),
            'rows': as_dict.get('rows', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'itemPadding': self.item_padding,
            'layout': self.layout,
            'rows': self.rows
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
