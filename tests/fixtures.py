# -*- coding: utf-8 -*-

"""
***********************************
tests._fixtures
***********************************

Fixtures used by the SQLAthanor test suite.

"""
import os

import pytest

from validator_collection import checkers


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
        else:
            new_key = to_camelCase(key)
        as_dict[new_key] = original[key]

    return as_dict


def Class__init__(cls, kwargs, error):
    if not error:
        result = cls(**kwargs)
        assert result is not None
        assert isinstance(result, cls) is True
        for key in kwargs:
            assert kwargs[key] == getattr(result, key)
    else:
        with pytest.raises(error):
            result = cls(**kwargs)


def Class__to_untrimmed_dict(cls, kwargs, error):
    if not error:
        instance = cls(**kwargs)
        result = instance._to_untrimmed_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        for key in kwargs:
            if '_' not in key:
                assert kwargs[key] == result.get(key)
            else:
                if 'html' in key:
                    assert kwargs[key] == result.get('useHTML')
                else:
                    assert kwargs[key] == result.get(to_camelCase(key))
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            result = instance._to_untrimmed_dict()


def Class_from_dict(cls, kwargs, error):
    as_dict = to_js_dict(kwargs)

    if not error:
        instance = cls.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, cls) is True
        for key in kwargs:
            assert kwargs[key] == getattr(instance, key)
    else:
        with pytest.raises(error):
            instance = cls.from_dict(as_dict)


def Class_to_dict(cls, kwargs, error):
    expected = to_js_dict(kwargs)
    for key in expected:
        if expected[key] is None:
            del expected[key]

    if not error:
        instance = cls(**kwargs)
        result = instance.to_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        print(expected)
        print(result)
        assert checkers.are_dicts_equivalent(result, expected) is True
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
        parsed_original, original_str = cls._validate_js_literal(as_str)
        result = cls.from_js_literal(input_string)
        assert result is not None
        assert isinstance(result, cls) is True

        as_js_literal = result.to_js_literal()
        parsed_output, output_str = cls._validate_js_literal(as_js_literal)
        print(as_str)
        print('-----------')
        print(as_js_literal)
        assert str(parsed_output) == str(parsed_original)
    else:
        with pytest.raises(error):
            result = cls.from_js_literal(input_string)
