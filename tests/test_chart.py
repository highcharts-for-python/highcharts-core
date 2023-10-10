"""Tests for ``highcharts.no_data``."""

import pytest
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from json.decoder import JSONDecodeError

from highcharts_core.chart import Chart as cls
from highcharts_core.global_options.shared_options import SharedOptions
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, Class_from_js_literal_with_expected, run_pandas_tests


STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', [
    ({}, errors.HighchartsValueError),
])
def test_bugfix34_SharedOptions_error(kwargs, error):
    shared_options = SharedOptions()
    instance = cls(**kwargs)
    if not error:
        instance.options = shared_options
    else:
        with pytest.raises(error):
            instance.options = shared_options


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
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
     False,
     None),
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
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



@pytest.mark.parametrize('json_str, expected_modules, error', [
    ("""{
    "chart": {
        "type": "column"
    },
    "colors": null,
    "credits": false,
    "exporting": {
        "scale": 1
    },
    "series": [{
        "baseSeries": 1,
        "color": "#434343",
        "name": "Pareto",
        "tooltip": {
            "valueDecimals": 2,
            "valueSuffix": "%"
        },
        "type": "pareto",
        "yAxis": 1,
        "zIndex": 10
    }, {
        "color": "#7cb5ec",
        "data": [1, 23, 45, 54, 84, 13, 8, 7, 23, 1, 34, 6, 8, 99, 85, 23, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],
        "name": "random-name",
        "type": "column",
        "zIndex": 2
    }],
    "title": {
        "text": "Random Name Pareto"
    },
    "tooltip": {
        "shared": true
    },
    "xAxis": {
        "categories": ["Something", "Something", "Something", "Something", "Something", "Something", "Hypovolemia", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something"],
        "crosshair": true,
        "labels": {
            "rotation": 90
        }
    },
    "yAxis": [{
        "title": {
            "text": "count"
        }
    }, {
        "labels": {
            "format": "{value}%"
        },
        "max": 100,
        "maxPadding": 0,
        "min": 0,
        "minPadding": 0,
        "opposite": true,
        "title": {
            "text": "accum percent"
        }
    }]
}""", ['highcharts', 'modules/exporting', 'modules/pareto'], None),
])
def test_get_required_modules(json_str, expected_modules, error):
    from highcharts_core.options import HighchartsOptions
    options = HighchartsOptions.from_json(json_str)
    chart = cls.from_options(options)
    if not error:
        result = chart.get_required_modules()
        if expected_modules:
            assert len(result) == len(expected_modules)
            for item in expected_modules:
                assert item in result
        else:
            assert result is None or len(result) == 0
    else:
        with pytest.raises(error):
            result = chart.get_required_modules()


@pytest.mark.parametrize('options_str, as_str, expected, error', [
    ("""{
        "chart": {
            "type": "column"
        },
        "colors": null,
        "credits": false,
        "exporting": {
            "scale": 1
        },
        "series": [{
            "baseSeries": 1,
            "color": "#434343",
            "name": "Pareto",
            "tooltip": {
                "valueDecimals": 2,
                "valueSuffix": "%"
            },
            "type": "pareto",
            "yAxis": 1,
            "zIndex": 10
        }, {
            "color": "#7cb5ec",
            "data": [1, 23, 45, 54, 84, 13, 8, 7, 23, 1, 34, 6, 8, 99, 85, 23, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],
            "name": "random-name",
            "type": "column",
            "zIndex": 2
        }],
        "title": {
            "text": "Random Name Pareto"
        },
        "tooltip": {
            "shared": true
        },
        "xAxis": {
            "categories": ["Something", "Something", "Something", "Something", "Something", "Something", "Hypovolemia", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something"],
            "crosshair": true,
            "labels": {
                "rotation": 90
            }
        },
        "yAxis": [{
            "title": {
                "text": "count"
            }
        }, {
            "labels": {
                "format": "{value}%"
            },
            "max": 100,
            "maxPadding": 0,
            "min": 0,
            "minPadding": 0,
            "opposite": true,
            "title": {
                "text": "accum percent"
            }
        }]
    }""",
    False,
    [
        '<script src="https://code.highcharts.com/highcharts.js"></script>',
        '<script src="https://code.highcharts.com/modules/exporting.js"></script>',
        '<script src="https://code.highcharts.com/modules/pareto.js"></script>'
    ], None),
    ("""{
        "chart": {
            "type": "column"
        },
        "colors": null,
        "credits": false,
        "exporting": {
            "scale": 1
        },
        "series": [{
            "baseSeries": 1,
            "color": "#434343",
            "name": "Pareto",
            "tooltip": {
                "valueDecimals": 2,
                "valueSuffix": "%"
            },
            "type": "pareto",
            "yAxis": 1,
            "zIndex": 10
        }, {
            "color": "#7cb5ec",
            "data": [1, 23, 45, 54, 84, 13, 8, 7, 23, 1, 34, 6, 8, 99, 85, 23, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],
            "name": "random-name",
            "type": "column",
            "zIndex": 2
        }],
        "title": {
            "text": "Random Name Pareto"
        },
        "tooltip": {
            "shared": true
        },
        "xAxis": {
            "categories": ["Something", "Something", "Something", "Something", "Something", "Something", "Hypovolemia", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something", "Something"],
            "crosshair": true,
            "labels": {
                "rotation": 90
            }
        },
        "yAxis": [{
            "title": {
                "text": "count"
            }
        }, {
            "labels": {
                "format": "{value}%"
            },
            "max": 100,
            "maxPadding": 0,
            "min": 0,
            "minPadding": 0,
            "opposite": true,
            "title": {
                "text": "accum percent"
            }
        }]
    }""",
    True,
    """<script src="https://code.highcharts.com/highcharts.js"></script>\n<script src="https://code.highcharts.com/modules/exporting.js"></script>\n<script src="https://code.highcharts.com/modules/pareto.js"></script>""", None),
])
def test_get_script_tags(options_str, as_str, expected, error):
    from highcharts_core.options import HighchartsOptions
    options = HighchartsOptions.from_json(options_str)
    chart = cls.from_options(options)

    if not error:
        result = chart.get_script_tags(as_str = as_str)
        if isinstance(expected, list):
            assert isinstance(result, list) is True
            assert len(result) == len(expected)
            for item in expected:
                assert item in result
        elif result:
            assert result == expected
        else:
            assert result is None or len(result) == 0
    else:
        with pytest.raises(error):
            result = chart.get_script_tags(as_str = as_str)
            

@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'container': 'my-container-name', 
        'module_url': 'https://mycustomurl.com/', 
        'options': {
            'title': {
                'text': 'My Chart'
            }
        }
    }, None),
])
def test__repr__(kwargs, error):
    obj = cls(**kwargs)
    if not error:
        result = repr(obj)
        if 'options' in kwargs:
            assert 'options = ' in result
    else:
        with pytest.raises(error):
            result = repr(obj)


@pytest.mark.parametrize('kwargs, error', [
    ({}, None),
    ({
        'container': 'my-container-name', 
        'module_url': 'https://mycustomurl.com/', 
        'options': {
            'title': {
                'text': 'My Chart'
            }
        }
    }, None),
])
def test__str__(kwargs, error):
    obj = cls(**kwargs)
    if not error:
        result = str(obj)
        print(result)
        if 'options' in kwargs:
            assert 'options = ' in result
    else:
        with pytest.raises(error):
            result = str(obj)
            

@pytest.mark.parametrize('kwargs, expected_series, expected_data_points, error', [
    ({}, 0, [], None),

    ({
        'series': [
            {
                'data': [[1, 2], [3, 4]],
                'type': 'line'
            }
        ]
    }, 1, [(0, 2)], None),
    ({
        'series': {
            'data': [[1, 2], [3, 4]],
            'type': 'line'
        }
    }, 1, [(0, 2)], None),
    
    ({
        'data': [[1, 2], [3, 4]],
        'series_type': 'line'
    }, 1, [(0, 2)], None),

    ({
        'data': [[1, 2], [3, 4]],
    }, 1, [(0, 2)], errors.HighchartsValueError),

])
def test_issue90_one_shot_creation(kwargs, expected_series, expected_data_points, error):
    if not error:
        result = cls(**kwargs)
        assert result is not None
        if kwargs:
            assert getattr(result, 'options') is not None
            assert getattr(result.options, 'series') is not None
            assert len(result.options.series) == expected_series
            for item in expected_data_points:
                assert len(result.options.series[item[0]].data) == item[1]
    else:
        with pytest.raises(error):
            result = cls(**kwargs)
            

@pytest.mark.parametrize('filename, error', [
    ('test-data-files/nst-est2019-01.csv', None),
])
def test_from_pandas_in_rows(run_pandas_tests, input_files, filename, error):
    if not run_pandas_tests:
        return

    import pandas
    
    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    print(df)
    
    if not error:
        result = cls.from_pandas_in_rows(df)
        assert result is not None
        assert isinstance(result, cls)
        assert len(result.options.series) == len(df)
        for series in result.options.series:
            assert series.data is not None
            assert len(series.data) == len(df.columns)
    else:
        with pytest.raises(error):
            result = cls.from_pandas_in_rows(df)


def prep_df(df):
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    
    return df


def reduce_to_two_columns(df):
    df = df[['Geographic Area', '2010']]
    
    return df


@pytest.mark.parametrize('filename, kwargs, pre_test_df_func, expected_series, expected_data_points, error', [
    # SCENARIO 0: Series in Rows
    ('test-data-files/nst-est2019-01.csv',
     {
         'series_in_rows': True
     },
     prep_df,
     57,
     10,
     None),
    
    # SCENARIO 1a: Has Property Map, Single Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'name': 'Geographic Area',
         },
         'series_in_rows': False
     },
     None,
     1,
     57,
     None),

    # SCENARIO 1b: Has Property Map, Multiple Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'x': ['Geographic Area', '2010']
         },
         'series_in_rows': False
     },
     None,
     2,
     57,
     None),
    
    # SCENARIO 2a: Single Property in KWARGS
    ('test-data-files/nst-est2019-01.csv',
     {
         'x': 'Geographic Area',
         'y': '2010'
     },
     None,
     1,
     57,
     None),
    
    # SCENARIO 3a: Exact Match on Column Count
    ('test-data-files/nst-est2019-01.csv',
     {},
     reduce_to_two_columns,
     1,
     57,
     None),
    
    # SCENARIO 3b: Multiple Series, Multipled Columns
    ('test-data-files/nst-est2019-01.csv',
     {},
     prep_df,
     10,
     57,
     None),

    # SCENARIO 4: Mismatched Columns
    # NOTE: On SeriesBase, this will actually return one series per column.
    # This is because SeriesBase supports 1D arrays.
    ('test-data-files/nst-est2019-01.csv',
     {},
     None,
     11,
     57,
     TypeError),
    
])
def test_from_pandas(run_pandas_tests,
                     input_files,
                     filename,
                     kwargs,
                     pre_test_df_func,
                     expected_series,
                     expected_data_points,
                     error):
    if not run_pandas_tests:
        return

    import pandas

    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    if pre_test_df_func:
        df = pre_test_df_func(df)
    print(df)

    if not error:
        result = cls.from_pandas(df, **kwargs)
        assert result is not None
        assert isinstance(result, cls)
        assert len(result.options.series) == expected_series
        for series in result.options.series:
            assert series.data is not None
            assert len(series.data) == expected_data_points
    else:
        with pytest.raises(error):
            result = cls.from_pandas(df, **kwargs)


@pytest.mark.parametrize('filename, expected_series, expected_data_points, error', [
    ('test-data-files/nst-est2019-01.csv', 57, 10, None),
])
def test_from_csv_in_rows(input_files, filename, expected_series, expected_data_points, error):
    input_file = check_input_file(input_files, filename)
    if not error:
        result = cls.from_csv_in_rows(input_file,
                                      wrapper_character = '"')
        assert result is not None
        assert isinstance(result, cls)
        assert result.options is not None
        assert result.options.series is not None
        assert isinstance(result.options.series, list)
        assert len(result.options.series) == expected_series
        for series in result.options.series:
            assert series.data is not None
            assert len(series.data) == expected_data_points
    else:
        with pytest.raises(error):
            result = cls.from_pandas_in_rows(input_file)


@pytest.mark.parametrize('filename, property_map, kwargs, expected_series, expected_data_points, error', [
    ('test-data-files/nst-est2019-01.csv', 
     {}, 
     {
         'wrapper_character': '"'
     },
     10,
     57,
     None),
    ('test-data-files/nst-est2019-01.csv',
     {
         'name': 'Geographic Area',
         'x': 'Geographic Area',
         'y': '2010'
     },
     {
         'wrapper_character': '"'
     },
     1,
     57,
     None),

    # SCENARIO 0: Series in Rows
    ('test-data-files/nst-est2019-01.csv',
     {},
     {
         'wrapper_character': '"',
         'series_in_rows': True
     },
     57,
     10,
     None),
    
    # SCENARIO 1a: Has Property Map, Single Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'name': 'Geographic Area'
     },
     {
         'wrapper_character': '"',
         'series_in_rows': False
     },
     1,
     57,
     None),

    ('test-data-files/nst-est2019-01.csv',
     {
         'x': 'Geographic Area',
         'y': '2010'
     },
     {
         'wrapper_character': '"'
     },
     1,
     57,
     None),

    # SCENARIO 1b: Has Property Map, Multiple Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'x': ['Geographic Area', '2010']
     },
     {
         'series_in_rows': False,
         'wrapper_character': '"'
          },
     2,
     57,
     None),
    
    # SCENARIO 2a: Single Property in KWARGS
    ('test-data-files/nst-est2019-01.csv',
     {},
     {
         'wrapper_character': '"',
         'x': 'Geographic Area',
         'y': '2010'
     },
     1,
     57,
     None),
    
    # SCENARIO 3a: Exact Match on Column Count
    ('test-data-files/nst-est2019-01-reduced-to-two.csv',
     {},
     {
         'wrapper_character': '"'
     },
     1,
     57,
     None),
    
    # SCENARIO 3b: Multiple Series, Multipled Columns
    ('test-data-files/nst-est2019-01-removed-column.csv',
     {},
     {
         'wrapper_character': '"'
     },
     9,
     57,
     None),

    # SCENARIO 4: Mismatched Columns
    # NOTE: On SeriesBase, this will actually return one series per column.
    # This is because SeriesBase supports 1D arrays.
    ('test-data-files/nst-est2019-01.csv',
     {},
     {
         'wrapper_character': '"'
     },
     10,
     57,
     None),
    
])
def test_from_csv(input_files, filename, property_map, kwargs, expected_series, expected_data_points, error):
    input_file = check_input_file(input_files, filename)
    
    if not error:
        result = cls.from_csv(input_file,
                              property_column_map = property_map,
                              **kwargs)
        assert result is not None
        assert isinstance(result, cls)
        assert result.options is not None
        assert result.options.series is not None
        if isinstance(result.options.series, list):
            assert len(result.options.series) == expected_series
            for series in result.options.series:
                assert series.data is not None
                assert len(series.data) == expected_data_points
    else:
        with pytest.raises(error):
            result = cls.from_csv(input_file,
                                  property_column_map = property_map,
                                  **kwargs)


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
    ], (2, 2), False, True, None),
    
    ('Not an Array', None, True, False, ValueError),
])
def test_from_array(value, expected_shape, has_ndarray, has_data_points, error):
    if has_ndarray is False and has_data_points is False:
        raise AssertionError('Test is invalid. has_ndarray or has_data_points must be '
                             'True. Both were supplied as False.')
    if not error:
        result = cls.from_array(value)
        assert result is not None
        assert result.options.series is not None
        assert len(result.options.series) == 1
        assert result.options.series[0].data is not None

        if has_ndarray:
            data = result.options.series[0].data
            if HAS_NUMPY:
                assert data.ndarray is not None
                assert isinstance(data.ndarray, dict) is True
                for key in data.ndarray:
                    assert data.ndarray[key] is not None
                    assert isinstance(data.ndarray[key], np.ndarray) is True
                    assert data.ndarray[key].shape[0] == expected_shape[0]
            else:
                assert data.array is not None or data.data_points is not None
                if data.array:
                    assert len(data.array) == expected_shape[0]
                else:
                    assert len(data.data_points) == expected_shape[0]
        if has_data_points:
            assert len(result.options.series[0].data) == expected_shape[0]
    else:
        with pytest.raises(error):
            result = cls.from_array(value)
