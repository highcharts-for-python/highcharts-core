"""Tests for ``highcharts.no_data``."""

import pytest

import datetime
from json.decoder import JSONDecodeError

from validator_collection import checkers

from highcharts_core.options.series.area import AreaSeries as cls
from highcharts_core.options.series.area import AreaRangeSeries as cls2
from highcharts_core.options.series.area import AreaSplineSeries as cls3
from highcharts_core.options.series.area import AreaSplineRangeSeries as cls4
from highcharts_core.options.series.area import LineSeries as cls5
from highcharts_core.options.series.area import StreamGraphSeries as cls6
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, run_pandas_tests

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
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3
    }, None),
    # + AreaOptions
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
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3,

      'fill_color': '#ccc',
      'fill_opacity': 0.7,
      'line_color': {
          'radialGradient': {
              'cx': 0.123,
              'cy': 0.456,
              'r': 0.789
          },
          'stops': [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      'negative_fill_color': '#ccc',
      'track_by_area': True
    }, None),
    # + Series + Generic Options
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
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3,

      'fill_color': '#ccc',
      'fill_opacity': 0.7,
      'line_color': {
          'radialGradient': {
              'cx': 0.123,
              'cy': 0.456,
              'r': 0.789
          },
          'stops': [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      'negative_fill_color': '#ccc',
      'track_by_area': True,

      'animation_limit': 10,
      'boost_blending': '#ccc',
      'boost_threshold': 1234,
      'color_axis': 1,
      'color_index': 5,
      'color_key': 'some-key-value',
      'connect_ends': True,
      'connect_nulls': True,
      'crisp': True,
      'crop_threshold': 123,
      'data_sorting': {
          'enabled': True,
          'matchByName': True,
          'sortKey': 'some-key-value'
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
      'find_nearest_point_by': 'x',
      'get_extremes_from_all': True,
      'linecap': 'round',
      'line_width': 2,
      'negative_color': '#fff',
      'point_interval': 5,
      'point_interval_unit': 'weeks',
      'point_placement': 'on',
      'point_start': 12,
      'relative_x_value': True,
      'shadow': False,
      'soft_threshold': True,
      'stacking': 'normal',
      'step': 'left',
      'zone_axis': 'y',
      'zones': [
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          }
      ],

      'accessibility': {
          'description': 'Description goes here',
          'enabled': True,
          'exposeAsGroupOnly': True,
          'keyboardNavigation': {
              'enabled': True
          },
          'point': {
              'dateFormat': 'format string',
              'dateFormatter': """function() { return true; }""",
              'describeNull': False,
              'descriptionFormatter': """function() { return true; }""",
              'valueDecimals': 2,
              'valueDescriptionFormat': 'format string',
              'valuePrefix': '$',
              'valueSuffix': 'USD'
          },
      },
      'allow_point_select': True,
      'animation': {
          'defer': 5
      },
      'class_name': 'some-class-name',
      'clip': False,
      'color': '#fff',
      'cursor': 'alias',
      'custom': {
          'item1': 'some value',
          'item2': 'some value'
      },
      'dash_style': 'Dash',
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
      'description': 'Description goes here',
      'enable_mouse_tracking': True,
      'events': {
        'afterAnimate': """function(event) { return true; }""",
        'click': """function(event) { return true; }""",
        'hide': """function(event) { return true; }""",
        'mouseOut': """function(event) { return true; }""",
        'show': """function(event) { return true; }"""
      },
      'include_in_data_export': True,
      'keys': [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      'label': {
          'boxesToAvoid': [
              {
               'bottom': 12,
               'left': -46,
               'right': 84,
               'top': 24
              },
              {
               'bottom': 48,
               'left': -46,
               'right': 84,
               'top': 86
              }
          ],
          'connectorAllowed': True,
          'connectorNeighbourDistance': 12,
          'enabled': True,
          'format': 'format string',
          'formatter': """function() { return true; }""",
          'maxFontSize': 18,
          'minFontSize': 6,
          'onArea': False,
          'style': 'some style string'
      },
      'linked_to': 'some_id',
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
      'on_point': {
          'connectorOptions': {
              'dashstyle': 'Dash',
              'stroke': '#ccc',
              'width': 2
          },
          'id': 'some-id',
          'position': {
              'align': 'left',
              'verticalAlign': 'top',
              'x': 15,
              'y': -46
          }
      },
      'opacity': 0.2,
      'point': {
          'events': {
            'click': """function(event) { return true; }""",
            'drag': """function(event) { return true; }""",
            'drop': """function(event) { return true; }""",
            'mouseOut': """function(event) { return true; }"""
          }
      },
      'point_description_formatter': """function (point) { return true; }""",
      'selected': False,
      'show_checkbox': True,
      'show_in_legend': True,
      'skip_keyboard_navigation': False,
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
      'sticky_tracking': True,
      'threshold': 123,
      'tooltip': {
        'animation': True,
        'backgroundColor': '#ccc',
        'borderColor': '#999',
        'borderRadius': 4,
        'borderWidth': 1,
        'className': 'some-class-name',
        'clusterFormat': 'format string',
        'dateTimeLabelFormats': {
          'day': 'test',
          'hour': 'test',
          'millisecond': 'test',
          'minute': 'test',
          'month': 'test',
          'second': 'test',
          'week': 'test',
          'year': 'test'
        },
        'distance': 12,
        'enabled': True,
        'followPointer': True,
        'followTouch_move': True,
        'footerFormat': 'format string',
        'formatter': """function() { return true; }""",
        'headerFormat': 'format string',
        'headerShape': 'circle',
        'hideDelay': 3,
        'nullFormat': 'format string',
        'nullFormatter': """function() { return true; }""",
        'outside': False,
        'padding': 6,
        'pointFormat': 'format string',
        'pointFormatter': """function() { return true; }""",
        'positioner': """function() { return true; }""",
        'shadow': False,
        'shape': 'rect',
        'shared': False,
        'snap': 4,
        'split': False,
        'stickOnContact': True,
        'style': 'style string goes here',
        'useHTML': False,
        'valueDecimals': 2,
        'valuePrefix': '$',
        'valueSuffix': ' USD',
        'xDateFormat': 'format string'
       },
      'turbo_threshold': 456,
      'visible': True
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AreaSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AreaSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AreaSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AreaSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/area/01.js', False, None),
    ('series/area/02.js', False, None),
    ('series/area/03.js', False, None),

    ('series/area/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/area/01.js', True, None),
    ('series/area/02.js', True, None),
    ('series/area/03.js', True, None),

    ('series/area/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_AreaSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


@pytest.mark.parametrize('filename, target_type, as_cls, error', [
    ('series/area/01.js', 'line', False, None),
    ('series/area/02.js', 'line', False, None),
    ('series/area/03.js', 'line', False, None),

    ('series/area/01.js', 'line', True, None),
    ('series/area/02.js', 'line', True, None),
    ('series/area/03.js', 'line', True, None),

    ('series/area/01.js', 'not a series type', False, ValueError),
    ('series/area/01.js', 123, False, ValueError),

])
def test_convert_to(input_files, filename, target_type, as_cls, error):
    input_file = check_input_file(input_files, filename)
    if not error:
        from highcharts_core.options.series.series_generator import SERIES_CLASSES

        original = cls.from_js_literal(input_file)

        if isinstance(target_type, str):
            target_type_cls = SERIES_CLASSES.get(target_type)
            target_type_name = target_type
        else:
            target_type_cls = target_type
            target_type_name = target_type.__name__

        if as_cls:
            target_type = target_type_cls
        else:
            target_type = target_type_name
        
        converted = original.convert_to(target_type)
        assert converted is not None
        assert isinstance(converted, cls)
        assert isinstance(converted, target_type_cls)
#### NEXT CLASS

STANDARD_PARAMS_2 = [
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
            'high': 123,
            'low': 12,
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
            'high': 123,
            'low': 12,
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

            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
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
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3
    }, None),
    # + AreaOptions
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
            'high': 123,
            'low': 12,
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
            'x': 'some category'
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
            'high': 123,
            'low': 12,
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

            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
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
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3,

      'fill_color': '#ccc',
      'fill_opacity': 0.7,
      'line_color': {
          'radialGradient': {
              'cx': 0.123,
              'cy': 0.456,
              'r': 0.789
          },
          'stops': [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      'negative_fill_color': '#ccc',
      'track_by_area': True
    }, None),
    # + Series + Generic Options
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
            'high': 123,
            'low': 12,
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
            'high': 123,
            'low': 12,
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

            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
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
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3,

      'fill_color': '#ccc',
      'fill_opacity': 0.7,
      'line_color': {
          'radialGradient': {
              'cx': 0.123,
              'cy': 0.456,
              'r': 0.789
          },
          'stops': [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      'negative_fill_color': '#ccc',
      'track_by_area': True,

      'animation_limit': 10,
      'boost_blending': '#ccc',
      'boost_threshold': 1234,
      'color_axis': 1,
      'color_index': 5,
      'color_key': 'some-key-value',
      'connect_ends': True,
      'connect_nulls': True,
      'crisp': True,
      'crop_threshold': 123,
      'data_sorting': {
          'enabled': True,
          'matchByName': True,
          'sortKey': 'some-key-value'
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
      'find_nearest_point_by': 'x',
      'get_extremes_from_all': True,
      'linecap': 'round',
      'line_width': 2,
      'negative_color': '#fff',
      'point_interval': 5,
      'point_interval_unit': 'weeks',
      'point_placement': 'on',
      'point_start': 12,
      'relative_x_value': True,
      'shadow': False,
      'soft_threshold': True,
      'stacking': 'normal',
      'step': 'left',
      'zone_axis': 'y',
      'zones': [
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          }
      ],

      'accessibility': {
          'description': 'Description goes here',
          'enabled': True,
          'exposeAsGroupOnly': True,
          'keyboardNavigation': {
              'enabled': True
          },
          'point': {
              'dateFormat': 'format string',
              'dateFormatter': """function() { return true; }""",
              'describeNull': False,
              'descriptionFormatter': """function() { return true; }""",
              'valueDecimals': 2,
              'valueDescriptionFormat': 'format string',
              'valuePrefix': '$',
              'valueSuffix': 'USD'
          },
      },
      'allow_point_select': True,
      'animation': {
          'defer': 5
      },
      'class_name': 'some-class-name',
      'clip': False,
      'color': '#fff',
      'cursor': 'alias',
      'custom': {
          'item1': 'some value',
          'item2': 'some value'
      },
      'dash_style': 'Dash',
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
      'description': 'Description goes here',
      'enable_mouse_tracking': True,
      'events': {
        'afterAnimate': """function(event) { return true; }""",
        'click': """function(event) { return true; }""",
        'hide': """function(event) { return true; }""",
        'mouseOut': """function(event) { return true; }""",
        'show': """function(event) { return true; }"""
      },
      'include_in_data_export': True,
      'keys': [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      'label': {
          'boxesToAvoid': [
              {
               'bottom': 12,
               'left': -46,
               'right': 84,
               'top': 24
              },
              {
               'bottom': 48,
               'left': -46,
               'right': 84,
               'top': 86
              }
          ],
          'connectorAllowed': True,
          'connectorNeighbourDistance': 12,
          'enabled': True,
          'format': 'format string',
          'formatter': """function() { return true; }""",
          'maxFontSize': 18,
          'minFontSize': 6,
          'onArea': False,
          'style': 'some style string'
      },
      'linked_to': 'some_id',
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
      'on_point': {
          'connectorOptions': {
              'dashstyle': 'Dash',
              'stroke': '#ccc',
              'width': 2
          },
          'id': 'some-id',
          'position': {
              'align': 'left',
              'verticalAlign': 'top',
              'x': 15,
              'y': -46
          }
      },
      'opacity': 0.2,
      'point': {
          'events': {
            'click': """function(event) { return true; }""",
            'drag': """function(event) { return true; }""",
            'drop': """function(event) { return true; }""",
            'mouseOut': """function(event) { return true; }"""
          }
      },
      'point_description_formatter': """function (point) { return true; }""",
      'selected': False,
      'show_checkbox': True,
      'show_in_legend': True,
      'skip_keyboard_navigation': False,
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
      'sticky_tracking': True,
      'threshold': 123,
      'tooltip': {
        'animation': True,
        'backgroundColor': '#ccc',
        'borderColor': '#999',
        'borderRadius': 4,
        'borderWidth': 1,
        'className': 'some-class-name',
        'clusterFormat': 'format string',
        'dateTimeLabelFormats': {
          'day': 'test',
          'hour': 'test',
          'millisecond': 'test',
          'minute': 'test',
          'month': 'test',
          'second': 'test',
          'week': 'test',
          'year': 'test'
        },
        'distance': 12,
        'enabled': True,
        'followPointer': True,
        'followTouch_move': True,
        'footerFormat': 'format string',
        'formatter': """function() { return true; }""",
        'headerFormat': 'format string',
        'headerShape': 'circle',
        'hideDelay': 3,
        'nullFormat': 'format string',
        'nullFormatter': """function() { return true; }""",
        'outside': False,
        'padding': 6,
        'pointFormat': 'format string',
        'pointFormatter': """function() { return true; }""",
        'positioner': """function() { return true; }""",
        'shadow': False,
        'shape': 'rect',
        'shared': False,
        'snap': 4,
        'split': False,
        'stickOnContact': True,
        'style': 'style string goes here',
        'useHTML': False,
        'valueDecimals': 2,
        'valuePrefix': '$',
        'valueSuffix': ' USD',
        'xDateFormat': 'format string'
       },
      'turbo_threshold': 456,
      'visible': True
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_AreaRangeSeries__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_AreaRangeSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_AreaRangeSeries_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_AreaRangeSeries_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/area/04.js', False, None),
    ('series/area/05.js', False, None),
    ('series/area/06.js', False, None),

    ('series/area/error-04.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/area/04.js', True, None),
    ('series/area/05.js', True, None),
    ('series/area/06.js', True, None),

    ('series/area/error-04.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_AreaRangeSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AreaSplineSeries__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AreaSplineSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AreaSplineSeries_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AreaSplineSeries_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/area/01.js', False, None),
    ('series/area/02.js', False, None),
    ('series/area/03.js', False, None),

    ('series/area/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/area/01.js', True, None),
    ('series/area/02.js', True, None),
    ('series/area/03.js', True, None),

    ('series/area/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_AreaSplineSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_AreaSplineRangeSeries__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_AreaSplineRangeSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_AreaSplineRangeSeries_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_AreaSplineRangeSeries_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/area/04.js', False, None),
    ('series/area/05.js', False, None),
    ('series/area/06.js', False, None),

    ('series/area/error-04.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/area/04.js', True, None),
    ('series/area/05.js', True, None),
    ('series/area/06.js', True, None),

    ('series/area/error-04.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_AreaSplineRangeSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)

#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LineSeries__init__(kwargs, error):
    Class__init__(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LineSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LineSeries_from_dict(kwargs, error):
    Class_from_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LineSeries_to_dict(kwargs, error):
    Class_to_dict(cls5, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/area/01.js', False, None),
    ('series/area/02.js', False, None),
    ('series/area/03.js', False, None),

    ('series/area/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/area/01.js', True, None),
    ('series/area/02.js', True, None),
    ('series/area/03.js', True, None),

    ('series/area/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_LineSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls5, input_files, filename, as_file, error)


@pytest.mark.parametrize('filename, error', [
    ('test-data-files/nst-est2019-01.csv', None),
])
def test_LineSeries_from_pandas_in_rows(run_pandas_tests, input_files, filename, error):
    if not run_pandas_tests:
        return

    import pandas
    
    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    print(df)
    
    if not error:
        result = cls5.from_pandas_in_rows(df)
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == len(df)
        for series in result:
            assert isinstance(series, cls5)
            assert series.data is not None
            assert len(series.data) == len(df.columns)
    else:
        with pytest.raises(error):
            result = cls5.from_pandas_in_rows(df)


def prep_df(df):
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    
    return df


def reduce_to_two_columns(df):
    df = df[['Geographic Area', '2010']]
    
    return df


@pytest.mark.parametrize('filename, kwargs, pre_test_df_func, expected_series, expected_data_points, error', [
    # SCENARIO 0: Series in Rows
    ('test-data-files/nst-est2019-01.csv',
     {
         'series_in_rows': True
     },
     prep_df,
     57,
     10,
     None),
    
    # SCENARIO 1a: Has Property Map, Single Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'name': 'Geographic Area',
         },
         'series_in_rows': False
     },
     None,
     1,
     57,
     None),

    # SCENARIO 1b: Has Property Map, Multiple Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'x': ['Geographic Area', '2010']
         },
         'series_in_rows': False
     },
     None,
     2,
     57,
     None),
    
    # SCENARIO 2a: Single Property in KWARGS
    ('test-data-files/nst-est2019-01.csv',
     {
         'x': 'Geographic Area',
         'y': '2010'
     },
     None,
     1,
     57,
     None),
    
    # SCENARIO 3a: Exact Match on Column Count
    ('test-data-files/nst-est2019-01.csv',
     {},
     reduce_to_two_columns,
     1,
     57,
     None),
    
    # SCENARIO 3b: Multiple Series, Multipled Columns
    ('test-data-files/nst-est2019-01.csv',
     {},
     prep_df,
     10,
     57,
     None),

    # SCENARIO 4: Mismatched Columns
    # NOTE: On SeriesBase, this will actually return one series per column.
    # This is because SeriesBase supports 1D arrays.
    ('test-data-files/nst-est2019-01.csv',
     {},
     None,
     11,
     57,
     TypeError),
    
])
def test_LineSeries_from_pandas(run_pandas_tests,
                                input_files, 
                                filename, 
                                kwargs, 
                                pre_test_df_func, 
                                expected_series, 
                                expected_data_points, 
                                error):
    if not run_pandas_tests:
        return

    import pandas

    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    if pre_test_df_func:
        df = pre_test_df_func(df)
    print(df)

    if not error:
        result = cls5.from_pandas(df, **kwargs)
        assert result is not None
        if expected_series > 1:
            assert isinstance(result, list)
            assert len(result) == expected_series
            for series in result:
                assert isinstance(series, cls)
                assert series.data is not None
                assert len(series.data) == expected_data_points
        else:
            assert isinstance(result, cls)
            assert result.data is not None
            assert len(result.data) == len(df)
    else:
        with pytest.raises(error):
            result = cls5.from_pandas(df, **kwargs)


@pytest.mark.parametrize('kwargs, error', [
    ({
        'as_string_or_file': "'Date','HeadCount'\r\n'01/01/2023','2'\r\n'01/02/2023','4'\r\n'01/03/2023','8'",
        'property_column_map': {'x': 'Date', 'y': 'HeadCount', 'id': 'Date'}
     }, None),
    ({
        'as_string_or_file': "Date,HeadCount\r\n01/01/2023,2\r\n01/02/2023,4\r\n01/03/2023,8",
        'property_column_map': {'x': 'Date', 'y': 'HeadCount', 'id': 'Date'}
     }, None),

])
def test_bugfix32_LineSeries_from_csv(kwargs, error):
    if not error:
        result = cls5.from_csv(**kwargs)
        assert result is not None
        assert isinstance(result, cls5) is True
        assert result.data is not None
        for item in result.data:
            assert item.x is not None or item.name is not None
            assert item.y is not None
            assert item.id is not None


@pytest.mark.parametrize('filename, expected_series, expected_data_points, error', [
    ('test-data-files/nst-est2019-01.csv', 57, 10, None),
])
def test_LineSeries_from_csv_in_rows(input_files, filename, expected_series, expected_data_points, error):
    input_file = check_input_file(input_files, filename)
    if not error:
        result = cls5.from_csv_in_rows(input_file,
                                       wrapper_character = '"')
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == expected_series
        for series in result:
            assert isinstance(series, cls5)
            assert series.data is not None
            assert len(series.data) == expected_data_points
    else:
        with pytest.raises(error):
            result = cls5.from_pandas_in_rows(input_file)


@pytest.mark.parametrize('filename, property_map, kwargs, expected_series, expected_data_points, error', [
    ('test-data-files/nst-est2019-01.csv', 
     {}, 
     {
         'wrapper_character': '"'
     },
     10,
     57,
     None),
    ('test-data-files/nst-est2019-01.csv',
     {
         'name': 'Geographic Area',
         'x': 'Geographic Area',
         'y': '2010'
     },
     {
         'wrapper_character': '"'
     },
     1,
     57,
     None),

    # SCENARIO 0: Series in Rows
    ('test-data-files/nst-est2019-01.csv',
     {},
     {
         'wrapper_character': '"',
         'series_in_rows': True
     },
     57,
     10,
     None),
    
    # SCENARIO 1a: Has Property Map, Single Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'name': 'Geographic Area'
     },
     {
         'wrapper_character': '"',
         'series_in_rows': False
     },
     1,
     57,
     None),

    ('test-data-files/nst-est2019-01.csv',
     {
         'x': 'Geographic Area',
         'y': '2010'
     },
     {
         'wrapper_character': '"'
     },
     1,
     57,
     None),

    # SCENARIO 1b: Has Property Map, Multiple Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'x': ['Geographic Area', '2010']
     },
     {
         'series_in_rows': False,
         'wrapper_character': '"'
          },
     2,
     57,
     None),
    
    # SCENARIO 2a: Single Property in KWARGS
    ('test-data-files/nst-est2019-01.csv',
     {},
     {
         'wrapper_character': '"',
         'x': 'Geographic Area',
         'y': '2010'
     },
     1,
     57,
     None),
    
    # SCENARIO 3a: Exact Match on Column Count
    ('test-data-files/nst-est2019-01-reduced-to-two.csv',
     {},
     {
         'wrapper_character': '"'
     },
     1,
     57,
     None),
    
    # SCENARIO 3b: Multiple Series, Multipled Columns
    ('test-data-files/nst-est2019-01-removed-column.csv',
     {},
     {
         'wrapper_character': '"'
     },
     9,
     57,
     None),

    # SCENARIO 4: Mismatched Columns
    # NOTE: On SeriesBase, this will actually return one series per column.
    # This is because SeriesBase supports 1D arrays.
    ('test-data-files/nst-est2019-01.csv',
     {},
     {
         'wrapper_character': '"'
     },
     10,
     57,
     None),
    
])
def test_LineSeries_from_csv(input_files, filename, property_map, kwargs, expected_series, expected_data_points, error):
    input_file = check_input_file(input_files, filename)
    
    if not error:
        result = cls5.from_csv(input_file,
                               property_column_map = property_map,
                               **kwargs)
        assert result is not None
        if isinstance(result, list):
            assert len(result) == expected_series
            for series in result:
                assert isinstance(series, cls5)
                assert series.data is not None
                assert len(series.data) == expected_data_points
        else:
            assert isinstance(result, cls5)
            assert result.data is not None
            for item in result.data:
                for key in property_map:
                    if key == 'x':
                        x_value = getattr(item, 'x', None)
                        if x_value is None:
                            assert getattr(item, 'name', None) is not None
                    else:
                        assert getattr(item, key, None) is not None

    else:
        with pytest.raises(error):
            result = cls5.from_csv(input_file, 
                                   property_column_map = property_map,
                                   **kwargs)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_StreamGraphSeries__init__(kwargs, error):
    Class__init__(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_StreamGraphSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_StreamGraphSeries_from_dict(kwargs, error):
    Class_from_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_StreamGraphSeries_to_dict(kwargs, error):
    Class_to_dict(cls6, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/area/01.js', False, None),
    ('series/area/02.js', False, None),
    ('series/area/03.js', False, None),

    ('series/area/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/area/01.js', True, None),
    ('series/area/02.js', True, None),
    ('series/area/03.js', True, None),

    ('series/area/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/area/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_StreamGraphSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls6, input_files, filename, as_file, error)
