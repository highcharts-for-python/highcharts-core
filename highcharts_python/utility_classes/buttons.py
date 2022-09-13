from typing import Optional, List
from decimal import Decimal
from collections import UserDict
try:
    import orjson as json
except ImportError:
    try:
        import rapidjson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            import json

from validator_collection import validators, checkers, errors as validator_errors

from highcharts_python import constants, errors, utility_functions
from highcharts_python.decorators import validate_types, class_sensitive
from highcharts_python.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_python.utility_classes.gradients import Gradient
from highcharts_python.utility_classes.patterns import Pattern
from highcharts_python.utility_classes.javascript_functions import CallbackFunction


class ButtonTheme(HighchartsMeta):
    """Settings used to style buttons."""

    def __init__(self, **kwargs):
        self._fill = None
        self._stroke = None

        self.fill = kwargs.get('fill', None)
        self.stroke = kwargs.get('stroke', None)

    @property
    def fill(self) -> Optional[str | Gradient | Pattern]:
        """The color of the button's fill. The default fill exists only to capture hover
        events.

        :rtype: :class:`str <python:str>` (for colors), :class:`Gradient` for gradients,
          :class:`Pattern` for pattern definitions, or :obj:`None <python:None>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = utility_functions.validate_color(value)

    @property
    def stroke(self) -> Optional[str]:
        """The color of the button's stroke. Defaults to ``'none'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        self._stroke = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'fill': as_dict.get('fill', None),
            'stroke': as_dict.get('stroke', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fill': self.fill,
            'stroke': self.stroke
        }

        return untrimmed


class ButtonConfiguration(HighchartsMeta):
    """Configuration of options that apply to a given button."""

    def __init__(self, **kwargs):
        self._enabled = None
        self._text = None
        self._theme = None
        self._y = None

        self.enabled = kwargs.get('enabled', None)
        self.text = kwargs.get('text', None)
        self.theme = kwargs.get('theme', None)
        self.y = kwargs.get('y', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the button. If ``False``, the button will be hidden but
        JavaScript API methods may still be available.

        Defaults to ``True``.

        :returns: Flag indicating whether the button is displayed on the chart.
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
    def text(self) -> Optional[str]:
        """The text to display on the button.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @property
    def theme(self) -> Optional[ButtonTheme]:
        """Configuration of the theme and styling to apply to the button.

        :rtype: :class:`ButtonTheme` or :obj:`None <python:None>`
        """
        return self._theme

    @theme.setter
    @class_sensitive(ButtonTheme)
    def theme(self, value):
        self._theme = value

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The vertical offset of the button's position relative to its ``verticalAlign``
        setting. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'text': as_dict.get('text', None),
            'theme': as_dict.get('theme', None),
            'y': as_dict.get('y', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'text': self.text,
            'theme': self.theme,
            'y': self.y
        }

        return untrimmed


class ContextButtonConfiguration(ButtonConfiguration):
    """Configuration options that apply to the Context Menu button."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._menu_class_name = None
        self._menu_items = None
        self._onclick = None
        self._symbol = None
        self._symbol_fill = None
        self._title_key = None
        self._x = None

        self.class_name = kwargs.get('class_name', None)
        self.menu_class_name = kwargs.get('menu_class_name', None)
        self.menu_items = kwargs.get('menu_items', None)
        self.onclick = kwargs.get('onclick', None)
        self.symbol = kwargs.get('symbol', None)
        self.symbol_fill = kwargs.get('symbol_fill', None)
        self.title_key = kwargs.get('title_key', None)
        self.x = kwargs.get('x', None)

        super().__init__(**kwargs)

    @property
    def class_name(self) -> Optional[str]:
        f"""The class name of the context button. Defaults to
        ``'{constants.DEFAULT_CONTEXT_BUTTON_CLASS_NAME}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def menu_class_name(self) -> Optional[str]:
        f"""The class name of the context menu that appears from the button. Defaults to
        ``'{constants.DEFAULT_CONTEXT_MENU_CLASS_NAME}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._menu_class_name

    @menu_class_name.setter
    def menu_class_name(self, value):
        self._menu_class_name = validators.string(value, allow_empty = True)

    @property
    def menu_items(self) -> Optional[List[str]]:
        f"""A collection of strings pointing to config options for the menu items.

        The config options are defined in the :class:`Exporting.menu_item_definitions`
        option.

        .. note::

          By default, the context menu contains "View in fullscreen" and "Print" menu
          items, plus one menu item for each of the available export types.

        Defaults to:

        .. code-block:: python

          {constants.DEFAULT_CONTEXT_MENU_ITEMS}

        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._menu_items

    @menu_items.setter
    def menu_items(self, value):
        if value is None:
            self._menu_items = None
        else:
            if not checkers.is_iterable(value):
                raise errors.HighchartsValueError(f'menu_items expects an iterable, but '
                                                  f'received: {value.__class__.__name__}')
            for item in value:
                if not isinstance(item, str):
                    raise errors.HighchartsValueError(f'specific menu items must be '
                                                      f'strings, but received: '
                                                      f'{item.__class__.__name}')

            self._menu_items = value

    @property
    def onclick(self) -> Optional[CallbackFunction]:
        """JavaScript event callback function which fires when the button is clicked.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._onclick

    @onclick.setter
    @class_sensitive(CallbackFunction)
    def onclick(self, value):
        self._onclick = value

    @property
    def symbol(self) -> Optional[str]:
        """The symbol to display on the button. Defaults to ``'menu'``.

        Points to a definition function in the JavaScript ``Highcharts.Renderer.symbols``
        collection.

        The default menu function is part of the exporting module. Possible values are:

          * ``"circle"``
          * ``"square"``
          * ``"diamond"``
          * ``"triangle"``
          * ``"triangle-down"``
          * ``"menu"``
          * ``"menuball"``
          * or a custom shape

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = validators.string(value, allow_empty = True)

    @property
    def symbol_fill(self) -> Optional[str]:
        """The color to use for the symbol. Defaults to ``'#666666'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._symbol_fill

    @symbol_fill.setter
    def symbol_fill(self, value):
        self._symbol_fill = validators.string(value, allow_empty = True)

    @property
    def title_key(self) -> Optional[str]:
        """The key to a :class:`Options.language` option setting that is used for the
        button's title tooltip.

        When the key is ``'contextButtonTitle'``, it refers to
        ``language.contextButtonTitle``, whose value defaults to ``"Chart context menu"``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._title_key

    @title_key.setter
    def title_key(self, value):
        self._title_key = validators.string(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The horizontal offset of the button's position relative to its ``align``
        setting. Defaults to ``-10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'enabled': as_dict.get('enabled', None),
            'menu_class_name': as_dict.get('menuClassName', None),
            'menu_items': as_dict.get('menuItems', None),
            'onclick': as_dict.get('onclick', None),
            'symbol': as_dict.get('symbol', None),
            'symbol_fill': as_dict.get('symbolFill', None),
            'text': as_dict.get('text', None),
            'theme': as_dict.get('theme', None),
            'title_key': as_dict.get('titleKey', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'enabled': self.enabled,
            'menuClassName': self.menu_class_name,
            'menuItems': self.menu_items,
            'onclick': self.onclick,
            'symbol': self.symbol,
            'symbolFill': self.symbol_fill,
            'text': self.text,
            'theme': self.theme,
            'titleKey': self.title_key,
            'x': self.x,
            'y': self.y
        }

        return untrimmed


class ExportingButtons(JavaScriptDict):
    """Special :class:`dict <python:dict>` class used to construct a collection of
    Highcharts button configurations. Each key represents the identifier of a button,
    while the object is a configuration of that button's settings.

    Keys are validated to be valid variable names, while each value is validated to be a
    :class:`ButtonConfiguration`.

    """
    _valid_value_types = ButtonConfiguration
    _allow_empty_value = True
