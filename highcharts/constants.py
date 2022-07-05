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
DEFAULT_LABEL_ALIGN = 'center'
DEFAULT_LABEL_BACKGROUND_COLOR = 'rgba(0, 0, 0, 0.75)'
DEFAULT_LABEL_BORDER_COLOR = '#000000'
DEFAULT_LABEL_BORDER_RADIUS = 3
DEFAULT_LABEL_BORDER_WIDTH = 1
DEFAULT_LABEL_CLASS_NAME = 'highcharts-no-tooltip'
DEFAULT_LABEL_OVERFLOW = 'justify'
DEFAULT_LABEL_FORMATTER = """function () { return defined(this.y) ? this.y : 'Annotation label'; }"""
DEFAULT_LABEL_PADDING = 5
DEFAULT_LABEL_SHAPE = 'callout'
DEFAULT_LABEL_VERTICAL_ALIGN = 'bottom'
DEFAULT_LABEL_X = 0
DEFAULT_LABEL_Y = -16


## SHAPES DEFAULTS
DEFAULT_SHAPES_FILL = 'rgba(0, 0, 0, 0.75)'
DEFALUT_SHAPES_R = 0
DEFAULT_SHAPES_SNAP = 2
DEFAULT_SHAPES_STROKE = 'rgba(0, 0, 0, 0.75)'
DEFAULT_SHAPES_STROKE_WIDTH = 1
DEFAULT_SHAPES_TYPE = 'rect'
SHAPES_ALLOWED_DASH_STYLES = ('Solid',
                              'ShortDash',
                              'ShortDot',
                              'ShortDashDot',
                              'ShortDashDotDot',
                              'Dot',
                              'Dash',
                              'LongDash',
                              'DashDot',
                              'LongDashDot',
                              'LongDashDotDot')
