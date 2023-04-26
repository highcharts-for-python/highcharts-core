"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.series.treegraph import TreegraphSeries as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'data': [
          {
            'colorValue': 2,
            'dataLabels': {
              'align': 'center',
              'allowOverlap': True,
              'animation': {
                  'defer': 5
              },
              'backgroundColor': {
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
              'borderColor': '#999999',
              'borderRadius': 24,
              'borderWidth': 1,
              'className': 'some-class-name',
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
              'nullFormat': 'some format',
              'nullFormatter': """function() { return true; }""",
              'overflow': 'none',
              'padding': 12,
              'position': 'center',
              'rotation': 0,
              'shadow': False,
              'shape': 'rect',
              'style': 'style goes here',
              'useHTML': False,
              'verticalAlign': 'top',
              'x': 10,
              'y': 20,
              'z': 0
            },
            'dragDrop': {
                'draggableX': True,
                'draggableY': True,
                'dragHandle': {
                    'className': 'draghandle-classname-goes-here',
                    'color': '#ccc',
                    'cursor': 'alias',
                    'lineColor': '#ddd',
                    'lineWidth': 2,
                    'pathFormatter': """function() { return true; }""",
                    'zIndex': 10
                },
                'dragMaxX': 3456,
                'dragMaxY': 6532,
                'dragMinX': 123,
                'dragMinY': 321,
                'dragPrecisionX': 5,
                'dragPrecisionY': 5,
                'dragSensitivity': 2,
                'groupBy': 'some-property-name',
                'guideBox': {
                    'default': {
                        'className': 'some-classname-goes-here',
                        'color': '#999',
                        'cursor': 'pointer',
                        'lineColor': '#ccc',
                        'lineWidth': 2,
                        'zIndex': 100
                    }
                },
                'liveRedraw': True
            },
            'drilldown': 'some-id-goes-here',
            'parent': 'some-id-goes-here',
          }
      ]
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
    ('series/treegraph/01.js', False, None),
    ('series/treegraph/02.js', False, None),

    ('series/treegraph/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/treegraph/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/treegraph/01.js', True, None),
    ('series/treegraph/02.js', True, None),

    ('series/treegraph/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/treegraph/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
