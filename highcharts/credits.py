from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.position import Position


class CreditStyleOptions(HighchartsMeta):
    """CSS styles that are applicable to the :class:`Credits` label."""

    def __init__(self, **kwargs):
        self._color = None
        self._cursor = None
        self._font_size = None

        self.color = kwargs.pop('color', None)
        self.cursor = kwargs.pop('cursor', None)
        self.font_size = kwargs.pop('font_size', None)

    @property
    def color(self) -> Optional[str]:
        """The color to apply to the label. Defaults to ``'#999999'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`.
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def cursor(self) -> Optional[str]:
        """The value to pass for the mouse cursor. Defaults to ``'pointer'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = validators.string(value, allow_empty = True)

    @property
    def font_size(self) -> Optional[str]:
        """The font size to apply to the label. Defaults to ``'9px'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'font_size': as_dict.pop('fontSize', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'color': self.color,
            'cursor': self.cursor,
            'fontSize': self.font_size
        }

        return untrimmed


class Credits(HighchartsMeta):
    """Highchart by default puts a credits label in the lower right corner of the
    chart. This can be changed using these options."""

    def __init__(self, **kwargs):
        self._enabled = None
        self._href = None
        self._position = None
        self._style = None
        self._text = None

        self.enabled = kwargs.pop('enabled', None)
        self.href = kwargs.pop('href', None)
        self.position = kwargs.pop('position', None)
        self.style = kwargs.pop('style', None)
        self.text = kwargs.pop('text', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, renders the credits text. Defaults to ``True``.

        :returns: Flag enabling or disabling credits.
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
    def href(self) -> Optional[str]:
        f"""The URL for the credits label. Defaults to
        ``'{constants.DEFAULT_CREDITS_HREF}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises ValueError: if not a URL, path-like string, or :obj:`None <python:None>`
        """
        return self._href

    @href.setter
    def href(self, value):
        self._href = validators.url(value, allow_empty = True)

    @property
    def position(self) -> Optional[Position]:
        """The position of the credits. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`Position` or :obj:`None <python:None>`
        """
        return self._position

    @position.setter
    @class_sensitive(Position)
    def position(self, value):
        self._position = value

    @property
    def style(self) -> Optional[CreditStyleOptions]:
        f"""CSS Styles for the credits label.

        Defaults to:

        .. code-block:: python

          {constants.DEFAULT_CREDITS_STYLE}

        :rtype: :class:`CreditStyleOptions` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    @class_sensitive(CreditStyleOptions)
    def style(self, value):
        self._style = value

    @property
    def text(self) -> Optional[str]:
        f"""The text for the credits label. Defaults to
        ``'{constants.DEFAULT_CREDITS_TEXT}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.pop('enabled', None),
            'href': as_dict.pop('href', None),
            'position': as_dict.pop('position', None),
            'style': as_dict.pop('style', None),
            'text': as_dict.pop('text', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'href': self.href,
            'position': self.position,
            'style': self.style,
            'text': self.text,
        }

        return untrimmed
