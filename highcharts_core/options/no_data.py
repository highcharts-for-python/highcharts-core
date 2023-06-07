from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.ast import AttributeObject
from highcharts_core.utility_classes.position import Position


class NoData(HighchartsMeta):
    """Options for displaying a message like "No data to display".

    .. warning::

      This feature requires the file ``no-data-to-display.js`` to be loaded in the
      page.

    .. tip::

      The actual text to display is set in the :meth:`language <Options.language>`
      options.

    """

    def __init__(self, **kwargs):
        self._attr = None
        self._position = None
        self._style = None
        self._use_html = None

        self.attr = kwargs.get('attr', None)
        self.position = kwargs.get('position', None)
        self.style = kwargs.get('style', None)
        self.use_html = kwargs.get('use_html', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'noData'

    @property
    def attr(self) -> Optional[AttributeObject]:
        """An object of additional SVG attributes for the no-data label.

        :rtype: :class:`AttributeObject` or :obj:`None <python:None>`
        """
        return self._attr

    @attr.setter
    @class_sensitive(AttributeObject)
    def attr(self, value):
        self._attr = value

    @property
    def position(self) -> Optional[Position]:
        """The position of the no-data label, relative to the plot area.

        :rtype: :class:`Position` or :obj:`None <python:None>`
        """
        return self._position

    @position.setter
    @class_sensitive(Position)
    def position(self, value):
        self._position = value

    @property
    def style(self) -> Optional[str]:
        """CSS styles to apply to the no-data label.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True, coerce_value = True)

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, inserts the label as HTML. If ``False``, inserts the label as
        pseudo-HTML rendered with SVG. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        if value is None:
            self._use_html = None
        else:
            self._use_html = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'attr': as_dict.get('attr', None),
            'position': as_dict.get('position', None),
            'style': as_dict.get('style', None),
            'use_html': as_dict.get('useHTML', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'attr': self.attr,
            'position': self.position,
            'style': self.style,
            'useHTML': self.use_html
        }

        return untrimmed
