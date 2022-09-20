
  .. method:: to_js_literal(self, filename = None, encoding = 'utf-8')
    :noindex:

    Convert the **Highcharts for Python** instance to Highcharts JS-compatible JavaScript
    code using :term:`JavaScript object literal notation`.

    :param filename: If supplied, persists the JavaScript code to the file indicated.
      Defaults to :obj:`None <python:None>`.
    :type filename: Path-like or :obj:`None <python:None>`

    :param encoding: Indicates the character encoding to use when producing the JavaScript
      literal string. Defaults to ``'utf-8'``.
    :type encoding: :class:`str <python:str>`

    :returns: Highcharts JS-compatible JavaScript code using
      :term:`JavaScript object literal notation`.
    :rtype: :class:`str <python:str>`


  .. method:: to_json(self, filename = None, encoding = 'utf-8')
    :noindex:

    Convert the **Highcharts for Python** instance to Highcharts JS-compatible JSON.

    .. warning::

      While similar, JSON is inherently different from
      :term:`JavaScript object literal notation`. In particular, it cannot include
      JavaScript functions. This means if you try to convert a Highcharts for Python object
      to JSON, any properties that are :class:`CallbackFunction` instances will not be
      included. If you want to convert those functions, please use ``.to_js_literal()``
      instead.

    :param filename: If supplied, persists the JSON is persisted to the file indicated.
      Defaults to :obj:`None <python:None>`.
    :type filename: Path-like or :obj:`None <python:None>`

    :param encoding: Indicates the character encoding to use when producing the JSON.
      Defaults to ``'utf-8'``.
    :type encoding: :class:`str <python:str>`

    :returns: Highcharts JS-compatible JSON representation of the object.
    :rtype: :class:`str <python:str>` or :class:`bytes <python:bytes>`

      .. note::

        **Highcharts for Python** works with different JSON encoders. If your environment
        has `orjson <https://github.com/ijl/orjson>`_, for example, the result will be
        returned as a :class:`bytes <python:bytes>` instance. Otherwise, the library will
        fallback to various other JSON encoders until finally falling back to the Python
        standard library's JSON encoder/decoder.


  .. method:: to_dict(self)
    :noindex:

    Convert the **Highcharts for Python** object into a Highcharts JS-compatible
    :class:`dict <python:dict>` object.

    :returns: Highcharts JS-compatible :class:`dict <python:dict>` object
    :rtype: :class:`dict <python:dict>`
