from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.plot_options.bar import BarOptions
from highcharts.plot_options.drag_drop import BulletDragDropOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class TargetOptions(HighchartsMeta):
    """All options related to the look and positiong of targets."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._color = None
        self._width = None
        self._height = None

        self.border_color = kwargs.pop('border_color', None)
        self.border_radius = kwargs.pop('border_radius', None)
        self.border_width = kwargs.pop('border_width', None)
        self.color = kwargs.pop('color', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)

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
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._width = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'color': as_dict.pop('color', None),
            'height': as_dict.pop('height', None),
            'width': as_dict.pop('width', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
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

    .. figure:: _static/bullet-example.png
      :alt: Bullet Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._target_options = None

        self.target_options = kwargs.pop('target_options', None)

        super(self).__init__(**kwargs)

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
            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'group_z_padding': as_dict.pop('groupZPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'target_options': as_dict.pop('target_Options', None)

        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'targetOptions': self.target_options
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
