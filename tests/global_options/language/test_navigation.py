"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.global_options.language.navigation import NavigationLanguageOptions as cls
from highcharts_core.global_options.language.navigation import PopupLanguageOptions as cls2
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'popup': {
        'addButton': 'Add',
        'algorithm': 'some string',
        'arrowInfinityLine': 'some string',
        'arrowRay': 'some string',
        'arrowSegment': 'string',
        'average': 'avg',
        'background': 'background',
        'backgroundColor': 'some string',
        'borderRadius': 'some string',
        'borderWidth': 'width',
        'bottomBand': 'band',
        'circle': 'some string',
        'clearFilter': 'clear',
        'color': 'some string',
        'connector': 'some string',
        'crooked3': 'some string',
        'crooked5': 'some string',
        'crosshairX': 'some string',
        'crosshairY': 'some string',
        'decimals': 'some string',
        'deviation': 'some string',
        'editButton': 'some string',
        'elliott3': 'some string',
        'elliott5': 'some string',
        'ellipse': 'some string',
        'factor': 'some string',
        'fastAvgPeriod': 'some string',
        'fibonacci': 'some string',
        'fibonacciTimeZones': 'some string',
        'fill': 'some string',
        'flags': 'some string',
        'fontSize': 'some string',
        'format': 'some string',
        'height': 'some string',
        'highIndex': 'some string',
        'horizontalLine': 'some string',
        'increment': 'some string',
        'index': 'some string',
        'infinityLine': 'some string',
        'initialAccelerationFactor': 'some string',
        'innerBackground': 'some string',
        'label': 'some string',
        'labelOptions': 'some string',
        'labels': 'some string',
        'line': 'some string',
        'lines': 'some string',
        'longPeriod': 'some string',
        'lowIndex': 'some string',
        'maxAccelerationFactor': 'some string',
        'measure': 'some string',
        'measureX': 'some string',
        'measureXY': 'some string',
        'measureY': 'some string',
        'multiplier': 'some string',
        'multiplierATR': 'some string',
        'name': 'some string',
        'noFilterMatch': 'some string',
        'outerBackground': 'some string',
        'padding': 'some string',
        'parallelChannel': 'some string',
        'period': 'some string',
        'periodATR': 'some string',
        'periods': 'some string',
        'periodSenkouSpanB': 'some string',
        'periodTenkan': 'some string',
        'pitchfork': 'some string',
        'ranges': 'some string',
        'ray': 'some string',
        'rectangle': 'some string',
        'removeButton': 'some string',
        'saveButton': 'some string',
        'searchIndicators': 'some string',
        'segment': 'some string',
        'series': 'some string',
        'shapeOptions': 'some string',
        'shapes': 'some string',
        'shortPeriod': 'some string',
        'signalPeriod': 'some string',
        'simpleShapes': 'some string',
        'slowAvgPeriod': 'some string',
        'standardDeviation': 'some string',
        'stroke': 'some string',
        'strokeWidth': 'some string',
        'style': 'some string',
        'timeCycles': 'some string',
        'title': 'some string',
        'topBand': 'some string',
        'tunnel': 'some string',
        'typeOptions': 'some string',
        'verticalArrow': 'some string',
        'verticalCounter': 'some string',
        'verticalLabel': 'some string',
        'verticalLine': 'some string',
        'volume': 'some string',
        'xAxisUnit': 'some string'
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
    ('global_options/language/navigation/01.js', False, None),

    ('global_options/language/navigation/error-01.js', False, (errors.HighchartsValueError,
                                                               errors.HighchartsParseError,
                                                               JSONDecodeError,
                                                               TypeError,
                                                               ValueError)),

    ('global_options/language/navigation/01.js', True, None),

    ('global_options/language/navigation/error-01.js', True, (errors.HighchartsValueError,
                                                              errors.HighchartsParseError,
                                                              JSONDecodeError,
                                                              TypeError,
                                                              ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'add_button': 'Add',
      'algorithm': 'some string',
      'arrow_infinity_line': 'some string',
      'arrow_ray': 'some string',
      'arrow_segment': 'string',
      'average': 'avg',
      'background': 'background',
      'background_color': 'some string',
      'border_radius': 'some string',
      'border_width': 'width',
      'bottom_band': 'band',
      'circle': 'some string',
      'clear_filter': 'clear',
      'color': 'some string',
      'connector': 'some string',
      'crooked3': 'some string',
      'crooked5': 'some string',
      'crosshairX': 'some string',
      'crosshairY': 'some string',
      'decimals': 'some string',
      'deviation': 'some string',
      'edit_button': 'some string',
      'elliott3': 'some string',
      'elliott5': 'some string',
      'ellipse': 'some string',
      'factor': 'some string',
      'fast_avg_period': 'some string',
      'fibonacci': 'some string',
      'fibonacci_time_zones': 'some string',
      'fill': 'some string',
      'flags': 'some string',
      'font_size': 'some string',
      'format': 'some string',
      'height': 'some string',
      'high_index': 'some string',
      'horizontal_line': 'some string',
      'increment': 'some string',
      'index': 'some string',
      'infinity_line': 'some string',
      'initial_acceleration_factor': 'some string',
      'inner_background': 'some string',
      'label': 'some string',
      'label_options': 'some string',
      'labels': 'some string',
      'line': 'some string',
      'lines': 'some string',
      'long_period': 'some string',
      'low_index': 'some string',
      'max_acceleration_factor': 'some string',
      'measure': 'some string',
      'measure_x': 'some string',
      'measure_xy': 'some string',
      'measure_y': 'some string',
      'multiplier': 'some string',
      'multiplier_atr': 'some string',
      'name': 'some string',
      'no_filter_match': 'some string',
      'outer_background': 'some string',
      'padding': 'some string',
      'parallel_channel': 'some string',
      'period': 'some string',
      'period_atr': 'some string',
      'periods': 'some string',
      'period_senkou_span_b': 'some string',
      'period_tenkan': 'some string',
      'pitchfork': 'some string',
      'ranges': 'some string',
      'ray': 'some string',
      'rectangle': 'some string',
      'remove_button': 'some string',
      'save_button': 'some string',
      'search_indicators': 'some string',
      'segment': 'some string',
      'series': 'some string',
      'shape_options': 'some string',
      'shapes': 'some string',
      'short_period': 'some string',
      'signal_period': 'some string',
      'simple_shapes': 'some string',
      'slow_avg_period': 'some string',
      'standard_deviation': 'some string',
      'stroke': 'some string',
      'stroke_width': 'some string',
      'style': 'some string',
      'time_cycles': 'some string',
      'title': 'some string',
      'top_band': 'some string',
      'tunnel': 'some string',
      'type_options': 'some string',
      'vertical_arrow': 'some string',
      'vertical_counter': 'some string',
      'vertical_label': 'some string',
      'vertical_line': 'some string',
      'volume': 'some string',
      'x_axis_unit': 'some string'
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_PopupLanguageOptions__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_PopupLanguageOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_PopupLanguageOptions_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_PopupLanguageOptions_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('global_options/language/navigation/02.js', False, None),

    ('global_options/language/navigation/error-03.js', False, (errors.HighchartsValueError,
                                                               errors.HighchartsParseError,
                                                               JSONDecodeError,
                                                               TypeError,
                                                               ValueError)),

    ('global_options/language/navigation/02.js', True, None),

    ('global_options/language/navigation/error-03.js', True, (errors.HighchartsValueError,
                                                              errors.HighchartsParseError,
                                                              JSONDecodeError,
                                                              TypeError,
                                                              ValueError)),
])
def test_PopupLanguageOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
