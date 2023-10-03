############################################
Creating JavaScript Callback Functions
############################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

Highcharts (JS) is known for how easy it is to configure and style
beautiful, interactive data visualizations. One of the core tools
it uses to achieve this is 
:term:`callback functions <callback function>`.

These can be used throughout your chart configuration, and let you
write custom code that will do what you need it to do in specific
situations. It is incredibly powerful!

However, Highcharts (JS) is a *JavaScript* suite, and that means 
that it only works with *JavaScript* callback functions. So if
we're using **Highcharts for Python**, how do we create JavaScript
:term:`callback functions <callback function>` that Highcharts (JS)
will know how to leverage?

The answer is simple: **Highcharts for Python** provides a special
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
class that you can use to create JavaScript 
:term:`callback functions <callback function>`. When using this class,
you can either:

#. Write your own JavaScript function and the 
   :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
   class will serialize it to JavaScript when needed, or
#. You can write a :term:`callback function` in *Python*, and rely on either 
   `OpenAI <https://www.openai.com>`__'s GPT or `Anthropic <https://anthropic.com>`__'s
   Claude generative AI model to suggest an equivalent JavaScript function.

Because you're using **Highcharts for Python**, let's look at the AI-driven 
approach first, because we already know how to write Python code. No JavaScript 
needed!

----------------------------

********************************************************
Creating Callback Functions using Generative AI
********************************************************

The 
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
class has a special helper class method called 
:meth:`.from_python() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_python>`
which can automatically create a 
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
instance containing the JavaScript function that you need.

Here's how that works. Let's imagine a scenario where we want a custom tooltip formatter function 
that customizes the content of each data point's tooltips. We can write that function in Python like
so:

  .. code-block:: python

    def my_custom_formatter():
        return f'The value for <b>{this.x}</b> is <b>{this.y}</b>.'

Really pretty straightforward, right? Now we can produce its equivalent by passing 
``my_custom_formatter`` as an argument to
:meth:`.from_python() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_python>`:

  .. code-block:: python

    my_callback = CallbackFunction.from_python(my_custom_formatter)

What the 
:meth:`.from_python() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_python>`
method call will do is:

  #. It will take the *Python* function's source code, and pass it to the generative AI model of your 
     choice. 
  #. The AI will return a *JavaScript* function that the AI believes will do the same thing as your 
     *Python* function.
  #. And it will then load that *JavaScript* function into a new 
     :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
     instance.

Now, when you use this 
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
instance in your chart configuration, it will get serialized to its approrpriate *JavaScript* source
code form when appropriate, for example when calling 
:meth:`Chart.display() <highcharts_core.chart.Chart.display>` or 
:meth:`Chart.to_js_literal() <highcharts_core.chart.Chart.to_js_literal>`.

Using Different Models
===============================

**Highcharts for Python** supports different models provided by `OpenAI <https://www.openai.com>`__
and `Anthropic <https://anthropic.com>`__. 

OpenAI's models in particular differ based on the *version* of GPT that the model supports, as
well as the number of tokens that they allow (more tokens mean they can convert more complicated/longer
function). Most typical callback functions should be converted reasonably reliably using 
the default model ``gpt-3.5-turbo``, though others are available:

* **OpenAI**

  * ``'gpt-3.5-turbo'`` (default)
  * ``'gpt-3.5-turbo-16k'``
  * ``'gpt-4'``
  * ``'gpt-4-32k'``

* **Anthropic**

  * ``'claude-instant-1'``
  * ``'claude-2'``

To use a different model, simply pass the ``model`` argument to the
:meth:`.from_python() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_python>`
method:

  .. code-block:: python

    my_callback = CallbackFunction.from_python(my_custom_formatter, model = "gpt-4")

Authenticating with Your AI Provider
==========================================

  .. caution::

    Because this relies on the outside APIs exposed by 
    `OpenAI <https://www.openai.com/>`__ and `Anthropic <https://www.anthropic.com>`__,
    if you wish to use one of their models you *must* supply your own API key.
    These are paid services which they provide, and so you *will* be incurring
    costs by using these generative AIs.

To use one of the supported AI models, you *must* have a valid user/customer account with either
`OpenAI <https://www.openai.com>`__ or `Anthropic <https://anthropic.com>`__. You must also have
an API key to their respective platform that has permission to use the model you request. You can
set your account up and get the relevant API key from each of the AI providers, respectively.

When you have the API key, you can pass it in as an argument (``api_key``) to the 
:meth:`.from_python() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_python>`
method:

  .. code-block:: python

    my_callback = CallbackFunction.from_python(my_custom_formatter, api_key = "YOUR-API-KEY-GOES-HERE")

However, if you do not supply an explicit ``api_key`` value, **Highcharts for Python** will look for
the API key in your ``OPENAI_API_KEY`` or ``ANTHROPIC_API_KEY`` environment variables.

.. tip::

  **BEST PRACTICE:** Treat your API key as a highly-sensitive piece of information. It should never
  be listed in your source code, or in your Jupyter Notebook. It should *only* be read from environment
  variables, which in turn should get set with as few places where your API key is visible/available as
  possible.

Reviewing Your JavaScript Code
===================================

  .. warning::

    Generating the JavaScript source code is *not* deterministic.
    That means that it may not be correct, and we **STRONGLY** 
    recommend reviewing it before using it in a production 
    application.

    Every single generative AI is known to have issues - whether 
    "hallucinations", biases, or incoherence. We cannot stress
    enough:

    **DO NOT RELY ON AI-GENERATED CODE IN PRODUCTION WITHOUT HUMAN REVIEW.**

    That being said, for "quick and dirty" EDA, fast prototyping, etc.
    the functionality may be "good enough".

Once you have created a
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
instance using the 
:meth:`.from_python() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_python>`
method, you can review the JavaScript source code that was generated by calling ``str()`` on your
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` instance:

  .. code-block::

    print(str(my_callback))

    # Output:
    # function my_custom_formatter() { return 'The value for <b>' + this.x + '</b> is <b>' + this.y + '</b>.'; }

We **STRONGLY** recommend reviewing the JavaScript source code that was generated before using it in 
production. Even if you are not a JavaScript expert, since you know Python and you know what your function *should*
be doing, you can probably follow along close-enough to make sure the JavaScript code "looks right".

  .. tip::

    **BEST PRACTICE:** Never let the AI generate JavaScript code based on *user-entered* Python code.

    Doing so may introduce unintended security vulnerabilities into your application, and should be
    considered *VERY* bad practice.

-------------------------------------

********************************************************
Creating Callback Functions Directly
********************************************************

If you do not wish to use generative AI to create your :term:`callback functions <callback function>`,
you can simply create 
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` 
instances directly. You can do this by:

Instantiating the ``CallbackFunction`` Directly
===================================================

.. code-block:: python

  my_callback = CallbackFunction(function_name = 'my_formatter',
                                 arguments = None,
                                 body = """return 'The value for <b>' + this.x + '</b> is <b>' + this.y + '</b>.';""")

When instantiating the callback function directly, you supply the body of the function as a string to
the ``body`` argument.  A best practice is to use Python's triple-quote syntax to make it easier to
handle quotation marks *within* your JavaScript code.

Using ``.from_js_literal()``
=================================

If you have your JavaScript function in a string, you can use the
:meth:`CallbackFunction.from_js_literal() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_js_literal>` class method to create the callback function instance:

  .. code-block:: python

    callback_as_str = """function my_formatter() {
       return 'The value for <b>' + this.x + '</b> is <b>' + this.y + '</b>.'; 
    }"""

    my_callback = CallbackFunction.from_js_literal(callback_as_str)

----------

And that's it! When your
:class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
instances are used in your chart configuration, they will automatically be serialized to the 
appropriate JavaScript syntax when needed.