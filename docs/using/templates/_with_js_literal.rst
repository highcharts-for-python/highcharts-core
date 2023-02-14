.. tip::

  **Best practice!**

  We really like to use JS literals written as separate files in our codebase. It
  makes it super simple to instantiate a **Highcharts for Python** instance with
  one method call.

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
    | ------------ shared_options.js
    | ------------ **bar-template-01.js**
    | ------------ **bar-template-02.js**
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

As you can see, there are two JS literal files named ``bar-template-01.js`` and
``bar-template-02.js`` respectively. These template files can be used to significantly
accelerate the configuration of our bar charts. Each template corresponds to one
sub-type of bar chart that we know we will need. These sub-types may have different
event functions, or more frequently use different formatting functions to make the
data look the way we want it to look.

Now with these template files, we can easily create a pair of
:class:`Chart <highcharts_core.chart.Chart>` instances by executing:

  .. code-block:: python

    from highcharts_core.highcharts import Chart
    from highcharts_core.options.series.bar import BarSeries

    type_1_chart = Chart.from_js_literal(
        '../../project_resources/highcharts_config/bar-template-01.js'
    )
    type_2_chart = Chart.from_js_literal(
        '../../project_resources/highcharts_config/bar-template-02.js'
    )

And that's it! Now you have two chart instances which you can further modify. For
example, you can add data to them by calling:

  .. code-block:: python

    type_1_chart.container = 'chart1_div'
    type_2_chart.container = 'chart2_div'

    type_1_chart.add_series(BarSeries.from_csv('../../project_resources/data_files/data-file-01.csv'))
    type_2_chart.add_series(BarSeries.from_csv('../../project_resources/data_files/data-file-02.csv'))

And then you can create the relevant JavaScript code to render the chart using:

  .. code-block:: python

    type_1_chart_js = type_1_chart.to_js_literal()
    type_2_chart_js = type_2_chart.to_js_literal()

And now you can deliver ``type_1_chart_js`` and ``type_2_chart_js`` to your HTML
template or wherever it will be rendered.
