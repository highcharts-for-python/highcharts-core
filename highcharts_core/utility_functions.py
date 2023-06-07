"""Collection of utility functions used across the library."""
import csv
import string
import random

from validator_collection import validators

from highcharts_core import errors


def get_random_string(length = 6):
    """Generate a short random alphanumeric string.
    
    :param length: The length of the string to generate. Defaults to ``8``.
    :type length: :class:`int <python:int>`
    
    :returns: A random alphanumeric string of length ``length``.
    :rtype: :class:`str <python:str>`
    """
    length = validators.integer(length, minimum = 1)
    result = ''.join(random.choices(string.ascii_uppercase + string.digits,
                                    k = length))

    return str(result)


def mro_to_dict(obj):
    """Work through ``obj``'s multiple parent classes, executing the appropriate
    ``to_dict()`` method for each parent and consolidaitng the results to a single
    :class:`dict <python:dict>`.

    :param obj: An object that has a ``to_dict()`` method.

    :rtype: :class:`dict <python:dict>`
    """
    if not hasattr(obj, 'to_dict'):
        raise TypeError('obj does not have a to_dict() method.')

    classes = [x for x in obj.__class__.mro()
               if x.__name__ != 'object']
    as_dict = {}

    for item in classes:
        has_to_dict = hasattr(super(item, obj), 'to_dict')
        if not has_to_dict:
            break

        try:
            item_dict = super(item, obj).to_dict()
        except (NotImplementedError, AttributeError):
            continue
        for key in item_dict:
            as_dict[key] = item_dict[key]

    return as_dict


def get_remaining_mro(cls,
                      in_cls = None,
                      method = '_to_untrimmed_dict'):
    """Retrieve the remaining classes that should be processed for ``method`` when
    traversing ``cls``.

    :param cls: The class whose ancestors are being traversed.
    :type cls: :class:`HighchartsMeta`

    :param in_cls: The class that the traversal currently finds itself in. Defaults to
      :obj:`None <python:None>`
    :type in_cls: ``type`` or :obj:`None <python:None>`

    :param method: The method to search for in the MRO. Defaults to
      ``'_to_untrimmed_dict'``.
    :type method: :class:`str <python:str>`

    :returns: List of classes that have ``method`` that occur *after* ``in_cls`` in
      the MRO for ``cls``.
    :rtype: :class:`list <python:list>` of ``type`` objects
    """
    mro = [x for x in cls.mro()
           if hasattr(x, method) and x.__name__ != 'HighchartsMeta']
    if in_cls is None:
        return mro[1:]
    else:
        index = mro.index(in_cls)
        return mro[(index + 1):]


def mro__to_untrimmed_dict(obj, in_cls = None):
    """Traverse the ancestor classes of ``obj`` and execute their ``_to_untrimmed_dict()``
    methods.

    :param obj: The object to be traversed.
    :type obj: :class:`HighchartsMeta`

    :param in_cls: The class from which ``mro__to_untrimmed_dict()`` was called.
    :type in_cls: ``type`` or :obj:`None <python:None>`

    :returns: Collection of untrimmed :class:`dict <python:dict>` representations in the
      same order as the MRO.
    :rtype: :class:`list <python:list>` of :class:`dict <python:dict>`

    for each class in the MRO, execute _to_untrimmed_dict()
    do not repeat for each class
    """
    cls = obj.__class__
    remaining_mro = get_remaining_mro(cls,
                                      in_cls = in_cls,
                                      method = '_to_untrimmed_dict')

    ancestor_dicts = []
    for x in remaining_mro:
        if hasattr(x, '_to_untrimmed_dict') and x != cls:
            ancestor_dicts.append(x._to_untrimmed_dict(obj,
                                                       in_cls = x))

    consolidated = {}
    for item in ancestor_dicts:
        for key in item:
            consolidated[key] = item[key]

    return consolidated


def validate_color(value):
    """Validate that ``value`` is either a :class:`Gradient`, :class:`Pattern`, or a
    :class:`str <python:str>`.

    :param value: The value to validate.

    :returns: The validated value.
    :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
      :obj:`None <python:None>`
    """
    from highcharts_core.utility_classes.gradients import Gradient
    from highcharts_core.utility_classes.patterns import Pattern

    if not value:
        return None
    elif value.__class__.__name__ == 'EnforcedNullType':
        return value
    elif isinstance(value, (Gradient, Pattern)):
        return value
    elif isinstance(value, (dict, str)) and ('linearGradient' in value or
                                             'radialGradient' in value):
        try:
            value = Gradient.from_json(value)
        except (TypeError, ValueError):
            if isinstance(value, dict):
                value = Gradient.from_dict(value)
            else:
                value = validators.string(value)
    elif isinstance(value, dict) and ('linear_gradient' in value or
                                      'radial_gradient' in value):
        value = Gradient(**value)
    elif isinstance(value, (dict, str)) and ('patternOptions' in value or
                                             'pattern' in value):
        try:
            value = Pattern.from_json(value)
        except (TypeError, ValueError):
            if isinstance(value, dict):
                value = Pattern.from_dict(value)
            else:
                value = validators.string(value)
    elif isinstance(value, dict) and 'pattern_options' in value:
        value = Pattern(**value)
    elif isinstance(value, str):
        value = validators.string(value)
    else:
        raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                          f'Gradient, or Pattern. Value received '
                                          f'was: {value}')

    return value


def to_camelCase(snake_case):
    """Convert ``snake_case`` to ``camelCase``.

    :param snake_case: A :class:`str <python:str>` which is likely to contain
      ``snake_case``.
    :type snake_case: :class:`str <python:str>`

    :returns: A ``camelCase`` representation of ``snake_case``.
    :rtype: :class:`str <python:str>`
    """
    snake_case = validators.string(snake_case)

    if '_' not in snake_case:
        return snake_case

    if 'url' in snake_case:
        snake_case = snake_case.replace('url', 'URL')
    elif 'utc' in snake_case:
        snake_case = snake_case.replace('utc', 'UTC')
    elif '_csv' in snake_case:
        snake_case = snake_case.replace('csv', 'CSV')
    elif '_jpeg' in snake_case:
        snake_case = snake_case.replace('jpeg', 'JPEG')
    elif '_pdf' in snake_case:
        snake_case = snake_case.replace('pdf', 'PDF')
    elif '_png' in snake_case:
        snake_case = snake_case.replace('png', 'PNG')
    elif '_svg' in snake_case:
        snake_case = snake_case.replace('svg', 'SVG')
    elif '_xls' in snake_case:
        snake_case = snake_case.replace('xls', 'XLS')
    elif '_atr' in snake_case:
        snake_case = snake_case.replace('atr', 'ATR')
    elif '_hlc' in snake_case:
        snake_case = snake_case.replace('hlc', 'HLC')
    elif '_ohlc' in snake_case:
        snake_case = snake_case.replace('ohlc', 'OHLC')
    elif '_xy' in snake_case:
        snake_case = snake_case.replace('xy', 'XY')
    elif snake_case.endswith('_x'):
        snake_case = snake_case.replace('_x', '_X')
    elif snake_case.endswith('_y'):
        snake_case = snake_case.replace('_y', '_Y')
    elif snake_case.endswith('_id'):
        snake_case = snake_case.replace('_id', '_ID')
    elif snake_case == 'drillup_text':
        snake_case = 'drillUpText'
    elif snake_case == 'drillup_button':
        snake_case = 'drillUpButton'
    elif snake_case == 'thousands_separator':
        snake_case = 'thousandsSep'
    elif snake_case == 'measure_xy':
        snake_case = 'measureXY'
    elif snake_case == 'use_gpu_translations':
        snake_case = 'useGPUTranslations'
    elif snake_case == 'label_rank':
        snake_case = 'labelrank'
    elif '_di_line' in snake_case:
        snake_case = snake_case.replace('_di_line', '_DILine')

    camel_case = ''
    previous_character = ''
    for character in snake_case:
        if character != '_' and previous_character != '_':
            camel_case += character
            previous_character = character
        elif character == '_':
            previous_character = character
        elif character != '_' and previous_character == '_':
            camel_case += character.upper()
            previous_character = character

    return camel_case


def parse_csv(csv_data,
              has_header_row = True,
              delimiter = ',',
              null_text = 'None',
              wrapper_character = "'",
              wrap_all_strings = False,
              double_wrapper_character_when_nested = False,
              escape_character = "\\",
              line_terminator = '\r\n'):
    """Parse ``csv_data`` to return a list of :class:`dict <python:dict>` objects, one
    for each record.

    :param csv_data: The CSV record expressed as a :class:`str <python:str>`
    :type csv_data: :class:`str <python:str>`

    :param delimiter: The delimiter used between columns. Defaults to ``,``.
    :type delimiter: :class:`str <python:str>`

    :param wrapper_character: The string used to wrap string values when
      wrapping is applied. Defaults to ``'``.
    :type wrapper_character: :class:`str <python:str>`

    :param null_text: The string used to indicate an empty value if empty
      values are wrapped. Defaults to `None`.
    :type null_text: :class:`str <python:str>`

    :returns: Collection of column names (or numerical keys) and CSV records as
      :class:`dict <python:dict>` values
    :rtype: :class:`tuple <python:tuple>` of a :class:`list <python:list>` of column names
      and :class:`list <python:list>` of :class:`dict <python:dict>`
    """
    if not csv_data:
        return [], []

    if isinstance(csv_data, str):
        csv_data = csv_data.split(line_terminator)

    if not wrapper_character:
        wrapper_character = "'"

    if wrap_all_strings:
        quoting = csv.QUOTE_NONNUMERIC
    else:
        quoting = csv.QUOTE_MINIMAL

    if 'highcharts' in csv.list_dialects():
        csv.unregister_dialect('highcharts')

    csv.register_dialect('highcharts',
                         delimiter = delimiter,
                         doublequote = double_wrapper_character_when_nested,
                         escapechar = escape_character,
                         quotechar = wrapper_character,
                         quoting = quoting,
                         lineterminator = line_terminator)

    if has_header_row:
        csv_reader = csv.DictReader(csv_data,
                                    dialect = 'highcharts',
                                    restkey = None,
                                    restval = None)
        records_as_dicts = [x for x in csv_reader]
        columns = csv_reader.fieldnames
    else:
        csv_reader = csv.reader(csv_data,
                                dialect = 'highcharts')
        records_as_dicts = []
        columns = []
        for row in csv_reader:
            record_as_dict = {}
            column_counter = 0
            for column in row:
                record_as_dict[column_counter] = column
                columns.append(column_counter)
                column_counter += 1

            records_as_dicts.append(record_as_dict)

    return columns, records_as_dicts


def jupyter_add_script(url, is_last = False):
    """Generates the JavaScript code Promise which adds a <script/> tag to the Jupyter 
    Lab environment.
    
    :param url: The URL to use for the script's source.
    :type url: :class:`str <python:str>`
    
    :param is_last: Whether the URL is the last of the promises.
    :type is_last: :class:`bool <python:bool>`
    
    :returns: The JavaScript code for adding the script.
    :rtype: :class:`str <python:str>`
    """
    url = validators.url(url)
    if url.endswith('.css'):
        return jupyter_add_link(url, is_last = is_last)
    
    js_str = """"""
    js_str += """new Promise(function(resolve, reject) {\n"""
    js_str += f"""  var existing_tags = document.querySelectorAll("script[src='{url}']");"""
    js_str += """  if (existing_tags.length == 0) {
        var script = document.createElement("script");
        script.onload = resolve;
        script.onerror = reject;"""
    js_str += f"""        script.src = '{url}';"""
    js_str += """        document.head.appendChild(script);
    };
})"""

    return js_str


def jupyter_add_link(url, is_last = False):
    """Generates the JavaScript code Promise which adds a <link/> tag to the Jupyter 
    Lab environment.
    
    :param url: The URL to use for the link's source.
    :type url: :class:`str <python:str>`
    
    :param is_last: Whether the URL is the last of the promises.
    :type is_last: :class:`bool <python:bool>`
    
    :returns: The JavaScript code for adding the link.
    :rtype: :class:`str <python:str>`
    """
    url = validators.url(url)
    
    js_str = ''
    js_str += """new Promise(function(resolve, reject) {\n"""
    js_str += f"""  var existing_tags = document.querySelectorAll("link[href='{url}']");"""
    js_str += """  if (existing_tags.length == 0) {
        var link = document.createElement("link");
        link.onload = resolve;
        link.onerror = reject;"""
    js_str += f"""        link.href = '{url}';"""
    js_str += f"""        link.rel = 'stylesheet';"""
    js_str += f"""        link.type = 'text/css';"""
    js_str += """        document.head.appendChild(link);
    };
})"""

    return js_str


def get_retryHighcharts():
    """Retrieve the ``retryHighcharts()`` JavaScript function.
    
    :returns: The JavaScript code of the ``retryHighcharts()`` JavaScript function.
    :rtype: :class:`str <python:str>`
    """
    js_str = """function retryHighcharts(fn, container = 'highcharts_target_div', retries = 5, retriesLeft = 5, 
        interval = 1000) {
            return new Promise((resolve, reject) => {
            try {
                fn()
                return resolve();
            } catch (err) {
                if ((err instanceof ReferenceError) || (err instanceof TypeError) || (err.message.includes('#17'))) {
                    if (retriesLeft === 0) {
                        var target_div = document.getElementById(container);
                        if (target_div) {
                            var timeElapsed = (retries * interval) / 1000;
                            var errorMessage = "Something went wrong with the Highcharts.js script. It should have been automatically loaded, but it did not load for over " + timeElapsed + " seconds. Check your internet connection, and then if the problem persists please reach out for support. (You can also check your browser's console log for more details.)<br/><br/>Detailed Error Message:<br/>" + err.message;
                            var errorHTML = "<p>" + errorMessage + "</p>";
                            target_div.innerHTML = errorMessage;
                            console.log(errorMessage);
                            console.error(err);
                        }
                        return reject();
                    }

                    setTimeout(() => {
                        retryHighcharts(fn, container, retries, retriesLeft - 1, interval).then(resolve).catch(reject);
                    }, interval);
                } else if ((err instanceof Error) && (err.message.includes('#13'))) {
                    var errorMessage = "It looks like the container specified \'" + container + "\' was not created successfully. Please check your browser\'s console log for more details.";
                    console.error(errorMessage);
                    console.error(err);
                    
                    return reject();
                } else {
                    throw err;
                }
            }
        });
    };"""
    
    return js_str


def prep_js_for_jupyter(js_str,
                        container = 'highcharts_target_div',
                        random_slug = None,
                        retries = 5,
                        interval = 1000):
    """Remove the JavaScript event listeners from the code in ``js_str`` and prepare the
    JavaScript code for rending in an IPython context.
    
    :param js_str: The JavaScript code from which the event listeners should be stripped.
    :type js_str: :class:`str <python:str>`
    
    :param container: The DIV where the Highcharts visualization is to be rendered. Defaults to
      ``'highcharts_target_div'``.
    :type container: :class:`str <python:str>`
    
    :param random_slug: The random sequence of characters to append to the container/function name to ensure uniqueness.
        Defaults to :obj:`None <python:None>`
    :type random_slug: :class:`str <python:str>` or :obj:`None <python:None>`

    :param retries: The number of times to retry the rendering. Defaults to 3.
    :type retries: :class:`int <python:int>`
    
    :param interval: The number of milliseconds to wait between retries. Defaults to 1000 (1 second).
    :type interval: :class:`int <python:int>`
    
    :returns: The JavaScript code having removed the non-Jupyter compliant JS code.
    :rtype: :class:`str <python:str>`
    """
    js_str = js_str.replace(
        """document.addEventListener('DOMContentLoaded', function() {""", '')
    js_str = js_str.replace('renderTo = ', '')
    js_str = js_str.replace(',\noptions = ', ',\n')
    js_str = js_str[:-3]

    if random_slug:
        function_str = f"""function insertChart_{random_slug}() """
    else:
        function_str = """function insertChart() """
    function_str += """{\n"""
    function_str += js_str
    function_str += """\n};\n"""
    if random_slug:
        function_str += f"""retryHighcharts(insertChart_{random_slug}, '{container}', {retries}, {retries}, {interval});"""
    else:
        function_str += f"""retryHighcharts(insertChart, '{container}', {retries}, {retries}, {interval});"""

    return function_str
