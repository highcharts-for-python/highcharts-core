"""Unit tests for ``highcharts.utility_classes.javascript_functions``."""

import pytest

import os

from validator_collection import checkers
import esprima
from esprima.error_handler import Error as ParseError

from highcharts_core.utility_classes import javascript_functions as js_f
from highcharts_core import errors


def validate_js_function(as_str, _break_loop_on_failure = False, range = True):
    """Parse ``as_str`` as a valid JavaScript function.

    :param as_str: A putative JavaScript function definition
    :type as_str: :class:`str <python:str>`

    :returns: The Esprima AST, and a boolean flag to indicate whether it was prefixed
    :rtype: :class:`tuple <python:tuple>` of :class:`esprima.nodes.Script`,
      :class:`bool <python:bool>`
    """
    try:
        parsed = esprima.parseScript(as_str, loc = range, range = range)
    except ParseError:
        try:
            parsed = esprima.parseModule(as_str, loc = range, range = range)
        except ParseError as error:
            if not _break_loop_on_failure:
                as_str = f"""const testFunction = {as_str}"""
                return validate_js_function(as_str,
                                            _break_loop_on_failure = True,
                                            range = range)
            else:
                raise error

    return parsed, as_str


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'function_name': 'testFunction',
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, None),
    ({
        'function_name': 123
    }, TypeError),
    ({
        'arguments': 'not-a-list'
    }, TypeError),
    ({
        'body': 123
    }, TypeError),
])
def test_CallbackFunction__init__(kwargs, error):
    if not error:
        result = js_f.CallbackFunction(**kwargs)
        assert result is not None
        assert isinstance(result, js_f.CallbackFunction) is True
        for key in kwargs:
            assert kwargs[key] == getattr(result, key)

    else:
        with pytest.raises(error):
            result = js_f.CallbackFunction(**kwargs)


@pytest.mark.parametrize('as_dict, error', [
    ({}, None),
    ({
        'function_name': 'testFunction',
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, None),
    ({
        'function_name': 123
    }, TypeError),
    ({
        'arguments': 'not-a-list'
    }, TypeError),
    ({
        'body': 123
    }, TypeError),
])
def test_CallbackFunction_from_dict(as_dict, error):
    if not error:
        result = js_f.CallbackFunction.from_dict(as_dict)
        assert result is not None
        assert isinstance(result, js_f.CallbackFunction) is True
        for key in as_dict:
            assert as_dict[key] == getattr(result, key)

    else:
        with pytest.raises(error):
            result = js_f.CallbackFunction.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'function_name': 'testFunction',
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, None),
])
def test_CallbackFunction__to_untrimmed_dict(kwargs, error):
    instance = js_f.CallbackFunction(**kwargs)
    if not error:
        result = instance._to_untrimmed_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        for key in kwargs:
            assert kwargs[key] == result[key]

    else:
        with pytest.raises(error):
            result = instance._to_untrimmed_dict()


@pytest.mark.parametrize('kwargs, expected, error', [
    ({}, """function() {}""", None),
    ({
        'function_name': None,
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, """function(test1,test2) {\nreturn True;}""", None),
    ({
        'function_name': 'testFunction',
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, """function testFunction(test1,test2) {\nreturn True;}""", None),
])
def test_CallbackFunction__str__(kwargs, expected, error):
    instance = js_f.CallbackFunction(**kwargs)
    if not error:
        result = str(instance)
        assert result is not None
        assert isinstance(result, str) is True
        assert result == expected
        validate_js_function(result)
    else:
        with pytest.raises(error):
            result = str(instance)


@pytest.mark.parametrize('kwargs, filename, expected, error', [
    ({}, None, """function() {}""", None),
    ({
        'function_name': None,
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, None, """function(test1,test2) {\nreturn True;}""", None),
    ({
        'function_name': 'testFunction',
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, None, """function testFunction(test1,test2) {\nreturn True;}""", None),

    ({}, 'test1.js', """function() {}""", None),
    ({
        'function_name': None,
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, 'test2.js', """function(test1,test2) {\nreturn True;}""", None),
    ({
        'function_name': 'testFunction',
        'arguments': ['test1', 'test2'],
        'body': """return True;"""
    }, 'test3.js', """function testFunction(test1,test2) {\nreturn True;}""", None),
])
def test_CallbackFunction_to_js_literal(tmp_path, kwargs, filename, expected, error):
    instance = js_f.CallbackFunction(**kwargs)
    if filename:
        filename = os.path.join(tmp_path, filename)
    if not error:
        result = instance.to_js_literal(filename)
        assert result is not None
        assert isinstance(result, str) is True
        assert result == expected
        if filename:
            assert checkers.is_file(filename) is True
            with open(filename, 'r') as file_:
                result_as_str = file_.read()
                assert result_as_str == expected
    else:
        with pytest.raises(error):
            result = instance.to_js_literal(filename)


@pytest.mark.parametrize('original_str, error', [
    ("""function() {}""", None),
    ("""function(test1,test2) {\nreturn True;}""", None),
    ("""function testFunction(test1,test2) {\nreturn True;}""", None),
])
def test_CallbackFunction_convert_from_js_ast(original_str, error):
    original_parsed, updated_str = validate_js_function(original_str)
    unranged_result = validate_js_function(original_str, range = False)
    unranged_parsed = unranged_result[0]
    if original_parsed.body[0].type != 'FunctionDeclaration':
        property_definition = original_parsed.body[0].declarations[0].init
    else:
        property_definition = original_parsed.body[0]

    if not error:
        result = js_f.CallbackFunction._convert_from_js_ast(property_definition,
                                                            updated_str)
        assert result is not None
        assert isinstance(result, js_f.CallbackFunction) is True
        as_str = str(result)
        as_str_parsed, updated_as_str = validate_js_function(as_str, range = False)
        assert str(as_str_parsed) == str(unranged_parsed)
    else:
        with pytest.raises(error):
            result = js_f.CallbackFunction._convert_from_js_ast(property_definition,
                                                                updated_str)


@pytest.mark.parametrize('original_str, error', [
    ("""function() {}""", None),
    ("""function(test1,test2) {\nreturn true;}""", None),
    ("""function testFunction(test1,test2) {\nreturn true;}""", None),

    (123, TypeError),
    ("""const abc = 123;""", errors.HighchartsParseError),
])
def test_CallbackFunction_from_js_literal(original_str, error):
    if not error:
        unranged_result = js_f.CallbackFunction._validate_js_function(original_str,
                                                                      range = False)
        unranged_parsed = unranged_result[0]

        result = js_f.CallbackFunction.from_js_literal(original_str)
        assert result is not None
        assert isinstance(result, js_f.CallbackFunction) is True
        as_str = str(result)
        result_parsed = js_f.CallbackFunction._validate_js_function(as_str, range = False)
        as_str_parsed = result_parsed[0]
        assert str(as_str_parsed) == str(unranged_parsed)
    else:
        with pytest.raises(error):
            result = js_f.CallbackFunction.from_js_literal(original_str)


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({'class_name': 'TestClass',
      'methods': []}, None),
    ({'class_name': 'TestClass',
      'methods': ["""function constructor() { return true; }"""]}, None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor() { return true; }"""]}, None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor() { return true; }""",
                  """testMethod(test1, test2) { return true; }"""]}, None),


    ({'methods': ["""function wrongName() { return true; }"""]}, errors.HighchartsJavaScriptError),
    ({'methods': ["""function() { return true;}"""]}, errors.HighchartsJavaScriptError),
])
def test_JavaScriptClass__init__(kwargs, error):
    if not error:
        result = js_f.JavaScriptClass(**kwargs)
        assert result is not None
        assert isinstance(result, js_f.JavaScriptClass)
        methods = result.methods or []
        if 'methods' in kwargs:
            method_strings = [x for x in kwargs['methods']]
            for key in kwargs:
                for method in methods:
                    for method_string in method_strings:
                        in_method_string = method.function_name in method_string
                        if in_method_string:
                            break

                    assert in_method_string is True

    else:
        with pytest.raises(error):
            result = js_f.JavaScriptClass(**kwargs)


@pytest.mark.parametrize('as_dict, error', [
    ({}, None),
    ({'className': 'TestClass',
      'methods': []}, None),
    ({'className': 'TestClass',
      'methods': ["""function constructor() { return true; }"""]}, None),
    ({'className': 'TestClass',
      'methods': ["""constructor() { return true; }"""]}, None),
    ({'className': 'TestClass',
      'methods': ["""constructor() { return true; }""",
                  """testMethod(test1, test2) { return true; }"""]}, None),


    ({'methods': ["""function wrongName() { return true; }"""]}, errors.HighchartsJavaScriptError),
    ({'methods': ["""function() { return true;}"""]}, errors.HighchartsJavaScriptError),
])
def test_JavaScriptClass_from_dict(as_dict, error):
    if not error:
        result = js_f.JavaScriptClass.from_dict(as_dict)
        assert result is not None
        assert isinstance(result, js_f.JavaScriptClass) is True
        if as_dict.get('className'):
            assert result.class_name is not None
            assert result.class_name == as_dict.get('className')
        methods = result.methods or []
        if 'methods' in as_dict:
            method_strings = [x for x in as_dict['methods']]
            for key in as_dict:
                for method in methods:
                    for method_string in method_strings:
                        in_method_string = method.function_name in method_string
                        if in_method_string:
                            break

                    assert in_method_string is True

    else:
        with pytest.raises(error):
            result = js_f.JavaScriptClass.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, expected, error', [
    ({'class_name': 'TestClass',
      'methods': []},
     """class TestClass {\n}""",
     None),
    ({'class_name': 'TestClass',
      'methods': ["""function constructor() { return true; }"""]},
     """class TestClass {\nconstructor() {\n return true; \n}\n}""",
     None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor(test1, test2) { return true; }"""]},
     """class TestClass {\nconstructor(test1,test2) {\n return true; \n}\n}""",
     None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor() { return true; }""",
                  """testMethod(test1, test2) { return true; }"""]},
     """class TestClass {\nconstructor() {\n return true; \n}\ntestMethod(test1,test2) {\n return true; \n}\n}""",
     None),

    ({},
     """class None {\n}""",
     errors.HighchartsMissingClassNameError),
])
def test_JavaScriptClass__str__(kwargs, expected, error):
    instance = js_f.JavaScriptClass(**kwargs)
    if not error:
        result = str(instance)
        assert result is not None
        assert isinstance(result, str) is True
        print(result)
        print(expected)
        assert result == expected
        validate_js_function(result)
    else:
        with pytest.raises(error):
            result = str(instance)

@pytest.mark.parametrize('kwargs, expected, filename, error', [
    ({'class_name': 'TestClass',
      'methods': []},
     """class TestClass {\n}""",
     None,
     None),
    ({'class_name': 'TestClass',
      'methods': ["""function constructor() { return true; }"""]},
     """class TestClass {\nconstructor() {\n return true; \n}\n}""",
     None,
     None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor(test1, test2) { return true; }"""]},
     """class TestClass {\nconstructor(test1,test2) {\n return true; \n}\n}""",
     None,
     None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor() { return true; }""",
                  """testMethod(test1, test2) { return true; }"""]},
     """class TestClass {\nconstructor() {\n return true; \n}\ntestMethod(test1,test2) {\n return true; \n}\n}""",
     None,
     None),

    ({'class_name': 'TestClass',
      'methods': []},
     """class TestClass {\n}""",
     'test.js',
     None),
    ({'class_name': 'TestClass',
      'methods': ["""function constructor() { return true; }"""]},
     """class TestClass {\nconstructor() {\n return true; \n}\n}""",
     'test.js',
     None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor(test1, test2) { return true; }"""]},
     """class TestClass {\nconstructor(test1,test2) {\n return true; \n}\n}""",
     'test.js',
     None),
    ({'class_name': 'TestClass',
      'methods': ["""constructor() { return true; }""",
                  """testMethod(test1, test2) { return true; }"""]},
     """class TestClass {\nconstructor() {\n return true; \n}\ntestMethod(test1,test2) {\n return true; \n}\n}""",
     'test.js',
     None),

    ({},
     """class None {\n}""",
     None,
     ValueError),
])
def test_JavaScriptClass_to_js_literal(tmp_path, kwargs, expected, filename, error):
    instance = js_f.JavaScriptClass(**kwargs)
    if filename:
        filename = os.path.join(tmp_path, filename)
    if not error:
        result = instance.to_js_literal(filename)
        assert result is not None
        assert isinstance(result, str) is True
        assert result == expected
        if filename:
            assert checkers.is_file(filename) is True
            with open(filename, 'r') as file_:
                result_as_str = file_.read()
                assert result_as_str == expected
    else:
        with pytest.raises(error):
            result = instance.to_js_literal(filename)


@pytest.mark.parametrize('original_str, error', [
    ("""class TestClass {\n}""", None),
    ("""class TestClass {\nconstructor() {\n return true; \n}\n}""", None),
    ("""class TestClass {\nconstructor(test1,test2) {\n return true; \n}\n}""", None),
    ("""class TestClass {\nconstructor() {\n return true; \n}\ntestMethod(test1,test2) {\n return true; \n}\n}""", None),

    ("""class None {\n}""", ValueError),
    ("""const notAClass = 123;""", errors.HighchartsParseError),
])
def test_JavaScriptClass_convert_from_js_ast(original_str, error):
    original_parsed, updated_str = validate_js_function(original_str)
    unranged_result = validate_js_function(original_str, range = False)
    unranged_parsed = unranged_result[0]
    definition = original_parsed.body[0]

    if not error:
        result = js_f.JavaScriptClass._convert_from_js_ast(definition, original_str)
        assert result is not None
        assert isinstance(result, js_f.JavaScriptClass) is True
        as_str = str(result)
        as_str_parsed, updated_as_str = validate_js_function(as_str, range = False)
        assert str(as_str_parsed) == str(unranged_parsed)
    else:
        with pytest.raises(error):
            result = js_f.JavaScriptClass._convert_from_js_ast(definition, original_str)


@pytest.mark.parametrize('original_str, error', [
    ("""class TestClass {\n}""", None),
    ("""class TestClass {\nconstructor() {\n return true; \n}\n}""", None),
    ("""class TestClass {\nconstructor(test1,test2) {\n return true; \n}\n}""", None),
    ("""class TestClass {\nconstructor() {\n return true; \n}\ntestMethod(test1,test2) {\n return true; \n}\n}""", None),

    ("""class None {\n}""", ValueError),
    ("""const notAClass = 123;""", errors.HighchartsParseError),
])
def test_JavaScriptClass_from_js_literal(original_str, error):
    if not error:
        unranged_result = validate_js_function(original_str, range = False)
        unranged_parsed = unranged_result[0]

        result = js_f.JavaScriptClass.from_js_literal(original_str)
        assert result is not None
        assert isinstance(result, js_f.JavaScriptClass) is True
        as_str = str(result)
        result_parsed = validate_js_function(as_str, range = False)
        as_str_parsed = result_parsed[0]
        assert str(as_str_parsed) == str(unranged_parsed)
    else:
        with pytest.raises(error):
            result = js_f.JavaScriptClass.from_js_literal(original_str)
