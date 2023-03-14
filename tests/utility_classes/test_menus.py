"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError
from copy import deepcopy
from collections import UserDict

from highcharts_core.utility_classes.menus import MenuItem as cls
from highcharts_core.utility_classes.menus import MenuObject as cls2
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, does_kwarg_value_match_result

STANDARD_PARAMS = [
    ({}, None),
    ({
      'onclick': """function() { return true; }""",
      'text': 'My Menu Item',
      'text_key': 'my-menu-item',
      'separator': False
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_MenuItem__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_MenuItem__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_MenuItem_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_MenuItem_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/menus/01.js', False, None),

    ('utility_classes/menus/error-01.js', False, (errors.HighchartsValueError,
                                                  errors.HighchartsParseError,
                                                  JSONDecodeError,
                                                  TypeError,
                                                  ValueError)),

    ('utility_classes/menus/01.js', True, None),

    ('utility_classes/menus/error-01.js', True, (errors.HighchartsValueError,
                                                 errors.HighchartsParseError,
                                                 JSONDecodeError,
                                                 TypeError,
                                                 ValueError)),
])
def test_MenuItem_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'item1': cls(text = 'My Menu Item',
                   text_key = 'item1',
                   separator = False),
      'item2': cls(text = 'Second Menu Item',
                   text_key = 'item2',
                   separator = False)
    }, None),
    ({
     'item1': {
         'onclick': """function() { return true; }""",
         'text': 'My Menu Item',
         'textKey': 'my-menu-item',
         'separator': False
     },
     'item2': {
         'onclick': """function() { return true; }""",
         'text': 'Second Menu Item',
         'textKey': 'my-menu-item2',
         'separator': False
     },
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_MenuObject__init__(kwargs, error):
    kwargs_copy = {}
    for key in kwargs:
        if isinstance(kwargs[key], dict):
            kwargs_copy[key] = deepcopy(kwargs[key])
        kwargs_copy[key] = kwargs[key]
    print('before init')
    print(kwargs_copy)
    if 'item1' in kwargs_copy:
        print(id(kwargs_copy['item1']))
        print(id(kwargs['item1']))
    if not error:
        result = cls2(**kwargs)
        assert result is not None
        assert isinstance(result, cls2) is True
        for key in kwargs:
            if isinstance(kwargs[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs[key], str) and kwargs[key].startswith('class'):
                continue

            print(f'after __init__ for key: {key}')
            print(kwargs_copy[key])
            print(result.get(key))
            assert does_kwarg_value_match_result(kwargs_copy[key],
                                                 result.get(key)) is True
    else:
        with pytest.raises(error):
            result = cls2(**kwargs)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_MenuObject__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_MenuObject_from_dict(kwargs, error):
    as_dict = to_js_dict(deepcopy(kwargs))

    if not error:
        instance = cls2.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, cls2) is True
        for key in kwargs:
            assert does_kwarg_value_match_result(kwargs[key],
                                                 instance.get(key)) is True
    else:
        with pytest.raises(error):
            instance = cls2.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_MenuObject_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)
