from typing import Optional
from decimal import Decimal

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
    if checkers.is_iterable(item):
        return [serialize_to_js_literal(x) for x in item]
    if checkers.is_string(item):
        return item
    elif checkers.is_numeric(item) and not isinstance(item, Decimal):
        return item
    elif isinstance(item, Decimal):
        return float(item)
    elif isinstance(item, constants.EnforcedNullType) or item == 'null':
        return constants.EnforcedNull
    elif item is None:
        return None
    elif item is True or item is False:
        return item
    elif checkers.is_type(item, ('CallbackFunction', dict)):
        return str(item)
    elif hasattr(item, 'to_js_literal'):
        return item.to_js_literal(encoding = encoding)

    return None


def is_js_function(as_str) -> bool:
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
            return False

    body = parsed.get('body', [])
    if not body:
        return False

    first_item = body[0]
    item_type = first_item.get('type', None)
    if item_type == 'FunctionDeclaration':
        return True
    elif as_str.startswith('function'):
        expression_item = f'const testName = {as_str}'
        try:
            parsed = esprima.parseScript(expression_item)
        except ParseError:
            try:
                parsed = esprima.parseModule(expression_item)
            except ParseError:
                return False

        body = parsed.get('body', [])
        if not body:
            return False

        first_item = body[0]
        first_item_type = first_item.get('type', None)
        if first_item_type != 'VariableDeclaration':
            return False

        init = first_item.get('init', None)
        if not init:
            return False
        init_type = init.get('type', None)
        if init_type in ('FunctionExpression', 'ArrowFunctionExpression'):
            return True
        elif init_type == 'NewExpression':
            callee = init.get('callee', None)
            if not callee:
                return False
            callee_name = callee.get('name', None)
            if callee_name == 'Function':
                return True

    return False


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
    for key in as_dict:
        key += 1
        item = as_dict[key]
        if item is None:
            continue

        as_str += f"""  {key}: """

        if checkers.is_string(item):
            if not is_js_function(item):
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

        if current_key < keys:
            as_str += ',\n'
        else:
            as_str += '\n'

    if not as_str:
        return None

    as_str = '{\n  ' + as_str + '}'

    return as_str


def convert_js_to_python(property_definition, original_str = None):
    """Convert a :class:`esprima.nodes.Property` object into a Python literal.

    .. note::

      The :class:`esprima.nodes.Property` objects are available in the ``value`` sub-item.

    """
    from highcharts.utility_classes.javascript_functions import CallbackFunction

    if not checkers.is_type(property_definition, 'Property'):
        raise errors.HighchartsParseError(f'property_definition should contain a '
                                          f'Property instance. Received: '
                                          f'{property_definition.__class__.__name__}')

    if property_definition.type == 'Literal':
        if property_definition.value is not None:
            return property_definition.value
        elif property_definition.raw == "'null'":
            return constants.EnforcedNull
        elif property_definition.name == 'undefined':
            return None
        else:
            raise errors.HighchartsParseError(f'unexpected parse error when '
                                              f'interpreting:\n{property_definition}')
    elif property_definition.type == 'ArrayExpression':
        return [convert_js_to_python(x, original_str)
                for x in property_definition.elements]
    elif property_definition.type == 'ObjectExpression':
        as_dict = {}
        key_value_pairs = get_key_value_pairs(property_definition.properties)
        for pair in key_value_pairs:
            as_dict[pair[0]] = pair[1]

        return as_dict
    elif property_definition.type == 'FunctionExpression':
        return CallbackFunction._convert_from_js_ast(property_definition, original_str)
    else:
        raise errors.HighchartsParseError('unable to find a literal, array, or object '
                                          'definition')


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
        key = item.key.name
        if not key:
            raise errors.HighchartsMissingKeyError('property was not formed correctly, '
                                                   'specifically missing a key')
        value = convert_js_to_python(item.value, original_str)
        pair = (key, value)
        key_value_pairs.append(pair)

    return key_value_pairs
