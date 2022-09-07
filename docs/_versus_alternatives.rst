Since `Highcharts JS <https://www.highcharts.com/>`_ is the most popular high-end data
visualization library for JavaScript, there are a variety of alternative ways of
working with Highcharts in Python. We have an obvious bias towards
**Highcharts for Python**, but it may be useful to compare it against some commonly-used
alternatives:

.. tabs::

  .. tab:: Rolling Your Own

    By far, this is the most common approach to integrating Highcharts into your Python
    code. As a developer, you know that your JavaScript front-end will be using Highcharts
    JS. So you work in your Python backend to deliver the data to your front-end that your
    front-end will need.

    There are many patterns for rolling your own Highcharts + Python implementation, but
    the patterns I have seen most often include:

      * **Hands Off Approach**. Your Python code is "hands off" - it does not touch any
        data visualization configuration or manipulation. All of that gets handled in your
        JavaScript front-end code.
      * **JSON Serialization**. Your Python code constructs a JSON object (typically by
        serializing a Python :class:`dict <python:dict>` to JSON) which gets delivered
        to your JavaScript front-end, which then hands the JSON code off to Highcharts to
        visualize.
      * **Custom Serialization**. The most sophisticated implementations I have seen
        actually replicate much of the functionality of **Highcharts for Python**, where
        they construct JavaScript literal notation serialization and de-serialization for
        their robust use cases.
      * **Don't Use Highcharts**. In many cases, particularly when working with data
        science teams who are data scientists first and software developers by necessity,
        the team turns to weaker data visualization packages because they are available
        in Python.

    The first approach is very "clean" from a code architecture standpoint. However, in
    practice it often problematic because it delegates data manipulation and
    (potentially) business logic handling to your front-end code. Depending on the overall
    design of your software, it can make your code harder to maintain. Furthermore,
    depending on your team composition, it may simply be impractical for your team.

    The second approach is also fairly clean. JSON, after all, is easy in both Python
    and JavaScript. But JSON is a suboptimal transport mechanism for some of Highcharts
    most powerful features: callback functions. As this is native JavaScript code, they
    cannot really be serialized securely to JSON and then executed directly by the
    Highcharts library. So while simple use cases can be handled through JSON
    serialization, many more robust or sophisticated uses of Highcharts (which would rely
    on formatters, event handling, etc.) will simply not work.

    The third approach is the most robust. And for the most sophisticated Highcharts +
    Python applications that I have seen, it has been the approach of choice because it
    eliminates all of the limitations of the other approaches mentioned. But to do it on a
    custom basis takes a huge amount of effort, because the complexity of constructing a
    library like **Highcharts for Python** is non-trivial.

    And the fourth option is - in my experience - one of the most common. Even though
    plenty of developers coming to Python from the JavaScript ecosystem ask "Why can't we
    just Highcharts?", many in the Python ecosystem will answer "because it's a pain to
    do". So they turn to Highcharts alternatives that are more Python-friendly, like
    `plotly <https://plotly.com/python/>`_.

    .. tip::

      **When to use it?**

      In practice, I find that rolling my own is great when I'm doing a limited number of
      simple and static (non-interactive) visualizations. Then I just quickly use some
      simple JSON serialization, and rapidly get a high-quality chart visualized cleanly
      using Highcharts. But anything more robust than that is going to prove "hacky" and
      incredibly difficult to maintain.

      Which is why I wrote **Highcharts for Python**.

  .. tab:: panel-highcharts

    The `panel-highcharts <https://pypi.org/project/panel-highcharts/>`_ library is -
    honestly - fantastic. It is a excellent wrapper for the Highcharts JS library to
    enable exploratory data analysis (EDA) in Jupyter Notebooks or in Holoviz web
    applications.

    There are really two limitations to be aware of:

      * It relies on the Jupyter Labs/Notebook or Holoviz context, which means that it
        would be hard to utilize unless you happen to be working in Jupyter or Holoviz.
      * It relies on configuration via :class:`dict <python:dict>` objects that map 1:1
        to the Highcharts API. In practice, this forces the developer to switch between
        Pythonic ``snake_case`` convention and JavaScript ``camelCase`` conventions
        within the same code. Not a big problem, but annoying.

    .. tip::

      **When to use it?**

      If my use cases involved highly-interactive exploratory data analysis in a
      Jupyter Labs/Notebook environment, I would seriously consider using this library.

      However, those are some pretty specific gating conditions. For integration with
      a non-Jupyter application? That's not what this library was designed for, and I'd
      rather opt for a more robust solution like **Highcharts for Python**.

  .. tab:: python-highcharts

    The `python-highcharts <https://github.com/kyper-data/python-highcharts/tree/master>`_
    library is a great start to working with Highcharts in the Python ecosystem. However,
    given that its last release was in December 2018, it can best be considered "stale"
    and "impractical".

    While the design of this library is an excellent start, and in some ways served as an
    inspiration for **Highcharts for Python**, it is not a practical solution for several
    key reasons:

      * **"Stale" / Unmaintained?** The last commit to the library was in 2018, almost
        four years ago (as of the time of writing).
      * **Not comprehensive**. The library is not comprehensive relative to the Highcharts
        API, and does not support many of the features introduced over the last several
        years to the Highcharts API. Not all Highcharts classes are supported, and not all
        Highcharts functionality is available.
      * **JavaScript-forward style**. The library relies heavily on Python
        :class:`dict <python:dict>` objects but using JavaScript style for naming
        conventions. This is not that big of a deal, but when building complex
        applications in Python it can be annoying to constantly context-switch from Python
        ``snake_case`` standards to JavaScript ``camelCase`` style.

    .. tip::

      **When to use it?**

      I wouldn't rely heavily on it, as it no longer seems to be maintained, has fallen
      out of alignment with more recent releases of Highcharts JS and its functionality is
      (by design) not comprehensive.

  .. tab:: PyHighcharts

    The `PyHighcharts <https://github.com/fidyeates/PyHighcharts>`_ library is closest
    in philosophy to **Highcharts for Python**, but it is also much more limited than any
    of the other alternatives discussed:

    * **Dead library**. This library hasn't seen any new releases since 2015. There's an
      open question whether it will even import / work in modern versions of Python (I
      admit, I haven't tested it meaningfully in the last couple of years).
    * **Extremely limited support**. By design, this library only supports a handful of
      the visualizations offered by Highcharts JS. Furthermore, even for those
      visualization types, only a limited number of configuration options are available.
      And because the library has not been updated in about seven years, there's an open
      question whether it will even work to produce relevant visualizations.

    .. tip::

      **When to use it?**

      I wouldn't. While you might still be able to use the other alternatives listed,
      this is one that I would not recommend be touched under any circumstances.
