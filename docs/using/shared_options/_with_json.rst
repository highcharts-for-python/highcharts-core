You can use the same exact pattern as using a JS literal with a JSON file instead.
We don't really think there's an advantage to this - but there might be one
significant disadvantage: JSON files cannot be used to provide JavaScript functions
to your Highcharts configuration. This means that formatters, event handlers, etc.
will not be applied through your shared options if you use a JSON file.

If your shared options don't require JavaScript functions? Then by all means, feel
free to use a JSON file and the ``.from_json()`` method instead.

With a file structure like:

  .. line-block::

    my_repository/
    | --- docs/
    | --- my_project/
    | ------ project_resources/
    | --------- image_files/
    | --------- data_files/
    | ------------ data-file-01.csv
    | ------------ data-file-02.csv
    | ------------ data-file-03.csv
    | --------- **highcharts_config/**
    | ------------ **shared_options.json**
    | ------------ bar-template.json
    | ------------ line-template.json
    | ------------ packed-bubble-template.json
    | ------ some_package/
    | --------- __init__.py
    | --------- package_module.py
    | --------- another_module.py
    | ------ __init__.py
    | ------ __version__.py
    | ------ some_module.py
    | --- tests/
    | --- .gitignore
    | --- requirements.txt

You can leverage shared options that read from
``my_project/project_resources/highcharts_config/shared_options.json`` by executing:

  .. code-block:: python

    from highcharts_core.highcharts import SharedOptions

    my_shared_options = SharedOptions.from_js_literal(
        '../../project_resources/highcharts_config/shared_options.json'
    )

    json_code_snippet = my_shared_options.to_js_literal()
