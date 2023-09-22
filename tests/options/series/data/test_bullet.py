"""Tests for ``highcharts.no_data``."""

import pytest

import datetime
from json.decoder import JSONDecodeError

from highcharts_core.options.series.data.bullet import BulletData as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'target': 123,
      'target_options': {
          'borderColor': '#999',
          'borderRadius': 2,
          'borderWidth': 1,
          'color': '#ccc',
          'height': 12,
          'width': '5%'
      },

      'border_color': '#ccc',
      'border_width': 2,
      'dash_style': 'Solid',
      'point_width': 12
    }, None),
    # Categorical X Value
    ({
      'target': 123,
      'target_options': {
          'borderColor': '#999',
          'borderRadius': 2,
          'borderWidth': 1,
          'color': '#ccc',
          'height': 12,
          'width': '5%'
      },

      'border_color': '#ccc',
      'border_width': 2,
      'dash_style': 'Solid',
      'point_width': 12,

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
      'drag_drop': {
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
      'y': 123,
      'name': 'some category'
    }, None),
    # + DataBase options
    # Categorical X Value
    ({
      'target': 123,
      'target_options': {
          'borderColor': '#999',
          'borderRadius': 2,
          'borderWidth': 1,
          'color': '#ccc',
          'height': 12,
          'width': '5%'
      },
      
      'border_color': '#ccc',
      'border_width': 2,
      'dash_style': 'Solid',
      'point_width': 12,

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
      'drag_drop': {
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
      'y': 123,

      'accessibility': {
          'description': 'Some description goes here',
          'enabled': True
      },
      'class_name': 'some-class-name',
      'color': '#ccc',
      'color_index': 2,
      'custom': {
          'some_key': 123,
          'other_key': 456
      },
      'description': 'Some description goes here',
      'events': {
        'click': """function(event) { return true; }""",
        'drag': """function(event) { return true; }""",
        'drop': """function(event) { return true; }""",
        'mouseOut': """function(event) { return true; }"""
      },
      'id': 'some-id-goes-here',
      'label_rank': 3,
      'name': 'Some Name Goes here',
      'selected': False
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_BulletData__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_BulletData__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BulletData_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BulletData_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/data/bullet/01.js', False, None),

    ('series/data/bullet/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/data/bullet/01.js', True, None),

    ('series/data/bullet/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_BulletData_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


utc_now = datetime.datetime.utcnow()
today = datetime.date.today()


@pytest.mark.parametrize('input_array, set_props, expected_type, expected', [
    ([], {}, list, []),
    ([[321, 123, 456], [123, 789, 123]], {}, list, [[321, 123, 456], [123, 789, 123]]),
    ([[123, 456], [789, 123]], {}, list, [[123, 456], [789, 123]]),
    ([['A', 123, 456], ['B', 321, 123]], {}, list, [['A', 123, 456], ['B', 321, 123]]),
    ([[utc_now, 123, 456], [utc_now, 321, 123]], {}, list, [[utc_now, 123, 456], [utc_now, 321, 123]]),
    ([[today, 123, 456], [today, 321, 123]], {}, list, [[today, 123, 456], [today, 321, 123]]),
    
    ([[123, 456], [789, 123]], {'id': 'some_id'}, dict, None),
])
def test_BulletData_to_array(input_array, set_props, expected_type, expected):
    iterable = cls.from_array(input_array)
    for data_point in iterable:
        for key in set_props:
            setattr(data_point, key, set_props[key])
    
    results = []
    for data_point in iterable:
        result = data_point.to_array()
        assert isinstance(result, expected_type) is True
        results.append(result)
        
    if expected_type == list:
        assert results == expected
