.. tip::

  **Best practice!**

  We really like to use JS literals written as separate files in our codebase. It
  makes it super simple to instantiate a
  :class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`
  instance with one method call.

Let's say you organize your files like so:

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
    | ------------ **shared_options.js**
    | ------------ bar-template-01.js
    | ------------ bar-template-02.js
    | ------------ line-template.js
    | ------------ packed-bubble-template.js
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

You'll notice that the organization has a ``project_resources`` folder. This is where
you would put the various files that your application wlil reference, like your static
images, or the files that contain data you might be using in your application. It also
contains a **highcharts_config** folder, which contains several files with a ``.js``
extension. Of particular note is the file in bold, ``shared_options.js``. This file
should contain a
:term:`JavaScript object literal <JavaScript object literal notation>`
version of the configuration settings you want to apply to *all* of your
visualizations. This file might look something like this:

  .. literalinclude:: /_static/shared_options.js
    :language: javascript

Now with this file, you can easily create a
:class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`
instance by executing:

  .. code-block:: python

    from highcharts_core.highcharts import SharedOptions

    my_shared_options = SharedOptions.from_js_literal('../../project_resources/highcharts_config/shared_options.js')

And that's it! Now you have a
:class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`
instance that can be used to apply your configuration standards to all of your charts.
You can do that by delivering its JavaScript output to your front-end by calling:

  .. code-block:: python

    js_code_snippet = my_shared_options.to_js_literal()

which will produce a string as follows:

  .. literalinclude:: /_static/shared_options_output.js
    :language: javascript

And now you can deliver ``js_code_snippet`` to your HTML template or wherever it will
be rendered.
