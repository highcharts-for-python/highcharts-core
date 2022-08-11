"""Tests for ``highcharts.title``."""

import pytest

from validator_collection import checkers

from highcharts.title import Title
from highcharts import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'text': 'Title aligned left',
        'align': 'left',
        'x': 70
    }, None),
    ({
        'text': 'Title floating left',
        'floating': True,
        'align': 'left',
        'x': 100,
        'y': 50
    }, None),
    ({
        'margin': 50
    }, None),
    ({
        'use_html': True
    }, None),
    ({
        'vertical_align': 'middle'
    }, None),
    ({
        'width_adjust': -44
    }, None),

    ({'align': 'not-valid'}, errors.HighchartsValueError),
    ({'x': 'not-valid'}, TypeError),
    ({'vertical_align': 'not-valid'}, errors.HighchartsValueError),
])
def test_Title__init__(kwargs, error):
    if not error:
        result = Title(**kwargs)
        assert result is not None
        assert isinstance(result, Title) is True
        for key in kwargs:
            assert kwargs[key] == getattr(result, key)
    else:
        with pytest.raises(error):
            result = Title(**kwargs)


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'text': 'Title aligned left',
        'align': 'left',
        'x': 70
    }, None),
    ({
        'text': 'Title floating left',
        'floating': True,
        'align': 'left',
        'x': 100,
        'y': 50
    }, None),
    ({
        'use_html': False
    }, None),
    ({
        'margin': 50
    }, None),
    ({
        'vertical_align': 'middle'
    }, None),
    ({
        'width_adjust': -44
    }, None),
])
def test_Title__to_untrimmed_dict(kwargs, error):
    if not error:
        instance = Title(**kwargs)
        result = instance._to_untrimmed_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        for key in kwargs:
            if '_' not in key:
                assert kwargs[key] == result.get(key)
            else:
                if 'html' in key:
                    assert kwargs[key] == result.get('useHTML')
                else:
                    assert kwargs[key] == result.get(to_camelCase(key))
    else:
        with pytest.raises(error):
            instance = Title(**kwargs)
            result = instance._to_untrimmed_dict()


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'text': 'Title aligned left',
        'align': 'left',
        'x': 70
    }, None),
    ({
        'text': 'Title floating left',
        'floating': True,
        'align': 'left',
        'x': 100,
        'y': 50
    }, None),
    ({
        'use_html': False
    }, None),
    ({
        'margin': 50
    }, None),
    ({
        'vertical_align': 'middle'
    }, None),
    ({
        'width_adjust': -44
    }, None),
])
def test_Title_from_dict(kwargs, error):
    as_dict = to_js_dict(kwargs)

    if not error:
        instance = Title.from_dict(as_dict)
        assert instance is not None
        assert isinstance(instance, Title) is True
        for key in kwargs:
            assert kwargs[key] == getattr(instance, key)
    else:
        with pytest.raises(error):
            instance = Title.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'text': 'Title aligned left',
        'align': 'left',
        'x': 70
    }, None),
    ({
        'text': 'Title floating left',
        'floating': True,
        'align': 'left',
        'x': 100,
        'y': 50
    }, None),
    ({
        'use_html': False
    }, None),
    ({
        'margin': 50
    }, None),
    ({
        'vertical_align': 'middle'
    }, None),
    ({
        'width_adjust': -44
    }, None),
])
def test_Title_to_dict(kwargs, error):
    expected = to_js_dict(kwargs)
    for key in expected:
        if expected[key] is None:
            del expected[key]

    if not error:
        instance = Title(**kwargs)
        result = instance.to_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        print(expected)
        print(result)
        assert checkers.are_dicts_equivalent(result, expected) is True
    else:
        with pytest.raises(error):
            instance = Title(**kwargs)
            result = instance.to_dict()


@pytest.mark.parametrize('filename, as_file, error', [
    ('title/title-01.js', False, None),
    ('title/title-02.js', False, None),

    ('title/title-error-01.js', False, errors.HighchartsValueError),
    ('title/title-error-02.js', False, errors.HighchartsParseError),

    ('title/title-01.js', True, None),
    ('title/title-02.js', True, None),

    ('title/title-error-01.js', True, errors.HighchartsValueError),
    ('title/title-error-02.js', True, errors.HighchartsParseError),
])
def test_Title_from_js_literal(input_files, filename, as_file, error):
    input_file = check_input_file(input_files, filename)

    with open(input_file, 'r') as file_:
        as_str = file_.read()

    if as_file:
        input_string = input_file
    else:
        input_string = as_str

    if not error:
        parsed_original, original_str = Title._validate_js_literal(as_str)
        result = Title.from_js_literal(input_string)
        assert result is not None
        assert isinstance(result, Title) is True

        as_js_literal = result.to_js_literal()
        parsed_output, output_str = Title._validate_js_literal(as_js_literal)
        print(as_str)
        print('-----------')
        print(as_js_literal)
        assert str(parsed_output) == str(parsed_original)
    else:
        with pytest.raises(error):
            result = Title.from_js_literal(input_string)
