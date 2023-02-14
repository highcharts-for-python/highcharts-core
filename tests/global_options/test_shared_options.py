"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.global_options.shared_options import SharedOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, Class_from_js_literal_with_expected

STANDARD_PARAMS = [
    ({}, None),
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


@pytest.mark.parametrize('input_filename, expected_filename, as_file, error', [
    ('global_options/shared_options/01-input.js',
     'global_options/shared_options/01-expected.js',
     False,
     None),
    ('global_options/shared_options/01-input.js',
     'global_options/shared_options/01-expected.js',
     False,
     None),
])
def test_from_js_literal(input_files, input_filename, expected_filename, as_file, error):
    Class_from_js_literal_with_expected(cls,
                                        input_files,
                                        input_filename,
                                        expected_filename,
                                        as_file,
                                        error)
