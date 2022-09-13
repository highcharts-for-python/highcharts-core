
  .. method:: from_js_literal(cls, as_string_or_file, allow_snake_case = True)
    :classmethod:
    :noindex:

    Convert a JavaScript object defined using :term:`JavaScript object literal notation`
    into a **Highcharts for Python** Python object, typically descended from
    :class:`HighchartsMeta`.

    :param cls: The class object itself.
    :type cls: :class:`type <python:type>`

    :param as_string_or_file: The JavaScript object you wish to convert. Expects either a
      :class:`str <python:str>` containing the JavaScript object, or a path to a file which
      consists of the object.
    :type as_string_or_file: :class:`str <python:str>`

    :param allow_snake_case: If ``True``, allows keys in ``as_string_or_file`` to apply the
      ``snake_case`` convention. If ``False``, will ignore keys that apply the
      ``snake_case`` convention and only process keys that use the ``camelCase`` convention.
      Defaults to ``True``.
    :type allow_snake_case: :class:`bool <python:bool>`

    :returns: A **Highcharts for Python** object corresponding to the JavaScript
      object supplied in ``as_string_or_file``.
    :rtype: Descendent of :class:`HighchartsMeta`


  .. method:: from_json(cls, as_json_or_file, allow_snake_case = True)
    :classmethod:
    :noindex:

    Convert a Highcharts JS object represented as JSON (in either :class:`str <python:str>`
    or :class:`bytes <python:bytes>` form, or as a file name) into a
    **Highcharts for Python** object, typically descended from :class:`HighchartsMeta`.

    :param cls: The class object itself.
    :type cls: :class:`type <python:type>`

    :param as_json_or_file: The JSON object you wish to convert, or a filename that contains
      the JSON object that you wish to convert.
    :type as_json_or_file: :class:`str <python:str>` or :class:`bytes <python:bytes>`

    :param allow_snake_case: If ``True``, allows keys in ``as_json`` to apply the
      ``snake_case`` convention. If ``False``, will ignore keys that apply the
      ``snake_case`` convention and only process keys that use the ``camelCase`` convention.
      Defaults to ``True``.
    :type allow_snake_case: :class:`bool <python:bool>`

    :returns: A **Highcharts for Python** Python object corresponding to the JSON
      object supplied in ``as_json``.
    :rtype: Descendent of :class:`HighchartsMeta`


  .. method:: from_dict(cls, as_dict, allow_snake_case = True)
    :classmethod:
    :noindex:

    Convert a :class:`dict <python:dict>` representation of a Highcharts JS object into a
    Python object representation, typically descended from :class:`HighchartsMeta`.

    :param cls: The class object itself.
    :type cls: :class:`type <python:type>`

    :param as_dict: The :class:`dict <python:dict>` representation of the object.
    :type as_dict: :class:`dict <python:dict>`

    :param allow_snake_case: If ``True``, allows keys in ``as_dict`` to apply the
      ``snake_case`` convention. If ``False``, will ignore keys that apply the
      ``snake_case`` convention and only process keys that use the ``camelCase`` convention.
      Defaults to ``True``.
    :type allow_snake_case: :class:`bool <python:bool>`
