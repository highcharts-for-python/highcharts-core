from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_python import errors
from highcharts_python.decorators import class_sensitive
from highcharts_python.metaclasses import HighchartsMeta
from highcharts_python.options.series.base import SeriesBase
from highcharts_python.utility_classes.gradients import Gradient
from highcharts_python.utility_classes.patterns import Pattern
from highcharts_python.options.axes.x_axis import XAxis
from highcharts_python.options.axes.y_axis import YAxis


class HandleOptions(HighchartsMeta):
    """Options for the handles that allow dragging the zoomed-in area."""

    def __init__(self, **kwargs):
        self._background_color = None
        self._border_color = None
        self._enabled = None
        self._height = None
        self._line_width = None
        self._symbols = None
        self._width = None

        self.background_color = kwargs.get('background_color', None)
        self.border_color = kwargs.get('border_color', None)
        self.enabled = kwargs.get('enabled', None)
        self.height = kwargs.get('height', None)
        self.line_width = kwargs.get('line_width', None)
        self.symbols = kwargs.get('symbols', None)
        self.width = kwargs.get('width', None)

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or gradient for the pane. Defaults to ``'#f2f2f2'``.

        :returns: The backgorund color for the handle.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        from highcharts_python import utility_functions
        self._background_color = utility_functions.validate_color(value)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the pane border. Defaults to ``'#999999'``.

        :returns: The color of the handle border and the stripes inside.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_python import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the handles. if ``False``, disables them. Defaults to
        :obj:`None <python:None>`, which behaves as ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height given to the handles, expressed in pixels. Defaults to ``15``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The width of the handle border and the stripes inside, expressed in pixels.
        Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value, allow_empty = True)

    @property
    def symbols(self) -> Optional[List[str]]:
        """Configuration of the shapes given to the handles. Defaults to
        :obj:`None <python:None>`, which applies
        ``['navigator-handle', 'navigator-handle']``.

        .. note::

          The ``symbols`` setting takes a 2-member collection of
          :class:`str <python:str>` values. These values can either indicate CSS styles
          (as in the default behavior), a ``url(...)`` to a graphic image, or the name
          of a (JavaScript) ``SVGRenderer.prototype.symbols`` callback method.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._symbols

    @symbols.setter
    def symbols(self, value):
        if not value:
            self._symbols = None
        else:
            self._symbols = [validators.string(x)
                             for x in validators.iterable(value,
                                                          minimum_length = 2,
                                                          maximum_length = 2)]

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width given to the handles, expressed in pixels. Defaults to ``7``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'enabled': as_dict.get('enabled', None),
            'height': as_dict.get('height', None),
            'line_width': as_dict.get('lineWidth', None),
            'symbols': as_dict.get('symbols', None),
            'width': as_dict.get('width', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'enabled': self.enabled,
            'height': self.height,
            'lineWidth': self.line_width,
            'symbols': self.symbols,
            'width': self.width,
        }

        return untrimmed


class Navigator(HighchartsMeta):
    """The navigator is a small series below the main series, displaying a view of the
    entire data set. It provides tools to zoom in and out on parts of the data as well as
    panning across the dataset."""

    def __init__(self, **kwargs):
        self._adapt_to_updated_data = None
        self._enabled = None
        self._handles = None
        self._height = None
        self._margin = None
        self._mask_fill = None
        self._mask_inside = None
        self._opposite = None
        self._outline_color = None
        self._outline_width = None
        self._series = None
        self._x_axis = None
        self._y_axis = None

        self.adapt_to_updated_data = kwargs.get('adapt_to_updated_data', None)
        self.enabled = kwargs.get('enabled', None)
        self.handles = kwargs.get('handles', None)
        self.height = kwargs.get('height', None)
        self.margin = kwargs.get('margin', None)
        self.mask_fill = kwargs.get('mask_fill', None)
        self.mask_inside = kwargs.get('mask_inside', None)
        self.opposite = kwargs.get('opposite', None)
        self.outline_color = kwargs.get('outline_color', None)
        self.outline_width = kwargs.get('outline_width', None)
        self.series = kwargs.get('series', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)

    @property
    def adapt_to_updated_data(self) -> Optional[bool]:
        """If ``True``, the navigator and scroll will adapt to updated data in the base
        X-axis. Defaults to :obj:`None <python:None>`, which behaves as ``False``.

        .. hint::

          When loading data asynchronously, this should be ``False``. Otherwise new data
          will trigger the navigator to redraw, which will cause unwanted looping.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._adapt_to_updated_data

    @adapt_to_updated_data.setter
    def adapt_to_updated_data(self, value):
        if value is None:
            self._adapt_to_updated_data = None
        else:
            self._adapt_to_updated_data = bool(value)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the navigator. if ``False``, disables it. Defaults to
        :obj:`None <python:None>`, which behaves as ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def handles(self) -> Optional[HandleOptions]:
        """Options for the handles that allow dragging the zoomed-in area. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`HandleOptions` or :obj:`None <python:None>`
        """
        return self._handles

    @handles.setter
    @class_sensitive(HandleOptions)
    def handles(self, value):
        self._handles = value

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height given to the navigator, expressed in pixels. Defaults to ``40``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def margin(self) -> Optional[int | float | Decimal]:
        """The distance from the nearest element (either the X-axis or the X-axis labels),
        expressed in pixels. Defaults to ``25``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = validators.numeric(value, allow_empty = True)

    @property
    def mask_fill(self) -> Optional[str | Gradient | Pattern]:
        """The color of the mask covering the areas of the navigator series that are
        currently not visible in the main series. Defaults to ``'rgba(102,103,194,0.3)'``,
        which is bluish and slightly transparent to see the series below.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._mask_fill

    @mask_fill.setter
    def mask_fill(self, value):
        if not value:
            self._mask_fill = None
        elif isinstance(value, (Gradient, Pattern)):
            self._mask_fill = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._mask_fill = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._mask_fill = Gradient.from_dict(value)
                else:
                    self._mask_fill = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._mask_fill = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._mask_fill = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._mask_fill = Pattern.from_dict(value)
                else:
                    self._mask_fill = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._mask_fill = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def mask_inside(self) -> Optional[bool]:
        """If ``True``, renders the mask inside the range marking the zoomed-in data. If
        ``False``, renders the mask outside the zoomed-in data range. Defaults to
        :obj:`None <python:None>`, which behaves as ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._mask_inside

    @mask_inside.setter
    def mask_inside(self, value):
        if value is None:
            self._mask_inside = None
        else:
            self._mask_inside = bool(value)

    @property
    def opposite(self) -> Optional[bool]:
        """If ``True``, renders the navigator on the opposite side when the chart is
        inverted. Defaults to :obj:`None <python:None>`, which behaves as ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._opposite

    @opposite.setter
    def opposite(self, value):
        if value is None:
            self._opposite = None
        else:
            self._opposite = bool(value)

    @property
    def outline_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the line marking the currently zoomed area in the navigator.
        Defaults to ``'#cccccc'.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._outline_color

    @outline_color.setter
    def outline_color(self, value):
        from highcharts_python import utility_functions
        self._outline_color = utility_functions.validate_color(value)

    @property
    def outline_width(self) -> Optional[int | float | Decimal]:
        """The width of the line marking the currently zoomed-in area of the navigator.
        Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._outline_width

    @outline_width.setter
    def outline_width(self, value):
        self._outline_width = validators.numeric(value, allow_empty = True)

    @property
    def series(self) -> Optional[SeriesBase]:
        """Options for the navigator series (the series of data drawn in the navigator).
        Defaults to :obj:`None <python:None>`, which is equivalent to:

          .. code-block:: python

            series = AreaSplineSeries(
                fill_opacity = 0.05,
                data_grouping = DataGrouping(smoothed = True),
                line_width = 1,
                marker = Marker(enabled = False)
            )

        .. hint::

          If the ``series`` setting does not have :meth:`data <SeriesBase.data>`
          explicitly provided, it will default to the :meth:`data <SeriesBase.data>`
          of the first series in the chart.

        :rtype: :class:`SeriesBase` or :obj:`None <python:None>`
        """
        return self._series

    @series.setter
    @class_sensitive(SeriesBase)
    def series(self, value):
        self._series = value

    @property
    def x_axis(self) -> Optional[XAxis]:
        """Configuration of the navigator's X-axis. Defaults to :obj:`None <python:None>`,
        which implicitly applies the following:

          .. code-block:: python

            x_axis = XAxis(
                tick_width = 0,
                line_width = 0,
                grid_line_width = 1,
                tick_pixel_interval = 200,
                labels = AxisLabelOptions(align = left,
                                          style = { 'color': '#888' },
                                          x = 3,
                                          y = -4)
            )

        :rtype: :class:`XAxis` or :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    @class_sensitive(XAxis)
    def x_axis(self, value):
        self._x_axis = value

    @property
    def y_axis(self) -> Optional[YAxis]:
        """Configuration of the navigator's X-axis. Defaults to :obj:`None <python:None>`,
        which implicitly applies the following:

          .. code-block:: python

            y_axis = YAxis(
                grid_line_width = 0,
                start_on_tick = False,
                end_on_tick = False,
                min_padding = 0.1,
                max_padding = 0.1
                labels = AxisLabelOptions(enabled = False),
                title = AxisTitle(text = None),
                tick_width = 0
            )

        :rtype: :class:`YAxis` or :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    @class_sensitive(YAxis)
    def y_axis(self, value):
        self._y_axis = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'adapt_to_updated_data': as_dict.get('adaptToUpdatedData', None),
            'enabled': as_dict.get('enabled', None),
            'handles': as_dict.get('handles', None),
            'height': as_dict.get('height', None),
            'margin': as_dict.get('margin', None),
            'mask_fill': as_dict.get('maskFill', None),
            'mask_inside': as_dict.get('maskInside', None),
            'opposite': as_dict.get('opposite', None),
            'outline_color': as_dict.get('outlineColor', None),
            'outline_width': as_dict.get('outlineWidth', None),
            'series': as_dict.get('series', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'adaptToUpdatedData': self.adapt_to_updated_data,
            'enabled': self.enabled,
            'handles': self.handles,
            'height': self.height,
            'margin': self.margin,
            'maskFill': self.mask_fill,
            'maskInside': self.mask_inside,
            'opposite': self.opposite,
            'outlineColor': self.outline_color,
            'outlineWidth': self.outline_width,
            'series': self.series,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed
