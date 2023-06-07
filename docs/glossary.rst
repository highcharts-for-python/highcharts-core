####################
Glossary
####################

.. glossary::

  Basic Authentication
    A simple method of authentication provided by most HTTP servers where a username and
    password are supplied. In terms of technical implementation, the HTTP request to the
    server contains a header field with ``Authorization: Basic <credentials>`` where
    ``<credentials>`` is the base-64 encoding of ``username:password``.

  Callback Function
    A JavaScript function which is passed to
    `Highcharts JS <https://www.highcharts.com>`__ in the
    :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` configuration
    which performs an action which affects the :term:`chart <charts>`.

    Typically, callback functions are used to define
    :term:`event handlers <event handler>` or to define
    :term:`Highcharts formatters <formatter>`.

    .. seealso::

      * :term:`Event Handler`
      * :term:`Formatter`
      * :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`

  Cartesian Charts
    Cartesian charts are :term:`charts` that typically feature two or more axes, by common
    convention referred to as the X axis (classically represented as the horizontal axis)
    and the Y axis (classically represented as the vertical axis). If the chart features a
    third axis (for example in a three dimensional chart), it is commonly called the Z
    axis.

    The location of a :term:`data point` on a Cartesian chart is the intersection of its
    :term:`metric` on one axis (typically the Y axis) and its :term:`dimension` on the
    other axis (typically the X axis).

  Cartesian Series
    A Cartesian series is a :term:`series` that can be visualized on a
    :term:`Cartesian chart <Cartesian charts>`, which is typically characterized by
    several different properties including its :term:`metric` and one or more
    :term:`dimensions <dimension>`, and whose :term:`data points <data point>` get
    visualized on their intersection.

  Charts
    The visualization of numerical, hierarchical, or sequential data in a somewhat
    graphical representation.

  Color Axis
    A color axis is an axis on the visualization that represents a value using its color.
    Typically, :term:`data point` :term:`metric` values are communicated using their
    position. However, they can also be communicated using the color in which they are
    rendered. A :class:`Color Axis <highcharts_core.options.axes.color_axis.ColorAxis>`
    is used to define the relationship between colors and metric values.

    .. seealso::

      * :class:`Color Axis <highcharts_core.options.axes.color_axis.ColorAxis>`

  Data Point
    A single value that is represented on a :term:`chart <charts>`.

  Data Label
    The meta-data associated with a :term:`data point` that is displayed on the chart.
    It will typically include labels, the value, and possibly some additional extraneous
    meta-data and will typically be displayed in a tooltip alongside the
    :term:`data point` when user hovers their mouse over the data point.

    Represented in **Highcharts for Python** by
    :class:`highcharts_core.utility_classes.data_labels.DataLabel` and also affected
    heavily by :meth:`highcharts_stock.options.HighchartsOptions.tooltip`.

    .. seealso::

      * :class:`highcharts_stock.utility_classes.data_labels.DataLabel`
      * :meth:`highcharts_stock.options.HighchartsOptions.tooltip`
      * :class:`highcharts_stock.options.tooltips.Tooltip`

  Dependency Wheel
    A dependency wheel chart is a type of flow diagram, where all nodes are laid out
    in a circle, and the flow between the are drawn as link bands.

      .. figure:: _static/dependencywheel-example.png
        :alt: Dependency Wheel Example Chart
        :align: center

    .. seealso::

      * :class:`DependencyWheelOptions <highcharts_core.options.plot_options.dependencywheel.DependencyWheelOptions>`
      * :class:`DependencyWheelSeries <highcharts_core.options.series.dependencywheel.DependencyWheelSeries>`

  Diamond of Death
    A multiple inheritance pattern that is considered an anti-pattern by the Python
    community because it creates difficult-to-maintain-and-debug complexity. The pattern
    involves the creation of one ancestor class (we'll call this class ``Ancestor``),
    two child classes (we'll call them ``ChildA`` and ``ChildB``, respectively), and a
    third grand-child class that inherits from *both* ``ChildA`` and ``ChildB``.

    This pattern is considered an anti-pattern because - absent a deep understanding of
    Python's :iabbr`MRO (Method Resolution Order)` - it is perceived as introducing
    ambiguity as to which ancestors methods will be executed when hoisting from the
    grand-child class.

    **Highcharts for Python** - to minimize repetition of code and to keep the code base
    maintainable - does use this anti-pattern extensively, as discussed in greater detail
    in the :ref:`contributors guidance <multiple_inheritance>`.

    .. seealso::

      * :ref:`Multiple Inheritance, DRY, and the Diamond of Death <multiple_inheritance>`

  Dimension
    A way in which :term:`metrics <metric>` can be organized or grouped. Typically a
    dimension can be the time period in which a metric was measured, recorded, or reported
    (e.g. "months" or "days"), or a dimension can be a category that sub-groups your
    metrics into subjects that you want to analyze (e.g. think "store locations" or
    "states").

    .. tip::

      In a :term:`chart <charts>`, dimensions are often displayed along the x-axis.

  Drilldown
    The act of expanding a :term:`data point` into a more granular view, typically by
    changing the properties (or interval) of a :term:`dimension`.

    For example:

    * if viewing a data point that presents a monthly value, drilling down into
      that data point may instead show a daily breakdown of the same :term:`metric`
    * if viewing a data point that presents information at the level of a given
      state/province, drilling down into that data point may instead show a breakdown
      of the same :term:`metric` grouped by city (within that state/province).

    In **Highcharts for Python**, the drilldown capabilities are configured using the
    :meth:`HighchartsOptions.drilldown <highcharts_core.options.HighchartsOptions.drilldown>`
    setting.

    .. seealso::

      * :meth:`HighchartsOptions.drilldown <highcharts_core.options.HighchartsOptions.drilldown>`
      * :class:`Drilldown <highcharts_core.options.drilldown.Drilldown>`

  Event Handler
    A JavaScript function that receives information when an event of some sort has
    occurred and can take action in response to that event.

    In Highcharts, this is typically seen as a :term:`callback function`.

    .. seealso::

      * :term:`Callback Function`
      * :class:`highcharts_stock.utility_classes.javascript_functions.CallbackFunction`

  Export Server
    A server application which can receive requests to generate :term:`charts`, produces
    those charts headlessly (without a UI), and returns a static export of the charts to
    the process that requested them.

    The **Highcharts Export Server** is an application written and maintained by Highsoft,
    creators of Highcharts JS. It is available as a NodeJS application which can be
    deployed by organizations that license Highcharts.

    In addition to the deployable Node Export Server, Highsoft also provides a
    Highsoft-hosted version of the export server. This Highsoft-provided server imposes
    rate limiting and other limitations, but can be used by licensees of Highcharts JS to
    programmatically generate downloadable static versions of their charts.

    .. seealso::

      * `Highcharts Node Export Server Documentation <https://github.com/highcharts/node-export-server>`__

  Format String
    .. versionadded: v.1.2.0

    Format strings are templates for labels introduced in Highcharts for Python v.1.2. 
    Since Highcharts (JS) v.11.1, format strings support logic. 
    
    We recommend using format strings if you:

      * Need to save the chart configuration to JSON.
      * Need to provide a GUI for end users so that callbacks are not practical, or XSS is a concern.
      * Need to send the charts over to our export server to execute (all callbacks are stripped out).
      * Are creating a wrapper for another programming language than JavaScript.
    
    .. seealso::

      For a full overview over templating in format strings, please see the Highcharts (JS) 
      `Templating <https://www.highcharts.com/docs/chart-concepts/templating>`__ article.

  Formatter
    A particular type of :term:`callback function` used extensively in Highcharts. In
    general terms, a formatter receives a context (for example a data point) and returns
    a string that has mutated the data point to apply some formatting.

    For example, the data point might be a numerical value (``500``) to which the formatter
    function will append a suffix (`` miles``) for display in the chart's
    :term:`data label`.

    .. seealso::

      * :term:`Callback Function`
      * :class:`highcharts_stock.utility_classes.javascript_functions.CallbackFunction`

  Gantt Chart
    A type of :term:`chart <charts>` which indicates the start and end of processes along
    a dimension of time, and may also indicate numerical values associated with that work
    along the same dimension.

    Typically used in projcet management, Gantt Charts are useful for indicating
    dependencies and critical path for complex multi-faceted workstreams.

  Gauge Chart
    A type of :term:`chart <charts>` which visualizes data as a position on a radial
    gauge. A classic example is a "spedometer" in a car, which depicts speed using the
    radial angle around the center point of the gauge.

      .. figure:: _static/gauge-example.png
        :alt: Gauge Example Chart
        :align: center

    .. seealso::

      * :class:`GaugeOptions <highcharts_core.options.plot_options.gauge.GaugeOptions>`
      * :class:`SolidGaugeOptions <highcharts_core.options.plot_options.gauge.SolidGaugeOptions>`
      * :class:`GaugeSeries <highcharts_core.options.series.gauge.GaugeSeries>`
      * :class:`SolidGaugeSeries <highcharts_core.options.series.gauge.SolidGaugeSeries>`

  Highpass
    A highpass audio filter lets high frequencies through, but stops low frequencies, making the sound thinner.

  JavaScript Object Literal Notation
    A way of representing data in JavaScript as native JavaScript objects which is
    necessary to maximize value from `Highcharts JS <http://www.highcharts.com/>`__.

    It is easiest to compare JavaScript object literal notation to the closely-related
    JSON (JavaScript Object Notation), though they are very different and serve very
    different purposes.

    JavaScript Object Literal Notation *is* JavaScript source code. JSON is not. JSON is
    a way of encoding data into a text form that JavaScript is able to parse and
    deserialize. Because Highcharts JS relies heavily on JavaScriot object literal
    notation to support the definition of :term:`event handlers <event handler>` and
    :term:`callback functions <callback function>`, **Highcharts for Python** is designed
    to serialize and deserialize Python representations to/from their JavaScript object
    literal form.

    Below is a comparison of a (similar) object represented in both JavaScript object
    literal notation and JSON, with further commentary:

    .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - JavaScriot Object Literal Notation
        - JSON
      * - |
          .. code-block:: JavaScript

            {
              myProperty: 'this is a property',
              anotherProperty: 123,
              aBooleanProperty: true,
              myCallback: function() { return true }
            }

        - |
          .. code-block:: JavaScript

          {
            "myProperty": "this is a property",
            "anotherProperty": 123,
            "aBooleanProperty": true
          }


    As you can see, the two forms are very similar. However, the JavaScript object literal
    notation has its keys directly accessible as properties of the object, while the JSON
    version has them represented as strings. Furthermore, because JSON is inherently a
    way of encoding data into *strings*, it is not wise to use it to transport functions
    which will then be executed by some other code (doing so is a dangerous security
    hole).

    .. caution::

      Typically, JSON can be converted to JavaScript object literal notation easily...but
      the opposite does not hold true.

  Lowpass
    A lowpass audio filter lets low frequencies through, but stops high frequencies, making the sound more dull.

  Metaclass
    A Python class that is used to define properties and methods - including abstract
    properties or methods which are not implemented in the metaclass itself - which are
    then inherited by sub-classes that derive from the metaclass.

    Metaclasses are typically used as good :iabbr:`DRY (Don't Repeat Yourself)`
    programming and to ensure a consistent interface (standard methods) across multiple
    classes in your code.

    In the **Highcharts for Python Toolkit**, metaclasses are defined in the
    :mod:`.metaclasses <highcharts_core.metaclasses>` module, and most inherit from the
    :class:`.metaclasses.HighchartsMeta <highcharts_core.metaclasses.HighchartsMeta>`
    class.

    .. seealso::

      * :mod:`.metaclasses <highcharts_core.metaclasses>`
      * :class:`HighchartsMeta <highcharts_core.metaclasses.HighchartsMeta>`

  Metric
    The value of a measurement. Think of it as a "type" of number. A metric might be
    "number of miles", or "dollars spent", or "temperature". It is a value that can be
    measured and recorded, and which is typically visualized in :term:`charts`.

    .. tip::

      In a :term:`chart <charts>`, metrics are often displayed along the y-axis.

  Metric Suffix
    A symbol that is used to shorten numerical values that would otherwise have a lot of
    (typically repetitive) numbers. For example, if ``10,000`` were represented as
    ``10k``, the ``k`` would be considered the metric suffix.

    .. seealso::

      * :meth:`Language.numeric_symbols <highcharts_core.global_options.language.Language.numeric_symbols>`

  Network Graph
    A network graph is a type of relationship chart, where connnections (links)
    attract nodes (points) and other nodes repulse each other.

      .. figure:: _static/networkgraph-example.png
        :alt: NetworkGraph Example Chart
        :align: center

    .. seealso::

      * :class:`NetworkGraphOptions <highcharts_core.options.plot_options.networkgraph.NetworkGraphOptions>`
      * :class:`NetworkGraphSeries <highcharts_core.options.series.networkgraph.NetworkGraphSeries>`

  Oscillator

      .. caution::

        Oscillators are only available in **Highcharts Stock for Python**.

    An oscillator is a type of :term:`technical indicator` that is used to analyze bands
    and trend evolutions. Oscillators typically are visualized by adding high and low
    bands around the :term:`series` being analyzed and then adding a trendline calculation
    that fluctuates between these bands.

    .. seealso::

      * :term:`Technical Indicator`
      * :doc:`Supported Visualizations <visualizations>` > :ref:`Technical Indicators <technical_indicator_visualizations>`
      * :doc:`Using Highcharts Stock for Python <using>` > :ref:`Using Technical Indicators <using_technical_indicators>`

  Plot Band
    A banded area displayed on a :term:`chart <charts>` bounded by two points on an axis.
    Typically used to either help highlight a particular range of values or to visually
    differentiate groupings of :term:`metrics <metric>` along a
    :term:`dimension <dimension>`.

      .. tip::

        A common use case is to specifically highlight a section of the chart in a range
        of interest along a particular axis.

    .. seealso::

      * :class:`PlotBand <highcharts_core.options.axes.plot_bands.PlotBand>`
      * :meth:`NumericAxis.plot_bands <highcharts_core.axes.numeric.NumericAxis.plot_bands>`
      * :term:`Plot Line`

  Plot Line
    A line drawn in the :term:`chart <charts>`'s plot area spanning the plot area in a
    position relative to the axis. Typically used to demarcate a cut-off point or
    transition point along a range of values.

    .. seealso::

      * :class:`PlotLine <highcharts_core.options.axes.plot_bands.PlotLine>`
      * :meth:`NumericAxis.plot_lines <highcharts_core.axes.numeric.NumericAxis.plot_lines>`
      * :term:`Plot Band`

  Polar Chart
    A Polar chart is a radial :term:`chart <charts>` that uses values and angles
    to show information as polar coordinates. While technically they are
    :term:`Cartesian charts` (the X-axis is typically wrapped around their perimeter),
    they are usually treated and considered their own category of data visualization.

  Sankey Chart
    A sankey diagram is a type of flow diagram, in which the width of the link between
    two nodes is shown proportionally to the flow quantity.

    .. tabs::

      .. tab:: Standard Sankey

        .. figure:: _static/sankey-example.png
          :alt: Sankey Example Chart
          :align: center

      .. tab:: Inverted Sankey

        .. figure:: _static/sankey-example-inverted.png
          :alt: Inverted Sankey Example Chart
          :align: center

      .. tab:: Sankey with Outgoing Links

        .. figure:: _static/sankey-example-outgoing.png
          :alt: Sankey Example Chart with Outgoing Links
          :align: center

    .. seealso::

      * :class:`SankeyOptions <highcharts_core.options.plot_options.sankey.SankeyOptions>`
      * :class:`SankeySeries <highcharts_core.options.series.sankey.SankeySeries>`

  Series
    A collection of :term:`data points <data point>` that are expressed using a shared
    :term:`metric`, along a shared :term:`dimension`, or sharing a common property (e.g.
    a meta-data category that describes the scope of the data points).

    .. tip::

      Think of a "series" as one line on a line chart.

  Shared Options
    Shared Options are global configurations that are applied to all Highcharts
    visualizations that are displayed at the same time (on one web page, typically). They
    are typically used to practice good :iabbr:`DRY (Don't Repeat Yourself)` programming
    and to minimize the amount of code rendered in the page itself.

    In the **Highcharts for Python Toolkit**, shared options are managed through the
    :class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`
    class.

    .. seealso::

      * :doc:`Using Highcharts for Python <using>` > :ref:`Using Shared Options <shared_options>`
      * :mod:`.global_options.shared_options` <highcharts_core.global_options.shared_options>
      * :class:`SharedOptions <highcharts_core.global_options.shared_options.SharedOptions>`

  SolidGauge
    A solid gauge is a circular gauge where the value is indicated by a filled arc,
    and the color of the arc may variate with the value.

      .. figure:: _static/solidgauge-example.png
        :alt: SolidGauge Example Chart
        :align: center

    .. seealso::

      * :class:`SolidGaugeOptions <highcharts_core.options.plot_options.gauge.SolidGaugeOptions>`
      * :class:`SolidGaugeSeries <highcharts_core.options.series.gauge.SolidGaugeSeries>`

  Stem
    In a :class:`BoxPlotSeries <highcharts_core.options.series.boxplot.BoxPlotSeries>`
    or similar, the vertical line extending from the box to the
    :term:`whiskers <whisker>`.

    .. seealso::

      * :class:`BoxPlotSeries <highcharts_core.options.series.boxplot.BoxPlotSeries>`

  Styled Mode
    Styled mode is a method of adjusting the look and feel of your Highcharts
    :term:`charts` using CSS styles as opposed to the explicit configuration in
    :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>`.

    When it is enabled, styling configuration in your options will be ignored in favor of
    CSS styling. To enable it, set
    :meth:`HighchartsOptions.chart.styled_mode <highcharts_core.options.chart.ChartOptions.styled_mode>`
    to ``True``.

    .. caution::

      **Highcharts for Python** does not currently support the configuration of CSS
      styles when operating in styled mode. It is, however, an item on our roadmap
      (:issue:`7`).

    .. seealso::

      * :meth:`ChartOptions.styled_mode <highcharts_core.options.chart.ChartOptions.styled_mode>`

  Sunburst
    A Sunburst displays hierarchical data, where a level in the hierarchy is
    represented by a circle. The center represents the root node of the tree. The
    visualization bears a resemblance to both treemap and pie charts.

      .. figure:: _static/sunburst-example.png
        :alt: Sunburst Example Chart
        :align: center

    .. seealso::

      * :class:`SunburstOptions <highcharts_core.options.plot_options.sunburst.SunburstOptions>`
      * :class:`SunburstSeries <highcharts_core.options.series.sunburst.SunburstSeries>`

  Technical Indicator

      .. caution::

        Technical indicators are only available in **Highcharts Stock for Python**.

    Technical indicators are analyses performed on another :term:`series` that can provide
    additional insights. For example, by looking at a linear regression of a time series
    you can gain insight into the overarching trend of the data.

    **Highcharts Stock for Python** supports over 50 different technical indicators.
    Indicators differ from typical :term:`series` in that they do not accept data of their
    own. They do not have a ``.data`` property, and do not receive their own data points.
    Instead, they are automatically calculated by
    `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ by linking the
    indicator series to a main series on the chart itself.

    .. seealso::

      * :doc:`Supported Visualizations <visualizations>` > :ref:`Technical Indicators <technical_indicator_visualizations>`

  Tremolo
    An audio effect with repeated changes in volume over time.
    
  Untrimmed

    .. note::

      This is a term that relates to **Highcharts for Python**'s internal operations.
      If you are not :doc:`contributing` to the library, you don't need to worry about it.

    An untrimmed :class:`dict <python:dict>` representation of a **Highcharts for Python**
    object includes those properties that have :obj:`None <python:None>` values. In order
    to minimize data on the wire and maintain consistency with
    `Highcharts JS <https://www.highcharts.com/>`__, properties that have values of
    :obj:`None <python:None>` will be *removed* when serializing objects to
    :term:`JavaScript object literal notation` or to JSON. The *untrimmed* object is
    the representation of the object before those properties are removed, where values of
    :obj:`None <python:None>` are still explicitly present.

    .. seealso::

      * :ref:`Handling Default Values <handling_defaults>`

  Venn Diagram
    A Venn diagram displays all possible logical relations between a collection of
    different sets. The sets are represented by circles, and the relation between the
    sets are displayed by the overlap or lack of overlap between them. The venn
    diagram is a special case of Euler diagrams, which can also be displayed by this
    series type.

    .. tabs::

      .. tab:: Venn Diagram

        .. figure:: _static/venn-example.png
          :alt: Venn Example Chart
          :align: center

      .. tab:: Euler Diagram

        .. figure:: _static/venn-example-euler.png
          :alt: Euler Example Chart
          :align: center

    .. seealso::

      * :class:`VennOptions <highcharts_core.options.plot_options.venn.VennOptions>`
      * :class:`VennSeries <highcharts_core.options.series.venn.VennSeries>`

  Whisker
    In a :class:`BoxPlotSeries <highcharts_core.options.series.boxplot.BoxPlotSeries>`
    or similar, the horizontal lines marking low and high values

    .. seealso::

      * :class:`BoxPlotSeries <highcharts_core.options.series.boxplot.BoxPlotSeries>`

  Wordcloud
    A word cloud is a visualization of a set of words, where the size and placement of
    a word is determined by how it is weighted.

      .. figure:: _static/wordcloud-example.png
        :alt: Wordcloud Example Chart
        :align: center

    .. seealso::

      * :class:`WordcloudOptions <highcharts_core.options.plot_options.wordcloud.WordcloudOptions>`
      * :class:`WordcloudSeries <highcharts_core.options.series.wordcloud.WordcloudSeries>`

----------

fin
