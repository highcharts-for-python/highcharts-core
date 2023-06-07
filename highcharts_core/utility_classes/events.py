from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


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
                setattr(self, non_private_name, kwargs.get(non_private_name, None))

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'chart.events'

    @property
    def add_series(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when a series is added to the chart
        after load time, using the JavaScript ``.addSeries()`` method.

        One parameter, ``event``, is passed to the JavaScript function, containing common
        event information. Through ``event.options`` you can access the series options
        that were passed to the ``.addSeries()`` method.

        Returning ``false`` prevents the series from being added.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._add_series

    @add_series.setter
    @class_sensitive(CallbackFunction)
    def add_series(self, value):
        self._add_series = value

    @property
    def after_print(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires after a chart has been printed through
        the context menu or the ``Chart.print()`` JavaScript method.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._after_print

    @after_print.setter
    @class_sensitive(CallbackFunction)
    def after_print(self, value):
        self._after_print = value

    @property
    def before_print(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires before a chart is printed through
        the context menu or the ``Chart.print()`` JavaScript method.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._before_print

    @before_print.setter
    @class_sensitive(CallbackFunction)
    def before_print(self, value):
        self._before_print = value

    @property
    def click(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the user clicks on the plot
        background. One parameter, ``event``, is passed to the JavaScript function,
        containing common event information.

        .. hint::

          Information on the clicked spot can be found in your JavaScript function through
          ``event.xAxis`` and ``event.yAxis``, which are arrays containing the axes of
          each dimension and each axis' value at the clicked spot.

          The primary axes are ``event.xAxis[0]`` and ``event.yAxis[0]``.

          Remember the unit of a datetime axis is milliseconds since 1970-01-01 00:00:00.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    @class_sensitive(CallbackFunction)
    def click(self, value):
        self._click = value

    @property
    def drilldown(self) -> Optional[CallbackFunction]:
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

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._drilldown

    @drilldown.setter
    @class_sensitive(CallbackFunction)
    def drilldown(self, value):
        self._drilldown = value

    @property
    def drillup(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the user drills up from a
        drilldown series.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._drillup

    @drillup.setter
    @class_sensitive(CallbackFunction)
    def drillup(self, value):
        self._drillup = value

    @property
    def drillupall(self) -> Optional[CallbackFunction]:
        """In a chart with multiple drilldown series, this JavaScript callback function
        fires after all the series have been drilled up.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._drillupall

    @drillupall.setter
    @class_sensitive(CallbackFunction)
    def drillupall(self, value):
        self._drillupall = value

    @property
    def export_data(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires while exporting data. This enables
        the modification of data rows before they are processed into their final format.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._export_data

    @export_data.setter
    @class_sensitive(CallbackFunction)
    def export_data(self, value):
        self._export_data = value

    @property
    def fullscreen_close(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when a fullscreen view is closed,
        either through a context menu item, the ``Esc`` key, or the JavaScript
        ``Chart.fullscreen.close()`` method.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._fullscreen_close

    @fullscreen_close.setter
    @class_sensitive(CallbackFunction)
    def fullscreen_close(self, value):
        self._fullscreen_close = value

    @property
    def fullscreen_open(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when a fullscreen view is opened,
        either through a context menu item or the JavaScript ``Chart.fullscreen.open()``
        method.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._fullscreen_open

    @fullscreen_open.setter
    @class_sensitive(CallbackFunction)
    def fullscreen_open(self, value):
        self._fullscreen_open = value

    @property
    def load(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the chart has finished loading
        (including images, for example in point markers). One parameter, ``event``, is
        passed to the JavaScript function, containing common event information.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._load

    @load.setter
    @class_sensitive(CallbackFunction)
    def load(self, value):
        self._load = value

    @property
    def redraw(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the chart is redrawn, either after
        a JavaScript call to ``chart.redraw()`` or after an axis, series, or point is
        modified in JavaScript with the ``redraw`` option set to ``true``.

        One parameter, ``event``, is passed to the JavaScript function, containing common
        event information.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._redraw

    @redraw.setter
    @class_sensitive(CallbackFunction)
    def redraw(self, value):
        self._redraw = value

    @property
    def selection(self) -> Optional[CallbackFunction]:
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

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._selection

    @selection.setter
    @class_sensitive(CallbackFunction)
    def selection(self, value):
        self._selection = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'add_series': as_dict.get('addSeries', None),
            'after_print': as_dict.get('afterPrint', None),
            'before_print': as_dict.get('beforePrint', None),
            'click': as_dict.get('click', None),
            'drilldown': as_dict.get('drilldown', None),
            'drillup': as_dict.get('drillup', None),
            'drillupall': as_dict.get('drillupall', None),
            'export_data': as_dict.get('exportData', None),
            'fullscreen_close': as_dict.get('fullscreenClose', None),
            'fullscreen_open': as_dict.get('fullscreenOpen', None),
            'load': as_dict.get('load', None),
            'redraw': as_dict.get('redraw', None),
            'selection': as_dict.get('selection', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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

        return untrimmed


class BreadcrumbEvents(HighchartsMeta):
    """Event listeners for breadcrumbs."""

    def __init__(self, **kwargs):
        self._click = None

        for attribute in dir(self):
            if attribute.startswith('_') and not attribute.startswith('__'):
                non_private_name = attribute[1:]
                setattr(self, non_private_name, kwargs.get(non_private_name, None))

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'breadcrumb.events'

    @property
    def click(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the user clicks on the plot
        background. One parameter, ``event``, is passed to the JavaScript function,
        containing common event information.

        .. hint::

          Information on the clicked spot can be found in your JavaScript function through
          ``event.xAxis`` and ``event.yAxis``, which are arrays containing the axes of
          each dimension and each axis' value at the clicked spot.

          The primary axes are ``event.xAxis[0]`` and ``event.yAxis[0]``.

          Remember the unit of a datetime axis is milliseconds since 1970-01-01 00:00:00.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    @class_sensitive(CallbackFunction)
    def click(self, value):
        self._click = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'click': as_dict.get('click', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'click': self.click
        }

        return untrimmed


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
                setattr(self, non_private_name, kwargs.get(non_private_name, None))

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'navigation.events'

    @property
    def close_popup(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when a popup should be closed, for
        example when clicking on an annotation again.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._close_popup

    @close_popup.setter
    @class_sensitive(CallbackFunction)
    def close_popup(self, value):
        self._close_popup = value

    @property
    def deselect_button(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when button state should change, for
        example after adding an annotation.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._deselect_button

    @deselect_button.setter
    @class_sensitive(CallbackFunction)
    def deselect_button(self, value):
        self._deselect_button = value

    @property
    def select_button(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires on a button click.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._select_button

    @select_button.setter
    @class_sensitive(CallbackFunction)
    def select_button(self, value):
        self._select_button = value

    @property
    def show_popup(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when when selecting an annotation.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._show_popup

    @show_popup.setter
    @class_sensitive(CallbackFunction)
    def show_popup(self, value):
        self._show_popup = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'close_popup': as_dict.get('closePopup', None),
            'deselect_button': as_dict.get('deselectButton', None),
            'select_button': as_dict.get('selectButton', None),
            'show_popup': as_dict.get('showPopup', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'closePopup': self.close_popup,
            'deselectButton': self.deselect_button,
            'selectButton': self.select_button,
            'showPopup': self.show_popup
        }

        return untrimmed


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

        self.click = kwargs.get('click', None)
        self.drag = kwargs.get('drag', None)
        self.drag_start = kwargs.get('drag_start', None)
        self.drop = kwargs.get('drop', None)
        self.mouse_out = kwargs.get('mouse_out', None)
        self.mouse_over = kwargs.get('mouse_over', None)
        self.remove = kwargs.get('remove', None)
        self.select = kwargs.get('select', None)
        self.unselect = kwargs.get('unselect', None)
        self.update = kwargs.get('update', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.series.point.events'

    @property
    def click(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when a point is clicked.

        One parameter, ``event``, is passed to the function, containing common event
        information.

        If the :meth:`Series.allow_point_select` option is ``True``, the default action
        for the point's click event is to toggle the point's select state. Returning
        ``False`` from the JavaScript event handler function cancels this action.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    @class_sensitive(CallbackFunction)
    def click(self, value):
        self._click = value

    @property
    def drag(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires while dragging a point.

        The mouse event is passed in as parameter. The original data can be accessed from
        ``e.origin``, and the new point values can be accessed from ``e.newPoints``. If
        there is only a single point being updated, it can be accessed from ``e.newPoint``
        for simplicity, and its ID can be accessed from ``e.newPointId``. The this context
        is the point being dragged. To stop the default drag action, return ``false``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._drag

    @drag.setter
    @class_sensitive(CallbackFunction)
    def drag(self, value):
        self._drag = value

    @property
    def drag_start(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when starting to drag a point.

        In JavaScript, the mouse event object is passed in as an argument. If a drag
        handle is used, ``e.updateProp`` is set to the data property being dragged.
        The ``this`` context is the point.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._drag_start

    @drag_start.setter
    @class_sensitive(CallbackFunction)
    def drag_start(self, value):
        self._drag_start = value

    @property
    def drop(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when a point is droped (when dragging ends).

        The mouse event is passed in as parameter. The original data can be accessed from
        ``e.origin``, and the new point values can be accessed from ``e.newPoints``. If
        there is only a single point being updated, it can be accessed from ``e.newPoint``
        for simplicity, and its ID can be accessed from ``e.newPointId``. The this context
        is the point being dragged.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._drop

    @drop.setter
    @class_sensitive(CallbackFunction)
    def drop(self, value):
        self._drop = value

    @property
    def mouse_out(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the mouse leaves the area close to the
        point.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._mouse_out

    @mouse_out.setter
    @class_sensitive(CallbackFunction)
    def mouse_out(self, value):
        self._mouse_out = value

    @property
    def mouse_over(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the mouse enters the area close to the
        point. One parameter, ``event``, is passed to the function, containing common
        event information.

        Returning ``false`` cancels the default behavior, which is to show a tooltip for
        the point.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._mouse_over

    @mouse_over.setter
    @class_sensitive(CallbackFunction)
    def mouse_over(self, value):
        self._mouse_over = value

    @property
    def remove(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the point is removed using the
        (JavaScript) ``.remove()`` method.

        One parameter, ``event``, is passed to the function. Returning ``false`` cancels
        the operation.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._remove

    @remove.setter
    @class_sensitive(CallbackFunction)
    def remove(self, value):
        self._remove = value

    @property
    def select(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the point is selected either
        programmatically or following a click on the point.

        One parameter, ``event``, is passed to the function. Returning ``false`` cancels
        the operation.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._select

    @select.setter
    @class_sensitive(CallbackFunction)
    def select(self, value):
        self._select = value

    @property
    def unselect(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when the point is unselected either
        programmatically or following a click on the point.

        One parameter, ``event``, is passed to the function. Returning ``false`` cancels
        the operation.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._unselect

    @unselect.setter
    @class_sensitive(CallbackFunction)
    def unselect(self, value):
        self._unselect = value

    @property
    def update(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when the point is updated programmatically
        through the (JavaScript) ``.update()`` method.

        One parameter, ``event``, is passed to the function. The new point options can be
        accessed through ``event.options``. Returning ``false`` cancels the operation.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._update

    @update.setter
    def update(self, value):
        self._update = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'click': as_dict.get('click', None),
            'drag': as_dict.get('drag', None),
            'drag_start': as_dict.get('dragStart', None),
            'drop': as_dict.get('drop', None),
            'mouse_out': as_dict.get('mouseOut', None),
            'mouse_over': as_dict.get('mouseOver', None),
            'remove': as_dict.get('remove', None),
            'select': as_dict.get('select', None),
            'unselect': as_dict.get('unselect', None),
            'update': as_dict.get('update', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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

        return untrimmed


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

        self.after_animate = kwargs.get('after_animate', None)
        self.checkbox_click = kwargs.get('checkbox_click', None)
        self.click = kwargs.get('click', None)
        self.hide = kwargs.get('hide', None)
        self.legend_item_click = kwargs.get('legend_item_click', None)
        self.mouse_out = kwargs.get('mouse_out', None)
        self.mouse_over = kwargs.get('mouse_over', None)
        self.show = kwargs.get('show', None)

    @property
    def after_animate(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires after the series has finished its initial
        animation, or if animation is disabled, immediately as the series is displayed.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._after_animate

    @after_animate.setter
    @class_sensitive(CallbackFunction)
    def after_animate(self, value):
        self._after_animate = value

    @property
    def checkbox_click(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when the checkbox next to the series' name in
        the legend is clicked.

        One parameter, ``event``, is passed to the (JavaScript) function. The state of the
        checkbox is found by ``event.checked``. The checked item is found by
        ``event.item``. Return ``false`` to prevent the default action which is to toggle
        the select state of the series.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._checkbox_click

    @checkbox_click.setter
    @class_sensitive(CallbackFunction)
    def checkbox_click(self, value):
        self._checkbox_click = value

    @property
    def click(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when when the series is clicked.

        One parameter, ``event``, is passed to the (JavaScript) function, containing
        common event information. Additionally, ``event.point`` holds a pointer to the
        nearest point on the graph.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    @class_sensitive(CallbackFunction)
    def click(self, value):
        self._click = value

    @property
    def hide(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when the series is hidden after chart generation
        time, either by clicking the legend item or by calling (in JavaScript)
        ``.hide()``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._hide

    @hide.setter
    @class_sensitive(CallbackFunction)
    def hide(self, value):
        self._hide = value

    @property
    def legend_item_click(self) -> Optional[CallbackFunction]:
        """JavaScript function that fires when the legend item belonging to the series is
        clicked.

        One parameter, ``event``, is passed to the (JavaScript) function. The default
        action is to toggle the visibility of the series. This can be prevented by
        returning ``false`` or calling (in JavaScript) ``event.preventDefault()``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._legend_item_click

    @legend_item_click.setter
    @class_sensitive(CallbackFunction)
    def legend_item_click(self, value):
        self._legend_item_click = value

    @property
    def mouse_out(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the mouse leaves the graph.

        One parameter, ``event``, is passed to the (JavaScript) function, containing
        common event information. If the ``stickyTracking`` option is ``true``,
        the ``mouse_out`` event doesn't happen before the mouse enters another graph or
        leaves the plot area.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._mouse_out

    @mouse_out.setter
    @class_sensitive(CallbackFunction)
    def mouse_out(self, value):
        self._mouse_out = value

    @property
    def mouse_over(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the mouse enters the graph.

        One parameter, ``event``, is passed to the function, containing common event
        information.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._mouse_over

    @mouse_over.setter
    @class_sensitive(CallbackFunction)
    def mouse_over(self, value):
        self._mouse_over = value

    @property
    def show(self) -> Optional[CallbackFunction]:
        """JavaScript function which fires when the series is shown after chart generation
        time, either by clicking the legend item or by calling (in JavaScript)
        ``.show()``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._show

    @show.setter
    @class_sensitive(CallbackFunction)
    def show(self, value):
        self._show = value

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
            'show': as_dict.get('show', None)
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
            'show': self.show
        }

        return untrimmed


class SimulationEvents(SeriesEvents):
    """Event listeners for series that involve simulation / layout.
    
    .. versionadded:: Highcharts Core for Python v.1.1.0 / Highcharts Core (JS) v.11.0.0
    
    """
    
    def __init__(self, **kwargs):
        self._after_simulation = None
        
        self.after_simulation = kwargs.get('after_simulation', None)
        
        super().__init__(**kwargs)
        
    @property
    def after_simulation(self) -> Optional[CallbackFunction]:
        """Event which fires after the simulation is ended and the layout is stable.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._after_simulation

    @after_simulation.setter
    @class_sensitive(CallbackFunction)
    def after_simulation(self, value):
        self._after_simulation = value

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
            
            'after_simulation': as_dict.get('afterSimulation', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'afterSimulation': self.after_simulation,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
    

class ClusterEvents(HighchartsMeta):
    """General event handlers for marker clusters."""

    def __init__(self, **kwargs):
        self._drill_to_cluster = None

        self.drill_to_cluster = kwargs.get('drill_to_cluster', None)

    @property
    def drill_to_cluster(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the cluster point is clicked and
        :meth:`Cluster.drill_to_cluster` is ``True``.

        One parameter, ``event``, is passed to the function. The default action is to zoom
        to the cluster points range. This can be prevented by calling (in JavaScript)
        ``event.preventDefault()``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._drill_to_cluster

    @drill_to_cluster.setter
    @class_sensitive(CallbackFunction)
    def drill_to_cluster(self, value):
        self._drill_to_cluster = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return {
            'drill_to_cluster': as_dict.get('drillToCluster', None)
        }

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'drillToCluster': self.drill_to_cluster
        }

        return untrimmed


class AxisEvents(HighchartsMeta):
    """Event listeners for axes."""

    def __init__(self, **kwargs):
        self._after_breaks = None
        self._after_set_extremes = None
        self._point_break = None
        self._point_in_break = None
        self._set_extremes = None

        self.after_breaks = kwargs.get('after_breaks', None)
        self.after_set_extremes = kwargs.get('after_set_extremes', None)
        self.point_break = kwargs.get('point_break', None)
        self.point_in_break = kwargs.get('point_in_break', None)
        self.set_extremes = kwargs.get('set_extremes', None)

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
        self._point_in_break = value

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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'after_breaks': as_dict.get('afterBreaks', None),
            'after_set_extremes': as_dict.get('afterSetExtremes', None),
            'point_break': as_dict.get('pointBreak', None),
            'point_in_break': as_dict.get('pointInBreak', None),
            'set_extremes': as_dict.get('setExtremes', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'afterBreaks': self.after_breaks,
            'afterSetExtremes': self.after_set_extremes,
            'pointBreak': self.point_break,
            'pointInBreak': self.point_in_break,
            'setExtremes': self.set_extremes
        }

        return untrimmed


class MouseEvents(HighchartsMeta):
    """Collection of basic / standard event handlers for mouse interactions."""

    def __init__(self, **kwargs):
        self._click = None
        self._mousemove = None
        self._mouseout = None
        self._mouseover = None

        self.click = kwargs.get('click', None)
        self.mousemove = kwargs.get('mousemove', None)
        self.mouseout = kwargs.get('mouseout', None)
        self.mouseover = kwargs.get('mouseover', None)

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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'click': as_dict.get('click', None),
            'mousemove': as_dict.get('mousemove', None),
            'mouseout': as_dict.get('mouseout', None),
            'mouseover': as_dict.get('mouseover', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'click': self.click,
            'mousemove': self.mousemove,
            'mouseout': self.mouseout,
            'mouseover': self.mouseover
        }

        return untrimmed


class SonificationEvents(HighchartsMeta):
    """Event handlers for sonification."""
    
    def __init__(self, **kwargs):
        self._after_update = None
        self._before_play = None
        self._before_update = None
        self._on_boundary_hit = None
        self._on_end = None
        self._on_play = None
        self._on_series_end = None
        self._on_series_start = None
        self._on_stop = None
        
        self.after_update = kwargs.get('after_update', None)
        self.before_play = kwargs.get('before_play', None)
        self.before_update = kwargs.get('before_update', None)
        self.on_boundary_hit = kwargs.get('on_boundary_hit', None)
        self.on_end = kwargs.get('on_end', None)
        self.on_play = kwargs.get('on_play', None)
        self.on_series_end = kwargs.get('on_series_end', None)
        self.on_series_start = kwargs.get('on_series_start', None)
        self.on_stop = kwargs.get('on_stop', None)

    @property
    def after_update(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called *after* updating the
        sonification.
        
        A context object is passed to the function, with properties ``chart`` and ``timeline``.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._after_update
    
    @after_update.setter
    @class_sensitive(CallbackFunction)
    def after_update(self, value):
        self._after_update = value

    @property
    def before_play(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called immediately when playback is requested.
        
        A context object is passed to the function, with properties ``chart`` and ``timeline``.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._before_play
    
    @before_play.setter
    @class_sensitive(CallbackFunction)
    def before_play(self, value):
        self._before_play = value

    @property
    def before_update(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called *before* updating the
        sonification.
        
        A context object is passed to the function, with properties ``chart`` and ``timeline``.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._before_update
    
    @before_update.setter
    @class_sensitive(CallbackFunction)
    def before_update(self, value):
        self._before_update = value

    @property
    def on_boundary_hit(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called when attempting to play an adjacent point
        or series, and there is none found. By defualt, a percussive sound is played.
        
        A context object is passed to the function, with properties ``chart``, ``timeline``, and ``attemptedNext``. The
        ``attemptedNext`` property is a boolean value that is ``true`` if the boundary hit was from trying to play the 
        next series/point, and ``false`` if it was from trying to play the previous.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._on_boundary_hit
    
    @on_boundary_hit.setter
    @class_sensitive(CallbackFunction)
    def on_boundary_hit(self, value):
        self._on_boundary_hit = value

    @property
    def on_end(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called when playback is completed.
        
        A context object is passed to the function, with properties ``chart``, ``timeline``, and ``pointsPlayed`` where
        ``pointsPlayed`` is an array of ``Point`` objects referencing data points related to the audio events played.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._on_end
    
    @on_end.setter
    @class_sensitive(CallbackFunction)
    def on_end(self, value):
        self._on_end = value

    @property
    def on_play(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called on play.
        
        A context object is passed to the function, with properties ``chart`` and ``timeline``.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._on_play
    
    @on_play.setter
    @class_sensitive(CallbackFunction)
    def on_play(self, value):
        self._on_play = value

    @property
    def on_series_end(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called when finished playing a series.
        
        A context object is passed to the function, with properties ``series`` and ``timeline``.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._on_series_end
    
    @on_series_end.setter
    @class_sensitive(CallbackFunction)
    def on_series_end(self, value):
        self._on_series_end = value

    @property
    def on_series_start(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called when starting to play a series.
        
        A context object is passed to the function, with properties ``series`` and ``timeline``.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._on_series_start
    
    @on_series_start.setter
    @class_sensitive(CallbackFunction)
    def on_series_start(self, value):
        self._on_series_start = value

    @property
    def on_stop(self) -> Optional[CallbackFunction]:
        """Event (Javascript) :term:`callback function` that is called on pause, cancel, or if playback is
        completed.
        
        A context object is passed to the function, with properties ``chart``, ``timeline``, and ``pointsPlayed`` where
        ``pointsPlayed`` is an array of ``Point`` objects referencing data points related to the audio events played.
        
        :rtype: :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`
        """
        return self._on_stop
    
    @on_stop.setter
    @class_sensitive(CallbackFunction)
    def on_stop(self, value):
        self._on_stop = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'after_update': as_dict.get('afterUpdate', None),
            'before_play': as_dict.get('beforePlay', None),
            'before_update': as_dict.get('beforeUpdate', None),
            'on_boundary_hit': as_dict.get('onBoundaryHit', None),
            'on_end': as_dict.get('onEnd', None),
            'on_play': as_dict.get('onPlay', None),
            'on_series_end': as_dict.get('onSeriesEnd', None),
            'on_series_start': as_dict.get('onSeriesStart', None),
            'on_stop': as_dict.get('onStop', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'afterUpdate': self.after_update,
            'beforePlay': self.before_play,
            'beforeUpdate': self.before_update,
            'onBoundaryHit': self.on_boundary_hit,
            'onEnd': self.on_end,
            'onPlay': self.on_play,
            'onSeriesEnd': self.on_series_end,
            'onSeriesStart': self.on_series_start,
            'onStop': self.on_stop,
        }

        return untrimmed
