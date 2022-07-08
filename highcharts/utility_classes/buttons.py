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

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import validate_types, class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradient import Gradient
from highcharts.utility_classes.pattern import Pattern


class ButtonTheme(HighchartsMeta):
    """Settings used to style buttons."""

    def __init__(self, **kwargs):
        self._fill = '#ffffff'
        self._stroke = 'none'

        self.fill = kwargs.pop('fill', '#ffffff')
        self.stroke = kwargs.pop('stroke', 'none')

    @property
    def fill(self) -> Optional[str | Gradient | Pattern]:
        """The color of the button's fill. The default fill exists only to capture hover
        events.

        :rtype: :class:`str <python:str>` (for colors), :class:`Gradient` for gradients,
          :clsas:`Pattern` for pattern definitions, or :obj:`None <python:None>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        if not value:
            self._fill = None
        elif isinstance(value, (Gradient, Pattern)):
            self._fill = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._fill = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill = Gradient.from_dict(value)
                else:
                    self._fill = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._fill = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._fill = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill = Pattern.from_dict(value)
                else:
                    self._fill = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._fill = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def stroke(self) -> Optional[str]:
        """The color of the button's stroke. Defaults to ``'none'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        self._stroke = validators.string(value, allow_empty = True) or 'none'

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'fill': as_dict.pop('fill', '#ffffff'),
            'stroke': as_dict.pop('stroke', 'none')
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'fill': self.fill,
            'stroke': self.stroke
        }

        return self.trim_dict(untrimmed)


class ButtonConfiguration(HighchartsMeta):
    """Configuration of options that apply to a given button."""

    def __init__(self, **kwargs):
        self._enabled = True
        self._text = None
        self._theme = None
        self._y = 0

        self.enabled = kwargs.pop('enabled', True)
        self.text = kwargs.pop('text', None)
        self.theme = kwargs.pop('theme', None)
        self.y = kwargs.pop('y', 0)

    @property
    def enabled(self) -> bool:
        """If ``True``, displays the button. If ``False``, the button will be hidden but
        JavaScript API methods may still be available.

        Defaults to ``True``.

        :returns: Flag indicating whether the button is displayed on the chart.
        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
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
    def from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.pop('enabled', True),
            'text': as_dict.pop('text', None),
            'theme': as_dict.pop('theme', None),
            'y': as_dict.pop('y', 0)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'enabled': self.enabled,
            'text': self.text,
            'theme': self.theme,
            'y': self.y
        }

        return self.trim_dict(untrimmed)


class ContextButtonConfiguration(ButtonConfiguration):
    """Configuration options that apply to the Context Menu button."""

    def __init__(self, **kwargs):
        self._class_name = constants.DEFAULT_CONTEXT_BUTTON_CLASS_NAME
        self._menu_class_name = constants.DEFAULT_CONTEXT_MENU_CLASS_NAME
        self._menu_items = constants.DEFAULT_CONTEXT_MENU_ITEMS
        self._onclick = None
        self._symbol = 'menu'
        self._symbol_fill = '#666666'
        self._title_key = 'contextButtonTitle'
        self._x = -10

        self.class_name = kwargs.pop('class_name',
                                     constants.DEFAULT_CONTEXT_BUTTON_CLASS_NAME)
        self.menu_class_name = kwargs.pop('menu_class_name',
                                          constants.DEFAULT_CONTEXT_MENU_CLASS_NAME)
        self.menu_items = kwargs.pop('menu_items', constants.DEFAULT_CONTEXT_MENU_ITEMS)
        self.onclick = kwargs.pop('onclick', None)
        self.symbol = kwargs.pop('symbol', 'menu')
        self.symbol_fill = kwargs.pop('symbol_fill', '#666666')
        self.title_key = kwargs.pop('title_key', 'contextButtonTitle')
        self.x = kwargs.pop('x', -10)

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
    def onclick(self) -> Optional[str]:
        """JavaScript event callback function which fires when the button is clicked.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._onclick

    @onclick.setter
    def onclick(self, value):
        self._onclick = validators.string(value, allow_empty = True)

    @property
    def symbol(self) -> str:
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

        :rtype: :class:`str <python:str>`
        """
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self.symbol = validators.string(value, allow_empty = True) or 'menu'

    @property
    def symbol_fill(self) -> str:
        """The color to use for the symbol. Defaults to ``'#666666'``.

        :rtype: :class:`str <python:str>`
        """
        return self._symbol_fill

    @symbol_fill.setter
    def symbol_fill(self, value):
        self._symbol_fill = validators.string(value, allow_empty = True) or '#666666'

    @property
    def title_key(self) -> str:
        """The The key to a :class:`Options.language` option setting that is used for the
        button's title tooltip.

        When the key is ``'contextButtonTitle'``, it refers to
        ``language.contextButtonTitle``, whose value defaults to ``"Chart context menu"``.

        :rtype: :class:`str <python:str>`
        """
        return self._title_key

    @title_key.setter
    def title_key(self, value):
        self._title_key = validators.string(value,
                                            allow_empty = True) or 'contextButtonTitle'

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
    def from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.pop('className',
                                      constants.DEFAULT_CONTEXT_BUTTON_CLASS_NAME),
            'enabled': as_dict.pop('enabled', True),
            'menu_class_name': as_dict.pop('menuClassName',
                                           constants.DEFALUT_CONTEXT_MENU_CLASS_NAME),
            'menu_items': as_dict.pop('menuItems', constants.DEFAULT_CONTEXT_MENU_ITEMS),
            'onclick': as_dict.pop('onclick', None),
            'symbol': as_dict.pop('symbol', 'menu'),
            'symbol_fill': as_dict.pop('symbolFill', '#666666'),
            'text': as_dict.pop('text', None),
            'theme': as_dict.pop('theme', None),
            'title_key': as_dict('titleKey', 'contextButtonTitle'),
            'x': as_dict.pop('x', -10),
            'y': as_dict.pop('y', 0)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'className': self.class_name,
            'enabled': self.enabled,
            'menuClassName': self.menu_class_name,
            'menu_items': self.menu_items,
            'onclick': self.onclick,
            'symbol': self.symbol,
            'symbolFill': self.symbol_fill,
            'text': self.text,
            'theme': self.theme,
            'title_key': self.title_key,
            'x': self.x,
            'y': self.y
        }

        return self.trim_dict(untrimmed)


class ExportingButtons(UserDict):
    """Special :class:`dict <python:dict>` class used to construct a collection of
    Highcharts button configurations. Each key represents the identifier of a button,
    while the object is a configuration of that button's settings.

    Keys are validated to be valid variable names, while each value is validated to be a
    :class:`ButtonConfiguration`.

    """

    def __setitem__(self, key, item):
        if key not in self:
            key = validators.variable_name(key, allow_empty = False)

        item = validate_types(item,
                              types = ButtonConfiguration,
                              allow_none = False)

        super().__setitem__(key, item)

    @classmethod
    def from_dict(cls, as_dict):
        """Construct an instance of the class from a :class:`dict <python:dict>` object.

        :param as_dict: A :class:`dict <python:dict>` representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: A Python object representation of ``as_dict``.
        :rtype: :class:`JavaScriptDict`
        """
        as_dict = validators.dict(as_dict, allow_empty = True)
        if not as_dict:
            return cls()

        as_obj = cls()
        for key in as_dict:
            as_obj[key] = as_dict.get(key, None)

        return as_obj

    @classmethod
    def from_json(cls, as_json):
        """Construct an instance of the class from a JSON string.

        :param as_json: The JSON string for the object.
        :type as_json: :class:`str <python:str>` or :class:`bytes <python:bytes>`

        :returns: A Python objcet representation of ``as_json``.
        :rtype: :class:`HighchartsMeta`
        """
        as_dict = json.loads(as_json)

        return cls.from_dict(as_dict)

    def to_dict(self):
        """Generate a :class:`dict <python:dict>` representation of the object compatible
        with the Highcharts JavaScript library.

        .. note::

          The :class:`dict <python:dict>` representation has a property structure and
          naming convention that is *intentionally* consistent with the Highcharts
          JavaScript library. This is not Pythonic, but it makes managing the interplay
          between the two languages much, much simpler.

        :returns: A :class:`dict <python:dict>` representation of the object.
        :rtype: :class:`dict <python:dict>`
        """
        return self.data

    def to_json(self, encoding = 'utf-8'):
        """Generate a JSON string/byte string representation of the object compatible with
        the Highcharts JavaScript library.

        .. note::

          This method will either return a standard :class:`str <python:str>` or a
          :class:`bytes <python:bytes>` object depending on the JSON serialization library
          you are using. For example, if your environment has
          `orjson <https://github.com/ijl/orjson>`_, the result will be a
          :class:`bytes <python:bytes>` representation of the string. For more
          information, please see :doc:`JSON Serialization and Deserialization`.

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf8'``.
        :type encoding: :class:`str <python:str>`

        :returns: A JSON representation of the object compatible with the Highcharts
          library.
        :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`
        """
        as_dict = self.to_dict()
        try:
            as_json = json.dumps(as_dict, encoding = encoding)
        except TypeError:
            as_json = json.dumps(as_dict)

        return as_json
