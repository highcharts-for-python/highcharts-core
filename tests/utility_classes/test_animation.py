"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.animation import AnimationOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'complete': """function () { return true; }""",
      'defer': 5,
      'duration': 30,
      'easing': 'easing',
      'step': """function () { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/animation/01.js', False, None),

    ('utility_classes/animation/error-01.js', False, (errors.HighchartsValueError,
                                                      errors.HighchartsParseError,
                                                      JSONDecodeError,
                                                      TypeError,
                                                      ValueError)),

    ('utility_classes/animation/01.js', True, None),

    ('utility_classes/animation/error-01.js', True, (errors.HighchartsValueError,
                                                     errors.HighchartsParseError,
                                                     JSONDecodeError,
                                                     TypeError,
                                                     ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
