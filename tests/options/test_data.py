"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from dotenv import load_dotenv

from highcharts_core.options.data import Data as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, run_pyspark_tests, run_pandas_tests

STANDARD_PARAMS = [
    ({}, None),
    ({
      'csv_url': 'https://www.somewhere.dev/test.csv',
      'data_refresh_rate': 3,
      'decimal_point': '.',
      'enable_polling': True,
      'first_row_as_names': True,
      'item_delimiter': ','
    }, None),
    ({
      'csv_url': '/test.csv',
      'data_refresh_rate': 3,
      'decimal_point': '.',
      'enable_polling': True,
      'first_row_as_names': True,
      'item_delimiter': ','
    }, None),

    ({
      'csv_url': 123,
      'data_refresh_rate': 3,
      'decimal_point': '.',
      'enable_polling': True,
      'first_row_as_names': True,
      'item_delimiter': ','
    }, (ValueError, TypeError)),
]

load_dotenv()


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


@pytest.mark.parametrize('filename, as_file, error', [
    ('data/01.js', False, None),
    ('data/02.js', False, None),

    ('data/error-01.js', False, (errors.HighchartsValueError,
                                 errors.HighchartsParseError,
                                 JSONDecodeError,
                                 ValueError)),
    ('data/error-02.js', False, (errors.HighchartsValueError,
                                 errors.HighchartsParseError,
                                 JSONDecodeError,
                                 ValueError)),

    ('data/01.js', True, None),
    ('data/02.js', True, None),

    ('data/error-01.js', True, (errors.HighchartsValueError,
                                errors.HighchartsParseError,
                                JSONDecodeError,
                                ValueError)),
    ('data/error-02.js', True, (errors.HighchartsValueError,
                                errors.HighchartsParseError,
                                JSONDecodeError,
                                ValueError)),
])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


@pytest.mark.parametrize('filename, kwargs, error', [
    ('test-data-files/nst-est2019-01-transposed.csv', {}, None),
    ('test-data-files/nst-est2019-01-transposed.csv',
     {'represent_as': 'html'},
     None),

])
def test_from_pandas(run_pandas_tests, input_files, filename, kwargs, error):
    if not run_pandas_tests:
        return

    import pandas

    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file)

    if not error:
        result = cls.from_pandas(df, **kwargs)
        assert result is not None
        assert isinstance(result, cls) is True

        if kwargs.get('represent_as', 'csv') == 'csv':
            assert result.csv is not None
            assert result.table is None
            assert isinstance(result.csv, str) is True
        else:
            assert result.csv is None
            assert result.table is not None
            assert isinstance(result.table, str) is True
    else:
        with pytest.raises(error):
            result = cls.from_pandas(df, **kwargs)


@pytest.mark.parametrize('filename, kwargs, error', [
    ('test-data-files/nst-est2019-01-transposed.csv', {}, None),
    ('test-data-files/nst-est2019-01-transposed.csv',
     {'consolidation': 'repartition'},
     None),
    ('test-data-files/nst-est2019-01-transposed.csv',
     {'consolidation': 'coalesce'},
     None),
    ('test-data-files/nst-est2019-01-transposed.csv',
     {'consolidation': None}, 
     None),

])
def test_from_pyspark(input_files, run_pyspark_tests, filename, kwargs, error):
    if run_pyspark_tests:
        from pyspark.sql import SparkSession

        spark = SparkSession.builder.appName('highcharts.tests').getOrCreate()

        input_file = check_input_file(input_files, filename)
        df = spark.read.csv(input_file)

        if not error:
            result = cls.from_pyspark(df, **kwargs)
            assert result is not None
            assert isinstance(result, cls) is True

            assert result.csv is not None
            assert result.table is None
            assert isinstance(result.csv, str) is True
        else:
            with pytest.raises(error):
                result = cls.from_pyspark(df, **kwargs)
