"""Tests for ``highcharts.no_data``."""
from copy import deepcopy
import pytest

from json.decoder import JSONDecodeError
from validator_collection import checkers

from highcharts_core.headless_export import ExportServer as cls
from highcharts_core.options import HighchartsOptions
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, run_download_tests, create_output_directory

STANDARD_PARAMS = [
    ({}, None),
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
    from tests.fixtures import trim_expected_dict, does_kwarg_value_match_result
    from validator_collection import checkers

    kwargs_copy = deepcopy(kwargs)
    if not kwargs:
        kwargs_copy['url'] = 'https://export.highcharts.com'
        kwargs_copy['format'] = 'png'
        kwargs_copy['scale'] = 1
        kwargs_copy['use_base64'] = False
        kwargs_copy['no_download'] = False
        kwargs_copy['async_rendering'] = False
        kwargs_copy['constructor'] = 'Chart'

        untrimmed_expected = {
            'url': kwargs_copy['url'],
            'type': kwargs_copy['format'],
            'scale': kwargs_copy['scale'],
            'constr': kwargs_copy['constructor'],
            'b64': kwargs_copy['use_base64'],
            'noDownload': kwargs_copy['no_download'],
            'asyncRendering': kwargs_copy['async_rendering']
        }

    else:
        untrimmed_expected = to_js_dict(deepcopy(kwargs))

    expected = trim_expected_dict(untrimmed_expected)
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
        result = instance.to_dict()
        assert result is not None
        assert isinstance(result, dict) is True
        print('EXPECTED:')
        print(expected)
        print('RESULT:')
        print(result)
        if check_dicts:
            assert len(expected) == len(result)
            for key in expected:
                print(f'CHECKING: {key}')
                assert does_kwarg_value_match_result(expected[key],
                                                     result.get(key)) is True
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            result = instance.to_dict()


@pytest.mark.parametrize('value, error', [
    ({
        'url': 'https://export.highcharts.com',
        'protocol': 'https',
        'domain': 'export.highcharts.com',
        'port': None,
        'path': None
    }, None),
    ({
        'url': 'https://export.highcharts.com:1234/some_path_goes_here/andcontinueshere',
        'protocol': 'https',
        'domain': 'export.highcharts.com',
        'port': 1234,
        'path': 'some_path_goes_here/andcontinueshere'
    }, None),
    ({
        'url': 'http://www.highcharts.com/some_path_goes_here/andcontinueshere',
        'protocol': 'http',
        'domain': 'www.highcharts.com',
        'port': None,
        'path': 'some_path_goes_here/andcontinueshere'
    }, None),
    ({
        'url': 'http://www.highcharts.com:8080',
        'protocol': 'http',
        'domain': 'www.highcharts.com',
        'port': 8080,
        'path': None
    }, None),
])
def test_url(value, error):
    instance = cls()
    if not error:
        if 'expected_url' not in value and 'url' in value:
            value['expected_url'] = value.get('url')

        url = value.get('url', None)

        instance.url = url
        assert instance.url is not None
        assert instance.url == value.get('expected_url')
        assert instance.protocol == value.get('protocol')
        assert instance.domain == value.get('domain')
        assert instance.port == value.get('port')
        assert instance.path == value.get('path')
    else:
        with pytest.raises(error):
            instance.url = value.get('url')


@pytest.mark.parametrize('input_filename, target_filename, kwargs, error', [
    ('headless_export/basic.json',
     'headless_export/output/test-basic.png',
     {
      'timeout': 5,
      'format_': 'png',
      'constructor': 'Chart'
     },
     None),
    ('headless_export/with-series-types.js',
     'headless_export/output/test-with-series-types.png',
     {
      'timeout': 5,
      'format_': 'png',
      'constructor': 'Chart'
     },
     None),
    ('headless_export/with-chart-type.js',
     'headless_export/output/test-with-chart-type.png',
     {
      'timeout': 5,
      'format_': 'png',
      'constructor': 'Chart'
     },
     None),
    ('headless_export/with-chart-type.js',
     'headless_export/output/test-with-chart-type.svg',
     {
      'timeout': 5,
      'format_': 'svg',
      'constructor': 'Chart'
     },
     None),
])
def test_get_chart(input_files,
                   run_download_tests,
                   create_output_directory,
                   input_filename,
                   target_filename,
                   kwargs,
                   error):
    if run_download_tests:
        input_file = check_input_file(input_files, input_filename)
        target_file = check_input_file(input_files, 
                                       target_filename,
                                       create_directory = create_output_directory)
        
        with open(input_file, 'r') as file_:
            as_str = file_.read()

        options = HighchartsOptions.from_js_literal(as_str)

        kwargs['options'] = options

        if target_filename:
            kwargs['filename'] = target_file

        if not error:
            result = cls.get_chart(**kwargs)
    
            format = kwargs.get('format_', None)
            print(f'TESTING FORMAT: {format}')
    
            assert result is not None
            if target_filename:
                assert checkers.is_on_filesystem(target_file) is True
                if format == 'svg':
                    with open(target_file, 'r', encoding = 'utf-8') as file_:
                        file_contents = file_.read()
                    contents = str(file_contents)
                    assert contents.startswith(
                        '<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"'
                    ) is True
