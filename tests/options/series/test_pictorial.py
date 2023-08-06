"""Tests for ``highcharts.no_data``."""

import pytest
import datetime

from json.decoder import JSONDecodeError

from highcharts_core.options.series.pictorial import PictorialSeries as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'data': [
          {
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
            'name': 'some category',
          },
          {
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
            'x': datetime.datetime(2022, 7, 26, 0, 4, 0),
            'y': 123
          },
          {
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
            'x': datetime.date(2022, 7, 26),
            'y': 123
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
    }, None),
    ({
      'data': [
          {
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
          },
          {
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
            'x': datetime.datetime(2022, 7, 26, 0, 4, 0),
            'y': 123
          },
          {
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
            'x': datetime.date(2022, 7, 26),
            'y': 123
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
      'paths': {
          'definition': None,
          'max': 123
      },
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_PictorialSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_PictorialSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_PictorialSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_PictorialSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/pictorial/01.js', False, None),

    ('series/pictorial/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/pictorial/01.js', True, None),

    ('series/pictorial/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_PictorialSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
