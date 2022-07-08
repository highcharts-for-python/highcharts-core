from typing import Optional, List

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.global_options.language.accessibility import AccessibilityLanguageOptions
from highcharts.global_options.language.export_data import ExportDataLanguageOptions
from highcharts.global_options.language.navigation import NavigationLanguageOptions


class Language(HighchartsMeta):
    """Collection of configuration settings for UI strings that can be adapted for
    display in specific languages.

    .. note::

      The :class:`Language` object is a global setting in Highcharts and it *cannot* be
      set on each chart initialization. Instead, it has to be set using (in JavaScript)
      ``Highcharts.setOptions(...)`` before any chart is initialized.

    """

    def __init__(self, **kwargs):
        self._accessibility = None
        self._context_button_title = None
        self._decimal_point = None
        self._download_csv = None
        self._download_jpeg = None
        self._download_pdf = None
        self._download_png = None
        self._download_svg = None
        self._download_xls = None
        self._drillup_text = None
        self._exit_fullscreen = None
        self._export_data = None
        self._hide_data = None
        self._invalid_date = None
        self._loading = None
        self._main_breadcumb = None
        self._months = None
        self._navigation = None
        self._no_data = None
        self._numeric_symbol_magnitude = None
        self._numeric_symbols = None
        self._print_chart = None
        self._reset_zoom = None
        self._reset_zoom_title = None
        self._short_months = None
        self._short_weekdays = None
        self._thousands_separator = None
        self._view_data = None
        self._view_fullscreen = None
        self._weekdays = None

        self.accessibility = kwargs.pop('accessibility', None)
        self.context_button_title = kwargs.pop('context_button_title',
                                               constants.DEFAULT_LANG_CONTEXT_BUTTON_TITLE)
        self.decimal_point = kwargs.pop('decimal_point', '.')
        self.download_csv = kwargs.pop('download_csv',
                                       constants.DEFAULT_LANG_DOWNLOAD_CSV)
        self.download_jpeg = kwargs.pop('download_jpeg',
                                        constants.DEFAULT_LANG_DOWNLOAD_JPEG)
        self.download_pdf = kwargs.pop('download_pdf',
                                       constants.DEFAULT_LANG_DOWNLOAD_PDF)
        self.download_png = kwargs.pop('download_png',
                                       constants.DEFAULT_LANG_DOWNLOAD_PNG)
        self.download_svg = kwargs.pop('download_svg',
                                       constants.DEFAULT_LANG_DOWNLOAD_SVG)
        self.download_xls = kwargs.pop('download_xls',
                                       constants.DEFAULT_LANG_DOWNLOAD_XLS)
        self.drillup_text = kwargs.pop('drillup_text',
                                       constants.DEFAULT_LANG_DRILLUP_TEXT)
        self.exit_fullscreen = kwargs.pop('exit_fullscreen',
                                          constants.DEFAULT_LANG_EXIT_FULLSCREEN)
        self.export_data = kwargs.pop('export_data', None)
        self.hide_data = kwargs.pop('hide_data', constants.DEFALUT_LANG_HIDE_DATA)
        self.invalid_date = kwargs.pop('invalid_date',
                                       constants.DEFAULT_LANG_INVALID_DATA)
        self.loading = kwargs.pop('loading', constants.DEFAULT_LANG_LOADING)
        self.main_breadcumb = kwargs.pop('main_breadcrumb',
                                         constants.DEFAULT_LANG_MAIN_BREADCRUM)
        self.months = kwargs.pop('months', constants.DEFAULT_LANG_MONTHS)
        self.navigation = kwargs.pop('navigation', None)
        self.no_data = kwargs.pop('no_data', constants.DEFAULT_LANG_NO_DATA)
        self.numeric_symbol_magnitude = kwargs.pop('numeric_symbol_magnitude',
                                                   constants.DEFAULT_LANG_NUMERIC_SYMBOL_MAGNITUDE)
        self.numeric_symbols = kwargs.pop('numeric_symbols',
                                          constants.DEFAULT_LANG_NUMERIC_SYMBOLS)
        self.print_chart = kwargs.pop('print_chart', constants.DEFAULT_LANG_PRINT_CHART)
        self.reset_zoom = kwargs.pop('reset_zoom', constants.DEFAULT_LANG_RESET_ZOOM)
        self.reset_zoom_title = kwargs.pop('reset_zoom_title',
                                           constants.DEFAULT_LANG_RESET_ZOOM_TITLE)
        self.short_months = kwargs.pop('short_months',
                                       constants.DEFAULT_LANG_SHORT_MONTHS)
        self.short_weekdays = kwargs.pop('short_weekdays',
                                         constants.DEFAULT_LANG_SHORT_WEEKDAYS)
        self.thousands_separator = kwargs.pop('thousands_separator',
                                              constants.DEFAULT_LANG_THOUSANDS_SEP)
        self.view_data = kwargs.pop('view_data', constants.DEFAULT_LANG_VIEW_DATA)
        self.view_fullscreen = kwargs.pop('view_fullscreen',
                                          constants.DEFAULT_LANG_VIEW_FULLSCREEN)
        self.weekdays = kwargs.pop('weekdays', constants.DEFAULT_LANG_WEEKDAYS)

    @property
    def accessibility(self) -> Optional[AccessibilityLanguageOptions]:
        """Configuration of accessibility strings in the chart.

        .. note::

          Requires the
          `accessibility module <https://code.highcharts.com/modules/accessibility.js>`_
          to be loaded.

          For a description of the module and information on its features, see
          `Accessibility <https://www.highcharts.com/docs/chart-concepts/accessibility>`_.

        .. hint::

          For more dynamic control over the accessibility functionality, see
          :meth:`Accessibility.point.description_formatter`,
          :meth:`Accessibility.series.description_formatter`, and
          :meth:`Accessibility.screen_reader_section.before_chart_formatter`.

        :returns: Accessibility strings used in the chart.
        :rtype: :class:`AccessibilityLanguageOptions` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(AccessibilityLanguageOptions)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def context_button_title(self) -> str:
        f"""The tooltip title for the context menu holding print and export menu items.

        Defaults to ``'{constants.DEFAULT_LANG_CONTEXT_BUTTON_TITLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._context_button_title

    @context_button_title.setter
    def context_button_title(self, value):
        self._context_button_title = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_CONTEXT_BUTTON_TITLE

    @property
    def decimal_point(self) -> str:
        f"""Decimal point used in (JavaScript) ``Highcharts.numberFormat``. Defaults to
        ``'{constants.DEFAULT_LANG_DECIMAL_POINT}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._decimal_point

    @decimal_point.setter
    def decimal_point(self, value):
        self._decimal_point = validators.string(value) or \
            constants.DEFAULT_LANG_DECIMAL_POINT

    @property
    def download_csv(self) -> str:
        f"""Text for the context menu item that allows the user to download a CSV of the
        chart/data. Defaults to ``'{constants.DEFAULT_LANG_DOWNLOAD_CSV}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._download_csv

    @download_csv.setter
    def download_csv(self, value):
        self._download_csv = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_DOWNLOAD_CSV

    @property
    def download_jpeg(self) -> str:
        f"""Text for the context menu item that allows the user to download a JPEG of the
        chart/data. Defaults to ``'{constants.DEFAULT_LANG_DOWNLOAD_CSV}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._download_jpeg

    @download_jpeg.setter
    def download_jpeg(self, value):
        self._download_jpeg = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_DOWNLOAD_JPEG

    @property
    def download_pdf(self) -> str:
        f"""Text for the context menu item that allows the user to download a PDF of the
        chart/data. Defaults to ``'{constants.DEFAULT_LANG_DOWNLOAD_PDF}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._download_pdf

    @download_pdf.setter
    def download_pdf(self, value):
        self._download_pdf = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_DOWNLOAD_PDF

    @property
    def download_png(self) -> str:
        f"""Text for the context menu item that allows the user to download a PNG of the
        chart/data. Defaults to ``'{constants.DEFAULT_LANG_DOWNLOAD_PNG}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._download_png

    @download_png.setter
    def download_png(self, value):
        self._download_png = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_DOWNLOAD_PNG

    @property
    def download_svg(self) -> str:
        f"""Text for the context menu item that allows the user to download an SVG of the
        chart/data. Defaults to ``'{constants.DEFAULT_LANG_DOWNLOAD_SVG}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._download_svg

    @download_svg.setter
    def download_svg(self, value):
        self._download_svg = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_DOWNLOAD_SVG

    @property
    def download_xls(self) -> str:
        f"""Text for the context menu item that allows the user to download a Microsoft
        Excel file  of the chart/data. Defaults to
        ``'{constants.DEFAULT_LANG_DOWNLOAD_XLS}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._download_xls

    @download_xls.setter
    def download_xls(self, value):
        self._download_xls = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_DOWNLOAD_XLS

    @property
    def drillup_text(self) -> Optional[str]:
        """The text for the button that appears when drilling down, linking back to the
        parent series.

        .. note::

          The parent series' name is inserted for ``{series.name}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drillup_text

    @drillup_text.setter
    def drillup_text(self, value):
        self._drillup_text = validators.string(value, allow_empty = True)

    @property
    def exit_fullscreen(self) -> str:
        f"""The text for the menu item to exit the chart from full screen. Defaults to
        ``'{constants.DEFAULT_LANG_EXIT_FULLSCREEN}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._exit_fullscreen

    @exit_fullscreen.setter
    def exit_fullscreen(self, value):
        self._exit_fullscreen = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_EXIT_FULLSCREEN

    @property
    def export_data(self) -> Optional[ExportDataLanguageOptions]:
        """Language strings used in the exported data table.

        :rtype: :class:`ExportDataLanguageOptions` or :obj:`None <python:None>`
        """
        return self._export_data

    @export_data.setter
    @class_sensitive(ExportDataLanguageOptions)
    def export_data(self, value):
        self._export_data = value

    @property
    def hide_data(self) -> str:
        f"""Text used for the hide data table menu item. Defaults to:
        ``'{constants.DEFAULT_LANG_HIDE_DATA}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._hide_data

    @hide_data.setter
    def hide_data(self, value):
        self._hide_data = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_HIDE_DATA

    @property
    def invalid_date(self) -> str:
        f"""Text to show in a date field for invalid dates. Defaults to
        ``'{constants.DEFAULT_LANG_INVALID_DATE}'`` (an empty string).

        :rtype: :class:`str <python:str>`
        """
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_INVALID_DATE

    @property
    def loading(self) -> str:
        f"""The loading text that appears when the chart is set into the loading state
        following a (JavaScript) call to ``chart.showLoading()``. Defaults to
        ``'{constants.DEFAULT_LANG_LOADING}'``.

        :rtype: :class:`str <python:None>`
        """
        return self._loading

    @loading.setter
    def loading(self, value):
        self._loading = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_LOADING

    @property
    def main_breadcrumb(self) -> str:
        """The root item in the breadcrums used when in drilldown mode. Defaults to
        ``'{constants.DEFAULT_LANG_MAIN_BREADCRUMB}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._main_breadcrumb

    @main_breadcrumb.setter
    def main_breadcrum(self, value):
        self._main_breadcrumb = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_MAIN_BREADCRUMB

    @property
    def months(self) -> List[str]:
        f"""An array containing the months names. Defaults to:
        ``{constants.DEFAULT_LANG_MONTHS}``

        .. note::

          Corresponds to the ``%B`` format string in (JavaScript)
          ``Highcharts.dateFormat()``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return self._months

    @months.setter
    def months(self, value):
        if not value:
            self._months = constants.DEFAULT_LANG_MONTHS
        else:
            if not checkers.is_iterable(value):
                raise errors.HighchartsValueError(f'months expects an iterable of strings'
                                                  f'. Received a: '
                                                  f'{value.__class__.__name__}')
            elif len(value) != 12:
                raise errors.HighchartsValueError(f'months expects 12 string values, but'
                                                  f'received: {len(value)}')

            self._months = [validators.string(x) for x in value]

    @property
    def navigation(self) -> Optional[NavigationLanguageOptions]:
        """The Popup strings used in the chart.

        .. note::

          Requires the ``annotations.js`` or ``annotations-advanced.src.js`` module to be
          loaded.

        :rtype: :class:`NavigationLanguageOptions` or :obj:`None <python:None>`
        """
        return self._navigation

    @navigation.setter
    @class_sensitive(NavigationLanguageOptions)
    def navigation(self, value):
        self._navigation = value

    @property
    def no_data(self) -> str:
        f"""The text to display when the chart contains no data. Defaults to
        ``'{constants.DEFAULT_LANG_NO_DATA}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._no_data

    @no_data.setter
    def no_data(self, value):
        self._no_data = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_NO_DATA

    @property
    def numeric_symbol_magnitude(self) -> int:
        """The magnitude of replacements for :meth:`Language.numeric_symbols`
        replacements. Defaults to ``{constants.DEFAULT_LANG_NUMERIC_SYMBOL_MAGNITUDE}``.

        .. hint::

          Use ``10000`` for Japanese, Korean and various Chinese locales, which use
          symbols for 10^4, 10^8 and 10^12.

        :rtype: :class:`int <python:int>`
        """
        return self._numeric_symbol_magnitude

    @numeric_symbol_magnitude.setter
    def numeric_symbol_magnitude(self, value):
        self._numeric_symbol_magnitude = validators.integer(value,
                                                            allow_empty = True,
                                                            minimum = 0,
                                                            coerce_value = True) or \
            constants.DEFAULT_LANG_NUMERIC_SYMBOL_MAGNITUDE

    @property
    def numeric_symbols(self) -> List[str] | constants.EnforcedNullType:
        """:term:`Metric prefixes <Metric Prefix>` used to shorten high numbers in axis
        labels. Defaults to ``{constants.DEFAULT_LANG_NUMERIC_SYMBOLS}``.

        .. note::

          Replacing any of the positions with :obj:`None <python:None>` or
          :class:`constants.EnforcedNullType` causes the full number to be written.
          Setting :meth:`Language.numeric_symbols` as a whole to :obj:`None <python:None>`
          or :class:`constants.EnforcedNullType` disables shortening altogether.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or
          :class:`EnforcedNullType`, or :class:`EnforcedNullType`
        """
        return self._numeric_symbols

    @numeric_symbols.setter
    def numeric_symbols(self, value):
        if not value:
            self._numeric_symbols = constants.EnforcedNull
        else:
            if not checkers.is_iterable(value):
                raise errors.HighchartsValueError(f'numeric_symbols expects an iterable '
                                                  f'of values, but received: '
                                                  f'{value.__class__.__name__}')
            validated = []
            for item in value:
                if item is None or item == constants.EnforcedNull:
                    validated.append(item)
                else:
                    validated.append(validators.string(item))

            self._numeric_symbols = validated

    @property
    def print_chart(self) -> str:
        f"""The text for the menu item to print the chart. Defaults to
        ``'{constants.DEFAULT_LANG_PRINT_CHART}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._print_chart

    @print_chart.setter
    def print_chart(self, value):
        self._print_chart = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_PRINT_CHART

    @property
    def reset_zoom(self) -> str:
        f"""The text for the label of the button to reset the zoom when a chart is zoomed.
        Defaults to ``'{constants.DEFAULT_LANG_RESET_ZOOM}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._reset_zoom

    @reset_zoom.setter
    def reset_zoom(self, value):
        self._reset_zoom = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_RESET_ZOOM

    @property
    def reset_zoom_title(self) -> str:
        f"""The text for the tooltip which appears above the button to reset the zoom when
        a chart is zoomed. Defaults to ``'{constants.DEFAULT_LANG_RESET_ZOOM_TITLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._reset_zoom_title

    @reset_zoom_title.setter
    def reset_zoom_title(self, value):
        self._reset_zoom_title = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_RESET_ZOOM_TITLE

    @property
    def short_months(self) -> List[str]:
        f"""A collection containing the months names in abbreviated form. Defaults to:
        ``{constants.DEFAULT_LANG_SHORT_MONTHS}``.

        .. note::

          Corresponds to the ``%b`` format in (JavaScript) ``Highcharts.dateFormat()``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return self._short_months

    @short_months.setter
    def short_months(self, value):
        if not value:
            self._short_months = constants.DEFAULT_LANG_SHORT_MONTHS
        else:
            if not checkers.is_iterable(value):
                raise errors.HighchartsValueError(f'short_months expects an iterable of '
                                                  f'strings. Received a: '
                                                  f'{value.__class__.__name__}')
            elif len(value) != 12:
                raise errors.HighchartsValueError(f'short_months expects 12 string values'
                                                  f', but received: {len(value)}')

            self._short_months = [validators.string(x) for x in value]

    @property
    def short_weekdays(self) -> Optional[str]:
        """Short week days, starting Sunday.

        If not specified, Highcharts uses the first three letters of the
        :meth:`Language.weekdays` setting.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._short_weekdays

    @short_weekdays.setter
    def short_weekdays(self, value):
        if not value:
            self._short_weekdays = None
        else:
            if not checkers.is_iterable(value):
                raise errors.HighchartsValueError(f'short_weekdays expects an iterable. '
                                                  f'Received: {value.__class__.__name__}')

            self._short_weekdays = [validators.string(x) for x in value]

    @property
    def thousands_separator(self) -> str:
        """The default thousands separator used in the (JavaScript)
        ``Highcharts.numberFormat()`` method unless otherwise specified in the function
        arguments.

        Defaults to a single space character, which is recommended in ISO 31-0 and works
        across Anglo-American and continental European languages.

        :rtype: :class:`str <python:str>`
        """
        return self._thousands_separator

    @thousands_separator.setter
    def thousands_separator(self, value):
        self._thousands_separator = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_THOUSANDS_SEP

    @property
    def view_data(self) -> str:
        f"""The text for the menu item to view the chart's data table. Defaults to:
        ``'{constants.DEFAULT_LANG_VIEW_DATA}'``

        :rtype: :class:`str <python:str>`
        """
        return self._view_data

    @view_data.setter
    def view_data(self, value):
        self._view_data = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_VIEW_DATA

    @property
    def view_fullscreen(self) -> str:
        f"""The text for the menu item to view the chart in fullscreen mode. Defaults to:
        ``'{constants.DEFAULT_LANG_VIEW_FULLSCREEN}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._view_fullscreen

    @view_fullscreen.setter
    def view_fullscreen(self, value):
        self._view_fullscreen = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_VIEW_FULLSCREEN

    @property
    def weekdays(self) -> List[str]:
        f"""An array containing the days of the week, starting with Sunday. Defaults to:
        ``{constants.DEFAULT_LANG_WEEKDAYS}``

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return self._weekdays

    @weekdays.setter
    def weekdays(self, value):
        if not value:
            self._weekdays = constants.DEFAULT_LANG_WEEKDAYS
        else:
            if not checkers.is_iterable(value):
                raise errors.HighchartsValueError(f'weekdays expects an iterable of '
                                                  f'strings. Received a: '
                                                  f'{value.__class__.__name__}')
            elif len(value) != 7:
                raise errors.HighchartsValueError(f'weekdays expects 7 string values, but'
                                                  f'received: {len(value)}')

            self._weekdays = [validators.string(x) for x in value]

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'context_button_title': as_dict.pop('contextButtonTitle',
                                                constants.DEFAULT_LANG_CONTEXT_BUTTON_TITLE),
            'decimal_point': as_dict.pop('decimalPoint', '.'),
            'download_csv': as_dict.pop('downloadCSV',
                                        constants.DEFAULT_LANG_DOWNLOAD_CSV),
            'download_jpeg': as_dict.pop('downloadJPEG',
                                         constants.DEFAULT_LANG_DOWNLOAD_JPEG),
            'download_pdf': as_dict.pop('downloadPDF',
                                        constants.DEFAULT_LANG_DOWNLOAD_PDF),
            'download_png': as_dict.pop('downloadPNG',
                                        constants.DEFAULT_LANG_DOWNLOAD_PNG),
            'download_svg': as_dict.pop('downloadSVG',
                                        constants.DEFAULT_LANG_DOWNLOAD_SVG),
            'download_xls': as_dict.pop('downloadXLS',
                                        constants.DEFAULT_LANG_DOWNLOAD_XLS),
            'drillup_text': as_dict.pop('drillUpText',
                                        constants.DEFAULT_LANG_DRILLUP_TEXT),
            'exit_fullscreen': as_dict.pop('exitFullscreen',
                                        constants.DEFAULT_LANG_EXIT_FULLSCREEN),
            'export_data': as_dict.pop('exportData', None),
            'hide_data': as_dict.pop('hideData', constants.DEFALUT_LANG_HIDE_DATA),
            'invalid_date': as_dict.pop('invalidDate',
                                        constants.DEFAULT_LANG_INVALID_DATA),
            'loading': as_dict.pop('loading', constants.DEFAULT_LANG_LOADING),
            'main_breadcumb': as_dict.pop('mainBreadcrumb',
                                          constants.DEFAULT_LANG_MAIN_BREADCRUM),
            'months': as_dict.pop('months', constants.DEFAULT_LANG_MONTHS),
            'navigation': as_dict.pop('navigation', None),
            'no_data': as_dict.pop('noData', constants.DEFAULT_LANG_NO_DATA),
            'numeric_symbol_magnitude': as_dict.pop('numericSymbolMagnitude',
                                                    constants.DEFAULT_LANG_NUMERIC_SYMBOL_MAGNITUDE),
            'numeric_symbols': as_dict.pop('numericSymbols',
                                           constants.DEFAULT_LANG_NUMERIC_SYMBOLS),
            'print_chart': as_dict.pop('printChart', constants.DEFAULT_LANG_PRINT_CHART),
            'reset_zoom': as_dict.pop('resetZoom', constants.DEFAULT_LANG_RESET_ZOOM),
            'reset_zoom_title': as_dict.pop('resetZoomTitle',
                                            constants.DEFAULT_LANG_RESET_ZOOM_TITLE),
            'short_months': as_dict.pop('shortMonths',
                                        constants.DEFAULT_LANG_SHORT_MONTHS),
            'short_weekdays': as_dict.pop('shortWeekdays',
                                          constants.DEFAULT_LANG_SHORT_WEEKDAYS),
            'thousands_separator': as_dict.pop('thousandsSep',
                                               constants.DEFAULT_LANG_THOUSANDS_SEP),
            'view_data': as_dict.pop('viewData', constants.DEFAULT_LANG_VIEW_DATA),
            'view_fullscreen': as_dict.pop('viewFullscreen',
                                           constants.DEFAULT_LANG_VIEW_FULLSCREEN),
            'weekdays': as_dict.pop('weekdays', constants.DEFAULT_LANG_WEEKDAYS)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'accessibility': self.accessibility,
            'contextButtonTitle': self.context_button_title,
            'decimalPoint': self.decimal_point,
            'downloadCSV': self.download_csv,
            'downloadJPEG': self.download_jpeg,
            'downloadPDF': self.download_pdf,
            'downloadPNG': self.download_png,
            'downloadSVG': self.download_svg,
            'downloadXLS': self.download_xls,
            'drillUpText': self.drillup_text,
            'exitFullscreen': self.exit_fullscreen,
            'exportData': self.export_data,
            'hideData': self.hide_data,
            'invalidDate': self.invalid_date,
            'loading': self.loading,
            'mainBreadcumb': self.main_breadcrumb,
            'months': self.months,
            'navigation': self.navigation,
            'noData': self.no_data,
            'numericSymbolMagnitude': self.numeric_symbol_magnitude,
            'numericSymbols': self.numeric_symbols,
            'printChart': self.print_chart,
            'resetZoom': self.reset_zoom,
            'resetZoomTitle': self.reset_zoom_title,
            'shortMonths': self.short_months,
            'shortWeekdays': self.short_weekdays,
            'thousandsSep': self.thousands_separator,
            'viewData': self.view_data,
            'viewFullscreen': self.view_fullscreen,
            'weekdays': self.weekdays
        }
        return self.trim_dict(untrimmed)
