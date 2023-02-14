"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.nodes import NodeOptions as cls
from highcharts_core.utility_classes.nodes import OrganizationNodeOptions as cls2
from highcharts_core.utility_classes.nodes import DependencyWheelNodeOptions as cls3

from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'color': '#cccccc',
      'color_index': 123,
      'data_labels': {
          'align': 'center',
          'allowOverlap': False,
          'backgroundColor': '#cccccc',
          'enabled': True,
          'overflow': 'justify',
          'shadow': False
      },
      'id': 'some-id-goes-here',
      'name': 'My Node Name',
      'offset_horizontal': 10,
      'offset_vertical': '5%'
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_NodeOptions__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_NodeOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_NodeOptions_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_NodeOptions_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/nodes/01.js', False, None),

    ('utility_classes/nodes/error-01.js', False, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),

    ('utility_classes/nodes/01.js', True, None),

    ('utility_classes/nodes/error-01.js', True, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),
])
def test_NodeOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)



STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'color': '#cccccc',
      'color_index': 123,
      'column': 2,
      'data_labels': {
          'align': 'center',
          'allowOverlap': False,
          'backgroundColor': '#cccccc',
          'enabled': True,
          'overflow': 'justify',
          'shadow': False
      },
      'id': 'some-id-goes-here',
      'image': 'http://www.somewhere.com/',
      'layout': 'normal',
      'level': 2,
      'name': 'My Node Name',
      'offset_horizontal': 10,
      'offset_vertical': '5%',
      'title': 'Grand High Muckety-Muck'
    }, None),

]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_OrganizationNodeOptions__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_OrganizationNodeOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_OrganizationNodeOptions_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_OrganizationNodeOptions_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/nodes/02.js', False, None),

    ('utility_classes/nodes/error-03.js', False, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),

    ('utility_classes/nodes/02.js', True, None),

    ('utility_classes/nodes/error-03.js', True, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),
])
def test_OrganizationNodeOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


STANDARD_PARAMS_3 = [
    ({}, None),
    ({
      'column': 2,
      'level': 2
    }, None),
    ({
      'column': 2,
      'level': 2,
      'color': '#cccccc',
      'color_index': 123,
      'data_labels': {
          'align': 'center',
          'allowOverlap': False,
          'backgroundColor': '#cccccc',
          'enabled': True,
          'overflow': 'justify',
          'shadow': False
      },
      'id': 'some-id-goes-here',
      'name': 'My Node Name',
      'offset_horizontal': 10,
      'offset_vertical': '5%'
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_DependencyWheelNodeOptions__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_DependencyWheelNodeOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_DependencyWheelNodeOptions_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_DependencyWheelNodeOptions_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/nodes/03.js', False, None),

    ('utility_classes/nodes/error-04.js', False, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),

    ('utility_classes/nodes/03.js', True, None),

    ('utility_classes/nodes/error-04.js', True, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),
])
def test_DependencyWheelNodeOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)
