"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.annotations import Annotation as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'animation': {
          'defer': 5
      },
      'control_point_options': {
          'positioner': """function(x, target) { return true; }"""
      },
      'crop': True,
      'draggable': 'xy',
      'events': {
          'add': """function(event) { return true; }""",
          'afterUpdate': """function(event) { return true; }""",
          'click': """function(event) { return true; }""",
          'remove': """function(event) { return true; }"""
      },
      'id': 'some-id',
      'label_options': {
          'accessibility': {
              'description': 'Description goes here'
          },
          'align': 'center',
          'allowOverlap': False,
          'backgroundColor': '#ccc',
          'borderColor': '#999',
          'borderRadius': 4,
          'borderWidth': 1,
          'className': 'some-class-name',
          'crop': False,
          'distance': 10,
          'format': 'format string',
          'formatter': """function() { return true; }""",
          'includeInDataExport': True,
          'overflow': 'justify',
          'padding': 12,
          'shadow': False,
          'shape': 'callout',
          'style': 'style-string-goes-here',
          'text': 'format string',
          'useHTML': False,
          'verticalAlign': 'top',
          'x': 5,
          'y': 10
      },
      'labels': [
          {
              'accessibility': {
                  'description': 'Description goes here'
              },
              'align': 'center',
              'allowOverlap': False,
              'backgroundColor': '#ccc',
              'borderColor': '#999',
              'borderRadius': 4,
              'borderWidth': 1,
              'className': 'some-class-name',
              'crop': False,
              'distance': 10,
              'format': 'format string',
              'formatter': """function() { return true; }""",
              'includeInDataExport': True,
              'overflow': 'justify',
              'padding': 12,
              'point': {
                  'x': 123,
                  'xAxis': 1,
                  'y': 456,
                  'yAxis': 1
              },
              'shadow': False,
              'shape': 'callout',
              'style': 'style-string-goes-here',
              'text': 'format string',
              'useHTML': False,
              'verticalAlign': 'top',
              'x': 5,
              'y': 10
          },
          {
              'accessibility': {
                  'description': 'Description goes here'
              },
              'align': 'center',
              'allowOverlap': False,
              'backgroundColor': '#ccc',
              'borderColor': '#999',
              'borderRadius': 4,
              'borderWidth': 1,
              'className': 'some-class-name',
              'crop': False,
              'distance': 10,
              'format': 'format string',
              'formatter': """function() { return true; }""",
              'includeInDataExport': True,
              'overflow': 'justify',
              'padding': 12,
              'point': 'point-id-goes-here',
              'shadow': False,
              'shape': 'callout',
              'style': 'style-string-goes-here',
              'text': 'format string',
              'useHTML': False,
              'verticalAlign': 'top',
              'x': 5,
              'y': 10
          },
          {
              'accessibility': {
                  'description': 'Description goes here'
              },
              'align': 'center',
              'allowOverlap': False,
              'backgroundColor': '#ccc',
              'borderColor': '#999',
              'borderRadius': 4,
              'borderWidth': 1,
              'className': 'some-class-name',
              'crop': False,
              'distance': 10,
              'format': 'format string',
              'formatter': """function() { return true; }""",
              'includeInDataExport': True,
              'overflow': 'justify',
              'padding': 12,
              'point': {
                  'x': 123,
                  'xAxis': 'axis-id',
                  'y': 456,
                  'yAxis': 'axis-id'
              },
              'shadow': False,
              'shape': 'callout',
              'style': 'style-string-goes-here',
              'text': 'format string',
              'useHTML': False,
              'verticalAlign': 'top',
              'x': 5,
              'y': 10
          }
      ],
      'shape_options': {
          'dashStyle': 'Solid',
          'fill': '#000',
          'height': 123,
          'r': 12,
          'ry': 24,
          'snap': 5,
          'src': 'https://www.somewhere.com',
          'stroke': '#ccc',
          'strokeWidth': 1,
          'type': 'rect',
          'width': 12,
          'xAxis': 1,
          'yAxis': 1
      },
      'shapes': [
          {
           'markerEnd': 'some-id-goes-here',
           'markerStart': 'some-id-goes-here',
           'point': {
               'x': 123,
               'xAxis': 1,
               'y': 456,
               'yAxis': 1
           },
           'points': [
               {
                'x': 123,
                'xAxis': 1,
                'y': 456,
                'yAxis': 1
               },
               'some-id-goes-here',
               """function() { return true; }"""
           ]
          }
      ],
      'visible': True,
      'z_index': 3
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
    ('annotations/annotation/01.js', False, None),

    ('annotations/annotation/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/annotation/01.js', True, None),

    ('annotations/annotation/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)
