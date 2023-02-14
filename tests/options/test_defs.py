"""Tests for ``highcharts.defs``."""

import pytest

from json.decoder import JSONDecodeError
from copy import deepcopy

from highcharts_core.options.defs import MarkerAttributeObject as cls
from highcharts_core.options.defs import MarkerASTNode as cls2
from highcharts_core.options.defs import MarkerDefinition as cls3

from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS_cls = [
    ({}, None),
    ({
      'id': 'test ID',
      'ref_x': 123,
      'ref_y': 456,
      'marker_height': 321
    }, None),
    ({
      'id': 'random ID',
      'new_key': 'test value',
      'hyphen-key': 123
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls)
def test_MarkerAttributeObject__init__(kwargs, error):
    kwargs_copy = deepcopy(kwargs)
    if not error:
        result = cls(**kwargs)
        print(kwargs_copy)
        assert result is not None
        assert isinstance(result, cls) is True
        for key in kwargs_copy:
            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('class'):
                continue

            assert kwargs_copy[key] == result.get(key)
    else:
        with pytest.raises(error):
            result = cls(**kwargs)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls)
def test_MarkerAttributeObject__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls)
def test_MarkerAttributeObject_from_dict(kwargs, error):
    as_dict = to_js_dict(deepcopy(kwargs))

    if not error:
        instance = cls.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, cls) is True
        for key in as_dict:
            if hasattr(instance, key):
                assert as_dict.get(key) == getattr(instance, key)
            else:
                assert as_dict.get(key) == instance.get(key)
    else:
        with pytest.raises(error):
            instance = cls.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls)
def test_MarkerAttributeObject_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


STANDARD_PARAMS_cls2 = [
    ({}, None),

]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls2)
def test_MarkerASTNode__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls2)
def test_MarkerASTNode__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls2)
def test_MarkerASTNode_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls2)
def test_MarkerASTNode_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


STANDARD_PARAMS_cls3 = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls3)
def test_MarkerDefinition__init__(kwargs, error):
    kwargs_copy = deepcopy(kwargs)
    if not error:
        result = cls(**kwargs)
        print(kwargs_copy)
        assert result is not None
        assert isinstance(result, cls) is True
        for key in kwargs_copy:
            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs_copy[key], str) and kwargs[key].startswith('class'):
                continue

            assert kwargs_copy[key] == result.get(key)
    else:
        with pytest.raises(error):
            result = cls(**kwargs)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls3)
def test_MarkerDefinition__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls3)
def test_MarkerDefinition_from_dict(kwargs, error):
    as_dict = to_js_dict(deepcopy(kwargs))

    if not error:
        instance = cls.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, cls) is True
        for key in kwargs:
            assert kwargs.get(key) == instance.get(key)
    else:
        with pytest.raises(error):
            instance = cls.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls3)
def test_MarkerDefinition_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)
