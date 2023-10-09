import datetime
import string
from typing import Optional
from decimal import Decimal
from collections import UserDict

from validator_collection import checkers, validators
import esprima
from esprima.error_handler import Error as ParseError

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    
from highcharts_core import constants, errors, utility_functions


def serialize_to_js_literal(item, 
                            encoding = 'utf-8', 
                            ignore_to_array = False,
                            careful_validation = False) -> Optional[str]:
    """Convert ``item`` to the contents of a JavaScript object literal code snippet.

    :param item: A value that is to be converted into a JS object literal notation value.

    :param encoding: The character encoding to apply to the resulting object. Defaults
      to ``'utf-8'``.
    :type encoding: :class:`str <python:str>`
    
    :param ignore_to_array: If ``True``, will ignore handling of the ``.to_array()`` method
      to break recursion. Defaults to ``False``.
    :type ignore_to_array: :class:`bool <python:bool>`

    :param careful_validation: if ``True``, will carefully validate JavaScript values
      along the way using the
      `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
      to ``False``.
      
      .. warning::
      
        Setting this value to ``True`` will significantly degrade serialization
        performance, though it may prove useful for debugging purposes.

    :type careful_validation: :class:`bool <python:bool>`

    :returns: A JavaScript object literal code snippet, expressed as a string. Or
      :obj:`None <python:None>` if ``item`` is not serializable.
    :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
    """
    if not ignore_to_array and hasattr(item, 'to_array'):
        requires_js_objects = getattr(item, 'requires_js_object', True)
        if requires_js_objects and hasattr(item, 'to_js_literal'):
            return item.to_js_literal(encoding = encoding,
                                      careful_validation = careful_validation)
        elif requires_js_objects:
            return serialize_to_js_literal(item, 
                                           encoding = encoding, 
                                           ignore_to_array = True,
                                           careful_validation = careful_validation)
        else:
            return serialize_to_js_literal(item.to_array(), 
                                           encoding = encoding,
                                           careful_validation = careful_validation)
    elif HAS_NUMPY and utility_functions.is_ndarray(item):
        return utility_functions.from_ndarray(item)
    elif hasattr(item, 'to_js_literal'):
        return item.to_js_literal(encoding = encoding, 
                                  careful_validation = careful_validation)
    elif not isinstance(item,
                        (str, bytes, dict, UserDict)) and hasattr(item, '__iter__'):
        requires_js_objects = False
        for x in item:
            try:
                if getattr(x, 'requires_js_object', True) is True:
                    requires_js_objects = True
                    break
            except ValueError as error:
                if utility_functions.is_ndarray(x):
                    continue
                else:
                    raise error
        if requires_js_objects:
            return [serialize_to_js_literal(x,
                                            encoding = encoding,
                                            ignore_to_array = True,
                                            careful_validation = careful_validation)
                    for x in item]
        else:
            result = []
            for x in item:
                if not utility_functions.is_ndarray(x):
                    js_literal = serialize_to_js_literal(x.to_array(),
                                                         encoding = encoding,
                                                         careful_validation = careful_validation)
                    result.append(js_literal)
                else:
                    result.append(utility_functions.from_ndarray(x))
            
            return result
    elif isinstance(item, constants.EnforcedNullType) or item == 'null':
        return constants.EnforcedNull
    elif isinstance(item, bool):
        return item
    elif isinstance(item, str):
        return_value = item.replace("'", "\\'")
        return return_value
    elif checkers.is_numeric(item) and not isinstance(item, Decimal):
        return item
    elif isinstance(item, Decimal):
        return float(item)
    elif checkers.is_type(item, ('CallbackFunction')):
        return str(item)
    elif isinstance(item, (dict, UserDict)):
        as_dict = {}
        for key in item:
            as_dict[key] = serialize_to_js_literal(item[key], 
                                                   encoding = encoding,
                                                   careful_validation = careful_validation)
        return str(as_dict)
    elif checkers.is_datetime(item):
        if not item.tzinfo:
            item = item.replace(tzinfo = datetime.timezone.utc)
        return item.timestamp() * 1000
    elif checkers.is_date(item):
        return f'Date.UTC({item.year}, {item.month - 1}, {item.day})'
    elif checkers.is_time(item):
        return item.isoformat()
    elif item is None:
        return None

    return None


def is_js_object(as_str, careful_validation = False):
    """Determine whether ``as_str`` is a JavaScript object.
    
    :param as_str: The string to evaluate.
    :type as_str: :class:`str <python:str>`
    
    :param careful_validation: if ``True``, will carefully validate JavaScript values
      along the way using the
      `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
      to ``False``.
      
      .. warning::
      
        Setting this value to ``True`` will significantly degrade serialization
        performance, though it may prove useful for debugging purposes.

    :type careful_validation: :class:`bool <python:bool>`

    :returns: ``True`` if ``as_str`` is a JavaScript function. ``False`` if not.
    :rtype: :class:`bool <python:bool>`
    """

    if not careful_validation:
        is_empty = as_str[1:-1].strip() == ''
        if is_empty:
            return True
        has_colon = ':' in as_str
        if has_colon:
            return True
        if 'new ' in as_str:
            return True
        if 'Object.create(' in as_str:
            return True
        return False
    else:
        expression_item = f'const testName = {as_str}'
        try:
            parsed = esprima.parseScript(expression_item)
        except ParseError:
            try:
                parsed = esprima.parseModule(expression_item)
            except ParseError:
                return False

        body = parsed.body
        if not body:
            return False

        first_item = body[0]
        if first_item.type != 'VariableDeclaration':
            return False

        init = first_item.declarations[0].init
        if not init:
            return False
        if init.type in ('ObjectExpression'):
            return True

        return False


def attempt_variable_declaration(as_str):
    """Attempt to coerce ``as_str`` to a JavaScript variable declaration form.

    :param as_str: The string to evaluate.
    :type as_str: :class:`str <python:str>`

    :returns: ``True`` if ``as_str`` is a JavaScript function. ``False`` if not.
    :rtype: :class:`bool <python:bool>`
    """
    expression_item = f'const testName = {as_str}'
    try:
        parsed = esprima.parseScript(expression_item)
    except ParseError:
        try:
            parsed = esprima.parseModule(expression_item)
        except ParseError:
            return False

    body = parsed.body
    if not body:
        return False

    first_item = body[0]
    if first_item.type != 'VariableDeclaration':
        return False

    init = first_item.declarations[0].init
    if not init:
        return False
    if init.type in ('FunctionExpression', 'ArrowFunctionExpression', 'ClassExpression'):
        return True
    elif init.type == 'NewExpression':
        callee = init.callee
        if not callee:
            return False
        if callee.name == 'Function':
            return True

    return False


def is_js_function_or_class(as_str, careful_validation = False) -> bool:
    """Determine whether ``as_str`` is a JavaScript function or not.

    :param as_str: The string to evaluate.
    :type as_str: :class:`str <python:str>`

    :param careful_validation: if ``True``, will carefully validate JavaScript values
      along the way using the
      `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
      to ``False``.
      
      .. warning::
      
        Setting this value to ``True`` will significantly degrade serialization
        performance, though it may prove useful for debugging purposes.

    :type careful_validation: :class:`bool <python:bool>`

    :returns: ``True`` if ``as_str`` is a JavaScript function. ``False`` if not.
    :rtype: :class:`bool <python:bool>`
    """
    if not isinstance(as_str, str):
        return False
    if not careful_validation:
        is_function = as_str.startswith('function ') or as_str.startswith('function*')
        if is_function:
            return True

        is_function = 'function(' in as_str or 'function*(' in as_str
        if is_function:
            return True

        is_function = ')=>' in as_str or ') =>' in as_str

        if is_function:
            return True

        is_function = 'new Function(' in as_str
        if is_function:
            return True
        
        is_class = as_str.startswith('class ')
        if is_class:
            return True        
        
        is_class = 'class {' in as_str or 'class{' in as_str
        if is_class:
            return True
        
        is_class = '= class' in as_str or '=class' in as_str
        if is_class:
            return True
        
        return False
    else:
        try:
            parsed = esprima.parseScript(as_str)
        except ParseError:
            try:
                parsed = esprima.parseModule(as_str)
            except ParseError:
                if as_str.startswith('function') is False:
                    return False
                else:
                    return attempt_variable_declaration(as_str)

        body = parsed.body
        if not body:
            return False

        first_item = body[0]
        if first_item.type in ('FunctionDeclaration', 'ClassDeclaration'):
            return True
        elif as_str.startswith('function') or as_str.startswith('class'):
            return attempt_variable_declaration(as_str)
        elif first_item.type == 'VariableDeclaration':
            init = first_item.declarations[0].init
            if not init:
                return False
            if init.type in ('FunctionExpression', 'ArrowFunctionExpression',
                            'ClassExpression'):
                return True
            elif init.type == 'NewExpression':
                callee = init.callee
                if not callee:
                    return False
                if callee.name == 'Function':
                    return True

    return False


def get_js_literal(item, careful_validation = False) -> str:
    """Convert the value of ``item`` into a JavaScript literal string.

    :param careful_validation: if ``True``, will carefully validate JavaScript values
      along the way using the
      `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
      to ``False``.
      
      .. warning::
      
        Setting this value to ``True`` will significantly degrade serialization
        performance, though it may prove useful for debugging purposes.

    :type careful_validation: :class:`bool <python:bool>`

    :returns: The JavaScript literal string.
    :rtype: :class:`str <python:str>`
    """
    as_str = ''
    if not isinstance(item, (str, bytes, dict, UserDict)) and hasattr(item, '__iter__'):
        subitems = [get_js_literal(x) for x in item]
        as_str += '['
        subitem_counter = 0
        for subitem in subitems:
            subitem_counter += 1
            if subitem == 'None':
                subitem = 'null'
            as_str += f"""{subitem}"""
            if subitem_counter < len(subitems):
                as_str += ',\n'
        as_str += ']'
    elif isinstance(item, str):
        if (item.startswith('[') or item.startswith('Date')) and item != 'Date':
            as_str += f"""{item}"""
        elif item.startswith('{') and item.endswith('}'):
            if is_js_object(item, careful_validation = careful_validation):
                as_str += f"""{item}"""
            elif "'" in item:
                item = item.replace("'", "\\'")
                as_str += f'"{item}"'
            else:
                as_str += f"'{item}'"
        elif item in string.whitespace:
            as_str += f"""`{item}`"""
        elif item.startswith == 'HCP: REPLACE-WITH-':
            item_str = item.replace('HCP: REPLACE-WITH-', '')
            as_str += f"""{item_str}"""
        elif not is_js_function_or_class(item, careful_validation = careful_validation):
            as_str += f"""'{item}'"""
        else:
            as_str += f"""{item}"""
    elif item == constants.EnforcedNull:
        as_str += """null"""
    elif item is True:
        as_str += """true"""
    elif item is False:
        as_str += """false"""
    else:
        as_str += f"""{item}"""

    return as_str


def assemble_js_literal(as_dict, 
                        keys_as_strings = False,
                        careful_validation = False) -> Optional[str]:
    """Convert ``as_dict`` into a JavaScript object literal string.

    :param as_dict: A :class:`dict <python:dict>` representation of the JavaScript object.
    :type as_dict: :class:`dict <pythoN:dict>`

    :param keys_as_strings: if ``True``, will return the keys as string values (wrapped
      in quotation marks). If ``False``, will return the keys as object literals. Defaults
      to ``False``.
    :type keys_as_strings: :class:`bool <python:bool>`

    :param careful_validation: if ``True``, will carefully validate JavaScript values
      along the way using the
      `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
      to ``False``.
      
      .. warning::
      
        Setting this value to ``True`` will significantly degrade serialization
        performance, though it may prove useful for debugging purposes.

    :type careful_validation: :class:`bool <python:bool>`

    :returns: The JavaScript object literal representation of ``as_dict``.
    :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
    """
    if careful_validation:
        as_dict = validators.dict(as_dict, allow_empty = True)

    if not as_dict:
        return None

    as_str = ''
    keys = len(as_dict)
    current_key = 0
    ended_on_None = False

    for key in as_dict:
        current_key += 1
        item = as_dict[key]
        if item is None:
            keys -= 1
            ended_on_None = True
            continue

        if keys_as_strings:
            as_str += f"""  '{key}': """
        else:
            as_str += f"""  {key}: """

        as_str += get_js_literal(item, careful_validation = careful_validation)

        if current_key < keys:
            as_str += ',\n'
        else:
            ended_on_None = False
            as_str += '\n'

    if not as_str:
        return None
    elif ended_on_None:
        as_str = as_str[:-2]
        as_str += '\n'

    as_str = '{\n' + as_str + '}'

    return as_str


def convert_js_literal_to_python(literal_definition, original_str: None):
    """Convert a :class:`esprima.nodes.Literal` object into a Python literal.

    .. note::

      The :class:`esprima.nodes.Property` objects are available in the ``value`` sub-item.

    :rtype: Python objcet
    """
    if not checkers.is_type(literal_definition, ('Literal', 'Identifier')):
        raise errors.HighchartsParseError(f'literal_definition should contain a '
                                          f'Literal or Identifier instance. Received: '
                                          f'{literal_definition.__class__.__name__}')

    if literal_definition.raw == 'null':
        return constants.EnforcedNull
    elif literal_definition.name == 'undefined':
        return None
    elif literal_definition.value is not None:
        return literal_definition.value
    else:
        raise errors.HighchartsParseError('unable to find a literal, array, or object '
                                          'definition')


def convert_js_property_to_python(property_definition, original_str = None):
    """Convert a :class:`esprima.nodes.Property` object into a Python literal.

    .. note::

      The :class:`esprima.nodes.Property` objects are available in the ``value`` sub-item.

    """
    from highcharts_core.utility_classes.javascript_functions import CallbackFunction, \
        JavaScriptClass

    if not checkers.is_type(property_definition, 'Property'):
        raise errors.HighchartsParseError(f'property_definition should contain a '
                                          f'Property instance. Received: '
                                          f'{property_definition.__class__.__name__}')

    if property_definition.value.type == 'Literal':
        if property_definition.value.raw == 'null':
            return constants.EnforcedNull
        elif property_definition.value.name == 'undefined':
            return None
        elif property_definition.value is not None:
            return property_definition.value.value
        else:
            raise errors.HighchartsParseError(f'unexpected parse error when '
                                              f'interpreting:\n{property_definition}')
    elif property_definition.value.type == 'TemplateLiteral':
        template_elements = property_definition.value.quasis
        if template_elements:
            element = template_elements[0]
            if element.type == 'TemplateElement':
                return element.value.cooked
            else:
                raise errors.HighchartsParseError('unable to properly parse a '
                                                  'TemplateLiteral. Specifically could '
                                                  'not find a TemplateElement where one '
                                                  'was expected.')
    elif property_definition.value.type == 'UnaryExpression':
        property_value = property_definition.value
        operator = property_value.operator
        if operator == '-':
            multiple = -1
        else:
            multiple = 1
        argument_type = property_value.argument.type
        if argument_type not in ['Literal']:
            raise errors.HighchartsParseError(f'unable to find a Literal value within'
                                              f'a Unary expression. Found: '
                                              f'{argument_type}')
        value = property_value.argument.value
        if checkers.is_numeric(value):
            return value * multiple
        else:
            return value

    elif property_definition.value.type == 'Identifier':
        if property_definition.value.name == 'undefined':
            return None
        else:
            raise errors.HighchartsParseError(f'unexpected parse error when '
                                              f'interpreting:\n{property_definition}')
    elif property_definition.value.type == 'ArrayExpression':
        return [convert_js_to_python(x, original_str)
                for x in property_definition.value.elements]
    elif property_definition.value.type == 'ObjectExpression':
        as_dict = {}
        key_value_pairs = get_key_value_pairs(property_definition.value.properties,
                                              original_str)
        for pair in key_value_pairs:
            as_dict[pair[0]] = pair[1]

        return as_dict
    elif property_definition.value.type == 'FunctionExpression':
        return CallbackFunction._convert_from_js_ast(property_definition, original_str)
    elif property_definition.value.type == 'ClassExpression':
        return JavaScriptClass._convert_from_js_ast(property_definition.value,
                                                    original_str)
    elif property_definition.value.type == 'CallExpression':
        expression = property_definition.value
        try:
            callee_obj = expression.callee.object.name
        except AttributeError:
            try:
                callee_obj = expression.callee.name
            except AttributeError:
                raise errors.HighchartsParseError('unable to parse the JS Call '
                                                  'Expression')
        call_arguments = [x.value for x in expression.arguments]
        if callee_obj == 'Date':
            if len(call_arguments) == 1:
                return validators.datetime(call_arguments[0])
            elif len(call_arguments) == 2:
                return datetime.date(year = call_arguments[0],
                                     month = call_arguments[1] + 1)
            elif len(call_arguments) == 3:
                return datetime.date(year = call_arguments[0],
                                     month = call_arguments[1] + 1,
                                     day = call_arguments[2])
            elif len(call_arguments) == 4:
                return datetime.datetime(year = call_arguments[0],
                                         month = call_arguments[1] + 1,
                                         day = call_arguments[2],
                                         hour = call_arguments[3])
            elif len(call_arguments) == 5:
                return datetime.datetime(year = call_arguments[0],
                                         month = call_arguments[1] + 1,
                                         day = call_arguments[2],
                                         hour = call_arguments[3],
                                         minute = call_arguments[4])
            elif len(call_arguments) == 6:
                return datetime.datetime(year = call_arguments[0],
                                         month = call_arguments[1] + 1,
                                         day = call_arguments[2],
                                         hour = call_arguments[3],
                                         minute = call_arguments[4],
                                         second = call_arguments[5])
            elif len(call_arguments) == 7:
                return datetime.datetime(year = call_arguments[0],
                                         month = call_arguments[1] + 1,
                                         day = call_arguments[2],
                                         hour = call_arguments[3],
                                         minute = call_arguments[4],
                                         second = call_arguments[5],
                                         microsecond = call_arguments[6])
            else:
                raise errors.HighchartsParseError('failed to parse the Date() '
                                                  'constructor from the JS literal')

    else:
        raise errors.HighchartsParseError('unable to find a literal, array, or object '
                                          'definition')


def convert_js_to_python(javascript, original_str = None):
    """Convert a :class:`esprima.nodes.Property` object into a Python literal.

    .. note::

      The :class:`esprima.nodes.Property` objects are available in the ``value`` sub-item.

    """
    if javascript.type not in ('Property',
                               'Literal',
                               'ObjectExpression',
                               'ArrayExpression',
                               'UnaryExpression',
                               'FunctionExpression'):
        raise errors.HighchartsParseError(f'javascript should contain a '
                                          f'Property, Literal, ObjectExpression, '
                                          f'ArrayExpression, UnaryExpression, or '
                                          f'FunctionExpression instance. Received: '
                                          f'{javascript.type}')

    if checkers.is_type(javascript, 'Property'):
        return convert_js_property_to_python(javascript, original_str)
    elif checkers.is_type(javascript, 'ObjectExpression'):
        as_dict = {}
        key_value_pairs = get_key_value_pairs(javascript.properties, original_str)
        for pair in key_value_pairs:
            as_dict[pair[0]] = pair[1]

        return as_dict
    elif checkers.is_type(javascript, 'ArrayExpression'):
        return [convert_js_to_python(x, original_str)
                for x in javascript.elements]
    elif checkers.is_type(javascript, 'UnaryExpression'):
        is_negative = javascript.operator == '-'
        if is_negative:
            multiple = -1
        converted_value = convert_js_literal_to_python(javascript.argument, original_str)
        return converted_value * multiple
    elif checkers.is_type(javascript, 'FunctionExpression'):
        from highcharts_core.utility_classes.javascript_functions import CallbackFunction

        start_char = javascript.range[0]
        end_char = javascript.range[1]
        function_as_str = original_str[start_char:end_char]
        return CallbackFunction.from_js_literal(function_as_str)
    else:
        return convert_js_literal_to_python(javascript, original_str)


def get_key_value_pairs(properties, original_str):
    """Return the key and value pairs for properties defined in ``properties``.

    :param properties: The definition of a JavaScript object Property.
    :type properties: :class:`list <python:list>` of :class:`esprima.nodes.Property`
      instances

    :rtype: :class:`list <python:list>` of :class:`tuples <python:tuple>` of
      :class:`str <python:str>` and any value
    """
    key_value_pairs = []
    for item in properties:
        if not checkers.is_type(item, 'Property'):
            raise errors.HighchartsParseError(f'properties should contain a list of '
                                              f'Property instances. Received: '
                                              f'{item.__class__.__name__}')
        key = item.key.name or item.key.value
        if not key:
            raise errors.HighchartsMissingKeyError('property was not formed correctly, '
                                                   'specifically missing a key')
        value = convert_js_to_python(item, original_str)
        pair = (key, value)
        key_value_pairs.append(pair)

    return key_value_pairs
