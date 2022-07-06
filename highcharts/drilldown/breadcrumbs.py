from typing import Optional, Any
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.events import BreadcrumbEvents
from highcharts.utility_classes.position import Position


class Separator(HighchartsMeta):
    """Configuration object for the Breadcrumbs Separator."""

    def __init__(self, **kwargs):
        self._style = None
        self._text = '/'

        self.style = kwargs.pop('style', constants.DEFAULT_BREADCRUMBS_SEPARATOR_STYLE)
        self.text = kwargs.pop('text', constants.DEFAULT_BREADCRUMBS_SEPARATOR_TEXT)

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
    def text(self) -> str:
        f"""The text to use as the separator. Defaults to
        ``'{constants.DEFAULT_BREADCRUMBS_SEPARATOR_TEXT}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'style': as_dict.pop('style', constants.DEFAULT_BREADCRUMBS_SEPARATOR_STYLE),
            'text': as_dict.pop('text', constants.DEFAULT_BREADCRUMBS_SEPARATOR_TEXT)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'style': self.style,
            'text': self.text
        }

        return self.trim_dict(untrimmed)


class BreadcrumbOptions(HighchartsMeta):
    """Configuration for the breadcrumbs, the navigation at the top leading the way
    up through the drilldown levels."""

    def __init__(self, **kwargs):
        self._button_spacing = 5
        self._button_theme = None
        self._events = None
        self._floating = False
        self._format = None
        self._formatter = None
        self._position = None
        self._relative_to = None
        self._rtl = False
        self._separator = None
        self._show_full_path = True
        self._style = None
        self._use_html = False
        self._z_index = 7

        self.button_spacing = kwargs.pop('button_spacing', 5)
        self.button_theme = kwargs.pop('button_theme', None)
        self.events = kwargs.pop('events', None)
        self.floating = kwargs.pop('floating', False)
        self.format = kwargs.pop('format', None)
        self.formatter = kwargs.pop('formatter', None)
        self.position = kwargs.pop('position',
                                   constants.DEFAULT_BREADCRUMBS_POSITION)
        self.relative_to = kwargs.pop('relative_to',
                                      constants.DEFAULT_BREADCRUMBS_RELATIVE_TO)
        self.rtl = kwargs.pop('rtl', False)
        self.separator = kwargs.pop('separator', Separator())
        self.show_full_path = kwargs.pop('show_full_path', True)
        self.style = kwargs.pop('style', constants.DEFAULT_BREADCRUMBS_STYLE)
        self.use_html = kwargs.pop('use_html', False)
        self.z_index = kwargs.pop('z_index', 7)

    @property
    def button_spacing(self) -> Any[int, float, Decimal]:
        """The default padding expressed in pixels for each button and separator in each
        direction.

        :rtype: numeric
        """
        return self._button_spacing

    @button_spacing.setter
    def button_spacing(self, value):
        self._button_spacing = validators.numeric(value, allow_empty = True) or 5

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
    def floating(self) -> bool:
        """If ``True`, sets the breadcrumbs to floating. When the breadcrumbs are
        floating, the plot area will not move to make space for it. Defaults to ``False``.

        .. warning::

          This property will not work when positioned in the middle.

        :rtype: :class:`bool <python:bool>`
        """
        return self._floating

    @floating.setter
    def floating(self, value):
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
    def formatter(self) -> Optional[str]:
        """JavaScript callback function to format the breadcrumb text.

        :returns: A JavaScript callback function.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    def formatter(self, value):
        self._formatter = validators.string(value, allow_empty = True)

    @property
    def position(self) -> Position:
        """The position of the button row.

        :rtype: :class:`Position`
        """
        return self._position

    @position.setter
    @class_sensitive(Position)
    def position(self, value):
        self._position = value

    @property
    def relative_to(self) -> str:
        f"""What frame the button placement should be related to. Defaults to
        ``'{constants.DEFAULT_BREADCRUMBS_RELATIVE_TO}'``.

        Accepts:

          * ``'plot'``
          * ``'chart'``
          * ``'plotBox'``
          * ``'spacingBox'

        :rtype: :class:`str <python:str>`
        """
        return self._relative_to

    @relative_to.setter
    def relative_to(self, value):
        if not value:
            self._relative_to = constants.DEFAULT_BREADCRUMBS_RELATIVE_TO
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['plot', 'chart', 'plotBox', 'spacingBox']:
                raise errors.HighchartsValueError(f'relative_to accepts "plot", "chart", '
                                                  f'"plotBox", "spacingBox", or None. '
                                                  f'Received: {value}')
            self._relative_to = value

    @property
    def rtl(self) -> bool:
        """If ``True`, reverses the order of the buttons (commonly used for Arabic or
        Hebrew). Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._rtl

    @rtl.setter
    def rtl(self, value):
        self._rtl = bool(value)

    @property
    def separator(self) -> Separator:
        """Configuration for the breadcrumb separator.

        :rtype: :class:`Separator`
        """
        return self._separator

    @separator.setter
    @class_sensitive(Separator)
    def separator(self, value):
        self._separator = value

    @property
    def show_full_path(self) -> bool:
        """If ``True``, shows the full breadcrumb path. If ``False``, shows only a single
        breadcrumb button. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._show_full_path

    @show_full_path.setter
    def show_full_path(self, value):
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
    def use_html(self) -> bool:
        """If ``True``, will use HTML to render the breadcrumbs. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render the breadcrumbs using HTML.
        :rtype: :class:`bool <python:bool>`
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        self._use_html = bool(value)

    @property
    def z_index(self) -> int:
        """The Z-Index for the breadcrumbs. Defaults to ``7``.

        :returns: The z-index for the annotation.
        :rtype: :class:`int <python:int>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        value = validators.integer(value, allow_empty = True) or 7

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'button_spacing': as_dict.pop('buttonSpacing', 5),
            'button_theme': as_dict.pop('buttonTheme', None),
            'events': as_dict.pop('events', None),
            'floating': as_dict.pop('floating', False),
            'format': as_dict.pop('format', None),
            'formatter': as_dict.pop('formatter', None),
            'position': as_dict.pop('position', constants.DEFAULT_BREADCRUMBS_POSITION),
            'relative_to': as_dict.pop('relativeTo',
                                       constants.DEFAULT_BREADCRUMBS_RELATIVE_TO),
            'rtl': as_dict.pop('rtl', False),
            'separator': as_dict.pop('separator', Separator()),
            'show_full_path': as_dict.pop('showFullPath', True),
            'style': as_dict.pop('style', None),
            'use_html': as_dict.pop('useHTML', False),
            'z_index': as_dict.pop('zIndex', 7)
        }

        return cls(**kwargs)

    def to_dict(self):
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

        return self.trim_dict(untrimmed)
