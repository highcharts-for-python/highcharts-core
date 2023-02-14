"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.axes.parallel_axes import ParallelAxesOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    # Y-Axis propeties only
    ({
      'max_color': '#ccc',
      'min_color': '#000',
      'stack_labels': {
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
      'stops': [
          [0.0, '#ccc'],
          [0.1, '#fff'],
          [0.25, '#999'],
          [1.0, '#ff0000']
      ],
      'tooltip_value_format': 'format string goes here'
    }, None),
    # XAxis properties only
    ({
      'max_color': '#ccc',
      'min_color': '#000',
      'stack_labels': {
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
      'stops': [
          [0.0, '#ccc'],
          [0.1, '#fff'],
          [0.25, '#999'],
          [1.0, '#ff0000']
      ],
      'tooltip_value_format': 'format string goes here',

      'crosshair': {
          'className': 'some-class-name',
          'color': '#ccc',
          'dashStyle': 'Dash',
          'snap': True,
          'width': 40,
          'zIndex': 6
      },
      'height': 60,
      'left': 5,
      'line_color': '#999',
      'line_width': 1,
      'show_empty': True,
      'top': 340,
      'width': 300,
    }, None),
    # with GenericAxis and NumericAxis properties
    ({
      'max_color': '#ccc',
      'min_color': '#000',
      'stack_labels': {
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
      'stops': [
          [0.0, '#ccc'],
          [0.1, '#fff'],
          [0.25, '#999'],
          [1.0, '#ff0000']
      ],
      'tooltip_value_format': 'format string goes here',

      'crosshair': {
          'className': 'some-class-name',
          'color': '#ccc',
          'dashStyle': 'Dash',
          'snap': True,
          'width': 40,
          'zIndex': 6
      },
      'height': 60,
      'left': 5,
      'line_color': '#999',
      'line_width': 1,
      'show_empty': True,
      'top': 340,
      'width': 300,

      'accessibility': {
          'description': 'Description goes here',
          'enabled': True,
          'rangeDescription': 'Range description goes here'
      },
      'align_ticks': False,
      'allow_decimals': True,
      'alternate_grid_color': '#ccc',
      'angle': 15,
      'breaks': [
          {
           'breakSize': 20,
           'from': 0,
           'repeat': 1,
           'to': 100
          },
          {
           'breakSize': 50,
           'from': 100,
           'repeat': 1,
           'to': 1000
          }
      ],
      'categories': [
          'Category 1',
          'Category 2',
          'Category 3',
          'Category 4'
      ],
      'ceiling': 120,
      'class_name': 'some-class-name',
      'date_time_label_formats': {
        'day': 'test',
        'hour': 'test',
        'millisecond': 'test',
        'minute': 'test',
        'month': 'test',
        'second': 'test',
        'week': 'test',
        'year': 'test'
      },
      'end_on_tick': False,
      'events': {
        'afterBreaks': """function(event) { return true; }""",
        'afterSetExtremes': """function(event) { return true; }""",
        'pointBreak': """function(event) { return true; }""",
        'setExtremes': """function(event) { return true; }"""
      },
      'floor': 0,
      'grid_line_color': '#ccc',
      'grid_line_dash_style': 'Solid',
      'grid_line_interpolation': 'circle',
      'grid_line_width': 1,
      'grid_z_index': 3,
      'id': 'some-id',
      'labels': {
          'align': 'center',
          'allowOverlap': False,
          'autoRotation': [-45],
          'autoRotationLimit': 80,
          'distance': 12,
          'enabled': True,
          'format': 'some format string',
          'formatter': """function () { return true; }""",
          'overflow': 'allow',
          'padding': 12,
          'position3d': 'offset',
          'reserveSpace': True,
          'rotation': 24,
          'skew3d': False,
          'staggerLines': 0,
          'step': 2,
          'style': 'some-style-string',
          'useHTML': False,
          'x': 5,
          'y': -10,
          'zIndex': 6
      },
      'linked_to': 3,
      'margin': 12,
      'max': 1000,
      'max_padding': 12,
      'min': 0,
      'min_range': 5,
      'min_tick_interval': 1,
      'minor_grid_line_color': '#999',
      'minor_grid_line_dash_style': 'Dash',
      'minor_grid_line_width': 1,
      'minor_tick_color': '#ccc',
      'minor_tick_interval': 0.1,
      'minor_tick_position': 'outside',
      'minor_ticks': True,
      'minor_tick_width': 1,
      'min_padding': 8,
      'offset': 0,
      'opposite': False,
      'pane': 1,
      'panning_enabled': True,
      'reversed': False,
      'reversed_stacks': False,
      'show_first_label': True,
      'show_last_label': True,
      'soft_max': 10,
      'soft_min': 6,
      'start_of_week': 1,
      'start_on_tick': False,
      'tick_amount': 5,
      'tick_color': '#000',
      'tick_interval': 5,
      'tick_length': 8,
      'tickmark_placement': 'on',
      'tick_pixel_interval': 8,
      'tick_position': 'outside',
      'tick_positioner': """function() { return true; }""",
      'tick_width': 1,
      'title': {
          'align': 'low',
          'margin': 20,
          'offset': 0,
          'position3d': 'offset',
          'reserveSpace': True,
          'rotation': 0,
          'skew3d': False,
          'style': 'some-style-string',
          'text': 'The Axis Title',
          'textAlign': 'center',
          'useHTML': False,
          'x': 5,
          'y': 10
      },
      'type': 'linear',
      'unique_names': True,
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
      ],
      'visible': True,
      'z_index': 3,
      'zoom_enabled': True

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
    ('axes/parallel_axes/01.js', False, None),
    ('axes/parallel_axes/02.js', False, None),

    ('axes/parallel_axes/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('axes/parallel_axes/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('axes/parallel_axes/01.js', True, None),
    ('axes/parallel_axes/02.js', True, None),

    ('axes/parallel_axes/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('axes/parallel_axes/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
