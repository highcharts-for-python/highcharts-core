from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class LinkOptions(HighchartsMeta):
    """Link style options."""

    def __init__(self, **kwargs):
        self._color = None
        self._dash_style = None
        self._width = None

        self.color = kwargs.get('color', None)
        self.dash_style = kwargs.get('dash_style', None)
        self.width = kwargs.get('width', None)

    @property
    def color(self) -> Optional[str]:
        """Color of the link between two nodes. Defaults to ``rgba(100, 100, 100, 0.5)``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def dash_style(self) -> Optional[str]:
        """A name for the dash style to use for links. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        self._dash_style = validators.string(value, allow_empty = True)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """Width (px) of the link between two nodes. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'dash_style': as_dict.get('dashStyle', None),
            'width': as_dict.get('width', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'color': self.color,
            'dashStyle': self.dash_style,
            'width': self.width
        }

        return untrimmed
