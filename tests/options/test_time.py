"""Tests for ``highcharts.time``."""

import pytest

from validator_collection import checkers

from highcharts_core.options.time import Time as cls
from highcharts_core.utility_classes.javascript_functions import CallbackFunction, \
    JavaScriptClass
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'timezone': 'Europe/Oslo',
      'use_utc': False
    }, None),
    ({
      'Date': JavaScriptClass(class_name = 'Date',
                              methods = ["""constructor() { return true; }"""])
    }, None),
    ({
      'Date': """class DateClass { constructor() { return true; }}"""
    }, None)
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('time/01.js', False, None),
    ('time/02.js', False, None),

    ('time/error-01.js', False, (TypeError, ValueError)),
    ('time/error-02.js', False, errors.HighchartsParseError),

    ('time/01.js', True, None),
    ('time/02.js', True, None),

    ('time/error-01.js', True, (TypeError, ValueError)),
    ('time/error-02.js', True, errors.HighchartsParseError),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
