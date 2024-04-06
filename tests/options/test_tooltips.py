"""Tests for ``highcharts.tooltips``."""

import pytest

from validator_collection import checkers

from highcharts_core.options.tooltips import (Tooltip as cls,
                                              DiagramTooltip as cls2)
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, compare_js_literals

STANDARD_PARAMS = [
    ({}, None),
    ({
      'animation': True,
      'background_color': '#ccc',
      'border_color': '#999',
      'border_radius': 4,
      'border_width': 1,
      'class_name': 'some-class-name',
      'cluster_format': 'format string',
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
      'distance': 12,
      'enabled': True,
      'follow_pointer': True,
      'follow_touch_move': True,
      'footer_format': 'format string',
      'formatter': """function() { return true; }""",
      'header_format': 'format string',
      'header_shape': 'circle',
      'hide_delay': 3,
      'null_format': 'format string',
      'null_formatter': """function() { return true; }""",
      'outside': False,
      'padding': 6,
      'point_format': 'format string',
      'point_formatter': """function() { return true; }""",
      'positioner': """function() { return true; }""",
      'shadow': False,
      'shape': 'rect',
      'shared': False,
      'snap': 4,
      'split': False,
      'stick_on_contact': True,
      'style': 'style string goes here',
      'use_html': False,
      'value_decimals': 2,
      'value_prefix': '$',
      'value_suffix': ' USD',
      'x_date_format': 'format string'
     }, None),
    ({
        'formatter': CallbackFunction.from_js_literal("""function () {
            // The first returned item is the header, subsequent items are the
            // points
            return ['<b>' + this.x + '</b>'].concat(
                this.points ?
                    this.points.map(function (point) {
                        return point.series.name + ': ' + point.y + 'm';
                    }) : []
            );
        }"""),
        'split': True
     }, None),
    ({
        'formatter': """function () {
            // The first returned item is the header, subsequent items are the
            // points
            return ['<b>' + this.x + '</b>'].concat(
                this.points ?
                    this.points.map(function (point) {
                        return point.series.name + ': ' + point.y + 'm';
                    }) : []
            );
        }""",
        'split': True
     }, None),
    ({
        'format': '{point.name} {point.y}'
      }, None),

    ({
      'border_width': 'not-a-number'
    }, (ValueError, TypeError)),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('tooltips/01.js', False, None),
    ('tooltips/02.js', False, None),

    ('tooltips/error-01.js', False, (TypeError, ValueError)),
    ('tooltips/error-02.js', False, errors.HighchartsParseError),

    ('tooltips/01.js', True, None),
    ('tooltips/02.js', True, None),

    ('tooltips/error-01.js', True, (TypeError, ValueError)),
    ('tooltips/error-02.js', True, errors.HighchartsParseError),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


def test_bug130_tooltip_serialization():
    as_js_literal = """{
        format: '{point.name}: {point.y}'
    }"""
    
    obj = cls.from_js_literal(as_js_literal)
    assert obj is not None
    assert isinstance(obj, cls) is True
    assert obj.format == '{point.name}: {point.y}'
    
    result = obj.to_js_literal()
    assert "'{point.name}: {point.y}'" in result or '"{point.name}: {point.y}"' in result
    
#### DIAGRAM TOOLTIP TESTS

STANDARD_PARAMS_2 = [
    ({}, None),
    ({
        'node_format': 'format string',
        'node_formatter': """function() { return true; }""",
    }, None),
    (
        {
            "animation": True,
            "background_color": "#ccc",
            "border_color": "#999",
            "border_radius": 4,
            "border_width": 1,
            "class_name": "some-class-name",
            "cluster_format": "format string",
            "date_time_label_formats": {
                "day": "test",
                "hour": "test",
                "millisecond": "test",
                "minute": "test",
                "month": "test",
                "second": "test",
                "week": "test",
                "year": "test",
            },
            "distance": 12,
            "enabled": True,
            "follow_pointer": True,
            "follow_touch_move": True,
            "footer_format": "format string",
            "formatter": """function() { return true; }""",
            "header_format": "format string",
            "header_shape": "circle",
            "hide_delay": 3,
            "null_format": "format string",
            "null_formatter": """function() { return true; }""",
            "outside": False,
            "padding": 6,
            "point_format": "format string",
            "point_formatter": """function() { return true; }""",
            "positioner": """function() { return true; }""",
            "shadow": False,
            "shape": "rect",
            "shared": False,
            "snap": 4,
            "split": False,
            "stick_on_contact": True,
            "style": "style string goes here",
            "use_html": False,
            "value_decimals": 2,
            "value_prefix": "$",
            "value_suffix": " USD",
            "x_date_format": "format string",
        },
        None,
    ),
    (
        {
            "formatter": CallbackFunction.from_js_literal("""function () {
            // The first returned item is the header, subsequent items are the
            // points
            return ['<b>' + this.x + '</b>'].concat(
                this.points ?
                    this.points.map(function (point) {
                        return point.series.name + ': ' + point.y + 'm';
                    }) : []
            );
        }"""),
            "split": True,
        },
        None,
    ),
    (
        {
            "formatter": """function () {
            // The first returned item is the header, subsequent items are the
            // points
            return ['<b>' + this.x + '</b>'].concat(
                this.points ?
                    this.points.map(function (point) {
                        return point.series.name + ': ' + point.y + 'm';
                    }) : []
            );
        }""",
            "split": True,
        },
        None,
    ),
    ({"format": "{point.name} {point.y}"}, None),
    ({"border_width": "not-a-number"}, (ValueError, TypeError)),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_DiagramTooltip__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_DiagramTooltip__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_DiagramTooltip_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_DiagramTooltip_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('tooltips/01.js', False, None),
    ('tooltips/02.js', False, None),
    ('tooltips/03-diagram.js', False, None),
    ('tooltips/04-diagram.js', False, None),

    ('tooltips/error-01.js', False, (TypeError, ValueError)),
    ('tooltips/error-02.js', False, errors.HighchartsParseError),

    ('tooltips/01.js', True, None),
    ('tooltips/02.js', True, None),
    ('tooltips/03-diagram.js', True, None),
    ('tooltips/04-diagram.js', False, None),

    ('tooltips/error-01.js', True, (TypeError, ValueError)),
    ('tooltips/error-02.js', True, errors.HighchartsParseError),
])
def test_DiagramTooltip_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)

