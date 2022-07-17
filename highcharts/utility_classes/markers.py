from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.states import States


class Marker(HighchartsMeta):
    """Options for the point markers of line-like series."""

    def __init__(self, **kwargs):
        self._enabled = None
        self._enabled_threshold = None
        self._fill_color = None
        self._height = None
        self._line_color = None
        self._line_width = None
        self._radius = None
        self._states = None
        self._symbol = None
        self._width = None

        self.enabled = kwargs.pop('enabled', None)
        self.enabled_threshold = kwargs.pop('enabled_threshold',
                                            constants.DEFAULT_MARKER.get('enabled_threshold'))
        self.fill_color = kwargs.pop('fill_color', None)
        self.height = kwargs.pop('height', None)
        self.line_color = kwargs.pop('line_color',
                                     constants.DEFAULT_MARKER.get('line_color'))
        self.line_width = kwargs.pop('line_width',
                                     constants.DEFAULT_MARKER.get('line_width'))
        self.radius = kwargs.pop('radius', constants.DEFAULT_MARKER.get('radius'))
        self.states = kwargs.pop('states', None)
        self.symbol = kwargs.pop('symbol', None)
        self.width = kwargs.pop('width', constants.DEFAULT_MARKER.get('width'))

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, markers are enabled. If ``False``, markers are disabled. If
        :obj:`None <python:None>`, markers are hidden when the data is dense and shown
        for more widespread data points.

        Defaults to :obj:`None <python:None>`

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def enabled_threshold(self) -> Optional[int]:
        """The threshold for how dense the point markers should be before they are hidden,
        assuming that :meth:`Marker.enabled` is :obj:`None <python:None>`. Defaults to
        ``2``.

        The number indicates the horizontal distance between the two closest points in the
        series, as multiples of the :Meth:`Marker.radius`. In other words, the default
        value of ``2`` means points are hidden if overlapping horizontally.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._enabled_threshold

    @enabled_threshold.setter
    def enabled_threshold(self, value):
        self._enabled_threshold = validators.integer(value,
                                                     allow_empty = True,
                                                     minimum = 0,
                                                     coerce_value = True)

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """The fill color or gradient for the marker. Defaults to
        :obj:`None <python:None>`, which causes the series' or point's color to be used.

        :returns: The fill color for the marker.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        if not value:
            self._fill_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._fill_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._fill_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Gradient.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._fill_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._fill_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Pattern.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._fill_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """Explicitly set the height of an image marker. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          Only applies to image markers. When setting this property, :meth:`Marker.width`
          must also be set.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The line color or gradient for the marker's outline. Defaults to
        ``'{constants.DEFAULT_MARKER.get('line_color')}'``.

        :returns: The line color for the marker.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        if not value:
            self._line_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._line_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._line_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Gradient.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._line_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._line_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Pattern.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._line_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        f"""The line width (in pixels) applied to the marker's border. Defaults to
        ``{constants.DEFAULT_MARKER.get('line_width')}``.

        :returns: The line width to apply to the marker's border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value, allow_empty = True)

    @property
    def radius(self) -> Optional[int | float | Decimal]:
        f"""The radius applied to the point marker. Defaults to
        ``{constants.DEFAULT_MARKER.get('radius')}``.

        :returns: The radius to apply to the point marker.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = validators.numeric(value, allow_empty = True)

    @property
    def states(self) -> Optional[States]:
        """States for a single point marker.

        :rtype: :class:`States` or :obj:`None <python:None>`
        """
        return self._states

    @states.setter
    @class_sensitive(States)
    def states(self, value):
        self._states = value

    @property
    def symbol(self) -> Optional[str]:
        """A predefined shape or symbol for the marker. Defaults to
        :obj:`None <python:None>`.

        When :obj:`None <python:None>`, the symbol is pulled from (JavaScript)
        ``options.symbols``. Other possible values are:

          * ``'circle'``
          * ``'square'``
          * ``'diamond'``
          * ``'triangle'``
          * ``'triangle-down'``

        Additionally, the URL to a graphic can be given using the form:
        ``'url(graphic.png)'``.

        .. note::

          For an image marker to be applied to exported charts, its URL needs to be
          accessible by the export server.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if not value:
            self._symbol = None
        else:
            value = validators.string(value)
            value = value.lower()
            if not value.startswith('url') and value not in ['circle',
                                                             'square',
                                                             'diamond',
                                                             'triangle',
                                                             'triangle-down']:
                raise errors.HighchartsValueError(f'symbol must be a recognized value. '
                                                  f'Was: {value}')
            self._symbol = value

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """Explicitly set the width of an image marker. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          Only applies to image markers. When setting this property, :meth:`Marker.height`
          must also be set.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.pop('enabled', None),
            'enabled_threshold': as_dict.pop('enabledThreshold',
                                             constants.DEFAULT_MARKER.get('enabled_threshold')),
            'fill_color': as_dict.pop('fillColor', None),
            'height': as_dict.pop('height', None),
            'line_color': as_dict.pop('lineColor',
                                      constants.DEFAULT_MARKER.get('line_color')),
            'line_width': as_dict.pop('lineWidth',
                                      constants.DEFAULT_MARKER.get('line_width')),
            'radius': as_dict.pop('radius', constants.DEFAULT_MARKER.get('radius')),
            'states': as_dict.pop('states', None),
            'symbol': as_dict.pop('symbol', None),
            'width': as_dict.pop('width', constants.DEFAULT_MARKER.get('width'))
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'enabled': self.enabled,
            'enabledThreshold': self.enabled_threshold,
            'fillColor': self.fill_color,
            'height': self.height,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
            'radius': self.radius,
            'states': self.states,
            'symbol': self.symbol,
            'width': self.width
        }

        return self.trim_dict(untrimmed)
