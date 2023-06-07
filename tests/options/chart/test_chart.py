"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.chart import ChartOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'align_thresholds': True,
      'align_ticks': True,
      'allow_mutating_data': True,
      'animation': False,
      'background_color': '#fff',
      'border_color': '#ccc',
      'border_radius': 3,
      'border_width': 1,
      'class_name': 'some-class-name',
      'color_count': 10,
      'display_errors': True,
      'events': {
        'addSeries': """function(event) { return true;}""",
        'afterPrint': """function(event) {return true;}""",
        'click': """function(event) { return true; }""",
        'selection': """function(event) { return true; }"""
      },
      'height': 120,
      'ignore_hidden_series': False,
      'inverted': False,
      'margin': 20,
      'number_formatter': """function(value) { return true; }""",
      'pan_key': 'ctrl',
      'panning': {
          'enabled': True,
          'type': 'x'
      },
      'parallel_coordinates': False,
      'plot_background_color': '#ccc',
      'plot_background_image': 'http://www.somewhere.com',
      'plot_border_color': '#999',
      'plot_border_width': 1,
      'plot_shadow': False,
      'polar': False,
      'reflow': False,
      'render_to': 'some-id',
      'scrollable_plot_area': {
          'minHeight': 120,
          'minWidth': 300,
          'opacity': 0.6,
          'scrollPositionX': 0,
          'scrollPositionY': 0
      },
      'selection_marker_fill': '#ccc',
      'shadow': False,
      'show_axes': True,
      'spacing': [5, 5, 5, 5],
      'style': 'style-string-goes-here',
      'styled_mode': False,
      'type': 'line',
      'width': 50
    }, None),
    ({
      'align_thresholds': True,
      'align_ticks': True,
      'allow_mutating_data': True,
      'animation': False,
      'background_color': '#fff',
      'border_color': '#ccc',
      'border_radius': 3,
      'border_width': 1,
      'class_name': 'some-class-name',
      'color_count': 10,
      'display_errors': True,
      'events': {
        'addSeries': """function(event) { return true;}""",
        'afterPrint': """function(event) {return true;}""",
        'click': """function(event) { return true; }""",
        'selection': """function(event) { return true; }"""
      },
      'height': 120,
      'ignore_hidden_series': False,
      'inverted': False,
      'margin': 20,
      'number_formatter': """function(value) { return true; }""",
      'pan_key': 'ctrl',
      'panning': {
          'enabled': True,
          'type': 'x'
      },
      'parallel_coordinates': False,
      'plot_background_color': '#ccc',
      'plot_background_image': 'http://www.somewhere.com',
      'plot_border_color': '#999',
      'plot_border_width': 1,
      'plot_shadow': False,
      'polar': False,
      'reflow': False,
      'render_to': 'some-id',
      'scrollable_plot_area': {
          'minHeight': 120,
          'minWidth': 300,
          'opacity': 0.6,
          'scrollPositionX': 0,
          'scrollPositionY': 0
      },
      'selection_marker_fill': '#ccc',
      'shadow': False,
      'show_axes': True,
      'spacing': [5, 5, 5, 5],
      'style': 'style-string-goes-here',
      'styled_mode': False,
      'type': 'line',
      'width': 50,
      'zooming': {
          'key': 'alt',
          'mouse_wheel': {
              'enabled': True,
              'sensitivity': 1.5,
              'type': 'xy'
          },
          'pinch_type': 'xy',
          'single_touch': False
      }
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
    ('chart/chart/01.js', False, None),
    ('chart/chart/02.js', False, None),

    ('chart/chart/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('chart/chart/01.js', True, None),
    ('chart/chart/02.js', False, None),

    ('chart/chart/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
