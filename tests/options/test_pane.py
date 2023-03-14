"""Tests for ``highcharts.pane``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.pane import Pane as cls
from highcharts_core.options.pane import PaneBackground
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'background': [{
          'className': 'test-class-name',
          'innerRadius': '24%',
          'shape': 'circle'
      }],
      'center': ['50%', '50%'],
      'size': '120',
      'start_angle': 0
    }, None),
    ({
      'background': [
          {
            'className': 'test-class-name',
            'innerRadius': '24%',
            'shape': 'circle'
          },
          {
            'innerRadius': '35%',
          }
      ],
      'center': ['50%', '50%'],
      'size': '120',
      'start_angle': 0
    }, None),

    ({
        'background': [{
            'className': 'test-class-name',
            'innerRadius': '24%',
            'shape': 'circle'
        }],
        'center': ['not-valid', 'not-valid'],
        'size': '120',
        'start_angle': 0
    }, (ValueError, TypeError)),
    ({
        'background': [
            {
                'className': 'test-class-name',
                'innerRadius': '24%',
                'shape': 'circle'
            },
            {
                'innerRadius': '35',
            }
        ],
        'center': ['not-valid'],
        'size': 120,
        'start_angle': 0
    }, (ValueError, TypeError)),
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
    ('pane/01.js', False, None),
    ('pane/02.js', False, None),

    ('pane/error-01.js', False, (errors.HighchartsValueError,
                                 errors.HighchartsParseError,
                                 JSONDecodeError,
                                 ValueError)),
    ('pane/error-02.js', False, (errors.HighchartsValueError,
                                 errors.HighchartsParseError,
                                 JSONDecodeError,
                                 ValueError)),

    ('pane/01.js', True, None),
    ('pane/02.js', True, None),

    ('pane/error-01.js', True, (errors.HighchartsValueError,
                                errors.HighchartsParseError,
                                JSONDecodeError,
                                ValueError)),
    ('pane/error-02.js', True, (errors.HighchartsValueError,
                                errors.HighchartsParseError,
                                JSONDecodeError,
                                ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
