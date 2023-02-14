from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.events import BreadcrumbEvents
from highcharts_core.utility_classes.position import Position
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class Separator(HighchartsMeta):
    """Configuration object for the Breadcrumbs Separator."""

    def __init__(self, **kwargs):
        self._style = None
        self._text = None

        self.style = kwargs.get('style', None)
        self.text = kwargs.get('text', None)

    @property
    def style(self) -> Optional[dict]:
        """CSS styles for the Breadcrumb Separator.

        :rtype: :class:`dict <python:dict>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.dict(value)

    @property
    def text(self) -> Optional[str]:
        """The text to use as the separator. Defaults to
        ``'/'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'style': self.style,
            'text': self.text
        }

        return untrimmed


class BreadcrumbOptions(HighchartsMeta):
    """Configuration for the breadcrumbs, the navigation at the top leading the way
    up through the drilldown levels."""

    def __init__(self, **kwargs):
        self._button_spacing = None
        self._button_theme = None
        self._events = None
        self._floating = None
        self._format = None
        self._formatter = None
        self._position = None
        self._relative_to = None
        self._rtl = None
        self._separator = None
        self._show_full_path = None
        self._style = None
        self._use_html = None
        self._z_index = None

        self.button_spacing = kwargs.get('button_spacing', None)
        self.button_theme = kwargs.get('button_theme', None)
        self.events = kwargs.get('events', None)
        self.floating = kwargs.get('floating', None)
        self.format = kwargs.get('format', None)
        self.formatter = kwargs.get('formatter', None)
        self.position = kwargs.get('position', None)
        self.relative_to = kwargs.get('relative_to', None)
        self.rtl = kwargs.get('rtl', None)
        self.separator = kwargs.get('separator', None)
        self.show_full_path = kwargs.get('show_full_path', None)
        self.style = kwargs.get('style', None)
        self.use_html = kwargs.get('use_html', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def button_spacing(self) -> Optional[int | float | Decimal]:
        """The default padding expressed in pixels for each button and separator in each
        direction.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._button_spacing

    @button_spacing.setter
    def button_spacing(self, value):
        self._button_spacing = validators.numeric(value, allow_empty = True)

    @property
    def button_theme(self) -> Optional[dict]:
        """A collection of attributes for the breadcrumb buttons.

        The object takes SVG attributes like ``fill``, ``stroke``, ``stroke-width`` or
        ``r``, the border radius.

        The theme also supports ``style``, a collection of CSS properties for the text.
        The object can also be extended with states, so you can set presentational options
        for ``hover``, ``select``, or ``disabled`` button states.

        :rtype: :class:`dict <python:dict>`
        """
        return self._theme

    @button_theme.setter
    def button_theme(self, value):
        self._theme = validators.dict(value, allow_empty = True)

    @property
    def events(self) -> Optional[BreadcrumbEvents]:
        """Definition of JavaScript event listeners to apply to the breadcrumbs.

        :rtype: :class:`ChartEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(BreadcrumbEvents)
    def events(self, value):
        self._events = value

    @property
    def floating(self) -> Optional[bool]:
        """If ``True`, sets the breadcrumbs to floating. When the breadcrumbs are
        floating, the plot area will not move to make space for it. Defaults to ``False``.

        .. warning::

          This property will not work when positioned in the middle.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._floating

    @floating.setter
    def floating(self, value):
        if value is None:
            self._floating = None
        else:
            self._floating = bool(value)

    @property
    def format(self) -> Optional[str]:
        """A format string for the breadcrumbs button. Variables are enclosed by curly
        brackets. Available values are passed in the declared point options.

        :returns: The format string to apply to the breadcrumbs.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format

    @format.setter
    def format(self, value):
        self._format = validators.string(value, allow_empty = True)

    @property
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format the breadcrumb text.

        :returns: A JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @property
    def position(self) -> Optional[Position]:
        """The position of the button row.

        :rtype: :class:`Position` or :obj:`None <python:None>`
        """
        return self._position

    @position.setter
    @class_sensitive(Position)
    def position(self, value):
        self._position = value

    @property
    def relative_to(self) -> Optional[str]:
        """What frame the button placement should be related to. Defaults to
        ``'plotBox'``.

        Accepts:

          * ``'plot'``
          * ``'chart'``
          * ``'plotBox'``
          * ``'spacingBox'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._relative_to

    @relative_to.setter
    def relative_to(self, value):
        if not value:
            self._relative_to = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['plot', 'chart', 'plotBox', 'spacingBox']:
                raise errors.HighchartsValueError(f'relative_to accepts "plot", "chart", '
                                                  f'"plotBox", "spacingBox", or None. '
                                                  f'Received: {value}')
            self._relative_to = value

    @property
    def rtl(self) -> Optional[bool]:
        """If ``True`, reverses the order of the buttons (commonly used for Arabic or
        Hebrew). Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._rtl

    @rtl.setter
    def rtl(self, value):
        if value is None:
            self._rtl = None
        else:
            self._rtl = bool(value)

    @property
    def separator(self) -> Optional[Separator]:
        """Configuration for the breadcrumb separator.

        :rtype: :class:`Separator` or :obj:`None <python:None>`
        """
        return self._separator

    @separator.setter
    @class_sensitive(Separator)
    def separator(self, value):
        self._separator = value

    @property
    def show_full_path(self) -> Optional[bool]:
        """If ``True``, shows the full breadcrumb path. If ``False``, shows only a single
        breadcrumb button. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_full_path

    @show_full_path.setter
    def show_full_path(self, value):
        if value is None:
            self._show_full_path = None
        else:
            self._show_full_path = bool(value)

    @property
    def style(self) -> Optional[dict]:
        """CSS styles to apply to all breadcrumbs.

        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.dict(value, allow_empty = True)

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the breadcrumbs. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render the breadcrumbs using HTML.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        if value is None:
            self._use_html = None
        else:
            self._use_html = bool(value)

    @property
    def z_index(self) -> Optional[int]:
        """The Z-Index for the breadcrumbs. Defaults to ``7``.

        :returns: The z-index for the annotation.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.integer(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'button_spacing': as_dict.get('buttonSpacing', None),
            'button_theme': as_dict.get('buttonTheme', None),
            'events': as_dict.get('events', None),
            'floating': as_dict.get('floating', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'position': as_dict.get('position', None),
            'relative_to': as_dict.get('relativeTo', None),
            'rtl': as_dict.get('rtl', None),
            'separator': as_dict.get('separator', None),
            'show_full_path': as_dict.get('showFullPath', None),
            'style': as_dict.get('style', None),
            'use_html': as_dict.get('useHTML', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'buttonSpacing': self.button_spacing,
            'buttonTheme': self.button_theme,
            'events': self.events,
            'floating': self.floating,
            'format': self.format,
            'formatter': self.formatter,
            'position': self.position,
            'relativeTo': self.relative_to,
            'rtl': self.rtl,
            'separator': self.separator,
            'showFullPath': self.show_full_path,
            'style': self.style,
            'useHTML': self.use_html,
            'zIndex': self.z_index
        }

        return untrimmed
