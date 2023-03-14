"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.data_grouping import DataGroupingOptions as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'anchor': 'start',
      'approximation': 'windbarb',
      'date_time_label_formats': {
        'day': 'test',
        'hour': 'test',
        'millisecond': 'test',
        'minute': 'test',
        'month': 'test',
        'second': 'test',
        'week': 'test',
        'year': 'test'
      },
      'enabled': True,
      'first_anchor': 'start',
      'forced': True,
      'group_all': True,
      'group_pixel_width': 10,
      'last_anchor': 'end',
      'units': [
          [
              'millisecond',
              [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
          ],
          [
              'second',
              [1, 2, 5, 10, 15, 30]
          ],
          [
              'minute',
              [1, 2, 5, 10, 15, 30]
          ],
          [
              'hour',
              [1, 2, 3, 4, 6, 8, 12]
          ],
          [
              'day',
              [1]
          ],
          [
              'week',
              [1]
          ],
          [
              'month',
              [1, 3, 6]
          ],
          [
              'year',
              None
          ]
      ]
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
    ('utility_classes/data_grouping/01.js', False, None),

    ('utility_classes/data_grouping/error-01.js', False, (errors.HighchartsValueError,
                                                          errors.HighchartsParseError,
                                                          JSONDecodeError,
                                                          TypeError,
                                                          ValueError)),

    ('utility_classes/data_grouping/01.js', True, None),

    ('utility_classes/data_grouping/error-01.js', True, (errors.HighchartsValueError,
                                                         errors.HighchartsParseError,
                                                         JSONDecodeError,
                                                         TypeError,
                                                         ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
