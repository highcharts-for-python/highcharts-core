"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.data_labels import DataLabel as cls
from highcharts_core.utility_classes.data_labels import NodeDataLabel as cls2
from highcharts_core.utility_classes.data_labels import SunburstDataLabel as cls3
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'align': 'center',
      'allow_overlap': True,
      'animation': {
          'defer': 5
      },
      'background_color': {
          'linearGradient': {
              'x1': 0.123,
              'x2': 0.234,
              'y1': 0.345,
              'y2': 0.456
          },
          'stops': [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      'border_color': '#999999',
      'border_radius': 24,
      'border_width': 1,
      'class_name': 'some-class-name',
      'color': '#000000',
      'crop': True,
      'defer': False,
      'enabled': True,
      'filter': {
          'operator': '>=',
          'property': 'some_property',
          'value': 123
      },
      'format': 'some format',
      'formatter': """function() { return true; }""",
      'inside': True,
      'null_format': 'some format',
      'null_formatter': """function() { return true; }""",
      'overflow': 'none',
      'padding': 12,
      'position': 'center',
      'rotation': 0,
      'shadow': False,
      'shape': 'rect',
      'style': 'style goes here',
      'use_html': False,
      'vertical_align': 'top',
      'x': 10,
      'y': 20,
      'z': 0
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_DataLabel__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_DataLabel__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_DataLabel_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_DataLabel_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/data_labels/01.js', False, None),

    ('utility_classes/data_labels/error-01.js', False, (errors.HighchartsValueError,
                                                        errors.HighchartsParseError,
                                                        JSONDecodeError,
                                                        TypeError,
                                                        ValueError)),

    ('utility_classes/data_labels/01.js', True, None),

    ('utility_classes/data_labels/error-01.js', True, (errors.HighchartsValueError,
                                                       errors.HighchartsParseError,
                                                       JSONDecodeError,
                                                       TypeError,
                                                       ValueError)),
])
def test_DataLabel_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'align': 'center',
      'allow_overlap': True,
      'animation': {
          'defer': 5
      },
      'background_color': {
          'linearGradient': {
              'x1': 0.123,
              'x2': 0.234,
              'y1': 0.345,
              'y2': 0.456
          },
          'stops': [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      'border_color': '#999999',
      'border_radius': 24,
      'border_width': 1,
      'class_name': 'some-class-name',
      'color': '#000000',
      'crop': True,
      'defer': False,
      'enabled': True,
      'filter': {
          'operator': '>=',
          'property': 'some_property',
          'value': 123
      },
      'format': 'some format',
      'formatter': """function() { return true; }""",
      'inside': True,
      'null_format': 'some format',
      'null_formatter': """function() { return true; }""",
      'overflow': 'none',
      'padding': 12,
      'position': 'center',
      'rotation': 0,
      'shadow': False,
      'shape': 'rect',
      'style': 'style goes here',
      'use_html': False,
      'vertical_align': 'top',
      'x': 10,
      'y': 20,
      'z': 0
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_NodeDataLabel__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_NodeDataLabel__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_NodeDataLabel_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_NodeDataLabel_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/data_labels/02.js', False, None),

    ('utility_classes/data_labels/error-03.js', False, (errors.HighchartsValueError,
                                                        errors.HighchartsParseError,
                                                        JSONDecodeError,
                                                        TypeError,
                                                        ValueError)),

    ('utility_classes/data_labels/02.js', True, None),

    ('utility_classes/data_labels/error-03.js', True, (errors.HighchartsValueError,
                                                       errors.HighchartsParseError,
                                                       JSONDecodeError,
                                                       TypeError,
                                                       ValueError)),
])
def test_NodeDataLabel_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


STANDARD_PARAMS_3 = [
    ({}, None),
    ({
      'align': 'center',
      'allow_overlap': True,
      'animation': {
          'defer': 5
      },
      'background_color': {
          'linearGradient': {
              'x1': 0.123,
              'x2': 0.234,
              'y1': 0.345,
              'y2': 0.456
          },
          'stops': [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      'border_color': '#999999',
      'border_radius': 24,
      'border_width': 1,
      'class_name': 'some-class-name',
      'color': '#000000',
      'crop': True,
      'defer': False,
      'enabled': True,
      'filter': {
          'operator': '>=',
          'property': 'some_property',
          'value': 123
      },
      'format': 'some format',
      'formatter': """function() { return true; }""",
      'inside': True,
      'overflow': 'none',
      'padding': 12,
      'position': 'center',
      'rotation': 0,
      'rotation_mode': 'circular',
      'shadow': False,
      'shape': 'rect',
      'style': 'style goes here',
      'use_html': False,
      'vertical_align': 'top',
      'x': 10,
      'y': 20,
      'z': 0
    }, None),
    
    ({
      'align': 'center',
      'allow_overlap': True,
      'animation': {
          'defer': 5
      },
      'background_color': {
          'linearGradient': {
              'x1': 0.123,
              'x2': 0.234,
              'y1': 0.345,
              'y2': 0.456
          },
          'stops': [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      'border_color': '#999999',
      'border_radius': 24,
      'border_width': 1,
      'class_name': 'some-class-name',
      'color': '#000000',
      'crop': True,
      'defer': False,
      'enabled': True,
      'filter': {
          'operator': '>=',
          'property': 'some_property',
          'value': 123
      },
      'format': 'some format',
      'formatter': """function() { return true; }""",
      'inside': True,
      'overflow': 'none',
      'padding': 12,
      'position': 'center',
      'rotation': 0,
      'rotation_mode': 'invalid-value',
      'shadow': False,
      'shape': 'rect',
      'style': 'style goes here',
      'use_html': False,
      'vertical_align': 'top',
      'x': 10,
      'y': 20,
      'z': 0
    }, errors.HighchartsValueError),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_SunburstDataLabel__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_SunburstDataLabel__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_SunburstDataLabel_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_SunburstDataLabel_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/data_labels/03.js', False, None),

    ('utility_classes/data_labels/error-03.js', False, (errors.HighchartsValueError,
                                                        errors.HighchartsParseError,
                                                        JSONDecodeError,
                                                        TypeError,
                                                        ValueError)),

    ('utility_classes/data_labels/03.js', True, None),

    ('utility_classes/data_labels/error-03.js', True, (errors.HighchartsValueError,
                                                       errors.HighchartsParseError,
                                                       JSONDecodeError,
                                                       TypeError,
                                                       ValueError)),
])
def test_SunburstDataLabel_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)
