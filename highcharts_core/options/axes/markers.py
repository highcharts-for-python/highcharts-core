from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.animation import AnimationOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class AxisMarker(HighchartsMeta):
    """The triangular marker on a scalar color axis that points to the value of the
    hovered area."""

    def __init__(self, **kwargs):
        self._animation = None
        self._color = None
        self._width = None

        self.animation = kwargs.get('animation', None)
        self.color = kwargs.get('color', None)
        self.width = kwargs.get('width', None)

    @property
    def animation(self) -> Optional[bool | AnimationOptions]:
        """Animation for the marker as it moves between values. If
        :obj:`None <python:None>`, defaults to ``duration: 50``.

        .. hint::

          If set to ``False``, will disable animation of the marker.

        :rtype: :class:`AnimationOptions` or :class:`bool <python:bool>` or
          :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if value is False:
            self._animation = False
        else:
            self._animation = validate_types(value, AnimationOptions)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the marker. Defaults to :obj:`None <python:None>`, which
        applies '#999999'.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width of the marker. Defaults to :obj:`None <python:None>`, which applies
        a value of ``0.01``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.get('animation', None),
            'color': as_dict.get('color', None),
            'width': as_dict.get('width', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'animation': self.animation,
            'color': self.color,
            'width': self.width,
        }

        return untrimmed
