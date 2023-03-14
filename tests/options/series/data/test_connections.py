"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.series.data.connections import ConnectionBase as cls
from highcharts_core.options.series.data.connections import ConnectionData as cls2
from highcharts_core.options.series.data.connections import WeightedConnectionData as cls3
from highcharts_core.options.series.data.connections import OutgoingWeightedConnectionData as cls4
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here'
    }, None),
    # + DataBase
    ({
      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here',

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
def test_ConnectionBase__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ConnectionBase__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ConnectionBase_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ConnectionBase_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/data/connections/01.js', False, None),

    ('series/data/connections/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/data/connections/01.js', True, None),

    ('series/data/connections/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_ConnectionBase_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


## NEXT CLASS

STANDARD_PARAMS_2 = [
    ({}, None),
    ({
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
    }, None),
    # + ConnectionBase
    ({
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

      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here'
    }, None),
    # + DataBase
    ({
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

      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here',

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_ConnectionData__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_ConnectionData__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_ConnectionData_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_ConnectionData_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/data/connections/02.js', False, None),

    ('series/data/connections/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/data/connections/02.js', True, None),

    ('series/data/connections/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_ConnectionData_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


## NEXT CLASS

STANDARD_PARAMS_3 = [
    ({}, None),
    ({
      'weight': 0.75
    }, None),
    # + ConnectionData
    ({
      'weight': 0.75,

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
    }, None),
    # + ConnectionBase
    ({
      'weight': 0.75,

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

      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here'
    }, None),
    # + DataBase
    ({
      'weight': 0.75,

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

      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here',

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_WeightedConnectionData__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_WeightedConnectionData__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_WeightedConnectionData_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_WeightedConnectionData_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/data/connections/03.js', False, None),

    ('series/data/connections/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/data/connections/03.js', True, None),

    ('series/data/connections/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_WeightedConnectionData_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


## NEXT CLASS

STANDARD_PARAMS_4 = [
    ({}, None),
    ({
      'outgoing': True
    }, None),
    # + WeightedConnectionData
    ({
      'outgoing': True,

      'weight': 0.75
    }, None),
    # + ConnectionData
    ({
      'outgoing': True,

      'weight': 0.75,

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
    }, None),
    # + ConnectionBase
    ({
      'outgoing': True,

      'weight': 0.75,

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

      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here'
    }, None),
    # + DataBase
    ({
      'outgoing': True,

      'weight': 0.75,

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

      'from_': 'some-id-goes-here',
      'to': 'some-id-goes-here',

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_4)
def test_OutgoingWeightedConnectionData__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_4)
def test_OutgoingWeightedConnectionData__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_4)
def test_OutgoingWeightedConnectionData_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_4)
def test_OutgoingWeightedConnectionData_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/data/connections/04.js', False, None),

    ('series/data/connections/04.js', True, None),

])
def test_OutgoingWeightedConnectionData_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)
