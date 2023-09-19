"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError
from validator_collection import checkers

from highcharts_core.options.series.base import SeriesBase as cls
from highcharts_core import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'data': [
          {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          },
          {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3
    }, None),
    # Series Options only
    ({
      'data': [
          {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          },
          {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3,

      'animation_limit': 10,
      'boost_blending': '#ccc',
      'boost_threshold': 1234,
      'color_axis': 1,
      'color_index': 5,
      'color_key': 'some-key-value',
      'connect_ends': True,
      'connect_nulls': True,
      'crisp': True,
      'crop_threshold': 123,
      'data_sorting': {
          'enabled': True,
          'matchByName': True,
          'sortKey': 'some-key-value'
      },
      'drag_drop': {
          'draggableX': True,
          'draggableY': True,
          'dragHandle': {
              'className': 'draghandle-classname-goes-here',
              'color': '#ccc',
              'cursor': 'alias',
              'lineColor': '#ddd',
              'lineWidth': 2,
              'pathFormatter': """function() { return true; }""",
              'zIndex': 10
          },
          'dragMaxX': 3456,
          'dragMaxY': 6532,
          'dragMinX': 123,
          'dragMinY': 321,
          'dragPrecisionX': 5,
          'dragPrecisionY': 5,
          'dragSensitivity': 2,
          'groupBy': 'some-property-name',
          'guideBox': {
              'default': {
                  'className': 'some-classname-goes-here',
                  'color': '#999',
                  'cursor': 'pointer',
                  'lineColor': '#ccc',
                  'lineWidth': 2,
                  'zIndex': 100
              }
          },
          'liveRedraw': True
      },
      'find_nearest_point_by': 'x',
      'get_extremes_from_all': True,
      'linecap': 'round',
      'line_width': 2,
      'negative_color': '#fff',
      'point_interval': 5,
      'point_interval_unit': 'weeks',
      'point_placement': 'on',
      'point_start': 12,
      'relative_x_value': True,
      'shadow': False,
      'soft_threshold': True,
      'stacking': 'normal',
      'step': 'left',
      'zone_axis': 'y',
      'zones': [
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          }
      ]
    }, None),
    # Series + Generic Options
    ({
      'data': [
          {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          },
          {
            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'id': 'some-id-goes-here',
      'index': 3,
      'legend_index': 3,
      'name': 'Series Name Goes Here',
      'stack': 'stack-id',
      'x_axis': 'some-id',
      'y_axis': 0,
      'z_index': 3,

      'animation_limit': 10,
      'boost_blending': '#ccc',
      'boost_threshold': 1234,
      'color_axis': 1,
      'color_index': 5,
      'color_key': 'some-key-value',
      'connect_ends': True,
      'connect_nulls': True,
      'crisp': True,
      'crop_threshold': 123,
      'data_sorting': {
          'enabled': True,
          'matchByName': True,
          'sortKey': 'some-key-value'
      },
      'drag_drop': {
          'draggableX': True,
          'draggableY': True,
          'dragHandle': {
              'className': 'draghandle-classname-goes-here',
              'color': '#ccc',
              'cursor': 'alias',
              'lineColor': '#ddd',
              'lineWidth': 2,
              'pathFormatter': """function() { return true; }""",
              'zIndex': 10
          },
          'dragMaxX': 3456,
          'dragMaxY': 6532,
          'dragMinX': 123,
          'dragMinY': 321,
          'dragPrecisionX': 5,
          'dragPrecisionY': 5,
          'dragSensitivity': 2,
          'groupBy': 'some-property-name',
          'guideBox': {
              'default': {
                  'className': 'some-classname-goes-here',
                  'color': '#999',
                  'cursor': 'pointer',
                  'lineColor': '#ccc',
                  'lineWidth': 2,
                  'zIndex': 100
              }
          },
          'liveRedraw': True
      },
      'find_nearest_point_by': 'x',
      'get_extremes_from_all': True,
      'linecap': 'round',
      'line_width': 2,
      'negative_color': '#fff',
      'point_interval': 5,
      'point_interval_unit': 'weeks',
      'point_placement': 'on',
      'point_start': 12,
      'relative_x_value': True,
      'shadow': False,
      'soft_threshold': True,
      'stacking': 'normal',
      'step': 'left',
      'zone_axis': 'y',
      'zones': [
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          }
      ],

      'accessibility': {
          'description': 'Description goes here',
          'enabled': True,
          'exposeAsGroupOnly': True,
          'keyboardNavigation': {
              'enabled': True
          },
          'point': {
              'dateFormat': 'format string',
              'dateFormatter': """function() { return true; }""",
              'describeNull': False,
              'descriptionFormatter': """function() { return true; }""",
              'valueDecimals': 2,
              'valueDescriptionFormat': 'format string',
              'valuePrefix': '$',
              'valueSuffix': 'USD'
          },
      },
      'allow_point_select': True,
      'animation': {
          'defer': 5
      },
      'class_name': 'some-class-name',
      'clip': False,
      'color': '#fff',
      'cursor': 'alias',
      'custom': {
          'item1': 'some value',
          'item2': 'some value'
      },
      'dash_style': 'Dash',
      'data_labels': {
        'align': 'center',
        'allowOverlap': True,
        'animation': {
            'defer': 5
        },
        'backgroundColor': {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.234,
                'y1': 0.345,
                'y2': 0.456
            },
            'stops': [
                [0.12, '#999'],
                [0.34, '#fff']
            ]
        },
        'borderColor': '#999999',
        'borderRadius': 24,
        'borderWidth': 1,
        'className': 'some-class-name',
        'color': '#000000',
        'crop': True,
        'defer': False,
        'enabled': True,
        'filter': {
            'operator': '>=',
            'property': 'some_property',
            'value': 123
        },
        'format': 'some format',
        'formatter': """function() { return true; }""",
        'inside': True,
        'nullFormat': 'some format',
        'nullFormatter': """function() { return true; }""",
        'overflow': 'none',
        'padding': 12,
        'position': 'center',
        'rotation': 0,
        'shadow': False,
        'shape': 'rect',
        'style': 'style goes here',
        'useHTML': False,
        'verticalAlign': 'top',
        'x': 10,
        'y': 20,
        'z': 0
      },
      'description': 'Description goes here',
      'enable_mouse_tracking': True,
      'events': {
        'afterAnimate': """function(event) { return true; }""",
        'click': """function(event) { return true; }""",
        'hide': """function(event) { return true; }""",
        'mouseOut': """function(event) { return true; }""",
        'show': """function(event) { return true; }"""
      },
      'include_in_data_export': True,
      'keys': [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      'label': {
          'boxesToAvoid': [
              {
               'bottom': 12,
               'left': -46,
               'right': 84,
               'top': 24
              },
              {
               'bottom': 48,
               'left': -46,
               'right': 84,
               'top': 86
              }
          ],
          'connectorAllowed': True,
          'connectorNeighbourDistance': 12,
          'enabled': True,
          'format': 'format string',
          'formatter': """function() { return true; }""",
          'maxFontSize': 18,
          'minFontSize': 6,
          'onArea': False,
          'style': 'some style string'
      },
      'linked_to': 'some_id',
      'marker': {
        'enabled': True,
        'fillColor': '#cccccc',
        'height': 24,
        'lineWidth': 2,
        'radius': 2,
        'states': {
            'hover': {
                'enabled': True
            }
        },
        'symbol': 'circle',
        'width': 48
      },
      'on_point': {
          'connectorOptions': {
              'dashstyle': 'Dash',
              'stroke': '#ccc',
              'width': 2
          },
          'id': 'some-id',
          'position': {
              'align': 'left',
              'verticalAlign': 'top',
              'x': 15,
              'y': -46
          }
      },
      'opacity': 0.2,
      'point': {
          'events': {
            'click': """function(event) { return true; }""",
            'drag': """function(event) { return true; }""",
            'drop': """function(event) { return true; }""",
            'mouseOut': """function(event) { return true; }"""
          }
      },
      'point_description_formatter': """function (point) { return true; }""",
      'selected': False,
      'show_checkbox': True,
      'show_in_legend': True,
      'skip_keyboard_navigation': False,
      'states': {
        'hover': {
            'animation': {
                'duration': 123
            },
            'borderColor': '#cccccc',
            'brightness': 0.3,
            'enabled': True
        },
        'inactive': {
            'enabled': True,
            'opacity': 0.5
        },
        'normal': {
            'animation': {
                'defer': 24
            }
        },
        'select': {
            'color': '#ff0000',
            'enabled': True,
        }
      },
      'sticky_tracking': True,
      'threshold': 123,
      'tooltip': {
        'animation': True,
        'backgroundColor': '#ccc',
        'borderColor': '#999',
        'borderRadius': 4,
        'borderWidth': 1,
        'className': 'some-class-name',
        'clusterFormat': 'format string',
        'dateTimeLabelFormats': {
          'day': 'test',
          'hour': 'test',
          'millisecond': 'test',
          'minute': 'test',
          'month': 'test',
          'second': 'test',
          'week': 'test',
          'year': 'test'
        },
        'distance': 12,
        'enabled': True,
        'followPointer': True,
        'followTouch_move': True,
        'footerFormat': 'format string',
        'formatter': """function() { return true; }""",
        'headerFormat': 'format string',
        'headerShape': 'circle',
        'hideDelay': 3,
        'nullFormat': 'format string',
        'nullFormatter': """function() { return true; }""",
        'outside': False,
        'padding': 6,
        'pointFormat': 'format string',
        'pointFormatter': """function() { return true; }""",
        'positioner': """function() { return true; }""",
        'shadow': False,
        'shape': 'rect',
        'shared': False,
        'snap': 4,
        'split': False,
        'stickOnContact': True,
        'style': 'style string goes here',
        'useHTML': False,
        'valueDecimals': 2,
        'valuePrefix': '$',
        'valueSuffix': ' USD',
        'xDateFormat': 'format string'
       },
      'turbo_threshold': 456,
      'visible': True
    }, None),
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
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/base/01.js', False, None),
    ('series/base/02.js', False, None),
    ('series/base/03.js', False, None),

    ('series/base/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/base/01.js', True, None),
    ('series/base/02.js', True, None),
    ('series/base/03.js', True, None),

    ('series/base/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


@pytest.mark.parametrize('filename, error', [
    ('test-data-files/nst-est2019-01.csv', None),
])
def test_from_pandas_in_rows(input_files, filename, error):
    import pandas
    
    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    print(df)
        
    if not error:
        result = cls.from_pandas_in_rows(df)
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == len(df)
        for series in result:
            assert isinstance(series, cls)
            assert series.data is not None
            assert len(series.data) == len(df.columns)
    else:
        with pytest.raises(error):
            result = cls.from_pandas_in_rows(df)

@pytest.mark.parametrize('filename, property_map, series_in_rows, error', [
    ('test-data-files/nst-est2019-01.csv',
     {
         'name': 'Geographic Area',
     },
     False,
     None),
    ('test-data-files/nst-est2019-01.csv', {}, False, ValueError),
    
])
def test_load_from_pandas(input_files, filename, property_map, series_in_rows, error):
    import pandas

    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0)
    print(df)
    instance = cls()

    if not error:
        instance.load_from_pandas(df, property_map = property_map)
        assert instance.data is not None
        assert len(instance.data) == len(df)
        for item in instance.data:
            for key in property_map:
                assert getattr(item, key) is not None
    else:
        with pytest.raises(error):
            instance.load_from_pandas(df, property_map = property_map)


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
     5,
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
     None),
    
])
def test_from_pandas(input_files, filename, kwargs, pre_test_df_func, expected_series, expected_data_points, error):
    import pandas

    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    if pre_test_df_func:
        df = pre_test_df_func(df)
    print(df)

    if not error:
        result = cls.from_pandas(df, **kwargs)
        assert result is not None
        if expected_series > 1:
            assert isinstance(result, list)
            assert len(result) == expected_series
            for series in result:
                assert isinstance(series, cls)
                assert series.data is not None
                assert len(series.data) == expected_data_points
        else:
            assert isinstance(result, cls)
            assert result.data is not None
            assert len(result.data) == len(df)
    else:
        with pytest.raises(error):
            result = cls.from_pandas(df, **kwargs)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_to_chart(kwargs, error):
    if not error:
        instance = cls(**kwargs)
        chart = instance.to_chart()
        assert chart is not None
        assert checkers.is_type(chart, 'Chart')
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            chart = instance.to_chart()


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__repr__(kwargs, error):
    obj = cls(**kwargs)
    if not error:
        result = repr(obj)
        if 'data' in kwargs:
            assert 'data = ' in result
    else:
        with pytest.raises(error):
            result = repr(obj)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__str__(kwargs, error):
    obj = cls(**kwargs)
    if not error:
        result = str(obj)
        print(result)
        assert 'data = ' not in result
    else:
        with pytest.raises(error):
            result = str(obj)
            
@pytest.mark.parametrize('filename, target_type, as_cls, error', [
    ('series/base/01.js', 'line', False, None),
    ('series/base/02.js', 'line', False, None),
    ('series/base/03.js', 'line', False, None),

    ('series/base/01.js', 'line', True, None),
    ('series/base/02.js', 'line', True, None),
    ('series/base/03.js', 'line', True, None),

    ('series/base/01.js', 'not a series type', False, ValueError),
    ('series/base/01.js', 123, False, ValueError),
])
def test_convert_to(input_files, filename, target_type, as_cls, error):
    input_file = check_input_file(input_files, filename)
    if not error:
        from highcharts_core.options.series.base import SeriesBase
        from highcharts_core.options.series.series_generator import SERIES_CLASSES

        original = cls.from_js_literal(input_file)

        if isinstance(target_type, str):
            target_type_cls = SERIES_CLASSES.get(target_type)
            target_type_name = target_type
        else:
            target_type_cls = target_type
            target_type_name = target_type.__name__

        if as_cls:
            target_type = target_type_cls
        else:
            target_type = target_type_name
        
        converted = original.convert_to(target_type)
        assert converted is not None
        assert isinstance(converted, SeriesBase)
        assert isinstance(converted, target_type_cls)