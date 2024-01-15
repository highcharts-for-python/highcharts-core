"""Tests for ``highcharts.no_data``."""

import pytest

import datetime
from json.decoder import JSONDecodeError

from validator_collection import checkers

from highcharts_core.options.series.custom import CustomSeries as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, run_pandas_tests

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CustomSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CustomSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CustomSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CustomSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)
