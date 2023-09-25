"""Tests for ``highcharts.no_data``."""

import pytest
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from json.decoder import JSONDecodeError
from validator_collection import checkers

from highcharts_core.options.series.bar import BaseBarSeries as cls
from highcharts_core.options.series.bar import BarSeries as cls2
from highcharts_core.options.series.bar import ColumnSeries as cls3
from highcharts_core.options.series.bar import ColumnPyramidSeries as cls4
from highcharts_core.options.series.bar import ColumnRangeSeries as cls5
from highcharts_core.options.series.bar import CylinderSeries as cls6
from highcharts_core.options.series.bar import VariwideSeries as cls7
from highcharts_core.options.series.bar import WaterfallSeries as cls8
from highcharts_core.options.series.bar import WindBarbSeries as cls9
from highcharts_core.options.series.bar import XRangeSeries as cls10
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal


STANDARD_PARAMS = [
    ({}, None),
    ({
      'data': [
          {
            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          },
          {
            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12,

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
    }, None),
    # + Options
    ({
      'data': [
          {
            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          },
          {
            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12,

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

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Series + Generic
    ({
      'data': [
          {
            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          },
          {
            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12,

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

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

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
def test_BaseBarSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_BaseBarSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BaseBarSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BaseBarSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/01.js', False, None),

    ('series/bar/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/bar/01.js', True, None),

    ('series/bar/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_BaseBarSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


# NEXT CLASS!

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_BarSeries__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_BarSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BarSeries_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BarSeries_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/01.js', False, None),

    ('series/bar/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/bar/01.js', True, None),

    ('series/bar/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_BarSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


@pytest.mark.parametrize('kwargs, name, expected, error', [
    ({'data': [[1, 2], [3, 4], [5, 6]]},
     'data', 
     cls2._data_point_class().from_array([[1, 2], [3, 4], [5, 6]]),
     None),
    ({'data': np.asarray([[1, 2], [3, 4], [5, 6]]) if HAS_NUMPY else [[1, 2], [3, 4], [5, 6]]},
     'data',
     cls2._data_collection_class().from_ndarray(np.asarray([[1, 2], [3, 4], [5, 6]])) if HAS_NUMPY else cls2._data_point_class().from_array([[1, 2], [3, 4], [5, 6]]),
     None),
    ({'data': [[1, 2], [3, 4], [5, 6]]},
     'x', 
     np.asarray([1, 3, 5]) if HAS_NUMPY else [1, 3, 5],
     None),
    ({'data': [[1, 2], [3, 4], [5, 6]]},
     'y', 
     np.asarray([2, 4, 6]) if HAS_NUMPY else [2, 4, 6],
     None),
    ({'data': np.asarray([[1, 2], [3, 4], [5, 6]]) if HAS_NUMPY else [[1, 2], [3, 4], [5, 6]]},
     'x', 
     np.asarray([1, 3, 5]) if HAS_NUMPY else [1, 3, 5],
     None),
    ({'data': np.asarray([[1, 2], [3, 4], [5, 6]]) if HAS_NUMPY else [[1, 2], [3, 4], [5, 6]]},
     'y', 
     np.asarray([2, 4, 6]) if HAS_NUMPY else [2, 4, 6],
     None),
])
def test_BarSeries__getattr__(kwargs, name, expected, error):
    if not error:
        obj = cls2(**kwargs)
        result = getattr(obj, name)
        if not checkers.is_type(expected, 'ndarray'):
            assert result == expected
        else:
            assert np.array_equiv(result, expected) is True
    else:
        with pytest.raises(error):
            obj = cls(**kwargs)
            result = getattr(obj, name)


@pytest.mark.parametrize('name, value, expected, error', [
    ('data',
     [[1, 2], [3, 4], [5, 6]],
     cls2._data_point_class().from_array([[1, 2], [3, 4], [5, 6]]),
     None),
    ('data', 
     np.asarray([[1, 2], [3, 4], [5, 6]]) if HAS_NUMPY else [[1, 2], [3, 4], [5, 6]],
     cls2._data_collection_class().from_ndarray(
         np.asarray([[1, 2], [3, 4], [5, 6]])
     ) if HAS_NUMPY else cls2._data_point_class().from_array([[1, 2], [3, 4], [5, 6]]),
     None),
    ('x',
     [1, 3, 5],
     np.asarray([1, 3, 5]) if HAS_NUMPY else [1, 3, 5],
     None),
    ('y',
     [2, 4, 6],
     np.asarray([2, 4, 6]) if HAS_NUMPY else [2, 4, 6],
     None),
    ('x',
     np.asarray([1, 3, 5]) if HAS_NUMPY else [1, 3, 5],
     np.asarray([1, 3, 5]) if HAS_NUMPY else [1, 3, 5],
     None),
    ('y',
     np.asarray([2, 4, 6]) if HAS_NUMPY else [2, 4, 6],
     np.asarray([2, 4, 6]) if HAS_NUMPY else [2, 4, 6],
     None),
])
def test_BarSeries__setattr__(name, value, expected, error):
    if not error:
        obj = cls()
        setattr(obj, name, value)
        result = getattr(obj, name)
        if not checkers.is_type(expected, 'ndarray') and name == 'data_points':
            assert len(result) == len(expected)
        elif not checkers.is_type(expected, 'ndarray'):
            assert result == expected
        else:
            assert np.array_equiv(result, expected) is True
    else:
        with pytest.raises(error):
            obj = cls()
            setattr(obj, name, value)
    

# NEXT CLASS!

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ColumnSeries__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ColumnSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ColumnSeries_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ColumnSeries_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/01.js', False, None),

    ('series/bar/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/bar/01.js', True, None),

    ('series/bar/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_ColumnSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


# NEXT CLASS!

STANDARD_PARAMS_4 = [
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
            'y': 123,
            'name': 'some category'
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
    # + Column Pyramid Options
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
            'y': 123,
            'name': 'some category'
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

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4
    }, None),
    # + Base Bar Options
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
            'y': 123,
            'name': 'some category'
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

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Base Bar + Series + Generic
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

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_4)
def test_ColumnPyramidSeries__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_4)
def test_ColumnPyramidSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_4)
def test_ColumnPyramidSeries_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_4)
def test_ColumnPyramidSeries_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/02.js', False, None),

    ('series/bar/02.js', True, None),

])
def test_ColumnPyramidSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)


# NEXT CLASS!

STANDARD_PARAMS_5 = [
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
      'z_index': 3,

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4
    }, None),
    # + Base Bar Options
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

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Base Bar + Series + Generic
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

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_5)
def test_ColumnRangeSeries__init__(kwargs, error):
    Class__init__(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_5)
def test_ColumnRangeSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_5)
def test_ColumnRangeSeries_from_dict(kwargs, error):
    Class_from_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_5)
def test_ColumnRangeSeries_to_dict(kwargs, error):
    Class_to_dict(cls5, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/03.js', False, None),

    ('series/bar/03.js', True, None),

])
def test_ColumnRangeSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls5, input_files, filename, as_file, error)


# NEXT CLASS!

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CylinderSeries__init__(kwargs, error):
    Class__init__(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CylinderSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CylinderSeries_from_dict(kwargs, error):
    Class_from_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CylinderSeries_to_dict(kwargs, error):
    Class_to_dict(cls6, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/01.js', False, None),

    ('series/bar/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/bar/01.js', True, None),

    ('series/bar/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_CylinderSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls6, input_files, filename, as_file, error)


# NEXT CLASS!

STANDARD_PARAMS_7 = [
    ({}, None),
    ({
      'data': [
          {
            'z': 456,

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
            'z': 456,

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
    }, None),
    # + Base Bar Options
    ({
      'data': [
          {
            'z': 456,

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
            'z': 456,

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

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Base Bar + Series + Generic
    ({
      'data': [
          {
            'z': 456,

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
            'z': 456,

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

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_7)
def test_VariwideSeries__init__(kwargs, error):
    Class__init__(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_7)
def test_VariwideSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_7)
def test_VariwideSeries_from_dict(kwargs, error):
    Class_from_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_7)
def test_VariwideSeries_to_dict(kwargs, error):
    Class_to_dict(cls7, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/04.js', False, None),
    ('series/bar/04.js', True, None),

])
def test_VariwideSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls7, input_files, filename, as_file, error)


# NEXT CLASS!

STANDARD_PARAMS_8 = [
    ({}, None),
    ({
      'data': [
          {
            'isIntermediateSum': True,
            'isSum': True
          },
          {
            'isIntermediateSum': True,
            'isSum': True
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
    }, None),
    # + Waterfall Options
    ({
      'data': [
          {
            'isIntermediateSum': True,
            'isSum': True
          },
          {
            'isIntermediateSum': True,
            'isSum': True
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

      'line_color': '#fff',
      'up_color': '#999'
    }, None),
    # + Base Bar Options
    ({
      'data': [
          {
            'isIntermediateSum': True,
            'isSum': True
          },
          {
            'isIntermediateSum': True,
            'isSum': True
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

      'line_color': '#fff',
      'up_color': '#999',

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Base Bar + Series + Generic
    ({
      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_8)
def test_WaterfallSeries__init__(kwargs, error):
    Class__init__(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_8)
def test_WaterfallSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_8)
def test_WaterfallSeries_from_dict(kwargs, error):
    Class_from_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_8)
def test_WaterfallSeries_to_dict(kwargs, error):
    Class_to_dict(cls8, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/05.js', False, None),
    ('series/bar/05.js', True, None),

])
def test_WaterfallSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls8, input_files, filename, as_file, error)


# NEXT CLASS!

STANDARD_PARAMS_9 = [
    ({}, None),
    ({
      'data': [
          {
           'direction': 45,
           'value': 123
          },
          {
           'direction': 45,
           'value': 123
          }
      ],
    }, None),
    # + Options
    ({
      'data': [
          {
           'direction': 45,
           'value': 123
          },
          {
           'direction': 45,
           'value': 123
          }
      ],

      'data_grouping': {
        'anchor': 'start',
        'approximation': 'windbarb',
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
        'enabled': True,
        'firstAnchor': 'start',
        'forced': True,
        'groupAll': True,
        'groupPixelWidth': 10,
        'lastAnchor': 'end',
        'units': [
            [
                'millisecond',
                [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
            ],
            [
                'second',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'minute',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'hour',
                [1, 2, 3, 4, 6, 8, 12]
            ],
            [
                'day',
                [1]
            ],
            [
                'week',
                [1]
            ],
            [
                'month',
                [1, 3, 6]
            ],
            [
                'year',
                None
            ]
        ]
      },
      'on_series': 'some-id-goes-here',
      'vector_length': 10,
      'x_offset': 5,
      'y_offset': 2
    }, None),
    # + Bar Options
    ({
      'data': [
          {
           'direction': 45,
           'value': 123
          },
          {
           'direction': 45,
           'value': 123
          }
      ],

      'data_grouping': {
        'anchor': 'start',
        'approximation': 'windbarb',
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
        'enabled': True,
        'firstAnchor': 'start',
        'forced': True,
        'groupAll': True,
        'groupPixelWidth': 10,
        'lastAnchor': 'end',
        'units': [
            [
                'millisecond',
                [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
            ],
            [
                'second',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'minute',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'hour',
                [1, 2, 3, 4, 6, 8, 12]
            ],
            [
                'day',
                [1]
            ],
            [
                'week',
                [1]
            ],
            [
                'month',
                [1, 3, 6]
            ],
            [
                'year',
                None
            ]
        ]
      },
      'on_series': 'some-id-goes-here',
      'vector_length': 10,
      'x_offset': 5,
      'y_offset': 2,

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4
    }, None),
    # + Base Bar Options
    ({
      'data': [
          {
           'direction': 45,
           'value': 123
          },
          {
           'direction': 45,
           'value': 123
          }
      ],

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Base Bar + Series + Generic
    ({
      'data': [
          {
           'direction': 45,
           'value': 123
          },
          {
           'direction': 45,
           'value': 123
          }
      ],

      'data_grouping': {
        'anchor': 'start',
        'approximation': 'windbarb',
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
        'enabled': True,
        'firstAnchor': 'start',
        'forced': True,
        'groupAll': True,
        'groupPixelWidth': 10,
        'lastAnchor': 'end',
        'units': [
            [
                'millisecond',
                [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
            ],
            [
                'second',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'minute',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'hour',
                [1, 2, 3, 4, 6, 8, 12]
            ],
            [
                'day',
                [1]
            ],
            [
                'week',
                [1]
            ],
            [
                'month',
                [1, 3, 6]
            ],
            [
                'year',
                None
            ]
        ]
      },
      'on_series': 'some-id-goes-here',
      'vector_length': 10,
      'x_offset': 5,
      'y_offset': 2,

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_9)
def test_WindbarbSeries__init__(kwargs, error):
    Class__init__(cls9, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_9)
def test_WindbarbSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls9, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_9)
def test_WindbarbSeries_from_dict(kwargs, error):
    Class_from_dict(cls9, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_9)
def test_WindbarbSeries_to_dict(kwargs, error):
    Class_to_dict(cls9, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/06.js', False, None),
    ('series/bar/06.js', True, None),

])
def test_WindbarbSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls9, input_files, filename, as_file, error)


# NEXT CLASS!

STANDARD_PARAMS_10 = [
    ({}, None),
    ({
      'data': [
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345
          },
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345
          },
      ]
    }, None),
    # + Options
    ({
      'data': [
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345,
          },
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345,
          }
      ],

      'group_z_padding': 4,
    }, None),
    # + Base Bar Options
    ({
      'data': [
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345
          },
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345
          },
      ],

      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Base Bar + Series + Generic
    ({
      'data': [
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345
          },
          {
           'partialFill': {
               'fill': '#ccc'
           },
           'x': 123,
           'x2': 345
          },
      ],

      'group_z_padding': 4,

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

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


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_10)
def test_XRangeSeries__init__(kwargs, error):
    Class__init__(cls10, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_10)
def test_XRangeSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls10, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_10)
def test_XRangeSeries_from_dict(kwargs, error):
    Class_from_dict(cls10, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_10)
def test_XRangeSeries_to_dict(kwargs, error):
    Class_to_dict(cls10, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bar/07.js', False, None),
    ('series/bar/08.js', False, None),

    ('series/bar/07.js', True, None),
    ('series/bar/08.js', True, None),

])
def test_XRangeSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls10, input_files, filename, as_file, error)
