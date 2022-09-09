from typing import Optional

from validator_collection import validators

from highcharts_python import constants
from highcharts_python.metaclasses import HighchartsMeta


class ExportingLanguageOptions(HighchartsMeta):
    """Exporting menu format strings for use in the accessibility module."""

    def __init__(self, **kwargs):
        self._chart_menu_label = None
        self._menu_button_label = None

        self.chart_menu_label = kwargs.get('chart_menu_label', None)
        self.menu_button_label = kwargs.get('menu_button_label', None)

    @property
    def chart_menu_label(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_EXPORTING_CHART_MENU_LABEL}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._chart_menu_label

    @chart_menu_label.setter
    def chart_menu_label(self, value):
        self._chart_menu_label = validators.string(value, allow_empty = True)

    @property
    def menu_button_label(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_EXPORTING_MENU_BTN_LABEL}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._menu_button_label

    @menu_button_label.setter
    def menu_button_label(self, value):
        self._menu_button_label = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'chart_menu_label': as_dict.get('chartMenuLabel', None),
            'menu_button_label': as_dict.get('menuButtonLabel', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'chartMenuLabel': self.chart_menu_label,
            'menuButtonLabel': self.menu_button_label
        }

        return untrimmed
