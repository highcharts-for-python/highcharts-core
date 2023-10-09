"""Tests for ``highcharts.no_data``."""

import pytest
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from json.decoder import JSONDecodeError

from validator_collection import checkers

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
        'data_points': [{
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
        }]
    }, None),
    ({
        'ndarray': np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3]
    }, None if HAS_NUMPY else ValueError),
    ({
        'ndarray': np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3],
        'data_points': [{
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
        }]
    }, None if HAS_NUMPY else ValueError),
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
     None if HAS_NUMPY else ValueError),

    ('series/data/collections/02-input.js',
     'series/data/collections/02-expected.js',
     False,
     None if HAS_NUMPY else ValueError),

    ('series/data/collections/03-input.js',
     'series/data/collections/03-expected.js',
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

if HAS_NUMPY:
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
            assert isinstance(result.ndarray, dict) is True
            for key in result.ndarray:
                key_value = result.ndarray[key]
                assert isinstance(key_value, np.ndarray) is True
                assert len(key_value) == expected_shape[0]
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
    ]) if HAS_NUMPY else [
        [0.0, 15.0], 
        [10.0, -50.0], 
        [20.0, -56.5], 
        [30.0, -46.5], 
        [40.0, -22.1],
        [50.0, -2.5], 
        [60.0, -27.7], 
        [70.0, -55.7], 
        [80.0, -76.5]
    ], (9, 2), True, False, None),
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
            if HAS_NUMPY:
                assert result.ndarray is not None
                assert isinstance(result.ndarray, dict) is True
                for key in result.ndarray:
                    key_value = result.ndarray[key]
                    assert isinstance(key_value, np.ndarray) is True
                    assert len(key_value) == expected_shape[0]
            else:
                assert result.array is not None or result.data_points is not None
                if result.array:
                    assert len(result.array) == expected_shape[0]
                else:
                    assert len(result.data_points) == expected_shape[0]
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
    ]) if HAS_NUMPY else [
        [0.0, 15.0], 
        [10.0, -50.0], 
        [20.0, -56.5], 
        [30.0, -46.5], 
        [40.0, -22.1],
        [50.0, -2.5], 
        [60.0, -27.7], 
        [70.0, -55.7], 
        [80.0, -76.5]
    ], {}, False, None),
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
    ]) if HAS_NUMPY else [
        [0.0, 15.0], 
        [10.0, -50.0], 
        [20.0, -56.5], 
        [30.0, -46.5], 
        [40.0, -22.1],
        [50.0, -2.5], 
        [60.0, -27.7], 
        [70.0, -55.7], 
        [80.0, -76.5]
    ], {'force_object': True}, True, None),
    ([
        {
            'id': 'some-value'
        },
        {
            'id': 'some other value'
        },
    ], {'force_ndarray': True}, False, None if HAS_NUMPY else ValueError),
    
])
def test_to_array(value, kwargs, expects_objects, error):
    if not error:
        obj = cls.from_array(value)
        result = obj.to_array(**kwargs)
        assert result is not None
        assert isinstance(result, list) is True
        # assert len(result) == len(value)
        if expects_objects:
            for item in result:
                assert isinstance(item, DataBase) is True
                

@pytest.mark.parametrize('kwargs, name, expected, error', [
    ({}, 'ndarray', None, None),
    ({}, 'data_points', None, None),
    ({
        'ndarray': np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3]
    }, 'ndarray', np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3], None if HAS_NUMPY else ValueError),
    ({
        'ndarray': np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3]
     },
     'data_points',
     None, 
     None if HAS_NUMPY else ValueError),
    ({
        'ndarray': np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3],
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
    },
     'ndarray',
     np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3],
     None if HAS_NUMPY else ValueError),
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
    }, 'color', np.asarray(['#ccc']) if HAS_NUMPY else ['#ccc'], None),
])
def test__getattr__(kwargs, name, expected, error):
    if not error:
        obj = cls(**kwargs)
        result = getattr(obj, name)
        if name == 'ndarray':
            if expected is None:
                assert result is None
            else:
                print(type(result))
                assert isinstance(result, dict) is True
        elif not checkers.is_type(result, 'ndarray'):
            assert checkers.are_equivalent(result, expected) is True
        elif HAS_NUMPY:
            assert np.array_equiv(result, expected) is True
    else:
        with pytest.raises(error):
            obj = cls(**kwargs)
            result = getattr(obj, name)
            

@pytest.mark.parametrize('name, value, expected, error', [
    ('ndarray', 
     np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3], 
     np.array([1, 2, 3]) if HAS_NUMPY else [1, 2, 3], 
     None if HAS_NUMPY else ValueError),
    ('data_points', {
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
        }, [DataBase(**{
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
        })], None),
])
def test__setattr__(name, value, expected, error):
    if not error:
        obj = cls()
        setattr(obj, name, value)
        result = getattr(obj, name)
        if name == 'ndarray':
            if expected is None:
                assert result is None
            else:
                assert isinstance(result, dict) is True
        elif not checkers.is_type(result, 'ndarray') and name == 'data_points':
            assert len(result) == len(expected)
        elif not checkers.is_type(result, 'ndarray'):
            assert checkers.are_equivalent(result, expected) is True
        else:
            assert np.array_equiv(result, expected) is True
    else:
        with pytest.raises(error):
            obj = cls()
            setattr(obj, name, value)
