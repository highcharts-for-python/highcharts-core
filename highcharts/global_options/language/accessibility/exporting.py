from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class ExportingLanguageOptions(HighchartsMeta):
    """Exporting menu format strings for use in the accessibility module."""

    def __init__(self, **kwargs):
        self._chart_menu_label = None
        self._menu_button_label = None

        self.chart_menu_label = kwargs.pop('chart_menu_label',
                                           constants.DEFAULT_LANG_ACS_EXPORTING_CHART_MENU_LABEL)
        self.menu_button_label = kwargs.pop('menu_button_label',
                                            constants.DEFAULT_LANG_ACS_EXPORTING_MENU_BTN_LABEL)

    @property
    def chart_menu_label(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_EXPORTING_CHART_MENU_LABEL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._chart_menu_label

    @chart_menu_label.setter
    def chart_menu_label(self, value):
        if value == '':
            self._chart_menu_label = ''
        else:
            self._chart_menu_label = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_EXPORTING_CHART_MENU_LABEL

    @property
    def menu_button_label(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_EXPORTING_MENU_BTN_LABEL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._menu_button_label

    @menu_button_label.setter
    def menu_button_label(self, value):
        if value == '':
            self._menu_button_label = ''
        else:
            self._menu_button_label = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_EXPORTING_MENU_BTN_LABEL

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'chart_menu_label': as_dict.pop('chartMenuLabel',
                                               constants.DEFAULT_LANG_ACS_EXPORTING_CHART_MENU_LABEL),
            'menu_button_label': as_dict.pop('menuButtonLabel',
                                                constants.DEFAULT_LANG_ACS_EXPORTING_MENU_BTN_LABEL)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'chartMenuLabel': self.chart_menu_label,
            'menuButtonLabel': self.menu_button_label
        }

        return self.trim_dict(untrimmed)
