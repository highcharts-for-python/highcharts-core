from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors, constants
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class CrosshairOptions(HighchartsMeta):
    """Configuration options for a crosshair that follows either the mouse pointer or the
    hovered point."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._dash_style = None
        self._snap = None
        self._width = None
        self._z_index = None

        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.dash_style = kwargs.get('dash_style', None)
        self.snap = kwargs.get('snap', None)
        self.width = kwargs.get('width', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def class_name(self) -> Optional[str]:
        """A class name for the crosshair, particularly useful for styling the crosshair.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the crosshair. Defaults to :obj:`None <python:None>`, which
        applies ``'#cccccc' for datetime and numeric axes, and
        ``'rgba(204, 214, 235, 0.25)'`` for category axes (where the crosshair by default
        highlights the whole category).

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
        """Name of the dash style to use for the crosshair. Defaults to ``Solid``.

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
    def snap(self) -> Optional[bool]:
        """If ``True``, the crosshair should snap to the point. If ``False``, the
        crosshair will follow the pointer. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._snap

    @snap.setter
    def snap(self, value):
        if value is None:
            self._snap = None
        else:
            self._snap = bool(value)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width of the crosshair, in pixels. Defaults to :obj:`None <python:None>`,
        which applies ``1`` for numeric and datetime axes, and a single category width
        for category axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The Z index for the crosshair. Defaults to ``2``.

        .. hint::

          Higher Z-indices allow drawing the crosshair on top of the series or behind the
          grid lines.

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
            'snap': as_dict.get('snap', None),
            'width': as_dict.get('width', None),
            'z_index': as_dict.get('zIndex', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'dashStyle': self.dash_style,
            'snap': self.snap,
            'width': self.width,
            'zIndex': self.z_index
        }

        return untrimmed
