from typing import Optional

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


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
