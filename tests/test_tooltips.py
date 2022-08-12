"""Tests for ``highcharts.tooltips``."""

import pytest

from validator_collection import checkers

from highcharts.tooltips import Tooltip as cls
from highcharts.utility_classes.javascript_functions import CallbackFunction
from highcharts import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'value_decimals': 2,
      'value_prefix': '$',
      'value_suffix': ' USD'
     }, None),
    ({
        'formatter': CallbackFunction.from_js_literal("""function () {
            // The first returned item is the header, subsequent items are the
            // points
            return ['<b>' + this.x + '</b>'].concat(
                this.points ?
                    this.points.map(function (point) {
                        return point.series.name + ': ' + point.y + 'm';
                    }) : []
            );
        }"""),
        'split': True
     }, None),
    ({
        'formatter': """function () {
            // The first returned item is the header, subsequent items are the
            // points
            return ['<b>' + this.x + '</b>'].concat(
                this.points ?
                    this.points.map(function (point) {
                        return point.series.name + ': ' + point.y + 'm';
                    }) : []
            );
        }""",
        'split': True
     }, None),

    ({
      'border_width': 'not-a-number'
    }, (ValueError, TypeError)),
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
    ('tooltips/01.js', False, None),
    ('tooltips/02.js', False, None),

    ('tooltips/error-01.js', False, (TypeError, ValueError)),
    ('tooltips/error-02.js', False, errors.HighchartsParseError),

    ('tooltips/01.js', True, None),
    ('tooltips/02.js', True, None),

    ('tooltips/error-01.js', True, (TypeError, ValueError)),
    ('tooltips/error-02.js', True, errors.HighchartsParseError),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
