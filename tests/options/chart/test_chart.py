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


@pytest.mark.parametrize('as_dict, as_js_literal, error', [
    ({
        'marginRight': 124
    }, False, None),
    ({
        'type': 'bar',
        'marginRight': 124,
        'marginTop': 421,
        'marginBottom': 321,
        'marginLeft': 789,
        'scrollablePlotArea': {
            'minHeight': 1000,
            'opacity': 1
        }
    }, False, None),

    ({
        'marginRight': 124
    }, True, None),
    ({
        'type': 'bar',
        'marginRight': 124,
        'marginTop': 421,
        'marginBottom': 321,
        'marginLeft': 789,
        'scrollablePlotArea': {
            'minHeight': 1000,
            'opacity': 1
        }
    }, True, None),
])
def test_bug124_margin_right(as_dict, as_js_literal, error):
    if not error:
        if not as_js_literal:
            result = cls.from_dict(as_dict)
        else:
            as_str = str(as_dict)
            result = cls.from_js_literal(as_str)
        assert isinstance(result, cls) is True
        if 'marginRight' in as_dict or 'margin_right' in as_dict:
            assert result.margin_right == as_dict.get('marginRight', None)
        if 'marginTop' in as_dict or 'margin_top' in as_dict:
            assert result.margin_top == as_dict.get('marginTop', None)
        if 'marginBottom' in as_dict or 'margin_bottom' in as_dict:
            assert result.margin_bottom == as_dict.get('marginBottom', None)
        if 'marginLeft' in as_dict or 'margin_left' in as_dict:
            assert result.margin_left == as_dict.get('marginLeft', None)
    else:
        with pytest.raises(error):
            if not as_js_literal:
                result = cls.from_dict(as_dict)
            else:
                as_str = str(as_dict)
                result = cls.from_js_literal(as_str)

            
@pytest.mark.parametrize('as_str, error', [
    ("""{
        marginRight: 124
    }""", None),
    ("""{type: 'bar',
        marginRight: 124,
        marginTop: 421,
        marginBottom: 321,
        marginLeft: 789,
        scrollablePlotArea: {
            minHeight: 1000,
            opacity: 1
        }
    }""", None),

    ("""{
        marginRight: null
    }""", None),
])
def test_bug124_margin_right_from_js_literal(as_str, error):
    if not error:
        result = cls.from_js_literal(as_str)
        assert isinstance(result, cls) is True
        if 'marginRight' in as_str or 'margin_right' in as_str:
            if 'marginRight: null' not in as_str:
                assert result.margin_right is not None
            else:
                assert result.margin_right is None
        if 'marginTop' in as_str or 'margin_top' in as_str:
            assert result.margin_top is not None
        if 'marginBottom' in as_str or 'margin_bottom' in as_str:
            assert result.margin_bottom is not None
        if 'marginLeft' in as_str or 'margin_left' in as_str:
            assert result.margin_left is not None
    else:
        with pytest.raises(error):
            result = cls.from_js_literal(as_str)


@pytest.mark.parametrize('as_dict, error', [
    ({
        'marginRight': 124
    }, None),
    ({
        'type': 'bar',
        'marginRight': 124,
        'marginTop': 421,
        'marginBottom': 321,
        'marginLeft': 789,
        'scrollablePlotArea': {
            'minHeight': 1000,
            'opacity': 1
        }
    }, None),

])
def test_bug124_margin_right_to_dict_from_dict(as_dict, error):
    if not error:
        initial_result = cls.from_dict(as_dict)
        as_new_dict = initial_result.to_dict()
        result = cls.from_dict(as_new_dict)
        assert isinstance(result, cls) is True
        assert result.margin_right == initial_result.margin_right
        assert result.margin_top == initial_result.margin_top
        assert result.margin_bottom == initial_result.margin_bottom
        assert result.margin_left == initial_result.margin_left
    else:
        with pytest.raises(error):
            initial_result = cls.from_dict(as_dict)
            as_new_dict = initial_result.to_dict()
            result = cls.from_dict(as_new_dict)


@pytest.mark.parametrize('as_dict, error', [
    ({
        'spacingRight': 124
    }, None),
    ({
        'type': 'bar',
        'spacingRight': 124,
        'spacingTop': 421,
        'spacingBottom': 321,
        'spacingLeft': 789,
        'scrollablePlotArea': {
            'minHeight': 1000,
            'opacity': 1
        }
    }, None),

])
def test_bug124_spacing_right_to_dict_from_dict(as_dict, error):
    if not error:
        initial_result = cls.from_dict(as_dict)
        as_new_dict = initial_result.to_dict()
        result = cls.from_dict(as_new_dict)
        assert isinstance(result, cls) is True
        assert result.spacing_right == initial_result.spacing_right
        assert result.spacing_top == initial_result.spacing_top
        assert result.spacing_bottom == initial_result.spacing_bottom
        assert result.spacing_left == initial_result.spacing_left
    else:
        with pytest.raises(error):
            initial_result = cls.from_dict(as_dict)
            as_new_dict = initial_result.to_dict()
            result = cls.from_dict(as_new_dict)
