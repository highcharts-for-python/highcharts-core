from validator_collection import validators

from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class FocusBorder(HighchartsMeta):
    """Options for the focus border drawn around elements while navigating through them.
    """

    def __init__(self, **kwargs):
        self._enabled = True
        self._hide_browser_focus_outline = True
        self._margin = 2
        self._style = None

        self.enabled = kwargs.pop('enabled', True)
        self.hide_browser_focus_outline = kwargs.pop('hide_browser_focus_outline', True)
        self.margin = kwargs.pop('margin', 2)
        self.style = kwargs.pop('style', None)

    @property
    def enabled(self) -> bool:
        """If ``True``, enables the focus border for the chart. Defaults to ``True``.

        :returns: Flag enabling or disabling the focus border around chart elements during
          navigation.
        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @property
    def hide_browser_focus_outline(self) -> bool:
        """If ``True``, hides the default browser-generated focus border. Defaults to
        ``True``.

        :returns: Flag indicating whether to hide the default browser focus border.
        :rtype: :class:`bool <python:bool>`
        """
        return self._hide_browser_focus_outline

    @hide_browser_focus_outline.setter
    def hide_browser_focus_outline(self, value):
        self._hide_browser_focus_outline = bool(value)

    @property
    def margin(self):
        """The focus border margin around the elements. Defaults to ``2``.

        :returns: The focus border margin around the elements.
        :rtype: numeric
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = validators.numeric(value, allow_empty = False)

    @property
    def style(self):
        """Style options for the focus border drawn around elements while navigating
        through them.

        .. warning::

          Some browsers, in addition, draw their own borders for focused elements.
          These automatic borders can not be styled by Highcharts.

        In styled mode, the border is given the ``.highcharts-focus-border`` class.

        :returns: Style options for the focus border.
        :rtype: :class:`FocusBorderStyle`
        """
        return self._style

    @style.setter
    @class_sensitive(FocusBorderStyle)
    def style(self, value):
        self._style = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.pop('enabled', True),
            'hide_browser_focus_outline': as_dict.pop('hideBrowserFocusOutline', True),
            'margin': as_dict.pop('margin', 2),
            'style': as_dict.pop('style', None)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'enabled': self.enabled,
            'hideBrowserFocusOutline': self.hide_browser_focus_outline,
            'margin': self.margin,
            'style': self.style
        }
        return self.trim_dict(untrimmed)


class FocusBorderStyle(HighchartsMeta):
    """Style options for the focus border drawn around elements while navigating
    through them.

    .. warning::

      Some browsers, in addition, draw their own borders for focused elements.
      These automatic borders can not be styled by Highcharts.

    In styled mode, the border is given the ``.highcharts-focus-border`` class.
    """

    def __init__(self, **kwargs):
        self._border_radius = 3
        self._color: '#335cad'
        self._line_width: 2

        self.border_radius = kwargs.pop('border_radius', 3)
        self.color = kwargs.pop('color', '#335cad')
        self.line_width = kwargs.pop('line_width', 2)

    @property
    def border_radius(self):
        """The border radius to apply. Defaults to ``3``.

        :rtype: numeric
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = False)

    @property
    def color(self) -> str:
        """The color to apply. Defaults to ``'#335cad'``.

        :rtype: :class:`str <python:str>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = False)

    @property
    def line_width(self):
        """The line width to apply. Defaults to ``2``.

        :rtype: numeric
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value, allow_empty = False)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'border_radius': as_dict.pop('borderRadius', 3),
            'color': as_dict.pop('color', '#335cad'),
            'line_width': as_dict.pop('lineWidth': 2)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'borderRadius': self.borderRadius,
            'color': self.color,
            'lineWidth': self.line_width
        }
        return self.trim_dict(untrimmed)
