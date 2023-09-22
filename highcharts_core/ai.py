import os
from collections import UserDict

try:
    from dill.source import getsource
    HAS_DILL = True
except ImportError:
    HAS_DILL = False

try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    
try:
    from anthropic import Anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
    
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from validator_collection import validators, checkers

from highcharts_core import errors


OPENAI_MESSAGES = [
    {
        'role': 'system',
        'content': """Read the Python source code provided. Consider its arguments, logic, and output, and produce a JavaScript function that accepts the same arguments, follows the same logic, replaces snake_case variables with camelCase variables, and produces the same output. Ensure that if Timer or sleep is used in the Python code, it is replaced by setTimeout in the JavaScript code."""  # noqa: E501
    },
    {
        'role': 'user',
        'name': 'example-input-1',
        'content': """```def addPoint(e):     point = e.point     series = e.target      if not series.pulse:         series.pulse = series.chart.renderer.circle().add(series.marker_group)      def pulse():         series.pulse.attr({             'x': series.x_axis.to_pixels(point.x, True),             'y': series.y_axis.to_pixels(point.y, True),             'r': series.options.marker.radius,             'opacity': 1,             'fill': series.color         }).animate({             'r': 20,             'opacity': 0         }, {             'duration': 1000         })      Timer(1/1000, pulse).start()```"""  # noqa: E501
    },
    {
        'role': 'assistant',
        'name': 'example-output-1',
        'content': """```function addPoint(e) {   const point = e.point;   const series = e.target;    if (!series.pulse) {       series.pulse = series.chart.renderer.circle().add(series.markerGroup);     }     setTimeout(() => {         series.pulse.attr({           'x': series.xAxis.toPixels(point.x, true),           'y': series.yAxis.toPixels(point.y, true),           'r': series.options.marker.radius,           'opacity': 1,           'fill': series.color         }).animate({           'r': 20,           'opacity': 0         }, {           'duration': 1000         });     }, 1);```"""  # noqa: E501
    },
    {
        'role': 'user',
        'name': 'example-input-2',
        'content': """```def click(e):     x = round(e.x_axis[0].value)     y = round(e.y_axis[0].value)     series = this.series[0]      series.addPoint([x, y])```"""  # noqa: E501
    },
    {
        'role': 'assistant',
        'name': 'example-output-2',
        'content': """```function click(e) {   const x = Math.round(e.xAxis[0].value);   const y = Math.round(e.yAxis[0].value);   const series = this.series[0];    series.addPoint([x, y]); }```"""  # noqa: E501
    },
    {
        'role': 'user',
        'name': 'example-input-3',
        'content': """```def click():     if len(this.series.data) > 1:         this.remove()```"""  # noqa: E501
    },
    {
        'role': 'assistant',
        'name': 'example-output-3',
        'content': """```function click() {   if (this.series.data.length > 1) {     this.remove();   } }```"""  # noqa: E501
    },
    {
        'role': 'user',
        'name': 'task',
        'content': """The Python source code, wrapped in three backticks, is: ```<HCP: REPLACE WITH SOURCE CODE>``` Please produce the JavaScript code, wrapping the JavaScript code in three backticks. If you are unable to do so, please say "I cannot convert the Python code to JavaScript." """  # noqa: E501
    }
]


ANTHROPIC_PROMPT = """\n\nHuman: Read the Python source code provided. Consider its arguments, logic, and output, and produce a JavaScript function that accepts the same arguments, follows the same logic, replaces snake_case variables with camelCase variables, and produces the same output. Ensure that if Timer or sleep is used in the Python code, it is replaced by setTimeout in the JavaScript code.

Here are some examples:
<example>
H: <python>def addPoint(e):     point = e.point     series = e.target      if not series.pulse:         series.pulse = series.chart.renderer.circle().add(series.marker_group)      def pulse():         series.pulse.attr({             'x': series.x_axis.to_pixels(point.x, True),             'y': series.y_axis.to_pixels(point.y, True),             'r': series.options.marker.radius,             'opacity': 1,             'fill': series.color         }).animate({             'r': 20,             'opacity': 0         }, {             'duration': 1000         })      Timer(1/1000, pulse).start()</python>
A: <javascript>function addPoint(e) {   const point = e.point;   const series = e.target;    if (!series.pulse) {       series.pulse = series.chart.renderer.circle().add(series.markerGroup);     }     setTimeout(() => {         series.pulse.attr({           'x': series.xAxis.toPixels(point.x, true),           'y': series.yAxis.toPixels(point.y, true),           'r': series.options.marker.radius,           'opacity': 1,           'fill': series.color         }).animate({           'r': 20,           'opacity': 0         }, {           'duration': 1000         });     }, 1);</javascript>
</example>
<example>
H: <python>def click(e):     x = round(e.x_axis[0].value)     y = round(e.y_axis[0].value)     series = this.series[0]      series.addPoint([x, y])</python>
A: <javascript>function click(e) {   const x = Math.round(e.xAxis[0].value);   const y = Math.round(e.yAxis[0].value);   const series = this.series[0];    series.addPoint([x, y]); }</javascript>
</example>
<example>
H: <python>function click() {   if (this.series.data.length > 1) {     this.remove();   } }</python>
A: <javascript>function click() {   if (this.series.data.length > 1) {     this.remove();   } }</javascript>
</example>

The Python source code, wrapped in <python></python>, is:

<python><HCP: REPLACE WITH SOURCE CODE></python>

Please produce the JavaScript code, wrapping the JavaScript code in <javascript></javascript> tags. If you are unable to do so, please say "I cannot convert the Python code to JavaScript."

Assistant:
"""  # noqa: E501

SUPPORTED_MODELS = {
    'gpt-3.5-turbo': ('OpenAI', OPENAI_MESSAGES),
    'gpt-3.5-turbo-16k': ('OpenAI', OPENAI_MESSAGES),
    'gpt-4': ('OpenAI', OPENAI_MESSAGES),
    'gpt-4-32k': ('OpenAI', OPENAI_MESSAGES),
    'claude-instant-1': ('Anthropic', ANTHROPIC_PROMPT),
    'claude-2': ('Anthropic', ANTHROPIC_PROMPT),
}


def get_source(callable):
    """Retrieve the source of ``callable``.
    
    :param callable: The Python callable object (function or method).
    :type callable: callable
    
    :returns: The source code of ``callable``.
    :rtype: :class:`str <python:str>`
    
    :raises HighchartsValueError: if ``callable`` is not a Python callable
    :raises HighchartsDependencyError: if `dill <https://dill.readthedocs.io/>`__
      is not installed
    
    """
    if not HAS_DILL:
        raise errors.HighchartsDependencyError('dill is required to retrieve the '
                                               'source of a callable, however it was '
                                               'not found in the runtime environment. '
                                               'Please install using "pip install dill"')

    if not checkers.is_callable(callable):
        raise errors.HighchartsValueError(f'callable must be a Python callable. Was: '
                                          f'{callable.__class__.__name__}')

    source_code = getsource(callable, force = True)

    return source_code


def convert_to_js(callable,
                  model = 'gpt-3.5-turbo',
                  api_key = None,
                  openai_api_type = None,
                  openai_api_base = None,
                  openai_api_version = None,
                  openai_deployment_id = None,
                  **kwargs):
    """Converts ``source`` into a JavaScript function.
    
    :param callable: The Python callable to convert.
    :type callable: callable
    
    :param model: The generative AI model to use. 
      Defaults to ``'gpt-3.5-turbo'``. Accepts:
      
        * ``'gpt-3.5-turbo'`` (default)
        * ``'gpt-3.5-turbo-16k'``
        * ``'gpt-4'``
        * ``'gpt-4-32k'``
        * ``'claude-instant-1'``
        * ``'claude-2'``
        
    :type model: :class:`str <python:str>`
    
    :param api_key: The API key used to authenticate against the
      generative AI provider. Defaults to 
      :obj:`None <python:None>`, which then tries to find the API
      key in the appropriate environment variable:
      
        * ``OPENAI_API_KEY`` if using an 
          `OpenAI <https://www.openai.com/>`__ provided model
        * ``ANTHROPIC_API_KEY`` if using an 
          `Anthropic <https://www.anthropic.com/>`__ provided model
          
    :type api_key: :class:`str <python:str>` or :obj:`None <python:None>`
    
    :param openai_api_type: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to ``'azure'``.
      Defaults to :obj:`None <python:None>`.
    :type openai_api_type: :class:`str <python:str>` or 
      :obj:`None <python:None>`

    :param openai_api_base: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your base API
      endpoint. Defaults to :obj:`None <python:None>`.
    :type openai_api_base: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param openai_api_version: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your API version.
      Defaults to :obj:`None <python:None>`.
    :type openai_api_version: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param openai_deployment_id: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your deployment
      ID. Defaults to :obj:`None <python:None>`.
    :type openai_deployment_id: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param **kwargs: Additional keyword arguments which are passed to
      the underlying model API. Useful for advanced configuration of
      the model's behavior.
    
    :returns: The JavaScript source code produced by the model.
    
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
        
    :rtype: :class:`str <python:str>`
    
    :raises HighchartsValueError: if ``callable`` is not a Python callable
    :raises HighchartsValueError: if no ``api_key`` is available
    :raises HighchartsDependencyError: if a required dependency is not
      available in the runtime environment
    :raises HighchartsModerationError: if using an OpenAI model, and 
      OpenAI detects that the supplied input violates their usage policies
    :raises HighchartsPythonConversionError: if the model was unable to
      convert ``callable`` into JavaScript source code
    
    """
    model = validators.string(model, allow_empty = False)
    model = model.lower()
    if model not in SUPPORTED_MODELS:
        raise errors.HighchartsValueError(f'The model supplied is not supported. '
                                          f'Received: {model}.')
    
    source = get_source(callable)
    
    provider = SUPPORTED_MODELS[model][0]
    prompt = SUPPORTED_MODELS[model][1]

    if provider == 'OpenAI':
        prompt[-1]['content'] = prompt[-1]['content'].replace(
            '<HCP: REPLACE WITH SOURCE CODE>', source
        )
        api_key = api_key or os.getenv('OPENAI_API_KEY', None)
        convert = openai_conversion
    elif provider == 'Anthropic':
        api_key = api_key or os.getenv('ANTHROPIC_API_KEY', None)
        prompt = prompt.replace('<HCP: REPLACE WITH SOURCE CODE>', source)
        convert = anthropic_conversion
    else:
        convert = None
        
    if not api_key:
        raise errors.HighchartsValueError('No API key was provided, and none '
                                          'was found in supported environment '
                                          'variables.')

    if provider == 'OpenAI':
        is_acceptable, flags = openai_moderate(prompt[-1],
                                               api_key,
                                               api_type = openai_api_type,
                                               api_base = openai_api_base,
                                               api_version = openai_api_version,
                                               deployment_id = openai_deployment_id)
        if not is_acceptable:
            raise errors.HighchartsModerationError(
                f'The supplied prompt violates OpenAI moderation policies. '
                f'Please review your callable / Python function, and address '
                f'the topics flagged in the following moderation report:\n{flags}'
            )

        result = convert(prompt,
                         model,
                         api_key,
                         api_type = openai_api_type,
                         api_base = openai_api_base,
                         api_version = openai_api_version,
                         deployment_id = openai_deployment_id,
                         **kwargs)
    else:
        result = convert(prompt, model, api_key, **kwargs)
    
    return result


def openai_moderate(prompt,
                    api_key = None,
                    api_type = None,
                    api_base = None,
                    api_version = None,
                    deployment_id = None):
    """Evaluates ``prompt`` against OpenAI's content moderation policies to determine if
    it violates their usage policies.
    
    This function calls OpenAI's `moderation API <https://platform.openai.com/docs/guides/moderation>`__
    to evaluate whether ``prompt`` violates their content moderation policies.
    
    :param prompt: The prompt to evaluate.
    :type prompt: :class:`str <python:str>`
    
    :param api_key: The API key used to authenticate with OpenAI.
      Defaults to :obj:`None <python:None>`, which then tries to find the API
      key in the ``OPENAI_API_KEY``.
    :type api_key: :class:`str <python:str>` or :obj:`None <python:None>`
    
    :param api_type: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to ``'azure'``.
      Defaults to :obj:`None <python:None>`.
    :type api_type: :class:`str <python:str>` or 
      :obj:`None <python:None>`

    :param api_base: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your base API
      endpoint. Defaults to :obj:`None <python:None>`.
    :type api_base: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param api_version: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your API version.
      Defaults to :obj:`None <python:None>`.
    :type api_version: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param deployment_id: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your deployment
      ID. Defaults to :obj:`None <python:None>`.
    :type deployment_id: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :returns: A :class:`tuple <python:tuple>` containing two members:
    
      1. ``True`` if the prompt is acceptable, ``False`` otherwise
      2. A :class:`dict <python:dict>` containing the topics flagged by
         OpenAI's moderation tools. This :class:`dict <python:dict>` will
         be empty if the prompt is acceptable.
         
    :rtype: :class:`tuple <python:tuple>` of :class:`bool <python:bool>` and
      :class:`dict <python:dict>`
      
    :raises HighchartsDependencyError: if `openai <https://pypi.org/project/openai/>`__
      is not installed/available in the runtime environment
    :raises HighchartsValueError: if no ``api_key`` is available
    
    """
    if not HAS_OPENAI:
        raise errors.HighchartsDependencyError('openai is required to use OpenAI '
                                               'models, however it was not found in '
                                               'the runtime environment. Please '
                                               'install using "pip install openai"')
    api_key = api_key or os.getenv('OPENAI_API_KEY', None)
    if not api_key:
        raise errors.HighchartsValueError('No API key was provided, and none '
                                          'was found in supported environment '
                                          'variables.')

    openai.api_key = api_key
    if api_type:
        openai.api_type = api_type
        openai.api_base = api_base
        openai.api_version = api_version

    kwargs = {
        'input': prompt['content']
    }
    if deployment_id:
        kwargs['deployment_id'] = deployment_id

    result = openai.Moderation.create(**kwargs)
    is_flagged = result['results'][0]['flagged']
    flags = result['results'][0]['categories']
    is_acceptable = is_flagged is False
    if is_acceptable:
        flags = {}

    return is_acceptable, flags


def openai_conversion(prompt,
                      model = 'gpt-3.5-turbo',
                      api_key = None,
                      api_type = None,
                      api_base = None,
                      api_version = None,
                      deployment_id = None,
                      **kwargs):
    """Submits ``prompt`` to the OpenAI API for conversion into JavaScript source code.

    :param prompt: The prompt to evaluate, using the Chat Completions form with a 
      few-shot strategy.
    :type prompt: :class:`list <python:list>` of :class:`dict <python:dict>`

    :param model: The generative AI model to use. 
      Defaults to ``'gpt-3.5-turbo'``. Accepts:
      
        * ``'gpt-3.5-turbo'`` (default)
        * ``'gpt-3.5-turbo-16k'``
        * ``'gpt-4'``
        * ``'gpt-4-32k'``
        
    :type model: :class:`str <python:str>`
    
    :param api_key: The API key used to authenticate against
      OpenAI. Defaults to :obj:`None <python:None>`, which 
      then tries to find the ``OPENAI_API_KEY`` environment
      variable.
    :type api_key: :class:`str <python:str>` or :obj:`None <python:None>`
    
    :param api_type: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to ``'azure'``.
      Defaults to :obj:`None <python:None>`.
    :type api_type: :class:`str <python:str>` or 
      :obj:`None <python:None>`

    :param api_base: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your base API
      endpoint. Defaults to :obj:`None <python:None>`.
    :type api_base: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param api_version: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your API version.
      Defaults to :obj:`None <python:None>`.
    :type api_version: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param deployment_id: If using `OpenAI <https://www.openai.com>`__
      and Azure endpoints, this value should be set to your deployment
      ID. Defaults to :obj:`None <python:None>`.
    :type deployment_id: :class:`str <python:str>` or
      :obj:`None <python:None>`

    :param **kwargs: Additional keyword arguments which are passed to
      the underlying model API. Useful for advanced configuration of
      the model's behavior.

    :returns: The JavaScript source code produced by the model.
    
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
        
    :rtype: :class:`str <python:str>`
    
    :raises HighchartsValueError: if no ``api_key`` is available
    :raises HighchartsDependencyError: if a required dependency is not
      available in the runtime environment
    """
    if not HAS_OPENAI:
        raise errors.HighchartsDependencyError('openai is required to use OpenAI '
                                               'models, however it was not found in '
                                               'the runtime environment. Please '
                                               'install using "pip install openai"')
    api_key = api_key or os.getenv('OPENAI_API_KEY', None)
    if not api_key:
        raise errors.HighchartsValueError('No API key was provided, and none '
                                          'was found in supported environment '
                                          'variables.')
        
    model = validators.string(model, allow_empty = False)
    model = model.lower()
    if model not in ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k']:
        raise errors.HighchartsValueError(f'The model supplied is not supported. '
                                          f'Received: {model}.')

    openai.api_key = api_key
    if api_type:
        openai.api_type = api_type
        openai.api_base = api_base
        openai.api_version = api_version

    if not deployment_id:
        result = openai.ChatCompletion.create(model = model,
                                              messages = prompt,
                                              **kwargs)
    else:
        result = openai.ChatCompletion.create(deployment_id = deployment_id,
                                              model = model,
                                              messages = prompt,
                                              **kwargs)

    raw_response = result.choices[0].message.content
    starting_index = raw_response.find('```')
    ending_index = raw_response.rfind('```')

    if 'I cannot convert the Python code to JavaScript.' in raw_response:
        return errors.HighchartsPythonConversionError(
            f'OpenAI was unable to convert the '
            f'callable to a JavaScript function '
            f'using the "{model}" model. Please '
            f'try again, possibly selecting a '
            f'different model.'
        )
    elif starting_index == -1 or ending_index == -1:
        return errors.HighchartsPythonConversionError(
            f'OpenAI was unable to convert the '
            f'callable to a JavaScript function '
            f'using the "{model}" model. Please '
            f'try again, possibly selecting a '
            f'different model.')

    js_as_str = raw_response[starting_index + 3:ending_index]
    if js_as_str.startswith('javascript\n') or js_as_str.startswith('JavaScript\n'):
        js_as_str = js_as_str[11:]

    return js_as_str


def anthropic_conversion(prompt,
                         model = 'gpt-3.5-turbo',
                         api_key = None,
                         **kwargs):
    """Submits ``prompt`` to the Anthropic API for conversion into JavaScript source code.

    :param prompt: The prompt to evaluate.
    :type prompt: :class:`str <python:str>`

    :param model: The generative AI model to use. 
      Defaults to ``'claude-instant-1'``. Accepts:
      
        * ``'claude-instant-1'``
        * ``'claude-2'``
        
    :type model: :class:`str <python:str>`
    
    :param api_key: The API key used to authenticate against
      OpenAI. Defaults to :obj:`None <python:None>`, which 
      then tries to find the ``ANTHROPIC_API_KEY`` environment
      variable.
    :type api_key: :class:`str <python:str>` or :obj:`None <python:None>`
    
    :param **kwargs: Additional keyword arguments which are passed to
      the underlying model API. Useful for advanced configuration of
      the model's behavior.

    :returns: The JavaScript source code produced by the model.
    
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
        
    :rtype: :class:`str <python:str>`
    
    :raises HighchartsValueError: if no ``api_key`` is available
    :raises HighchartsDependencyError: if a required dependency is not
      available in the runtime environment
    """
    if not HAS_ANTHROPIC:
        raise errors.HighchartsDependencyError('anthropic is required to use Anthropic '
                                               'models, however it was not found in '
                                               'the runtime environment. Please '
                                               'install using "pip install anthropic"')
    api_key = api_key or os.getenv('ANTHROPIC_API_KEY', None)
    if not api_key:
        raise errors.HighchartsValueError('No API key was provided, and none '
                                          'was found in supported environment '
                                          'variables.')

    model = validators.string(model, allow_empty = False)
    model = model.lower()
    if model not in ['claude-instant-1', 'claude-2']:
        raise errors.HighchartsValueError(f'The model supplied is not supported. '
                                          f'Received: {model}.')

    anthropic = Anthropic(api_key = api_key)
    result = anthropic.completions.create(model = model,
                                          prompt = prompt,
                                          **kwargs)
    raw_response = result.completion

    starting_index = raw_response.find('<javascript>')
    ending_index = raw_response.rfind('</javascript>')

    if 'I cannot convert the Python code to JavaScript.' in raw_response:
        return errors.HighchartsPythonConversionError(
            f'Anthropic was unable to convert the '
            f'callable to a JavaScript function '
            f'using the "{model}" model. Please '
            f'try again, possibly selecting a '
            f'different model.'
        )
    elif starting_index == -1 or ending_index == -1:
        return errors.HighchartsPythonConversionError(
            f'Anthropic was unable to convert the '
            f'callable to a JavaScript function '
            f'using the "{model}" model. Please '
            f'try again, possibly selecting a '
            f'different model.'
        )

    js_as_str = raw_response[starting_index + 12:ending_index]

    return js_as_str
