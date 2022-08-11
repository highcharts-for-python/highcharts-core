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
