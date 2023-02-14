from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class LinearGradient(HighchartsMeta):
    """Configuration of a linear gradient pattern."""

    def __init__(self, **kwargs):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self.x1 = kwargs.get('x1', None)
        self.x2 = kwargs.get('x2', None)
        self.y1 = kwargs.get('y1', None)
        self.y2 = kwargs.get('y2', None)

    @property
    def x1(self) -> Optional[float]:
        """Start horizontal position for the gradient. Expects a value between 0 - 1.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._x1

    @x1.setter
    def x1(self, value):
        self._x1 = validators.float(value,
                                    allow_empty = True,
                                    minimum = 0,
                                    maximum = 1)

    @property
    def x2(self) -> Optional[float]:
        """End horizontal position for the gradient. Expects a value between 0 - 1.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._x2

    @x2.setter
    def x2(self, value):
        self._x2 = validators.float(value,
                                    allow_empty = True,
                                    minimum = 0,
                                    maximum = 1)

    @property
    def y1(self) -> Optional[float]:
        """Start vertical position for the gradient. Expects a value between 0 - 1.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._y1

    @y1.setter
    def y1(self, value):
        self._y1 = validators.float(value,
                                    allow_empty = True,
                                    minimum = 0,
                                    maximum = 1)

    @property
    def y2(self) -> Optional[float]:
        """End vertical position for the gradient. Expects a value between 0 - 1.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._y2

    @y2.setter
    def y2(self, value):
        self._y2 = validators.float(value,
                                    allow_empty = True,
                                    minimum = 0,
                                    maximum = 1)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'x1': as_dict.get('x1', None),
            'x2': as_dict.get('x2', None),
            'y1': as_dict.get('y1', None),
            'y2': as_dict.get('y2', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'x1': self.x1,
            'x2': self.x2,
            'y1': self.y1,
            'y2': self.y2
        }

        return untrimmed


class RadialGradient(HighchartsMeta):
    """Configuration of a radial gradient pattern."""

    def __init__(self, **kwargs):
        self._cx = None
        self._cy = None
        self._r = None

        self.cx = kwargs.get('cx', None)
        self.cy = kwargs.get('cy', None)
        self.r = kwargs.get('r', None)

    @property
    def cx(self) -> Optional[float]:
        """Center position for the gradient along the horizontal axis. Expects a value
        between 0 - 1, relative to the shape.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._cx

    @cx.setter
    def cx(self, value):
        self._cx = validators.float(value,
                                    allow_empty = True,
                                    minimum = 0,
                                    maximum = 1)

    @property
    def cy(self) -> Optional[float]:
        """Center position for the gradient along the vertical axis. Expects a value
        between 0 - 1, relative to the shape.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._cy

    @cy.setter
    def cy(self, value):
        self._cy = validators.float(value,
                                    allow_empty = True,
                                    minimum = 0,
                                    maximum = 1)

    @property
    def r(self) -> Optional[float]:
        """Radius of the gradient relative to the shape. Expects a value between 0 - 1.

        :rtype: :class:`float <python:float>` or :obj:`None <python:None>`
        """
        return self._r

    @r.setter
    def r(self, value):
        self._r = validators.float(value,
                                   allow_empty = True,
                                   minimum = 0,
                                   maximum = 1)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'cx': as_dict.get('cx', None),
            'cy': as_dict.get('cy', None),
            'r': as_dict.get('r', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'cx': self.cx,
            'cy': self.cy,
            'r': self.r
        }

        return untrimmed


class Gradient(HighchartsMeta):
    """Configuration of a gradient color pattern."""

    def __init__(self, **kwargs):
        self._linear_gradient = None
        self._radial_gradient = None
        self._stops = None

        self.linear_gradient = kwargs.get('linear_gradient', None)
        self.radial_gradient = kwargs.get('radial_gradient', None)
        self.stops = kwargs.get('stops', None)

    @property
    def linear_gradient(self) -> Optional[LinearGradient]:
        """Holds an object that defines the start position and end position of the
        gradient relative to the shape.

        :rtype: :class:`LinearGradient` or :obj:`None <python:None>`
        """
        return self._linear_gradient

    @linear_gradient.setter
    @class_sensitive(LinearGradient)
    def linear_gradient(self, value):
        self._linear_gradient = value

    @property
    def radial_gradient(self) -> Optional[RadialGradient]:
        """Holds an object that defines the center and radius of a radial gradient
        relative to the shape.

        :rtype: :class:`RadialGradient` or :obj:`None <python:None>`
        """
        return self._radial_gradient

    @radial_gradient.setter
    @class_sensitive(RadialGradient)
    def radial_gradient(self, value):
        self._radial_gradient = value

    @property
    def stops(self):
        """Definition of the stop points within the color gradient.

        The value expected is an iterable of two-value iterables, where the first value
        is the start position of the gradient, the second is the color to apply to this
        section of the gradient.

        :rtype: :class:`list <python:list>` of 2-item :class:`list <python:list>` where
          item 1 is a numeric, and item 2 is a :class:`str <python:str>`

        """
        return self._stops

    @stops.setter
    def stops(self, value):
        value = validators.iterable(value, allow_empty = True)
        if not value:
            self._stops = None
        else:
            stops = []
            for item in value:
                stop = validators.iterable(item,
                                           allow_empty = False,
                                           minimum_length = 2,
                                           maximum_length = 2)
                stop[0] = validators.numeric(stop[0],
                                             allow_empty = False)
                stop[1] = validators.string(stop[1],
                                            allow_empty = False)
                stops.append(stop)

            self._stops = stops

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'linear_gradient': as_dict.get('linearGradient', None),
            'radial_gradient': as_dict.get('radialGradient', None),
            'stops': as_dict.get('stops', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'linearGradient': self.linear_gradient,
            'radialGradient': self.radial_gradient,
            'stops': self.stops
        }

        return untrimmed
