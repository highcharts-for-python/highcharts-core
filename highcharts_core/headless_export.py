try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import json
import os
from typing import Optional

import requests
from validator_collection import validators

from highcharts_core import errors, constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.options import HighchartsOptions
from highcharts_core.options.data import Data


class ExportServer(HighchartsMeta):
    """Class that provides methods for interacting with the Highcharts
    `Export Server <https://github.com/highcharts/node-export-server>`_.

    .. note::

      By default, the :class:`ExportServer` class operates using the Highcharts-provided
      export server. If you wish to use your own (or a custom) export server, you can
      configure the class using either the :meth:`url <ExportServer.url>`,
      :meth:`port <ExportServer.port>`, and
      :meth:`path <ExportServer.path>` properties explicitly or by setting
      the ``HIGHCHARTS_EXPORT_SERVER_DOMAIN`, ``HIGHCHARTS_EXPORT_SERVER_PORT``, or
      ``HIGHCHARTS_EXPORT_SERVER_PATH`` environment variables.

    """

    def __init__(self, **kwargs):
        self._url = None
        self._port = None
        self._path = None
        self._options = None
        self._format_ = None
        self._scale = None
        self._width = None
        self._callback = None
        self._constructor = None
        self._use_base64 = None
        self._no_download = None
        self._async_rendering = None
        self._global_options = None
        self._data_options = None
        self._custom_code = None

        self.protocol = kwargs.get('protocol',
                                   os.getenv('HIGHCHARTS_EXPORT_SERVER_PROTOCOL',
                                             'https'))
        self.domain = kwargs.get('domain', os.getenv('HIGHCHARTS_EXPORT_SERVER_DOMAIN',
                                                     'export.highcharts.com'))
        self.port = kwargs.get('port', os.getenv('HIGHCHARTS_EXPORT_SERVER_PORT',
                                                 ''))
        self.path = kwargs.get('path', os.getenv('HIGHCHARTS_EXPORT_SERVER_PATH',
                                                 ''))
        self.options = kwargs.get('options', None)
        self.format_ = kwargs.get('format_', kwargs.get('type', 'png'))
        self.scale = kwargs.get('scale', 1)
        self.width = kwargs.get('width', None)
        self.callback = kwargs.get('callback', None)
        self.constructor = kwargs.get('constructor', 'Chart')
        self.use_base64 = kwargs.get('use_base64', False)
        self.no_download = kwargs.get('no_download', False)
        self.async_rendering = kwargs.get('async_rendering', False)
        self.global_options = kwargs.get('global_options', None)
        self.data_options = kwargs.get('data_options', None)
        self.custom_code = kwargs.get('custom_code', None)

        super().__init__(**kwargs)

    @property
    def protocol(self) -> Optional[str]:
        """The protocol over which the Highcharts for Python library should communicate
        with the :term:`Export Server`. Accepts either ``'https'`` or ``'http'``. Defaults
        to the ``HIGHCHARTS_EXPORT_SERVER_PROTOCOL`` environment variable if present,
        otherwise falls back to default of ``'https'``.

        .. tip::

          This property is set automatically by the ``HIGHCHARTS_EXPORT_SERVER_PROTOCOL``
          environment variable, if present.

        .. warning::

          If set to :obj:`None <python:None>`, will fall back to the
          ``HIGHCHARTS_EXPORT_SERVER_PROTOCOL`` value if available, and the Highsoft-
          provided server (``'export.highcharts.com'``) if not.

        :rtype: :class:`str <python:str>`
        """
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            value = os.getenv('HIGHCHARTS_EXPORT_SERVER_PROTOCOL', 'https')

        value = value.lower()
        if value not in ['https', 'http']:
            raise errors.HighchartsUnsupportedProtocolError(f'protocol expects either '
                                                            f'"https" or "http". '
                                                            f'Received: "{value}"')

        self._protocol = value
        self._url = None

    @property
    def domain(self) -> Optional[str]:
        """The domain where the :term:`Export Server` can be found. Defaults to the
        Highsoft-provided Export Server at ``'export.highcharts.com'``, unless over-ridden
        by the ``HIGHCHARTS_EXPORT_SERVER_DOMAIN`` environment variable.

        .. tip::

          This property is set automatically by the ``HIGHCHARTS_EXPORT_SERVER_DOMAIN``
          environment variable, if present.

        .. warning::

          If set to :obj:`None <python:None>`, will fall back to the
          ``HIGHCHARTS_EXPORT_SERVER_DOMAIN`` value if available, and the Highsoft-
          provided server (``'export.highcharts.com'``) if not.

        :rtype: :class:`str <pythoon:str>`
        """
        return self._domain

    @domain.setter
    def domain(self, value):
        value = validators.domain(value, allow_empty = True)
        if not value:
            value = os.getenv('HIGHCHARTS_EXPORT_SERVER_DOMAIN',
                              'export.highcharts.com')
        self._domain = value
        self._url = None

    @property
    def port(self) -> Optional[int]:
        """The port on which the :term:`Export Server` can be found. Defaults to
        :obj:`None <python:None>` (for the Highsoft-provided export server), unless
        over-ridden by the ``HIGHCHARTS_EXPORT_SERVER_PORT`` environment variable.

        .. tip::

          This property is set automatically by the ``HIGHCHARTS_EXPORT_SERVER_PORT``
          environment variable, if present.

        .. warning::

          If set to :obj:`None <python:None>`, will fall back to the
          ``HIGHCHARTS_EXPORT_SERVER_PORT`` value if available. If unavailable, will
          revert to :obj:`None <python:None>`.

        :rtype: :class:`str <pythoon:str>`
        """
        return self._port

    @port.setter
    def port(self, value):
        if value or value == 0:
            value = validators.integer(value,
                                       allow_empty = True,
                                       minimum = 0,
                                       maximum = 65536)
        else:
            value = os.getenv('HIGHCHARTS_EXPORT_SERVER_PORT', None)

        self._port = value
        self._url = None

    @property
    def path(self) -> Optional[str]:
        """The path (at the :meth:`ExportServer.url`) where the :term:`Export Server` can
        be reached. Defaults to :obj:`None <python:None>` (for the Highsoft-provided
        export server), unless over-ridden by the ``HIGHCHARTS_EXPORT_SERVER_PATH``
        environment variable.

        .. tip::

          This property is set automatically by the ``HIGHCHARTS_EXPORT_SERVER_PATH``
          environment variable, if present.

        .. warning::

          If set to :obj:`None <python:None>`, will fall back to the
          ``HIGHCHARTS_EXPORT_SERVER_PATH`` value if available. If unavailable, will
          revert to :obj:`None <python:None>`.

        :rtype: :class:`str <pythoon:str>`
        """
        return self._path

    @path.setter
    def path(self, value):
        value = validators.path(value, allow_empty = True)
        if value is None:
            value = os.getenv('HIGHCHARTS_EXPORT_SERVER_PATH', None)

        self._path = value
        self._url = None

    @property
    def url(self) -> Optional[str]:
        """The fully-formed URL for the :term:`Export Server`, consisting of a
        :meth:`protocol <ExportServer.protocol>`, a :meth:`domain <ExportServer.domain>`,
        and optional :meth:`port <ExportServer.port>` and
        :meth:`path <ExportServer.path>`.

        .. note::

          If explicitly set, will override the values in related properties:

            * :meth:`protocol <ExportServer.protocol>`,
            * :meth:`domain <ExportServer.domain>`,
            * :meth:`port <ExportServer.port>`, and
            * :meth:`path <ExportServer.path>`

        :rtype: :class:`str <python:str>`
        """
        if self._url:
            return self._url
        else:
            return_value = f'{self.protocol}://{self.domain}'
            if self.port is not None:
                return_value += f':{self.port}/'
            if self.path is not None:
                return_value += self.path

            return return_value

    @url.setter
    def url(self, value):
        value = validators.url(value, allow_empty = True)
        if not value:
            self.protocol = None
            self.domain = None
            self.port = None
            self.path = None
        else:
            original_value = value
            self.protocol = value[:value.index(':')]

            protocol = self.protocol + '://'
            value = value.replace(protocol, '')

            no_port = False
            try:
                end_of_domain = value.index(':')
                self.domain = value[:end_of_domain]
            except ValueError:
                no_port = True
                try:
                    end_of_domain = value.index('/')
                    self.domain = value[:end_of_domain]
                except ValueError:
                    self.domain = value

            domain = self.domain + '/'
            if domain in value:
                value = value.replace(domain, '')
            elif self.domain in value:
                value = value.replace(self.domain, '')

            if value and no_port:
                if value.startswith('/'):
                    self.path = value[1:]
                else:
                    self.path = value
            else:
                if value.startswith(':'):
                    start_of_port = 1
                else:
                    start_of_port = 0
                try:
                    end_of_port = value.index('/')
                except ValueError:
                    end_of_port = None

                if end_of_port:
                    self.port = value[start_of_port:end_of_port]
                else:
                    self.port = value[start_of_port:]

                port = f':{self.port}'
                value = value.replace(port, '')
                if value.startswith('/'):
                    self.path = value[1:]
                elif value:
                    self.path = value
                else:
                    self.path = None

            self._url = original_value

    @property
    def options(self) -> Optional[HighchartsOptions]:
        """The :class:`HighchartsOptions` which should be applied to render the exported
        chart. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`HighchartsOptions` or :obj:`None <pythoN:None>`
        """
        return self._options

    @options.setter
    @class_sensitive(HighchartsOptions)
    def options(self, value):
        self._options = value

    @property
    def format_(self) -> Optional[str]:
        """The format in which the exported chart should be returned. Defaults to
        ``'png'``.

        Accepts:

          * ``'png'``
          * ``'jpeg'``
          * ``'pdf'``
          * ``'svg'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format_

    @format_.setter
    def format_(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._format_ = None
        else:
            value = value.lower()
            if value not in ['png', 'jpeg', 'pdf', 'svg']:
                raise errors.HighchartsUnsupportedExportTypeError(
                    f'format_ expects either '
                    f'"png", "jpeg", "pdf", or '
                    f'"svg". Received: {value}'
                )
            self._format_ = value

    @property
    def scale(self) -> Optional[int | float]:
        """The scale factor by which the exported chart image should be scaled. Defaults
        to ``1``.

        .. tip::

          Use this setting to improve resolution when exporting PNG or JPEG images. For
          example, setting ``.scale = 2`` on a chart whose width is 600px will produce
          an image with a width of 1200px.

        .. warning::

          If :meth:`width <ExportServer.width>` is explicitly set, this setting will be
          overridden.

        :rtype: numeric
        """
        return self._scale

    @scale.setter
    def scale(self, value):
        value = validators.numeric(value,
                                   allow_empty = True,
                                   minimum = 0)
        if not value:
            value = 1

        self._scale = value

    @property
    def width(self) -> Optional[int | float]:
        """The width that the exported chart should have. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          If explicitly set, this setting will override
          :meth:`scale <ExportServer.scale>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        value = validators.numeric(value,
                                   allow_empty = True,
                                   minimum = 0)
        if not value:
            value = None

        self._width = value

    @property
    def callback(self) -> Optional[CallbackFunction]:
        """A JavaScript function to execute in the (JavaScript) Highcharts constructor.

        .. note::

          This setting is equivalent to providing the :meth:`Chart.callback` setting.

        :rtype: :class:`CallbackFunction` or :obj:`None <pythoN:None>`
        """
        return self._callback

    @callback.setter
    @class_sensitive(CallbackFunction)
    def callback(self, value):
        self._callback = value

    @property
    def constructor(self) -> Optional[str]:
        """The (JavaScript) constructor to use when generating the exported chart.
        Defaults to :obj:`None <python:None>`.

        Accepts:

          * ``'Chart'``
          * ``'Stock'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._constructor

    @constructor.setter
    def constructor(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._constructor = None
        else:
            if value not in ['Chart', 'Stock']:
                raise errors.HighchartsUnsupportedConstructorError(f'constructor expects '
                                                                   f'either "Chart" or '
                                                                   f'"Stock", but '
                                                                   f'received: "{value}"')

            self._constructor = value

    @property
    def use_base64(self) -> bool:
        """If ``True``, returns the exported chart in base64 encoding. If ``False``,
        returns the exported chart in binary. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._use_base64

    @use_base64.setter
    def use_base64(self, value):
        self._use_base64 = bool(value)

    @property
    def no_download(self) -> bool:
        """If ``True``, will not send attachment headers in the HTTP response when
        exporting a chart. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._no_download

    @no_download.setter
    def no_download(self, value):
        self._no_download = bool(value)

    @property
    def async_rendering(self) -> bool:
        """If ``True``, will delay the (server-side) rendering of the exported chart
        until all scripts, functions, and event handlers provided have been executed
        and the (JavaScript) method ``highexp.done()`` is called. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._async_rendering

    @async_rendering.setter
    def async_rendering(self, value):
        self._async_rendering = bool(value)

    @property
    def global_options(self) -> Optional[HighchartsOptions]:
        """The global options which will be passed to the (JavaScript)
        ``Highcharts.setOptions()`` method, and which will be applied to the exported
        chart. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`HighchartsOptions`
        """
        return self._global_options

    @global_options.setter
    @class_sensitive(HighchartsOptions)
    def global_options(self, value):
        self._global_options = value

    @property
    def data_options(self) -> Optional[Data]:
        """Configuration of data options to add data to the chart from sources like CSV.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`Data` or :obj:`None <python:None>`
        """
        return self._data_options

    @data_options.setter
    @class_sensitive(Data)
    def data_options(self, value):
        self._data_options = value

    @property
    def custom_code(self) -> Optional[CallbackFunction]:
        """When :meth:`data_options <ExportServer.data_options>` is not
        :obj:`None <python:None>`, this (JavaScript) callback function is executed after
        the data options are applied. The only argument it receives is the complete
        set of :class:`HighchartsOptions` (as a JS literal object), which will be passed
        to the Highcharts constructor on return. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._custom_code

    @custom_code.setter
    @class_sensitive(CallbackFunction)
    def custom_code(self, value):
        self._custom_code = value

    @classmethod
    def is_export_supported(cls, options) -> bool:
        """Evaluates whether the Highcharts Export Server supports exporting the series types in ``options``.
        
        :rtype: :class:`bool <python:bool>`
        """
        if not isinstance(options, HighchartsOptions):
            return False

        if not options.series:
            return True

        series_types = [x.type for x in options.series]
        for item in series_types:
            if item in constants.EXPORT_SERVER_UNSUPPORTED_SERIES_TYPES:
                return False
            
        return True

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        url = as_dict.get('url', None)
        protocol = None
        domain = None
        port = None
        path = None
        if not url:
            protocol = as_dict.get('protocol', None)
            domain = as_dict.get('domain', None)
            port = as_dict.get('port', None)
            path = as_dict.get('path', None)

        kwargs = {
            'options': as_dict.get('options', None),
            'format_': as_dict.get('type', as_dict.get('format_', 'png')),
            'scale': as_dict.get('scale', 1),
            'width': as_dict.get('width', None),
            'callback': as_dict.get('callback', None),
            'constructor': as_dict.get('constructor',
                                       None) or as_dict.get('constr', None),
            'use_base64': as_dict.get('use_base64', None) or as_dict.get('b64', False),
            'no_download': as_dict.get('noDownload',
                                       None) or as_dict.get('no_download', None),
            'async_rendering': as_dict.get('asyncRendering',
                                           False) or as_dict.get('async_rendering',
                                                                 False),
            'global_options': as_dict.get('global_options',
                                          None) or as_dict.get('globalOptions',
                                                               None),
            'data_options': as_dict.get('data_options',
                                        None) or as_dict.get('dataOptions', None),
            'custom_code': as_dict.get('custom_code',
                                       None) or as_dict.get('customCode', None)
        }
        if url:
            kwargs['url'] = url
        if protocol:
            kwargs['protocol'] = protocol
        if domain:
            kwargs['domain'] = domain
        if port:
            kwargs['port'] = port
        if path:
            kwargs['path'] = path

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'url': self.url,
            'options': self.options,
            'type': self.format_,
            'scale': self.scale,
            'width': self.width,
            'callback': self.callback,
            'constr': self.constructor,
            'b64': self.use_base64,
            'noDownload': self.no_download,
            'asyncRendering': self.async_rendering,
            'globalOptions': self.global_options,
            'dataOptions': self.data_options,
            'customCode': self.custom_code
        }

        return untrimmed

    def request_chart(self,
                      filename = None,
                      auth_user = None,
                      auth_password = None,
                      timeout = 3,
                      **kwargs):
        """Execute a request against the export server based on the configuration in the
        instance.

        :param filename: The name of the file where the exported chart should (optionally)
          be persisted. Defaults to :obj:`None <python:None>`.
        :type filename: Path-like or :obj:`None <python:None>`

        :param auth_user: The username to use to authenticate against the
          Export Server, using :term:`basic authentication`. Defaults to
          :obj:`None <python:None>`.
        :type auth_user: :class:`str <python:str>` or :obj:`None <python:None>`

        :param auth_password: The password to use to authenticate against the Export
          Server (using :term:`basic authentication`). Defaults to
          :obj:`None <python:None>`.
        :type auth_password: :class:`str <python:str>` or :obj:`None <python:None>`

        :param timeout: The number of seconds to wait before issuing a timeout error.
          The timeout check is passed if bytes have been received on the socket in less
          than the ``timeout`` value. Defaults to ``3``.
        :type timeout: numeric or :obj:`None <python:None>`

        .. note::

          All other keyword arguments are as per the :class:`ExportServer` constructor
          :meth:`ExportServer.__init__() <highcharts_core.headless_export.ExportServer.__init__>`

        :returns: The exported chart image, either as a :class:`bytes <python:bytes>`
          binary object or as a base-64 encoded string (depending on the
          :meth:`use_base64 <ExportServer.use_base64>` property).
        :rtype: :class:`bytes <python:bytes>` or :class:`str <python:str>`
        """
        self.options = kwargs.get('options', self.options)
        self.format_ = kwargs.get('format_', kwargs.get('type', self.format_))
        self.scale = kwargs.get('scale', self.scale)
        self.width = kwargs.get('width', self.width)
        self.callback = kwargs.get('callback', self.callback)
        self.constructor = kwargs.get('constructor', self.constructor)
        self.use_base64 = kwargs.get('use_base64', self.use_base64)
        self.no_download = kwargs.get('no_download', self.no_download)
        self.async_rendering = kwargs.get('async_rendering', self.async_rendering)
        self.global_options = kwargs.get('global_options', self.global_options)
        self.data_options = kwargs.get('data_options', self.data_options)
        self.custom_code = kwargs.get('custom_code', self.custom_code)

        missing_details = []
        if not self.options:
            missing_details.append('options')
        if not self.format_:
            missing_details.append('format_')
        if not self.constructor:
            missing_details.append('constructor')
        if not self.url:
            missing_details.append('url')

        if missing_details:
            raise errors.HighchartsMissingExportSettingsError(
                f'Unable to export a chart.'
                f'ExportServer was missing '
                f' following settings: '
                f'{missing_details}'
            )

        basic_auth = None
        if auth_user and auth_password:
            basic_auth = requests.HTTPBasicAuth(auth_user, auth_password)

        payload = {
            'infile': 'HIGHCHARTS FOR PYTHON: REPLACE WITH OPTIONS',
            'type': self.format_,
            'scale': self.scale,
            'constr': self.constructor,
            'b64': self.use_base64,
            'noDownload': self.no_download,
            'asyncRendering': self.async_rendering
        }
        if self.width:
            payload['width'] = self.width
        if self.callback:
            payload['callback'] = 'HIGHCHARTS FOR PYTHON: REPLACE WITH CALLBACK'
        if self.global_options:
            payload['globalOptions'] = 'HIGHCHARTS FOR PYTHON: REPLACE WITH GLOBAL'
        if self.data_options:
            payload['dataOptions'] = 'HIGHCHARTS FOR PYTHON: REPLACE WITH DATA'
        if self.custom_code:
            payload['customCode'] = 'HIGHCHARTS FOR PYTHON: REPLACE WITH CUSTOM'

        as_json = json.dumps(payload)
        
        if not self.is_export_supported(self.options):
            raise errors.HighchartsUnsupportedExportError('The Highcharts Export Server currently only supports '
                                                          'exports from Highcharts (Javascript) v.10. You are '
                                                          'using a series type introduced in v.11. Sorry, but '
                                                          'that functionality is still forthcoming.')
        
        options_as_json = self.options.to_json()
        if isinstance(options_as_json, bytes):
            options_as_str = str(options_as_json, encoding = 'utf-8')
        else:
            options_as_str = options_as_json

        as_json = as_json.replace('"HIGHCHARTS FOR PYTHON: REPLACE WITH OPTIONS"',
                                  options_as_str)
        if self.callback:
            callback_as_json = self.callback.to_json()
            if isinstance(callback_as_json, bytes):
                callback_as_str = str(callback_as_json, encoding = 'utf-8')
            else:
                callback_as_str = callback_as_json
            as_json = as_json.replace('"HIGHCHARTS FOR PYTHON: REPLACE WITH CALLBACK"',
                                      callback_as_str)
        if self.global_options:
            global_as_json = self.global_options.to_json()
            if isinstance(global_as_json, bytes):
                global_as_str = str(global_as_json, encoding = 'utf-8')
            else:
                global_as_str = global_as_json
            as_json = as_json.replace('"HIGHCHARTS FOR PYTHON: REPLACE WITH GLOBAL"',
                                      global_as_str)
        if self.data_options:
            data_as_json = self.data_options.to_json()
            if isinstance(data_as_json, bytes):
                data_as_str = str(data_as_json, encoding = 'utf-8')
            else:
                data_as_str = data_as_json
            as_json = as_json.replace('"HIGHCHARTS FOR PYTHON: REPLACE WITH DATA"',
                                      data_as_str)
        if self.custom_code:
            code_as_json = self.custom_code.to_json()
            if isinstance(code_as_json, bytes):
                code_as_str = str(code_as_json, encoding = 'utf-8')
            else:
                code_as_str = code_as_json
            as_json = as_json.replace('"HIGHCHARTS FOR PYTHON: REPLACE WITH CUSTOM"',
                                      code_as_str)

        result = requests.post(self.url,
                               data = as_json,
                               headers = { 'Content-Type': 'application/json' },
                               auth = basic_auth,
                               timeout = timeout)

        result.raise_for_status()

        if filename and self.format_ != 'svg':
            with open(filename, 'wb') as file_:
                file_.write(result.content)
        elif filename and self.format_ == 'svg':
            content = str(result.content, encoding = 'utf-8')
            with open(filename, 'wt') as file_:
                file_.write(content)

        return result.content

    @classmethod
    def get_chart(cls,
                  filename = None,
                  auth_user = None,
                  auth_password = None,
                  timeout = 3,
                  **kwargs):
        """Produce an exported chart image.

        :param filename: The name of the file where the exported chart should (optionally)
          be persisted. Defaults to :obj:`None <python:None>`.
        :type filename: Path-like or :obj:`None <python:None>`

        :param auth_user: The username to use to authenticate against the
          Export Server, using :term:`basic authentication`. Defaults to
          :obj:`None <python:None>`.
        :type auth_user: :class:`str <python:str>` or :obj:`None <python:None>`

        :param auth_password: The password to use to authenticate against the Export
          Server (using :term:`basic authentication`). Defaults to
          :obj:`None <python:None>`.
        :type auth_password: :class:`str <python:str>` or :obj:`None <python:None>`

        :param timeout: The number of seconds to wait before issuing a timeout error.
          The timeout check is passed if bytes have been received on the socket in less
          than the ``timeout`` value. Defaults to ``3``.
        :type timeout: numeric or :obj:`None <python:None>`

        .. note::

          All other keyword arguments are as per the :class:`ExportServer` constructor
          :meth:`ExportServer.__init__() <highcharts_core.headless_export.ExportServer.__init__>`

        :returns: The exported chart image, either as a :class:`bytes <python:bytes>`
          binary object or as a base-64 encoded string (depending on the ``use_base64``
          keyword argument).
        :rtype: :class:`bytes <python:bytes>` or :class:`str <python:str>`
        """
        instance = cls(**kwargs)

        exported_chart = instance.request_chart(filename = filename,
                                                auth_user = auth_user,
                                                auth_password = auth_password,
                                                timeout = timeout)

        return exported_chart
