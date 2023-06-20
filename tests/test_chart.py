"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.chart import Chart as cls
from highcharts_core.global_options.shared_options import SharedOptions
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


@pytest.mark.parametrize('kwargs, error', [
    ({}, errors.HighchartsValueError),
])
def test_bugfix34_SharedOptions_error(kwargs, error):
    shared_options = SharedOptions()
    instance = cls(**kwargs)
    if not error:
        instance.options = shared_options
    else:
        with pytest.raises(error):
            instance.options = shared_options


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
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
     False,
     None),
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
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



@pytest.mark.parametrize('json_str, expected_modules, error', [
    ("""{
    "chart": {
        "type": "column"
    },
    "colors": null,
    "credits": false,
    "exporting": {
        "scale": 1
    },
    "series": [{
        "baseSeries": 1,
        "color": "#434343",
        "name": "Pareto",
        "tooltip": {
            "valueDecimals": 2,
            "valueSuffix": "%"
        },
        "type": "pareto",
        "yAxis": 1,
        "zIndex": 10
    }, {
        "color": "#7cb5ec",
        "data": [1, 23, 45, 54, 84, 13, 8, 7, 23, 1, 34, 6, 8, 99, 85, 23, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],
        "name": "random-name",
        "type": "column",
        "zIndex": 2
    }],
    "title": {
        "text": "Random Name Pareto"
    },
    "tooltip": {
        "shared": true
    },
    "xAxis": {
        "categories": ["Something", "Something", "Something", "Something", "Something", "Something", "Hypovolemia", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something"],
        "crosshair": true,
        "labels": {
            "rotation": 90
        }
    },
    "yAxis": [{
        "title": {
            "text": "count"
        }
    }, {
        "labels": {
            "format": "{value}%"
        },
        "max": 100,
        "maxPadding": 0,
        "min": 0,
        "minPadding": 0,
        "opposite": true,
        "title": {
            "text": "accum percent"
        }
    }]
}""", ['highcharts', 'modules/exporting', 'modules/pareto'], None),
])
def test_get_required_modules(json_str, expected_modules, error):
    from highcharts_core.options import HighchartsOptions
    options = HighchartsOptions.from_json(json_str)
    chart = cls.from_options(options)
    if not error:
        result = chart.get_required_modules()
        if expected_modules:
            assert len(result) == len(expected_modules)
            for item in expected_modules:
                assert item in result
        else:
            assert result is None or len(result) == 0
    else:
        with pytest.raises(error):
            result = chart.get_required_modules()
