"""Tests for ``highcharts.no_data``."""

import pytest
from copy import deepcopy

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.buttons import ButtonConfiguration as cls
from highcharts_core.utility_classes.buttons import ContextButtonConfiguration as cls2
from highcharts_core.utility_classes.buttons import ExportingButtons as cls3
from highcharts_core import errors, constants
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, does_kwarg_value_match_result

STANDARD_PARAMS = [
    ({}, None),
    ({
      'enabled': True,
      'text': 'Button Label',
      'theme': {
          'fill': '#fff',
          'stroke': '#ccc'
      },
      'y': 0
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ButtonConfiguration__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ButtonConfiguration__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ButtonConfiguration_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ButtonConfiguration_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/buttons/01.js', False, None),

    ('utility_classes/buttons/error-01.js', False, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),

    ('utility_classes/buttons/01.js', True, None),

    ('utility_classes/buttons/error-01.js', True, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
])
def test_ButtonConfiguration_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


STANDARD_PARAMS_2 = [
    ({}, None),
    ({
      'class_name': 'some-class-name',
      'enabled': True,
      'menu_class_name': 'menu-class',
      'menu_items': ['item1', 'item2'],
      'onclick': """function (event) { return true; }""",
      'symbol': 'menu',
      'symbol_fill': '#ccc',
      'text': 'Button Label',
      'theme': {
          'fill': '#fff',
          'stroke': '#ccc'
      },
      'title_key': 'somevalue',
      'x': 10,
      'y': 0
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_ContextButtonConfiguration__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_ContextButtonConfiguration__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_ContextButtonConfiguration_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_ContextButtonConfiguration_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/buttons/02.js', False, None),

    ('utility_classes/buttons/error-03.js', False, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),

    ('utility_classes/buttons/02.js', True, None),

    ('utility_classes/buttons/error-03.js', True, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
])
def test_ContextButtonConfiguration_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


STANDARD_PARAMS_3 = [
    ({}, None),
    ({
      'button1': {
        'enabled': True,
        'text': 'Button Label',
        'theme': {
            'fill': '#fff',
            'stroke': '#ccc'
        },
        'y': 0
      },
      'button2': {
        'className': 'some-class-name',
        'enabled': True,
        'menuClassName': 'menu-class',
        'menuItems': ['item1', 'item2'],
        'onclick': """function (event) { return true; }""",
        'symbol': 'menu',
        'symbolFill': '#ccc',
        'text': 'Button Label',
        'theme': {
            'fill': '#fff',
            'stroke': '#ccc'
        },
        'titleKey': 'somevalue',
        'x': 10,
        'y': 0
      }
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_ExportingButtons__init__(kwargs, error):
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
        result = cls3(**kwargs)
        assert result is not None
        assert isinstance(result, cls3) is True
        for key in kwargs:
            if key in ['context_button', 'contextButton']:
                continue
            if isinstance(kwargs[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs[key], str) and kwargs[key].startswith('class'):
                continue

            print(f'after __init__ for key: {key}')
            print(kwargs_copy[key])
            print(result)
            print(result.get(key))
            assert does_kwarg_value_match_result(kwargs_copy[key],
                                                 result.get(key)) is True
    else:
        with pytest.raises(error):
            result = cls3(**kwargs)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_3)
def test_ExportingButtons__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_ExportingButtons_from_dict(kwargs, error):
    as_dict = to_js_dict(deepcopy(kwargs))

    if not error:
        instance = cls3.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, cls3) is True
        for key in kwargs:
            assert does_kwarg_value_match_result(kwargs[key],
                                                 instance.get(key)) is True
    else:
        with pytest.raises(error):
            instance = cls3.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_3)
def test_ExportingButtons_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)
