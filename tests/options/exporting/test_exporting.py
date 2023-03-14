"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.exporting import Exporting as cls
from highcharts_core import errors, constants
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'accessibility': {
          'enabled': True
      },
      'allow_html': False,
      'buttons': {
          'context_button': constants.EnforcedNullType(),
          'test_key': {
              'text': 'Test Text',
              'enabled': True
          },
          'test_key2': {
              'text': 'Test Text 2',
              'enabled': True
          }
      },
      'enabled': True,
      'error': """function() { return true; }""",
      'fallback_to_export_server': True,
      'filename': 'test-filename',
      'form_attributes': {
          'test_attr': 'value-123',
          'test_attr2': 'value-345'
      },
      'lib_url': 'http://www.somewhere.com/',
      'menu_item_definitions': {
          'menu1': {
            'onclick': """function() { return true; }""",
            'text': 'My Menu Item',
            'textKey': 'my-menu-item',
            'separator': False
          },
          'menu2': {
            'onclick': """function() { return true; }""",
            'text': 'My Menu Item',
            'textKey': 'my-menu-item',
            'separator': False
          }
      },
      'pdf_font': {
          'bold': 'http://www.somefile.com/flie.otf',
          'bolditalic': 'http://www.somefile.com/flie.otf',
          'italic': 'http://www.somefile.com/flie.otf',
          'normal': 'http://www.somefile.com/flie.otf',
      },
      'print_max_width': 300,
      'scale': 1200,
      'show_table': True,
      'source_height': 120,
      'source_width': 300,
      'table_caption': 'Caption goes here',
      'type': 'image/png',
      'url': 'http://www.somewhere.com/',
      'use_multi_level_headers': False,
      'use_rowspan_headers': False,
      'width': 300
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('exporting/exporting/01.js', False, None),

    ('exporting/exporting/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('exporting/exporting/01.js', True, None),

    ('exporting/exporting/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
