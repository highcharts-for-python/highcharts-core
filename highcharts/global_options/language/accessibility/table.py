from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class TableLanguageOptions(HighchartsMeta):
    """Accessibility language options for the data table."""

    def __init__(self, **kwargs):
        self._table_summary = None
        self._view_as_data_table_button_text = None

        self.table_summary = kwargs.pop('table_summary',
                                        constants.DEFAULT_LANG_ACS_TABLE_SUMMARY)
        self.view_as_data_table_button_text = kwargs.pop('view_as_data_table_button_text',
                                                         constants.DEFAULT_LANG_ACS_TABLE_VIEW_AS_DATA_TABLE)

    @property
    def table_summary(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_TABLE_SUMMARY}'``

        :rtype: :class:`str <python:str>`
        """
        return self._table_summary

    @table_summary.setter
    def table_summary(self, value):
        if value == '':
            self._table_summary = ''
        else:
            self._table_summary = validators.string(value, allow_empty = True) \
                or constants.DEFAULT_LANG_ACS_TABLE_SUMMARY

    @property
    def view_as_data_table_button_text(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_TABLE_VIEW_AS_DATA_TABLE}'``

        :rtype: :class:`str <python:str>`
        """
        return self._view_as_data_table_button_text

    @view_as_data_table_button_text.setter
    def view_as_data_table_button_text(self, value):
        if value == '':
            self._view_as_data_table_button_text = ''
        else:
            self._view_as_data_table_button_text = validators.string(value, allow_empty = True)\
                or constants.DEFAULT_LANG_ACS_TABLE_VIEW_AS_DATA_TABLE

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'table_summary': as_dict.pop('tableSummary',
                                         constants.DEFAULT_LANG_ACS_TABLE_SUMMARY),
            'view_as_data_table_button_text': as_dict.pop('viewAsDataTableButtonText',
                                                          constants.DEFAULT_LANG_ACS_TABLE_VIEW_AS_DATA_TABLE)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'tableSummary': self.table_summary,
            'viewAsDataTableButtonText': self.view_as_data_table_button_text
        }

        return self.trim_dict(untrimmed)
