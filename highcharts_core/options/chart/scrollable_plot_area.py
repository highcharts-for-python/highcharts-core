from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class ScrollablePlotArea(HighchartsMeta):
    """Configuration settings to make the plot area scrollable.

    This feature provides a minimum size for the plot area of the chart. If the size
    gets smaller than this, typically on mobile devices, a native browser scrollbar is
    presented. This scrollbar provides smooth scrolling for the contents of the plot
    area, whereas the title, legend and unaffected axes are fixed.

    .. hint::

      Since v7.1.2, a scrollable plot area can be defined for either horizontal or
      vertical scrolling, depending on whether the `minimum_width` or `minimum_height`
      options are set.

    """

    def __init__(self, **kwargs):
        self._minimum_height = None
        self._minimum_width = None
        self._opacity = None
        self._scroll_position_x = None
        self._scroll_position_y = None

        self.minimum_height = kwargs.get('minimum_height', None)
        self.minimum_width = kwargs.get('minimum_width', None)
        self.opacity = kwargs.get('opacity', None)
        self.scroll_position_x = kwargs.get('scroll_position_x', None)
        self.scroll_position_y = kwargs.get('scroll_position_y', None)

    @property
    def minimum_height(self) -> Optional[int | float | Decimal]:
        """The minimum height for the plot area expressed in pixels. If it gets smaller
        than this, the plot area will become scrollable.

        :rtype: numeric
        """
        return self._minimum_height

    @minimum_height.setter
    def minimum_height(self, value):
        self._minimum_height = validators.numeric(value, allow_empty = True)

    @property
    def minimum_width(self) -> Optional[int | float | Decimal]:
        """The minimum width for the plot area expressed in pixels. If it gets smaller
        than this, the plot area will become scrollable.

        :rtype: numeric
        """
        return self._minimum_width

    @minimum_width.setter
    def minimum_width(self, value):
        self._minimum_width = validators.numeric(value, allow_empty = True)

    @property
    def opacity(self) -> Optional[float]:
        """The opacity of the mask applied on one of the sides of the plot area, expressed
        as a value between ``0`` and ``1``. Defaults to ``0.85``.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.float(value, allow_empty = True)

    @property
    def scroll_position_x(self) -> Optional[float]:
        """The initial scrolling position of the scrollable plot area along the
        horizontal axis. Ranges from 0 to 1, where 0 aligns the plot area to the left and
        1 aligns it to the right.

        .. hint::

          Typically, we would use a value of ``1`` if the chart has right aligned Y axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._scroll_position_x

    @scroll_position_x.setter
    def scroll_position_x(self, value):
        self._scroll_position_x = validators.numeric(value,
                                                     allow_empty = True,
                                                     minimum = 0,
                                                     maximum = 1)

    @property
    def scroll_position_y(self) -> Optional[float]:
        """The initial scrolling position of the scrollable plot area along the
        vertical axis. Ranges from 0 to 1, where 0 aligns the plot area to the top and
        1 aligns it to the bottom.

        .. hint::

          Typically, we would use a value of ``1`` if the chart has right aligned Y axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._scroll_position_y

    @scroll_position_y.setter
    def scroll_position_y(self, value):
        self._scroll_position_y = validators.numeric(value,
                                                     allow_empty = True,
                                                     minimum = 0,
                                                     maximum = 1)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'minimum_height': as_dict.get('minHeight', None),
            'minimum_width': as_dict.get('minWidth', None),
            'opacity': as_dict.get('opacity', None),
            'scroll_position_x': as_dict.get('scrollPositionX', None),
            'scroll_position_y': as_dict.get('scrollPositionY', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'minHeight': self.minimum_height,
            'minWidth': self.minimum_width,
            'opacity': self.opacity,
            'scrollPositionX': self.scroll_position_x,
            'scrollPositionY': self.scroll_position_y
        }

        return untrimmed
