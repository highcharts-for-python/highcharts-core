"""Defines a set of constants that are used throughout the library."""
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
try:
    import orjson as json
except ImportError:
    try:
        import rapidjson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            import json

with open(os.path.join(os.path.dirname(__file__), 
                       './module_requirements.json'), 
          'r') as module_requirements:
    try:
        MODULE_REQUIREMENTS = json.load(module_requirements)
    except AttributeError:
        MODULE_REQUIREMENTS = json.loads(module_requirements.read())


class EnforcedNullType:
    def __eq__(self, other):
        return isinstance(other, self.__class__)


EnforcedNull = EnforcedNullType()


JAVASCRIPT_INDENT_SPACES = os.getenv('JAVASCRIPT_INDENT_SPACES') or 2
JAVASCRIPT_INDENT = ''
indent_count = 1
while indent_count < int(JAVASCRIPT_INDENT_SPACES):
    JAVASCRIPT_INDENT += ' '
    indent_count += 1

DEFAULT_COLORS = ["#7cb5ec", "#434348", "#90ed7d", "#f7a35c", "#8085e9", "#f15c80",
                  "#e4d354", "#2b908f", "#f45b5b", "#91e8e1"]

INCLUDE_LIBS = [
    'https://code.highcharts.com/highcharts.js',
    'https://code.highcharts.com/highcharts-more.js',
    'https://code.highcharts.com/highcharts-3d.js',
    'https://code.highcharts.com/modules/sonification.js',
    'https://code.highcharts.com/modules/accessibility.js',
    'https://code.highcharts.com/modules/annotations.js',
    'https://code.highcharts.com/modules/annotations-advanced.js',
    'https://code.highcharts.com/modules/sankey.js',
    'https://code.highcharts.com/modules/arc-diagram.js',
    'https://code.highcharts.com/modules/boost.js',
    'https://code.highcharts.com/modules/broken-axis.js',
    'https://code.highcharts.com/modules/bullet.js',
    'https://code.highcharts.com/modules/cylinder.js',
    'https://code.highcharts.com/modules/data.js',
    'https://code.highcharts.com/modules/datagrouping.js',
    'https://code.highcharts.com/modules/debugger.js',
    'https://code.highcharts.com/modules/dependency-wheel.js',
    'https://code.highcharts.com/modules/drag-panes.js',
    'https://code.highcharts.com/modules/draggable-points.js',
    'https://code.highcharts.com/modules/drilldown.js',
    'https://code.highcharts.com/modules/dumbbell.js',
    'https://code.highcharts.com/modules/export-data.js',
    'https://code.highcharts.com/modules/exporting.js',
    'https://code.highcharts.com/modules/funnel.js',
    'https://code.highcharts.com/modules/funnel3d.js',
    'https://code.highcharts.com/modules/heatmap.js',
    'https://code.highcharts.com/modules/item-series.js',
    'https://code.highcharts.com/modules/lollipop.js',
    'https://code.highcharts.com/modules/networkgraph.js',
    'https://code.highcharts.com/modules/no-data-to-display.js',
    'https://code.highcharts.com/modules/offline-exporting.js',
    'https://code.highcharts.com/modules/oldie.js',
    'https://code.highcharts.com/modules/organization.js',
    'https://code.highcharts.com/modules/parallel-coordinates.js',
    'https://code.highcharts.com/modules/pareto.js',
    'https://code.highcharts.com/modules/pictorial.js',
    'https://code.highcharts.com/modules/pyramid3d.js',
    'https://code.highcharts.com/modules/series-label.js',
    'https://code.highcharts.com/modules/series-on-point.js',
    'https://code.highcharts.com/modules/solid-gauge.js',
    'https://code.highcharts.com/modules/streamgraph.js',
    'https://code.highcharts.com/modules/sunburst.js',
    'https://code.highcharts.com/modules/tilemap.js',
    'https://code.highcharts.com/modules/timeline.js',
    'https://code.highcharts.com/modules/treegraph.js',
    'https://code.highcharts.com/modules/treemap.js',
    'https://code.highcharts.com/modules/variable-pie.js',
    'https://code.highcharts.com/modules/variwide.js',
    'https://code.highcharts.com/modules/vector.js',
    'https://code.highcharts.com/modules/venn.js',
    'https://code.highcharts.com/modules/windbarb.js',
    'https://code.highcharts.com/modules/wordcloud.js',
    'https://code.highcharts.com/modules/xrange.js',
]

INCLUDE_STR = """
    <script src="https://code.highcharts.com/highcharts.js"/>
    <script src="https://code.highcharts.com/highcharts-more.js"/>
    <script src="https://code.highcharts.com/highcharts-3d.js"/>
    <script src="https://code.highcharts.com/modules/sonification.js"/>
    <script src="https://code.highcharts.com/modules/accessibility.js"/>
    <script src="https://code.highcharts.com/modules/annotations.js"/>
    <script src="https://code.highcharts.com/modules/annotations-advanced.js"/>
    <script src="https://code.highcharts.com/modules/arc-diagram.js"/>
    <script src="https://code.highcharts.com/modules/bellcurve.js"/>
    <script src="https://code.highcharts.com/modules/boost.js"/>
    <script src="https://code.highcharts.com/modules/broken-axis.js"/>
    <script src="https://code.highcharts.com/modules/bullet.js"/>
    <script src="https://code.highcharts.com/modules/cylinder.js"/>
    <script src="https://code.highcharts.com/modules/data.js"/>
    <script src="https://code.highcharts.com/modules/datagrouping.js"/>
    <script src="https://code.highcharts.com/modules/debugger.js"/>
    <script src="https://code.highcharts.com/modules/dependency-wheel.js"/>
    <script src="https://code.highcharts.com/modules/drag-panes'
    <script src="https://code.highcharts.com/modules/draggable-points.js"/>
    <script src="https://code.highcharts.com/modules/drilldown.js"/>
    <script src="https://code.highcharts.com/modules/dumbbell.js"/>
    <script src="https://code.highcharts.com/modules/export-data.js"/>
    <script src="https://code.highcharts.com/modules/exporting.js"/>
    <script src="https://code.highcharts.com/modules/full-screen.js"/>
    <script src="https://code.highcharts.com/modules/funnel.js"/>
    <script src="https://code.highcharts.com/modules/funnel3d.js"/>
    <script src="https://code.highcharts.com/modules/histogram.js"/>
    <script src="https://code.highcharts.com/modules/item-series.js"/>
    <script src="https://code.highcharts.com/modules/lollipop.js"/>
    <script src="https://code.highcharts.com/modules/networkgraph.js"/>
    <script src="https://code.highcharts.com/modules/no-data-to-display.js"/>
    <script src="https://code.highcharts.com/modules/offline-exporting.js"/>
    <script src="https://code.highcharts.com/modules/oldie.js"/>
    <script src="https://code.highcharts.com/modules/organization.js"/>
    <script src="https://code.highcharts.com/modules/parallel-coordinates.js"/>
    <script src="https://code.highcharts.com/modules/pareto.js"/>
    <script src="https://code.highcharts.com/modules/pictorial.js"/>
    <script src="https://code.highcharts.com/modules/pyramid3d.js"/>
    <script src="https://code.highcharts.com/modules/sankey.js"/>
    <script src="https://code.highcharts.com/modules/series-label.js"/>
    <script src="https://code.highcharts.com/modules/series-on-point.js"/>
    <script src="https://code.highcharts.com/modules/solid-gauge.js"/>
    <script src="https://code.highcharts.com/modules/streamgraph.js"/>
    <script src="https://code.highcharts.com/modules/sunburst.js"/>
    <script src="https://code.highcharts.com/modules/tilemap.js"/>
    <script src="https://code.highcharts.com/modules/timeline.js"/>
    <script src="https://code.highcharts.com/modules/treegraph.js"/>
    <script src="https://code.highcharts.com/modules/treemap.js"/>
    <script src="https://code.highcharts.com/modules/variable-pie.js"/>
    <script src="https://code.highcharts.com/modules/variwide.js"/>
    <script src="https://code.highcharts.com/modules/vector.js"/>
    <script src="https://code.highcharts.com/modules/venn.js"/>
    <script src="https://code.highcharts.com/modules/windbarb.js"/>
    <script src="https://code.highcharts.com/modules/wordcloud.js"/>
    <script src="https://code.highcharts.com/modules/xrange.js"/>
"""

AXIS_TYPES = [
    'linear',
    'logarithmic',
    'datetime',
    'category'
]

SUPPORTED_CURSOR_VALUES = [
    'alias',
    'all-scroll',
    'auto',
    'cell',
    'col-resize',
    'context-menu',
    'copy',
    'crosshair',
    'default',
    'e-resize',
    'ew-resize',
    'grab',
    'grabbing',
    'help',
    'move',
    'n-resize',
    'ne-resize',
    'nesw-resize',
    'no-drop',
    'none',
    'not-allowed',
    'ns-resize',
    'nw-resize',
    'nwse-resize',
    'pointer',
    'progress',
    'row-resize',
    's-resize',
    'se-resize',
    'sw-resize',
    'text',
    'vertical-text',
    'w-resize',
    'wait',
    'zoom-in',
    'zoom-out'
]
SUPPORTED_DASH_STYLE_VALUES = [
    'Dash',
    'DashDot',
    'Dot',
    'LongDash',
    'LongDashDot',
    'LongDashDotDot',
    'ShortDash',
    'ShortDashDot',
    'ShortDashDotDot',
    'ShortDot',
    'Solid'
]

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
DEFAULT_SHAPES_R = 0
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


## LANG
DEFAULT_LANG_CONTEXT_BUTTON_TITLE = 'Chart context menu'
DEFAULT_LANG_DOWNLOAD_CSV = 'Download CSV'
DEFAULT_LANG_DOWNLOAD_JPEG = 'Download JPEG'
DEFAULT_LANG_DOWNLOAD_PDF = 'Download PDF'
DEFAULT_LANG_DOWNLOAD_PNG = 'Download PNG'
DEFAULT_LANG_DOWNLOAD_SVG = 'Download SVG'
DEFAULT_LANG_DOWNLOAD_XLS = 'Download Excel'
DEFAULT_LANG_DRILLUP_TEXT = None
DEFAULT_LANG_EXIT_FULLSCREEN = 'Exit from full screen'
DEFAULT_LANG_HIDE_DATA = 'Hide data table'
DEFAULT_LANG_INVALID_DATE = ''
DEFAULT_LANG_LOADING = 'Loading...'
DEFAULT_LANG_MAIN_BREADCRUM = 'Main'
DEFAULT_LANG_MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
DEFAULT_LANG_NO_DATA = 'No data to display'
DEFAULT_LANG_NUMERIC_SYMBOL_MAGNITUDE = 1000
DEFAULT_LANG_NUMERIC_SYMBOLS = ["k", "M", "G", "T", "P", "E"]
DEFAULT_LANG_PRINT_CHART = 'Print chart'
DEFAULT_LANG_RESET_ZOOM = 'Reset zoom'
DEFAULT_LANG_RESET_ZOOM_TITLE = 'Reset zoom level 1:1'
DEFAULT_LANG_SHORT_MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]
DEFAULT_LANG_SHORT_WEEKDAYS = None
DEFAULT_LANG_THOUSANDS_SEP = '\u0020'
DEFAULT_LANG_VIEW_DATA = 'View data table'
DEFAULT_LANG_VIEW_FULLSCREEN = 'View in full screen'
DEFAULT_LANG_WEEKDAYS = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

## LANGUAGE: ACCESSIBILITY
DEFAULT_LANG_ACCESSIBILITY_CHART_CONTAINER_LABEL = '{title}. Highcharts interactive chart.'
DEFAULT_LANG_ACCESSIBILITY_CREDITS = 'Chart credits: {creditsStr}'
DEFAULT_LANG_ACCESSIBILITY_DEFAULT_CHART_TITLE = 'Chart'
DEFAULT_LANG_ACCESSIBILITY_DRILLUP_BUTTON = '{buttonText}'
DEFAULT_LANG_ACCESSIBILITY_GRAPHIC_CONTAINER_LABEL = ''
DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_LABEL = 'Interactive chart'
DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_TITLE = ''
DEFAULT_LANG_ACCESSIBILITY_THOUSANDSSEP = ','

DEFAULT_LANG_ACS_ANNOUNCE_NEW_DATA = 'Updated data for chart {chartTitle}'
DEFAULT_LANG_ACS_ANNOUNCE_NEW_POINT_MULTIPLE = 'New data point in chart {chartTitle}: {pointDesc}'
DEFAULT_LANG_ACS_ANNOUNCE_NEW_POINT_SINGLE = 'New data point: {pointDesc}'
DEFAULT_LANG_ACS_ANNOUNCE_NEW_SERIES_MULTIPLE = 'New data series in chart {chartTitle}: {seriesDesc}'
DEFAULT_LANG_ACS_ANNOUNCE_NEW_SERIES_SINGLE = 'New data series: {seriesDesc}'

DEFAULT_LANG_ACS_AXIS_RANGE_CATEGORIES = 'Data range: {numCategories} categories.'
DEFAULT_LANG_ACS_AXIS_RANGE_FROM_TO = 'Data ranges from {rangeFrom} to {rangeTo}.'
DEFAULT_LANG_ACS_AXIS_TIME_RANGE_DAYS = 'Data range: {range} days.'
DEFAULT_LANG_ACS_AXIS_TIME_RANGE_HOURS = 'Data range: {range} hours.'
DEFAULT_LANG_ACS_AXIS_TIME_RANGE_MINUTES = 'Data range: {range} minutes.'
DEFAULT_LANG_ACS_AXIS_TIME_RANGE_SECONDS = 'Data range: {range} seconds.'
DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_PLURAL = 'The chart has {numAxes} X axes displaying {#each(names, -1), }and {names[-1]}.'
DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_SINGULAR = 'The chart has 1 X axis displaying {names[0]}. {ranges[0]}'
DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_PLURAL = 'The chart has {numAxes} Y axes displaying {#each(names, -1), }and {names[-1]}.'
DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_SINGULAR = 'The chart has 1 Y axis displaying {names[0]}. {ranges[0]}'

DEFAULT_LANG_ACS_CHART_TYPES_BAR_MULTIPLE = 'Bar chart with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_BAR_SINGLE = 'Bar chart with {numPoints} {#plural(numPoints, bars, bar)}.'
DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_MULTIPLE = 'Boxplot with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_BOXPLOT_SINGLE = 'Boxplot with {numPoints} {#plural(numPoints, boxes, box)}.'
DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_MULTIPLE = 'Bubble chart with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_BUBBLE_SINGLE = 'Bubble chart with {numPoints} {#plural(numPoints, bubbles, bubble)}.'
DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_MULTIPLE = 'Bar chart with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_COLUMN_SINGLE = 'Bar chart with {numPoints} {#plural(numPoints, bars, bar)}.'
DEFAULT_LANG_ACS_CHART_TYPES_COMBO = 'Combination chart with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_MULTIPLE = 'Chart with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_DEFAULT_SINGLE = 'Chart with {numPoints} data {#plural(numPoints, points, point)}.'
DEFAULT_LANG_ACS_CHART_TYPES_EMPTY_CHART = 'Empty chart'
DEFAULT_LANG_ACS_CHART_TYPES_LINE_MULTIPLE = 'Line chart with {numSeries} lines.'
DEFAULT_LANG_ACS_CHART_TYPES_LINE_SINGLE = 'Line chart with {numPoints} data {#plural(numPoints, points, point)}.'
DEFAULT_LANG_ACS_CHART_TYPES_MAP_TYPE_DESCRIPTION = 'Map of {mapTitle} with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_PIE_MULTIPLE = 'Pie chart with {numSeries} pies.'
DEFAULT_LANG_ACS_CHART_TYPES_PIE_SINGLE = 'Pie chart with {numPoints} {#plural(numPoints, slices, slice)}.'
DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_MULTIPLE = 'Scatter chart with {numSeries} data series.'
DEFAULT_LANG_ACS_CHART_TYPES_SCATTER_SINGLE = 'Scatter chart with {numPoints} {#plural(numPoints, points, point)}.'
DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_MULTIPLE = 'Line chart with {numSeries} lines.'
DEFAULT_LANG_ACS_CHART_TYPES_SPLINE_SINGLE = 'Line chart with {numPoints} data {#plural(numPoints, points, point)}.'
DEFAULT_LANG_ACS_CHART_TYPES_UNKNOWN_MAP = 'Map of unspecified region with {numSeries} data series.'

DEFAULT_LANG_ACS_EXPORTING_CHART_MENU_LABEL = 'Chart menu'
DEFAULT_LANG_ACS_EXPORTING_MENU_BTN_LABEL = 'View chart menu, {chartTitle}'


DEFAULT_LANG_ACS_LEGEND_ITEM = 'Show {itemName}'
DEFAULT_LANG_ACS_LEGEND_LABEL = 'Chart legend: {legendTitle}'
DEFAULT_LANG_ACS_LEGEND_LABEL_NO_TITLE = 'Toggle series visibility, {chartTitle}'


DEFAULT_LANG_ACS_RANGE_SELECTOR_CLICK_BTN_ANNOUNCEMENT = 'Viewing {axisRangeDescription}'
DEFAULT_LANG_ACS_RANGE_SELECTOR_DROPDOWN_LBL = '{rangeTitle}'
DEFAULT_LANG_ACS_RANGE_SELECTOR_MAX_INPUT_LBL = 'Select end date.'
DEFAULT_LANG_ACS_RANGE_SELECTOR_MIN_INPUT_LBL = 'Select start date.'


DEFAULT_LANG_ACS_SRS_AFTER_REGION_LBL = ''
DEFAULT_LANG_ACS_SRS_BEFORE_REGION_LBL = ''
DEFAULT_LANG_ACS_SRS_END_OF_CHART_MRKR = 'End of interactive chart.'


DEFAULT_LANG_ACS_SRS_ANNOTATION_DESCRIPTION_MULTIPLE_PTS = '{annotationText}. Related to {annotationPoint}{ Also related to, #each(additionalAnnotationPoints)}'
DEFAULT_LANG_ACS_SRS_ANNOTATION_DESCRIPTION_NO_PTS = '{annotationText}'
DEFAULT_LANG_ACS_SRS_ANNOTATION_DESCRIPTION_SINGLE_PT = '{annotationText}. Related to {annotationPoint}'
DEFAULT_LANG_ACS_SRS_ANNOTATION_HEADING = 'Chart annotations summary'


DEFAULT_LANG_ACS_SERIES_DESCRIPTION = ''
DEFAULT_LANG_ACS_SERIES_NULL_PT_VALUE = ''
DEFAULT_LANG_ACS_SERIES_PT_ANNOTATIONS_DESCRIPTION = ''
DEFAULT_LANG_ACS_SERIES_XAXIS_DESCRIPTION = ''
DEFAULT_LANG_ACS_SERIES_YAXIS_DESCRIPTION = ''


DEFAULT_LANG_ACS_SERIES_SUMMARY = {
    'bar': '{series.name}, bar series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bars, bar)}.',
    'bar_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Bar series with {series.points.length} {#plural(series.points.length, bars, bar)}.',
    'boxplot': '{series.name}, boxplot {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, boxes, box)}.',
    'boxplot_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Boxplot with {series.points.length} {#plural(series.points.length, boxes, box)}.',
    'bubble': '{series.name}, bubble series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.',
    'bubble_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Bubble series with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.',
    'column': '{series.name}, bar series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bars, bar)}.',
    'column_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Bar series with {series.points.length} {#plural(series.points.length, bars, bar)}.',
    'default': '{series.name}, series {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.',
    'default_combination': '{series.name}, series {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.',
    'line': '{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.',
    'line_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#plural(series.points.length, points, point)}.',
    'map': '{series.name}, map {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, areas, area)}.',
    'map_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Map with {series.points.length} {#plural(series.points.length, areas, area)}.',
    'mapbubble': '{series.name}, bubble series {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.',
    'mapbubble_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Bubble series with {series.points.length} {#plural(series.points.length, bubbles, bubble)}.',
    'mapline': '{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.',
    'mapline_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#plural(series.points.length, points, point)}.',
    'pie': '{series.name}, pie {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, slices, slice)}.',
    'pie_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Pie with {series.points.length} {#plural(series.points.length, slices, slice)}.',
    'scatter': '{series.name}, scatter plot {seriesNumber} of {chart.series.length} with {series.points.length} {#plural(series.points.length, points, point)}.',
    'scatter_combination': '{series.name}, series {seriesNumber} of {chart.series.length}, scatter plot with {series.points.length} {#plural(series.points.length, points, point)}.',
    'spline': '{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#plural(series.points.length, points, point)}.',
    'spline_combination': '{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#plural(series.points.length, points, point)}.',
}


DEFAULT_LANG_ACS_SERIES_TYPES = {
    'arearange': 'Arearange charts are line charts displaying a range between a lower and higher value for each point.',
    'areasplinerange': 'These charts are line charts displaying a range between a lower and higher value for each point.',
    'boxplot': 'Box plot charts are typically used to display groups of statistical data. Each data point in the chart can have up to 5 values: minimum, lower quartile, median, upper quartile, and maximum.',
    'bubble': 'Bubble charts are scatter charts where each data point also has a size value.',
    'columnrange': 'Columnrange charts are column charts displaying a range between a lower and higher value for each point.',
    'errorbar': 'Errorbar series are used to display the variability of the data.',
    'funnel': 'Funnel charts are used to display reduction of data in stages.',
    'pyramid': 'Pyramid charts consist of a single pyramid with item heights corresponding to each point value.',
    'waterfall': 'A waterfall chart is a column chart where each column contributes towards a total end value.'
}


## LANGUAGE: ACCESSIBILITY: SONIFICATION
DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_BTN_TXT = 'Play as sound, {chartTitle}'
DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_CLK_ANNOUNCEMENT = 'Play'


## LANGUAGES: ACCESSIBILITY: TABLE
DEFAULT_LANG_ACS_TABLE_SUMMARY = 'Table representation of chart.'
DEFAULT_LANG_ACS_TABLE_VIEW_AS_DATA_TABLE = 'View as data table, {chartTitle}'


## LANGUAGES: ACCESSIBILITY: ZOOM
DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_IN = 'Zoom chart'
DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_OUT = 'Zoom out chart'
DEFAULT_LANG_ACS_ZOOM_RESET_ZOOM_BTN = 'Reset zoom'


## LANGUAGES: EXPORT DATA
DEFAULT_LANG_EXPORT_DATA = {
    'annotation_header': 'Annotations',
    'category_datetime_header': 'DateTime',
    'category_header': 'Category'
}


## LANGUAGES: NAVIGATION
DEFAULT_LANG_NAVIGATION = {
    'add_button': 'add',
    'algorithm': 'Algorithm',
    'arrow_infinity_line': 'Arrow line',
    'arrow_ray': 'Arrow ray',
    'arrow_segment': 'Arrow segment',
    'average': 'Average',
    'background': 'Background',
    'background_color': 'Background color',
    'background_colors': 'Background colors',
    'border_color': 'Border color',
    'border_radius': 'Border radius',
    'border_width': 'Border width',
    'bottom_band': 'Bottom band',
    'circle': 'Circle',
    'clear_filter': 'X Clear Filter',
    'color': 'Color',
    'connector': 'Connector',
    'crooked3': 'Crooked 3 line',
    'crooked5': 'Crooked 5 line',
    'crosshairX': 'Crosshair X',
    'crosshairY': 'Crosshair Y',
    'decimals': 'Decimals',
    'deviation': 'Deviation',
    'edit_button': 'edit',
    'elliott3': 'Elliott 3 line',
    'elliott5': 'Elliott 5 line',
    'ellipse': 'Ellipse',
    'factor': 'Factor',
    'fast_avg_period': 'Fast average period',
    'fibonacci': 'Fibonacci',
    'fibonacci_time_zones': 'Fibonacci Time Zones',
    'fill': 'Fill',
    'flags': 'Flags',
    'font_size': 'Font size',
    'format': 'Text',
    'height': 'Height',
    'high_index': 'High index',
    'horizontal_line': 'Horizontal line',
    'increment': 'Increment',
    'index': 'Index',
    'infinity_line': 'Infinity line',
    'initial_acceleration_factor': 'Initial acceleration factor',
    'inner_background': 'Inner background',
    'label': 'Label',
    'label_options': 'Label options',
    'labels': 'Labels',
    'line': 'Line',
    'lines': 'Lines',
    'long_period': 'Long period',
    'low_index': 'Low index',
    'max_acceleration_factor': 'Max acceleration factor',
    'measure': 'Measure',
    'measure_x': 'Measure X',
    'measure_xy': 'Measure XY',
    'measure_y': 'Measure Y',
    'multiplier': 'Multiplier',
    'multiplier_atr': 'ATR multiplier',
    'name': 'Name',
    'no_filter_match': 'No match',
    'outer_background': 'Outer background',
    'padding': 'Padding',
    'parallel_channel': 'Parallel channel',
    'period': 'Period',
    'period_atr': 'ATR period',
    'periods': 'Periods',
    'period_senkou_span_b': 'Senkou Span B period',
    'period_tenkan': 'Tenkan period',
    'pitchfork': 'Pitchfork',
    'ranges': 'Ranges',
    'ray': 'Ray',
    'rectangle': 'Rectangle',
    'remove_button': 'remove',
    'save_button': 'save',
    'search_indicators': 'Search Indicators',
    'segment': 'Segment',
    'series': 'Series',
    'shape_options': 'Shape options',
    'shapes': 'Shape options',
    'short_period': 'Short period',
    'signal_period': 'Signal period',
    'simple_shapes': 'Simple shapes',
    'slow_avg_period': 'Slow average period',
    'standard_deviation': 'Standard deviation',
    'stroke': 'Line color',
    'stroke_width': 'Line width',
    'style': 'Style',
    'time_cycles': 'Time Cycles',
    'title': 'Title',
    'top_band': 'Top band',
    'tunnel': 'Tunnel',
    'type_options': 'Details',
    'vertical_arrow': 'Vertical arrow',
    'vertical_counter': 'Vertical counter',
    'vertical_label': 'Vertical label',
    'vertical_line': 'Vertical line',
    'volume': 'Volume',
    'x_axis_unit': 'x-axis unit'
}


## DEFAULTS: LEGEND
DEFAULT_LEGEND = {
    'accessibility': None,
    'align': 'center',
    'align_columns': True,
    'background_color': None,
    'border_color': '#999999',
    'border_radius': 0,
    'border_width': 0,
    'bubble_legend': None,
    'class_name': 'highcharts-no-tooltip',
    'enabled': False,
    'floating': False,
    'item_checkbox_style': '{"width": "13px", "height": "13px", "position":"absolute"}',
    'item_distance': 20,
    'item_hidden_style': '{"color": "#cccccc"}',
    'item_hover_style': '{"color": "#000000"}',
    'item_margin_bottom': 0,
    'item_margin_top': 0,
    'item_style': '{"color": "#333333", "cursor": "pointer", "fontSize": "12px", "fontWeight": "bold", "textOverflow": "ellipsis"}',
    'item_width': None,
    'label_format': '{name}',
    'label_formatter': None,
    'layout': 'horizontal',
    'margin': 12,
    'max_height': None,
    'navigation': {
        'active_color': '#003399',
        'arrow_size': 12,
        'inactive_color': '#cccccc',
        'style': None
    },
    'padding': 8,
    'reversed': False,
    'rtl': False,
    'shadow': False,
    'square_symbol': True,
    'symbol_height': None,
    'symbol_padding': 5,
    'symbol_radius': None,
    'symbol_width': None,
    'title': {
        'style': '{"fontWeight": "bold"}'
    },
    'use_html': False,
    'vertical_align': 'bottom',
    'width': None,
    'x': 0,
    'y': 0
}
DEFAULT_BUBBLE_LEGEND = {
    'border_color': None,
    'border_width': 2,
    'class_name': None,
    'color': None,
    'connector_class_name': None,
    'connector_color': None,
    'connector_distance': None,
    'connector_width': None,
    'enabled': False,
    'labels': {
        'align': 'right',
        'allow_overlap': False,
        'class_name': None,
        'format': '',
        'formatter': None,
        'style': None,
        'x': 0,
        'y': 0
    },
    'legend_index': 0,
    'max_size': 60,
    'min_size': 10,
    'ranges': None,
    'size_by': 'area',
    'size_by_absolute_value': False,
    'z_index': 1,
    'z_threshold': 0

}


## LOADING
DEFAULT_LOADING = {
    'hide_duration': 100,
    'label_style': '{"fontWeight": "bold", "position": "relative", "top": "45%"}',
    'show_duration': 100,
    'style': '{"position": "absolute", "backgroundColor": "#ffffff", "opacity": 0.5, "textAlign": "center"}'
}


## NAVIGATION
DEFAULT_NAVIGATION = {
    'bindings_class_name': 'highcharts-bindings-container',
    'icons_url': 'https://code.highcharts.com/@product.version@/gfx/stock-icons/'
}

## PANE
DEFAULT_PANE = {
    'center': [['50%', '50%']],
    'end_angle': None,
    'inner_size': '0%',
    'size': '85%',
    'start_angle': 0
}
DEFAULT_PANE_BACKGROUND = {
    'background_color': '{ "linearGradient": { "x1": 0, "y1": 0, "x2": 0, "y2": 1 }, stops: [[0, "#ffffff"], [1, "#e6e6e6"]] }',
    'border_color': '#cccccc',
    'border_width': 1,
    'class_name': 'highcharts-pane',
    'inner_radius': 0,
    'outer_radius': '105%',
    'shape': 'circle'
}


## TOOLTIP
DEFAULT_TOOLTIP = {
    'border_radius': 3,
    'border_width': 1,
    'distance': 16,
    'footer_format': '',
    'header_shape': 'callout',
    'hide_delay': 500,
    'padding': 8,
    'shape': 'callout',
    'snap': None
}


DEFAULT_DATE_TIME_LABEL_FORMATS = {
    'day': '%A, %b %e, %Y',
    'hour': '%A, %b %e, %H:%M',
    'millisecond': '%A, %b %e, %H:%M:%S.%L',
    'minute': '%A, %b %e, %H:%M',
    'month': '%B %Y',
    'second': '%A, %b %e, %H:%M:%S',
    'week': 'Week from %A, %b %e, %Y',
    'year': '%Y'
}


## DATA LABELS
DEFAULT_DATA_LABEL = {
    'border_radius': 0,
    'border_width': 0,
    'class_name': None,
    'color': None,
    'crop': True,
    'defer': True,
    'format': 'point.value',
    'overflow': 'justify',
    'padding': 5,
    'position': 'center',
    'rotation': 0,
    'shadow': False,
    'shape': 'square',
    'style': None,
    'vertical_align': None,
    'x': 0,
    'y': None,
    'z': 6
}


## MARKER
DEFAULT_MARKER = {
    'enabled_threshold': 2,
    'line_color': '#ffffff',
    'line_width': 0,
    'radius': 4,
    'symbol': None,
    'width': None
}


## DAYS OF WEEK
DAYS_OF_WEEK = {
    'sunday': 0,
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6
}

## SONIFICATION INSTRUMENTS
INSTRUMENT_PRESETS = [
    'piano',
    'flute',
    'saxophone',
    'trumpet',
    'sawsynth',
    'wobble',
    'basic1',
    'basic2',
    'sine',
    'sineGlide',
    'triangle',
    'square',
    'sawtooth',
    'noise',
    'filteredNoise',
    'wind',
]

EXPORT_SERVER_UNSUPPORTED_SERIES_TYPES = [
    'pictorial',
    'flowmap',
    'geoheatmap',
    'treegraph',
]