from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors, utility_functions
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class PaneBackground(HighchartsMeta):
    """Configuration of the background items to display within a :class:`Pane`."""

    def __init__(self, **kwargs):
        self._background_color = None
        self._border_color = None
        self._border_width = None
        self._class_name = None
        self._inner_radius = None
        self._outer_radius = None
        self._shape = None

        self.background_color = kwargs.get('background_color', None)
        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.class_name = kwargs.get('class_name', None)
        self.inner_radius = kwargs.get('inner_radius', None)
        self.outer_radius = kwargs.get('outer_radius', None)
        self.shape = kwargs.get('shape', None)

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or gradient for the pane. Defaults to
        ``'{ "linearGradient": { "x1": 0, "y1": 0, "x2": 0, "y2": 1 }, stops: [[0, "#ffffff"], [1, "#e6e6e6"]] }'``.

        :returns: The backgorund color for the outer chart area.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = utility_functions.validate_color(value)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the pane border. Defaults to
        ``'#cccccc'``.

        :returns: The color of the pane's border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width (in pixels) applied to the outer chart border. Defaults to
        ``1``.

        :returns: The border width to apply to the pane.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS. Defaults to
        ``'highcharts-pane'``.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def inner_radius(self) -> Optional[int | float | Decimal | str]:
        """The inner radius (in pixels if numeric or as a percentage string) applied to
        the pane. Defaults to ``0``.

        :returns: The inner radius of the pane background.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, value):
        if value is None or value == '':
            self._inner_radius = None
        else:
            try:
                self._inner_radius = validators.string(value, allow_empty = True)
            except ValueError:
                self._inner_radius = validators.numeric(value, allow_empty = True)

    @property
    def outer_radius(self) -> Optional[int | float | Decimal | str]:
        """The outer radius (in pixels if numeric or as a percentage string) applied to
        a circular pane background. Defaults to
        ``'105%'``.

        :returns: The outer radius of the pane background.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._outer_radius

    @outer_radius.setter
    def outer_radius(self, value):
        if value is None or value == '':
            self._outer_radius = None
        else:
            try:
                self._outer_radius = validators.string(value, allow_empty = True)
            except ValueError:
                self._outer_radius = validators.numeric(value, allow_empty = True)

    @property
    def shape(self) -> Optional[str]:
        """The shape of the pane background. Defaults to
        ``'circle'``.

        Accepts:

          * ``'circle'``
          * ``'solid'``
          * ``'arc'``

        .. note::

          When ``'solid'``, the background is circular.
          When ``'arc'``, the background extends only from the min to the max of the value
          axis.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._shape

    @shape.setter
    def shape(self, value):
        if not value:
            self._shape = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['circle', 'solid', 'arc']:
                raise errors.HighchartsValueError(f'shape expects "circle", "solid", or '
                                                  f'"arc". Received: {value}')
            self._shape = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'inner_radius': as_dict.get('innerRadius', None),
            'outer_radius': as_dict.get('outerRadius', None),
            'shape': as_dict.get('shape', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'innerRadius': self.inner_radius,
            'outerRadius': self.outer_radius,
            'shape': self.shape
        }

        return untrimmed


class Pane(HighchartsMeta):
    """The pane serves as a container for axes and backgrounds for circular gauges and
    polar charts."""

    def __init__(self, **kwargs):
        self._background = None
        self._center = None
        self._end_angle = None
        self._inner_size = None
        self._size = None
        self._start_angle = None

        self.background = kwargs.get('background', None)
        self.center = kwargs.get('center', None)
        self.end_angle = kwargs.get('end_angle', None)
        self.inner_size = kwargs.get('inner_size', None)
        self.size = kwargs.get('size', None)
        self.start_angle = kwargs.get('start_angle', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'pane'

    @property
    def background(self) -> Optional[List[PaneBackground]]:
        """An array of background items for the pane.

        :rtype: :class:`list <python:list>` of :class:`PaneBackground`, or
          :obj:`None <python:None>`
        """
        return self._background

    @background.setter
    @class_sensitive(PaneBackground, force_iterable = True)
    def background(self, value):
        self._background = value

    @property
    def center(self) -> Optional[List[str | int]]:
        """The center of a polar chart or angular gauge, given as an array of ``[x, y]``
        positions. Positions can be given as integers that transform to pixels, or as
        percentages of the plot area size. Defaults to
        ``[['50%', '50%']]``.

        :returns: Collection of positions, or :obj:`None <python:None>`
        :rtype: :class:`list <python:list>` of two-item :class:`list <python:list>`
          where each item is either a :class:`str <python:str>` or
          :class:`int <python:int>`, or :obj:`None <python:None>`
        """
        return self._center

    @center.setter
    def center(self, value):
        if not value:
            self._center = None
        else:
            value = validators.iterable(value,
                                        allow_empty = False,
                                        minimum_length = 2,
                                        maximum_length = 2)
            validated = []
            for item in value:
                try:
                    item = validators.string(item)
                    if '%' not in item:
                        raise errors.HighchartsValueError('center expects either a '
                                                          'numeric value or a percentage '
                                                          'string. No "%"" symbol found.')
                except ValueError:
                    item = validators.numeric(item)

                validated.append(item)

            self._center = validated

    @property
    def end_angle(self) -> Optional[int | float | Decimal]:
        """The end angle of the polar X axis or gauge value axis, given in degrees where
        ``0`` is north. Defaults to :meth:`Pane.start_angle` if :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._end_angle

    @end_angle.setter
    def end_angle(self, value):
        self._end_angle = validators.numeric(value, allow_empty = True)

    @property
    def inner_size(self) -> Optional[int | float | Decimal | str]:
        """The inner size of the pane, either as a number defining pixels, or a
        percentage defining a percentage of the pane's size. Defaults to
        ``'0%'``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._inner_size

    @inner_size.setter
    def inner_size(self, value):
        if not value:
            self._inner_size = None
        else:
            try:
                self._inner_size = validators.string(value)
            except ValueError:
                self._inner_size = validators.numeric(value)

    @property
    def size(self) -> Optional[int | float | Decimal | str]:
        """The size of the pane, either as a number defining pixels, or a
        percentage defining a percentage of the pane's size. Defaults to
        ``'85%'``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._size

    @size.setter
    def size(self, value):
        if not value:
            self._size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('size expects either a number or '
                                                      'a percentage string. No "%" '
                                                      'symbol found.')
            except (ValueError, TypeError):
                self._size = validators.numeric(value)

    @property
    def start_angle(self) -> Optional[int | float | Decimal]:
        """The start angle of the polar X axis or gauge value axis, given in degrees where
        ``0`` is north. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._start_angle

    @start_angle.setter
    def start_angle(self, value):
        self._start_angle = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'background': as_dict.get('background', None),
            'center': as_dict.get('center', None),
            'end_angle': as_dict.get('endAngle', None),
            'inner_size': as_dict.get('innerSize', None),
            'size': as_dict.get('size', None),
            'start_angle': as_dict.get('startAngle', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'background': self.background,
            'center': self.center,
            'endAngle': self.end_angle,
            'innerSize': self.inner_size,
            'size': self.size,
            'startAngle': self.start_angle
        }

        return untrimmed
