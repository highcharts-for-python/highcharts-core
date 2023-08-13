"""Tests for ``highcharts.no_data``."""

import pytest
from copy import deepcopy

from json.decoder import JSONDecodeError

from highcharts_core.utility_classes.buttons import ButtonConfiguration as cls
from highcharts_core.utility_classes.buttons import ContextButtonConfiguration as cls2
from highcharts_core.utility_classes.buttons import ExportingButtons as cls3
from highcharts_core.utility_classes.buttons import NavigationButtonConfiguration as cls4
from highcharts_core.utility_classes.buttons import ButtonTheme as cls5
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
          'padding': None,
          'states': None,
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
          'padding': None,
          'states': None,
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
            'padding': None,
            'states': None,
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
            'padding': None,
            'states': None,
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


def test_issue84_ExportingButtons_as_ContextButtonConfiguration():
    as_dict = {
        'contextButton': {
            'enabled': False
        },
        'exportButton': {
            'text': "Download",
            'menuItems': ['downloadPNG']
        }
    }
    instance = cls3.from_dict(as_dict)
    for key in as_dict:
        print({f'Instance: {instance.to_json()}'})
        print({f'Instance: {instance.to_js_literal()}'})
        assert key in instance
        assert does_kwarg_value_match_result(as_dict[key],
                                             instance.get(key)) is True


STANDARD_PARAMS_4 = [
    ({}, None),
    ({
        'use_html': True
    }, None),
]

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_NavigationButtonConfiguration__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_NavigationButtonConfiguration__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_NavigationButtonConfiguration_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_NavigationButtonConfiguration_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/buttons/03.js', False, None),
    ('utility_classes/buttons/04.js', False, None),

    ('utility_classes/buttons/error-01.js', False, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),

    ('utility_classes/buttons/03.js', True, None),
    ('utility_classes/buttons/04.js', True, None),

    ('utility_classes/buttons/error-01.js', True, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
])
def test_NavigationButtonConfiguration_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)


STANDARD_PARAMS_5 = [
    ({'fill': None, 'padding': None, 'stroke': None, 'states': None}, None),
    ({
        'fill': '#ccc',
        'padding': 6,
        'stroke': '#000',
        'states': {
            'hover': {
                'color': '#000'
            }
        },
        'style': {
            'fontSize': '30px',
            'color': '#888'
        },
    }, None),
]

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_5)
def test_ButtonTheme__init__(kwargs, error):
    Class__init__(cls5, kwargs, error, check_as_dict = True)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_5)
def test_ButtonTheme__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_5)
def test_ButtonTheme_from_dict(kwargs, error):
    Class_from_dict(cls5, kwargs, error, check_as_dict = True)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_5)
def test_ButtonTheme_to_dict(kwargs, error):
    Class_to_dict(cls5, kwargs, error, trim_expected = False)


@pytest.mark.parametrize('filename, as_file, error', [
    ('utility_classes/buttons/06.js', False, None),

    ('utility_classes/buttons/error-01.js', False, (errors.HighchartsValueError,
                                                    errors.HighchartsParseError,
                                                    JSONDecodeError,
                                                    TypeError,
                                                    ValueError)),

    ('utility_classes/buttons/06.js', True, None),

    ('utility_classes/buttons/error-01.js', True, (errors.HighchartsValueError,
                                                   errors.HighchartsParseError,
                                                   JSONDecodeError,
                                                   TypeError,
                                                   ValueError)),
])
def test_ButtonTheme_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls5, input_files, filename, as_file, error)
    
    
def test_issue86_ButtonTheme_to_json():
    try:
        import orjson as json
    except ImportError:
        print('using standard library')
        import json

    kwargs = STANDARD_PARAMS_5[1][0]
    instance = cls5(**kwargs)
    
    assert instance['states'] is not None
    assert instance['states'].hover is not None
    
    input_as_json = json.dumps(kwargs)
    print(type(input_as_json))
    
    result_as_json = instance.to_json()
    if isinstance(result_as_json, str) and isinstance(input_as_json, bytes):
        result_as_json = result_as_json.encode('utf-8')
    elif isinstance(result_as_json, bytes) and isinstance(input_as_json, str):
        input_as_json = input_as_json.encode('utf-8')

    assert result_as_json == input_as_json