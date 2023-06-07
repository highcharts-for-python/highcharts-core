from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class LegendKeyboardNavigation(HighchartsMeta):
    """Options for keyboard navigation of the legend."""

    def __init__(self, **kwargs):
        self._enabled = None

        self.enabled = kwargs.get('enabled', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'legend.accessibility.keyboardNavigation'

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables keyboard navigation for the legend. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'enabled': self.enabled
        }


class LegendAccessibilityOptions(HighchartsMeta):
    """Accessibility options for the legend.

    .. note::

      Requires the Accessibility module.

    """

    def __init__(self, **kwargs):
        self._enabled = None
        self._keyboard_navigation = None

        self.enabled = kwargs.get('enabled', None)
        self.keyboard_navigation = kwargs.get('keyboard_navigation', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'legend.accessibility'

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables accessibility support for the legend. Defaults to
        ``True``.

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
    def keyboard_navigation(self) -> Optional[LegendKeyboardNavigation]:
        """Options for keyboard navigation of the legend.

        :rtype: :class:`LegendKeyboardNavigation` or :obj:`None <python:None>`
        """
        return self._keyboard_navigation

    @keyboard_navigation.setter
    @class_sensitive(LegendKeyboardNavigation)
    def keyboard_navigation(self, value):
        self._keyboard_navigation = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'keyboard_navigation': as_dict.get('keyboardNavigation', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'keyboardNavigation': self.keyboard_navigation
        }

        return untrimmed
