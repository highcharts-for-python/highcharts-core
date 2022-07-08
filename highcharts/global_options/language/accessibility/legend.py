from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class LegendLanguageOptions(HighchartsMeta):
    """Language options for the legend when used in accessibility mode."""

    def __init__(self, **kwargs):
        self._legend_item = None
        self._legend_label = None
        self._legend_label_no_title = None

        self.legend_item = kwargs.pop('legend_item',
                                      constants.DEFAULT_LANG_ACS_LEGEND_ITEM)
        self.legend_label = kwargs.pop('legend_label',
                                       constants.DEFAULT_LANG_ACS_LEGEND_LABEL)
        self.legend_label_no_title = kwargs.pop('legend_label_no_title',
                                                constants.DEFAULT_LANG_ACS_LEGEND_LABEL_NO_TITLE)

    @property
    def legend_item(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_LEGEND_ITEM}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._legend_item

    @legend_item.setter
    def legend_item(self, value):
        if value == '':
            self._legend_item = ''
        else:
            self._legend_item = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_LEGEND_ITEM

    @property
    def legend_label(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_LEGEND_LABEL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._legend_label

    @legend_label.setter
    def legend_label(self, value):
        if value == '':
            self._legend_label = ''
        else:
            self._legend_label = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_LEGEND_LABEL

    @property
    def legend_label_no_title(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_LEGEND_LABEL_NO_TITLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._legend_label_no_title

    @legend_label_no_title.setter
    def legend_label_no_title(self, value):
        if value == '':
            self._legend_label_no_title = ''
        else:
            self._legend_label_no_title = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_LEGEND_LABEL_NO_TITLE

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'legend_item': as_dict.pop('legendItem',
                                       constants.DEFAULT_LANG_ACS_LEGEND_ITEM),
            'legend_label': as_dict.pop('legendLabel',
                                        constants.DEFAULT_LANG_ACS_LEGEND_LABEL),
            'legend_label_no_title': as_dict.pop('legendLabelNoTitle',
                                                 constants.DEFAULT_LANG_ACS_LEGEND_LABEL_NO_TITLE)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'legend_item': self.legend_item,
            'legend_label': self.legend_label,
            'legend_label_no_title': self.legend_label_no_title
        }

        return self.trim_dict(untrimmed)
