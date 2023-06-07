from typing import Optional, List

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.global_options.language.accessibility import AccessibilityLanguageOptions
from highcharts_core.global_options.language.export_data import ExportDataLanguageOptions
from highcharts_core.global_options.language.navigation import NavigationLanguageOptions


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
        self._download_midi = None
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
        self._main_breadcrumb = None
        self._months = None
        self._navigation = None
        self._no_data = None
        self._numeric_symbol_magnitude = None
        self._numeric_symbols = None
        self._play_as_sound = None
        self._print_chart = None
        self._reset_zoom = None
        self._reset_zoom_title = None
        self._short_months = None
        self._short_weekdays = None
        self._thousands_separator = None
        self._view_data = None
        self._view_fullscreen = None
        self._weekdays = None

        self.accessibility = kwargs.get('accessibility', None)
        self.context_button_title = kwargs.get('context_button_title', None)
        self.decimal_point = kwargs.get('decimal_point', None)
        self.download_csv = kwargs.get('download_csv', None)
        self.download_jpeg = kwargs.get('download_jpeg', None)
        self.download_midi = kwargs.get('download_midi', None)
        self.download_pdf = kwargs.get('download_pdf', None)
        self.download_png = kwargs.get('download_png', None)
        self.download_svg = kwargs.get('download_svg', None)
        self.download_xls = kwargs.get('download_xls', None)
        self.drillup_text = kwargs.get('drillup_text', None)
        self.exit_fullscreen = kwargs.get('exit_fullscreen', None)
        self.export_data = kwargs.get('export_data', None)
        self.hide_data = kwargs.get('hide_data', None)
        self.invalid_date = kwargs.get('invalid_date', None)
        self.loading = kwargs.get('loading', None)
        self.main_breadcrumb = kwargs.get('main_breadcrumb', None)
        self.months = kwargs.get('months', None)
        self.navigation = kwargs.get('navigation', None)
        self.no_data = kwargs.get('no_data', None)
        self.numeric_symbol_magnitude = kwargs.get('numeric_symbol_magnitude', None)
        self.numeric_symbols = kwargs.get('numeric_symbols', None)
        self.play_as_sound = kwargs.get('play_as_sound', None)
        self.print_chart = kwargs.get('print_chart', None)
        self.reset_zoom = kwargs.get('reset_zoom', None)
        self.reset_zoom_title = kwargs.get('reset_zoom_title', None)
        self.short_months = kwargs.get('short_months', None)
        self.short_weekdays = kwargs.get('short_weekdays', None)
        self.thousands_separator = kwargs.get('thousands_separator', None)
        self.view_data = kwargs.get('view_data', None)
        self.view_fullscreen = kwargs.get('view_fullscreen', None)
        self.weekdays = kwargs.get('weekdays', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'lang'

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
    def context_button_title(self) -> Optional[str]:
        """The tooltip title for the context menu holding print and export menu items.

        Defaults to ``'Chart context menu'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._context_button_title

    @context_button_title.setter
    def context_button_title(self, value):
        self._context_button_title = validators.string(value, allow_empty = True)

    @property
    def decimal_point(self) -> Optional[str]:
        """Decimal point used in (JavaScript) ``Highcharts.numberFormat``. Defaults to
        ``.``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._decimal_point

    @decimal_point.setter
    def decimal_point(self, value):
        self._decimal_point = validators.string(value, allow_empty = True)

    @property
    def download_csv(self) -> Optional[str]:
        """Text for the context menu item that allows the user to download a CSV of the
        chart/data. Defaults to ``'Download CSV'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._download_csv

    @download_csv.setter
    def download_csv(self, value):
        self._download_csv = validators.string(value, allow_empty = True)

    @property
    def download_jpeg(self) -> Optional[str]:
        """Text for the context menu item that allows the user to download a JPEG of the
        chart/data. Defaults to ``'Download JPEG'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._download_jpeg

    @download_jpeg.setter
    def download_jpeg(self, value):
        self._download_jpeg = validators.string(value, allow_empty = True)

    @property
    def download_midi(self) -> Optional[str]:
        """
        .. versionadded:: Highcharts Core for Python v.1.1.0 / Highcharts Core (JS) v.11.0.0
        
          Text for the context menu item that allows the user to download a MIDI of the
          chart/data. Defaults to ``'Download MIDI'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._download_midi

    @download_midi.setter
    def download_midi(self, value):
        self._download_midi = validators.string(value, allow_empty = True)

    @property
    def download_pdf(self) -> Optional[str]:
        """Text for the context menu item that allows the user to download a PDF of the
        chart/data. Defaults to ``'Download PDF'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._download_pdf

    @download_pdf.setter
    def download_pdf(self, value):
        self._download_pdf = validators.string(value, allow_empty = True)

    @property
    def download_png(self) -> Optional[str]:
        """Text for the context menu item that allows the user to download a PNG of the
        chart/data. Defaults to ``'Download PNG'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._download_png

    @download_png.setter
    def download_png(self, value):
        self._download_png = validators.string(value, allow_empty = True)

    @property
    def download_svg(self) -> Optional[str]:
        """Text for the context menu item that allows the user to download an SVG of the
        chart/data. Defaults to ``'Download SVG'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._download_svg

    @download_svg.setter
    def download_svg(self, value):
        self._download_svg = validators.string(value, allow_empty = True)

    @property
    def download_xls(self) -> Optional[str]:
        """Text for the context menu item that allows the user to download a Microsoft
        Excel file  of the chart/data. Defaults to
        ``'Download Excel'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._download_xls

    @download_xls.setter
    def download_xls(self, value):
        self._download_xls = validators.string(value, allow_empty = True)

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
    def exit_fullscreen(self) -> Optional[str]:
        """The text for the menu item to exit the chart from full screen. Defaults to
        ``'Exit from full screen'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._exit_fullscreen

    @exit_fullscreen.setter
    def exit_fullscreen(self, value):
        self._exit_fullscreen = validators.string(value, allow_empty = True)

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
    def hide_data(self) -> Optional[str]:
        """Text used for the hide data table menu item. Defaults to:
        ``'Hide data table'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._hide_data

    @hide_data.setter
    def hide_data(self, value):
        self._hide_data = validators.string(value, allow_empty = True)

    @property
    def invalid_date(self) -> Optional[str]:
        """Text to show in a date field for invalid dates. Defaults to
        ``''`` (an empty string).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = validators.string(value, allow_empty = True)

    @property
    def loading(self) -> Optional[str]:
        """The loading text that appears when the chart is set into the loading state
        following a (JavaScript) call to ``chart.showLoading()``. Defaults to
        ``'Loading...'``.

        :rtype: :class:`str <python:None>`
        """
        return self._loading

    @loading.setter
    def loading(self, value):
        self._loading = validators.string(value, allow_empty = True)

    @property
    def main_breadcrumb(self) -> Optional[str]:
        """The root item in the breadcrums used when in drilldown mode. Defaults to
        ``'Main'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._main_breadcrumb

    @main_breadcrumb.setter
    def main_breadcrumb(self, value):
        self._main_breadcrumb = validators.string(value, allow_empty = True)

    @property
    def months(self) -> Optional[List[str]]:
        """An array containing the months names. Defaults to:

          .. code-block::

            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]

        .. note::

          Corresponds to the ``%B`` format string in (JavaScript)
          ``Highcharts.dateFormat()``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._months

    @months.setter
    def months(self, value):
        if not value:
            self._months = None
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
    def no_data(self) -> Optional[str]:
        """The text to display when the chart contains no data. Defaults to
        ``'No data to display'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._no_data

    @no_data.setter
    def no_data(self, value):
        self._no_data = validators.string(value, allow_empty = True)

    @property
    def numeric_symbol_magnitude(self) -> Optional[int]:
        """The magnitude of replacements for :meth:`Language.numeric_symbols`
        replacements. Defaults to ``1000``.

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
                                                            coerce_value = True)

    @property
    def numeric_symbols(self) -> Optional[List[str] | constants.EnforcedNullType]:
        """:term:`Metric suffixes <Metric Suffix>` used to shorten high numbers in axis
        labels. Defaults to ``["k", "M", "G", "T", "P", "E"]``.

        .. note::

          Replacing any of the positions with :obj:`None <python:None>` or
          :class:`constants.EnforcedNullType` causes the full number to be written.
          Setting :meth:`Language.numeric_symbols` as a whole to :obj:`None <python:None>`
          or :class:`constants.EnforcedNullType` disables shortening altogether.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or
          :class:`EnforcedNullType`, or :class:`EnforcedNullType`, or
          :obj:`None <python:None>`
        """
        return self._numeric_symbols

    @numeric_symbols.setter
    def numeric_symbols(self, value):
        if not value:
            self._numeric_symbols = None
        elif isinstance(value, constants.EnforcedNullType):
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
    def play_as_sound(self) -> Optional[str]:
        """
        .. versionadded:: Highcharts Core for Python v.1.1.0 / Highcharts Core (JS) v.11.0.0

          Text for the context menu item that allows the user to play the chart/data as a sound. 
          Defaults to ``'Play as sound'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._play_as_sound

    @play_as_sound.setter
    def play_as_sound(self, value):
        self._play_as_sound = validators.string(value, allow_empty = True)

    @property
    def print_chart(self) -> Optional[str]:
        """The text for the menu item to print the chart. Defaults to
        ``'Print chart'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._print_chart

    @print_chart.setter
    def print_chart(self, value):
        self._print_chart = validators.string(value, allow_empty = True)

    @property
    def reset_zoom(self) -> Optional[str]:
        """The text for the label of the button to reset the zoom when a chart is zoomed.
        Defaults to ``'Reset zoom'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._reset_zoom

    @reset_zoom.setter
    def reset_zoom(self, value):
        self._reset_zoom = validators.string(value, allow_empty = True)

    @property
    def reset_zoom_title(self) -> Optional[str]:
        """The text for the tooltip which appears above the button to reset the zoom when
        a chart is zoomed. Defaults to ``'Reset zoom level 1:1'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._reset_zoom_title

    @reset_zoom_title.setter
    def reset_zoom_title(self, value):
        self._reset_zoom_title = validators.string(value, allow_empty = True)

    @property
    def short_months(self) -> Optional[List[str]]:
        """A collection containing the months names in abbreviated form. Defaults to:

          .. code-block::

            [
              "Jan",
              "Feb",
              "Mar",
              "Apr",
              "May",
              "Jun",
              "Jul",
              "Aug",
              "Sep",
              "Oct",
              "Nov",
              "Dec"
            ]

        .. note::

          Corresponds to the ``%b`` format in (JavaScript) ``Highcharts.dateFormat()``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._short_months

    @short_months.setter
    def short_months(self, value):
        if not value:
            self._short_months = None
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
    def short_weekdays(self) -> Optional[List[str]]:
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
    def thousands_separator(self) -> Optional[str]:
        """The default thousands separator used in the (JavaScript)
        ``Highcharts.numberFormat()`` method unless otherwise specified in the function
        arguments.

        Defaults to a single space character, which is recommended in ISO 31-0 and works
        across Anglo-American and continental European languages.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._thousands_separator

    @thousands_separator.setter
    def thousands_separator(self, value):
        self._thousands_separator = validators.string(value, allow_empty = True)

    @property
    def view_data(self) -> Optional[str]:
        """The text for the menu item to view the chart's data table. Defaults to:
        ``'View data table'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._view_data

    @view_data.setter
    def view_data(self, value):
        self._view_data = validators.string(value, allow_empty = True)

    @property
    def view_fullscreen(self) -> Optional[str]:
        """The text for the menu item to view the chart in fullscreen mode. Defaults to:
        ``'View in full screen'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._view_fullscreen

    @view_fullscreen.setter
    def view_fullscreen(self, value):
        self._view_fullscreen = validators.string(value, allow_empty = True)

    @property
    def weekdays(self) -> Optional[List[str]]:
        """An array containing the days of the week, starting with Sunday. Defaults to:

        .. code-block::

          [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
          ]

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._weekdays

    @weekdays.setter
    def weekdays(self, value):
        if not value:
            self._weekdays = None
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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'context_button_title': as_dict.get('contextButtonTitle', None),
            'decimal_point': as_dict.get('decimalPoint', None),
            'download_csv': as_dict.get('downloadCSV', None),
            'download_jpeg': as_dict.get('downloadJPEG', None),
            'download_midi': as_dict.get('downloadMIDI', None),
            'download_pdf': as_dict.get('downloadPDF', None),
            'download_png': as_dict.get('downloadPNG', None),
            'download_svg': as_dict.get('downloadSVG', None),
            'download_xls': as_dict.get('downloadXLS', None),
            'drillup_text': as_dict.get('drillUpText', None),
            'exit_fullscreen': as_dict.get('exitFullscreen', None),
            'export_data': as_dict.get('exportData', None),
            'hide_data': as_dict.get('hideData', None),
            'invalid_date': as_dict.get('invalidDate', None),
            'loading': as_dict.get('loading', None),
            'main_breadcrumb': as_dict.get('mainBreadcrumb', None),
            'months': as_dict.get('months', None),
            'navigation': as_dict.get('navigation', None),
            'no_data': as_dict.get('noData', None),
            'numeric_symbol_magnitude': as_dict.get('numericSymbolMagnitude', None),
            'numeric_symbols': as_dict.get('numericSymbols', None),
            'play_as_sound': as_dict.get('playAsSound', None),
            'print_chart': as_dict.get('printChart', None),
            'reset_zoom': as_dict.get('resetZoom', None),
            'reset_zoom_title': as_dict.get('resetZoomTitle', None),
            'short_months': as_dict.get('shortMonths', None),
            'short_weekdays': as_dict.get('shortWeekdays', None),
            'thousands_separator': as_dict.get('thousandsSep', None),
            'view_data': as_dict.get('viewData', None),
            'view_fullscreen': as_dict.get('viewFullscreen', None),
            'weekdays': as_dict.get('weekdays',  None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'contextButtonTitle': self.context_button_title,
            'decimalPoint': self.decimal_point,
            'downloadCSV': self.download_csv,
            'downloadJPEG': self.download_jpeg,
            'downloadMIDI': self.download_midi,
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
            'mainBreadcrumb': self.main_breadcrumb,
            'months': self.months,
            'navigation': self.navigation,
            'noData': self.no_data,
            'numericSymbolMagnitude': self.numeric_symbol_magnitude,
            'numericSymbols': self.numeric_symbols,
            'playAsSound': self.play_as_sound,
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

        return untrimmed


__all__ = [
    'Language',
    'AccessibilityLanguageOptions',
    'ExportDataLanguageOptions',
    'NavigationLanguageOptions'
]
