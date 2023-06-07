import tempfile
import os
from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class Data(HighchartsMeta):
    """The ``data`` property provides a simplified interface for adding data to a
    chart from sources like CVS, HTML tables, or grid views. See also
    `the tutorial article on the Data module <https://www.highcharts.com/docs/working-with-data/data-module>`_.

    .. warning::

      It requires the ``modules/data.js`` file to be loaded in the browser / client.

    .. warning::

      Please note that the default way of adding data in Highcharts, without the need
      of a module, is through the ``series.data`` property.

    """

    def __init__(self, **kwargs):
        self._before_parse = None
        self._columns = None
        self._columns_url = None
        self._complete = None
        self._csv = None
        self._csv_url = None
        self._data_refresh_rate = None
        self._date_format = None
        self._decimal_point = None
        self._enable_polling = None
        self._end_column = None
        self._end_row = None
        self._first_row_as_names = None
        self._google_api_key = None
        self._google_spreadsheet_key = None
        self._google_spreadsheet_range = None
        self._item_delimiter = None
        self._line_delimiter = None
        self._parsed = None
        self._parse_date = None
        self._rows = None
        self._rows_url = None
        self._series_mapping = None
        self._start_column = None
        self._start_row = None
        self._switch_rows_and_columns = None
        self._table = None

        self.before_parse = kwargs.get('before_parse', None)
        self.columns = kwargs.get('columns', None)
        self.columns_url = kwargs.get('columns_url', None)
        self.complete = kwargs.get('complete', None)
        self.csv = kwargs.get('csv', None)
        self.csv_url = kwargs.get('csv_url', None)
        self.data_refresh_rate = kwargs.get('data_refresh_rate', None)
        self.date_format = kwargs.get('date_format', None)
        self.decimal_point = kwargs.get('decimal_point', None)
        self.enable_polling = kwargs.get('enable_polling', None)
        self.end_column = kwargs.get('end_column', None)
        self.end_row = kwargs.get('end_row', None)
        self.first_row_as_names = kwargs.get('first_row_as_names', None)
        self.google_api_key = kwargs.get('google_api_key', None)
        self.google_spreadsheet_key = kwargs.get('google_spreadsheet_key', None)
        self.google_spreadsheet_range = kwargs.get('google_spreadsheet_range', None)
        self.item_delimiter = kwargs.get('item_delimiter', None)
        self.line_delimiter = kwargs.get('line_delimiter', None)
        self.parsed = kwargs.get('parsed', None)
        self.parse_date = kwargs.get('parse_date', None)
        self.rows = kwargs.get('rows', None)
        self.rows_url = kwargs.get('rows_url', None)
        self.series_mapping = kwargs.get('series_mapping', None)
        self.start_column = kwargs.get('start_column', None)
        self.start_row = kwargs.get('start_row', None)
        self.switch_rows_and_columns = kwargs.get('switch_rows_and_columns', None)
        self.table = kwargs.get('table', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'data'

    @property
    def before_parse(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function that is used to modify the CSV data before it is
        parsed. The function should return a modified version of the CSV string. Defaults
        to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._before_parse

    @before_parse.setter
    @class_sensitive(CallbackFunction)
    def before_parse(self, value):
        self._before_parse = value

    @property
    def columns(self) -> Optional[List[List[int | str | float | Decimal | type(None) | constants.EnforcedNullType]]]:
        """The data itself represented in a tabular form. Expects an iterable of
        iterables, where each second-level iterable represents a column of data. Defaults
        to :obj:`None <python:None>`.

        .. code-block:: python

          my_data = Data()
          my_data.columns = [
            [None, 'Apples', 'Pears', 'Oranges'], # categories
            ['Ola', 1, 4, 3], # first series for "Ola"
            ['Kari', 5, 4, 2] # second series for "Kari"
          ]

        .. note::

          Each cell in the second-level iterable can either be a
          :class:`str <python:str>`, numeric value, :obj:`None <python:None>`, or
          :class:`EnforcedNullType`.

        .. hint::

          Provided that :meth:`Data.switch_rows_and_columns` is not set, the columns will
          be interpreted as series.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of
          :class:`list <python:list>` instances with :class:`str <python:str>`, numeric,
          :obj:`None <python:None>`, or :class:`EnforcedNullType` members
        """
        return self._columns

    @columns.setter
    def columns(self, value):
        if not value:
            self._columns = None
        else:
            value = validators.iterable(value)
            processed_values = []
            for item in value:
                if not item or isinstance(item, constants.EnforcedNullType):
                    processed_values.append(item)
                elif isinstance(item, str):
                    processed_values.append(item)
                else:
                    item = validators.numeric(item)
                    processed_values.append(item)

            self._columns = processed_values

    @property
    def columns_url(self):
        """A URL to a remote JSON dataset, structured as a column array. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Will be fetched when the chart is created using Ajax.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._columns_url

    @columns_url.setter
    def columns_url(self, value):
        if not value:
            self._columns_url = None
        else:
            try:
                self._columns_url = validators.url(value)
            except ValueError as error:
                try:
                    self._columns_url = validators.path(value)
                except ValueError:
                    raise error

    @property
    def complete(self) -> Optional[CallbackFunction]:
        """The JavaScript callback function that is evaluated when the data has finished
        loading (optionally from an external source) and been parsed. The first argument
        passed is a finished chart options object, containing the series. These options
        can be extended with additional options and passed directly to the chart
        constructor. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._complete

    @complete.setter
    @class_sensitive(CallbackFunction)
    def complete(self, value):
        self._complete = value

    @property
    def csv(self) -> Optional[str]:
        """A comma-delimited string to be parsed. Defaults to :obj:`None <python:None>`.

        .. seealso::

          The object has closely-related properties that determine which part of the CSV
          string should be used when constructing the chart and to configure how the CSV
          string should be parsed. In particular, please review:

            * :meth:`Data.start_row`
            * :meth:`Data.start_column`
            * :meth:`Data.end_row`
            * :meth:`Data.end_column`
            * :meth:`Data.line_delimiter`
            * :meth:`Data.item_delimiter`

        .. warning::

          The built-in CSV parser does *not* support all flavours of CSV, so in some cases
          it may be necessary to use an external CSV parser. See
          `this example <https://jsfiddle.net/highcharts/u59176h4/>`_ of parsing a CSV
          through the MIT-licensed `Papa Parse <http://papaparse.com/>`_ library.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._csv

    @csv.setter
    def csv(self, value):
        self._csv = validators.string(value, allow_empty = True)

    @property
    def csv_url(self):
        """A URL to a remote CSV dataset. Defaults to :obj:`None <python:None>`.

        .. note::

          Will be fetched when the chart is created using Ajax.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._csv_url

    @csv_url.setter
    def csv_url(self, value):
        if not value:
            self._csv_url = None
        else:
            try:
                self._csv_url = validators.url(value)
            except ValueError as error:
                try:
                    self._csv_url = validators.path(value)
                except ValueError:
                    raise error

    @property
    def data_refresh_rate(self) -> Optional[int | float | Decimal]:
        """The number of seconds between each poll of data from a remote source configured
        using either :meth:`Data.columns_url`, :meth:`Data.csv_url`,
        :meth:`Data.rows_url`, or :meth:`Data.google_spreadsheet_key`. Defaults to ``1``.

        .. warning::

          Cannot be set to less than ``1``.

        .. note::

          For polling to be enabled, :meth:`Data.enable_polling` must be ``True``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._data_refresh_rate

    @data_refresh_rate.setter
    def data_refresh_rate(self, value):
        self._data_refresh_rate = validators.numeric(value, allow_empty = True)

    @property
    def date_format(self) -> Optional[str]:
        """Indicates the format string to use to parse date values. If
        :obj:`None <python:None>`, defaults to a best-guess based on what format gives
        valid and ordered dates. Defaults to :obj:`None <python:None>`.

        Valid options include:

          * ``'YYYY/mm/dd'``
          * ``'dd/mm/YYYY'``
          * ``'mm/dd/YYYY'``
          * ``'dd/mm/YY'``
          * ``'mm/dd/YY'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._date_format

    @date_format.setter
    def date_format(self, value):
        self._date_format = validators.string(value, allow_empty = True)

    @property
    def decimal_point(self) -> Optional[str]:
        """The decimal point used when parsing number values. Defaults to ``'.'`` if
        :obj:`None <python:None>`.

        .. note::

          If both ``decimal_point`` and :meth:`Data.delimiter` are set to
          :obj:`None <python:None>`, the parser will attempt to deduce the decimal point
          automatically.

        :rtype: :class:`str <python:str>`
        """
        return self._decimal_point

    @decimal_point.setter
    def decimal_point(self, value):
        self._decimal_point = validators.string(value, allow_empty = True)

    @property
    def enable_polling(self) -> Optional[bool]:
        """If ``True``, automatically re-fetches remote datasets every *n* seconds (as
        per :meth:`Data.data_refresh_rate`). Defaults to ``False``.

        .. note::

          This flag only has an impact if remote datasets are in use, as specified by
          any one of:

            * :meth:`Data.columns_url`
            * :meth:`Data.csv_url`
            * :meth:`Data.google_spreadsheet_key`
            * :meth:`Data.rows_url`

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enable_polling

    @enable_polling.setter
    def enable_polling(self, value):
        if value is None:
            self._enable_polling = None
        else:
            self._enable_polling = bool(value)

    @property
    def end_column(self) -> Optional[int]:
        """In tabular input data, the last column (indexed by ``0``) to use. If
        :obj:`None <python:None>`, defaults to the last column that contains data.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._end_column

    @end_column.setter
    def end_column(self, value):
        self._end_column = validators.integer(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def end_row(self) -> Optional[int]:
        """In tabular input data, the last row (indexed by ``0``) to use. If
        :obj:`None <python:None>`, defaults to the last row that contains data.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._end_row

    @end_row.setter
    def end_row(self, value):
        self._end_row = validators.integer(value,
                                           allow_empty = True,
                                           minimum = 0)

    @property
    def first_row_as_names(self) -> Optional[bool]:
        """If ``True``, use the first row of data as series names. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._first_row_as_names

    @first_row_as_names.setter
    def first_row_as_names(self, value):
        if value is None:
            self._first_row_as_names = None
        else:
            self._first_row_as_names = bool(value)

    @property
    def google_api_key(self) -> Optional[str]:
        """The Google Spreadsheet API key required for access. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Be sure to generate your Google Spreadsheet API key at Google's
          `API Services / Credentials <https://console.cloud.google.com/apis/credentials>`_.

        .. warning::

          To load data from Google Sheets, the :meth:`Data.google_spreadsheet_key` must be
          set, and must have access to the spreadsheet indicated by the spreadsheet key.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._google_api_key

    @google_api_key.setter
    def google_api_key(self, value):
        self._google_api_key = validators.string(value, allow_empty = True)

    @property
    def google_spreadsheet_key(self) -> Optional[str]:
        """The key or ``spreadsheetId`` value for the Google
        Sheets spreadsheet from which you wish to load data. Defaults to
        :obj:`None <python:None>`.

        .. hint::

          If you need help finding your spreadsheet key, please review the
          `Google Sheets API Overview <https://developers.google.com/sheets/api/guides/concepts>`_

        .. warning::

          To load data from Google Sheets, the :meth:`Data.google_api_key` must be set,
          and must have access to the spreadsheet indicated by the spreadsheet key.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._google_spreadsheet_key

    @google_spreadsheet_key.setter
    def google_spreadsheet_key(self, value):
        self._google_spreadsheet_key = validators.string(value, allow_empty = True)

    @property
    def google_spreadsheet_range(self) -> Optional[str]:
        """The Google Sheets A1 or R1C1 notation cell range from which to retrieve data.
        Defaults to :obj:`None <python:None>`.

        .. note::

          If set, this property takes precedence over :meth:`Data.start_column`,
          :meth:`Data.end_column`, :meth:`Data.start_row`, and :meth:`Data.end_row`.

        .. hint::

          For more details on how to determine and provide the spreadsheet range, please
          review the relevant
          `Google Sheets API documentation <https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get>`_.

        .. warning::

          To load data from Google Sheets, the :meth:`Data.google_api_key` and
          :meth:`Data.google_spreadsheet_key` must both be set.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._google_spreadsheet_range

    @google_spreadsheet_range.setter
    def google_spreadsheet_range(self, value):
        self._google_spreadsheet_range = validators.string(value, allow_empty = True)

    @property
    def item_delimiter(self) -> Optional[str | bool]:
        """Item or cell delimiter used when parsing CSV data. If
        :obj:`None <python:None>` or ``False``, defaults to the tab character ``\t`` if a
        tab character is found in the CSV string. If no tab character is found, defaults
        to ``','``.

        :rtype: :class:`str <python:str>` or :class:`bool <python:bool>` or
          :obj:`None <python:None>`
        """
        return self._item_delimiter

    @item_delimiter.setter
    def item_delimiter(self, value):
        if value is False:
            self._item_delimiter = False
        else:
            self._item_delimiter = validators.string(value, allow_empty = True)

    @property
    def line_delimiter(self) -> Optional[str]:
        """The string used to delimit records (lines) when parsing CSV data. Defaults to
        :obj:`None <python:None>`, which assumes ``'\\n'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_delimiter

    @line_delimiter.setter
    def line_delimiter(self, value):
        self._line_delimiter = validators.string(value, allow_empty = True)

    @property
    def parsed(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function to access the parsed columns (the
        two-dimentional input data array) directly *before* they are interpreted into
        series data and categories. The function should return ``false`` to stop
        completion, or call (in JavaScript) ``this.complete()`` to continue
        asynchronously. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._parsed

    @parsed.setter
    @class_sensitive(CallbackFunction)
    def parsed(self, value):
        self._parsed = value

    @property
    def parse_date(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function to parse string representations of dates into
        JavaScript timestamps. Should return an integer timestamp on success. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._parse_date

    @parse_date.setter
    @class_sensitive(CallbackFunction)
    def parse_date(self, value):
        self._parse_date = value

    @property
    def rows(self) -> Optional[List[List[int | str | float | Decimal | type(None) | constants.EnforcedNullType]]]:
        """The data itself represented in a tabular form. Expects an iterable of
        iterables, where each second-level iterable represents a row of data. Defaults
        to :obj:`None <python:None>`.

        .. code-block:: python

          my_data = Data()
          my_data.rows = [
            [None, 'Apples', 'Pears', 'Oranges'], # categories
            ['Ola', 1, 4, 3], # first series for "Ola"
            ['Kari', 5, 4, 2] # second series for "Kari"
          ]

        .. note::

          Each cell in the second-level iterable can either be a
          :class:`str <python:str>`, numeric value, :obj:`None <python:None>`, or
          :class:`EnforcedNullType`.

        .. hint::

          Provided that :meth:`Data.switch_rows_and_columns` is not set, the rows will
          be interpreted as series.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of
          :class:`list <python:list>` instances with :class:`str <python:str>`, numeric,
          :obj:`None <python:None>`, or :class:`EnforcedNullType` members
        """
        return self._rows

    @rows.setter
    def rows(self, value):
        if not value:
            self._rows = None
        else:
            value = validators.iterable(value)
            processed_values = []
            for item in value:
                if not item or isinstance(item, constants.EnforcedNullType):
                    processed_values.append(item)
                elif isinstance(item, str):
                    processed_values.append(item)
                else:
                    item = validators.numeric(item)
                    processed_values.append(item)

            self._rows = processed_values

    @property
    def rows_url(self):
        """A URL to a remote JSON dataset, structured as a row array. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Will be fetched when the chart is created using Ajax.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._rows_url

    @rows_url.setter
    def rows_url(self, value):
        if not value:
            self._rows_url = None
        else:
            try:
                self._rows_url = validators.url(value)
            except ValueError as error:
                try:
                    self._rows_url = validators.path(value)
                except ValueError:
                    raise error

    @property
    def series_mapping(self) -> Optional[dict[str, int]]:
        """A dictionary used to indicate where point properties are to be found in the data.
        Property names are the keys, while the values are the column indices indicating where
        in the CSV the data for that point is to be found. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`dict <python:dict>` with :class:`str <python:str>` keys and
          :class:`int <python:int>` values, or :obj:`None <python:None>`.
        """
        return self._series_mapping

    @series_mapping.setter
    def series_mapping(self, value):
        if not value:
            self._series_mapping = None
        else:
            value = validators.dict(value)
            for key in value:
                key = validators.string(value)
                item = value[key]
                item = validators.integer(item)

            self._series_mapping = value

    @property
    def start_column(self) -> Optional[int]:
        """In tabular input data, the first column (indexed by ``0``) to use. If
        :obj:`None <python:None>`, defaults to ``0``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._start_column

    @start_column.setter
    def start_column(self, value):
        self._start_column = validators.integer(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def start_row(self) -> Optional[int]:
        """In tabular input data, the first row (indexed by ``0``) to use. If
        :obj:`None <python:None>`, defaults to ``0``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._start_row

    @start_row.setter
    def start_row(self, value):
        self._start_row = validators.integer(value,
                                             allow_empty = True,
                                             minimum = 0)

    @property
    def switch_rows_and_columns(self) -> Optional[bool]:
        """If ``True``, swiches the interpretation of columns and rows so that
        :meth:`Data.columns` effectively becomes rows of the data while :meth:`Data.rows`
        is interpreted as the series of data. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._switch_rows_and_columns

    @switch_rows_and_columns.setter
    def switch_rows_and_columns(self, value):
        if value is None:
            self._switch_rows_and_columns = None
        else:
            self._switch_rows_and_columns = bool(value)

    @property
    def table(self) -> Optional[str]:
        """An HTML table (in :class:`str <pythoN:str>` form), or the ID of such a table
        found in the browser DOM, which should be parsed to extract the data intended for
        visualization. Defaults to :obj:`None <python:None>`.

        .. seealso::

          The object has closely-related properties that determine which part of the HTML
          table should be used when constructing the chart and to configure how the table
          string should be parsed. In particular, please review:

            * :meth:`Data.start_row`
            * :meth:`Data.start_column`
            * :meth:`Data.end_row`
            * :meth:`Data.end_column`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._table

    @table.setter
    def table(self, value):
        self._table = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'before_parse': as_dict.get('beforeParse', None),
            'columns': as_dict.get('columns', None),
            'columns_url': as_dict.get('columnsURL', None),
            'complete': as_dict.get('complete', None),
            'csv': as_dict.get('csv', None),
            'csv_url': as_dict.get('csvURL', None),
            'data_refresh_rate': as_dict.get('dataRefreshRate', None),
            'date_format': as_dict.get('dateFormat', None),
            'decimal_point': as_dict.get('decimalPoint', None),
            'enable_polling': as_dict.get('enablePolling', None),
            'end_column': as_dict.get('endColumn', None),
            'end_row': as_dict.get('endRow', None),
            'first_row_as_names': as_dict.get('firstRowAsNames', None),
            'google_api_key': as_dict.get('googleAPIKey', None),
            'google_spreadsheet_key': as_dict.get('googleSpreadsheetKey', None),
            'google_spreadsheet_range': as_dict.get('googleSpreadsheetRange', None),
            'item_delimiter': as_dict.get('itemDelimiter', None),
            'line_delimiter': as_dict.get('lineDelimiter', None),
            'parsed': as_dict.get('parsed', None),
            'parse_date': as_dict.get('parseDate', None),
            'rows': as_dict.get('rows', None),
            'rows_url': as_dict.get('rowsURL', None),
            'series_mapping': as_dict.get('seriesMapping', None),
            'start_column': as_dict.get('startColumn', None),
            'start_row': as_dict.get('startRow', None),
            'switch_rows_and_columns': as_dict.get('switchRowsAndColumns', None),
            'table': as_dict.get('table', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'beforeParse': self.before_parse,
            'columns': self.columns,
            'columnsURL': self.columns_url,
            'complete': self.complete,
            'csv': self.csv,
            'csvURL': self.csv_url,
            'dataRefreshRate': self.data_refresh_rate,
            'dateFormat': self.date_format,
            'decimalPoint': self.decimal_point,
            'enablePolling': self.enable_polling,
            'endColumn': self.end_column,
            'endRow': self.end_row,
            'firstRowAsNames': self.first_row_as_names,
            'googleAPIKey': self.google_api_key,
            'googleSpreadsheetKey': self.google_spreadsheet_key,
            'googleSpreadsheetRange': self.google_spreadsheet_range,
            'itemDelimiter': self.item_delimiter,
            'lineDelimiter': self.line_delimiter,
            'parsed': self.parsed,
            'parseDate': self.parse_date,
            'rows': self.rows,
            'rowsURL': self.rows_url,
            'seriesMapping': self.series_mapping,
            'startColumn': self.start_column,
            'startRow': self.start_row,
            'switchRowsAndColumns': self.switch_rows_and_columns,
            'table': self.table,
        }

        return untrimmed

    @classmethod
    def from_pandas(cls,
                    as_df,
                    represent_as = 'csv',
                    data_kwargs = None,
                    pandas_kwargs = None):
        """Create a :class:`Data` instance from a Pandas
        :class:`DataFrame <pandas:DataFrame`.

        :param as_df: The :class:`DataFrame <pandas:DataFrame>` from which to create the
          :class:`Data` instance.
        :type as_df: :class:`DataFrame <pandas:DataFrame>`

        :param represent_as: The format to which ``as_df`` should be serialized. Accepts
          ``'csv'`` or ``'html'``. Defaults to ``'csv'``.
        :type represent_as: :class:`str <python:str>`

        :param data_kwargs: Additional keyword arguments to pass to the :class:`Data`
          constructor (``__init__()``) method. Defaults to :obj:`None <python:None>`.
        :type data_kwargs: :class:`dict <python:dict>`

        :param pandas_kwargs: Keyword arguments to pass to the Pandas
          :meth:`DataFrame.to_csv()` or :meth:`DataFrame.to_html()` methods. Defaults to
          :obj:`None <python:None>`.
        :type pandas_kwargs: :class:`dict <python:dict>`

        .. note::

          To prevent unexpected behavior, if ``represent_as`` is set to ``'csv'``, the
          :meth:`Data.table` property will be set to :obj:`None <python:None>`. If
          ``represent_as`` is set to ``'html'``, the :meth:`Data.csv` property will be set
          to :obj:`None <python:None>`.

        :returns: A :class:`Data` instance.
        """
        from pandas import DataFrame

        if not data_kwargs:
            data_kwargs = {}
        if not pandas_kwargs:
            pandas_kwargs = {}

        if not isinstance(as_df, DataFrame):
            raise errors.HighchartsValueError(f'as_df must be a Pandas DataFrame.'
                                              f'Was: {as_df.__class__.__name__}')

        represent_as = validators.string(represent_as, allow_empty = True) or 'csv'
        represent_as = represent_as.lower()
        if represent_as not in ['csv', 'html']:
            raise errors.HighchartsValueError(f'represent_as expects either "csv" or '
                                              f'"html". Received: {represent_as}')
        if represent_as == 'csv':
            pandas_kwargs['path_or_buf'] = None
            as_csv = as_df.to_csv(**pandas_kwargs)

            data_kwargs['csv'] = as_csv
            data_kwargs['table'] = None
        else:
            pandas_kwargs['buf'] = None
            as_table = as_df.to_html(**pandas_kwargs)

            data_kwargs['csv'] = None
            data_kwargs['table'] = as_table

        return cls(**data_kwargs)

    @classmethod
    def from_pyspark(cls,
                     as_df,
                     data_kwargs = None,
                     pyspark_kwargs = None,
                     consolidation = 'repartition'):
        """Create a :class:`Data` instance from a PySpark
        :class:`DataFrame <pyspark:sql.DataFrame>`.

        .. warning::

          If you are using PySpark, you might be working with extremely large datasets
          (proverbial "big data"). Are you sure you want to be visualizing datasets of
          such size? If so, you should be aware that Highcharts for Python tries to store
          the dataset in the Python environment's memory - **not** on disk.

          If you need to read large datasets from disk, using the
          :meth:`Data.from_pyspark()` is **not** recommended for this reason.


        :param as_df: The :class:`DataFrame <pyspark:sql.DataFrame>` from which to create
          the :class:`Data` instance.
        :type as_df: :class:`pyspark.sql.DataFrame <pyspark:sql.DataFrame>`

        :param data_kwargs: Additional keyword arguments to pass to the :class:`Data`
          constructor (``__init__()``) method. Defaults to :obj:`None <python:None>`.

          .. warning::

            The :meth:`Data.csv` and :meth:`Data.table` properties will be overwritten
            by Highcharts for Python if specified, so don't bother.

        :type data_kwargs: :class:`dict <python:dict>`

        :param pyspark_kwargs: Keyword arguments to pass to the Pyspark
          :meth:`DataFrame.write().csv() <pyspark:sql.DataFrameWriter.csv>` method.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            The ``path`` and ``mode`` arguments will be overwritten by Highcharts for
            Python if specified, so don't bother.

        :type pyspark_kwargs: :class:`dict <python:dict>`

        :param consolidation: If ``'repartition'``, will repartition your PySpark
          :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` into a single unpartitioned
          table prior to the generation of a CSV dataset. If ``'coalesce'``, will
          coalesce your PySpark :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` into
          a single unpartitioned table prior to the generation of a CSV dataset. If
          :obj:`None <python:None>`, will not apply any consolidation to the
          :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`. Defaults to ``'coalesce'``.

          .. hint::

            Setting this value to ``'coalesce'`` is particularly useful if you are working
            on your :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` in multiple Spark
            nodes to prevent loss of data.

            Setting this value to :obj:`None <python:None>` may provide a boost to
            performance, however use with caution as it may lead to unexpected data loss
            or errors if using multiple Spark nodes.

        :returns: A :class:`Data` instance.
        """
        from pyspark.sql import DataFrame

        if not data_kwargs:
            data_kwargs = {}
        if not pyspark_kwargs:
            pyspark_kwargs = {}
            pyspark_kwargs['mode'] = 'overwrite'

        if not isinstance(as_df, DataFrame):
            raise errors.HighchartsValueError(f'as_df must be a Pyspark DataFrame.'
                                              f'Was: {as_df.__class__.__name__}')

        with tempfile.NamedTemporaryFile() as csv_file:
            pyspark_kwargs['path'] = csv_file.name

            if consolidation == 'repartition':
                as_df.repartition(1).write.csv(**pyspark_kwargs)
            elif consolidation:
                as_df.coalesce(1).write.csv(**pyspark_kwargs)
            else:
                as_df.write.csv(**pyspark_kwargs)

            csv_file.seek(0)
            data_kwargs['csv'] = csv_file.read()

        data_kwargs['table'] = None

        return cls(**data_kwargs)
