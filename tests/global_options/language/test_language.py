"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.global_options.language import Language as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'context_button_title': 'some title goes here',
      'decimal_point': '--',
      'download_csv': 'Download CSV',
      'download_jpeg': 'Download JPEG',
      'download_pdf': 'Download PDF',
      'download_png': 'Download PNG',
      'download_svg': 'Download SVG',
      'download_xls': 'Download Excel',
      'drillup_text': 'Backup',
      'exit_fullscreen': 'Exit Fullscreen Mode',
      'hide_data': 'Hide',
      'invalid_date': 'Invalid Time Period',
      'loading': 'Loading...',
      'main_breadcrumb': 'Home',
      'months': [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec'
      ],
      'no_data': 'No data available.',
      'numeric_symbol_magnitude': 1,
      'numeric_symbols': ['#', 'k', 'm'],
      'print_chart': 'Print',
      'reset_zoom': 'Reset',
      'reset_zoom_title': 'Reset Zoom',
      'short_months': [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec'
      ],
      'short_weekdays': [
          'Mon',
          'Tue',
          'Wed',
          'Thurs',
          'Fri',
          'Sat',
          'Sun'
      ],
      'thousands_separator': ',',
      'view_data': 'View Data',
      'view_fullscreen': 'Fullscreen',
      'weekdays': [
          'Mon',
          'Tue',
          'Wed',
          'Thurs',
          'Fri',
          'Sat',
          'Sun'
      ]
    }, None),
    ({
      'export_data': {
        'annotationHeader': 'some string',
        'categoryDatetimeHeader': 'some string',
        'categoryHeader': 'a different string'
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
    ('global_options/language/language/01.js', False, None),

    ('global_options/language/language/error-01.js', False, (errors.HighchartsValueError,
                                                             errors.HighchartsParseError,
                                                             JSONDecodeError,
                                                             TypeError,
                                                             ValueError)),

    ('global_options/language/language/01.js', True, None),

    ('global_options/language/language/error-01.js', True, (errors.HighchartsValueError,
                                                            errors.HighchartsParseError,
                                                            JSONDecodeError,
                                                            TypeError,
                                                            ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
