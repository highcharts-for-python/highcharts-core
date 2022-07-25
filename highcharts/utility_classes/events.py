from typing import Optional

from validator_collection import validators

from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.javascript_functions import CallbackFunction


class ChartEvents(HighchartsMeta):
    """Event listeners for the chart."""

    def __init__(self, **kwargs):
        self._add_series = None
        self._after_print = None
        self._before_print = None
        self._click = None
        self._drilldown = None
        self._drillup = None
        self._drillupall = None
        self._export_data = None
        self._fullscreen_close = None
        self._fullscreen_open = None
        self._load = None
        self._redraw = None
        self._render = None
        self._selection = None

        for attribute in dir(self):
            if attribute.startswith('_') and not attribute.startswith('__'):
                non_private_name = attribute[1:]
                setattr(self, non_private_name, kwargs.pop(non_private_name, None))

    @property
    def add_series(self) -> Optional[str]:
        """JavaScript callback function that fires when a series is added to the chart
        after load time, using the JavaScript ``.addSeries()`` method.

        One parameter, ``event``, is passed to the JavaScript function, containing common
        event information. Through ``event.options`` you can access the series options
        that were passed to the ``.addSeries()`` method.

        Returning ``false`` prevents the series from being added.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._add_series

    @add_series.setter
    def add_series(self, value):
        self._add_series = validators.string(value, allow_empty = False)

    @property
    def after_print(self) -> Optional[str]:
        """JavaScript callback function that fires after a chart has been printed through
        the context menu or the ``Chart.print()`` JavaScript method.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._after_print

    @after_print.setter
    def after_print(self, value):
        self._after_print = validators.string(value, allow_empty = False)

    @property
    def before_print(self) -> Optional[str]:
        """JavaScript callback function that fires before a chart is printed through
        the context menu or the ``Chart.print()`` JavaScript method.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._before_print

    @before_print.setter
    def before_print(self, value):
        self._before_print = validators.string(value, allow_empty = False)

    @property
    def click(self) -> Optional[str]:
        """JavaScript callback function that fires when the user clicks on the plot
        background. One parameter, ``event``, is passed to the JavaScript function,
        containing common event information.

        .. hint::

          Information on the clicked spot can be found in your JavaScript function through
          ``event.xAxis`` and ``event.yAxis``, which are arrays containing the axes of
          each dimension and each axis' value at the clicked spot.

          The primary axes are ``event.xAxis[0]`` and ``event.yAxis[0]``.

          Remember the unit of a datetime axis is milliseconds since 1970-01-01 00:00:00.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    def click(self, value):
        self._click = validators.string(value, allow_empty = False)

    @property
    def drilldown(self) -> Optional[str]:
        """JavaScript callback function that fires when a drilldown point is clicked,
        before the new series is added.

        This callback function is also used for asynchronous drilldown, where the
        JavaScript ``seriesOptions`` are not added using the configuration options, but
        are instead loaded asynchronously.

        .. warning::

          When the user clicks a category label to triggle multiple series drilldowns,
          one ``drilldown`` event is triggered per point in the category.

        One parameter, ``event``, is passed to the JavaScript function,
        containing common event information plus certain specific properties:

          * ``category``: if a category label was clicked, this will contain its index
          * ``originalEvent``: the original browser event (typically a click) that
            triggered the drilldown
          * ``point``: the originating point
          * ``points``: if a category label was clicked, this will be an array that holds
            all points corresponding to the category
          * ``seriesOptions``: options for the new series

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drilldown

    @drilldown.setter
    def drilldown(self, value):
        self._drilldown = validators.string(value, allow_empty = False)

    @property
    def drillup(self) -> Optional[str]:
        """JavaScript callback function that fires when the user drills up from a
        drilldown series.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drillup

    @drillup.setter
    def drillup(self, value):
        self._drillup = validators.string(value, allow_empty = False)

    @property
    def drillupall(self) -> Optional[str]:
        """In a chart with multiple drilldown series, this JavaScript callback function
        fires after all the series have been drilled up.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drillupall

    @drillupall.setter
    def drillupall(self, value):
        self._drillupall = validators.string(value, allow_empty = False)

    @property
    def export_data(self) -> Optional[str]:
        """JavaScript callback function that fires while exporting data. This enables
        the modification of data rows before they are processed into their final format.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._export_data

    @export_data.setter
    def export_data(self, value):
        self._export_data = validators.string(value, allow_empty = False)

    @property
    def fullscreen_close(self) -> Optional[str]:
        """JavaScript callback function that fires when a fullscreen view is closed,
        either through a context menu item, the ``Esc`` key, or the JavaScript
        ``Chart.fullscreen.close()`` method.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fullscreen_close

    @fullscreen_close.setter
    def fullscreen_close(self, value):
        self._fullscreen_close = validators.string(value, allow_empty = False)

    @property
    def fullscreen_open(self) -> Optional[str]:
        """JavaScript callback function that fires when a fullscreen view is opened,
        either through a context menu item or the JavaScript ``Chart.fullscreen.open()``
        method.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fullscreen_open

    @fullscreen_open.setter
    def fullscreen_open(self, value):
        self._fullscreen_open = validators.string(value, allow_empty = False)

    @property
    def load(self) -> Optional[str]:
        """JavaScript callback function that fires when the chart has finished loading
        (including images, for example in point markers). One parameter, ``event``, is
        passed to the JavaScript function, containing common event information.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._load

    @load.setter
    def load(self, value):
        self._load = validators.string(value, allow_empty = False)

    @property
    def redraw(self) -> Optional[str]:
        """JavaScript callback function that fires when the chart is redrawn, either after
        a JavaScript call to ``chart.redraw()`` or after an axis, series, or point is
        modified in JavaScript with the ``redraw`` option set to ``true``.

        One parameter, ``event``, is passed to the JavaScript function, containing common
        event information.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._redraw

    @redraw.setter
    def redraw(self, value):
        self._redraw = validators.string(value, allow_empty = False)

    @property
    def selection(self) -> Optional[str]:
        """JavaScript callback function that fires when an area of the chart has been
        selected (selection is enabled by setting :class:`Chart.zoom_type`).

        One parameter, ``event``, is passed to the JavaScript function, containing common
        event information.

        .. hint::

          The default action for the selection event is to zoom the chart to the selected
          area, however this can be prevented by calling ``event.preventDefault()`` or
          returning ``false`` from your JavaScript callback function.

        .. hint::

          Information on the selected area can be found in your JavaScript function
          through ``event.xAxis`` and ``event.yAxis``, which are arrays containing the
          axes of each dimension and each axis' minimum and maximum value within the
          selected area.

          The primary axes are ``event.xAxis[0]`` and ``event.yAxis[0]``.

          Remember the unit of a datetime axis is milliseconds since 1970-01-01 00:00:00.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._selection

    @selection.setter
    def selection(self, value):
        self._selection = validators.string(value, allow_empty = False)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'add_series': as_dict.pop('addSeries', None),
            'after_print': as_dict.pop('afterPrint', None),
            'before_print': as_dict.pop('beforePrint', None),
            'click': as_dict.pop('click', None),
            'drilldown': as_dict.pop('drilldown', None),
            'drillup': as_dict.pop('drillup', None),
            'drillupall': as_dict.pop('drillupall', None),
            'export_data': as_dict.pop('exportData', None),
            'fullscreen_close': as_dict.pop('fullscreenClose', None),
            'fullscreen_open': as_dict.pop('fullscreenOpen', None),
            'load': as_dict.pop('load', None),
            'redraw': as_dict.pop('redraw', None),
            'selection': as_dict.pop('selection', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'addSeries': self.add_series,
            'afterPrint': self.after_print,
            'beforePrint': self.before_print,
            'click': self.click,
            'drilldown': self.drilldown,
            'drillup': self.drillup,
            'drillupall': self.drillupall,
            'exportData': self.export_data,
            'fullscreenClose': self.fullscreen_close,
            'fullscreenOpen': self.fullscreen_open,
            'load': self.load,
            'redraw': self.redraw,
            'selection': self.selection
        }

        return self.trim_dict(untrimmed)


class BreadcrumbEvents(HighchartsMeta):
    """Event listeners for breadcrumbs."""

    def __init__(self, **kwargs):
        self._click = None

        for attribute in dir(self):
            if attribute.startswith('_') and not attribute.startswith('__'):
                non_private_name = attribute[1:]
                setattr(self, non_private_name, kwargs.pop(non_private_name, None))

    @property
    def click(self) -> Optional[str]:
        """JavaScript callback function that fires when the user clicks on the plot
        background. One parameter, ``event``, is passed to the JavaScript function,
        containing common event information.

        .. hint::

          Information on the clicked spot can be found in your JavaScript function through
          ``event.xAxis`` and ``event.yAxis``, which are arrays containing the axes of
          each dimension and each axis' value at the clicked spot.

          The primary axes are ``event.xAxis[0]`` and ``event.yAxis[0]``.

          Remember the unit of a datetime axis is milliseconds since 1970-01-01 00:00:00.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    def click(self, value):
        self._click = validators.string(value, allow_empty = False)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'click': as_dict.pop('click', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'click': self.click
        }

        return self.trim_dict(untrimmed)


class NavigationEvents(HighchartsMeta):
    """Event listeners for the chart."""

    def __init__(self, **kwargs):
        self._close_popup = None
        self._deselect_button = None
        self._select_button = None
        self._show_popup = None

        for attribute in dir(self):
            if attribute.startswith('_') and not attribute.startswith('__'):
                non_private_name = attribute[1:]
                setattr(self, non_private_name, kwargs.pop(non_private_name, None))

    @property
    def close_popup(self) -> Optional[str]:
        """JavaScript callback function that fires when a popup should be closed, for
        example when clicking on an annotation again.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._close_popup

    @close_popup.setter
    def close_popup(self, value):
        self._close_popup = validators.string(value, allow_empty = False)

    @property
    def deselect_button(self) -> Optional[str]:
        """JavaScript callback function that fires when button state should change, for
        example after adding an annotation.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._deselect_button

    @deselect_button.setter
    def deselect_button(self, value):
        self._deselect_button = validators.string(value, allow_empty = False)

    @property
    def select_button(self) -> Optional[str]:
        """JavaScript callback function that fires on a button click.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._select_button

    @select_button.setter
    def select_button(self, value):
        self._select_button = validators.string(value, allow_empty = False)

    @property
    def show_popup(self) -> Optional[str]:
        """JavaScript callback function that fires when when selecting an annotation.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._show_popup

    @show_popup.setter
    def show_popup(self, value):
        self._show_popup = validators.string(value, allow_empty = False)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'close_popup': as_dict.pop('closePopup', None),
            'deselect_button': as_dict.pop('deselectButton', None),
            'select_button': as_dict.pop('selectButton', None),
            'show_popup': as_dict.pop('showPopup', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'closePopup': self.close_popup,
            'deselectButton': self.deselect_button,
            'selectButton': self.select_button,
            'showPopup': self.show_popup
        }

        return self.trim_dict(untrimmed)


class PointEvents(HighchartsMeta):
    """Event listeners for Points."""

    def __init__(self, **kwargs):
        self._click = None
        self._drag = None
        self._drag_start = None
        self._drop = None
        self._mouse_out = None
        self._mouse_over = None
        self._remove = None
        self._select = None
        self._unselect = None
        self._update = None

        self.click = kwargs.pop('click', None)
        self.drag = kwargs.pop('drag', None)
        self.drag_start = kwargs.pop('drag_start', None)
        self.drop = kwargs.pop('drop', None)
        self.mouse_out = kwargs.pop('mouse_out', None)
        self.mouse_over = kwargs.pop('mouse_over', None)
        self.remove = kwargs.pop('remove', None)
        self.select = kwargs.pop('select', None)
        self.unselect = kwargs.pop('unselect', None)
        self.update = kwargs.pop('update', None)

    @property
    def click(self) -> Optional[str]:
        """JavaScript function that fires when a point is clicked.

        One parameter, ``event``, is passed to the function, containing common event
        information.

        If the :meth:`Series.allow_point_select` option is ``True``, the default action
        for the point's click event is to toggle the point's select state. Returning
        ``False`` from the JavaScript event handler function cancels this action.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    def click(self, value):
        self._click = validators.string(value, allow_empty = True)

    @property
    def drag(self) -> Optional[str]:
        """JavaScript callback function that fires while dragging a point.

        The mouse event is passed in as parameter. The original data can be accessed from
        ``e.origin``, and the new point values can be accessed from ``e.newPoints``. If
        there is only a single point being updated, it can be accessed from ``e.newPoint``
        for simplicity, and its ID can be accessed from ``e.newPointId``. The this context
        is the point being dragged. To stop the default drag action, return ``false``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drag

    @drag.setter
    def drag(self, value):
        self._drag = validators.string(value, allow_empty = True)

    @property
    def drag_start(self) -> Optional[str]:
        """JavaScript callback function that fires when starting to drag a point.

        In JavaScript, the mouse event object is passed in as an argument. If a drag
        handle is used, ``e.updateProp`` is set to the data property being dragged.
        The ``this`` context is the point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drag_start

    @drag_start.setter
    def drag_start(self, value):
        self._drag_start = validators.string(value, allow_empty = True)

    @property
    def drop(self) -> Optional[str]:
        """JavaScript function that fires when a point is droped (when dragging ends).

        The mouse event is passed in as parameter. The original data can be accessed from
        ``e.origin``, and the new point values can be accessed from ``e.newPoints``. If
        there is only a single point being updated, it can be accessed from ``e.newPoint``
        for simplicity, and its ID can be accessed from ``e.newPointId``. The this context
        is the point being dragged.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drop

    @drop.setter
    def drop(self, value):
        self._drop = validators.string(value, allow_empty = True)

    @property
    def mouse_out(self) -> Optional[str]:
        """JavaScript function which fires when the mouse leaves the area close to the
        point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mouse_out

    @mouse_out.setter
    def mouse_out(self, value):
        self._mouse_out = validators.string(value, allow_empty = True)

    @property
    def mouse_over(self) -> Optional[str]:
        """JavaScript function which fires when the mouse enters the area close to the
        point. One parameter, ``event``, is passed to the function, containing common
        event information.

        Returning ``false`` cancels the default behavior, which is to show a tooltip for
        the point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mouse_over

    @mouse_over.setter
    def mouse_over(self, value):
        self._mouse_over = validators.string(value, allow_empty = True)

    @property
    def remove(self) -> Optional[str]:
        """JavaScript function which fires when the point is removed using the
        (JavaScript) ``.remove()`` method.

        One parameter, ``event``, is passed to the function. Returning ``false`` cancels
        the operation.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._remove

    @remove.setter
    def remove(self, value):
        self._remove = validators.string(value, allow_empty = True)

    @property
    def select(self) -> Optional[str]:
        """JavaScript function which fires when the point is selected either
        programmatically or following a click on the point.

        One parameter, ``event``, is passed to the function. Returning ``false`` cancels
        the operation.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._select

    @select.setter
    def select(self, value):
        self._select = validators.string(value, allow_empty = True)

    @property
    def unselect(self) -> Optional[str]:
        """JavaScript function that fires when the point is unselected either
        programmatically or following a click on the point.

        One parameter, ``event``, is passed to the function. Returning ``false`` cancels
        the operation.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._unselect

    @unselect.setter
    def unselect(self, value):
        self._unselect = validators.string(value, allow_empty = True)

    @property
    def update(self) -> Optional[str]:
        """JavaScript function that fires when the point is updated programmatically
        through the (JavaScript) ``.update()`` method.

        One parameter, ``event``, is passed to the function. The new point options can be
        accessed through ``event.options``. Returning ``false`` cancels the operation.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._update

    @update.setter
    def update(self, value):
        self._update = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'click': as_dict.pop('click', None),
            'drag': as_dict.pop('drag', None),
            'drag_start': as_dict.pop('dragStart', None),
            'drop': as_dict.pop('drop', None),
            'mouse_out': as_dict.pop('mouseOut', None),
            'mouse_over': as_dict.pop('mouseOver', None),
            'remove': as_dict.pop('remove', None),
            'select': as_dict.pop('select', None),
            'unselect': as_dict.pop('unselect', None),
            'update': as_dict.pop('update', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'click': self.click,
            'drag': self.drag,
            'dragStart': self.drag_start,
            'drop': self.drop,
            'mouseOut': self.mouse_out,
            'mouseOver': self.mouse_over,
            'remove': self.remove,
            'select': self.select,
            'unselect': self.unselect,
            'update': self.update
        }

        return self.trim_dict(untrimmed)


class SeriesEvents(HighchartsMeta):
    """Event listeners for Series."""

    def __init__(self, **kwargs):
        self._after_animate = None
        self._checkbox_click = None
        self._click = None
        self._hide = None
        self._legend_item_click = None
        self._mouse_out = None
        self._mouse_over = None
        self._show = None

        self.after_animate = kwargs.pop('after_animate', None)
        self.checkbox_click = kwargs.pop('checkbox_click', None)
        self.click = kwargs.pop('click', None)
        self.hide = kwargs.pop('hide', None)
        self.legend_item_click = kwargs.pop('legend_item_click', None)
        self.mouse_out = kwargs.pop('mouse_out', None)
        self.mouse_over = kwargs.pop('mouse_over', None)
        self.show = kwargs.pop('show', None)

    @property
    def after_animate(self) -> Optional[str]:
        """JavaScript function that fires after the series has finished its initial
        animation, or if animation is disabled, immediately as the series is displayed.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._after_animate

    @after_animate.setter
    def after_animate(self, value):
        self._after_animate = validators.string(value, allow_empty = True)

    @property
    def checkbox_click(self) -> Optional[str]:
        """JavaScript function that fires when the checkbox next to the series' name in
        the legend is clicked.

        One parameter, ``event``, is passed to the (JavaScript) function. The state of the
        checkbox is found by ``event.checked``. The checked item is found by
        ``event.item``. Return ``false`` to prevent the default action which is to toggle
        the select state of the series.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._checkbox_click

    @checkbox_click.setter
    def checkbox_click(self, value):
        self._checkbox_click = validators.string(value, allow_empty = True)

    @property
    def click(self) -> Optional[str]:
        """JavaScript function that fires when when the series is clicked.

        One parameter, ``event``, is passed to the (JavaScript) function, containing
        common event information. Additionally, ``event.point`` holds a pointer to the
        nearest point on the graph.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    def click(self, value):
        self._click = validators.string(value, allow_empty = True)

    @property
    def hide(self) -> Optional[str]:
        """JavaScript function that fires when the series is hidden after chart generation
        time, either by clicking the legend item or by calling (in JavaScript)
        ``.hide()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._hide

    @hide.setter
    def hide(self, value):
        self._hide = validators.string(value, allow_empty = True)

    @property
    def legend_item_click(self) -> Optional[str]:
        """JavaScript function that fires when the legend item belonging to the series is
        clicked.

        One parameter, ``event``, is passed to the (JavaScript) function. The default
        action is to toggle the visibility of the series. This can be prevented by
        returning ``false`` or calling (in JavaScript) ``event.preventDefault()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._legend_item_click

    @legend_item_click.setter
    def legend_item_click(self, value):
        self._legend_item_click = validators.string(value, allow_empty = True)

    @property
    def mouse_out(self) -> Optional[str]:
        """JavaScript function which fires when the mouse leaves the graph.

        One parameter, ``event``, is passed to the (JavaScript) function, containing
        common event information. If the ``stickyTracking`` option is ``true``,
        the ``mouse_out`` event doesn't happen before the mouse enters another graph or
        leaves the plot area.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mouse_out

    @mouse_out.setter
    def mouse_out(self, value):
        self._mouse_out = validators.string(value, allow_empty = True)

    @property
    def mouse_over(self) -> Optional[str]:
        """JavaScript function which fires when the mouse enters the graph.

        One parameter, ``event``, is passed to the function, containing common event
        information.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mouse_over

    @mouse_over.setter
    def mouse_over(self, value):
        self._mouse_over = validators.string(value, allow_empty = True)

    @property
    def show(self) -> Optional[str]:
        """JavaScript function which fires when the series is shown after chart generation
        time, either by clicking the legend item or by calling (in JavaScript)
        ``.show()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._show

    @show.setter
    def show(self, value):
        self._show = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'after_animate': as_dict.pop('afterAnimate', None),
            'checkbox_click': as_dict.pop('checkboxClick', None),
            'click': as_dict.pop('click', None),
            'hide': as_dict.pop('hide', None),
            'legend_item_click': as_dict.pop('legendItemClick', None),
            'mouse_out': as_dict.pop('mouseOut', None),
            'mouse_over': as_dict.pop('mouseOver', None),
            'show': as_dict.pop('show', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'afterAnimate': self.after_animate,
            'checkboxClick': self.checkbox_click,
            'click': self.click,
            'hide': self.hide,
            'legendItemClick': self.legend_item_click,
            'mouseOut': self.mouse_out,
            'mouseOver': self.mouse_over,
            'show': self.show
        }

        return self.trim_dict(untrimmed)


class ClusterEvents(HighchartsMeta):
    """General event handlers for marker clusters."""

    def __init__(self, **kwargs):
        self._drill_to_cluster = None

        self.drill_to_cluster = kwargs.pop('drill_to_cluster', None)

    @property
    def drill_to_cluster(self) -> Optional[str]:
        """JavaScript callback function that fires when the cluster point is clicked and
        :meth:`Cluster.drill_to_cluster` is ``True``.

        One parameter, ``event``, is passed to the function. The default action is to zoom
        to the cluster points range. This can be prevented by calling (in JavaScript)
        ``event.preventDefault()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drill_to_cluster

    @drill_to_cluster.setter
    def drill_to_cluster(self, value):
        self._drill_to_cluster = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        return cls({
            'drill_to_cluster': as_dict.pop('drillToCluster', None)
        })

    def to_dict(self) -> Optional[dict]:
        return self.trim_dict({
            'drillToCluster': self.drill_to_cluster
        })


class AxisEvents(HighchartsMeta):
    """Event listeners for axes."""

    def __init__(self, **kwargs):
        self._after_breaks = None
        self._after_set_extremes = None
        self._point_break = None
        self._point_in_break = None
        self._set_extremes = None

        self.after_breaks = kwargs.pop('after_breaks', None)
        self.after_set_extremes = kwargs.pop('after_set_extremes', None)
        self.point_breaks = kwargs.pop('point_breaks', None)
        self.point_in_break = kwargs.pop('point_in_break', None)
        self.set_extremes = kwargs.pop('set_extremes', None)

    @property
    def after_breaks(self) -> Optional[CallbackFunction]:
        """A JavaScript event function fired after breaks have rendered. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._after_breaks

    @after_breaks.setter
    @class_sensitive(CallbackFunction)
    def after_breaks(self, value):
        self._after_breaks = value

    @property
    def after_set_extremes(self) -> Optional[CallbackFunction]:
        """As opposed to :meth:`AxisEvent.set_extremes`, this JavaScript event fires after
        the final min and max values are computed and corrected for
        :meth:`GenericAxis.min_range`. Defaults to :obj:`None <python:None>`.

        Fires when the minimum and maximum is set for the axis, either by calling the
        (JavaScript) ``.setExtremes()`` method or by selecting an area in the chart. One
        parameter, ``event``, is passed to the function, containing common event
        information.

        The new user-set minimum and maximum values can be found (in JavaScript) by
        ``event.min`` and ``event.max``. These reflect the axis minimum and maximum in
        axis values. The actual data extremes are found in ``event.dataMin`` and
        ``event.dataMax``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._after_set_extremes

    @after_set_extremes.setter
    @class_sensitive(CallbackFunction)
    def after_set_extremes(self, value):
        self._after_set_extremes = value

    @property
    def point_break(self) -> Optional[CallbackFunction]:
        """A JavaScript event fired when a break from this axis occurs on a point.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._point_break

    @point_break.setter
    @class_sensitive(CallbackFunction)
    def point_break(self, value):
        self._point_break = value

    @property
    def point_in_break(self) -> Optional[CallbackFunction]:
        """A JavaScript event fired when a point falls inside a break from this axis.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._point_in_break

    @point_in_break.setter
    @class_sensitive(CallbackFunction)
    def point_in_break(self, value):
        self._point_break = value

    @property
    def set_extremes(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the minimum and maximum is set for the
        axis, either by calling the (JavaScript) ``.setExtremes()`` method or by selecting
        an area in the chart.

        One parameter, ``event``, is passed to the function, containing common event
        information.

        The new user-set minimum and maximum values can be found by ``event.min`` and
        ``event.max``. These reflect the axis minimum and maximum in data values. When an
        axis is zoomed all the way out from the "Reset zoom" button, ``event.min`` and
        ``event.max`` are ``null``, and the new extremes are set based on
        ``this.dataMin`` and ``this.dataMax``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._set_extremes

    @set_extremes.setter
    @class_sensitive(CallbackFunction)
    def set_extremes(self, value):
        self._set_extremes = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'after_breaks': as_dict.pop('after_breaks', None),
            'after_set_extremes': as_dict.pop('after_set_extremes', None),
            'point_break': as_dict.pop('point_break', None),
            'point_in_break': as_dict.pop('point_in_break', None),
            'set_extremes': as_dict.pop('set_extremes', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'afterBreaks': self.after_breaks,
            'afterSetExtremes': self.after_set_extremes,
            'pointBreak': self.point_break,
            'pointInBreak': self.point_in_break,
            'setExtremes': self.set_extremes
        }

        return self.trim_dict(untrimmed)


class MouseEvents(HighchartsMeta):
    """Collection of basic / standard event handlers for mouse interactions."""

    def __init__(self, **kwargs):
        self._click = None
        self._mousemove = None
        self._mouseout = None
        self._mouseover = None

        self.click = kwargs.pop('click', None)
        self.mousemove = kwargs.pop('mousemove', None)
        self.mouseout = kwargs.pop('mouseout', None)
        self.mouseover = kwargs.pop('mouseover', None)

    @property
    def click(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the user clicks on the plot
        band. One parameter, ``event``, is passed to the JavaScript function,
        containing common event information. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    @class_sensitive(CallbackFunction)
    def click(self, value):
        self._click = value

    @property
    def mousemove(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires on the mousemove event within the plot
        band. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._mousemove

    @mousemove.setter
    @class_sensitive(CallbackFunction)
    def mousemove(self, value):
        self._mousemove = value

    @property
    def mouseout(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the mouse moves away from the
        corner of the plot band. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._mouseout

    @mouseout.setter
    @class_sensitive(CallbackFunction)
    def mouseout(self, value):
        self._mouseout = value

    @property
    def mouseover(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the user moves their mouse over
        the plot band. One parameter, ``event``, is passed to the JavaScript function,
        containing common event information. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._mouseover

    @mouseover.setter
    @class_sensitive(CallbackFunction)
    def mouseover(self, value):
        self._mouseover = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'click': as_dict.pop('click', None),
            'mousemove': as_dict.pop('mousemove', None),
            'mouseout': as_dict.pop('mouseout', None),
            'mouseover': as_dict.pop('mouseover', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'click': self.click,
            'mousemove': self.mousemove,
            'mouseout': self.mouseout,
            'mouseover': self.mouseover
        }

        return self.trim_dict(untrimmed)
