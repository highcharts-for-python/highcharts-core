"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.legend import Legend as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'accessibility': {
          'enabled': True,
          'keyboardNavigation': {
              'enabled': True
          }
      },
      'align': 'right',
      'align_columns': True,
      'background_color': '#fff',
      'border_color': '#ccc',
      'border_radius': 4,
      'class_name': 'some-class-name',
      'enabled': True,
      'floating': False,
      'item_checkbox_style': 'some-style-setting',
      'item_distance': 12,
      'item_hidden_style': 'some-style-setting',
      'item_hover_style': 'some-style-setting',
      'item_margin_bottom': 7,
      'item_margin_top': 7,
      'item_style': 'some-style-setting',
      'item_width': 36,
      'label_format': 'format string',
      'label_formatter': """function () { return true; }""",
      'layout': 'vertical',
      'margin': 7,
      'max_height': 120,
      'padding': 8,
      'reversed': False,
      'rtl': False,
      'shadow': False,
      'square_symbol': False,
      'symbol_height': 12,
      'symbol_padding': 2,
      'symbol_radius': 0,
      'symbol_width': 12,
      'title': {
          'style': 'some-style-string',
          'text': 'Legend Title Goes Here'
      },
      'use_html': False,
      'vertical_align': 'top',
      'width': 120,
      'x': 0,
      'y': 0
    }, None),
    ({
        'item_style': {
            'color': '#5f5e5e',
            'fontFamily': 'Roboto',
            'fontSize': '12px'
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
    ('legend/legend/01.js', False, None),

    ('legend/legend/error-01.js', False, (errors.HighchartsValueError,
                                          errors.HighchartsParseError,
                                          JSONDecodeError,
                                          TypeError,
                                          ValueError)),

    ('legend/legend/01.js', True, None),

    ('legend/legend/error-01.js', True, (errors.HighchartsValueError,
                                         errors.HighchartsParseError,
                                         JSONDecodeError,
                                         TypeError,
                                         ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
