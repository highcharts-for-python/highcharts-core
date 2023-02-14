"""Tests for ``highcharts.subtitle``."""

import pytest

from highcharts_core.options.subtitle import Subtitle as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
        'text': 'Subtitle aligned left',
        'align': 'left',
        'x': 70
    }, None),
    ({
        'text': 'Subtitle floating left',
        'floating': True,
        'align': 'left',
        'x': 100,
        'y': 50
    }, None),
    ({
        'use_html': True
    }, None),
    ({
        'vertical_align': 'middle'
    }, None),
    ({
        'width_adjust': -44
    }, None),

    ({'align': 'not-valid'}, errors.HighchartsValueError),
    ({'x': 'not-valid'}, TypeError),
    ({'vertical_align': 'not-valid'}, errors.HighchartsValueError),
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
    ('subtitle/01.js', False, None),
    ('subtitle/02.js', False, None),

    ('subtitle/error-01.js', False, errors.HighchartsValueError),
    ('subtitle/error-02.js', False, errors.HighchartsParseError),

    ('subtitle/01.js', True, None),
    ('subtitle/02.js', True, None),

    ('subtitle/error-01.js', True, errors.HighchartsValueError),
    ('subtitle/error-02.js', True, errors.HighchartsParseError),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
