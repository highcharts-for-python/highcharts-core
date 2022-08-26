from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts.plot_options.pie import PieOptions
from highcharts.plot_options.bar import ColumnOptions


class FunnelOptions(PieOptions):
    """General options to apply to all Funnel series types.

    Funnel charts are a type of chart often used to visualize stages in a sales
    project, where the top are the initial stages with the most clients.

    .. warning::

      Funnel charts require that the ``modules/funnel.js`` file is loaded client-side.

    .. figure:: _static/funnel-example.png
      :alt: Funnel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._height = None
        self._neck_height = None
        self._neck_width = None
        self._reversed = None
        self._width = None

        self.height = kwargs.pop('height', None)
        self.neck_height = kwargs.pop('neck_height', None)
        self.neck_width = kwargs.pop('neck_width', None)
        self.reversed = kwargs.pop('reversed', None)
        self.width = kwargs.pop('width', None)

        super().__init__(**kwargs)

    @property
    def height(self) -> Optional[str | int | float | Decimal]:
        """The height of the funnel or pyramid. Defaults to ``'100%'``.

        If it is a number, it defines the height in pixels. If it is a percentage string,
        the height represents the percentage of the plot area height.

        :rtype: :class:`str <python:str>`, numeric, or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        if value is None:
            self._height = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._height = value

    @property
    def neck_height(self) -> Optional[str | int | float | Decimal]:
        """The height of the neck, the lower part of the funnel. Defaults to ``'25%'``.

        A number defines pixel width, a percentage string defines a percentage of the
        plot area height.

        :rtype: :class:`str <python:str>`, numeric, or :obj:`None <python:None>`
        """
        return self._neck_height

    @neck_height.setter
    def neck_height(self, value):
        if value is None:
            self._neck_height = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._neck_height = value

    @property
    def neck_width(self) -> Optional[str | int | float | Decimal]:
        """The width of the neck, the lower part of the funnel. Defaults to ``'30%'``.

        A number defines pixel width, a percentage string defines a percentage of the
        plot area width.

        :rtype: :class:`str <python:str>`, numeric, or :obj:`None <python:None>`
        """
        return self._neck_width

    @neck_width.setter
    def neck_width(self, value):
        if value is None:
            self._neck_width = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._neck_width = value

    @property
    def reversed(self) -> Optional[bool]:
        """If ``True``, the widest area of the funnel is lower down. A reversed funnel
        with no neck width and neck height is a pyramid.

        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._reversed

    @reversed.setter
    def reversed(self, value):
        if value is None:
            self._reversed = None
        else:
            self._reversed = bool(value)

    @property
    def width(self) -> Optional[str | int | float | Decimal]:
        """The width of the funnel. Defaults to ``'90%'``.

        A number defines pixel width, a percentage string defines a percentage of the
        plot area width.

        :rtype: :class:`str <python:str>`, numeric, or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        if value is None:
            self._width = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._width = value

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

            'height': as_dict.pop('height', None),
            'neck_height': as_dict.pop('neckHeight', None),
            'neck_width': as_dict.pop('neckWidth', None),
            'reversed': as_dict.pop('reversed', None),
            'width': as_dict.pop('width', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'height': self.height,
            'neckHeight': self.neck_height,
            'neckWidth': self.neck_width,
            'reversed': self.reversed,
            'width': self.width
        }
        parent_as_dict = super()._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class Funnel3DOptions(FunnelOptions, ColumnOptions):
    """General options to apply to all Funnel 3D series types.

    A Funnel 3D chart is a three-dimensional version of funnel series type. Funnel
    charts are a type of chart often used to visualize stages in a sales project,
    where the top are the initial stages with the most clients.

    .. warning::

      Funnel 3D charts require that the following files are all loaded client-side:

        * ``highcharts-3d.js``,
        * ``cylinder.js`` and
        * ``funnel3d.js``

    .. figure:: _static/funnel_3d-example.png
      :alt: Funnel 3D Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._gradient_for_sides = None

        self.gradient_for_sides = kwargs.pop('gradient_for_sides', None)

        super(Funnel3DOptions, self).__init__(**kwargs)

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
            'gradient_for_sides': as_dict.pop('gradientForSides', None)
        }
        mro = cls.__mro__
        parent_kwargs = [x._get_kwargs_from_dict(as_dict) for x in mro[1:2]]
        for kwarg_set in parent_kwargs:
            for key in kwarg_set:
                kwargs[key] = kwarg_set[key]

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'centerInCategory': self.center_in_category,
            'colorByPoint': self.color_by_point,
            'depth': self.depth,
            'edgeColor': self.edge_color,
            'edgeWidth': self.edge_width,
            'grouping': self.grouping,
            'groupPadding': self.group_padding,
            'groupZPadding': self.group_z_padding,
            'maxPointWidth': self.max_point_width,
            'minPointLength': self.min_point_length,
            'pointPadding': self.point_padding,
            'pointRange': self.point_range,
            'pointWidth': self.point_width,

            'height': self.height,
            'neckHeight': self.neck_height,
            'neckWidth': self.neck_width,
            'reversed': self.reversed,
            'width': self.width,

            'gradientForSides': self.gradient_for_sides
        }
        parent_as_dict = super()._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
