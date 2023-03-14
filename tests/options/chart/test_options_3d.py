"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.chart.options_3d import Options3D as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'alpha': 0.5,
      'axis_label_position': 'auto',
      'beta': 15,
      'depth': 20,
      'enabled': True,
      'fit_to_plot': True,
      'frame': {
          'back': {
              'color': '#ccc',
              'size': 2,
              'visible': 'auto'
          },
          'bottom': {
              'color': '#ccc',
              'size': 2,
              'visible': 'auto'
          },
          'front': {
              'color': '#ccc',
              'size': 2,
              'visible': 'auto'
          },
          'left': {
              'color': '#ccc',
              'size': 2,
              'visible': 'auto'
          },
          'right': {
              'color': '#ccc',
              'size': 2,
              'visible': 'auto'
          },
          'top': {
              'color': '#ccc',
              'size': 2,
              'visible': 'auto'
          },
          'size': 2,
          'visible': True
      },
      'view_distance': 20
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
    ('chart/options_3d/01.js', False, None),

    ('chart/options_3d/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('chart/options_3d/01.js', True, None),

    ('chart/options_3d/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
