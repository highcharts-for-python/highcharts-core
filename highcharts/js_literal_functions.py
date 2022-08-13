from typing import Optional
from decimal import Decimal
from collections import UserDict

from validator_collection import checkers, validators
import esprima
from esprima.error_handler import Error as ParseError

from highcharts import constants, errors


def serialize_to_js_literal(item, encoding = 'utf-8') -> Optional[str]:
    """Convert ``item`` to the contents of a JavaScript object literal code snippet.

    :param item: A value that is to be converted into a JS object literal notation value.

    :param encoding: The character encoding to apply to the resulting object. Defaults
      to ``'utf-8'``.
    :type encoding: :class:`str <python:str>`

    :returns: A JavaScript object literal code snippet, expressed as a string. Or
      :obj:`None <python:None>` if ``item`` is not serializable.
    :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
    """
    if checkers.is_iterable(item, forbid_literals = (str, bytes, dict, UserDict)):
        return [serialize_to_js_literal(x) for x in item]
    elif hasattr(item, 'to_js_literal'):
        return item.to_js_literal(encoding = encoding)
    elif isinstance(item, constants.EnforcedNullType) or item == 'null':
        return constants.EnforcedNull
    elif isinstance(item, bool):
        return item
    elif checkers.is_string(item):
        return item
    elif checkers.is_numeric(item) and not isinstance(item, Decimal):
        return item
    elif isinstance(item, Decimal):
        return float(item)
    elif checkers.is_type(item, ('CallbackFunction', dict, UserDict)):
        return str(item)
    elif item is None:
        return None

    return None


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


def is_js_function_or_class(as_str) -> bool:
    """Determine whether ``as_str`` is a JavaScript function or not.

    :param as_str: The string to evaluate.
    :type as_str: :class:`str <python:str>`

    :returns: ``True`` if ``as_str`` is a JavaScript function. ``False`` if not.
    :rtype: :class:`bool <python:bool>`
    """
    if not checkers.is_string(as_str):
        return False

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


def get_js_literal(item) -> str:
    """Convert the value of ``item`` into a JavaScript literal string.

    :returns: The JavaScript literal string.
    :rtype: :class:`str <python:str>`
    """
    as_str = ''
    if checkers.is_iterable(item, forbid_literals = (str, bytes, dict, UserDict)):
        subitems = [get_js_literal(x) for x in item]
        as_str += '['
        subitem_counter = 0
        for subitem in subitems:
            subitem_counter += 1
            as_str += f"""{subitem}"""
            if subitem_counter < len(subitems):
                as_str += ',\n'
        as_str += ']'
    elif checkers.is_string(item):
        if item.startswith('{') or item.startswith('['):
            as_str += f"""{item}"""
        elif not is_js_function_or_class(item):
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


def assemble_js_literal(as_dict) -> Optional[str]:
    """Convert ``as_dict`` into a JavaScript object literal string.

    :param as_dict: A :class:`dict <python:dict>` representation of the JavaScript object.
    :type as_dict: :class:`dict <pythoN:dict>`

    :returns: The JavaScript object literal representation of ``as_dict``.
    :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
    """
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

        as_str += f"""  {key}: """

        as_str += get_js_literal(item)

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
    from highcharts.utility_classes.javascript_functions import CallbackFunction, \
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
    else:
        raise errors.HighchartsParseError('unable to find a literal, array, or object '
                                          'definition')


def convert_js_to_python(javascript, original_str = None):
    """Convert a :class:`esprima.nodes.Property` object into a Python literal.

    .. note::

      The :class:`esprima.nodes.Property` objects are available in the ``value`` sub-item.

    """
    if javascript.type not in ('Property', 'Literal', 'ObjectExpression'):
        raise errors.HighchartsParseError(f'javascript should contain a '
                                          f'Property, Literal, or ObjectExpression '
                                          f'instance. Received: {javascript.type}')

    if checkers.is_type(javascript, 'Property'):
        return convert_js_property_to_python(javascript, original_str)
    elif checkers.is_type(javascript, 'ObjectExpression'):
        as_dict = {}
        key_value_pairs = get_key_value_pairs(javascript.properties, original_str)
        for pair in key_value_pairs:
            as_dict[pair[0]] = pair[1]

        return as_dict
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
