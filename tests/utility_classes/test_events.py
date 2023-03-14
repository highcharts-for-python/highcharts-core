"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.events import ChartEvents as cls
from highcharts_core.utility_classes.events import BreadcrumbEvents as cls2
from highcharts_core.utility_classes.events import NavigationEvents as cls3
from highcharts_core.utility_classes.events import PointEvents as cls4
from highcharts_core.utility_classes.events import SeriesEvents as cls5
from highcharts_core.utility_classes.events import ClusterEvents as cls6
from highcharts_core.utility_classes.events import AxisEvents as cls7
from highcharts_core.utility_classes.events import MouseEvents as cls8

from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'add_series': """function(event) { return true;}""",
      'after_print': """function(event) {return true;}""",
      'click': """function(event) { return true; }""",
      'selection': """function(event) { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ChartEvents__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ChartEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ChartEvents_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ChartEvents_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/01.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-01.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/01.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-01.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_ChartEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'click': """function(event) { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_BreadcrumbEvents__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_BreadcrumbEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_BreadcrumbEvents_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_BreadcrumbEvents_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/02.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-02.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/02.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-02.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_BreadcrumbEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


STANDARD_PARAMS_3 = [
    ({}, None),
    ({
      'close_popup': """function (event) { return true; }""",
      'select_button': """function (event) {return true;}""",
      'show_popup': """function(event) {return true;}"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_NavigationEvents__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_NavigationEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_NavigationEvents_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_NavigationEvents_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/03.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-03.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/03.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-03.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_NavigationEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


STANDARD_PARAMS_4 = [
    ({}, None),
    ({
      'click': """function(event) { return true; }""",
      'drag': """function(event) { return true; }""",
      'drop': """function(event) { return true; }""",
      'mouse_out': """function(event) { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_4)
def test_PointEvents__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_4)
def test_PointEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_4)
def test_PointEvents_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_4)
def test_PointEvents_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/04.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-04.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/04.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-04.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_PointEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)


STANDARD_PARAMS_5 = [
    ({}, None),
    ({
      'after_animate': """function(event) { return true; }""",
      'click': """function(event) { return true; }""",
      'hide': """function(event) { return true; }""",
      'mouse_out': """function(event) { return true; }""",
      'show': """function(event) { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_5)
def test_SeriesEvents__init__(kwargs, error):
    Class__init__(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_5)
def test_SeriesEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_5)
def test_SeriesEvents_from_dict(kwargs, error):
    Class_from_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_5)
def test_SeriesEvents_to_dict(kwargs, error):
    Class_to_dict(cls5, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/05.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-05.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/05.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-05.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_SeriesEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls5, input_files, filename, as_file, error)


STANDARD_PARAMS_6 = [
    ({}, None),
    ({
      'drill_to_cluster': """function(event) { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_6)
def test_ClusterEvents__init__(kwargs, error):
    Class__init__(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_6)
def test_ClusterEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_6)
def test_ClusterEvents_from_dict(kwargs, error):
    Class_from_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_6)
def test_ClusterEvents_to_dict(kwargs, error):
    Class_to_dict(cls6, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/06.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-06.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/06.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-06.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_ClusterEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls6, input_files, filename, as_file, error)


STANDARD_PARAMS_7 = [
    ({}, None),
    ({
      'after_breaks': """function(event) { return true; }""",
      'after_set_extremes': """function(event) { return true; }""",
      'point_break': """function(event) { return true; }""",
      'set_extremes': """function(event) { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_7)
def test_AxisEvents__init__(kwargs, error):
    Class__init__(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_7)
def test_AxisEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_7)
def test_AxisEvents_from_dict(kwargs, error):
    Class_from_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_7)
def test_AxisEvents_to_dict(kwargs, error):
    Class_to_dict(cls7, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/07.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-07.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/07.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-07.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_AxisEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls7, input_files, filename, as_file, error)


STANDARD_PARAMS_8 = [
    ({}, None),
    ({
      'click': """function(event) { return true; }""",
      'mousemove': """function(event) { return true; }""",
      'mouseout': """function(event) { return true; }""",
      'mouseover': """function(event) { return true; }"""
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_8)
def test_MouseEvents__init__(kwargs, error):
    Class__init__(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_8)
def test_MouseEvents__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_8)
def test_MouseEvents_from_dict(kwargs, error):
    Class_from_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_8)
def test_MouseEvents_to_dict(kwargs, error):
    Class_to_dict(cls8, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/events/08.js', False, None),

    ('utility_classes/events/error-00.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
    ('utility_classes/events/error-08.js', False, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),

    ('utility_classes/events/08.js', True, None),

    ('utility_classes/events/error-00.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
    ('utility_classes/events/error-08.js', True, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),
])
def test_MouseEvents_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls8, input_files, filename, as_file, error)
