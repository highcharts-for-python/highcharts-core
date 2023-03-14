"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.markers import Marker as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'enabled': True,
      'fill_color': '#cccccc',
      'height': 24,
      'line_width': 2,
      'radius': 2,
      'states': {
          'hover': {
              'enabled': True
          }
      },
      'symbol': 'circle',
      'width': 48
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
    ('utility_classes/markers/01.js', False, None),

    ('utility_classes/markers/error-01.js', False, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),

    ('utility_classes/markers/01.js', True, None),

    ('utility_classes/markers/error-01.js', True, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
