"""Tests for ``highcharts.no_data``."""

import pytest

import datetime
from json.decoder import JSONDecodeError

from validator_collection import checkers

from highcharts_core.options.series.custom import CustomSeries as cls
from highcharts_core import errors
from tests.fixtures import (
    input_files,
    check_input_file,
    to_camelCase,
    to_js_dict,
    Class__init__,
    Class__to_untrimmed_dict,
    Class_from_dict,
    Class_to_dict,
    Class_from_js_literal,
    run_pandas_tests,
)

STANDARD_PARAMS = [
    ({}, None),
    (
        {
            "type": "lowmedhigh",
            "parent_type": "boxplot",
            "keys": ["low", "median", "high"],
        },
        None,
    ),
]


@pytest.mark.parametrize("kwargs, error", STANDARD_PARAMS)
def test_CustomSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize("kwargs, error", STANDARD_PARAMS)
def test_CustomSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize("kwargs, error", STANDARD_PARAMS)
def test_CustomSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize("kwargs, error", STANDARD_PARAMS)
def test_CustomSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize(
    "kwargs, expected, error",
    [
        (
            {
                "type": "lowmedhigh",
                "parent_type": "boxplot",
                "keys": ["low", "median", "high"],
            },
            """Highcharts.seriesType('lowmedhigh', 'boxplot', {\n  keys: ['low',\n'median',\n'high']\n}\n);""",
            None,
        ),
    ],
)
def test_CustomSeries_to_registration_js_literal(kwargs, expected, error):
    if not error:
        obj = cls(**kwargs)
        result = obj.to_registration_js_literal()
        # print(result)
        assert result == expected
    else:
        with pytest.raises(error):
            result = cls.to_registration_js_literal(kwargs)


def test_CustomSeries_instance_init():
    kwargs = {
        "type": "lowmedhigh",
        "parent_type": "boxplot",
        "keys": ["low", "median", "high"],
        "low": 1,
        "median": 2,
        "high": 3,
        "name": "Test Name",
    }

    instance = cls(**kwargs)
    assert instance.type == kwargs["type"]
    assert instance.parent_type == kwargs["parent_type"]
    assert instance.keys == kwargs["keys"]
    assert instance.name == kwargs["name"]
    assert instance.low == kwargs["low"]
    assert instance.median == kwargs["median"]
    assert instance.high == kwargs["high"]
    assert instance._parent_instance is not None


def test_CustomSeries_instance_to_js_literal():
    kwargs = {
        "type": "lowmedhigh",
        "parent_type": "boxplot",
        "keys": ["low", "median", "high"],
        "data": {
            "low": 1,
            "median": 2,
            "high": 3,
        },
        "name": "Test Name",
    }

    instance = cls(**kwargs)
    result = instance.to_js_literal()
    print(result)
    expected = """"""
    assert result == expected