import datetime
from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.options.plot_options.generic import GenericTypeOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.shadows import ShadowOptions
from highcharts_core.utility_classes.zones import Zone
from highcharts_core.options.plot_options.data_sorting import DataSorting
from highcharts_core.options.plot_options.drag_drop import DragDropOptions


class SeriesBaseOptions(GenericTypeOptions):
    """General options to apply to all series types."""

    def __init__(self, **kwargs):
        self._animation_limit = None
        self._boost_blending = None
        self._boost_threshold = None
        self._color_index = None
        self._color_key = None
        self._connect_nulls = None
        self._crisp = None
        self._crop_threshold = None
        self._data_sorting = None
        self._find_nearest_point_by = None
        self._get_extremes_from_all = None
        self._linecap = None
        self._line_width = None
        self._relative_x_value = None
        self._shadow = None
        self._soft_threshold = None
        self._step = None
        self._zone_axis = None
        self._zones = None

        self.animation_limit = kwargs.get('animation_limit', None)
        self.boost_blending = kwargs.get('boost_blending', None)
        self.boost_threshold = kwargs.get('boost_threshold', None)
        self.color_index = kwargs.get('color_index', None)
        self.color_key = kwargs.get('color_key', None)
        self.connect_nulls = kwargs.get('connect_nulls', None)
        self.crisp = kwargs.get('crisp', None)
        self.crop_threshold = kwargs.get('crop_threshold', None)
        self.data_sorting = kwargs.get('data_sorting', None)
        self.find_nearest_point_by = kwargs.get('find_nearest_point_by', None)
        self.get_extremes_from_all = kwargs.get('get_extremes_from_all', None)
        self.linecap = kwargs.get('linecap', None)
        self.line_width = kwargs.get('line_width', None)
        self.relative_x_value = kwargs.get('relative_x_value', None)
        self.shadow = kwargs.get('shadow', None)
        self.soft_threshold = kwargs.get('soft_threshold',  None)
        self.step = kwargs.get('step', None)
        self.zone_axis = kwargs.get('zone_axis', None)
        self.zones = kwargs.get('zones', None)

        super().__init__(**kwargs)

    @property
    def animation_limit(self) -> Optional[int | float | Decimal]:
        """For some series, there is a limit that shuts down initial animation by default
        when the total number of points in the chart is too high. Defaults to
        :obj:`None <python:None>`.

        For example, for a column chart and its derivatives, animation does not run if
        there is more than 250 points totally. To disable this cap, set
        ``animation_limit`` to ``float("inf")`` (which represents infinity).

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._animation_limit

    @animation_limit.setter
    def animation_limit(self, value):
        if value == float('inf'):
            self._animation_limit = float('inf')
        else:
            self._animation_limit = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def boost_blending(self) -> Optional[str]:
        """Sets the color blending in the boost module. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boost_blending

    @boost_blending.setter
    def boost_blending(self, value):
        self._boost_blending = validators.string(value, allow_empty = True)

    @property
    def boost_threshold(self) -> Optional[int]:
        """Set the point threshold for when a series should enter boost mode. Defaults to
        ``5000``.

        Setting it to e.g. 2000 will cause the series to enter boost mode when there are
        2,000 or more points in the series.

        To disable boosting on the series, set the ``boost_threshold`` to ``0``. Setting
        it to ``1`` will force boosting.

        .. note::

          The :meth:`AreaOptions.crop_threshold` also affects this setting.

          When zooming in on a series that has fewer points than the ``crop_threshold``,
          all points are rendered although outside the visible plot area, and the
          ``boost_threshold`` won't take effect.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._boost_threshold

    @boost_threshold.setter
    def boost_threshold(self, value):
        self._boost_threshold = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        .. tip::
        
          .. versionadded:: Highcharts (JS) v.11

          With Highcharts (JS) v.11, using CSS variables of the form ``--highcharts-color-{n}`` make
          changing the color scheme very simple.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def color_key(self) -> Optional[str]:
        """Determines what data value should be used to calculate point color if
        :meth:`AreaOptions.color_axis` is used.

        .. note::

          Requires to set ``min`` and ``max`` if some custom point property is used or if
          approximation for data grouping is set to ``'sum'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color_key

    @color_key.setter
    def color_key(self, value):
        self._color_key = validators.string(value, allow_empty = True)

    @property
    def connect_nulls(self) -> Optional[bool]:
        """If ``True``, connect a graph line across null points. If ``False``, renders
        a gap between the points on either side of the null point. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._connect_nulls

    @connect_nulls.setter
    def connect_nulls(self, value):
        if value is None:
            self._connect_nulls = None
        else:
            self._connect_nulls = bool(value)

    @property
    def crisp(self) -> Optional[bool]:
        """If ``True``, each point or column edge is rounded to its nearest pixel in order
        to render sharp on screen. Defaults to ``True``.

        .. hint::

          In some cases, when there are a lot of densely packed columns, this leads to
          visible difference in column widths or distance between columns. In these cases,
          setting ``crisp`` to ``False`` may look better, even though each column is
          rendered blurry.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crisp

    @crisp.setter
    def crisp(self, value):
        if value is None:
            self._crisp = None
        else:
            self._crisp = bool(value)

    @property
    def crop_threshold(self) -> Optional[int]:
        """When the series contains less points than the crop threshold, all points are
        drawn, even if the points fall outside the visible plot area at the current zoom.
        Defaults to ``300``.

        The advantage of drawing all points (including markers and columns), is that
        animation is performed on updates. On the other hand, when the series contains
        more points than the crop threshold, the series data is cropped to only contain
        points that fall within the plot area. The advantage of cropping away invisible
        points is to increase performance on large series.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._crop_threshold

    @crop_threshold.setter
    def crop_threshold(self, value):
        self._crop_threshold = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def data_sorting(self) -> Optional[DataSorting]:
        """Options for the series data sorting.

        :rtype: :class:`DataSorting` or :obj:`None <python:None>`
        """
        return self._data_sorting

    @data_sorting.setter
    @class_sensitive(DataSorting)
    def data_sorting(self, value):
        self._data_sorting = value

    @property
    def find_nearest_point_by(self) -> Optional[str]:
        """Determines whether the series should look for the nearest point in both
        dimensions or just the x-dimension when hovering the series.

        If :obj:`None <python:None>`, defaults to ``'xy'`` for scatter series and ``'x'``
        for most other series. If the data has duplicate x-values, it is recommended to
        set this to ``'xy'`` to allow hovering over all points.

        Applies only to series types using nearest neighbor search (not direct hover) for
        tooltip.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._find_nearest_point_by

    @find_nearest_point_by.setter
    def find_nearest_point_by(self, value):
        self._find_nearest_point_by = validators.string(value, allow_empty = True)

    @property
    def get_extremes_from_all(self) -> Optional[bool]:
        """If ``True``, uses the Y extremes of the total chart width or only the zoomed
        area when zooming in on parts of the X axis. By default, the Y axis adjusts to the
        min and max of the visible data.

        .. warning::

          Applies to :term:`Cartesian series` only.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._get_extremes_from_all

    @get_extremes_from_all.setter
    def get_extremes_from_all(self, value):
        if value is None:
            self._get_extremes_from_all = None
        else:
            self._get_extremes_from_all = bool(value)

    @property
    def linecap(self) -> Optional[str]:
        """The SVG value used for the ``stroke-linecap`` and ``stroke-linejoin`` of a line
        graph. Defaults to ``'round'``, which means that lines are rounded in the ends and
        bends.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._linecap

    @linecap.setter
    def linecap(self, value):
        self._linecap = validators.string(value, allow_empty = True)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the graph line. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def relative_x_value(self) -> Optional[bool]:
        """When ``True``, X values in the data set are relative to the current
        :meth:`point_start <AreaOptions.point_start>`,
        :meth:`point_interval <AreaOptions.point_interval>`, and
        :meth:`point_interval_unit <AreaOptions.point_interval_unit>` settings. This
        allows compression of the data for datasets with irregular X values. Defaults to
        ``False``.

        The real X values are computed on the formula ``f(x) = ax + b``, where ``a`` is
        the :meth:`point_interval <AreaOptions.point_interval>` (optionally with a time
        unit given by :meth:`point_interval_unit <AreaOptions.point_interval_unit>`), and
        ``b`` is the :meth:`point_start <AreaOptions.point_start>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._relative_x_value

    @relative_x_value.setter
    def relative_x_value(self, value):
        if value is None:
            self._relative_x_value = None
        else:
            self._relative_x_value = bool(value)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
        """Configuration for the shadow to apply to the tooltip. Defaults to
        ``False``.

        If ``False``, no shadow is applied.

        :returns: The shadow configuration to apply or a boolean setting which hides the
          shadow or displays the default shadow.
        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if isinstance(value, bool):
            self._shadow = value
        elif not value:
            self._shadow = None
        else:
            value = validate_types(value,
                                   types = ShadowOptions)
            self._shadow = value

    @property
    def soft_threshold(self) -> Optional[bool]:
        """When ``True``, the series will not cause the Y axis to cross the zero plane (or
        threshold option) unless the data actually crosses the plane. Defaults to
        ``True``.

        For example, if ``False``, a series of ``0, 1, 2, 3`` will make the Y axis show
        negative values according to the ``min_padidng`` option. If ``True``, the Y axis
        starts at 0.

        :rtype: :class:`bool <python:bool>`
        """
        return self._soft_threshold

    @soft_threshold.setter
    def soft_threshold(self, value):
        if value is None:
            self._soft_threshold = None
        else:
            self._soft_threshold = bool(value)

    @property
    def step(self) -> Optional[str]:
        """Whether to apply steps to the line. Defaults to :obj:`None <python:None>`.

        Possible values are:

          * :obj:`None <python:None>`
          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._step

    @step.setter
    def step(self, value):
        self._step = validators.string(value, allow_empty = True)

    @property
    def zone_axis(self) -> Optional[str]:
        """Defines the Axis on which the zones are applied. Defaults to ``'y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zone_axis

    @zone_axis.setter
    def zone_axis(self, value):
        self._zone_axis = validators.string(value, allow_empty = True)

    @property
    def zones(self) -> Optional[List[Zone]]:
        """An array defining zones within a series. Defaults to :obj:`None <python:None>`.

        Zones can be applied to the X axis, Y axis or Z axis for bubbles, according to the
        :meth:`zone_axis <AreaOptions.zone_axis>` setting.

        .. warning::

          The zone definitions have to be in ascending order regarding to the value.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of
          :class:`Zone` instances
        """
        return self._zones

    @zones.setter
    @class_sensitive(Zone,
                     force_iterable = True)
    def zones(self, value):
        self._zones = value

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
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'animationLimit': self.animation_limit,
            'boostBlending': self.boost_blending,
            'boostThreshold': self.boost_threshold,
            'colorIndex': self.color_index,
            'colorKey': self.color_key,
            'connectNulls': self.connect_nulls,
            'crisp': self.crisp,
            'cropThreshold': self.crop_threshold,
            'dataSorting': self.data_sorting,
            'findNearestPointBy': self.find_nearest_point_by,
            'getExtremesFromAll': self.get_extremes_from_all,
            'linecap': self.linecap,
            'lineWidth': self.line_width,
            'relativeXValue': self.relative_x_value,
            'shadow': self.shadow,
            'softThreshold': self.soft_threshold,
            'step': self.step,
            'zoneAxis': self.zone_axis,
            'zones': self.zones
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class SeriesOptions(SeriesBaseOptions):
    """General options to apply to all (core) series types."""

    def __init__(self, **kwargs):
        self._color_axis = None
        self._connect_ends = None
        self._drag_drop = None
        self._negative_color = None
        self._point_interval = None
        self._point_interval_unit = None
        self._point_placement = None
        self._point_start = None
        self._stacking = None

        self.color_axis = kwargs.get('color_axis', None)
        self.connect_ends = kwargs.get('connect_ends', None)
        self.drag_drop = kwargs.get('drag_drop', None)
        self.negative_color = kwargs.get('negative_color', None)
        self.point_description_format = kwargs.get('point_description_format', None)
        self.point_interval = kwargs.get('point_interval', None)
        self.point_interval_unit = kwargs.get('point_interval_unit', None)
        self.point_placement = kwargs.get('point_placement', None)
        self.point_start = kwargs.get('point_start', None)
        self.stacking = kwargs.get('stacking', None)

        super().__init__(**kwargs)

    @property
    def color_axis(self) -> Optional[str | int | bool]:
        """When using dual or multiple color axes, this setting defines which
        :term:`color axis` the particular series is connected to. It refers to either the
        :meth:`ColorAxis.id` or the index of the axis in the :class:`ColorAxis` array,
        with ``0`` being the first. Set this option to ``False`` to prevent a series from
        connecting to the default color axis.

        Defaults to ``0``.

        :rtype: :obj:`None <python:None>` or :class:`str <python:str>` or
          :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._color_axis

    @color_axis.setter
    def color_axis(self, value):
        if value is None:
            self._color_axis = None
        elif value is False:
            self._color_axis = False
        else:
            try:
                self._color_axis = validators.string(value)
            except TypeError:
                self._color_axis = validators.integer(value,
                                                      minimum = 0)

    @property
    def connect_ends(self) -> Optional[bool]:
        """If ``True``, connect the ends of a line series plot across the extremes.
        Defaults to :obj:`None <python:None>`.

        .. warning::

          Applies to :term:`polar charts <polar chart>` only.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._connect_ends

    @connect_ends.setter
    def connect_ends(self, value):
        if value is None:
            self._connect_ends = None
        else:
            self._connect_ends = bool(value)

    @property
    def drag_drop(self) -> Optional[DragDropOptions]:
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
    @class_sensitive(DragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def negative_color(self) -> Optional[str | Gradient | Pattern]:
        """The color for the parts of the graph or points that are below the
        :meth:`AreaOptions.threshold`.

        .. note::

          :meth:`Zones <AreaOptions.zones>` take precedence over the negative color.
          Using ``negative_color`` is equivalent to applying a zone with value of 0.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._negative_color

    @negative_color.setter
    def negative_color(self, value):
        from highcharts_core import utility_functions
        self._negative_color = utility_functions.validate_color(value)

    @property
    def point_description_format(self) -> Optional[str]:
        """A :term:`format string` to use instead of the default for 
        point descriptions on the series. Defaults to :obj:`None <python:None>`.
        
        .. note::
        
          Overrides the chart-wide configuration, as applicable.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_description_format
    
    @point_description_format.setter
    def point_description_format(self, value):
        self._point_description_format = validators.string(value, allow_empty = True)

    @property
    def point_interval(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_interval`` defines
        the interval of the x values. Defaults to ``1``.

        For example, if a series contains one value every decade starting from year 0, set
        ``point_interval`` to ``10``. In true datetime axes, the ``point_interval`` is set
        in milliseconds.

        .. hint::

          ``point_interval`` can be also be combined with
          :meth:`point_interval_unit <AreaOptions.point_interval_unit>` to draw irregular
          time intervals.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point, and the ``point_interval`` is added x times to
          the :meth:`point_start <AreaOptions.point_start>` setting.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_interval

    @point_interval.setter
    def point_interval(self, value):
        self._point_interval = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def point_interval_unit(self) -> Optional[str]:
        """On datetime series, this allows for setting the
        :meth:`point_interval <AreaOptions.point_interval>` to irregular time units, day,
        month, and year.

        A day is usually the same as 24 hours, but ``point_interval_unit`` also takes the
        DST crossover into consideration when dealing with local time.

        Combine this option with :meth:`point_interval <AreaOptions.point_interval>` to
        draw weeks, quarters, 6 month periods, 10 year periods, etc.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_interval_unit

    @point_interval_unit.setter
    def point_interval_unit(self, value):
        self._point_interval_unit = validators.string(value, allow_empty = True)

    @property
    def point_placement(self) -> Optional[str | int | float | Decimal]:
        """Used to determine the placement of the point in relation to tick marks on the
        X axis. Defaults to :obj:`None <python:None>`, which behaves as undefined in
        :term:`cartesian charts`, and ``"between"`` in polar charts.

        Accepts possible values:

          * ``'on'`` - where the point will not create any padding of the X axis. In a
            polar column chart this means that the first column points directly
            north.
          * ``"between"`` - where the columns will be laid out between ticks. This is
            useful for example for visualising an amount between two points in time or in
            a certain sector of a polar chart.
          * a numeric value - where ``0`` is on the axis value, ``-0.5`` is between this
            value and the previous, and ``0.5`` is between this value and the next. Unlike
            the textual options, numeric point placement options won't affect axis
            padding.

        .. warning::

          Requires :meth:`point_range <AreaOptions.point_range>` to work. For
          column series this is computed, but for line-type series it needs to be set.

        .. note::

          For the xrange series type and gantt charts, if the Y axis is a category axis,
          the ``point_placement`` applies to the Y axis rather than the (typically
          datetime) X axis.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_placement

    @point_placement.setter
    def point_placement(self, value):
        if value is None:
            self._point_placement = None
        else:
            try:
                self._point_placement = validators.numeric(value,
                                                           minimum = -0.5,
                                                           maximum = 0.5)
            except (TypeError, ValueError):
                value = validators.string(value)
                value = value.lower()
                if value not in ['on', 'between']:
                    raise errors.HighchartsValueError(f'point_placement must be a number,'
                                                      f' "on", or "between". Was: '
                                                      f'{value}')
                self._point_placement = value

    @property
    def point_start(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_start`` defines
        on what value to start. For example, if a series contains one yearly value
        starting from 1945, set ``point_start`` to ``1945``. Defaults to ``0``.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point. The x value from the point options is multiplied
          by :meth:`point_interval <AreaOptions.point_interval>` and added to
          ``point_start`` to produce a modified x value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_start

    @point_start.setter
    def point_start(self, value):
        try:
            value = validators.numeric(value, allow_empty = True)
        except (TypeError, ValueError) as error:
            value = validators.datetime(value)

            if hasattr(value, 'timestamp') and value.tzinfo is not None:
                self._point_start = value.timestamp()*1000
            elif hasattr(value, 'timestamp'):
                value = value.replace(tzinfo = datetime.timezone.utc)
                value = value.timestamp()*1000
            else:
                raise error
            
        self._point_start = value
                
    @property
    def stacking(self) -> Optional[str]:
        """Whether to stack the values of each series on top of each other. Defaults to
        :obj:`None <python:None>`.

        Acceptable values are:

          * :obj:`None <python:None>` to disable stacking,
          * ``"normal"`` to stack by value or
          * ``"percent"``
          * ``'stream'`` (for streamgraph series type only)
          * ``'overlap'`` (for waterfall series type only)

        .. note::

          When stacking is enabled, data must be sorted in ascending X order.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stacking

    @stacking.setter
    def stacking(self, value):
        if not value:
            self._stacking = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['normal', 'percent', 'stream', 'overlap']:
                raise errors.HighchartsValueError(f'stacking expects a valid stacking '
                                                  f'value. However, received: {value}')
            self._stacking = value

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
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'color_axis': as_dict.get('colorAxis', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'stacking': as_dict.get('stacking', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'colorAxis': self.color_axis,
            'connectEnds': self.connect_ends,
            'dragDrop': self.drag_drop,
            'negativeColor': self.negative_color,
            'pointDescriptionFormat': self.point_description_format,
            'pointInterval': self.point_interval,
            'pointIntervalUnit': self.point_interval_unit,
            'pointPlacement': self.point_placement,
            'pointStart': self.point_start,
            'stacking': self.stacking,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
