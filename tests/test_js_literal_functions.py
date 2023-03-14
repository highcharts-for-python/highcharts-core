"""Unit tests for ``highcharts.js_literal_functions``."""

import pytest

from highcharts_core import js_literal_functions as js
from highcharts_core import constants, errors

from decimal import Decimal

import esprima
from validator_collection import checkers


@pytest.mark.parametrize('item, expected_type, expected_value, error', [
    (123, int, 123, None),
    ('this-is-a-string', str, 'this-is-a-string', None),
    (123.45, float, 123.45, None),
    (Decimal(123.45), float, 123.45, None),
    (True, bool, True, None),
    (False, bool, False, None),
    ([1, 2, 3], list, [1, 2, 3], None),
    ('null', constants.EnforcedNullType, constants.EnforcedNull, None),
    (constants.EnforcedNull, constants.EnforcedNullType, constants.EnforcedNull, None),
    (None, type(None), None, None),
    ({'test': 123}, str, str({'test': 123}), None),
])
def test_serialize_to_js_literal(item, expected_type, expected_value, error):
    if not error:
        result = js.serialize_to_js_literal(item)

        assert isinstance(result, expected_type)
        assert result == expected_value
    else:
        with pytest.raises(error):
            result = js.serialize_to_js_literal(item)


@pytest.mark.parametrize('as_str, expected, error', [
    ("""function testFunction() { return True; };""", True, None),
    ("""function() { return True; }""", True, None),
    ("""const testFunction = function() { return True; }""", True, None),
    ("""const testFunction = () => { return True; }""", True, None),
    ("""const testFunction = new Function('return True;')""", True, None),

    ("""class TestClass { constructor() { return true; }};""", True, None),
    ("""let a = 123;""", False, None),
])
def test_is_js_function_or_class(as_str, expected, error):
    if not error:
        is_function = js.is_js_function_or_class(as_str)

        assert is_function is expected
    else:
        with pytest.raises(error):
            is_function = js.is_js_function_or_class(as_str)


@pytest.mark.parametrize('as_str, expected, error', [
    ("""function testFunction() { return True; };""", True, None),
    ("""function() { return True; }""", True, None),
    ("""const testFunction = function() { return True; }""", False, None),
    ("""const testFunction = () => { return True; }""", False, None),
    ("""const testFunction = new Function('return True;')""", False, None),
    ("""let a = 123;""", False, None),
])
def test_attempt_variable_declaration(as_str, expected, error):
    if not error:
        is_function = js.attempt_variable_declaration(as_str)

        assert is_function is expected
    else:
        with pytest.raises(error):
            is_function = js.attempt_variable_declaration(as_str)


@pytest.mark.parametrize('as_dict, expected, error', [
    (None, None, None),
    ({'item1': 123}, """{\n  item1: 123\n}""", None),
    ({'item1': 123, 'item2': 456}, """{\n  item1: 123,\n  item2: 456\n}""", None),
    ({'item1': True}, """{\n  item1: true\n}""", None),
    ({'item1': False}, """{\n  item1: false\n}""", None),
    ({'item1': constants.EnforcedNull}, """{\n  item1: null\n}""", None),
    ({'item1': 'test string'}, """{\n  item1: 'test string'\n}""", None),
    ({'item1': 'function() { return True; }'},
     """{\n  item1: function() { return True; }\n}""", None),
    ({'item1': 123, 'item2': None}, """{\n  item1: 123\n}""", None),
    ({}, None, None),
    ('not-a-dict', None, TypeError),
])
def test_assemble_js_literal(as_dict, expected, error):
    if not error:
        result = js.assemble_js_literal(as_dict)
        assert result == expected
    else:
        with pytest.raises(error):
            result = js.assemble_js_literal(as_dict)


@pytest.mark.parametrize('original_str, override, expected, error', [
    ("""const testObject = {item1:123,item2:456}""", None, [('item1', 123),('item2',456)], None),
    ("""const testObj = {item1:true}""", None, [('item1',True)], None),
    ("""const testObj = {item1:undefined}""", None, [('item1',None)], None),
    ("""const testObj = {item1:null}""", None, [('item1',constants.EnforcedNull)], None),
    ("""const testObj = {item1:[1, 2, 3]}""", None, [('item1', [1, 2, 3])], None),
    ("""const testObj = {item1:{subitem:123}}""", None, [('item1',{'subitem':123})], None),
])
def test_get_key_value_pairs(original_str, override, expected, error):
    if not override:
        parsed = esprima.parseScript(original_str)
        properties = parsed.body[0].declarations[0].init.properties
    else:
        properties = override

    if not error:
        result = js.get_key_value_pairs(properties, original_str)
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == len(properties)
        counter = 0
        for item in result:
            assert isinstance(item, tuple)
            assert len(item) == 2
            assert item[0] == expected[counter][0]
            assert item[1] == expected[counter][1]
            if isinstance(item[1], dict):
                assert checkers.are_dicts_equivalent(item[1],
                                                     expected[counter][1]) is True
            counter += 1
        assert result == expected
    else:
        with pytest.raises(error):
            result = js.get_key_value_pairs(properties, original_str)


@pytest.mark.parametrize('original_str, override, expected, error', [
    ("""const testObj = {item1:true}""", None, True, None),
    ("""const testObj = {item1:false}""", None, False, None),
    ("""const testObj = {item1:123}""", None, 123, None),
    ("""const testObj = {item1:'test string'}""", None, 'test string', None),
    ("""const testObj = {item1:undefined}""", None, None, None),
    ("""const testObj = {item1:null}""", None, constants.EnforcedNull, None),

    ('', 'not-a-literal', None, errors.HighchartsParseError),
])
def test_convert_js_literal_to_python(original_str, override, expected, error):
    if not override:
        parsed = esprima.parseScript(original_str)
        literal = parsed.body[0].declarations[0].init.properties[0].value
    else:
        literal = override

    if not error:
        result = js.convert_js_literal_to_python(literal, original_str)
        if expected is not None:
            assert result is not None
            assert result == expected
        else:
            assert result is None
    else:
        with pytest.raises(error):
            result = js.convert_js_literal_to_python(literal, original_str)


@pytest.mark.parametrize('original_str, override, expected, error', [
    ("""const testObj = {item1:true}""", None, True, None),
    ("""const testObj = {item1:false}""", None, False, None),
    ("""const testObj = {item1:123}""", None, 123, None),
    ("""const testObj = {item1:'test string'}""", None, 'test string', None),
    ("""const testObj = {item1:undefined}""", None, None, None),
    ("""const testObj = {item1:null}""", None, constants.EnforcedNull, None),
    ("""const testObj = {item1:[1,2]}""", None, [1,2], None),
    ("""const testObj = {item1:{subitem:'test'}}""", None, {'subitem': 'test'}, None),

    ('', 'not-a-property', None, errors.HighchartsParseError),
])
def test_convert_js_property_to_python(original_str, override, expected, error):
    if not override:
        parsed = esprima.parseScript(original_str)
        item = parsed.body[0].declarations[0].init.properties[0]
    else:
        item = override

    if not error:
        result = js.convert_js_property_to_python(item, original_str)
        if expected is not None:
            assert result is not None
            assert result == expected
        else:
            assert result is None
    else:
        with pytest.raises(error):
            result = js.convert_js_property_to_python(item, original_str)
