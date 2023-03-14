from typing import Optional

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.position import Position


class ResetZoomButtonOptions(HighchartsMeta):
    """Configuration settings for the button that appears after a selection zoom,
    allowing the user to reset zoom."""

    def __init__(self, **kwargs):
        self._position = None
        self._relative_to = None
        self._theme = None

        self.position = kwargs.get('position', None)
        self.relative_to = kwargs.get('relative_to', None)
        self.theme = kwargs.get('theme', None)

    @property
    def position(self) -> Optional[Position]:
        """The position of the button.

        :rtype: :class:`Position` or :obj:`None <python:None>`
        """
        return self._position

    @position.setter
    @class_sensitive(Position)
    def position(self, value):
        self._position = value

    @property
    def relative_to(self) -> Optional[str]:
        """What frame the button placement should be related to. Defaults to ``'plot'``.

        Accepts:

          * ``'plot'``
          * ``'chart'``
          * ``'plotBox'``
          * ``'spacingBox'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._relative_to

    @relative_to.setter
    def relative_to(self, value):
        if not value:
            self._relative_to = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['plot', 'chart', 'plotBox', 'spacingBox']:
                raise errors.HighchartsValueError(f'relative_to accepts "plot", "chart", '
                                                  f'"plotBox", "spacingBox", or None. '
                                                  f'Received: {value}')
            self._relative_to = value

    @property
    def theme(self) -> Optional[dict]:
        """A collection of attributes for the button.

        The object takes SVG attributes like ``fill``, ``stroke``, ``stroke-width`` or
        ``r``, the border radius.

        The theme also supports ``style``, a collection of CSS properties for the text.
        Equivalent attributes for the hover state are given in JavaScript
        ``theme.states.hover``.

        :rtype: :class:`dict <python:dict>`
        """
        return self._theme

    @theme.setter
    def theme(self, value):
        if not value or isinstance(value, constants.EnforcedNullType):
            self._theme = None
        else:
            self._theme = validators.dict(value, allow_empty = False)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'position': as_dict.get('position', None),
            'relative_to': as_dict.get('relativeTo', None),
            'theme': as_dict.get('theme', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'position': self.position,
            'relativeTo': self.relative_to,
            'theme': self.theme
        }

        return untrimmed
