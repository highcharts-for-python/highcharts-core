from copy import deepcopy
from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.options.plot_options.pie import PieOptions
from highcharts_core.options.plot_options.bar import ColumnOptions


class FunnelOptions(PieOptions):
    """General options to apply to all Funnel series types.

    Funnel charts are a type of chart often used to visualize stages in a sales
    project, where the top are the initial stages with the most clients.

    .. warning::

      Funnel charts require that the ``modules/funnel.js`` file is loaded client-side.

    .. figure:: ../../../_static/funnel-example.png
      :alt: Funnel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_radius = None
        self._height = None
        self._neck_height = None
        self._neck_width = None
        self._reversed = None
        self._width = None

        self.border_radius = kwargs.get('border_radius', None)
        self.height = kwargs.get('height', None)
        self.neck_height = kwargs.get('neck_height', None)
        self.neck_width = kwargs.get('neck_width', None)
        self.reversed = kwargs.get('reversed', None)
        self.width = kwargs.get('width', None)

        super().__init__(**kwargs)

    @property
    def border_radius(self) -> Optional[str | int | float | Decimal]:
        """The corner radius of the border surrounding all points or series. Defaults to ``0``.
        
        .. note::
        
          A number signifies pixels. A percentage string (e.g.``'50%'``) signifies a size 
          relative to the series width.
          
        :rtype: :class:`str <python:str>`, numeric, or :obj:`None <python:None>`
        """
        return self._border_radius
        
    @border_radius.setter
    def border_radius(self, value):
        if value is None:
            self._border_radius = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('border_radius expects a number or a "%" '
                                                      'string. No "%" character found.')
            except TypeError:
                value = validators.numeric(value, minimum = 0)

            self._border_radius = value
        

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
                    raise errors.HighchartsValueError('height expects a number or a "%" '
                                                      'string. No "%" character found.')
            except TypeError:
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
                    raise errors.HighchartsValueError('neck_height expects a number or a '
                                                      '"%" string. No "%" character '
                                                      'found.')
            except TypeError:
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
                    raise errors.HighchartsValueError('neck_width expects a number or a '
                                                      '"%" string. No "%" character '
                                                      'found.')
            except TypeError:
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
                    raise errors.HighchartsValueError('width expects a number or a '
                                                      '"%" string. No "%" character '
                                                      'found.')
            except TypeError:
                value = validators.numeric(value, minimum = 0)

            self._width = value

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

            'border_radius': as_dict.get('borderRadius', None),
            'height': as_dict.get('height', None),
            'neck_height': as_dict.get('neckHeight', None),
            'neck_width': as_dict.get('neckWidth', None),
            'reversed': as_dict.get('reversed', None),
            'width': as_dict.get('width', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderRadius': self.border_radius,
            'height': self.height,
            'neckHeight': self.neck_height,
            'neckWidth': self.neck_width,
            'reversed': self.reversed,
            'width': self.width
        }
        parent_as_dict = self._untrimmed_mro_ancestors(in_cls = in_cls)

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

    .. figure:: ../../../_static/funnel_3d-example.png
      :alt: Funnel 3D Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._gradient_for_sides = None

        self.gradient_for_sides = kwargs.get('gradient_for_sides', None)

        super().__init__(**kwargs)

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
            'gradient_for_sides': as_dict.get('gradientForSides', None)
        }
        mro = cls.mro()
        parent_kwargs = [x._get_kwargs_from_dict(as_dict) for x in mro[1:2]]
        for kwarg_set in parent_kwargs:
            for key in kwarg_set:
                kwargs[key] = kwarg_set[key]

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'gradientForSides': self.gradient_for_sides,
        }
        parent_as_dict = self._untrimmed_mro_ancestors(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
