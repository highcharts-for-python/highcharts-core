"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.zones import Zone as cls
from highcharts_core.utility_classes.zones import ClusterZone as cls2
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'class_name': 'some-class-name1',
      'color': '#999999',
      'dash_style': 'Solid',
      'fill_color': '#cccccc',
      'value': 123
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_Zone__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_Zone__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_Zone_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_Zone_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/zones/01.js', False, None),

    ('utility_classes/zones/error-01.js', False, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),

    ('utility_classes/zones/01.js', True, None),

    ('utility_classes/zones/error-01.js', True, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),
])
def test_Zone_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
     'class_name': 'classname-1',
     'from_': 1,
     'marker': {
       'fillColor': '#cccccc',
       'enabled': True,
       'height': 24,
       'lineWidth': 2,
       'radius': 2,
       'states': {
           'hover': {
               'enabled': True
           }
       },
       'symbol': 'circle',
       'width': 48
     },
     'to': 123
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_ClusterZone__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_ClusterZone__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_ClusterZone_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_ClusterZone_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/zones/02.js', False, None),

    ('utility_classes/zones/error-03.js', False, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),

    ('utility_classes/zones/02.js', True, None),

    ('utility_classes/zones/error-03.js', True, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),
])
def test_ClusterZone_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
