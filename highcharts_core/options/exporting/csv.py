from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class CSVAnnotationOptions(HighchartsMeta):
    """Options for annotations in the export-data table."""

    def __init__(self, **kwargs):
        self._item_delimiter = None
        self._join = None

        self.item_delimiter = kwargs.get('item_delimiter', None)
        self.join = kwargs.get('join', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'exporting.csv.annotations'

    @property
    def item_delimiter(self) -> Optional[str]:
        """The way to mark the separator for annotations combined in one export-data table
        cell. Defaults to ``'; '``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._item_delimiter

    @item_delimiter.setter
    def item_delimiter(self, value):
        self._item_delimiter = validators.string(value, allow_empty = True)

    @property
    def join(self) -> Optional[bool]:
        """If ``True``, then when several labels are assigned to a specific point, they
        will be displayed in one field in the table.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._join

    @join.setter
    def join(self, value):
        if value is None:
            self._join = None
        else:
            self._join = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'item_delimiter': as_dict.get('itemDelimiter', None),
            'join': as_dict.get('join', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'itemDelimiter': self.item_delimiter,
            'join': self.join
        }

        return untrimmed


class ExportingCSV(HighchartsMeta):
    """Options for exporting data to CSV or Microsoft Excel, or displaying the data in
    a HTML table or a JavaScript structure.

    This module adds data export options to the export menu and provides JavaScript
    functions like ``Chart.getCSV()``, ``Chart.getTable()``, ``Chart.getDataRows()``,
    and ``Chart.viewData()``.

    .. warning::

      The XLS converter is limited and only creates a HTML string that is passed for
      download, which works but creates a warning before opening. The workaround for
      this is to use a third party XLSX converter.

    """

    def __init__(self, **kwargs):
        self._annotations = None
        self._column_header_formatter = None
        self._date_format = None
        self._decimal_point = None
        self._item_delimiter = None
        self._line_delimiter = None

        self.annotations = kwargs.get('annotations', None)
        self.column_header_formatter = kwargs.get('column_header_formatter', None)
        self.date_format = kwargs.get('date_format', None)
        self.decimal_point = kwargs.get('decimal_point', None)
        self.item_delimiter = kwargs.get('item_delimiter', None)
        self.line_delimiter = kwargs.get('line_delimiter', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'exporting.csv'

    @property
    def annotations(self) -> Optional[CSVAnnotationOptions]:
        """Options for annotations in the export-data table.

        :rtype: :class:`CSVAnnotationOption`
        """
        return self._annotations

    @annotations.setter
    @class_sensitive(CSVAnnotationOptions)
    def annotations(self, value):
        self._annotations = value

    @property
    def column_header_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript formatter callback function for the column headers.

        The parameters received by the callback function are:

          * ``item`` - The series or axis object
          * ``key`` - The point key, for example y or z
          * ``keyLength`` - The amount of value keys for this item, for example a range
            series has the keys low and high so the key length is 2.

        If :class:`Exporting.use_multi_level_headers` is ``True``, the JavaScript function
        should by default return an object with ``columnTitle`` and
        ``topLevelColumnTitle`` for each key. Columns with the same
        ``topLevelColumnTitle`` have their titles merged into a single cell with
        ``colspan`` for table/Excel export.

        If :class:`Exporting.use_multi_level_headers` is ``False``, or for CSV export, it
        should return the series name, followed by the key if there is more than one key.

        For the axis, it returns the axis title or "Category" or "DateTime" by default.

        To use Highcharts' automatically-suggested header, the callback function should
        return ``False``.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._column_header_formatter

    @column_header_formatter.setter
    @class_sensitive(CallbackFunction)
    def column_header_formatter(self, value):
        self._column_header_formatter = value

    @property
    def date_format(self) -> Optional[str]:
        """The date format to apply to exported dates on a datetime axis. Defaults to
        ``'%Y-%m-%d %H:%M:%S'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._date_format

    @date_format.setter
    def date_format(self, value):
        self._date_format = validators.string(value, allow_empty = True)

    @property
    def decimal_point(self) -> Optional[str | constants.EnforcedNullType]:
        """Decimal point to use for exported CSV. Defaults to the same as the browser
        locale, typically ``'.'`` (English) or ``','`` (German, French, etc).

        Returns either a string value, or an :class:`EnforcedNull <EnforcedNullType>`
        instance.

        :rtype: :class:`str <python:str>` or :class:`EnforcedNullType` or
          :obj:`None <python:None>`
        """
        return self._decimal_point

    @decimal_point.setter
    def decimal_point(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._decimal_point = constants.EnforcedNull
        else:
            self._decimal_point = validators.string(value, allow_empty = True)

    @property
    def item_delimiter(self) -> Optional[str | constants.EnforcedNullType]:
        """The item delimiter in the exported data.

        Use ``';'`` for direct exporting to Excel. If
        :class:`EnforcedNull <constants.EnforcedNullType>`, defaults to a best guess based
        on the browser locale. If the locale decimal point is ``','``, defaults to
        ``';'``. Otherwise, the delimiter defaults to ``','``.

        Returns either a string value, or an :class:`EnforcedNull <EnforcedNullType>`
        instance.

        :rtype: :class:`str <python:str>` or :class:`EnforcedNullType` or
          :obj:`None <python:None>`
        """
        return self._item_delimiter

    @item_delimiter.setter
    def item_delimiter(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._item_delimiter = constants.EnforcedNull
        else:
            self._item_delimiter = validators.string(value, allow_empty = True)

    @property
    def line_delimiter(self) -> Optional[str]:
        """The line delimiter in the exported data. Defaults to a new line.

        Returns either a string value, or an :class:`EnforcedNull <EnforcedNullType>`
        instance.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_delimiter

    @line_delimiter.setter
    def line_delimiter(self, value):
        self._line_delimiter = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'annotations': as_dict.get('annotations', None),
            'column_header_formatter': as_dict.get('columnHeaderFormatter', None),
            'date_format': as_dict.get('dateFormat', None),
            'decimal_point': as_dict.get('decimalPoint', None),
            'item_delimiter': as_dict.get('itemDelimiter', None),
            'line_delimiter': as_dict.get('lineDelimiter', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'annotations': self.annotations,
            'columnHeaderFormatter': self.column_header_formatter,
            'dateFormat': self.date_format,
            'decimalPoint': self.decimal_point,
            'itemDelimiter': self.item_delimiter,
            'lineDelimiter': self.line_delimiter
        }

        return untrimmed
