from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.plot_options.bar import BarOptions
from highcharts_core.options.plot_options.drag_drop import BulletDragDropOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class TargetOptions(HighchartsMeta):
    """All options related to the look and positiong of targets."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._color = None
        self._width = None
        self._height = None

        self.border_color = kwargs.get('border_color', None)
        self.border_radius = kwargs.get('border_radius', None)
        self.border_width = kwargs.get('border_width', None)
        self.color = kwargs.get('color', None)
        self.height = kwargs.get('height', None)
        self.width = kwargs.get('width', None)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The border color of the rectangle representing the target. When
        :obj:`None <python:None>`, the point's border color is used. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The corner radius of the rectangle surrounding the target. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width of the rectangle representing the target. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the rectangle representing the target. When
        :obj:`None <python:None>`, applies the point's color (if set in point's options -
        ``color``), or the zone of the target value (if ``zones`` or ``negative_color``
        are set), or the same color as the point.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height of the rectangle representing the target, expressed in pixels.
        Defaults to ``3``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def width(self) -> Optional[str | int | float | Decimal]:
        """The width of the rectangle representing the target. Could be set as a pixel
        value or as a percentage of a column width. Defaults to ``'140%'``.

        :rtype: numeric, :class:`str <python:str>`, or :obj:`None <python:None>`
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
                    raise errors.HighchartsValueError('width expects either a number or '
                                                      'a % string. No "%" character '
                                                      'found.')
            except TypeError:
                value = validators.numeric(value, minimum = 0)

            self._width = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'color': as_dict.get('color', None),
            'height': as_dict.get('height', None),
            'width': as_dict.get('width', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'color': self.color,
            'height': self.height,
            'width': self.width
        }

        return untrimmed


class BulletOptions(BarOptions):
    """General options to apply to all Bullet series types.

    A bullet graph is a variation of a bar graph. The bullet graph features a single
    measure, compares it to a target, and displays it in the context of qualitative
    ranges of performance that could be set using :meth:`YAxis.plot_bands`.

    .. figure:: ../../../_static/bullet-example.png
      :alt: Bullet Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._target_options = None

        self.target_options = kwargs.get('target_options', None)

        super().__init__(**kwargs)

    @property
    def drag_drop(self) -> Optional[BulletDragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(BulletDragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def target_options(self) -> Optional[TargetOptions]:
        """All options related to the look and positiong of targets.

        :rtype: :class:`TargetOptions` or :obj:`None <python:None>`
        """
        return self._target_options

    @target_options.setter
    @class_sensitive(TargetOptions)
    def target_options(self, value):
        self._target_options = value

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

            'target_options': as_dict.get('targetOptions', None)

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'targetOptions': self.target_options
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
