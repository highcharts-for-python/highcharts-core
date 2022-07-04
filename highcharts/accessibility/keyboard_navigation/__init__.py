from typing import Optional

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta
from highcharts.decorators import class_sensitive
from highcharts.keyboard_navigation.focus_border import FocusBorder
from highcharts.keyboard_navigation.series_navigation import SeriesNavigation


class KeyboardNavigation(HighchartsMeta):
    """Options for Keyboard Navigation."""

    def __init__(self, **kwargs):
        self._enabled = True
        self._focus_border = None
        self._order = None
        self._series_navigation = None,
        self._wrap_around = True

        self.enabled = kwargs.pop('enabled', True)
        self.focus_border = kwargs.pop('focus_border', None)
        self.order = kwargs.pop('order', None)
        self.series_navigation = kwargs.pop('series_navigation', None)
        self.wrap_around = kwargs.pop('wrap_around', True)

    @property
    def enabled(self) -> bool:
        """Enable keyboard navigation for the chart. Defaults to ``True``.

        :returns: Flag indicating whether keyboard navigation is enabled for the chart.
        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @property
    def focus_border(self) -> Optional[FocusBorder]:
        """Options for the focus border drawn around elements while navigating through
        them.

        :returns: Configuration of the focus border to be drawn around elements while
          navigating through them using the keyboard.
        :rtype: :class:`FocusBorder` or :obj:`None <python:None>`
        """
        return self._focus_border

    @focus_border.setter
    @class_sensitive(FocusBorder)
    def focus_border(self, value):
        self._focus_border = value

    @property
    def order(self):
        """Order of tab navigation in the chart.

        Determines which elements are tabbed to first. Available elements are:
          * ``'series'``
          * ``'zoom'``
          * ``'rangeSelector'``
          * ``'chartMenu'``
          * ``'legend'``
          * ``'container'``.

        In addition, any custom components can be added here. Adding container first in
        order will make the keyboard focus stop on the chart container first, requiring
        the user to tab again to enter the chart.

        :returns: Order of components to follow when tab navigating the chart.
        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._order

    @order.setter
    def order(self, value):
        value = validators.iterable(value, allow_empty = True)
        if not value:
            value = None
        else:
            value = [validators.string(x, allow_empty = False) for x in value]

        self._order = value

    @property
    def series_navigation(self) -> SeriesNavigation:
        """Options for the keyboard navigation of data points and series.

        :returns: Configuration for series navigation.
        :rtype: :class:`SeriesNavigation` or :obj:`None <python:None>`
        """
        return self._series_navigation

    @series_navigation.setter
    @class_sensitive(SeriesNavigation)
    def series_navigation(self, value):
        self._series_navigation = value

    @property
    def wrap_around(self) -> bool:
        """If ``True``, indicates that keyboard navigation should wrap around when
        reaching the end of arrow-key navigation for an element in the chart.

        Defaults to ``True``.

        :returns: Flag indicating whether navigation should wrap around when reaching the
          end of arrow-key navigation for an element in the chart.
        :rtype: :class:`bool <python:bool>`
        """
        return self._wrap_around

    @wrap_around.setter
    def wrap_around(self, value):
        self._wrap_around = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        as_dict = validators.dict(as_dict, allow_empty = True)
        kwargs = {
            'enabled': as_dict.pop('enabled', True),
            'focus_border': as_dict.pop('focusBorder', None),
            'order': as_dict.pop('order', None),
            'series_navigation': as_dict.pop('seriesNavigation', None),
            'wrap_around': as_dict.pop('wrapAround', True)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'enabled': self.enabled,
            'focusBorder': self.focus_border,
            'order': self.order,
            'seriesNavigation': self.series_navigation,
            'wrapAround': self.wrapAround
        }
        return self.trim_dict(untrimmed)
