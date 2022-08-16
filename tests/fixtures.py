# -*- coding: utf-8 -*-

"""
***********************************
tests._fixtures
***********************************

Fixtures used by the SQLAthanor test suite.

"""
import os
from copy import deepcopy
from collections import UserDict

import pytest

from validator_collection import checkers, validators


class State(object):
    """Class to hold incremental test state."""
    # pylint: disable=too-few-public-methods
    pass


@pytest.fixture
def state(request):
    """Return the :class:`State` object that holds incremental test state."""
    # pylint: disable=W0108
    return request.cached_setup(
        setup = lambda: State(),
        scope = "session"
    )


@pytest.fixture
def run_pyspark_tests(request):
    """Return the ``--pyspark`` command-line option."""
    value = request.config.getoption("--pyspark")
    value = value.lower()
    if value in ['false', False, 0, 'no', 'no']:
        return False
    else:
        return True


@pytest.fixture
def input_files(request):
    """Return the ``--inputs`` command-line option."""
    return request.config.getoption("--inputs")


def check_input_file(input_directory, input_value):
    inputs = os.path.abspath(input_directory)
    if not os.path.exists(input_directory):
        raise AssertionError('input directory (%s) does not exist' % inputs)
    elif not os.path.isdir(input_directory):
        raise AssertionError('input directory (%s) is not a directory' % inputs)

    try:
        input_file = os.path.join(input_directory, input_value)
    except (TypeError, AttributeError):
        input_file = None

    if input_file is not None and checkers.is_file(input_file):
        input_value = input_file

    return input_value


def to_camelCase(variable_name):
    if '_' not in variable_name:
        return variable_name

    if 'url' in variable_name:
        variable_name = variable_name.replace('url', 'URL')

    camel_case = ''
    previous_character = ''
    for character in variable_name:
        if character != '_' and previous_character != '_':
            camel_case += character
            previous_character = character
        elif character == '_':
            previous_character = character
        elif character != '_' and previous_character == '_':
            camel_case += character.upper()
            previous_character = character

    return camel_case


def to_js_dict(original):
    as_dict = {}
    for key in original:
        if 'html' in key:
            new_key = 'useHTML'
        elif 'utc' in key:
            new_key = 'useUTC'
        else:
            new_key = to_camelCase(key)
        as_dict[new_key] = original[key]

    return as_dict


def does_kwarg_value_match_result(kwarg_value, result_value):
    """Validate whether the value of ``kwarg_value`` matches the value of ``result_value``.

    :returns: ``True`` if match, ``False`` if not
    """
    if isinstance(kwarg_value, (dict,
                                UserDict)) and not isinstance(result_value, (dict,
                                                                             UserDict)):
        result_cls = result_value.__class__
        try:
            test_value = result_cls.from_dict(kwarg_value)
        except AttributeError:
            if not result_value and not kwarg_value:
                return True
            else:
                return False

        print(test_value.to_js_literal())
        print(result_value.to_js_literal())

        return test_value == result_value
    elif not isinstance(kwarg_value, (int, float)) and isinstance(result_value, (int,
                                                                                 float)):
        test_value = validators.numeric(kwarg_value)
        return test_value == result_value
    elif isinstance(kwarg_value, (int, float)) and not isinstance(result_value, (int,
                                                                                 float)):
        result_value = validators.numeric(result_value)
        return test_value == result_value
    elif isinstance(kwarg_value, dict) and isinstance(result_value, dict):
        return checkers.are_dicts_equivalent(kwarg_value, result_value)
    elif isinstance(kwarg_value, (dict,
                                  UserDict)) and isinstance(result_value, (dict,
                                                                           UserDict)):
        if len(kwarg_value) != len(result_value):
            return False
        for key in kwarg_value:
            if kwarg_value.get(key) != result_value.get(key):
                return False

        return True
    elif checkers.is_iterable(kwarg_value):
        print('is iterable')
        if len(kwarg_value) != len(result_value):
            return False
        counter = 0
        for item in kwarg_value:
            result_item = result_value[counter]
            item_match = does_kwarg_value_match_result(item, result_item)
            if not item_match:
                return False
            counter += 1
    else:
        print('running else')
        return kwarg_value == result_value

    return True


def trim_expected(expected):
    """Remove keys from ``expected`` or its children that should not be evaluated."""
    new_dict = {}
    if not isinstance(expected, dict):
        return expected
    for key in expected:
        if expected[key] is None:
            continue
        elif isinstance(expected[key], dict):
            trimmed_value = trim_expected(expected[key])
            if trimmed_value:
                new_dict[key] = trimmed_value
        elif checkers.is_iterable(expected[key]):
            trimmed_value = []
            for item in expected[key]:
                trimmed_item = trim_expected(item)
                if trimmed_item:
                    trimmed_value.append(trimmed_item)

            if trimmed_value:
                new_dict[key] = trimmed_value
        else:
            new_dict[key] = expected[key]

    return new_dict


def Class__init__(cls, kwargs, error):
    kwargs_copy = deepcopy(kwargs)
    if not error:
        result = cls(**kwargs)
        print(kwargs_copy)
        assert result is not None
        assert isinstance(result, cls) is True
        for key in kwargs_copy:
            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('class'):
                continue

            kwarg_value = kwargs_copy[key]
            result_value = getattr(result, key)
            print(f'KWARG VALUE:\n{kwarg_value}')
            print(f'RESULT VALUE:\n{result_value}')
            assert does_kwarg_value_match_result(kwargs_copy[key],
                                                 getattr(result, key)) is True
    else:
        with pytest.raises(error):
            result = cls(**kwargs)


def Class__to_untrimmed_dict(cls, kwargs, error):
    kwargs_copy = deepcopy(kwargs)
    if not error:
        instance = cls(**kwargs)
        result = instance._to_untrimmed_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        for key in kwargs_copy:
            kwarg_value = kwargs_copy[key]
            result_value = result.get(key)
            print(f'checking key: {key}')
            print(f'KWARG VALUE:\n{kwarg_value}')
            print(f'RESULT VALUE:\n{result_value}')

            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('class'):
                continue
            if '_' not in key:
                assert does_kwarg_value_match_result(kwargs_copy[key],
                                                     result.get(key)) is True
            else:
                if 'html' in key:
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get('useHTML')) is True
                elif 'utc' in key:
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get('useUTC')) is True
                elif 'url' in key:
                    updated_key = key.replace('url', 'URL')
                    matches = does_kwarg_value_match_result(
                        kwargs_copy[key],
                        result.get(to_camelCase(updated_key))
                    )
                    assert matches is True
                elif key == 'pattern_options':
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get('pattern')) is True
                elif isinstance(instance, UserDict):
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get(key)) is True
                else:
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get(to_camelCase(key))) is True
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            result = instance._to_untrimmed_dict()


def Class_from_dict(cls, kwargs, error):
    as_dict = to_js_dict(deepcopy(kwargs))

    if not error:
        instance = cls.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, cls) is True
        for key in kwargs:
            if isinstance(kwargs[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs[key], str) and kwargs[key].startswith('class'):
                continue
            kwarg_value = kwargs[key]
            if key in ['pattern_options', 'patternOptions']:
                result_value = getattr(instance, 'pattern_options')
            else:
                result_value = getattr(instance, key)
            print(kwarg_value)
            print(result_value)
            assert does_kwarg_value_match_result(kwarg_value, result_value)
    else:
        with pytest.raises(error):
            instance = cls.from_dict(as_dict)


def Class_to_dict(cls, kwargs, error):
    untrimmed_expected = to_js_dict(deepcopy(kwargs))
    expected = trim_expected(untrimmed_expected)
    check_dicts = True
    for key in expected:
        if not checkers.is_type(expected[key], (str, int, float, bool, list, dict)):
            check_dicts = False
        elif isinstance(expected[key], str) and expected[key].startswith('function'):
            check_dicts = False
        elif isinstance(expected[key], str) and expected[key].startswith('class'):
            check_dicts = False

    if not error:
        instance = cls(**kwargs)
        result = instance.to_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        print(expected)
        print(result)
        if checkers.is_type(instance, ('MarkerAttributeObject')):
            check_dicts = False
        if check_dicts:
            assert len(expected) == len(result)
            for key in expected:
                if key == 'patternOptions':
                    assert does_kwarg_value_match_result(expected[key],
                                                         result.get('pattern')) is True
                else:
                    assert does_kwarg_value_match_result(expected[key], result.get(key))
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            result = instance.to_dict()


def Class_from_js_literal(cls, input_files, filename, as_file, error):
    input_file = check_input_file(input_files, filename)

    with open(input_file, 'r') as file_:
        as_str = file_.read()

    if as_file:
        input_string = input_file
    else:
        input_string = as_str

    if not error:
        print('-------------------')
        print('ORIGINAL VALIDATION')
        parsed_original, original_str = cls._validate_js_literal(as_str, range = False)
        print('-------------')
        print('ORIGINAL CALL')
        print(as_str)
        result = cls.from_js_literal(input_string)
        assert result is not None
        assert isinstance(result, cls) is True

        as_js_literal = result.to_js_literal()
        print('-----------------')
        print('RESULT VALIDATION')
        if 'pattern:' in as_js_literal:
            as_js_literal = as_js_literal.replace('pattern:', 'patternOptions:')

        print(as_js_literal)
        parsed_output, output_str = cls._validate_js_literal(as_js_literal, range = False)
        assert str(parsed_output) == str(parsed_original)
    else:
        with pytest.raises(error):
            result = cls.from_js_literal(input_string)
