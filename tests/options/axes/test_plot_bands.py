"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.axes.plot_bands import PlotBand as cls
from highcharts_core.options.axes.plot_bands import PlotLine as cls2
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'border_color': '#ccc',
      'border_width': 1,
      'class_name': 'some-class-name',
      'color': '#999',
      'events': {
        'click': """function(event) { return true; }""",
        'mousemove': """function(event) { return true; }""",
        'mouseout': """function(event) { return true; }""",
        'mouseover': """function(event) { return true; }"""
      },
      'from_': 123,
      'id': 'some-id',
      'label': {
          'align': 'center',
          'rotation': 0,
          'style': 'some-style-string',
          'text': 'The title of the plot band',
          'textAlign': 'left',
          'useHTML': False,
          'verticalAlign': 'middle',
          'x': -10,
          'y': 100
      },
      'to': 456,
      'z_index': 3
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_PlotBand__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_PlotBand__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_PlotBand_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_PlotBand_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('axes/plot_bands/01.js', False, None),

    ('axes/plot_bands/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('axes/plot_bands/01.js', True, None),

    ('axes/plot_bands/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_PlotBand_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'class_name': 'some-class-name',
      'color': '#fff',
      'dash_style': 'Dash',
      'events': {
        'click': """function(event) { return true; }""",
        'mousemove': """function(event) { return true; }""",
        'mouseout': """function(event) { return true; }""",
        'mouseover': """function(event) { return true; }"""
      },
      'label': {
          'align': 'center',
          'formatter': """function() { return true; }""",
          'rotation': 0,
          'style': 'some-style-string',
          'text': 'The title of the plot band',
          'textAlign': 'left',
          'useHTML': False,
          'verticalAlign': 'middle',
          'x': -10,
          'y': 100
      },
      'value': 123,
      'width': 2,
      'z_index': 3
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_PlotLine__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_PlotLine__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_PlotLine_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_PlotLine_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('axes/plot_bands/02.js', False, None),

    ('axes/plot_bands/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('axes/plot_bands/02.js', True, None),

    ('axes/plot_bands/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_PlotLine_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
