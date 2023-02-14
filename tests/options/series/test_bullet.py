"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.series.bullet import BulletSeries as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'data': [
          {
            'target': 123,
            'targetOptions': {
                'borderColor': '#999',
                'borderRadius': 2,
                'borderWidth': 1,
                'color': '#ccc',
                'height': 12,
                'width': '5%'
            },

            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          }
      ]
    }, None),
    # + BulletOptions
    ({
      'data': [
          {
            'target': 123,
            'targetOptions': {
                'borderColor': '#999',
                'borderRadius': 2,
                'borderWidth': 1,
                'color': '#ccc',
                'height': 12,
                'width': '5%'
            },

            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          }
      ],

      'drag_drop': {
          'draggableTarget': True,
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
      'target_options': {
          'borderColor': '#999',
          'borderRadius': 2,
          'borderWidth': 1,
          'color': '#ccc',
          'height': 12,
          'width': '5%'
      }
    }, None),
    # + Bar Options
    ({
      'data': [
          {
            'target': 123,
            'targetOptions': {
                'borderColor': '#999',
                'borderRadius': 2,
                'borderWidth': 1,
                'color': '#ccc',
                'height': 12,
                'width': '5%'
            },

            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          }
      ],

      'drag_drop': {
          'draggableTarget': True,
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
      'target_options': {
          'borderColor': '#999',
          'borderRadius': 2,
          'borderWidth': 1,
          'color': '#ccc',
          'height': 12,
          'width': '5%'
      },

      'depth': 10,
      'edge_color': '#999',
      'edge_width': 1,
      'group_z_padding': 4
    }, None),
    # + Base Bar Options
    ({
      'data': [
          {
            'target': 123,
            'targetOptions': {
                'borderColor': '#999',
                'borderRadius': 2,
                'borderWidth': 1,
                'color': '#ccc',
                'height': 12,
                'width': '5%'
            },

            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          }
      ],

      'drag_drop': {
          'draggableTarget': True,
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
      'target_options': {
          'borderColor': '#999',
          'borderRadius': 2,
          'borderWidth': 1,
          'color': '#ccc',
          'height': 12,
          'width': '5%'
      },

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
            'target': 123,
            'targetOptions': {
                'borderColor': '#999',
                'borderRadius': 2,
                'borderWidth': 1,
                'color': '#ccc',
                'height': 12,
                'width': '5%'
            },

            'borderColor': '#ccc',
            'borderWidth': 2,
            'dashStyle': 'Solid',
            'pointWidth': 12
          }
      ],

      'drag_drop': {
          'draggableTarget': True,
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
      'target_options': {
          'borderColor': '#999',
          'borderRadius': 2,
          'borderWidth': 1,
          'color': '#ccc',
          'height': 12,
          'width': '5%'
      },

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
def test_BulletSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_BulletSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BulletSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_BulletSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/bullet/01.js', False, None),

    ('series/bullet/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/bullet/01.js', True, None),

    ('series/bullet/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_BulletSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
