from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class TableLanguageOptions(HighchartsMeta):
    """Accessibility language options for the data table."""

    def __init__(self, **kwargs):
        self._table_summary = None
        self._view_as_data_table_button_text = None

        self.table_summary = kwargs.get('table_summary', None)
        self.view_as_data_table_button_text = kwargs.get('view_as_data_table_button_text',
                                                         None)

    @property
    def table_summary(self) -> Optional[str]:
        """Defaults to
        ``'Table representation of chart.'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._table_summary

    @table_summary.setter
    def table_summary(self, value):
        self._table_summary = validators.string(value, allow_empty = True)

    @property
    def view_as_data_table_button_text(self) -> Optional[str]:
        """Defaults to
        ``'View as data table, {chartTitle}'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._view_as_data_table_button_text

    @view_as_data_table_button_text.setter
    def view_as_data_table_button_text(self, value):
        self._view_as_data_table_button_text = validators.string(value,
                                                                 allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'table_summary': as_dict.get('tableSummary', None),
            'view_as_data_table_button_text': as_dict.get('viewAsDataTableButtonText',
                                                          None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'tableSummary': self.table_summary,
            'viewAsDataTableButtonText': self.view_as_data_table_button_text
        }

        return untrimmed
