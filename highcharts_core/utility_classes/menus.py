from typing import Optional
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

import esprima
from esprima.error_handler import Error as ParseError

from validator_collection import validators, errors as validator_errors

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.js_literal_functions import assemble_js_literal, serialize_to_js_literal


class MenuItem(HighchartsMeta):
    """Configuration for an item that appears in a context menu."""

    def __init__(self, **kwargs):
        self._onclick = None
        self._text = None
        self._text_key = None
        self._separator = False

        self.onclick = kwargs.get('onclick', None)
        self.text = kwargs.get('text', None)
        self.text_key = kwargs.get('text_key', None)
        self.separator = kwargs.get('separator', None)

    @property
    def onclick(self) -> Optional[CallbackFunction]:
        """JavaScript event callback function which fires when the menu item is clicked.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._onclick

    @onclick.setter
    @class_sensitive(CallbackFunction)
    def onclick(self, value):
        self._onclick = value

    @property
    def text(self) -> Optional[str]:
        """The text to display for the menu item.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @property
    def text_key(self) -> Optional[str]:
        """If internationalization is required, the key to a language string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text_key

    @text_key.setter
    def text_key(self, value):
        self._text_key = validators.string(value, allow_empty = True)

    @property
    def separator(self) -> Optional[bool]:
        """If ``True``, indicates that the item should be rendered as a separator.
        Defaults to ``False``, but may also be :obj:`None <python:None>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._separator

    @separator.setter
    def separator(self, value):
        if value is False or value is None:
            self._separator = value
        elif value:
            self._separator = True
        else:
            self._separator = False

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'onclick': as_dict.get('onclick', None),
            'text': as_dict.get('text', None),
            'text_key': as_dict.get('textKey', None),
            'separator': as_dict.get('separator', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'onclick': self.onclick,
            'text': self.text,
            'textKey': self.text_key,
            'separator': self.separator
        }

        return untrimmed


class MenuObject(JavaScriptDict):
    """Special :class:`dict <python:dict>` class used to construct a Highcharts menu
    configuration. Each key represents the identifier of a menu item, while the object
    is a configuration of that menu item's settings.

    Keys are validated to be valid variable names, while each value is validated to be a
    :class:`MenuItem`.

    """
    _valid_value_types = MenuItem
    _allow_empty_value = False
