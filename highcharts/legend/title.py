from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class LegendTitle(HighchartsMeta):
    """A title to be added on top of the legend."""

    def __init__(self, **kwargs):
        self._style = None
        self._text = None

        self.style = kwargs.pop('style', constants.DEFAULT_LEGEND.get('title',
                                                                      {}).get('style'))
        self.style = kwargs.pop('text', None)

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the title. Defaults to
        ``'{constants.DEFAULT_LEGEND.get('title', {}).get('style')}'``.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @property
    def text(self) -> Optional[str]:
        """A text or HTML string for the tite.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'style': as_dict.pop('style', constants.DEFAULT_LEGEND.get('title',
                                                                       {}).get('style')),
            'text': as_dict.pop('text', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'style': self.style,
            'text': self.text
        }

        return self.trim_dict(untrimmed)
