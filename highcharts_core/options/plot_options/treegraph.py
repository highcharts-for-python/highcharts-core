import datetime
from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.plot_options.generic import GenericTypeOptions
from highcharts_core.utility_classes.buttons import CollapseButtonConfiguration
from highcharts_core.utility_classes.events import SeriesEvents
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.options.plot_options.link import LinkOptions


class TreegraphEvents(SeriesEvents):
    """General event handlers for the series items. 
    
    .. tip::
    
      These event hooks can also be attached to the series at run time using the ``Highcharts.addEvent()`` (JavaScript) 
      function.
      
    """
    
    def __init__(self, **kwargs):
        self._set_root_node = None
        
        self.set_root_node = kwargs.get('set_root_node', None)
        
        super().__init__(**kwargs)
        
    @property
    def set_root_node(self) -> Optional[CallbackFunction]:
        """Event handler that fires on a request to change the tree's root node, *before* the update is made. 
        
        An event object is passed to the function, containing additional properties ``newRootId``, ``previousRootId``, 
        ``redraw``, and ``trigger``.
        
        Defaults to :obj:`None <python:None>`
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._set_root_node
    
    @set_root_node.setter
    @class_sensitive(CallbackFunction)
    def set_root_node(self, value):
        self._set_root_node = value
        
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'after_animate': as_dict.get('afterAnimate', None),
            'checkbox_click': as_dict.get('checkboxClick', None),
            'click': as_dict.get('click', None),
            'hide': as_dict.get('hide', None),
            'legend_item_click': as_dict.get('legendItemClick', None),
            'mouse_out': as_dict.get('mouseOut', None),
            'mouse_over': as_dict.get('mouseOver', None),
            'show': as_dict.get('show', None),
            
            'set_root_node': as_dict.get('setRootNode', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'afterAnimate': self.after_animate,
            'checkboxClick': self.checkbox_click,
            'click': self.click,
            'hide': self.hide,
            'legendItemClick': self.legend_item_click,
            'mouseOut': self.mouse_out,
            'mouseOver': self.mouse_over,
            'setRootNode': self.set_root_node,
            'show': self.show
        }

        return untrimmed


class TreegraphOptions(GenericTypeOptions):
    """General options to apply to all :term:`Treegraph` series types.
    
    A treegraph visualizes a relationship between ancestors and descendants with a clear parent-child relationship,
    e.g. a family tree or a directory structure.
    
    .. figure:: ../../../_static/treegraph-example.png
      :alt: Treegraph Example Chart
      :align: center
    
    """

    def __init__(self, **kwargs):
        self._animation_limit = None
        self._boost_blending = None
        self._boost_threshold = None
        self._color_index = None
        self._crisp = None
        self._crop_threshold = None
        self._find_nearest_point_by = None
        self._get_extremes_from_all = None
        self._relative_x_value = None
        self._soft_threshold = None
        self._step = None

        self._point_interval = None
        self._point_interval_unit = None
        self._point_start = None
        self._stacking = None

        self._allow_traversing_tree = None
        self._collapse_button = None
        self._color_by_point = None
        self._fill_space = None
        self._link = None
        self._reversed = None        
        self._traverse_up_button = None
        
        self.animation_limit = kwargs.get('animation_limit', None)
        self.boost_blending = kwargs.get('boost_blending', None)
        self.boost_threshold = kwargs.get('boost_threshold', None)
        self.color_index = kwargs.get('color_index', None)
        self.crisp = kwargs.get('crisp', None)
        self.crop_threshold = kwargs.get('crop_threshold', None)
        self.find_nearest_point_by = kwargs.get('find_nearest_point_by', None)
        self.get_extremes_from_all = kwargs.get('get_extremes_from_all', None)
        self.relative_x_value = kwargs.get('relative_x_value', None)
        self.soft_threshold = kwargs.get('soft_threshold',  None)
        self.step = kwargs.get('step', None)

        self.point_interval = kwargs.get('point_interval', None)
        self.point_interval_unit = kwargs.get('point_interval_unit', None)
        self.point_start = kwargs.get('point_start', None)
        self.stacking = kwargs.get('stacking', None)

        self.allow_traversing_tree = kwargs.get('allow_traversing_tree', None)
        self.collapse_button = kwargs.get('collapse_button', None)
        self.color_by_point = kwargs.get('color_by_point', None)
        self.fill_space = kwargs.get('fill_space', None)
        self.link = kwargs.get('link', None)
        self.reversed = kwargs.get('reversed', None)
        
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
    def events(self) -> Optional[TreegraphEvents]:
        """General event handlers for the series items.

        .. note::

          These event hooks can also be attached to the series at run time using the
          (JavaScript) ``Highcharts.addEvent()`` function.

        :rtype: :class:`TreegraphEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(TreegraphEvents)
    def events(self, value):
        self._events = value

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

    @property
    def allow_traversing_tree(self) -> Optional[bool]:
        """If ``True``, the user can click on a point which is a parent and zoom in on its
        children. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_traversing_tree

    @allow_traversing_tree.setter
    def allow_traversing_tree(self, value):
        if value is None:
            self._allow_traversing_tree = None
        else:
            self._allow_traversing_tree = bool(value)

    @property
    def collapse_button(self) -> Optional[CollapseButtonConfiguration]:
        """Options applied to the Collapse Button, which is the small button that indicates the node is collapsible.
        
        :rtype: :class:`CollapseButtonConfiguration <highcharts_core.utility_classes.buttons.CollapseButtonConfiguration>` 
          or :obj:`None <python:None>`
        """
        return self._collapse_button
    
    @collapse_button.setter
    @class_sensitive(CollapseButtonConfiguration)
    def collapse_button(self, value):
        self._collapse_button = value
        
    @property
    def color_by_point(self) -> Optional[bool]:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        if value is None:
            self._color_by_point = None
        else:
            self._color_by_point = bool(value)

    @property
    def fill_space(self) -> Optional[bool]:
        """If ``True``, the treegraph series should fill the entire plot area in the 
        X-axis direction, even when there are collapsed points. Defaults to ``False``.
        
        :rtype: :class:`bool <python:bool>`
        """
        return self._fill_space
    
    @fill_space.setter
    def fill_space(self, value):
        if value is None:
            self._fill_space = None
        else:
            self._fill_space = bool(value)
            
    @property
    def link(self) -> Optional[LinkOptions]:
        """Link style options.

        :rtype: :class:`LinkOptions` or :obj:`None <python:None>`
        """
        return self._link

    @link.setter
    @class_sensitive(LinkOptions)
    def link(self, value):
        self._link = value

    @property
    def reversed(self) -> Optional[bool]:
        """If ``True``, places the series on the other side of the plot area. Defaults to
        ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._reversed

    @reversed.setter
    def reversed(self, value):
        if value is None:
            self._reversed = None
        else:
            self._reversed = bool(value)
            
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
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
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_index': as_dict.get('colorIndex', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'step': as_dict.get('step', None),

            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_start': as_dict.get('pointStart', None),
            'stacking': as_dict.get('stacking', None),

            'allow_traversing_tree': as_dict.get('allowTraversingTree', None),
            'collapse_button': as_dict.get('collapseButton', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'fill_space': as_dict.get('fillSpace', None),
            'link': as_dict.get('link', None),
            'reversed': as_dict.get('reversed', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'allowPointSelect': self.allow_point_select,
            'animation': self.animation,
            'className': self.class_name,
            'clip': self.clip,
            'color': self.color,
            'cursor': self.cursor,
            'custom': self.custom,
            'dashStyle': self.dash_style,
            'dataLabels': self.data_labels,
            'description': self.description,
            'enableMouseTracking': self.enable_mouse_tracking,
            'events': self.events,
            'includeInDataExport': self.include_in_data_export,
            'keys': self.keys,
            'label': self.label,
            'linkedTo': self.linked_to,
            'marker': self.marker,
            'onPoint': self.on_point,
            'opacity': self.opacity,
            'point': self.point,
            'pointDescriptionFormatter': self.point_description_formatter,
            'selected': self.selected,
            'showCheckbox': self.show_checkbox,
            'showInLegend': self.show_in_legend,
            'skipKeyboardNavigation': self.skip_keyboard_navigation,
            'states': self.states,
            'stickyTracking': self.sticky_tracking,
            'threshold': self.threshold,
            'tooltip': self.tooltip,
            'turboThreshold': self.turbo_threshold,
            'visible': self.visible,
            'type': self.type,

            'animationLimit': self.animation_limit,
            'boostBlending': self.boost_blending,
            'boostThreshold': self.boost_threshold,
            'colorIndex': self.color_index,
            'crisp': self.crisp,
            'cropThreshold': self.crop_threshold,
            'findNearestPointBy': self.find_nearest_point_by,
            'getExtremesFromAll': self.get_extremes_from_all,
            'relativeXValue': self.relative_x_value,
            'softThreshold': self.soft_threshold,
            'step': self.step,

            'pointInterval': self.point_interval,
            'pointIntervalUnit': self.point_interval_unit,
            'pointStart': self.point_start,
            'stacking': self.stacking,

            'allowTraversingTree': self.allow_traversing_tree,
            'collapseButton': self.collapse_button,
            'colorByPoint': self.color_by_point,
            'fillSpace': self.fill_space,
            'link': self.link,
            'reversed': self.reversed,
        }

        return untrimmed
