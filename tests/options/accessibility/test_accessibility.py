"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.accessibility import Accessibility as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'announce_new_data': {
          'announcementFormatter': """function() { return true; }""",
          'enabled': True,
          'interruptUser': True,
          'minimumAnnouncementInterval': 3
      },
      'custom_components': {
          'item1': 'some-value-goes-here',
          'item2': 'some_other_value_goes_here'
      },
      'description': 'Description goes here',
      'enabled': True,
      'high_contrast_theme': 'something goes here',
      'keyboard_navigation': {
          'enabled': True,
          'focusBorder': {
              'enabled': True,
              'hideBrowserFocusOutline': False,
              'margin': 20,
              'style': {
                  'borderRadius': 2,
                  'color': '#ccc',
                  'lineWidth': 1
              }
          },
          'order': [
              'series',
              'item1',
              'zoom',
              'container'
          ],
          'seriesNavigation': {
              'mode': 'normal',
              'pointNavigationEnabledThreshold': 20,
              'rememberPointFocus': True,
              'skipNullPoints': False
          },
          'wrapAround': True
      },
      'landmark_verbosity': 'all',
      'linked_description': 'some-item-goes-here',
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
      'screen_reader_section': {
          'afterChartFormat': 'format string',
          'afterChartFormatter': """function() { return true; }""",
          'axisRangeDateFormat': 'format string',
          'beforeChartFormat': 'format string',
          'beforeChartFormatter': """function() { return true; }""",
          'onPlayAsSoundClick': """function() { return true; }""",
          'onViewDataTableClick': """function() { return true; }"""
      },
      'series': {
          'describeSingleSeries': True,
          'descriptionFormat': 'format string goes here',
          'descriptionFormatter': """function() { return true; }""",
          'pointDescriptionEnabledThreshold': 100
      },
      'type_description': 'some description goes here'
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
    ('accessibility/accessibility/01.js', False, None),

    ('accessibility/accessibility/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('accessibility/accessibility/01.js', True, None),

    ('accessibility/accessibility/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
