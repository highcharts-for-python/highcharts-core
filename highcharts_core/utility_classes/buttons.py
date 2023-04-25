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

from highcharts_core import constants, errors, utility_functions
from highcharts_core.decorators import validate_types, class_sensitive
from highcharts_core.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


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


class CollapseButtonConfiguration(HighchartsMeta):
    """Configuration options that apply to the Collapse button used in certain series types."""
    
    def __init__(self, **kwargs):
        self._enabled = None
        self._height = None
        self._line_width = None
        self._only_on_hover = None
        self._shape = None
        self._style = None
        self._width = None
        self._x = None
        self._y = None
        
        self.enabled = kwargs.get('enabled', None)
        self.height = kwargs.get('height', None)
        self.line_width = kwargs.get('line_width', None)
        self.only_on_hover = kwargs.get('only_on_hover', None)
        self.shape = kwargs.get('shape', None)
        self.style = kwargs.get('style', None)
        self.width = kwargs.get('width', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
        
    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the button. If ``False``, the button will be hidden.

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
    def height(self) -> Optional[int | float | Decimal]:
        """The height of the button, expressed in pixels. Defaults to ``10``.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height
    
    @height.setter
    def height(self, value):
        if value is None:
            self._height = None
        else:
            self._height = validators.numeric(value, 
                                              allow_empty = False,
                                              minimum = 0)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The line_width of the button, expressed in pixels. Defaults to ``1``.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width
    
    @line_width.setter
    def line_width(self, value):
        if value is None:
            self._line_width = None
        else:
            self._line_width = validators.numeric(value, 
                                                  allow_empty = False,
                                                  minimum = 0)

    @property
    def only_on_hover(self) -> Optional[bool]:
        """Whether the button should be visible only when the node is hovered. Defaults to ``True``.
        
        .. note::

          When set to ``True``, the button is hidden for uncollapsed nodes and shown for collapsed nodes.
    
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._only_on_hover
    
    @only_on_hover.setter
    def only_on_hover(self, value):
        if value is None:
            self._only_on_hover = None
        else:
            self._only_on_hover = bool(value)
            
    @property
    def shape(self) -> Optional[str]:
        """The symbol to use on the collapse button. Defaults to ``'circle'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._shape
    
    @shape.setter
    def shape(self, value):
        self._shape = validators.string(value, allow_empty = True)

    @property
    def style(self) -> Optional[dict]:
        """CSS styles for the collapse button.
        
        .. note::
        
          In styled mode, the collapse button style is given in the ``.highcharts-collapse-button`` CSS class.
          
        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._value = validators.dict(value, allow_empty = True)
        
    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width of the button, expressed in pixels. Defaults to ``10``.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = validators.numeric(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The horizontal offset of the button's position. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The vertical offset of the button's position. Defaults to ``0``.

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
            'height': as_dict.get('height', None),
            'line_width': as_dict.get('lineWidth', None),
            'only_on_hover': as_dict.get('onlyOnHover', None),
            'shape': as_dict.get('shape', None),
            'style': as_dict.get('style', None),
            'width': as_dict.get('width', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'height': self.height,
            'lineWidth': self.line_width,
            'onlyOnHover': self.only_on_hover,
            'shape': self.shape,
            'style': self.style,
            'width': self.width,
            'x': self.x,
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
        """The class name of the context button. Defaults to
        ``'highcharts-contextbutton'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def menu_class_name(self) -> Optional[str]:
        """The class name of the context menu that appears from the button. Defaults to
        ``'highcharts-contextmenu'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._menu_class_name

    @menu_class_name.setter
    def menu_class_name(self, value):
        self._menu_class_name = validators.string(value, allow_empty = True)

    @property
    def menu_items(self) -> Optional[List[str]]:
        """A collection of strings pointing to config options for the menu items.

        The config options are defined in the :class:`Exporting.menu_item_definitions`
        option.

        .. note::

          By default, the context menu contains "View in fullscreen" and "Print" menu
          items, plus one menu item for each of the available export types.

        Defaults to:

        .. code-block:: python

          [
              "viewFullscreen",
              "printChart",
              "separator",
              "downloadPNG",
              "downloadJPEG",
              "downloadPDF",
              "downloadSVG"
          ]

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
    
    def __init__(self, **kwargs):
        context_button = kwargs.pop('context_button', 
                                    None) or kwargs.pop('contextButton', 
                                                        None)
        if isinstance(context_button, constants.EnforcedNullType):
            context_button = None
        elif not context_button:
            context_button = ContextButtonConfiguration()
        elif isinstance(context_button, ButtonConfiguration):
            pass
        elif isinstance(context_button, dict):
            context_button = ContextButtonConfiguration.from_dict(context_button)
        elif isinstance(context_button, str):
            context_button = ContextButtonConfiguration.from_json(context_button)

        super().__init__(**kwargs)

        self['contextButton'] = context_button

    def __setitem__(self, key, item):
        if key == 'context_button':
            key = 'contextButton'

        validate_key = False
        try:
            validate_key = key not in self
        except AttributeError:
            validate_key = True

        if validate_key:
            try:
                key = validators.variable_name(key, allow_empty = False)
            except validator_errors.InvalidVariableNameError as error:
                if '-' in key:
                    try:
                        test_key = key.replace('-', '_')
                        validators.variable_name(test_key, allow_empty = False)
                    except validator_errors.InvalidVariableNameError:
                        raise error
                else:
                    raise error

        if self._valid_value_types:
            try:
                item = validate_types(item,
                                      types = self._valid_value_types,
                                      allow_none = self._allow_empty_value)
            except errors.HighchartsValueError as error:
                if self._allow_empty_value and not item:
                    item = None
                else:
                    try:
                        item = self._valid_value_types(item)
                    except (TypeError, ValueError, AttributeError):
                        raise error

        super().__setitem__(key, item)

    def __getitem__(self, key):
        if key == 'context_button':
            key = 'contextButton'
            
        return super().__getitem__(key)