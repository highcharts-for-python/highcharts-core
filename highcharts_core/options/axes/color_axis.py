from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern

from highcharts_core.options.axes.generic import GenericAxis
from highcharts_core.options.axes.data_classes import DataClass
from highcharts_core.options.axes.markers import AxisMarker


class ColorAxis(GenericAxis):
    """A color axis for series.

    Visually, the color axis will appear as a gradient or as separate items inside the
    legend, depending on whether the axis is scalar or based on data classes.

    .. seealso::

      For supported color formats, see the
      `documentation article about colors <https://www.highcharts.com/docs/chart-design-and-style/colors>`_.

    A scalar color axis is represented by a gradient. The colors either range between the
    :meth:`ColorAxis.min_color` and the :meth:`ColorAxis.max_color`, or for more
    fine-grained control the colors can be defined in :meth:`ColorAxis.stops`. Often
    times, the color axis needs to be adjusted to get the right color spread for the data.
    In addition to :meth:`stops <ColorAxis.stops>`, consider using a logarithmic axis
    type, or setting min and max to avoid the colors being determined by outliers.

    .. note::

      When :meth:`ColorAxis.data_classes` are used, the ranges are subdivided into
      separate classes like categories based on their values. This can be used for ranges
      between two values, but also for a true category. However, when your data is
      categorized, it may be as convenient to add each category to a separate series.

    .. warning::

      :class:`ColorAxis` does not work with the following series types:

        * :term:`sankey <Sankey Chart>`
        * :term:`sunburst <Sunburst>`
        * :term:`dependency wheels <Dependency Wheel>`
        * :term:`network graphs <Network Graph>`
        * :term:`wordclouds <Wordcloud>`
        * :term:`venn diagrams <Venn Diagram>`
        * :term:`solidgauge <SolidGauge>`

    """

    def __init__(self, **kwargs):
        self._data_class_color = None
        self._data_classes = None
        self._layout = None
        self._line_color = None
        self._marker = None
        self._max_color = None
        self._min_color = None
        self._show_in_legend = None
        self._stops = None

        self.data_class_color = kwargs.get('data_class_color', None)
        self.data_classes = kwargs.get('data_classes', None)
        self.layout = kwargs.get('layout', None)
        self.line_color = kwargs.get('line_color', None)
        self.marker = kwargs.get('marker', None)
        self.max_color = kwargs.get('max_color', None)
        self.min_color = kwargs.get('min_color', None)
        self.show_in_legend = kwargs.get('show_in_legend', None)
        self.stops = kwargs.get('stops', None)

        super().__init__(**kwargs)

    @property
    def data_class_color(self) -> Optional[str]:
        """Determines how to set each data class' color if no individual color is set.
        The default value, ``'tween'``, computes intermediate colors between
        :meth:`ColorAxis.min_color` and :meth:`ColorAxis.max_color`. The other possible
        value, ``'category'``, pulls colors from the global or chart specific ``colors``
        array.

        Defaults to ``'tween'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._data_class_color

    @data_class_color.setter
    def data_class_color(self, value):
        if not value:
            self._data_class_color = None
        else:
            value = validators.string(value)
            if value not in ['tween', 'category']:
                raise errors.HighchartsValueError(f'data_class_color expects either '
                                                  f'"tween" or "category". Received: '
                                                  f'{value}')
            self._data_class_color = value

    @property
    def data_classes(self) -> Optional[List[DataClass]]:
        """A collection of data classes or ranges for the choropleth map. If
        :obj:`None <python:None>`, the color axis will be scalar and values will be
        distributed as a gradient between the minimum and maximum colors. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`DataClass` instances, or
          :obj:`None <python:None>`
        """
        return self._data_classes

    @data_classes.setter
    @class_sensitive(DataClass, force_iterable = True)
    def data_classes(self, value):
        self._data_classes = value

    @property
    def layout(self) -> Optional[str]:
        """The layout of the color axis. Defaults to :obj:`None <python:None>`.

        Accepts either:

          * ``'horizontal'``
          * ``'vertical'``

        If :obj:`None <python:None>`, the color axis will have the same layout as the
        legend.

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
                raise errors.HighchartsValueError(f'layout expects either '
                                                  f'"horizontal" or "vertical", but '
                                                  f'received: {value}')

            self._layout = value

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
    def marker(self) -> Optional[AxisMarker]:
        """The triangular marker on a scalar color axis that points to the value of the
        hovered area. To disable the marker, set the value to :obj:`None <python:None>`.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`AxisMarker` or :obj:`None <python:None>`
        """
        return self._marker

    @marker.setter
    @class_sensitive(AxisMarker)
    def marker(self, value):
        self._marker = value

    @property
    def max_color(self) -> Optional[str | Gradient | Pattern]:
        """The color used to represent the maximum value of the color axis. Defaults to
        ``'#003399'``.

        Unless :meth:`data_classes <ColorAxis.data_classes>` or
        :meth:`stops <ColorAxis.stops>` are set, the gradient ends at this value.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._max_color

    @max_color.setter
    def max_color(self, value):
        from highcharts_core import utility_functions
        self._max_color = utility_functions.validate_color(value)

    @property
    def min_color(self) -> Optional[str | Gradient | Pattern]:
        """The color used to represent the minimum value of the color axis. Defaults to
        ``'#e6ebf5'``.

        Unless :meth:`data_classes <ColorAxis.data_classes>` or
        :meth:`stops <ColorAxis.stops>` are set, the gradient starts at this value.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._min_color

    @min_color.setter
    def min_color(self, value):
        from highcharts_core import utility_functions
        self._min_color = utility_functions.validate_color(value)

    @property
    def show_in_legend(self) -> Optional[bool]:
        """Whether to display the color axis in the legend. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._show_in_legend

    @show_in_legend.setter
    def show_in_legend(self, value):
        if value is None:
            self._show_in_legend = None
        else:
            self._show_in_legend = bool(value)

    @property
    def stops(self) -> Optional[List[List[int | float | Decimal | str]]]:
        """Color stops for the gradient in a color axis. Defaults to
        :obj:`None <python:None>`.

        .. hint::

          Use this in cases where a linear gradient between a
          :meth:`min_color <ColorAxis.min_color>` and
          :meth:`max_color <ColorAxis.max_color>` is not sufficient.

        .. note::

          Expects an iterable of 2-member iterables. Each 2-member iterable should be
          composed of a number and a string. The number should be a value between 0 and
          1 which assigns the relative position of the color in the gradient, while the
          string should represent the color itself.

        :rtype: :class:`list <python:list>` of :class:`list <python:list>`, where each
          second :class:`list <python:list>` consists of a :class:`float <python:float>`
          and a :class:`str <python:str>` / or :obj:`None <python:None>`
        """
        return self._stops

    @stops.setter
    def stops(self, value):
        if not value:
            self._stops = None
        else:
            value = validators.iterable(value)
            processed_items = []
            for item in value:
                item = validators.iterable(item)
                if len(item) != 2:
                    raise errors.HighchartsValueError(f'stops expects a list of 2-'
                                                      f'member iterables. Received a '
                                                      f'{len(item)}-member iterable.')
                item = [validators.float(item[0],
                                         minimum = 0,
                                         maximum = 1),
                        validators.string(item[1])]
                processed_items.append(item)

            self._stops = processed_items

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'angle': as_dict.get('angle', None),
            'ceiling': as_dict.get('ceiling', None),
            'class_name': as_dict.get('className', None),
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
            'panning_enabled': as_dict.get('panningEnabled', None),
            'reversed': as_dict.get('reversed', None),
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
            'type': as_dict.get('type', None),
            'unique_names': as_dict.get('uniqueNames', None),
            'units': as_dict.get('units', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),

            'data_class_color': as_dict.get('dataClassColor', None),
            'data_classes': as_dict.get('dataClasses', None),
            'layout': as_dict.get('layout', None),
            'line_color': as_dict.get('lineColor', None),
            'marker': as_dict.get('marker', None),
            'max_color': as_dict.get('maxColor', None),
            'min_color': as_dict.get('minColor', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'stops': as_dict.get('stops', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'angle': self.angle,
            'ceiling': self.ceiling,
            'className': self.class_name,
            'endOnTick': self.end_on_tick,
            'events': self.events,
            'floor': self.floor,
            'gridLineColor': self.grid_line_color,
            'gridLineDashStyle': self.grid_line_dash_style,
            'gridLineInterpolation': self.grid_line_interpolation,
            'gridLineWidth': self.grid_line_width,
            'gridZIndex': self.grid_z_index,
            'id': self.id,
            'labels': self.labels,
            'margin': self.margin,
            'max': self.max,
            'maxPadding': self.max_padding,
            'min': self.min,
            'minorGridLineColor': self.minor_grid_line_color,
            'minorGridLineDashStyle': self.minor_grid_line_dash_style,
            'minorGridLineWidth': self.minor_grid_line_width,
            'minorTickColor': self.minor_tick_color,
            'minorTickInterval': self.minor_tick_interval,
            'minorTickLength': self.minor_tick_length,
            'minorTickPosition': self.minor_tick_position,
            'minorTicks': self.minor_ticks,
            'minorTickWidth': self.minor_tick_width,
            'minPadding': self.min_padding,
            'panningEnabled': self.panning_enabled,
            'reversed': self.reversed,
            'showFirstLabel': self.show_first_label,
            'showLastLabel': self.show_last_label,
            'softMax': self.soft_max,
            'softMin': self.soft_min,
            'startOfWeek': self.start_of_week,
            'startOnTick': self.start_on_tick,
            'tickAmount': self.tick_amount,
            'tickColor': self.tick_color,
            'tickInterval': self.tick_interval,
            'tickLength': self.tick_length,
            'tickmarkPlacement': self.tickmark_placement,
            'tickPixelInterval': self.tick_pixel_interval,
            'tickPosition': self.tick_position,
            'tickPositioner': self.tick_positioner,
            'tickPositions': self.tick_positions,
            'tickWidth': self.tick_width,
            'type': self.type,
            'uniqueNames': self.unique_names,
            'units': self.units,
            'visible': self.visible,
            'zIndex': self.z_index,

            'dataClassColor': self.data_class_color,
            'dataClasses': self.data_classes,
            'layout': self.layout,
            'lineColor': self.line_color,
            'marker': self.marker,
            'maxColor': self.max_color,
            'minColor': self.min_color,
            'showInLegend': self.show_in_legend,
            'stops': self.stops
        }

        return untrimmed
