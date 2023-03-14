"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.legend.bubble_legend import BubbleLegend as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'border_color': '#ccc',
      'border_width': 12,
      'class_name': 'some-class-name',
      'color': '#fff',
      'connector_class_name': 'some-class-name',
      'connector_color': '#999',
      'connector_distance': 6,
      'connector_width': 2,
      'enabled': True,
      'labels': {
          'align': 'center',
          'allowOverlap': False,
          'className': 'some-class-name',
          'format': 'a format string',
          'formatter': """function () { return true; }""",
          'style': 'some style string',
          'x': 3,
          'y': 1
      },
      'legend_index': 1,
      'max_size': 24,
      'min_size': 6,
      'ranges': [
          {
           'borderColor': '#ccc',
           'color': '#fff',
           'connectorColor': '#999',
           'value': 123
          },
          {
           'borderColor': '#ccc',
           'color': '#fff',
           'connectorColor': '#999',
           'value': 123
          },
          {
           'borderColor': '#ccc',
           'color': '#fff',
           'connectorColor': '#999',
           'value': 123
          }
      ],
      'size_by': 'width',
      'size_by_absolute_value': True,
      'z_index': 3,
      'z_threshold': 123
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
    ('legend/bubble_legend/01.js', False, None),

    ('legend/bubble_legend/error-01.js', False, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),

    ('legend/bubble_legend/01.js', True, None),

    ('legend/bubble_legend/error-01.js', True, (errors.HighchartsValueError,
                                                errors.HighchartsParseError,
                                                JSONDecodeError,
                                                TypeError,
                                                ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
