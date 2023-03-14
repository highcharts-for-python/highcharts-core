# -*- coding: utf-8 -*-

"""
***********************************
tests._fixtures
***********************************

Fixtures used by the SQLAthanor test suite.

"""
import os
import pathlib
from copy import deepcopy
from collections import UserDict

import pytest

from validator_collection import checkers, validators
from highcharts_core import constants


class State(object):
    """Class to hold incremental test state."""
    # pylint: disable=too-few-public-methods
    pass


@pytest.fixture
def state(request):
    """Return the :class:`State` object that holds incremental test state."""
    # pylint: disable=W0108
    return request.cached_setup(
        setup = lambda: State(),
        scope = "session"
    )


@pytest.fixture
def run_pyspark_tests(request):
    """Return the ``--pyspark`` command-line option."""
    value = request.config.getoption("--pyspark")
    value = value.lower()
    if value in ['false', False, 0, 'no', 'no']:
        return False
    else:
        return True


@pytest.fixture
def run_download_tests(request):
    """Return the ``--downloads`` command-line option."""
    value = request.config.getoption("--downloads")
    value = value.lower()
    if value in ['false', False, 0, 'no', 'no']:
        return False
    else:
        return True


@pytest.fixture
def input_files(request):
    """Return the ``--inputs`` command-line option."""
    return request.config.getoption("--inputs")

@pytest.fixture
def create_output_directory(request):
    """Return the ``--create-output-directory`` command-line option."""
    value = request.config.getoption("--create-output-directory")
    value = value.lower()
    if value in ['false', False, 0, 'no', 'no']:
        return False
    else:
        return True


def check_input_file(input_directory, input_value, create_directory = False):
    inputs = os.path.abspath(input_directory)
    if not os.path.exists(input_directory) and not create_directory:
        raise AssertionError('input directory (%s) does not exist' % inputs)
    elif not os.path.exists(input_directory) and create_directory:
        pathlib.Path(input_directory).mkdir(parents = True, exist_ok = True)
    elif not os.path.isdir(input_directory):
        raise AssertionError('input directory (%s) is not a directory' % inputs)

    try:
        input_file = os.path.join(input_directory, input_value)
    except (TypeError, AttributeError):
        input_file = None

    if input_file is not None:
        input_value = input_file

    return input_value


def to_camelCase(variable_name):
    if '_' not in variable_name:
        return variable_name

    if 'url' in variable_name:
        variable_name = variable_name.replace('url', 'URL')

    camel_case = ''
    previous_character = ''
    for character in variable_name:
        if character != '_' and previous_character != '_':
            camel_case += character
            previous_character = character
        elif character == '_':
            previous_character = character
        elif character != '_' and previous_character == '_':
            camel_case += character.upper()
            previous_character = character

    return camel_case


def to_js_dict(original):
    print(f'\n{original}\n')
    as_dict = {}
    for key in original:
        if 'use_html' in key:
            new_key = 'useHTML'
        elif key == 'allow_html':
            new_key = 'allowHTML'
        elif 'utc' in key:
            new_key = 'useUTC'
        elif '_csv' in key:
            new_key = 'downloadCSV'
        elif '_jpeg' in key:
            new_key = 'downloadJPEG'
        elif '_pdf' in key:
            new_key = 'downloadPDF'
        elif '_png' in key:
            new_key = 'downloadPNG'
        elif '_svg' in key:
            new_key = 'downloadSVG'
        elif '_xls' in key:
            new_key = 'downloadXLS'
        elif '_atr' in key:
            new_key = key.replace('_atr', 'ATR')
        elif key == 'drillup_text':
            new_key = 'drillUpText'
        elif key == 'drillup_button':
            new_key = 'drillUpButton'
        elif key == 'thousands_separator':
            new_key = 'thousandsSep'
        elif key == 'measure_xy':
            new_key = 'measureXY'
        elif key == 'use_gpu_translations':
            new_key = 'useGPUTranslations'
        elif key == 'label_rank':
            new_key = 'labelrank'
        else:
            new_key = to_camelCase(key)

        as_dict[new_key] = original[key]

    return as_dict


def does_kwarg_value_match_result(kwarg_value, result_value):
    """Validate whether the value of ``kwarg_value`` matches the value of ``result_value``.

    :returns: ``True`` if match, ``False`` if not
    """
    print(f'EVALUATING KWARG_VALUE:\n{kwarg_value}')
    print(f'  against\n    {result_value}')
    if isinstance(kwarg_value, (dict,
                                UserDict)) and not isinstance(result_value, (dict,
                                                                             UserDict)):
        print('- converting KWARG dict back to object INSTANCE')
        result_cls = result_value.__class__
        try:
            test_value = result_cls.from_dict(kwarg_value)
        except AttributeError:
            if not result_value and not kwarg_value:
                return True
            else:
                return False

        ('-- converted INSTANCE as JS literal:')
        print(test_value.to_js_literal())
        print('-- original result as JS literal:')
        print(result_value.to_js_literal())

        return test_value == result_value
    elif not isinstance(kwarg_value, (int, float)) and isinstance(result_value, (int,
                                                                                 float)):
        print('- converting KWARG value into numeric')
        test_value = validators.numeric(kwarg_value)
        return test_value == result_value
    elif isinstance(kwarg_value, (int, float)) and not isinstance(result_value, (int,
                                                                                 float)):
        print('- converting RESULT value into numeric')
        result_value = validators.numeric(result_value)
        return test_value == result_value
    elif isinstance(kwarg_value, (dict,
                                  UserDict)) and isinstance(result_value, (dict,
                                                                           UserDict)):
        print('- checking two dict objects')
        if len(kwarg_value) != len(result_value):
            print('-- len does not match')
            return False
        for key in kwarg_value:
            print(f'CHECKING: {key}')
            if key == 'patternOptions':
                matches = does_kwarg_value_match_result(kwarg_value.get(key),
                                                        result_value.get('pattern'))
            else:
                matches = does_kwarg_value_match_result(kwarg_value.get(key),
                                                        result_value.get(key))
            if not matches:
                print(f'-- dict key ({key}) does not match')
                return False

        return True
    elif checkers.is_iterable(kwarg_value):
        print('- evaluating a KWARG value that is iterable')
        if hasattr(result_value, 'from_setter'):
            print('- converting iterable to a HighchartsMeta from_setter()')
            updated_kwarg_value = result_value.__class__.from_array([kwarg_value])[0]
            matches = does_kwarg_value_match_result(updated_kwarg_value, result_value)
            return matches
        elif len(kwarg_value) != len(result_value):
            print('-- len does not match')
            return False
        counter = 0
        for item in kwarg_value:
            print('-- processing items in KWARG iterable')
            result_item = result_value[counter]
            print(f'-- evaluating:\n   {item}')
            print(f'-- against:\n   {result_item}')
            item_match = does_kwarg_value_match_result(item, result_item)
            if not item_match:
                print('-- DOES NOT MATCH')
                return False
            counter += 1
    elif kwarg_value is None and result_value is not None:
        print('- converting None to "null" to check')
        if result_value == 'null' or isinstance(result_value, constants.EnforcedNullType):
            return True
        else:
            return False
    elif isinstance(kwarg_value, str) and isinstance(result_value, dict):
        print('- checking function string against function dict')
        if 'body' in result_value and kwarg_value.startswith('function'):
            return True
        else:
            return False
    else:
        print('- falling back to simple equivalency check')
        return kwarg_value == result_value

    return True


def trim_expected(expected):
    """Remove keys from ``expected`` or its children that should not be evaluated."""
    new_dict = {}
    if not isinstance(expected, dict):
        return expected
    for key in expected:
        if expected[key] is None:
            continue
        elif isinstance(expected[key], dict):
            trimmed_value = trim_expected(expected[key])
            if trimmed_value:
                new_dict[key] = trimmed_value
        elif checkers.is_iterable(expected[key]):
            trimmed_value = []
            for item in expected[key]:
                trimmed_item = trim_expected(item)
                if trimmed_item:
                    trimmed_value.append(trimmed_item)

            if trimmed_value:
                new_dict[key] = trimmed_value
        else:
            new_dict[key] = expected[key]

    return new_dict


def compare_js_literals(original, new):
    if not isinstance(original, str):
        original = str(original)
    if not isinstance(new, str):
        new = str(new)

    counter = 0
    for char in original:
        min_index = max(0, counter - 20)
        max_index = min(counter + 20, len(original))

        if new[counter] != char:
            print(f'\nMISMATCH FOUND AT ORIGINAL CHARACTER: {counter}')
            print(f'-- ORIGINAL: {original[min_index:max_index]}')
            print(f'-- NEW: {new[min_index:max_index]}')
            break

        counter += 1


def Class__init__(cls, kwargs, error):
    kwargs_copy = deepcopy(kwargs)
    if not error:
        result = cls(**kwargs)
        print(kwargs_copy)
        assert result is not None
        assert isinstance(result, cls) is True
        if checkers.is_type(result, 'GenericTypeOptions'):
            kwargs_copy['type'] = result.type
            #kwargs['type'] = result.type
        for key in kwargs_copy:
            print(f'CHECKING: {key}')
            if kwargs.get(key) and isinstance(kwargs_copy[key],
                                              str) and kwargs[key].startswith('function'):
                continue
            if kwargs.get(key) and isinstance(kwargs_copy[key],
                                              str) and kwargs[key].startswith('class'):
                continue
            if key == 'type' and checkers.is_type(result, 'GenericTypeOptions'):
                assert does_kwarg_value_match_result(kwargs_copy[key],
                                                     getattr(result, 'type'))
            elif key == 'margin' and checkers.is_type(result, 'ChartOptions'):
                print(f'CHECKING: {key}, which gets split over other values')
                if checkers.is_iterable(kwargs_copy[key]):
                    print('is iterable')
                    assert does_kwarg_value_match_result(kwargs_copy[key][0],
                                                         getattr(result, 'margin_top'))
                    assert does_kwarg_value_match_result(kwargs_copy[key][1],
                                                         getattr(result, 'margin_right'))
                    assert does_kwarg_value_match_result(kwargs_copy[key][2],
                                                         getattr(result, 'margin_bottom'))
                    assert does_kwarg_value_match_result(kwargs_copy[key][3],
                                                         getattr(result, 'margin_left'))
                elif kwargs_copy[key]:
                    print('not iterable')
                    print('checking margin_top')
                    print(result.margin_top)
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         getattr(result, 'margin_top'))
                    print('checking margin_right')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         getattr(result, 'margin_right'))
                    print('checking margin_bottom')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         getattr(result, 'margin_bottom'))
                    print('checking margin_left')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         getattr(result, 'margin_left'))
            else:
                print('not margin')
                kwarg_value = kwargs_copy[key]
                result_value = getattr(result, key)
                print(f'KWARG VALUE:\n{kwarg_value}')
                print(f'RESULT VALUE:\n{result_value}')
                assert does_kwarg_value_match_result(kwargs_copy[key],
                                                     getattr(result, key)) is True
    else:
        with pytest.raises(error):
            result = cls(**kwargs)


def Class__to_untrimmed_dict(cls, kwargs, error):
    kwargs_copy = deepcopy(kwargs)
    if not error:
        instance = cls(**kwargs)
        result = instance._to_untrimmed_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        if checkers.is_type(instance, 'GenericTypeOptions'):
            print('updating the type!')
            kwargs_copy['type'] = instance.type

        for key in kwargs_copy:
            kwarg_value = kwargs_copy[key]
            result_value = result.get(key)

            if kwargs.get(key) and isinstance(kwargs_copy[key],
                                              str) and kwargs[key].startswith('function'):
                continue
            if kwargs.get(key) and isinstance(kwargs_copy[key],
                                              str) and kwargs[key].startswith('class'):
                continue
            if '_' not in key and (key != 'margin' and not checkers.is_type(instance,
                                                                            'ChartOptions')):
                assert does_kwarg_value_match_result(kwargs_copy[key],
                                                     result.get(key)) is True
            else:
                if 'use_html' in key:
                    print(f'CHECKING: {key}')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get('useHTML')) is True
                elif key == 'allow_html':
                    print(f'CHECKING: {key}')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get('allowHTML')) is True
                elif 'utc' in key:
                    print(f'CHECKING: {key}')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get('useUTC')) is True
                elif 'url' in key:
                    print(f'CHECKING: {key}')
                    updated_key = key.replace('url', 'URL')
                    matches = does_kwarg_value_match_result(
                        kwargs_copy[key],
                        result.get(to_camelCase(updated_key))
                    )
                    assert matches is True
                elif '_kd_tree' in key:
                    updated_key = key.replace('_kd_tree', 'KDTree')
                    matches = does_kwarg_value_match_result(
                        kwargs_copy[key],
                        result.get(to_camelCase(updated_key))
                    )
                    assert matches is True
                elif key == 'use_gpu_translations':
                    updated_key = 'useGPUTranslations'
                    print(f'using key: {updated_key}')
                    matches = does_kwarg_value_match_result(
                        kwargs_copy[key],
                        result.get(to_camelCase(updated_key))
                    )
                    assert matches is True
                elif '_csv' in key:
                    print(f'CHECKING: {key}')
                    new_key = 'downloadCSV'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif '_jpeg' in key:
                    print(f'CHECKING: {key}')
                    new_key = 'downloadJPEG'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif '_pdf' in key:
                    print(f'CHECKING: {key}')
                    new_key = 'downloadPDF'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif '_png' in key:
                    print(f'CHECKING: {key}')
                    new_key = 'downloadPNG'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif '_svg' in key:
                    print(f'CHECKING: {key}')
                    new_key = 'downloadSVG'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif '_xls' in key:
                    print(f'CHECKING: {key}')
                    new_key = 'downloadXLS'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif '_atr' in key:
                    print(f'CHECKING: {key}')
                    new_key = key.replace('_atr', 'ATR')
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif key == 'drillup_text':
                    print(f'CHECKING: {key}')
                    new_key = 'drillUpText'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif key == 'drillup_button':
                    print(f'CHECKING: {key}')
                    new_key = 'drillUpButton'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif key == 'thousands_separator':
                    print(f'CHECKING: {key}')
                    new_key = 'thousandsSep'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif key == 'measure_xy':
                    print(f'CHECKING: {key}')
                    new_key = 'measureXY'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                elif key == 'pattern_options':
                    print(f'CHECKING: {key}')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get('pattern')) is True
                elif isinstance(instance, UserDict):
                    print(f'CHECKING: {key}')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get(key)) is True
                elif key == 'margin' and checkers.is_type(instance, 'ChartOptions'):
                    print(f'CHECKING: {key}, which gets split over other values')
                    if checkers.is_iterable(kwargs_copy[key]):
                        assert does_kwarg_value_match_result(kwargs_copy[key][0],
                                                             result.get('marginTop'))
                        assert does_kwarg_value_match_result(kwargs_copy[key][1],
                                                             result.get('marginRight'))
                        assert does_kwarg_value_match_result(kwargs_copy[key][2],
                                                             result.get('marginBottom'))
                        assert does_kwarg_value_match_result(kwargs_copy[key][3],
                                                             result.get('marginLeft'))
                    elif kwargs_copy[key]:
                        print('EVALUATING single margin value to list')
                        assert does_kwarg_value_match_result([kwargs_copy[key],
                                                              kwargs_copy[key],
                                                              kwargs_copy[key],
                                                              kwargs_copy[key]],
                                                             result.get('margin'))
                        assert does_kwarg_value_match_result(kwargs_copy[key],
                                                             result.get('marginTop'))
                        assert does_kwarg_value_match_result(kwargs_copy[key],
                                                             result.get('marginRight'))
                        assert does_kwarg_value_match_result(kwargs_copy[key],
                                                             result.get('marginBottom'))
                        assert does_kwarg_value_match_result(kwargs_copy[key],
                                                             result.get('marginLeft'))
                elif key == 'spacing' and checkers.is_type(instance, 'ChartOptions'):
                    print(f'CHECKING: {key}, which gets split over other values')
                    if checkers.is_iterable(kwargs_copy[key]):
                        assert does_kwarg_value_match_result(kwargs_copy[key][0],
                                                             result.get('spacingTop'))
                        assert does_kwarg_value_match_result(kwargs_copy[key][1],
                                                             result.get('spacingRight'))
                        assert does_kwarg_value_match_result(kwargs_copy[key][2],
                                                             result.get('spacingBottom'))
                        assert does_kwarg_value_match_result(kwargs_copy[key][3],
                                                             result.get('spacingLeft'))
                    elif kwargs_copy[key]:
                        print('EVALUATING single spacing value to list')
                        assert does_kwarg_value_match_result([kwargs_copy[key],
                                                              kwargs_copy[key],
                                                              kwargs_copy[key],
                                                              kwargs_copy[key]],
                                                             result.get('spacing'))
                elif key == 'label_rank':
                    new_key = 'labelrank'
                    matches = does_kwarg_value_match_result(kwargs_copy[key],
                                                            result.get(new_key))
                    assert matches is True
                else:
                    print(f'CHECKING: {key}')
                    assert does_kwarg_value_match_result(kwargs_copy[key],
                                                         result.get(to_camelCase(key))) is True
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            result = instance._to_untrimmed_dict()


def Class_from_dict(cls, kwargs, error):
    if kwargs:
        as_dict = to_js_dict(deepcopy(kwargs))
    else:
        as_dict = {}

    if not error:
        instance = cls.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, cls) is True
        for key in kwargs:
            print(f'CHECKING: {key}')
            if isinstance(kwargs[key], str) and kwargs[key].startswith('function'):
                continue
            if isinstance(kwargs[key], str) and kwargs[key].startswith('class'):
                continue
            elif key == 'margin' and checkers.is_type(instance, 'ChartOptions'):
                print(f'CHECKING: {key}, which gets split over other values')
                if checkers.is_iterable(kwargs[key]):
                    print('is iterable')
                    assert does_kwarg_value_match_result(kwargs[key][0],
                                                         getattr(instance, 'margin_top'))
                    assert does_kwarg_value_match_result(kwargs[key][1],
                                                         getattr(instance, 'margin_right'))
                    assert does_kwarg_value_match_result(kwargs[key][2],
                                                         getattr(instance, 'margin_bottom'))
                    assert does_kwarg_value_match_result(kwargs[key][3],
                                                         getattr(instance, 'margin_left'))
                elif kwargs[key]:
                    print('not iterable')
                    print('checking margin_top')
                    assert does_kwarg_value_match_result(kwargs[key],
                                                         getattr(instance, 'margin_top'))
                    print('checking margin_right')
                    assert does_kwarg_value_match_result(kwargs[key],
                                                         getattr(instance, 'margin_right'))
                    print('checking margin_bottom')
                    assert does_kwarg_value_match_result(kwargs[key],
                                                         getattr(instance, 'margin_bottom'))
                    print('checking margin_left')
                    assert does_kwarg_value_match_result(kwargs[key],
                                                         getattr(instance, 'margin_left'))
            else:
                kwarg_value = kwargs[key]
                if key in ['pattern_options', 'patternOptions']:
                    result_value = getattr(instance, 'pattern_options')
                elif key == 'type':
                    result_value = getattr(instance, 'type')
                else:
                    result_value = getattr(instance, key)
                print(kwarg_value)
                print(result_value)
                assert does_kwarg_value_match_result(kwarg_value, result_value)
    else:
        with pytest.raises(error):
            instance = cls.from_dict(as_dict)


def Class_to_dict(cls, kwargs, error):
    untrimmed_expected = to_js_dict(deepcopy(kwargs))
    expected = trim_expected(untrimmed_expected)
    check_dicts = True
    for key in expected:
        if not checkers.is_type(expected[key], (str, int, float, bool, list, dict)):
            check_dicts = False
        elif isinstance(expected[key], str) and expected[key].startswith('function'):
            check_dicts = False
        elif isinstance(expected[key], str) and expected[key].startswith('class'):
            check_dicts = False

    if not error:
        instance = cls(**kwargs)
        if checkers.is_type(instance, 'GenericTypeOptions'):
            expected['type'] = instance.type

        result = instance.to_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        print('EXPECTED:')
        print(expected)
        print('RESULT:')
        print(result)
        if checkers.is_type(instance, ('MarkerAttributeObject')):
            check_dicts = False
        if check_dicts:
            if 'contextButton' not in result and 'context_button' not in result:
                assert len(expected) == len(result)
            else:
                assert len(result) == len(expected) + 1
            for key in expected:
                print(f'CHECKING: {key}')
                if key == 'patternOptions':
                    print('running special check for patternOptions')
                    assert does_kwarg_value_match_result(expected[key],
                                                         result.get('pattern')) is True
                elif key in ['contextButton', 'context_button']:
                    continue
                else:
                    assert does_kwarg_value_match_result(expected[key],
                                                         result.get(key)) is True
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            result = instance.to_dict()


def append_plot_options_type(cls, as_str):
    """Append a JavaScript Literal ``type`` value to ``as_str`` based on ``cls``.

    :returns: An updated ``as_str``.
    :rtype: :class:`str <python:str>`
    """
    class_name = cls.__name__
    class_parents = cls.mro()
    is_generic_type_options = False
    for parent in class_parents:
        if 'GenericTypeOptions' in parent.__name__:
            is_generic_type_options = True
            break
    if not is_generic_type_options:
        return as_str
    class_name = class_name.replace('TypeOptions', '')
    class_name = class_name.replace('Options', '')
    if class_name.endswith('Series') and class_name != 'Series':
        class_name = class_name.replace('Series', '')

    class_name = class_name.lower()
    str_to_append = f"""type: '{class_name}'"""

    if str_to_append not in as_str:
        as_str = as_str[:-2] + """,\n  """ + str_to_append + """}"""

    return as_str


def Class_from_js_literal(cls, input_files, filename, as_file, error):
    input_file = check_input_file(input_files, filename)

    with open(input_file, 'r') as file_:
        as_str = file_.read()

    if as_file:
        input_string = input_file
    else:
        input_string = as_str

    as_str = append_plot_options_type(cls, as_str)

    if not error:
        #print('-------------------')
        #print('ORIGINAL VALIDATION')
        parsed_original, original_str = cls._validate_js_literal(as_str, range = False)
        #print('-------------')
        #print('ORIGINAL CALL')
        #print(as_str)
        result = cls.from_js_literal(input_string)
        assert result is not None
        assert isinstance(result, cls) is True

        as_js_literal = result.to_js_literal()
        #print('-----------------')
        #print('RESULT VALIDATION')
        if 'pattern:' in as_js_literal:
            as_js_literal = as_js_literal.replace('pattern:', 'patternOptions:')

        #print(as_js_literal)
        parsed_output, output_str = cls._validate_js_literal(as_js_literal, range = False)
        try:
            assert str(parsed_output) == str(parsed_original)
        except AssertionError as error:
            print('\n')
            compare_js_literals(str(parsed_original), str(parsed_output))
            raise error
    else:
        with pytest.raises(error):
            result = cls.from_js_literal(input_string)


def Class_from_js_literal_with_expected(cls,
                                        input_files,
                                        filename,
                                        expected_filename,
                                        as_file,
                                        error):
    input_file = check_input_file(input_files, filename)
    expected_file = check_input_file(input_files, expected_filename)

    with open(input_file, 'r') as file_:
        as_str = file_.read()

    with open(expected_file, 'r') as file_:
        expected_as_str = file_.read()

    if as_file:
        input_string = input_file
        expected_string = expected_file
    else:
        input_string = as_str
        expected_string = expected_as_str

    as_str = append_plot_options_type(cls, as_str)

    if not error:
        # print('-------------------')
        # print('ORIGINAL VALIDATION')
        parsed_expected, parsed_expected_str = cls._validate_js_literal(expected_string,
                                                                        range = False)
        # print('-------------')
        # print('ORIGINAL CALL')
        # print(as_str)
        result = cls.from_js_literal(input_string)
        assert result is not None
        assert isinstance(result, cls) is True

        as_js_literal = result.to_js_literal()
        # print('-----------------')
        # print('RESULT VALIDATION')
        if 'pattern:' in as_js_literal:
            as_js_literal = as_js_literal.replace('pattern:', 'patternOptions:')

        # print(as_js_literal)
        parsed_output, output_str = cls._validate_js_literal(as_js_literal, range = False)
        try:
            assert str(parsed_output) == str(parsed_expected)
        except AssertionError as error:
            print('\n')
            compare_js_literals(str(parsed_expected), str(parsed_output))
            raise error
    else:
        with pytest.raises(error):
            result = cls.from_js_literal(input_string)
