"""Tests for ``highcharts_core.ai``."""
import os

import pytest

from highcharts_core import ai
from highcharts_core import errors
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from tests.fixtures import disable_ai, openai_api_key


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
def test_convert_to_js(disable_ai, openai_api_key, callable, model, expected, error):
    if not error and not disable_ai:
        try:
            result = ai.convert_to_js(callable,
                                      model,
                                      api_key = openai_api_key)
        except errors.HighchartsValueError as error:
            openai_api_key = os.getenv('OPENAI_API_KEY', None)
            api_key_present = openai_api_key is not None
            print(f'OPENAI_API_KEY: {api_key_present}')
            print(f'os.environ keys:\n{os.environ.keys()}')
            raise error
        try:
            assert result == expected
        except AssertionError:
            try:
                parsed, as_str = CallbackFunction._validate_js_function(result)
            except (errors.HighchartsParseError, TypeError):
                raise AssertionError(f'Expected {expected} but got something '
                                     f'that was not a valid JavaScript '
                                     f'function:\n{result}')
    elif not disable_ai:
        with pytest.raises(error):
            result = ai.convert_to_js(callable, 
                                      model,
                                      api_key = openai_api_key)
