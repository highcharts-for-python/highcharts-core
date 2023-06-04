from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.metaclasses import HighchartsMeta


class AnnotationPoint(HighchartsMeta):
    """Object representation of a shape point."""

    def __init__(self, **kwargs):
        self._x = None
        self._x_axis = None
        self._y = None
        self._y_axis = None

        self.x = kwargs.get('x', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y = kwargs.get('y', None)
        self.y_axis = kwargs.get('y_axis', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations.shapes.point'

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x position of the point.

        Units can be either in axis or chart pixel coordinates.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def x_axis(self) -> Optional[str | int]:
        """This number defines which xAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the xAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's x coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if value is None or value == '':
            self._x_axis = None
        else:
            try:
                try:
                    self._x_axis = validators.integer(value)
                except (ValueError, TypeError):
                    self._x_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y position of the point.

        Units can be either in axis or chart pixel coordinates.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @property
    def y_axis(self) -> Optional[str | int]:
        """This number defines which yAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the yAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's y coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if value is None or value == '':
            self._y_axis = None
        else:
            try:
                try:
                    self._y_axis = validators.integer(value)
                except (ValueError, TypeError):
                    self._y_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'x': as_dict.get('x', None),
            'x_axis': as_dict.get('xAxis', None),
            'y': as_dict.get('y', None),
            'y_axis': as_dict.get('yAxis', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'x': self.x,
            'xAxis': self.x_axis,
            'y': self.y,
            'yAxis': self.y_axis
        }
