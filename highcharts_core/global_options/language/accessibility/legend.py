from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class LegendLanguageOptions(HighchartsMeta):
    """Language options for the legend when used in accessibility mode."""

    def __init__(self, **kwargs):
        self._legend_item = None
        self._legend_label = None
        self._legend_label_no_title = None

        self.legend_item = kwargs.get('legend_item', None)
        self.legend_label = kwargs.get('legend_label', None)
        self.legend_label_no_title = kwargs.get('legend_label_no_title', None)

    @property
    def legend_item(self) -> Optional[str]:
        """Defaults to ``'Show {itemName}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._legend_item

    @legend_item.setter
    def legend_item(self, value):
        self._legend_item = validators.string(value, allow_empty = True)

    @property
    def legend_label(self) -> Optional[str]:
        """Defaults to ``'Chart legend: {legendTitle}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._legend_label

    @legend_label.setter
    def legend_label(self, value):
        self._legend_label = validators.string(value, allow_empty = True)

    @property
    def legend_label_no_title(self) -> Optional[str]:
        """Defaults to ``'Toggle series visibility, {chartTitle}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._legend_label_no_title

    @legend_label_no_title.setter
    def legend_label_no_title(self, value):
        self._legend_label_no_title = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'legend_item': as_dict.get('legendItem', None),
            'legend_label': as_dict.get('legendLabel', None),
            'legend_label_no_title': as_dict.get('legendLabelNoTitle', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'legendItem': self.legend_item,
            'legendLabel': self.legend_label,
            'legendLabelNoTitle': self.legend_label_no_title
        }

        return untrimmed
