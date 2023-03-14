from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class FocusBorderStyle(HighchartsMeta):
    """Style options for the focus border drawn around elements while navigating
    through them.

    .. warning::

      Some browsers, in addition, draw their own borders for focused elements.
      These automatic borders can not be styled by Highcharts.

    In styled mode, the border is given the ``.highcharts-focus-border`` class.
    """

    def __init__(self, **kwargs):
        self._border_radius = None
        self._color = None
        self._line_width = None

        self.border_radius = kwargs.get('border_radius', None)
        self.color = kwargs.get('color', None)
        self.line_width = kwargs.get('line_width', None)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The border radius to apply. Defaults to ``3``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def color(self) -> Optional[str]:
        """The color to apply. Defaults to ``'#335cad'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The line width to apply. Defaults to ``2``.

        :rtype: numeric
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'border_radius': as_dict.get('borderRadius', None),
            'color': as_dict.get('color', None),
            'line_width': as_dict.get('lineWidth', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderRadius': self.border_radius,
            'color': self.color,
            'lineWidth': self.line_width
        }
        return untrimmed


class FocusBorder(HighchartsMeta):
    """Options for the focus border drawn around elements while navigating through them.
    """

    def __init__(self, **kwargs):
        self._enabled = None
        self._hide_browser_focus_outline = None
        self._margin = None
        self._style = None

        self.enabled = kwargs.get('enabled', None)
        self.hide_browser_focus_outline = kwargs.get('hide_browser_focus_outline', None)
        self.margin = kwargs.get('margin', None)
        self.style = kwargs.get('style', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the focus border for the chart. Defaults to ``True``.

        :returns: Flag enabling or disabling the focus border around chart elements during
          navigation.
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
    def hide_browser_focus_outline(self) -> Optional[bool]:
        """If ``True``, hides the default browser-generated focus border. Defaults to
        ``True``.

        :returns: Flag indicating whether to hide the default browser focus border.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._hide_browser_focus_outline

    @hide_browser_focus_outline.setter
    def hide_browser_focus_outline(self, value):
        if value is None:
            self._hide_browser_focus_outline = None
        else:
            self._hide_browser_focus_outline = bool(value)

    @property
    def margin(self) -> Optional[int | float | Decimal]:
        """The focus border margin around the elements. Defaults to ``2``.

        :returns: The focus border margin around the elements.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = validators.numeric(value, allow_empty = True)

    @property
    def style(self) -> Optional[FocusBorderStyle]:
        """Style options for the focus border drawn around elements while navigating
        through them.

        .. warning::

          Some browsers, in addition, draw their own borders for focused elements.
          These automatic borders can not be styled by Highcharts.

        In styled mode, the border is given the ``.highcharts-focus-border`` class.

        :returns: Style options for the focus border.
        :rtype: :class:`FocusBorderStyle` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    @class_sensitive(FocusBorderStyle)
    def style(self, value):
        self._style = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'hide_browser_focus_outline': as_dict.get('hideBrowserFocusOutline', None),
            'margin': as_dict.get('margin', None),
            'style': as_dict.get('style', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'hideBrowserFocusOutline': self.hide_browser_focus_outline,
            'margin': self.margin,
            'style': self.style
        }
        return untrimmed
