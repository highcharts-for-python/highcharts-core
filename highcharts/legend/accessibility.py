from typing import Optional

from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class LegendKeyboardNavigation(HighchartsMeta):
    """Options for keyboard navigation of the legend."""

    def __init__(self, **kwargs):
        self._enabled = True

        self.enabled = kwargs.pop('enabled', True)

    @property
    def enabled(self) -> bool:
        """If ``True``, enables keyboard navigation for the legend. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        return cls(enabled = as_dict.pop('enabled', True))

    def to_dict(self):
        return self.trim_dict({
            'enabled': self.enabled
        })


class LegendAccessibilityOptions(HighchartsMeta):
    """Accessibility options for the legend.

    .. note::

      Requires the Accessibility module.

    """

    def __init__(self, **kwargs):
        self._enabled = True
        self._keyboard_navigation = None

        self.enabled = kwargs.pop('enabled', True)
        self.keyboard_navigation = kwargs.pop('keyboard_navigation', None)

    @property
    def enabled(self) -> bool:
        """If ``True``, enables accessibility support for the legend. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
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
    def from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.pop('enabled', True),
            'keyboard_navigation': as_dict.pop('keyboardNavigation', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'enabled': self.enabled,
            'keyboardNavigation': self.keyboard_navigation
        }

        return self.trim_dict(untrimmed)
