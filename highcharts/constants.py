"""Defines a set of constants that are used throughout the library."""
import os

from dotenv import load_dotenv

load_dotenv()


class EnforcedNullType:
    pass


EnforcedNull = EnforcedNullType()


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

## BOOST DEFAULTS
DEFAULT_BOOST_PIXEL_RATIO = 1
DEFAULT_BOOST_SERIES_THRESHOLD = 50


## CAPTION DEFAULTS
DEFAULT_CAPTION_ALIGN = 'left'
DEFAULT_CAPTION_MARGIN = 15
DEFAULT_CAPTION_STYLE = '{"color": "#666666"}'
DEFAULT_CAPTION_VERTICAL_ALIGN = 'bottom'
DEFAULT_CAPTION_X = 0
DEFAULT_CAPTION_Y = None


## CHART DEFAULTS
DEFAULT_CHART_BACKGROUND_COLOR = '#ffffff'
DEFAULT_CHART_BORDER_COLOR = '#335cad'
DEFAULT_CHART_BORDER_RADIUS = 0
DEFAULT_CHART_BORDER_WIDTH = 0
DEFAULT_CHART_COLOR_COUNT = 10
DEFAULT_CHART_SERIES_TYPE = 'line'
DEFAULT_CHART_PLOT_BACKGROUND_COLOR = None
DEFAULT_CHART_PLOT_BORDER_COLOR = '#cccccc'
DEFAULT_CHART_PLOT_BORDER_WIDTH = 0
DEFAULT_CHART_SELECTION_MARKER_FILL = 'rgba(51,92,173,0.25)'
DEFAULT_CHART_SPACING_BOTTOM = 15
DEFAULT_CHART_SPACING_LEFT = 10
DEFAULT_CHART_SPACING_TOP = 10
DEFAULT_CHART_SPACING_RIGHT = 10
DEFAULT_CHART_SPACING = [DEFAULT_CHART_SPACING_TOP,
                         DEFAULT_CHART_SPACING_RIGHT,
                         DEFAULT_CHART_SPACING_BOTTOM,
                         DEFAULT_CHART_SPACING_LEFT]
DEFAULT_CHART_STYLE = '{"fontFamily": "\"Lucida Grande\", \"Lucida Sans Unicode\", Verdana, Arial, Helvetica, sans-serif","fontSize":"12px"}'
DEFAULT_CHART_TYPE = 'line'
DEFAULT_CHART_PARALLEL_AXES = {
    'line_width': 1,
    'gridlines_width': 0,
    'title': {
        'text': '',
        'reserve_space': False
    },
    'labels': {
        'x': 0,
        'y': 0,
        'align': 'center',
        'reserve_space': False
    },
    'offset': 0
}


## RESET ZOOM BUTTON DEFAULTS
DEFAULT_RESET_ZOOM_BUTTON_POSITION = {
    'align': 'right',
    'vertical_align': 'top',
    'x': -10,
    'y': 10
}
DEFAULT_RESET_ZOOM_BUTTON_THEME = {
    'zIndex': 6
}


## CREDITS DEFAULTS
DEFAULT_CREDITS_HREF = 'https://www.highcharts.com?credits'
DEFAULT_CREDITS_STYLE = {
    'color': '#999999',
    'cursor': 'pointer',
    'fontSize': '9px'
}
DEFAULT_CREDITS_TEXT = 'Highcharts'


## DRILLDOWN DEFAULTS
DEFAULT_DRILLDOWN_ACTIVE_AXIS_LABEL_STYLE = {
    "cursor": "pointer",
    "color": "#003399",
    "fontWeight": "bold",
    "textDecoration": "underline"
}
DEFAULT_DRILLDOWN_ACTIVE_DATA_LABEL_STYLE = {
    'color': '#003399',
    'cursor': 'pointer',
    'fontWeight': 'bold',
    'textDecoration': 'underline'
}


## DRILLDOWN BREAADCRUMB DEFAULTS
DEFAULT_BREADCRUMBS_POSITION = {
    'align': 'left',
    'vertical_align': 'top',
    'x': 0,
    'y': None
}
DEFAULT_BREADCRUMBS_RELATIVE_TO = 'plotBox'
DEFAULT_BREADCRUMBS_STYLE = None
DEFAULT_BREADCRUMBS_SEPARATOR_STYLE = {
    'color': '#666666'
}
DEFAULT_BREADCRUMBS_SEPARATOR_TEXT = '/'


## EXPORTING DEFAULTS
DEFAULT_EXPORTING_FILENAME = 'chart'
DEFAULT_EXPORTING_LIB_URL = None
DEFAULT_EXPORTING_MENU_ITEM_DEFINITIONS = {
    "viewFullscreen": {},
    "printChart": {},
    "separator": {},
    "downloadPNG": {},
    "downloadJPEG": {},
    "downloadPDF": {},
    "downloadSVG": {}
}
DEFAULT_EXPORTING_PRINT_MAX_WIDTH = 780
DEFAULT_EXPORTING_SCALE = 2
DEFAULT_EXPORTING_TYPE = 'image/png'
DEFAULT_EXPORTING_URL = 'https://export.highcharts.com/'

## EXPORTING: CONTEXT BUTTON
DEFAULT_CONTEXT_BUTTON_CLASS_NAME = 'highcharts-contextbutton'
DEFAULT_CONTEXT_MENU_CLASS_NAME = 'highcharts-contextmenu'
DEFAULT_CONTEXT_MENU_ITEMS = [
    "viewFullscreen",
    "printChart",
    "separator",
    "downloadPNG",
    "downloadJPEG",
    "downloadPDF",
    "downloadSVG"
]

## EXPORTING: CSV
DEFAULT_CSV_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_CSV_LINE_DELIMITER = '\n'
