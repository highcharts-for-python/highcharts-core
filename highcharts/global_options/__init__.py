from typing import Optional

from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.options import HighchartsOptions
from highcharts.global_options.language import Language


class SharedOptions(HighchartsMeta):
    """Python object which can be used to configure global settings that can apply to
    multiple Highcharts charts when serialized to JavaScript."""

    def __init__(self, **kwargs):
        self._global_options = None
        self._language = None

        self.global_options = kwargs.get('global_options', None)
        self.language = kwargs.get('language', None)

    @property
    def global_options(self) -> Optional[HighchartsOptions]:
        """The options which should be configured as the default for all Highcharts
        visualizations rendered on the page. Defaults to :obj:`None <python:None>`.

        .. note::

          These options are applied using the (JavaScript) ``Highcharts.setOptions()``
          method.

        .. warning::

          Because the Highcharts JS API documentation is somewhat unclear, the standard
          :class:`HighchartsOptions` objects do not support the
          :meth:`language <SharedOptions.langugae>` property. If you wish to configure
          a global language setting, you should assign it directly to the
          :meth:`language <SharedOptions.language>` property.

        :rtype: :class:`HighchartsOptions` or :obj:`None <python:None>
        """
        return self._global_options

    @global_options.setter
    @class_sensitive(HighchartsOptions)
    def global_options(self, value):
        self._global_options = value

    @property
    def language(self) -> Optional[Language]:
        """The language strings which should be applied to all Highcharts visualizations
        rendered on the page. Defaults to :obj:`None <python:None>`, which apply the
        Highcharts default English-language options.

        .. note::

          These options are applied using the (JavaScript) ``Highcharts.setOptions()``
          method.

        :rtype: :class:`Language` or :obj:`None <python:None>`
        """
        return self._language

    @language.setter
    @class_sensitive(Language)
    def language(self, value):
        self._language = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'global_options': as_dict.get(
                'global_options',
                None) or as_dict.get(
                    'options',
                    None) or as_dict.get(
                        'globalOptions',
                        None),
            'language': as_dict.get('language', None) or as_dict.get('lang', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'global_options': self.global_options,
            'language': self.language
        }

        return untrimmed

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        .. note::

          Returns a JavaScript string which applies the Highcharts global options. The
          JavaScript returned by this method takes the (pseudo-code) form:

          .. code-block:: javascript

            Highcharts.setOptions({... configuration options ... });

        :rtype: :class:`str <python:str>`
        """
        prefix = 'Highcharts.setOptions('
        options_as_str = ''
        if self.global_options:
            options_as_str = self.global_options.to_js_literal(encoding = encoding)
            if self.language:
                options_as_str = options_as_str[:-1] + ',\n'
        if self.language:
            language_as_str = self.language.to_js_literal(encoding = encoding)
            language_as_str = """lang: """ + language_as_str
            options_as_str += language_as_str

        as_str = prefix + options_as_str + '\n});'

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str
