"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options import HighchartsOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

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


@pytest.mark.parametrize('filename, as_file, error', [
    ('options/01.js', False, None),
    ('options/01.js', True, None),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'title': {
            'text': 'My Chart'
        }
    }, None),
    ({
        'plot_options': {
            'series': {
                'crisp': True
            }
        }
    }, None),
    ({
        'series': [
            {
                'crisp': True,
                'type': 'bar'
            },
            {
                'crisp': False,
                'type': 'bar'
            }
        ]
    }, None),
])
def test__repr__(kwargs, error):
    obj = cls(**kwargs)
    if not error:
        result = repr(obj)
        if 'plot_options' in kwargs:
            assert 'plot_options = ' in result
        if 'series' in kwargs:
            assert 'series = ' in result
    else:
        with pytest.raises(error):
            result = repr(obj)


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'title': {
            'text': 'My Chart'
        }
    }, None),
    ({
        'plot_options': {
            'series': {
                'crisp': True
            }
        }
    }, None),
    ({
        'series': [
            {
                'crisp': True,
                'type': 'bar'
            },
            {
                'crisp': False,
                'type': 'bar'
            }
        ]
    }, None),
])
def test__str__(kwargs, error):
    obj = cls(**kwargs)
    if not error:
        result = str(obj)
        print(result)
        assert 'plot_options = ' not in result
        assert 'series = ' not in result
    else:
        with pytest.raises(error):
            result = str(obj)