Since `Highcharts Core (JS) <https://www.highcharts.com/products/highcharts/>`_ is such a
popular high-end data visualization library for JavaScript, there are a variety of 
ways to work with it in Python. We have an obvious bias towards the
**Highcharts for Python Toolkit**, but it may be useful to compare that toolkit against 
some commonly-used alternatives:

.. tabs::

  .. tab:: Rolling Your Own

    By far, this is the most common approach to integrating Highcharts into your Python
    code. As a developer, you know that your JavaScript front-end will be using Highcharts
    (JS)). So you work in your Python backend to deliver the data to your front-end that your
    front-end will need.

    There are many patterns for rolling your own Highcharts + Python implementation, but
    the patterns we have seen most often include:

    .. tabs:: 
      
      .. tab:: Hands-Off Approach

        Your Python code is "hands off" - it does not touch any data visualization configuration 
        or manipulation. All of that gets handled in your JavaScript front-end code.

        This approach is very "clean" from a code architecture standpoint. However, in
        practice it often problematic because it delegates data manipulation and
        (potentially) business logic handling to your front-end code. Depending on the overall
        design of your software, it can make your code harder to maintain. Furthermore,
        depending on your team composition, it may simply be impractical for your team.

      .. tab:: JSON
        
        Your Python code constructs a JSON object (typically by serializing a Python 
        :class:`dict <python:dict>` to JSON) which gets delivered to your JavaScript front-end, 
        which then hands the JSON code off to Highcharts to visualize.

        This approach is also fairly clean. JSON, after all, is easy in both Python
        and JavaScript. But JSON is a suboptimal transport mechanism for some of Highcharts
        most powerful features: callback functions. As this is native JavaScript code, they
        cannot really be serialized securely to JSON and then executed directly by the
        Highcharts library. So while simple use cases can be handled through JSON
        serialization, many more robust or sophisticated uses of Highcharts (which would rely
        on formatters, event handling, etc.) will simply not work.

      .. tab:: Custom Serialization
        
        The most sophisticated implementations we have seen actually replicate much of the 
        functionality of the **Highcharts for Python Toolkit**, where they construct 
        :term:`JavaScript object literal notation` serialization and de-serialization for their 
        robust use cases.

        This approach is the most robust of all custom implementations, for obvious reasons. 
        However, as with any full-fledged custom implementation your mileage may vary. For the 
        most sophisticated Highcharts + Python applications that we have seen, this has been 
        the approach of choice because it eliminates all of the limitations of the other 
        approaches mentioned. 
        
        But, to create custom serialization on a one-off/custom basis can take a large amount 
        of effort. Constructing a comprehensive solution like the **Highcharts for Python Toolkit** 
        is deeply non-trivial, and so we think it's wiser to use a toolkit where:
        
          * the implementation/heavy lifting has been done for you
          * you are guaranteed ongoing maintenance
          * you are guaranteed available support

      .. tab:: Opt Out
        
        In many cases, particularly when working with data science teams who are data scientists 
        first and software developers by necessity, the team traditionally turns to weaker data 
        visualization packages simply because those packages are available in Python.

        This option has historically - sadly - been fairly common, and is one of the primary 
        reasons for our development of the **Highcharts for Python Toolkit**. Even though plenty 
        of developers coming to Python from the JavaScript ecosystem ask "Why can't we just use 
        Highcharts?", many in the Python ecosystem will answer "because it's a pain to do". So 
        they turn to Highcharts alternatives that are are more limited but more Python-friendly.

    .. tip::

      **When to use it?**

      In practice, we find that rolling our own solution is great when doing a limited number of
      simple and static (non-interactive) visualizations. Then you can just quickly use some
      simple JSON serialization, and rapidly get a high-quality chart visualized cleanly
      using Highcharts. But anything more robust than that is going to prove "hacky" and
      incredibly difficult to maintain.

      Which is why we created the **Highcharts for Python Toolkit** in the first place, so that:

      * you gain the ability to use as much or as little of Highcharts rich functionality as you
        need
      * you get native integration with key Python ecosystem members "out of the box"
      * you don't have to worry about maintaining the "glue" code connecting your Python
        implementation with Highcharts (JS)
      * you have support available when you need it

  .. tab:: panel-highcharts

    The `panel-highcharts <https://pypi.org/project/panel-highcharts/>`_ library is -
    honestly - fantastic. It is a excellent wrapper for the Highcharts (JS) suite to
    enable exploratory data analysis (EDA) in Jupyter Notebooks or in Holoviz web
    applications.

    There are really two limitations to be aware of:

      * It relies on the Jupyter Labs/Notebook or Holoviz context, which means that it
        would be hard to utilize unless you happen to be working in Jupyter or Holoviz.
      * It relies on configuration via :class:`dict <python:dict>` objects that map 1:1
        to the Highcharts API. In practice, this forces the developer to switch between
        Pythonic ``snake_case`` convention and JavaScript ``camelCase`` conventions
        within the same code. Not a big problem, but annoying.
      * To really benefit from its capabilities, it requires a fair bit of Holoviz
        boilerplate and widget configuration, which can be complicated, verbose, and 
        "fiddly".

    .. tip::

      **When to use it?**

      If your use case is limited to highly-interactive exploratory data analysis in a 
      Jupyter Labs/Notebook environment and you are willing to construct some complicated
      Holoviz widget configuration code, it may be worth considering this library.

      However, those are some pretty specific gating conditions. For integration with
      a non-Jupyter application? That's not what the **Highcharts for Python Toolkit** was 
      designed for.

  .. tab:: python-highcharts

    The `python-highcharts <https://github.com/kyper-data/python-highcharts/tree/master>`_
    library is a great start to working with Highcharts in the Python ecosystem. However,
    given that its last release was in December 2018, it can best be considered "stale"
    and "impractical".

    While the design of this library is an excellent start, and in some ways served as an
    inspiration for the **Highcharts for Python Toolkit**, it is not a practical solution 
    for several key reasons:

      * **"Stale" / Unmaintained?** The last commit to the library was in 2018, almost
        four years ago (as of the time of writing).
      * **Not comprehensive**. The library is not comprehensive relative to the Highcharts
        API, and does not support many of the features and chart types introduced over the 
        last several years. Not all Highcharts chart types and classes are supported, and 
        not all Highcharts functionality is available.
      * **JavaScript-forward style**. The library relies heavily on Python
        :class:`dict <python:dict>` objects but relying on the JavaScript style for naming
        conventions. This is not that big of a deal, but when building complex
        applications in Python it can be annoying to constantly context-switch from Python
        ``snake_case`` standards to JavaScript ``camelCase`` style.

    .. tip::

      **When to use it?**

      We wouldn't rely heavily on it, as it no longer seems to be maintained, has fallen
      out of alignment with more recent releases of the Highcharts suite and its functionality is
      (by design) not comprehensive.

  .. tab:: PyHighcharts

    The `PyHighcharts <https://github.com/fidyeates/PyHighcharts>`_ library is closest
    in philosophy to the **Highcharts for Python Toolkit**, but it is also much more limited than 
    any of the other alternatives discussed:

    * **Dead library**. This library hasn't seen any new releases since 2015. There's an
      open question whether it will even import / work in modern versions of Python (we haven't 
      tested it meaningfully in the last couple of years).
    * **Extremely limited support**. By design, this library only supports a handful of
      the visualizations offered by Highcharts (JS). Furthermore, even for those
      visualization types, only a limited number of configuration options are available.
      And because the library has not been updated in about seven years, there's an open
      question whether it will even work to produce relevant visualizations.

    .. tip::

      **When to use it?**

      We wouldn't. While you might still be able to use the other alternatives listed,
      this is one that we would not recommend be touched under any circumstances.
