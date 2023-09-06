"""Tests for ``highcharts.no_data``."""

import pytest
import numpy as np

from json.decoder import JSONDecodeError

from highcharts_core.options.series.data.collections import DataPointCollection as cls
from highcharts_core.options.series.data.base import DataBase
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal_with_expected


class NonAbstractDataBase(DataBase):

    @classmethod
    def from_array(cls, value):
        pass


class RequiringJSObject(NonAbstractDataBase):
    def _to_untrimmed_dict(self):
        return {'someKey': 123}


STANDARD_PARAMS = [
    ({}, None),
    ({
        'data_points': {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
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
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
        }
    }, None),
    ({
        'ndarray': np.array([1, 2, 3])
    }, None),
    ({
        'ndarray': np.array([1, 2, 3]),
        'data_points': {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
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
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
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


@pytest.mark.parametrize('input_filename, expected_filename, as_file, error', [
    ('series/data/collections/01-input.js',
     'series/data/collections/01-expected.js',
     False,
     None),

    ('series/data/collections/02-input.js',
     'series/data/collections/02-expected.js',
     False,
     None),
])
def test_from_js_literal(input_files, input_filename, expected_filename, as_file, error):
    Class_from_js_literal_with_expected(cls,
                                        input_files,
                                        input_filename,
                                        expected_filename,
                                        as_file,
                                        error)


@pytest.mark.parametrize('value, expected_shape, has_data_points, error', [
    (np.asarray([
        [0.0, 15.0], 
        [10.0, -50.0], 
        [20.0, -56.5], 
        [30.0, -46.5], 
        [40.0, -22.1],
        [50.0, -2.5], 
        [60.0, -27.7], 
        [70.0, -55.7], 
        [80.0, -76.5]
    ]), (9, 2), False, None),
    
    ('Not an Array', None, False, ValueError),
])
def test_from_ndarray(value, expected_shape, has_data_points, error):
    if not error:
        result = cls.from_ndarray(value)
        assert result is not None
        assert result.ndarray is not None
        assert result.ndarray.shape == expected_shape
        if has_data_points:
            assert result.data_points is not None
    else:
        with pytest.raises(error):
            result = cls.from_ndarray(value)
            

@pytest.mark.parametrize('value, expected_shape, has_ndarray, has_data_points, error', [
    (np.asarray([
        [0.0, 15.0], 
        [10.0, -50.0], 
        [20.0, -56.5], 
        [30.0, -46.5], 
        [40.0, -22.1],
        [50.0, -2.5], 
        [60.0, -27.7], 
        [70.0, -55.7], 
        [80.0, -76.5]
    ]), (9, 2), True, False, None),
    ([
        {
            'id': 'some-value'
        },
        {
            'id': 'some other value'
        },
    ], (9, 2), False, True, None),
    
    ('Not an Array', None, True, False, ValueError),
])
def test_from_array(value, expected_shape, has_ndarray, has_data_points, error):
    if has_ndarray is False and has_data_points is False:
        raise AssertionError('Test is invalid. has_ndarray or has_data_points must be '
                             'True. Both were supplied as False.')
    if not error:
        result = cls.from_array(value)
        assert result is not None
        if has_ndarray:
            assert result.ndarray is not None
            assert result.ndarray.shape == expected_shape
        if has_data_points:
            assert result.data_points is not None
    else:
        with pytest.raises(error):
            result = cls.from_array(value)
            

@pytest.mark.parametrize('value, kwargs, expects_objects, error', [
    (np.asarray([
        [0.0, 15.0], 
        [10.0, -50.0], 
        [20.0, -56.5], 
        [30.0, -46.5], 
        [40.0, -22.1],
        [50.0, -2.5], 
        [60.0, -27.7], 
        [70.0, -55.7], 
        [80.0, -76.5]
    ]), {}, False, None),
    ([
        {
            'id': 'some-value'
        },
        {
            'id': 'some other value'
        },
    ], {}, True, None),
    (np.asarray([
        [0.0, 15.0], 
        [10.0, -50.0], 
        [20.0, -56.5], 
        [30.0, -46.5], 
        [40.0, -22.1],
        [50.0, -2.5], 
        [60.0, -27.7], 
        [70.0, -55.7], 
        [80.0, -76.5]
    ]), {'force_object': True}, True, None),
    ([
        {
            'id': 'some-value'
        },
        {
            'id': 'some other value'
        },
    ], {'force_ndarray': True}, False, None),
    
])
def test_to_array(value, kwargs, expects_objects, error):
    if not error:
        obj = cls.from_array(value)
        result = obj.to_array(**kwargs)
        assert result is not None
        assert isinstance(result, list) is True
        assert len(result) == len(value)
        if expects_objects:
            for item in result:
                assert isinstance(item, DataBase) is True