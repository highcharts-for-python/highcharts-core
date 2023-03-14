"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.global_options.language.accessibility import AccessibilityLanguageOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'announce_new_data': {
          'newDataAnnounce': 'New Data!',
          'newPointAnnounceMultiple': 'New data points added',
          'newPointAnnounceSingle': 'New data point added',
          'newSeriesAnnounceMultiple': 'New data series added',
          'newSeriesAnnounceSingle': 'Added a data series'
      },
      'axis': {
          'rangeCategories': 'Categories',
          'rangeFromTo': 'X to Y',
          'timeRangeDays': 'Monday - Friday',
          'timeRangeHours': '0h - 24h',
          'timeRangeMinutes': ':00 - :59',
          'timeRangeSeconds': ':00:00 - :00:59',
          'xAxisDescriptionPlural': 'X Axis Description when pluralized',
          'xAxisDescriptionSingular': 'X Axis Description',
          'yAxisDescriptionPlural': 'Y-Axis description when pluralized',
          'yAxisDescriptionSingular': 'Y-Axis Description'
      },
      'chart_container_label': 'some string',
      'chart_types': {
          'barMultiple': 'Bar Charts',
          'barSingle': 'Bar Chart',
          'boxplotMultiple': 'Boxplot Charts',
          'boxplotSingle': 'Boxplot Chart',
          'bubbleMultiple': 'Bubble Charts',
          'bubbleSingle': 'Bubble Chart',
          'columnMultiple': 'Column Charts',
          'columnSingle': 'Column Chart',
          'combinationChart': 'Combo Chart',
          'defaultMultiple': 'Charts',
          'defaultSingle': 'Chart',
          'emptyChart': 'Empty Chart',
          'lineMultiple': 'Line Charts',
          'lineSingle': 'Line Chart',
          'mapTypeDescription': 'Map',
          'pieMultiple': 'Pie Charts',
          'pieSingle': 'Pie Chart',
          'scatterMultiple': 'Scatter Charts',
          'scatterSingle': 'Scatter Chart',
          'splineMultiple': 'Spline Charts',
          'splineSingle': 'Spline Chart',
          'unknownMap': 'Unknown Map'
      },
      'credits': 'credits go here',
      'default_chart_title': 'default title goes here',
      'drillup_button': 'drillup button label',
      'exporting': {
          'chartMenuLabel': 'Menu',
          'menuButtonLabel': 'Menu Button'
      },
      'graphic_container_label': 'Graphic Container',
      'legend': {
          'legendItem': 'Item',
          'legendLabel': 'Legend',
          'legendLabelNoTitle': 'Label with no Title'
      },
      'range_selector': {
          'clickButtonAnnouncement': 'Selected Range',
          'dropdownLabel': 'Range',
          'maxInputLabel': 'Max.',
          'minInputLabel': 'Min.'
      },
      'screen_reader_section': {
          'afterRegionLabel': 'After Region',
          'annotations': {
              'descriptionMultiplePoints': 'Description of multiple points',
              'descriptionNoPoints': 'Description with no points',
              'descriptionSinglePoint': 'Description of a single point',
              'heading': 'My Heading'
          },
          'beforeRegionLabel': 'Before Region',
          'endOfChartMarker': 'End of Chart'
      },
      'sonification': {
          'playAsSoundButtonText': 'Play as Sound',
          'playAsSoundClickAnnouncement': 'Playing as Sound'
      },
      'svg_container_label': 'SVG',
      'svg_container_title': 'SVG',
      'table': {
          'tableSummary': 'Summary goes here',
          'viewAsDataTableButtonText': 'View as Table'
      },
      'thousands_separator': ',',
      'zoom': {
          'mapZoomIn': 'Zoom In',
          'mapZoomOut': 'Zoom out',
          'resetZoomButton': 'Reset Zoom'
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
    ('global_options/language/accessibility/accessibility/01.js', False, None),

    ('global_options/language/accessibility/accessibility/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('global_options/language/accessibility/accessibility/01.js', True, None),

    ('global_options/language/accessibility/accessibility/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
