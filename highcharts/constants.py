"""Defines a set of constants that are used throughout the library."""
import os

from dotenv import load_dotenv

load_dotenv()


JAVASCRIPT_INDENT_SPACES = os.getenv('JAVASCRIPT_INDENT_SPACES') or 2
JAVASCRIPT_INDENT = ''
indent_count = 1
while indent_count < int(JAVASCRIPT_INDENT_SPACES):
    JAVASCRIPT_INDENT += ' '
    indent_count += 1

DEFAULT_COLORS = ["#7cb5ec", "#434348", "#90ed7d", "#f7a35c", "#8085e9", "#f15c80",
                  "#e4d354", "#2b908f", "#f45b5b", "#91e8e1"]

## ACCESSIBILITY DEFAULTS
DEFAULT_LANDMARK_VERBOSITY = 'all'
LANDMARK_VERBOSITY_VALUES = ['all',
                              'one',
                              'disabled'
                             ]

DEFAULT_LINKED_DESCRIPTION = '*[data-highcharts-chart="{index}"] + .highcharts-description'

DEFAULT_ACCESSIBILITY_POINT_VALUE_FORMAT = '{xDescription}{separator}{value}'
DEFAULT_AFTER_CHART_FORMAT = '{endOfChartMarker}'
DEFAULT_AXIS_RANGE_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_BEFORE_CHART_FORMAT = ('<{headingTagName}>{chartTitle}</{headingTagName}><div>'
                               '{typeDescription}</div><div>{chartSubtitle}</div>'
                               '<div>{chartLongdesc}</div><div>{playAsSoundButton}</div>'
                               '<div>{viewTableButton}</div><div>{xAxisDescription}</div>'
                               '<div>{yAxisDescription}</div>'
                               '<div>{annotationsTitle}{annotationsList}</div>')
DEFAULT_DESCRIPTION_FORMAT = '{seriesDescription}{authorDescription}{axisDescription}'

## JAVASCRIPT LITERAL DEFAULTS

# TODO: DETERMINE IF THE FOLLOWING WILL ACTUALLY BE NEEDED
ALLOWED_JS_LITERAL_TYPES = [
    'FunctionDeclaration',
    'VariableDeclaration',
    'ClassDeclaration',
]


## ANNOTATIONS DEFAULTS
DEFAULT_DRAGGABLE = 'xy'
