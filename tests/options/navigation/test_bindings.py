"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.navigation.bindings import Binding as cls
from highcharts_core.options.navigation.bindings import Bindings as cls2
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'class_name': 'CircleAnnotationBinding',
      'init': 'some-event-marker',
      'start': 'some-event-marker',
      'steps': [
          'some-event-marker',
          'some-event-marker',
          'some-event-marker'
      ],
      'end': 'some-event-marker'
    }, None),

]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_Binding__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_Binding__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_Binding_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_Binding_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('navigation/bindings/01.js', False, None),

    ('navigation/bindings/error-01.js', False, (errors.HighchartsValueError,
                                                errors.HighchartsParseError,
                                                JSONDecodeError,
                                                TypeError,
                                                ValueError)),

    ('navigation/bindings/01.js', True, None),

    ('navigation/bindings/error-01.js', True, (errors.HighchartsValueError,
                                               errors.HighchartsParseError,
                                               JSONDecodeError,
                                               TypeError,
                                               ValueError)),
])
def test_Binding_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)



STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'circle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'ellipse_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker',
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'label_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': None,
        'end': 'some-event-marker'
      },
      'rectangle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      }
    }, None),

    ({
      'circle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker',
            'some-event-marker',
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'ellipse_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker',
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'label_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': None,
        'end': 'some-event-marker'
      },
      'rectangle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      }
    }, ValueError),
    ({
      'circle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'ellipse_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker',
            'some-event-marker',
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'label_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': None,
        'end': 'some-event-marker'
      },
      'rectangle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      }
    }, ValueError),
    ({
      'circle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'ellipse_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker',
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'label_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': ['some-event-marker'],
        'end': 'some-event-marker'
      },
      'rectangle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      }
    }, ValueError),
    ({
      'circle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'ellipse_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker',
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      },
      'label_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': None,
        'end': 'some-event-marker'
      },
      'rectangle_annotation': {
        'className': None,
        'init': 'some-event-marker',
        'start': 'some-event-marker',
        'steps': [
            'some-event-marker',
            'some-event-marker'
        ],
        'end': 'some-event-marker'
      }
    }, ValueError),

]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_Bindings__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_Bindings__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_Bindings_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_Bindings_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('navigation/bindings/02.js', False, None),

    ('navigation/bindings/error-03.js', False, (errors.HighchartsValueError,
                                                errors.HighchartsParseError,
                                                JSONDecodeError,
                                                TypeError,
                                                ValueError)),

    ('navigation/bindings/02.js', True, None),

    ('navigation/bindings/error-03.js', True, (errors.HighchartsValueError,
                                               errors.HighchartsParseError,
                                               JSONDecodeError,
                                               TypeError,
                                               ValueError)),
])
def test_Bindings_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
