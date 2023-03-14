If you are hoping to configure a simple set of options, one of the fastest ways to do
so in your Python code is to instantiate your
:class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`
instance from a simple :class:`dict <python:dict>`:

  .. code-block:: python

    as_dict = {
        'chart': {
            'backgroundColor': '#fff',
            'borderWidth': 2,
            'plotBackgroundColor': 'rgba(255, 255, 255, 0.9)',
            'plotBorderWidth': 1
        }
    }

    my_shared_options = SharedOptions.from_dict(as_dict)

    js_code_snippet = my_shared_options.to_js_literal()

  .. tip::

    This method is particularly helpful and easy to maintain if you are only using a
    *very* small subset of the `Highcharts JS <https://www.highcharts.com>`__
    configuration options.
