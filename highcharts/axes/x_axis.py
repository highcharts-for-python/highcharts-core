from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern

from highcharts.axes.numeric import NumericAxis
from highcharts.axes.crosshair import CrosshairOptions


class XAxis(NumericAxis):
    """Configuration settings for the X axis or category axis.

    Normally, this is the horizontal axis, though if the chart is inverted this becomes
    the vertical axis."""

    def __init__(self, **kwargs):
        self._crosshair = None
        self._height = None
        self._left = None
        self._line_color = None
        self._line_width = None
        self._show_empty = None
        self._top = None
        self._width = None

        self.crosshair = kwargs.pop('crosshair', None)
        self.height = kwargs.pop('height', None)
        self.left = kwargs.pop('left', None)
        self.line_color = kwargs.pop('line_color', None)
        self.line_width = kwargs.pop('line_width', None)
        self.show_empty = kwargs.pop('show_empty', None)
        self.top = kwargs.pop('top', None)
        self.width = kwargs.pop('width', None)

        super().__init__(**kwargs)

    @property
    def crosshair(self) -> Optional[CrosshairOptions]:
        """Configure a crosshair that follows either the mouse pointer or the hovered
        point. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CrosshairOptions` or :obj:`None <python:None>`
        """
        return self._crosshair

    @crosshair.setter
    @class_sensitive(CrosshairOptions)
    def crosshair(self, value):
        self._crosshair = value

    @property
    def height(self) -> Optional[str | int | float | Decimal]:
        """The height of the axis when operating as the vertical axis, expressed either in
        pixels or as a percentage of the total plot height. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
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
    def left(self) -> Optional[str | int | float | Decimal]:
        """The left position of the axis when operating as a horizontal axis, expresesd
        as the pixel position relative to the chart or a percentage of the plot width,
        offset from the plot area's ``left`` position. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._left

    @left.setter
    def left(self, value):
        if value is None:
            self._left = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._left = value

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the line marking the axis itself. Defaults to ``'#ccd6eb'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        if not value:
            self._line_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._line_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._line_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Gradient.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._line_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._line_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Pattern.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._line_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The width of the marking the axis itself, in pixels. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def show_empty(self) -> Optional[bool]:
        """If ``True``, render the axis title and axis line even if the axis has no data.
        If ``False``, does not render the axis when the axis has no data. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_empty

    @show_empty.setter
    def show_empty(self, value):
        if value is None:
            self._show_empty = None
        else:
            self._show_empty = bool(value)

    @property
    def top(self) -> Optional[str | int | float | Decimal]:
        """The top position of the axis when operating as a vertical axis, expresesd
        as the pixel position relative to the chart or a percentage of the plot width,
        offset from the plot area's ``top`` position. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._top

    @top.setter
    def top(self, value):
        if value is None:
            self._top = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._top = value

    @property
    def width(self) -> Optional[str | int | float | Decimal]:
        """The width of the axis when operating as the vertical axis, expressed either in
        pixels or as a percentage of the total plot width. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
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
            'accessibility': as_dict.pop('accessibility', None),
            'align_ticks': as_dict.pop('alignTicks', None),
            'allow_decimals': as_dict.pop('allowDecimals', None),
            'alternate_grid_color': as_dict.pop('alternateGridColor', None),
            'angle': as_dict.pop('angle', None),
            'breaks': as_dict.pop('breaks', None),
            'categories': as_dict.pop('categories', None),
            'ceiling': as_dict.pop('ceiling', None),
            'class_name': as_dict.pop('className', None),
            'date_time_label_formats': as_dict.pop('dateTimeLabelFormats', None),
            'end_on_tick': as_dict.pop('endOnTick', None),
            'events': as_dict.pop('events', None),
            'floor': as_dict.pop('floor', None),
            'grid_line_color': as_dict.pop('gridLineColor', None),
            'grid_line_dash_style': as_dict.pop('gridLineDashStyle', None),
            'grid_line_interpolation': as_dict.pop('gridLineInterpolation', None),
            'grid_line_width': as_dict.pop('gridLineWidth', None),
            'grid_z_index': as_dict.pop('gridZIndex', None),
            'id': as_dict.pop('id', None),
            'labels': as_dict.pop('labels', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'margin': as_dict.pop('margin', None),
            'max': as_dict.pop('max', None),
            'max_padding': as_dict.pop('maxPadding', None),
            'min': as_dict.pop('min', None),
            'minor_grid_line_color': as_dict.pop('minorGridLineColor', None),
            'minor_grid_line_dash_style': as_dict.pop('minorGridLineDashStyle', None),
            'minor_grid_line_width': as_dict.pop('minorGridLineWidth', None),
            'minor_tick_color': as_dict.pop('minorTickColor', None),
            'minor_tick_interval': as_dict.pop('minorTickInterval', None),
            'minor_tick_length': as_dict.pop('minorTickLength', None),
            'minor_tick_position': as_dict.pop('minorTickPosition', None),
            'minor_ticks': as_dict.pop('minorTicks', None),
            'minor_tick_width': as_dict.pop('minorTickWidth', None),
            'min_padding': as_dict.pop('minPadding', None),
            'min_range': as_dict.pop('minRange', None),
            'min_tick_interval': as_dict.pop('minTickInterval', None),
            'offset': as_dict.pop('offset', None),
            'opposite': as_dict.pop('opposite', None),
            'pane': as_dict.pop('pane', None),
            'panning_enabled': as_dict.pop('panningEnabled', None),
            'plot_bands': as_dict.pop('plotBands', None),
            'plot_lines': as_dict.pop('plotLines', None),
            'reversed': as_dict.pop('reversed', None),
            'reversed_stacks': as_dict.pop('reversedStacks', None),
            'show_first_label': as_dict.pop('showFirstLabel', None),
            'show_last_label': as_dict.pop('showLastLabel', None),
            'soft_max': as_dict.pop('softMax', None),
            'soft_min': as_dict.pop('softMin', None),
            'start_of_week': as_dict.pop('startOfWeek', None),
            'start_on_tick': as_dict.pop('startOnTick', None),
            'tick_amount': as_dict.pop('tickAmount', None),
            'tick_color': as_dict.pop('tickColor', None),
            'tick_interval': as_dict.pop('tickInterval', None),
            'tick_length': as_dict.pop('tickLength', None),
            'tickmark_placement': as_dict.pop('tickmarkPlacement', None),
            'tick_pixel_interval': as_dict.pop('tickPixelInterval', None),
            'tick_position': as_dict.pop('tickPosition', None),
            'tick_positioner': as_dict.pop('tickPositioner', None),
            'tick_positions': as_dict.pop('tickPositions', None),
            'tick_width': as_dict.pop('tickWidth', None),
            'title': as_dict.pop('title', None),
            'type': as_dict.pop('type', None),
            'unique_names': as_dict.pop('uniqueNames', None),
            'units': as_dict.pop('units', None),
            'visible': as_dict.pop('visible', None),
            'z_index': as_dict.pop('zIndex', None),
            'zoom_enabled': as_dict.pop('zoomEnabled', None),

            'crosshair': as_dict.pop('crosshair', None),
            'height': as_dict.pop('height', None),
            'left': as_dict.pop('left', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'show_empty': as_dict.pop('showEmpty', None),
            'top': as_dict.pop('top', None),
            'width': as_dict.pop('width', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'crosshair': self.crosshair,
            'height': self.height,
            'left': self.left,
            'line_color': self.line_color,
            'line_width': self.line_width,
            'show_empty': self.show_empty,
            'top': self.top,
            'width': self.width
        }

        parent_as_dict = super()._to_untrimmed_dict()
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
