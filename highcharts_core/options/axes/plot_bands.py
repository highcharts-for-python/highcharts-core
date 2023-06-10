from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors, constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.events import MouseEvents

from highcharts_core.options.axes.labels import PlotBandLabel, PlotLineLabel


class PlotBand(HighchartsMeta):
    """Definition of a :term:`plot band`, which is a colored band stretching across the
    plot area which can be used to visually mark an interval along the axis.

    .. note::

      In a :term:`gauge chart`, a plot band on the :class:`YAxis` (value axis) will
      stretch along the perimeter of the gauge.

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._class_name = None
        self._color = None
        self._events = None
        self._from_ = None
        self._id = None
        self._label = None
        self._to = None
        self._z_index = None

        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.events = kwargs.get('events', None)
        self.from_ = kwargs.get('from_', None)
        self.id = kwargs.get('id', None)
        self.label = kwargs.get('label', None)
        self.to = kwargs.get('to', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """Border color for the plot band. Defaults to :obj:`None <python:None>`.

        .. warning::

          Also requires :meth:`PlotBand.border_width` to be set.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """Border width for the plot band. Defaults to :obj:`None <python:None>`.

        .. warning::

          Also requires :meth:`PlotBand.border_color` to be set.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A custom class name (in addition to the default ``highcharts-plot-band``) to
        apply to each individual band. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the plot band. Defaults to ``#e6ebf5``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def events(self) -> Optional[MouseEvents]:
        """Event handlers for the Plot Band.

        :rtype: :class:`MouseEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(MouseEvents)
    def events(self, value):
        self._events = value

    @property
    def from_(self) -> Optional[int | float | Decimal]:
        """The point where the plot band starts, expressed in axis units. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._from

    @from_.setter
    def from_(self, value):
        self._from = validators.numeric(value, allow_empty = True)

    @property
    def id(self) -> Optional[str]:
        """An identifier used for identifying the plot band if calling (in JavaScript)
        ``Axis.removePlotBand()``. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def label(self) -> Optional[PlotBandLabel]:
        """Label options for the Plot Band. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`PlotBandLabel` or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(PlotBandLabel)
    def label(self, value):
        self._label = value

    @property
    def to(self) -> Optional[int | float | Decimal]:
        """The end position of the plot band, expressed in axis units. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.numeric(value, allow_empty = True)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The Z index for the plot band. Defaults to :obj:`None <python:None>`.

        .. warning::

          Using the same z-index as another element may give unpredictable results, as the
          last rendered element will be on top. Values from ``0`` to ``20`` make sense.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'events': as_dict.get('events', None),
            'from_': as_dict.get('from', None),
            'id': as_dict.get('id', None),
            'label': as_dict.get('label', None),
            'to': as_dict.get('to', None),
            'z_index': as_dict.get('zIndex', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'color': self.color,
            'events': self.events,
            'from': self.from_,
            'id': self.id,
            'label': self.label,
            'to': self.to,
            'zIndex': self.z_index
        }

        return untrimmed


class PlotLine(HighchartsMeta):
    """A line that stretches across the plot area, marking a specific value on an axis."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._dash_style = None
        self._events = None
        self._id = None
        self._label = None
        self._value = None
        self._width = None
        self._z_index = None

        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.dash_style = kwargs.get('dash_style', None)
        self.events = kwargs.get('events', None)
        self.id = kwargs.get('id', None)
        self.label = kwargs.get('label', None)
        self.value = kwargs.get('value', None)
        self.width = kwargs.get('width', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def class_name(self) -> Optional[str]:
        """A custom class name (in addition to the default ``highcharts-plot-line``) to
        apply to each individual line. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the line. Defaults to ``#999999``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the lines. Defaults to ``Solid``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        if not value:
            self._dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._dash_style = value

    @property
    def events(self) -> Optional[MouseEvents]:
        """Event handlers for the Plot Line.

        :rtype: :class:`MouseEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(MouseEvents)
    def events(self, value):
        self._events = value

    @property
    def label(self) -> Optional[PlotLineLabel]:
        """Label options for the Plot Line. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`PlotLineLabel` or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(PlotLineLabel)
    def label(self, value):
        self._label = value

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The position of the line, expressed in axis units. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value):
        if hasattr(value, 'timestamp'):
            value = value.timestamp() * 1000

        self._value = validators.numeric(value, allow_empty = True)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width or thickness of the line, expressed in pixels. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, width):
        self._width = validators.numeric(width,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The Z index for the plot line. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'dash_style': as_dict.get('dashStyle', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label': as_dict.get('label', None),
            'value': as_dict.get('value', None),
            'width': as_dict.get('width', None),
            'z_index': as_dict.get('zIndex', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'dashStyle': self.dash_style,
            'events': self.events,
            'id': self.id,
            'label': self.label,
            'value': self.value,
            'width': self.width,
            'zIndex': self.z_index
        }

        return untrimmed
