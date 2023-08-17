"""Tests for ``highcharts.no_data``."""

import pytest
from typing import List

from json.decoder import JSONDecodeError

from highcharts_core.options.series.data.base import DataBase
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal


class NonAbstractDataBase(DataBase):

    @classmethod
    def from_array(cls, value):
        pass

    def _get_props_from_array(self) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`
        method.
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return ['fromArrayProp1', 'fromArrayProp2']



cls = NonAbstractDataBase


class RequiringJSObject(NonAbstractDataBase):
    def _to_untrimmed_dict(self):
        return {'someKey': 123}

class NotRequiringJSObject(NonAbstractDataBase):
    def _to_untrimmed_dict(self):
        return {
            'fromArrayProp1': 456,
            'fromArrayProp2': 789
        }


class RequiringJSObject2(NonAbstractDataBase):
    def _to_untrimmed_dict(self):
        return {'someKey': 123,
                'fromArrayProp1': 456,
                'fromArrayProp2': 789}


STANDARD_PARAMS = [
    ({}, None),
    ({
      'accessibility': {
          'description': 'Some description goes here',
          'enabled': True
      },
      'class_name': 'some-class-name',
      'color': '#ccc',
      'color_index': 2,
      'custom': {
          'some_key': 123,
          'other_key': 456
      },
      'description': 'Some description goes here',
      'events': {
        'click': """function(event) { return true; }""",
        'drag': """function(event) { return true; }""",
        'drop': """function(event) { return true; }""",
        'mouseOut': """function(event) { return true; }"""
      },
      'id': 'some-id-goes-here',
      'label_rank': 3,
      'name': 'Some Name Goes here',
      'selected': False
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
    ('series/data/base/01.js', False, None),

    ('series/data/base/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/data/base/01.js', True, None),

    ('series/data/base/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


@pytest.mark.parametrize('cls, expected', [
    (NonAbstractDataBase, False),
    (NotRequiringJSObject, False),
    (RequiringJSObject, True),
    (RequiringJSObject2, True)

])
def test_requires_js_object(cls, expected):
    obj = cls()
    assert obj.requires_js_object is expected