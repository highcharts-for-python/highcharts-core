"""Tests for ``highcharts.utility_classes.ast``."""

import pytest

from json.decoder import JSONDecodeError
from copy import deepcopy

from highcharts_core.utility_classes.ast import AttributeObject as cls
from highcharts_core.utility_classes.ast import ASTNode as cls2
from highcharts_core.utility_classes.ast import ASTMap as cls3
from highcharts_core.utility_classes.ast import TextPath as cls4

from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS_cls = [
    ({}, None),
    ({
        'stroke': '#ff0000',
        'stroke-width': 2,
        'rotation': 45,
        'd': ['M', 10, 10, 'L', 30, 30, 'z']
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls)
def test_AttributeObject__init__(kwargs, error):
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
def test_AttributeObject__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls)
def test_AttributeObject_from_dict(kwargs, error):
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


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls)
def test_AttributeObject_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


STANDARD_PARAMS_cls2 = [
    ({}, None),

]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls2)
def test_ASTNode__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls2)
def test_ASTNode__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls2)
def test_ASTNode_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls2)
def test_ASTNode_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


STANDARD_PARAMS_cls3 = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls3)
def test_ASTMap__init__(kwargs, error):
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
def test_ASTMap__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls3)
def test_ASTMap_from_dict(kwargs, error):
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
def test_ASTMap_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


STANDARD_PARAMS_cls4 = [
    ({}, None),

]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls4)
def test_TextPath__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_cls4)
def test_TextPath__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls4)
def test_TextPath_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_cls4)
def test_TextPath_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)
