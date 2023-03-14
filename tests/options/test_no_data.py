"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.no_data import NoData as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
        'attr': {
            'stroke': '#ff0000',
            'stroke-width': 2,
            'rotation': 45,
            'd': ['M', 10, 10, 'L', 30, 30, 'z']
        },
        'position': {
            'align': 'center',
            'verticalAlign': 'top',
            'x': 10,
            'y': 15
        },
        'use_html': False
    }, None),
    
    ({
          'attr': {
              'stroke': '#ff0000',
              'stroke-width': 2,
              'rotation': 45,
              'd': ['M', 10, 10, 'L', 30, 30, 'z'],
              'not a valid attribute key': 123
          },
          'position': {
              'align': 'center',
              'verticalAlign': 'top',
              'x': 10,
              'y': 15
          },
          'use_html': False
    }, (errors.HighchartsValueError,
        errors.HighchartsParseError,
        JSONDecodeError,
        ValueError)),
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
    ('no_data/01.js', False, None),
    ('no_data/02.js', False, None),

    ('no_data/error-01.js', False, (errors.HighchartsValueError,
                                    errors.HighchartsParseError,
                                    JSONDecodeError,
                                    ValueError)),
    ('no_data/error-02.js', False, (errors.HighchartsValueError,
                                    errors.HighchartsParseError,
                                    JSONDecodeError,
                                    ValueError)),

    ('no_data/01.js', True, None),
    ('no_data/02.js', True, None),

    ('no_data/error-01.js', True, (errors.HighchartsValueError,
                                   errors.HighchartsParseError,
                                   JSONDecodeError,
                                   ValueError)),
    ('no_data/error-02.js', True, (errors.HighchartsValueError,
                                   errors.HighchartsParseError,
                                   JSONDecodeError,
                                   ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
