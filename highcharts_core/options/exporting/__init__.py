from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.exporting.csv import ExportingCSV
from highcharts_core.options.exporting.pdf_font import PDFFontOptions
from highcharts_core.utility_classes.menus import MenuObject
from highcharts_core.utility_classes.buttons import ContextButtonConfiguration, \
    ExportingButtons
from highcharts_core.utility_classes.javascript_functions import CallbackFunction

default_context_button = ExportingButtons()
default_context_button['contextButton'] = ContextButtonConfiguration()


class ExportingAccessibilityOptions(HighchartsMeta):
    """Accessibility options for the exporting menu."""

    def __init_(self, **kwargs):
        self._enabled = None

        self.enabled = kwargs.get('enabled', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'exporting.accessibility'

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables accessibility support for the export menu. Defaults to
        ``True``.

        :returns: Flag indicating whether accessibility support is enabled for the
          export menu.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'enabled': self.enabled
        }


class Exporting(HighchartsMeta):
    """Options to configure the export functionality enabled for the chart."""

    def __init__(self, **kwargs):
        self._accessibility = None
        self._allow_html = None
        self._buttons = None
        self._chart_options = None
        self._csv = None
        self._enabled = None
        self._error = None
        self._fallback_to_export_server = None
        self._filename = None
        self._form_attributes = None
        self._lib_url = None
        self._menu_item_definitions = None
        self._pdf_font = None
        self._print_max_width = None
        self._scale = None
        self._show_table = None
        self._source_height = None
        self._source_width = None
        self._table_caption = None
        self._type = None
        self._url = None
        self._use_multi_level_headers = None
        self._use_rowspan_headers = None
        self._width = None

        self.accessibility = kwargs.get('accessibility', None)
        self.allow_html = kwargs.get('allow_html', None)
        self.buttons = kwargs.get('buttons', default_context_button)
        self.chart_options = kwargs.get('chart_options', None)
        self.csv = kwargs.get('csv', None)
        self.enabled = kwargs.get('enabled', None)
        self.error = kwargs.get('error', None)
        self.fallback_to_export_server = kwargs.get('fallback_to_export_server', None)
        self.filename = kwargs.get('filename', None)
        self.form_attributes = kwargs.get('form_attributes', None)
        self.lib_url = kwargs.get('lib_url', None)
        self.menu_item_definitions = kwargs.get('menu_item_definitions', None)
        self.pdf_font = kwargs.get('pdf_font', None)
        self.print_max_width = kwargs.get('print_max_width', None)
        self.scale = kwargs.get('scale', None)
        self.show_table = kwargs.get('show_table', None)
        self.source_height = kwargs.get('source_height', None)
        self.source_width = kwargs.get('source_width', None)
        self.table_caption = kwargs.get('table_caption', None)
        self.type = kwargs.get('type', None)
        self.url = kwargs.get('url', None)
        self.use_multi_level_headers = kwargs.get('use_multi_level_headers', None)
        self.use_rowspan_headers = kwargs.get('use_rowspan_headers', None)
        self.width = kwargs.get('width', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'exporting'

    @property
    def accessibility(self) -> Optional[ExportingAccessibilityOptions]:
        """Accessibility options for the exporting menu.

        :rtype: :class:`ExportingAccessibilityOptions` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(ExportingAccessibilityOptions)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def allow_html(self) -> Optional[bool]:
        """If ``True``, allows HTML inside the chart (added using
        ``.use_html`` properties present on various chart components) to be added 
        directly to the exported image. This allows you to preserve complicated HTML 
        structures like tables or bi-directional text in exported charts.

        Defaults to ``False``.

        .. warning::

          This setting is **EXPERIMENTAL**.

          The HTML is rendered in a ``foreignObject`` tag in the generated SVG. The
          official export server is based on PhantomJS, which supports this, but other 
          SVG clients, like Batik, do not support it. This also applies to downloaded 
          SVG that you want to open in a desktop client.

        :returns: Flag indicating whether to allow HTML in the exported image.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_html

    @allow_html.setter
    def allow_html(self, value):
        if value is None:
            self._allow_html = None
        else:
            self._allow_html = bool(value)

    @property
    def buttons(self) -> Optional[ExportingButtons]:
        """Options for the export related buttons: print and export.

        .. note::

          In addition to the default buttons listed above, custom buttons can be added.
          
        .. warning::
        
          The ``.buttons`` property accepts an 
          :class:`ExportingButtons <highcharts_core.utility_classes.buttons.ExportingButtons>`
          instance as its value. This object is a descendent of the special :class:`JavaScriptDict <highcharts_core.metaclasses.JavaScriptDict>`
          which by default initially contains a ``'context

        :rtype: :class:`ExportingButtons`
        """
        return self._buttons

    @buttons.setter
    @class_sensitive(ExportingButtons)
    def buttons(self, value):
        self._buttons = value

    @property
    def chart_options(self):
        """Additional chart options to be merged into the chart before exporting to an
        image format. This does not apply to printing the chart via the export menu.

        For example, a common use case is to add data labels to improve readability of the
        exported chart, or to add a printer-friendly color scheme to exported PDFs.

        .. warning::

          To avoid a circular import error, this property **REQUIRES** that you supply a
          value that is an :class:`Options` instance (e.g. :class:`HighchartsOptions`,
          :class:`HighchartsStockOptions`, :class:`HighchartsMapsOptions`, etc.). Unlike
          other Highcharts for Python properties, it does **not** accept
          :class:`dict <python:dict>` or JSON (:class:`str <python:dict>`) values.

          Please be sure to either supply it a valid :class:`Options` instance, or the
          value of :obj:`None <python:None>`.

        :rtype: :class:`Options` or :obj:`None <python:None>`
        """
        return self._chart_options

    @chart_options.setter
    def chart_options(self, value):
        if not value:
            self._chart_options = None
        elif not checkers.is_type(value, 'Options'):
            raise errors.InstanceNeededError(f'The Exporting.chart_options property is '
                                             f'one of the few properties in Highcharts '
                                             f'for Python that REQUIRES a Highcharts for '
                                             f'Python instance as its value (or None). '
                                             f'Specifically, you should supply an Options'
                                             f' instance to it, rather than a dict or a '
                                             f'string. The value you supplied was: '
                                             f'{value.__class__.__name}')
        else:
            self._chart_options = value

    @property
    def csv(self) -> Optional[ExportingCSV]:
        """Options for exporting data to CSV or Microsoft Excel, or displaying the data in
        a HTML table or a JavaScript structure.

        This module adds data export options to the export menu and provides JavaScript
        functions like ``Chart.getCSV()``, ``Chart.getTable()``, ``Chart.getDataRows()``,
        and ``Chart.viewData()``.

        .. warning::

          The XLS converter is limited and only creates a HTML string that is passed for
          download, which works but creates a warning before opening. The workaround for
          this is to use a third party XLSX converter.

        :returns: Configuration for exporting data to CSV or Microsoft Excel.
        :rtype: :class:`ExportingCSV` or :obj:`None <python:None>`
        """
        return self._csv

    @csv.setter
    @class_sensitive(ExportingCSV)
    def csv(self, value):
        self._csv = value

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the export context button and allows for exporting the
        chart. If ``False``, the context button will be hidden but JavaScript export API
        methods will still be available.

        Defaults to ``True``.

        :returns: Flag indicating whether the export menu is displayed on the chart.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def error(self) -> Optional[CallbackFunction]:
        """JavaScript function that is called if the offline-exporting module fails to
        export a chart on the client side, and :meth:`Exporting.fallback_to_export_server`
        is disabled.

        If :obj:`None <python:None>`, a JavaScript exception is thrown instead. The
        JavaScript function receives two parameters, the exporting options, and the error
        from the module.

        .. seealso::

          * :meth:`Exporting.fallback_to_export_server`

        :returns: JavaScript function code
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._error

    @error.setter
    @class_sensitive(CallbackFunction)
    def error(self, value):
        self._error = value

    @property
    def fallback_to_export_server(self) -> Optional[bool]:
        """If ``True``, falls back to the export server if the offline-exporting module is
        unable to export the chart on the client side. Defaults to ``True``.

        This happens for certain browsers, and certain features (e.g.
        :meth:`Exporting.allow_html`), depending on the image type exporting to.

        .. hint::

          For very complex charts, it is possible that export can fail in browsers that
          don't support Blob objects, due to data URL length limits. It is recommended to
          define the :meth:`Exporting.error` handler if disabling fallback, in order to
          notify users in case export fails.

        :returns: Flag indicating whether to fall back to the export server if chart
          export fails.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._fallback_to_export_server

    @fallback_to_export_server.setter
    def fallback_to_export_server(self, value):
        if value is None:
            self._fallback_to_export_server = None
        else:
            self._fallback_to_export_server = bool(value)

    @property
    def filename(self) -> Optional[str]:
        """The filename (without file type extension) to use for the exported chart.
        Defaults to ``'{constants.DEFAULT_EXPORTING_FILENAME}'``.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = validators.string(value, allow_empty = True)

    @property
    def form_attributes(self) -> Optional[dict]:
        """An object containing additional key value data for the POST form that sends the
        SVG to the export server.

        For example, a ``target`` can be set to make sure the generated image is received
        in another frame, or a custom ``enctype`` or ``encoding`` can be set.

        :returns: Additional form attributes to supply to the export server.
        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._form_attributes

    @form_attributes.setter
    def form_attributes(self, value):
        self._form_attributes = validators.dict(value, allow_empty = True)

    @property
    def lib_url(self) -> Optional[str]:
        """Path where Highcharts will look for export module dependencies to load on
        demand if they don't already exist on window.

        Should currently point to location of the
        `CanVG <https://github.com/canvg/canvg>`_ library,
        `jsPDF <https://github.com/parallax/jsPDF>`_ and
        `svg2pdf.js <https://github.com/yWorks/svg2pdf.js>`_, which are all required for
        client side export in certain browsers.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._lib_url

    @lib_url.setter
    def lib_url(self, value):
        self._lib_url = validators.url(value, allow_empty = True)

    @property
    def menu_item_definitions(self) -> Optional[MenuObject]:
        """An object consisting of definitions for the menu items in the context menu.

        Each key value pair has a key that is referenced in the ``menu_items`` setting,
        and a value, which is an object with the following properties:

          * ``onclick``: The click handler for the menu item
          * ``text``: The text for the menu item
          * ``textKey``: If internationalization is required, the key to a language 
            string

        .. note::

          Custom text for ``"exitFullScreen"`` can be set only in ``language`` options 
          (it is not a separate button).

        Defaults to:

        .. code-block:: python

          {
              "viewFullscreen": {},
              "printChart": {},
              "separator": {},
              "downloadPNG": {},
              "downloadJPEG": {},
              "downloadPDF": {},
              "downloadSVG": {}
          }

        :returns: Definitions for menu items in the Exporting context menu.
        :rtype: :class:`MenuObject` or :obj:`None <python:None>`
        """
        return self._menu_item_definitions

    @menu_item_definitions.setter
    @class_sensitive(MenuObject)
    def menu_item_definitions(self, value):
        self._menu_item_definitions = value

    @property
    def pdf_font(self) -> Optional[PDFFontOptions]:
        """Settings for a custom font for the exported PDF, when using the
        ``offline-exporting`` module.

        This is used for languages containing non-ASCII characters, like Chinese, Russian,
        Japanese etc.

        As described in the
        `jsPDF docs <https://github.com/parallax/jsPDF#use-of-unicode-characters--utf-8>`_,
        the 14 standard fonts in PDF are limited to the ASCII-codepage. Therefore, in
        order to support other text in the exported PDF, one or more TTF font files have
        to be passed on to the exporting module.

        :returns: Additionl font settings for use in exporting PDFs.
        :rtype: :class:`PDFFontOptions` or :obj:`None <python:None>`
        """
        return self._pdf_font

    @pdf_font.setter
    @class_sensitive(PDFFontOptions)
    def pdf_font(self, value):
        self._pdf_font = value

    @property
    def print_max_width(self) -> Optional[int | float | Decimal]:
        """When printing the chart from the menu item in the burger menu, if the
        on-screen chart exceeds this width, it is resized. After printing or cancelled, it
        is restored.

        By default, set to ``780`` which makes
        the chart fit into typical paper format.

        .. note::

          This does not affect the chart when printing the web page as a whole.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._print_max_width

    @print_max_width.setter
    def print_max_width(self, value):
        self._print_max_width = validators.numeric(value, allow_empty = True)

    @property
    def scale(self) -> Optional[int | float | Decimal]:
        """Defines the scale or zoom factor for the exported image compared to the
        on-screen display. Defaults to ``2``.

        While for instance a 600px wide chart may look good on a website, it will look bad
        in print. The default scale of ``2`` makes this
        chart export to a 1200px PNG or JPG.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = validators.numeric(value, allow_empty = True)

    @property
    def show_table(self) -> Optional[bool]:
        """If ``True``, shows an HTML table below the chart with the chart's current data.
        Defaults to ``False``.

        :returns: Flag indicating whether to display an HTML table with the export.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_table

    @show_table.setter
    def show_table(self, value):
        if value is None:
            self._show_table = None
        else:
            self._show_table = bool(value)

    @property
    def source_height(self) -> Optional[int | float | Decimal]:
        """The height of the original chart when exported, unless an explicit (JavaScript)
        ``chart.height`` is set, or a pixel width is set on the container.

        The height exported raster image is then multiplied by :meth:`Exporting.scale`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._source_height

    @source_height.setter
    def source_height(self, value):
        self._source_height = validators.numeric(value, allow_empty = True)

    @property
    def source_width(self) -> Optional[int | float | Decimal]:
        """The width of the original chart when exported, unless an explicit (JavaScript)
        ``chart.width`` is set, or a pixel width is set on the container.

        The width exported raster image is then multiplied by :meth:`Exporting.scale`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._source_width

    @source_width.setter
    def source_width(self, value):
        self._source_width = validators.numeric(value, allow_empty = True)

    @property
    def table_caption(self) -> Optional[bool | str]:
        """Caption for the data table. If not specified (:obj:`None <python:None>`)`), will
        default to the chart title.

        Also accepts a :class:`bool <python:bool>` value of ``False``, which disables
        the table caption entirely.

        :returns: Flag (value of ``False``) indicating whether to disable the table
          caption, or the text of the table caption to use if different from the chart
          title.
        :rtype: :class:`bool <python:bool>` or :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._table_caption

    @table_caption.setter
    def table_caption(self, value):
        if value is False:
            self._table_caption = False
        elif not value:
            self._table_caption = None
        else:
            self._table_caption = validators.string(value, allow_empty = False)

    @property
    def type(self) -> Optional[str]:
        """Default MIME type for exporting if the JavaScript ``chart.exportChart()`` is
        called without specifying a ``type`` option.

        Accepts:

          * ``'image/png'``
          * ``'image/jpeg'``
          * ``'application/pdf'``
          * ``'image/svg+xml'``

        Defaults to ``'image/png'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['image/png',
                             'image/jpeg',
                             'application/pdf',
                             'image/svg+xml']:
                raise errors.HighchartsValueError(f'type expects a supported export MIME '
                                                  f'type. Received: "{value}"')

            self._type = value

    @property
    def url(self) -> Optional[str]:
        """The URL for the server module converting the SVG string to an image format. By
        default this points to Highchart's free web service:
        ``'{constants.DEFAULT_EXPORTING_URL}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises ValueError: if not a well-formed URL or path
        """
        return self._url

    @url.setter
    def url(self, value):
        try:
            self._url = validators.url(value, allow_empty = True)
        except ValueError:
            self._url = validators.path(value)

    @property
    def use_multi_level_headers(self) -> Optional[bool]:
        """If ``True``, uses multi-level (nested) headers in the exported data table.
        Defaults to ``True``.

        .. warning::

          If
          :meth:`Exporting.csv.column_header_formatter <ExportingCSV.column_header_formatter>`
          is specified, then the formatter must return objects for multi-level headers to
          work properly.

        :returns: Flag indicating whether to use multi-level headers in the data table.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_multi_level_headers

    @use_multi_level_headers.setter
    def use_multi_level_headers(self, value):
        if value is None:
            self._use_multi_level_headers = None
        else:
            self._use_multi_level_headers = bool(value)

    @property
    def use_rowspan_headers(self) -> Optional[bool]:
        """If ``True`` and using multi-level headers, uses rowspans in the data table for
        headers that only have one level. Defaults to ``True``.

        :returns: Flag indicating whether to use rowspans for single-level headers in a
          data table using multi-level headers.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_rowspan_headers

    @use_rowspan_headers.setter
    def use_rowspan_headers(self, value):
        if value is None:
            self._use_rowspan_headers = None
        else:
            self._use_rowspan_headers = bool(value)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """An explicitly set pixel width for charts exported to PNG or JPG. Defaults to
        :obj:`None <python:None>`.

        .. note::

          If not specified (:obj:`None <python:None>`), the default pixel
          width is a function of the :meth:`Chart.width` or :meth:`Exporting.source_width`
          and :meth:`Exporting.scale`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_html': as_dict.get('allowHTML', None),
            'buttons': as_dict.get('buttons', None),
            'chart_options': as_dict.get('chartOptions', None),
            'csv': as_dict.get('csv', None),
            'enabled': as_dict.get('enabled', None),
            'error': as_dict.get('error', None),
            'fallback_to_export_server': as_dict.get('fallbackToExportServer', None),
            'filename': as_dict.get('filename', None),
            'form_attributes': as_dict.get('formAttributes', None),
            'lib_url': as_dict.get('libURL', None),
            'menu_item_definitions': as_dict.get('menuItemDefinitions', None),
            'pdf_font': as_dict.get('pdfFont', None),
            'print_max_width': as_dict.get('printMaxWidth', None),
            'scale': as_dict.get('scale', None),
            'show_table': as_dict.get('showTable', None),
            'source_height': as_dict.get('sourceHeight', None),
            'source_width': as_dict.get('sourceWidth', None),
            'table_caption': as_dict.get('tableCaption', None),
            'type': as_dict.get('type', None),
            'url': as_dict.get('url', None),
            'use_multi_level_headers': as_dict.get('useMultiLevelHeaders', None),
            'use_rowspan_headers': as_dict.get('useRowspanHeaders', None),
            'width': as_dict.get('width', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'allowHTML': self.allow_html,
            'buttons': self.buttons,
            'chartOptions': self.chart_options,
            'csv': self.csv,
            'enabled': self.enabled,
            'error': self.error,
            'fallbackToExportServer': self.fallback_to_export_server,
            'filename': self.filename,
            'formAttributes': self.form_attributes,
            'libURL': self.lib_url,
            'menuItemDefinitions': self.menu_item_definitions,
            'pdfFont': self.pdf_font,
            'printMaxWidth': self.print_max_width,
            'scale': self.scale,
            'showTable': self.show_table,
            'sourceHeight': self.source_height,
            'sourceWidth': self.source_width,
            'tableCaption': self.table_caption,
            'type': self.type,
            'url': self.url,
            'useMultiLevelHeaders': self.use_multi_level_headers,
            'useRowspanHeaders': self.use_rowspan_headers,
            'width': self.width
        }

        return untrimmed
