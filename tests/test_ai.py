"""Tests for ``highcharts.ai``."""

import pytest

from highcharts_core import ai
from highcharts_core import errors
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


def func1():
    return 'A value!'


func1_as_js = """function func1() {
    return 'A value!';
}"""


def func2(arg1, keyword_arg = 'default'):
    arg1 += 123
    return arg1 in keyword_arg


func2_as_js = """function func2(arg1, keyword_arg = 'default') {
    arg1 = arg1 + 123;
    return keyword_arg.includes(arg1.toString());
}"""


@pytest.mark.parametrize('callable, expected, error', [
    (func1, """def func1():\n    return 'A value!'\n""", None),
    (func2, """def func2(arg1, keyword_arg = 'default'):\n    arg1 += 123\n    return arg1 in keyword_arg\n""", None),
    
    (1, None, errors.HighchartsValueError),
])
def test_get_source(callable, expected, error):
    if not error:
        result = ai.get_source(callable)
        assert result == expected
    else:
        with pytest.raises(error):
            result = ai.get_source(callable)


@pytest.mark.parametrize('callable, model, expected, error', [
    (func1, 'gpt-3.5-turbo', func1_as_js, None),
    (func2, 'gpt-3.5-turbo', func2_as_js, None),

    (1, 'gpt-3.5-turbo', 'not a valid function', ValueError),
])
def test_convert_to_js(callable, model, expected, error):
    if not error:
        result = ai.convert_to_js(callable, model)
        try:
            assert result == expected
        except AssertionError:
            try:
                parsed, as_str = CallbackFunction._validate_js_function(result)
            except (errors.HighchartsParseError, TypeError):
                raise AssertionError(f'Expected {expected} but got something '
                                     f'that was not a valid JavaScript '
                                     f'function:\n{result}')
    else:
        with pytest.raises(error):
            result = ai.convert_to_js(callable, model)