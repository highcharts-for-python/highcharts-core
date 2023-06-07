from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern

from highcharts_core.options.axes.numeric import NumericAxis
from highcharts_core.options.axes.crosshair import CrosshairOptions


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
        self._minor_ticks_per_major = None
        self._show_empty = None
        self._top = None
        self._width = None

        self.crosshair = kwargs.get('crosshair', None)
        self.height = kwargs.get('height', None)
        self.left = kwargs.get('left', None)
        self.line_color = kwargs.get('line_color', None)
        self.line_width = kwargs.get('line_width', None)
        self.minor_ticks_per_major = kwargs.get('minor_ticks_per_major', None)
        self.show_empty = kwargs.get('show_empty', None)
        self.top = kwargs.get('top', None)
        self.width = kwargs.get('width', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'xAxis'

    @property
    def crosshair(self) -> Optional[CrosshairOptions]:
        """Configure a crosshair that follows either the mouse pointer or the hovered
        point. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CrosshairOptions` or :obj:`None <python:None>`
        """
        return self._crosshair

    @crosshair.setter
    def crosshair(self, value):
        if isinstance(value, bool):
            value = {
                'enabled': value
            }

        self._crosshair = validate_types(value, CrosshairOptions)

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
            except (TypeError, ValueError):
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
            except (TypeError, ValueError):
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
        from highcharts_core import utility_functions
        self._line_color = utility_functions.validate_color(value)

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
    def minor_ticks_per_major(self) -> Optional[int | float | Decimal]:
        """The number of minor ticks per major tick. Defaults to ``5``.
        
        .. note::
        
          Works for ``linear``, ``logarithmic`` and ``datetime`` axes.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._minor_ticks_per_major
        
    @minor_ticks_per_major.setter
    def minor_ticks_per_major(self, value):
        self._minor_ticks_per_major = validators.numeric(value,
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
            except (TypeError, ValueError):
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
            except (TypeError, ValueError):
                value = validators.numeric(value, minimum = 0)

            self._width = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'align_ticks': as_dict.get('alignTicks', None),
            'allow_decimals': as_dict.get('allowDecimals', None),
            'alternate_grid_color': as_dict.get('alternateGridColor', None),
            'angle': as_dict.get('angle', None),
            'breaks': as_dict.get('breaks', None),
            'categories': as_dict.get('categories', None),
            'ceiling': as_dict.get('ceiling', None),
            'class_name': as_dict.get('className', None),
            'crossing': as_dict.get('crossing', None),
            'date_time_label_formats': as_dict.get('dateTimeLabelFormats', None),
            'end_on_tick': as_dict.get('endOnTick', None),
            'events': as_dict.get('events', None),
            'floor': as_dict.get('floor', None),
            'grid_line_color': as_dict.get('gridLineColor', None),
            'grid_line_dash_style': as_dict.get('gridLineDashStyle', None),
            'grid_line_interpolation': as_dict.get('gridLineInterpolation', None),
            'grid_line_width': as_dict.get('gridLineWidth', None),
            'grid_z_index': as_dict.get('gridZIndex', None),
            'id': as_dict.get('id', None),
            'labels': as_dict.get('labels', None),
            'linked_to': as_dict.get('linkedTo', None),
            'margin': as_dict.get('margin', None),
            'max': as_dict.get('max', None),
            'max_padding': as_dict.get('maxPadding', None),
            'min': as_dict.get('min', None),
            'minor_grid_line_color': as_dict.get('minorGridLineColor', None),
            'minor_grid_line_dash_style': as_dict.get('minorGridLineDashStyle', None),
            'minor_grid_line_width': as_dict.get('minorGridLineWidth', None),
            'minor_tick_color': as_dict.get('minorTickColor', None),
            'minor_tick_interval': as_dict.get('minorTickInterval', None),
            'minor_tick_length': as_dict.get('minorTickLength', None),
            'minor_tick_position': as_dict.get('minorTickPosition', None),
            'minor_ticks': as_dict.get('minorTicks', None),
            'minor_tick_width': as_dict.get('minorTickWidth', None),
            'min_padding': as_dict.get('minPadding', None),
            'min_range': as_dict.get('minRange', None),
            'min_tick_interval': as_dict.get('minTickInterval', None),
            'offset': as_dict.get('offset', None),
            'opposite': as_dict.get('opposite', None),
            'pane': as_dict.get('pane', None),
            'panning_enabled': as_dict.get('panningEnabled', None),
            'plot_bands': as_dict.get('plotBands', None),
            'plot_lines': as_dict.get('plotLines', None),
            'reversed': as_dict.get('reversed', None),
            'reversed_stacks': as_dict.get('reversedStacks', None),
            'show_first_label': as_dict.get('showFirstLabel', None),
            'show_last_label': as_dict.get('showLastLabel', None),
            'soft_max': as_dict.get('softMax', None),
            'soft_min': as_dict.get('softMin', None),
            'start_of_week': as_dict.get('startOfWeek', None),
            'start_on_tick': as_dict.get('startOnTick', None),
            'tick_amount': as_dict.get('tickAmount', None),
            'tick_color': as_dict.get('tickColor', None),
            'tick_interval': as_dict.get('tickInterval', None),
            'tick_length': as_dict.get('tickLength', None),
            'tickmark_placement': as_dict.get('tickmarkPlacement', None),
            'tick_pixel_interval': as_dict.get('tickPixelInterval', None),
            'tick_position': as_dict.get('tickPosition', None),
            'tick_positioner': as_dict.get('tickPositioner', None),
            'tick_positions': as_dict.get('tickPositions', None),
            'tick_width': as_dict.get('tickWidth', None),
            'title': as_dict.get('title', None),
            'type': as_dict.get('type', None),
            'unique_names': as_dict.get('uniqueNames', None),
            'units': as_dict.get('units', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),
            'zoom_enabled': as_dict.get('zoomEnabled', None),

            'crosshair': as_dict.get('crosshair', None),
            'height': as_dict.get('height', None),
            'left': as_dict.get('left', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'minor_ticks_per_major': as_dict.get('minorTicksPerMajor', None),
            'show_empty': as_dict.get('showEmpty', None),
            'top': as_dict.get('top', None),
            'width': as_dict.get('width', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'crosshair': self.crosshair,
            'height': self.height,
            'left': self.left,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
            'minorTicksPerMajor': self.minor_ticks_per_major,
            'showEmpty': self.show_empty,
            'top': self.top,
            'width': self.width
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
