import os
from typing import Optional, List
from collections import UserDict

from validator_collection import validators, checkers

from highcharts_core import constants, errors, utility_functions
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options import HighchartsOptions
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.js_literal_functions import serialize_to_js_literal
from highcharts_core.headless_export import ExportServer
from highcharts_core.options.series.series_generator import create_series_obj, SERIES_CLASSES
from highcharts_core.global_options.shared_options import SharedOptions


class Chart(HighchartsMeta):
    """Python representation of a Highcharts ``Chart`` object."""

    def __init__(self, **kwargs):
        """Creates a :class:`Chart <highcharts_core.chart.Chart>` instance.
        
        When creating a :class:`Chart <highcharts_core.chart.Chart>` instance, you can
        provide any of the object's properties as keyword arguments.
        **Positional arguments are not supported**.
        
        In addition to the standard properties, there are three special keyword 
        arguments which streamline the creation of 
        :class:`Chart <highcharts_core.chart.Chart>` instances:
        
          * ``series`` which accepts an iterable of 
            :class:`SeriesBase <highcharts_core.options.series.SeriesBase>` descendents.
            These are automatically then populated as series within the chart.
            
            .. note::
            
              Each member of ``series`` must be coercable into a Highcharts Core for Python
              series. And it must contain a ``type`` property.
              
          * ``data`` which accepts an iterable of objects that are coercable to Highcharts
            data point objects, which are then automatically used to create/populate a 
            series on your chart instance
          * ``series_type`` which accepts a string indicating the type of series to render
            for your data.
            
        .. warning::
        
          If you supply ``series``, the ``data`` and ``series_type`` keywords will be 
          *ignored*.
          
          If you supply ``data``, then ``series_type`` must *also* be supplied. Failure 
          to do so will raise a 
          :exc:`HighchartsValueError <highcharts_core.errors.HighchartsValueError>`.

          If you are also supplying an 
          :meth:`options <highcharts_core.chart.Chart.options>` keyword argument, then 
          any series derived from ``series``, ``data``, and ``series_type`` will be 
          *added* to any series defined in that ``options`` value.

        :raises: :exc:`HighchartsValueError <highcharts_core.errors.HighchartsValueError>`
          if supplying ``data`` with no ``series_type``.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        """
        self._callback = None
        self._container = None
        self._options = None
        self._variable_name = None
        self._module_url = None

        self._random_slug = {}

        self.callback = kwargs.get('callback', None)
        self.container = kwargs.get('container', None)
        self.options = kwargs.get('options', None)
        self.variable_name = kwargs.get('variable_name', None)
        self.module_url = kwargs.get('module_url',
                                     None) or os.environ.get('HIGHCHARTS_MODULE_URL',
                                                             'https://code.highcharts.com/')

        series = kwargs.get('series', None)
        series_type = kwargs.get('series_type', None)
        data = kwargs.get('data', None)

        if series_type and not data:
            data = []

        if series is not None:
            if not checkers.is_iterable(series, forbid_literals = (str, bytes, dict, UserDict)):
                series = [series]
            self.add_series(*series)
        elif data is not None and series_type:
            series_as_dict = {
                'data': data,
                'type': series_type
            }
            self.add_series(series_as_dict)
        elif data is not None:
            raise errors.HighchartsValueError('If ``data`` is provided, then '
                                              '``series_type`` must also be provided. '
                                              '``series_type`` was empty.')

    def __str__(self):
        """Return a human-readable :class:`str <python:str>` representation of the chart.

        .. warning::
        
          To ensure that the result is human-readable, the chart's ``options`` property will 
          be rendered *without* its ``plot_options`` and ``series`` sub-properties. 
        
          .. tip::
        
            If you would like a *complete* and *unambiguous* :class:`str <python:str>` 
            representation, then you can:
            
            * use the :meth:`__repr__() <highcharts_core.chart.Chart.__repr__>` method,
            * call ``repr(my_chart)``, or
            * serialize the chart to JSON using ``my_chart.to_json()``.
            
        :returns: A :class:`str <python:str>` representation of the chart.
        :rtype: :class:`str <python:str>`
        """
        as_dict = self.to_dict()

        kwargs = {utility_functions.to_snake_case(key): as_dict[key]
                  for key in as_dict if key not in ['options', 'userOptions']}

        if 'options' in as_dict:
            kwargs['options'] = str(as_dict['options'])
        elif 'userOptions' in as_dict:
            kwargs['options'] = str(as_dict['userOptions'])

        kwargs_as_str = ''
        for index, key in enumerate(kwargs):
            if index > 0:
                kwargs_as_str += ', '
            if key == 'options':
                kwargs_as_str += f'options = {kwargs[key]}'
            else:
                kwargs_as_str += f'{key} = {repr(kwargs[key])}'
            
        return f'{self.__class__.__name__}({kwargs_as_str})'

    def _jupyter_include_scripts(self, **kwargs):
        """Return the JavaScript code that is used to load the Highcharts JS libraries.

        :rtype: :class:`str <python:str>`
        """
        required_modules = [f'{self.module_url}{x}' 
                            for x in self.get_required_modules(include_extension = True)]
        js_str = ''
        for item in required_modules:
            js_str += utility_functions.jupyter_add_script(item)
            js_str += """.then(() => {"""
        
        for item in required_modules:
            js_str += """});"""

        return js_str

    def _jupyter_javascript(self,
                            global_options = None,
                            container = None,
                            random_slug = None,
                            retries = 5,
                            interval = 1000):
        """Return the JavaScript code which Jupyter Labs will need to render the chart.

        :param global_options: The :term:`shared options` to use when rendering the chart.
          Defaults to :obj:`None <python:None>`
        :type global_options: :class:`SharedOptions <highcharts_stock.global_options.shared_options.SharedOptions>`
          or :obj:`None <python:None>`

        :param container: The ID to apply to the HTML container when rendered in Jupyter Labs. Defaults to
          :obj:`None <python:None>`, which applies the :meth:`.container <highcharts_core.chart.Chart.container>`
          property if set, and ``'highcharts_target_div'`` if not set.
        :type container: :class:`str <python:str>` or :obj:`None <python:None>`

        :param random_slug: The random sequence of characters to append to the container name to ensure uniqueness.
          Defaults to :obj:`None <python:None>`
        :type random_slug: :class:`str <python:str>` or :obj:`None <python:None>`

        :param retries: The number of times to retry rendering the chart. Used to avoid race conditions with the
          Highcharts script. Defaults to 3.
        :type retries: :class:`int <python:int>`

        :param interval: The number of milliseconds to wait between retrying rendering the chart. Defaults to 1000 (1
          second).
        :type interval: :class:`int <python:int>`

        :rtype: :class:`str <python:str>`
        """
        original_container = self.container
        new_container = container or self.container or 'highcharts_target_div'
        if not random_slug:
            self.container = new_container
        else:
            self.container = f'{new_container}_{random_slug}'

        if global_options is not None:
            global_options = validate_types(global_options,
                                            types = SharedOptions)

        js_str = utility_functions.get_retryHighcharts()

        if global_options:
            js_str += '\n' + utility_functions.prep_js_for_jupyter(global_options.to_js_literal()) + '\n'

        js_str += utility_functions.prep_js_for_jupyter(self.to_js_literal(),
                                                        container = self.container,
                                                        random_slug = random_slug,
                                                        retries = retries,
                                                        interval = interval)

        self.container = original_container

        return js_str

    def _jupyter_container_html(self,
                                container = None,
                                random_slug = None):
        """Returns the Jupyter Labs HTML container for rendering the chart in Jupyter Labs context.

        :param container: The ID to apply to the HTML container when rendered in Jupyter Labs. Defaults to
          :obj:`None <python:None>`, which applies the :meth:`.container <highcharts_core.chart.Chart.container>`
          property if set, and ``'highcharts_target_div'`` if not set.
        :type container: :class:`str <python:str>` or :obj:`None <python:None>`

        :param random_slug: The random sequence of characters to append to the container/function name to ensure
          uniqueness. Defaults to :obj:`None <python:None>`
        :type random_slug: :class:`str <python:str>` or :obj:`None <python:None>`

        :rtype: :class:`str <python:str>`
        """
        if self.options.chart:
            height = self.options.chart.height or 400
        else:
            height = 400

        container = container or self.container or 'highcharts_target_div'
        if random_slug:
            container = f'{container}_{random_slug}'

        container_str = f"""<div id=\"{container}\" style=\"width:100%; height:{height};\"></div>\n"""

        return container_str

    def _repr_html_(self):
        """Produce the HTML representation of the chart.

        .. note::

          Currently includes *all* `Highcharts JS <https://www.highcharts.com/>`_ modules
          in the HTML. This issue will be addressed when roadmap issue :issue:`2` is
          released.

        :returns: The HTML representation of the chart.
        :rtype: :class:`str <python:str>`
        """
        return self.display()

    def get_script_tags(self, as_str = False) -> List[str] | str:
        """Return the collection of ``<script/>`` tags needed to load the modules
        for the chart to render.
        
        :param as_str: if ``True``, will return the result as a 
          :class:`str <python:str>` instance, rather than a :class:`list <python:list>`
          of :class:`str <python:str>`. Defaults to ``False``.
        :type as_str: :class:`bool <python:bool>`

        :rtype: :class:`list <python:list>` of :class:`str <python:str>` or 
          :class:`str <python:str>`
        """
        scripts = [f'<script src="{self.module_url}{x}"></script>' 
                   for x in self.get_required_modules(include_extension = True)]

        if as_str:
            return '\n'.join(scripts)
            
        return scripts

    def get_required_modules(self, 
                             include_extension = False) -> List[str]:
        """Return the list of URLs from which the Highcharts JavaScript modules
        needed to render the chart can be retrieved.
        
        :param include_extension: if ``True``, will return script names with the 
          ``'.js'`` extension included. Defaults to ``False``.
        :type include_extension: :class:`bool <python:bool>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        initial_scripts = ['highcharts']
        scripts = self._process_required_modules(initial_scripts, include_extension)

        return scripts

    def _get_jupyter_script_loader(self, chart_js_str) -> str:
        """Return the JavaScript code that loads ``required_modules`` in a Jupyter 
        context.
        
        :param chart_js_str: The JavaScript code that renders the chart.
        :type chart_js_str: :class:`str <python:str>`
        
        :returns: The JavaScript code that loads the required modules.
        :rtype: :class:`str <python:str>`
        """
        if_no_requirejs = ''

        if_requirejs = """require.config({\n"""
        if_requirejs += """  packages: [{\n"""
        if_requirejs += """    name: 'highcharts', main: 'highcharts' }],\n"""
        if_requirejs += """  paths: {\n"""
        if_requirejs += f"""    'highcharts': '{self.module_url}'\n"""
        if_requirejs += """  }\n\n});"""
        
        if_requirejs += """ require(["""
        requirejs_modules = []
        for item in self.get_required_modules():
            if item == 'highcharts' and item not in requirejs_modules:
                requirejs_modules.append(item)
            else:
                revised_item = f'highcharts/{item}'
                if revised_item not in requirejs_modules:
                    requirejs_modules.append(revised_item)
                
        for index, item in enumerate(requirejs_modules):
            is_last = index == len(requirejs_modules) - 1
            if_requirejs += f"""'{item}'"""
            if not is_last:
                if_requirejs += ', '
        if_requirejs += """], function (Highcharts) {\n"""
        if_requirejs += chart_js_str
        if_requirejs += """\n});"""

        required_modules = [f'{self.module_url}{x}' 
                            for x in self.get_required_modules(include_extension = True)]
        for item in required_modules:
            if_no_requirejs += utility_functions.jupyter_add_script(item)
            if_no_requirejs += """.then(() => {"""

        for item in required_modules:
            if_no_requirejs += """});"""
            
        js_str = utility_functions.wrap_for_requirejs(if_requirejs, if_no_requirejs)
            
        return js_str

    @property
    def callback(self) -> Optional[CallbackFunction]:
        """A (JavaScript) function that is run when the chart has loaded and all external
        images have been loaded. Defaults to :obj:`None <python:None>`.

        .. note::

          Setting this proprety is equivalent to setting a value for
          :meth:`ChartOptions.events.load <highcharts.utility_classes.events.ChartEvents.load>`

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._callback

    @callback.setter
    @class_sensitive(CallbackFunction)
    def callback(self, value):
        self._callback = value

    @property
    def module_url(self) -> str:
        """The URL from which Highcharts modules should be downloaded when 
        generating the ``<script/>`` tags. Will default to the
        ``HIGHCHARTS_MODULE_URL`` environment variable if available, and 
        otherwise defaults to ``'https://code.highcharts.com/'``.
        
        .. tip::
        
          If you need to lock the version of Highharts used to render your
          charts, we recommend supplying one of the Highcharts CDN version
          paths, e.g.:
          
            * ``'https://code.highcharts.com/11.0.1/'``
            * ``'https://code.highcharts.com/11.0.0/'``
            * etc.
        
        .. warning::
        
          Module paths wlil be appended to this value without checking that
          they resolve to an actual file, e.g. the module 
          ``module/accessibility.js`` will get appended as 
          ``'https://code.highcharts.com/module/accessibility.js'``. Be sure
          to modify this default value carefully.
          
          As a general rule of thumb, we *strongly* recommend that your URL 
          always end in a slash (``'/'``), unless your custom URL is loading
          modules dynamically (e.g. requires a ``'?module='`` or similar).
          
        :returns: The url from which Highcharts modules should be loaded.
        :rtype: :class:`str <python:str>`
        
        """
        return self._module_url
    
    @module_url.setter
    def module_url(self, value):
        try:
            value = validators.url(value, allow_empty = True)
        except (ValueError, TypeError):
            value = validators.path(value, allow_empty = True)
            
        self._module_url = value

    @property
    def options(self) -> Optional[HighchartsOptions]:
        """The Python representation of the `Highcharts <https://highcharts.com>`_
        ``options`` `configuration object <https://api.highcharts.com/highcharts/>`_
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`HighchartsOptions` or :obj:`None <python:None>`
        """
        return self._options

    @options.setter
    def options(self, value):
        if not value:
            self._options = None
        elif isinstance(value, SharedOptions):
            raise errors.HighchartsValueError('Chart.options expects a HighchartsOptions instance '
                                              'or a valid descendent. However, the value you supplied '
                                              'is a SharedOptions instance, which wil a descendent is not '
                                              'valid for this parameter.')
        else:
            value = validate_types(value,
                                   types = HighchartsOptions)

        self._options = value

    @property
    def container(self) -> Optional[str]:
        """The ``id`` of the ``<div>`` element in which your Highcharts chart should be
        rendered. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if self._container:
            return self._container

        if self.options and self.options.chart and self.options.chart.render_to:
            return self.options.chart.render_to

        return None

    @container.setter
    def container(self, value):
        self._container = validators.string(value, allow_empty = True)

    @property
    def variable_name(self) -> Optional[str]:
        """The name given to the (JavaScript) variable to which the (JavaScript) Chart
        instance wil be assigned. Defaults to :obj:`None <python:None>`.

        .. note::

          When the :class:`Chart` object is converted to JavaScript code, the
          (JavaScript) chart instance is assigned to a variable in your JavaScript code.
          In the example code below, the Chart instance is assigned to a ``variable_name``
          of ``chart1``:

          .. code-block:: javascript

            var chart1 = Highcharts.Chart('myTargetDiv', {});

        .. warning::

          If :obj:`None <python:None>`, when converted to a JavaScript literal, the
          :class:`Chart` instance will simply not be assigned to a variable.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, value):
        self._variable_name = validators.variable_name(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'callback': as_dict.get('callback', None),
            'container': as_dict.get('container', None) or as_dict.get('renderTo', None),
            'options': as_dict.get('options', None) or as_dict.get('userOptions', None),
            'variable_name': as_dict.get('variable_name',
                                         None) or as_dict.get('variableName', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'callback': self.callback,
            'container': self.container,
            'userOptions': self.options
        }

        return untrimmed

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8',
                      careful_validation = False) -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :param careful_validation: if ``True``, will carefully validate JavaScript values
          along the way using the
          `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
          to ``False``.
        
          .. warning::
        
            Setting this value to ``True`` will significantly degrade serialization
            performance, though it may prove useful for debugging purposes.

        :type careful_validation: :class:`bool <python:bool>`

        .. note::

          If :meth:`variable_name <Chart.variable_name>` is set, will render a string as
          a new JavaScript instance invocation in the (pseudo-code) form:

          .. code-block:: javascript

            new VARIABLE_NAME = new Chart(...);

          If :meth:`variable_name <Chart.variable_name>` is not set, will simply return
          the ``new Chart(...)`` portion in the string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            serialized = serialize_to_js_literal(item, 
                                                 encoding = encoding,
                                                 careful_validation = careful_validation)
            if serialized is not None:
                as_dict[key] = serialized

        signature_elements = 2

        if self.container:
            container_as_str = f"""'{self.container}'"""
        else:
            container_as_str = """null"""

        if self.options:
            options_as_str = "{}".format(
                self.options.to_js_literal(encoding = encoding,
                                           careful_validation = careful_validation)
            )
        else:
            options_as_str = """null"""

        callback_as_str = ''
        if self.callback:
            callback_as_str = "{}".format(
                self.callback.to_js_literal(encoding = encoding,
                                            careful_validation = careful_validation)
            )
            signature_elements += 1

        signature = """Highcharts.chart("""
        signature += container_as_str
        if signature_elements > 1:
            signature += ',\n'
        signature += options_as_str
        if signature_elements > 1:
            signature += ',\n'
        if callback_as_str:
            signature += callback_as_str
        signature += ');'

        constructor_prefix = ''
        if self.variable_name:
            constructor_prefix = f'var {self.variable_name} = '

        as_str = constructor_prefix + signature

        prefix = """document.addEventListener('DOMContentLoaded', function() {\n"""
        suffix = """});"""
        as_str = prefix + as_str + '\n' + suffix

        if validators.path(filename, allow_empty = True):
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    def download_chart(self,
                       format = 'png',
                       scale = 1,
                       width = None,
                       filename = None,
                       auth_user = None,
                       auth_password = None,
                       timeout = 3,
                       server_instance = None,
                       **kwargs):
        """Export a downloaded form of the chart using a Highcharts :term:`Export Server`.

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

        :param server_instance: Provide an already-configured :class:`ExportServer`
          instance to use to programmatically produce the exported chart. Defaults to
          :obj:`None <python:None>`, which causes Highcharts for Python to instantiate
          a new :class:`ExportServer` instance.
        :type server_instance: :class:`ExportServer` or :obj:`None <python:None>`

        .. note::

          All other keyword arguments are as per the :class:`ExportServer` constructor.

        :returns: The exported chart image, either as a :class:`bytes <python:bytes>`
          binary object or as a base-64 encoded string (depending on the ``use_base64``
          keyword argument).
        :rtype: :class:`bytes <python:bytes>` or :class:`str <python:str>`
        """
        if checkers.is_type(self.options, 'HighchartsStockOptions'):
            constructor = 'Stock'
        else:
            constructor = 'Chart'

        if not server_instance:
            return ExportServer.get_chart(filename = filename,
                                          auth_user = auth_user,
                                          auth_password = auth_password,
                                          timeout = timeout,
                                          options = self.options,
                                          constructor = constructor,
                                          scale = scale,
                                          width = width,
                                          format_ = format,
                                          **kwargs)

        if not isinstance(server_instance, ExportServer):
            raise errors.HighchartsValueError(f'server_instance is expected to be an '
                                              f'ExportServer instance. Was: '
                                              f'{server_instance.__class__.__name__}')

        return server_instance.request_chart(filename = filename,
                                             auth_user = auth_user,
                                             auth_password = auth_password,
                                             timeout = timeout,
                                             options = self.options,
                                             constructor = constructor,
                                             format_ = format,
                                             **kwargs)

    @classmethod
    def _copy_dict_key(cls,
                       key,
                       original,
                       other,
                       overwrite = True,
                       **kwargs):
        """Copies the value of ``key`` from ``original`` to ``other``.

        :param key: The key that is to be copied.
        :type key: :class:`str <python:str>`

        :param original: The original :class:`dict <python:dict>` from which it should
          be copied.
        :type original: :class:`dict <python:dict>`

        :param other: The :class:`dict <python:dict>` to which it should be copied.
        :type other: :class:`dict <python:dict>`

        :returns: The value that should be placed in ``other`` for ``key``.
        """
        preserve_data = kwargs.get('preserve_data', True)

        original_value = original[key]
        if other is None:
            other = {}

        other_value = other.get(key, None)

        if key == 'data' and preserve_data:
            return other_value

        if key == 'points' and preserve_data:
            return other_value

        if key == 'series' and preserve_data:
            if not other_value:
                return [x for x in original_value]

            if len(other_value) != len(original_value):
                matched_series = []
                new_series = []
                for original_item in original_value:
                    matched = False
                    for other_item in other_value:
                        if checkers.are_dicts_equivalent(original_item, other_item):
                            matched_series.append((original_item, other_item))
                            matched = True
                            break
                    if not matched:
                        new_series.append(original_item)
                updated_series = []
                for items in matched_series:
                    original_item = items[0]
                    other_item = items[1]
                    new_item = {}
                    for subkey in original_item:
                        new_item_value = cls._copy_dict_key(subkey,
                                                            original_item,
                                                            new_item,
                                                            overwrite = overwrite,
                                                            **kwargs)
                        new_item[subkey] = new_item_value
                    updated_series.append(new_item)
                updated_series.extend(new_series)

                return updated_series

        elif isinstance(original_value, (dict, UserDict)):
            new_value = {subkey: cls._copy_dict_key(subkey,
                                                   original_value,
                                                   other_value,
                                                   overwrite = overwrite,
                                                   **kwargs)
                         for subkey in original_value}

            return new_value

        elif checkers.is_iterable(original_value,
                                  forbid_literals = (str,
                                                     bytes,
                                                     dict,
                                                     UserDict)):
            if overwrite:
                new_value = [x for x in original_value]

                return new_value

            return other_value

        elif other_value and not overwrite:
            return other_value

        return original_value

    def copy(self,
             other = None,
             overwrite = True,
             **kwargs):
        """Copy the configuration settings from this chart to the ``other`` chart.

        :param other: The target chart to which the properties of this chart should
          be copied. If :obj:`None <python:None>`, will create a new chart and populate
          it with properties copied from ``self``. Defaults to :obj:`None <python:None>`.
        :type other: :class:`Chart`

        :param overwrite: if ``True``, properties in ``other`` that are already set will
          be overwritten by their counterparts in ``self``. Defaults to ``True``.
        :type overwrite: :class:`bool <python:bool>`

        :param preserve_data: If ``True``, will preserve the data values in any
          :term:`series` contained in ``other`` and the configuration of the
          :meth:`options.data <Options.data>` property, but will still copy other
          properties as applicable. If ``False``, will overwrite data in ``other``
          with data from ``self``. Defaults to ``True``.
        :type preserve_data: :class:`bool <python:bool>`

        :param kwargs: Additional keyword arguments. Some special descendents of
          :class:`HighchartsMeta` may have special implementations of this method which
          rely on additional keyword arguments.

        :returns: A mutated version of ``other`` with new property values

        """
        return super().copy(other = other,
                            overwrite = overwrite,
                            **kwargs)

    def add_series(self, *series):
        """Adds ``series`` to the
        :meth:`Chart.options.series <highcharts_core.options.HighchartsOptions.series>`
        property.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          or coercable

        """
        new_series = [create_series_obj(item)
                      for item in series]

        if self.options and self.options.series:
            existing_series = [x for x in self.options.series]
        elif self.options:
            existing_series = []
        else:
            existing_series = []
            self.options = HighchartsOptions()

        updated_series = existing_series + new_series

        self.options.series = updated_series

    def update_series(self, *series, add_if_unmatched = False):
        """Replace existing series with the new versions supplied in ``series``,
        matching them based on their
        :meth:`.id <highcharts_core.options.series.base.SeriesBase.id>` property.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          or coercable

        :param add_if_unmatched: If ``True``, will add a series that does not have a
          match. If ``False``, will raise a
          :exc:`HighchartsMissingSeriesError <highcharts_core.errors.HighchartsMissingSeriesError>`
          if a series does not have a match on the chart. Defaults to ``False``.
        :type add_if_unmatched: :class:`bool <python:bool>`
        """
        new_series = [create_series_obj(item)
                      for item in series]

        if self.options and self.options.series:
            existing_series = [x for x in self.options.series]
        elif self.options:
            existing_series = []
        else:
            existing_series = []
            self.options = HighchartsOptions()

        existing_ids = [x.id for x in existing_series]
        new_ids = [x.id for x in new_series]
        overlap_ids = [x for x in new_ids if x in existing_ids]

        updated_series = [existing
                          for existing in existing_series
                          if existing.id not in overlap_ids]

        for new in new_series:
            if new.id not in overlap_ids and not add_if_unmatched:
                raise errors.HighchartsMissingSeriesError(f'attempted to update series '
                                                          f'id "{new.id}", but that '
                                                          f'series is not present in '
                                                          f'the chart')

            updated_series.append(new)

        self.options.series = updated_series

    @classmethod
    def from_series(cls, *series, kwargs = None):
        """Creates a new :class:`Chart <highcharts_core.chart.Chart>` instance populated
        with ``series``.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          or coercable

        :param kwargs: Other properties to use as keyword arguments for the instance to be
          created.

          .. warning::

            If ``kwargs`` sets the
            :meth:`options.series <highcharts_core.options.HighchartsOptions.series>`
            property, that setting will be *overridden* by the contents of ``series``.

        :type kwargs: :class:`dict <python:dict>`

        :returns: A new :class:`Chart <highcharts_core.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        """
        kwargs = validators.dict(kwargs, allow_empty = True) or {}
        instance = cls(**kwargs)

        if checkers.is_iterable(series) is True:
            for item in series:
                instance.add_series(item)
        else:
            instance.add_series(series)

        return instance

    def display(self,
                global_options = None,
                container = None,
                retries = 5,
                interval = 1000):
        """Display the chart in `Jupyter Labs <https://jupyter.org/>`_ or
        `Jupyter Notebooks <https://jupyter.org/>`_.

        :param global_options: The :term:`shared options` to use when rendering the chart.
          Defaults to :obj:`None <python:None>`
        :type global_options: :class:`SharedOptions <highcharts_stock.global_options.shared_options.SharedOptions>`
          or :obj:`None <python:None>`

        :param container: The ID to apply to the HTML container when rendered in Jupyter Labs. Defaults to
          :obj:`None <python:None>`, which applies the :meth:`.container <highcharts_core.chart.Chart.container>`
          property if set, and ``'highcharts_target_div'`` if not set.

          .. note::

            Highcharts for Python will append a 6-character random string to the value of ``container``
            to ensure uniqueness of the chart's container when rendering in a Jupyter Notebook/Labs context. The
            :class:`Chart <highcharts_core.chart.Chart>` instance will retain the mapping between container and the
            random string so long as the instance exists, thus allowing you to easily update the rendered chart by
            calling the :meth:`.display() <highcharts_core.chart.Chart.display>` method again.

            If you wish to create a new chart from the instance that does not update the existing chart, then you can do
            so by specifying a new ``container`` value.

        :type container: :class:`str <python:str>` or :obj:`None <python:None>`

        :param retries: The number of times to retry rendering the chart. Used to avoid race conditions with the 
          Highcharts script. Defaults to 5.
        :type retries: :class:`int <python:int>`

        :param interval: The number of milliseconds to wait between retrying rendering the chart. Defaults to 1000 (1
          second).
        :type interval: :class:`int <python:int>`

        :raises HighchartsDependencyError: if
          `ipython <https://ipython.readthedocs.io/en/stable/>`_ is not available in the
          runtime environment
        """
        try:
            from IPython import display as display_mod
            from IPython.core.display_functions import display
        except ImportError:
            raise errors.HighchartsDependencyError('Unable to import IPython modules. '
                                                   'Make sure that it is available in '
                                                   'your runtime environment. To install,'
                                                   'use: pip install ipython')

        container = container or self.container or 'highcharts_target_div'
        if not self._random_slug:
            self._random_slug = {}

        random_slug = self._random_slug.get(container, None)

        if not random_slug:
            random_slug = utility_functions.get_random_string()
            self._random_slug[container] = random_slug

        html_str = self._jupyter_container_html(container, random_slug)
        html_display = display_mod.HTML(data = html_str)

        chart_js_str = self._jupyter_javascript(global_options = global_options,
                                                container = container,
                                                random_slug = random_slug,
                                                retries = retries,
                                                interval = interval)
        wrapped_chart_js_str = utility_functions.wrap_for_requirejs('', chart_js_str)
        javascript_display = display_mod.Javascript(data = wrapped_chart_js_str)

        include_js_str = self._get_jupyter_script_loader(chart_js_str)
        include_display = display_mod.Javascript(data = include_js_str)

        display(html_display)
        display(include_display)
        display(javascript_display)

    @classmethod
    def from_array(cls,
                   value,
                   series_type = 'line',
                   series_kwargs = None,
                   options_kwargs = None,
                   chart_kwargs = None):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance with
        one series populated from the array contained in ``value``.
        
        .. seealso::

          The specific structure of the expected array is highly dependent on the type of data
          point that the series needs, which itself is dependent on the series type itself.

          Please review the detailed :ref:`series documentation <series_documentation>` for
          series type-specific details of relevant array structures.

        :param value: The array to use to populate the series data.
        :type value: iterable
        
        :param series_type: Indicates the series type that should be created from the array
          data. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`
        
        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`
        
        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``value``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_array(value, series_kwargs = series_kwargs)

        options_kwargs['series'] = [series]
        options = HighchartsOptions(**options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_csv_in_rows(cls,
                         as_string_or_file,
                         series_type = 'line',
                         has_header_row = True,
                         series_kwargs = None,
                         options_kwargs = None,
                         chart_kwargs = None,
                         delimiter = ',',
                         null_text = 'None',
                         wrapper_character = "'",
                         line_terminator = '\r\n',
                         wrap_all_strings = False,
                         double_wrapper_character_when_nested = False,
                         escape_character = "\\",
                         series_index = None,
                         **kwargs):
        """Create a new :class:`Chart <highcharts_core.chart.Chart>` instance with
        data populated from a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_chart = Chart.from_csv('some-csv-file.csv',
                                          property_column_map = {
                                              'x': 0,
                                              'y': 3,
                                              'id': 'id'
                                          },
                                          series_type = 'line')

            As the example above shows, data is loaded into the ``my_chart`` instance
            from the CSV file with a filename ``some-csv-file.csv``. The
            :meth:`x <CartesianData.x>`
            values for each data point will be taken from the first (index 0) column in
            the CSV file. The :meth:`y <CartesianData.y>` values will be taken from the
            fourth (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>`
            values will be taken from a column whose header row is labeled ``'id'``
            (regardless of its index).

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param series_type: Indicates the series type that should be created from the CSV
          data. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from the CSV file instead.

        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and CSV file instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce
            any value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\\\`` (which is Python for ``'\\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param series_index: If supplied, generate the chart with the series that 
          Highcharts for Python generated from ``df`` at the ``series_index`` position. 
          Defaults to :obj:`None <python:None>`, which includes all series generated 
          from ``df`` on the chart.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the CSV data.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        return cls.from_csv(as_string_or_file,
                            property_column_map = None,
                            series_type = series_type,
                            has_header_row = has_header_row,
                            series_kwargs = series_kwargs,
                            options_kwargs = options_kwargs,
                            chart_kwargs = chart_kwargs,
                            delimiter = delimiter,
                            null_text = null_text,
                            wrapper_character = wrapper_character,
                            line_terminator = line_terminator,
                            wrap_all_strings = wrap_all_strings,
                            double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                            escape_character = escape_character,
                            series_in_rows = True,
                            series_index = series_index,
                            **kwargs)

    @classmethod
    def from_csv(cls,
                 as_string_or_file,
                 property_column_map = None,
                 series_type = 'line',
                 has_header_row = True,
                 series_kwargs = None,
                 options_kwargs = None,
                 chart_kwargs = None,
                 delimiter = ',',
                 null_text = 'None',
                 wrapper_character = "'",
                 line_terminator = '\r\n',
                 wrap_all_strings = False,
                 double_wrapper_character_when_nested = False,
                 escape_character = "\\",
                 series_in_rows = False,
                 series_index = None,
                 **kwargs):
        """Create a new :class:`Chart <highcharts_core.chart.Chart>` instance with
        data populated from a CSV string or file.

          .. note::

            For an example chart containing
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` 
            instances, the minimum code required would be:

              .. code-block:: python

                # EXAMPLE 1: The minimum code:
                my_chart = Chart.from_csv('some-csv-file.csv', series_type = 'line')
                
                # EXAMPLE 2: For more precise configuration and *one* series:
                my_chart = Chart.from_csv('some-csv-file.csv',
                                          property_column_map = {
                                              'x': 0,
                                              'y': 3,
                                              'id': 'id'
                                          },
                                          series_type = 'line')
                
                # EXAMPLE 3: For more precise configuration and *multiple* series:
                my_chart = Chart.from_csv('some-csv-file.csv',
                                          property_column_map = {
                                              'x': 0,
                                              'y': [3, 5, 8],
                                              'id': 'id'
                                          },
                                          series_type = 'line')
                                          

            As the example above shows, data is loaded into the ``my_chart`` instance
            from the CSV file with a filename ``some-csv-file.csv``. 
            
            In EXAMPLE 1, the chart will contain one or more series where each series 
            will default to having its :meth:`.x <CartesianData.x>` values taken from 
            the first (index 0) column in the CSV, and one 
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` 
            instance will be created for each subsequent column (which will populate 
            that series' :meth:`.y <CartesianData.y>` values.
            
            In EXAMPLE 2, the chart will contain one series, where the
            :meth:`x <CartesianData.x>`
            values for each data point will be taken from the first (index 0) column in
            the CSV file. The :meth:`y <CartesianData.y>` values will be taken from the
            fourth (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>`
            values will be taken from a column whose header row is labeled ``'id'``
            (regardless of its index).
            
            In EXAMPLE 3, the chart will contain three series, all of which will have
            :meth:`.x <CartesianData.x>` values taken from the first (index 0) column,
            :meth:`.id <CartesianData.id>` values from the column whose header row is 
            labeled ``'id'``, and whose :meth:`.y <CartesianData.y>` will be taken
            from the fourth (index 3) column for the first series, the sixth (index 5)
            column for the second series, and the ninth (index 8) column for the third
            series.

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param property_column_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which CSV column. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value can either be a numerical index (starting with 0) or a
          :class:`str <python:str>` indicating the label for the CSV column. Defaults to
          :obj:`None <python:None>`.
          
          .. note::
          
            If any of the values in ``property_column_map`` contain an iterable, then
            one series will be produced for each item in the iterable. For example,
            the following:
            
            .. code-block:: python
            
              {
                  'x': 0,
                  'y': [3, 5, 8]
              }
              
            will return *three* series, each of which will have its 
            :meth:`.x <CartesianData.x>` value populated from the first column 
            (index 0), and whose :meth:`.y <CartesianData.y>`
            values will be populated from the fourth, sixth, and ninth columns (indices 
            3, 5, and 8), respectively.

          .. warning::

            If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
            file *must* have a header row (this is expected, by default). If there is no
            header row and a :class:`str <python:str>` value is found, a
            :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>`

        :param series_type: Indicates the series type that should be created from the CSV
          data. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from the CSV file instead.

        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and CSV file instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce
            any value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\\\`` (which is Python for ``'\\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to ``False``.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: if :obj:`None <python:None>`, will attempt to populate
          the chart with multiple series from the CSV data. If an :class:`int <python:int>`
          is supplied, will populate the chart only with the series found at 
          ``series_index``.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the CSV data.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        if series_in_rows:
            series = series_cls.from_csv_in_rows(
                as_string_or_file,
                has_header_row = has_header_row,
                series_kwargs = series_kwargs,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = wrap_all_strings,
                double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                escape_character = escape_character,
                **kwargs
            )
        else:
            series = series_cls.from_csv(as_string_or_file,
                                         property_column_map = property_column_map,
                                         has_header_row = has_header_row,
                                         series_kwargs = series_kwargs,
                                         delimiter = delimiter,
                                         null_text = null_text,
                                         wrapper_character = wrapper_character,
                                         line_terminator = line_terminator,
                                         wrap_all_strings = wrap_all_strings,
                                         double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                                         escape_character = escape_character,
                                         **kwargs)

        if isinstance(series, list) and series_index is not None:
            series = series[series_index]

        if not isinstance(series, list):
            series = [series]

        options_kwargs['series'] = series

        options = HighchartsOptions(**options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pandas_in_rows(cls,
                            df,
                            series_type = 'line',
                            series_kwargs = None,
                            options_kwargs = None,
                            chart_kwargs = None,
                            series_index = None,
                            **kwargs):
        """Create a chart from a Pandas :class:`DataFrame <pandas:pandas.DataFrame>`, 
        treating each row in the dataframe as a :term:`series` instances.

        :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
          should be loaded.
        :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`
        
        :param series_type: Indicates the series type that should be created from the data
          in ``df``. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`
        
        :param series_index: If supplied, generate the chart with the series that 
          Highcharts for Python generated from ``df`` at the ``series_index`` position. 
          Defaults to :obj:`None <python:None>`, which includes all series generated 
          from ``df`` on the chart.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Additional keyword arguments that are - in turn - propagated to 
          the series created from the ``df``.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment

        """
        return cls.from_pandas(df,
                               property_map = None,
                               series_type = series_type,
                               series_kwargs = series_kwargs,
                               options_kwargs = options_kwargs,
                               chart_kwargs = chart_kwargs,
                               series_in_rows = True,
                               series_index = series_index,
                               **kwargs)

    @classmethod
    def from_pandas(cls,
                    df,
                    property_map = None,
                    series_type = 'line',
                    series_kwargs = None,
                    options_kwargs = None,
                    chart_kwargs = None,
                    series_in_rows = False,
                    series_index = None,
                    **kwargs):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance whose
        series are populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:pandas.DataFrame>`.

          .. code-block:: python

            from highcharts_core.chart import Chart
            from highcharts_core.options.series.area import LineSeries

            # Create a chart with one or more LineSeries instances from 
            # the CSV file "some-csv-file.csv".

            # EXAMPLE 1: The minimum code:

            my_chart = Chart.from_csv('some-csv-file.csv', series_type = 'line')
        
            # EXAMPLE 2: For more precise configuration and *one* series:

            my_chart = Chart.from_csv('some-csv-file.csv',
                                      property_column_map = {
                                          'x': 0,
                                          'y': 3,
                                          'id': 'id'
                                      },
                                      series_type = 'line')
        
            # EXAMPLE 3: For more precise configuration and *multiple* series:

            my_chart = Chart.from_csv('some-csv-file.csv',
                                      property_column_map = {
                                          'x': 0,
                                          'y': [3, 5, 8],
                                          'id': 'id'
                                      },
                                      series_type = 'line')

        :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:pandas.DataFrame>` column. Defaults to 
          :obj:`None <python:None>`.

            .. note::
          
              If any of the values in ``property_map`` contain an iterable, then
              one series will be produced for each item in the iterable. For example,
              the following:
            
                .. code-block:: python
            
                  {
                      'x': 'timestamp',
                      'y': ['value1', 'value2', 'value3']
                  }
              
              will return *three* series, each of which will have its 
              :meth:`.x <CartesianData.x>` value populated from the column
              labeled ``'timestamp'``, and whose :meth:`.y <CartesianData.y>`
              values will be populated from the columns labeled ``'value1'``,
              ``'value2'``, and ``'value3'``, respectively.

        :type property_map: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_type: Indicates the series type that should be created from the data
          in ``df``. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`
        
        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to 
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: If supplied, generate the chart with the series that 
          Highcharts for Python generated from ``df`` at the ``series_index`` position. 
          Defaults to :obj:`None <python:None>`, which includes all series generated 
          from ``df`` on the chart.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Additional keyword arguments that are - in turn - propagated to 
          the series created from the ``df``.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        if not series_type:
            raise errors.HighchartsValueError('series_type cannot be empty')
        series_type = str(series_type).lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        if not isinstance(options_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'options_kwarts expects a dict. '
                                              f'Received: {options_kwargs.__class__.__name__}')
        if not options_kwargs:
            options_kwargs = {}
            
        if not isinstance(chart_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'chart_kwargs expects a dict. '
                                              f'Received: {chart_kwargs.__class__.__name__}')
        if not chart_kwargs:
            chart_kwargs = {}
            
        if not isinstance(kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'kwargs expects a dict. '
                                              f'Received: {kwargs.__class__.__name__}')
        if not kwargs:
            kwargs = {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        if series_in_rows:
            series = series_cls.from_pandas_in_rows(df,
                                                    series_kwargs = series_kwargs,
                                                    series_index = series_index,
                                                    **kwargs)
        else:
            series = series_cls.from_pandas(df,
                                            property_map = property_map,
                                            series_kwargs = series_kwargs,
                                            series_index = series_index,
                                            **kwargs)

        if isinstance(series, series_cls):
            series = [series]

        options_kwargs['series'] = series
        options = HighchartsOptions(**options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pyspark(cls,
                     df,
                     property_map,
                     series_type,
                     series_kwargs = None,
                     options_kwargs = None,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance whose
        data is populated from a
        `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
        :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`.

        :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
          should be loaded.
        :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :param series_type: Indicates the series type that should be created from the data
          in ``df``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsPySparkDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if
          `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
          in the runtime environment
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_pyspark(df,
                                         property_map,
                                         series_kwargs)

        options = HighchartsOptions(**options_kwargs)
        options.series = [series]

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_options(cls,
                     options,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance from a
        :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` object.

        :param options: The configuration options to use to instantiate the chart.
        :type options:
          :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` or
          coercable

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the instance. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten* by the contents of ``options``.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: The :class:`Chart <highcharts_core.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}
        options = validate_types(options,
                                 types = (HighchartsOptions))

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

