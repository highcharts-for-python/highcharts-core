"""Unit tests for ``highcharts/utility_functions``"""

import pytest

from abc import ABC, abstractmethod

from highcharts_core import utility_functions


@pytest.mark.parametrize('kwargs, expected_column_names, expected_records, error', [
    ({
        'csv_data': "Date,Header\r\n01/01/2023,2\r\n01/02/2023,4\r\n01/03/2023,8"
     }, ['Date', 'HeadCount'], 3, None),
])
def test_parse_csv(kwargs, expected_column_names, expected_records, error):
    if not error:
        columns, records_as_dicts = utility_functions.parse_csv(**kwargs)
        assert columns is not None
        assert len(columns) == len(expected_column_names)
        
        assert records_as_dicts is not None
        assert len(records_as_dicts) == expected_records
    else:
        with pytest.raises(error):
            result = utility_functions.parse_csv(**kwargs)
            

@pytest.mark.parametrize('camelCase, expected, error', [
    ('camelCase', 'camel_case', None),
    ('camelCaseURL', 'camel_case_url', None),
    ('camel123Case', 'camel123_case', None),
])
def test_to_snake_case(camelCase, expected, error):
    if not error:
        result = utility_functions.to_snake_case(camelCase)
        assert result == expected
    else:
        with pytest.raises(error):
            result = utility_functions.to_snake_case(camelCase)
