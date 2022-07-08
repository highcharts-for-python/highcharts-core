from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class ShadowOptions(HighchartsMeta):
    """Object configuring the shadow to apply to another object."""

    def __init__(self, **kwargs):
        self._color = None,
        self._offset_x = None
        self._offset_y = None
        self._opacity = None
        self._width = None

        self.color = kwargs.pop('color', None)
        self.offset_x = kwargs.pop('offset_x', None)
        self.offset_y = kwargs.pop('offset_y', None)
        self.opacity = kwargs.pop('opacity', None)
        self.width = kwargs.pop('width', None)

    @property
    def color(self) -> Optional[str]:
        """The color to apply to the shadow.

        :returns: Color string
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def offset_x(self) -> Optional[int | float | Decimal]:
        """The offset to apply along the horizontal axis.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._offset_x

    @offset_x.setter
    def offset_x(self, value):
        self._offset_x = validators.numeric(value, allow_empty = True)

    @property
    def offset_y(self) -> Optional[int | float | Decimal]:
        """The offset to apply along the vertical axis.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._offset_y

    @offset_y.setter
    def offset_y(self, value):
        self._offset_y = validators.numeric(value, allow_empty = True)

    @property
    def opacity(self) -> Optional[int | float | Decimal]:
        """The opacity to apply to the shadow.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.numeric(value, allow_empty = True)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width of the shadow in pixels.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.pop('color', None),
            'offset_x': as_dict.pop('offsetX', None),
            'offset_y': as_dict.pop('offsetY', None),
            'opacity': as_dict.pop('opacity', None),
            'width': as_dict.pop('width', None)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'color': self.color,
            'offsetX': self.offset_x,
            'offsetY': self.offset_y,
            'opacity': self.opacity,
            'width': self.width
        }
        as_dict = self.trim_dict(untrimmed)

        return as_dict
