"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.patterns import Pattern as cls
from highcharts_core.utility_classes.patterns import PatternOptions as cls2
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'animation': {
          'defer': 5
      },
      'pattern_options': None,
      'pattern_index': 1
    }, None),
    ({
      'animation': {
          'defer': 5
      },
      'pattern_options': {
          'aspectRatio': 0.5,
          'backgroundColor': '#999999',
          'id': 'some_id_goes_here',
          'opacity': 0.5,
          'width': 120,
          'x': 5,
          'y': 10
      },
      'pattern_index': 2
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_Pattern__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_Pattern__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_Pattern_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_Pattern_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/patterns/01.js', False, None),

    ('utility_classes/patterns/error-01.js', False, (errors.HighchartsValueError,
                                                     errors.HighchartsParseError,
                                                     JSONDecodeError,
                                                     TypeError,
                                                     ValueError)),

    ('utility_classes/patterns/01.js', True, None),

    ('utility_classes/patterns/error-01.js', True, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),
])
def test_Pattern_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)



STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'aspect_ratio': 0.5,
      'background_color': '#999999',
      'id': 'some_id_goes_here',
      'opacity': 0.5,
      'width': 120,
      'x': 5,
      'y': 10
     }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_PatternOptions__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_PatternOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_PatternOptions_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_PatternOptions_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/patterns/02.js', False, None),

    ('utility_classes/patterns/error-03.js', False, (errors.HighchartsValueError,
                                                     errors.HighchartsParseError,
                                                     JSONDecodeError,
                                                     TypeError,
                                                     ValueError)),

    ('utility_classes/patterns/02.js', True, None),

    ('utility_classes/patterns/error-03.js', True, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),
])
def test_PatternOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
