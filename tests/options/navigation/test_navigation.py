"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.navigation import Navigation as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'bindings_class_name': 'some-class-name',
      'breadcrumbs': {
        'buttonSpacing': 6,
        'buttonTheme': {
            'fill': '#fff'
        },
        'events': {
          'click': """function(event) { return true; }"""
        },
        'floating': True,
        'format': 'some format string',
        'formatter': """function () { return true; }""",
        'position': None,
        'relativeTo': 'plot',
        'rtl': False,
        'separator': {
            'text': '>',
            'style': {
                'some-key': 'some-value'
            }
        },
        'useHTML': False,
        'zIndex': 3
      },
      'button_options': {
        'enabled': True,
        'text': 'Button Label',
        'theme': {
            'fill': '#fff',
            'stroke': '#ccc'
        },
        'y': 0
      },
      'events': {
        'closePopup': """function (event) { return true; }""",
        'selectButton': """function (event) {return true;}""",
        'showPopup': """function(event) {return true;}"""
      },
      'icons_url': 'https://www.somewhere.com/'
    }, None),
    ({
      'bindings_class_name': 'some-class-name',
      'breadcrumbs': {
        'buttonSpacing': 6,
        'buttonTheme': {
            'fill': '#fff'
        },
        'events': {
          'click': """function(event) { return true; }"""
        },
        'floating': True,
        'format': 'some format string',
        'formatter': """function () { return true; }""",
        'position': None,
        'relativeTo': 'plot',
        'rtl': False,
        'separator': {
            'text': '>',
            'style': {
                'some-key': 'some-value'
            }
        },
        'useHTML': False,
        'zIndex': 3
      },
      'button_options': {
        'enabled': True,
        'text': 'Button Label',
        'theme': {
            'fill': '#fff',
            'stroke': '#ccc'
        },
        'useHTML': True,
        'y': 0
      },
      'events': {
        'closePopup': """function (event) { return true; }""",
        'selectButton': """function (event) {return true;}""",
        'showPopup': """function(event) {return true;}"""
      },
      'icons_url': 'https://www.somewhere.com/',
      'menu_item_style': {"fontWeight": "bold", "fontSize": "12px"},
      'menu_item_hover_style': {"fontWeight": "bold", "fontSize": "12px"},
      'menu_style': {"border-width": "1px"}
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
    ('navigation/navigation/01.js', False, None),

    ('navigation/navigation/error-01.js', False, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),

    ('navigation/navigation/01.js', True, None),

    ('navigation/navigation/error-01.js', True, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
