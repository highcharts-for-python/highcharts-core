"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.global_options.language.accessibility.series import SeriesTypeDescriptions as cls
from highcharts_core.global_options.language.accessibility.series import SeriesLanguageOptions as cls2
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'arearange': 'Area Range',
      'areasplinerange': 'Area Spline Range',
      'boxplot': 'Boxplot',
      'bubble': 'Bubble',
      'columnrange': 'Column Range',
      'errorbar': 'Errorbar',
      'funnel': 'Funnel',
      'pyramid': 'Pyramid',
      'waterfall': 'Waterfall'
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_SeriesTypeDescriptions__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_SeriesTypeDescriptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_SeriesTypeDescriptions_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_SeriesTypeDescriptions_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('global_options/language/accessibility/series/01.js', False, None),

    ('global_options/language/accessibility/series/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('global_options/language/accessibility/series/01.js', True, None),

    ('global_options/language/accessibility/series/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
])
def test_SeriesTypeDescriptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'description': 'Description goes here',
      'null_point_value': 'Null point value',
      'point_annotations_description': 'Point annotations description',
      'summary': {},
      'x_axis_description': 'X-Axis description',
      'y_axis_description': 'Y-Axis description'
    }, None),
    ({
      'description': 'Description goes here',
      'null_point_value': 'Null point value',
      'point_annotations_description': 'Point annotations description',
      'summary': {
          'bar': 'Bar',
          'barCombination': 'Bar combo',
          'boxplot': 'Boxplot',
          'boxplotCombination': 'Boxplot combo',
          'bubble': 'Bubble',
          'bubbleCombination': 'bubble combination',
          'column': 'column',
          'columnCombination': 'column_combination',
          'default': 'Default summary',
          'defaultCombination': 'Default combination',
          'line': 'Line',
          'lineCombination': 'Line combination',
          'map': 'Map',
          'mapCombination': 'Map combo',
          'mapbubble': 'Map Bubble',
          'mapbubbleCombination': 'Mapbubble Combo',
          'mapline': 'Map/Line',
          'maplineCombination': 'Map/Line Combo',
          'pie': 'Pie',
          'pieCombination': 'Pie Combo',
          'scatter': 'Scatter',
          'scatterCombination': 'Scatter Combo',
          'spline': 'Spline',
          'splineCombination': 'Spline Combination'
      },
      'x_axis_description': 'X-Axis description',
      'y_axis_description': 'Y-Axis description'
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_SeriesLanguageOptions__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_SeriesLanguageOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_SeriesLanguageOptions_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_SeriesLanguageOptions_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('global_options/language/accessibility/series/02.js', False, None),

    ('global_options/language/accessibility/series/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('global_options/language/accessibility/series/02.js', True, None),

    ('global_options/language/accessibility/series/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
])
def test_SeriesLanguageOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
