"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.clusters import ClusterOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'allow_overlap': True,
      'animation': {
          'defer': 5
      },
      'data_labels': {
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
      'drill_to_cluster': True,
      'enabled': True,
      'events': {
        'drillToCluster': """function(event) { return true; }"""
      },
      'layout_algorithm': {
          'distance': '20%',
          'gridSize': 123,
          'iterations': 5,
          'kmeansThreshold': 1000
      },
      'marker': {
        'fillColor': '#cccccc',
        'enabled': True,
        'height': 24,
        'lineWidth': 2,
        'radius': 2,
        'states': {
            'hover': {
                'enabled': True
            }
        },
        'symbol': 'circle',
        'width': 48
      },
      'minimum_cluster_size': 5,
      'states': {
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
      },
      'zones': [
          {
           'className': 'classname-1',
           'from': 0,
           'marker': {
             'enabled': True,
             'fillColor': '#cccccc',
             'height': 24,
             'lineWidth': 2,
             'radius': 2,
             'states': {
                 'hover': {
                     'enabled': True
                 }
             },
             'symbol': 'circle',
             'width': 48
           },
           'to': 123
          },
          {
           'className': 'classname-1',
           'from': 0,
           'marker': {
             'enabled': True,
             'fillColor': '#cccccc',
             'height': 24,
             'lineWidth': 2,
             'radius': 2,
             'states': {
                 'hover': {
                     'enabled': True
                 }
             },
             'symbol': 'circle',
             'width': 48
           },
           'to': 123
          },
          {
           'className': 'classname-1',
           'from': 0,
           'marker': {
             'enabled': True,
             'fillColor': '#cccccc',
             'height': 24,
             'lineWidth': 2,
             'radius': 2,
             'states': {
                 'hover': {
                     'enabled': True
                 }
             },
             'symbol': 'circle',
             'width': 48
           },
           'to': 123
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
    ('utility_classes/clusters/01.js', False, None),

    ('utility_classes/clusters/error-01.js', False, (errors.HighchartsValueError,
                                                     errors.HighchartsParseError,
                                                     JSONDecodeError,
                                                     TypeError,
                                                     ValueError)),

    ('utility_classes/clusters/01.js', True, None),

    ('utility_classes/clusters/error-01.js', True, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
