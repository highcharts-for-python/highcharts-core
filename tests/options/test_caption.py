"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.caption import Caption as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'align': 'center',
      'text': 'Test Text for the Caption',
      'vertical_align': 'top',
      'x': 123,
      'y': -123
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
    ('caption/01.js', False, None),
    ('caption/02.js', False, None),

    ('caption/error-01.js', False, (errors.HighchartsValueError,
                                    errors.HighchartsParseError,
                                    JSONDecodeError,
                                    TypeError,
                                    ValueError)),
    ('caption/error-02.js', False, (errors.HighchartsValueError,
                                    errors.HighchartsParseError,
                                    JSONDecodeError,
                                    TypeError,
                                    ValueError)),

    ('caption/01.js', True, None),
    ('caption/02.js', True, None),

    ('caption/error-01.js', True, (errors.HighchartsValueError,
                                   errors.HighchartsParseError,
                                   JSONDecodeError,
                                   TypeError,
                                   ValueError)),
    ('caption/error-02.js', True, (errors.HighchartsValueError,
                                   errors.HighchartsParseError,
                                   JSONDecodeError,
                                   TypeError,
                                   ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
