"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.states import States as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'hover': {
          'animation': {
              'duration': 123
          },
          'borderColor': '#cccccc',
          'brightness': 0.3,
          'enabled': True
      },
      'inactive': {
          'enabled': True,
          'opacity': 0.5
      },
      'normal': {
          'animation': {
              'defer': 24
          }
      },
      'select': {
          'color': '#ff0000',
          'enabled': True,
      }
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
    ('utility_classes/states/01.js', False, None),
    ('utility_classes/states/02.js', False, None),

    ('utility_classes/states/error-01.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/states/error-02.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/states/01.js', True, None),
    ('utility_classes/states/02.js', True, None),

    ('utility_classes/states/error-01.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/states/error-02.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
