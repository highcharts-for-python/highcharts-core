from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class PopupLanguageOptions(HighchartsMeta):
    """Translations for all field names used in popup."""

    def __init__(self, **kwargs):
        self._add_button = None
        self._algorithm = None
        self._arrow_infinity_line = None
        self._arrow_ray = None
        self._arrow_segment = None
        self._average = None
        self._background = None
        self._background_color = None
        self._background_colors = None
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._bottom_band = None
        self._circle = None
        self._clear_filter = None
        self._color = None
        self._connector = None
        self._crooked3 = None
        self._crooked5 = None
        self._crosshairX = None
        self._crosshairY = None
        self._decimals = None
        self._deviation = None
        self._edit_button = None
        self._elliott3 = None
        self._elliott5 = None
        self._ellipse = None
        self._factor = None
        self._fast_avg_period = None
        self._fibonacci = None
        self._fibonacci_time_zones = None
        self._fill = None
        self._flags = None
        self._font_size = None
        self._format = None
        self._height = None
        self._high_index = None
        self._horizontal_line = None
        self._increment = None
        self._index = None
        self._infinity_line = None
        self._initial_acceleration_factor = None
        self._inner_background = None
        self._label = None
        self._label_options = None
        self._labels = None
        self._line = None
        self._lines = None
        self._long_period = None
        self._low_index = None
        self._max_acceleration_factor = None
        self._measure = None
        self._measure_x = None
        self._measure_xy = None
        self._measure_y = None
        self._multiplier = None
        self._multiplier_atr = None
        self._name = None
        self._no_filter_match = None
        self._outer_background = None
        self._padding = None
        self._parallel_channel = None
        self._period = None
        self._period_atr = None
        self._periods = None
        self._period_senkou_span_b = None
        self._period_tenkan = None
        self._pitchfork = None
        self._ranges = None
        self._ray = None
        self._rectangle = None
        self._remove_button = None
        self._save_button = None
        self._search_indicators = None
        self._segment = None
        self._series = None
        self._shape_options = None
        self._shapes = None
        self._short_period = None
        self._signal_period = None
        self._simple_shapes = None
        self._slow_avg_period = None
        self._standard_deviation = None
        self._stroke = None
        self._stroke_width = None
        self._style = None
        self._time_cycles = None
        self._title = None
        self._top_band = None
        self._tunnel = None
        self._type_options = None
        self._vertical_arrow = None
        self._vertical_counter = None
        self._vertical_label = None
        self._vertical_line = None
        self._volume = None
        self._x_axis_unit = None

        self.add_button = kwargs.pop('add_button', None)
        self.algorithm = kwargs.pop('algorithm', None)
        self.arrow_infinity_line = kwargs.pop('arrow_infinity_line', None)
        self.arrow_ray = kwargs.pop('arrow_ray', None)
        self.arrow_segment = kwargs.pop('arrow_segment', None)
        self.average = kwargs.pop('average', None)
        self.background = kwargs.pop('background', None)
        self.background_color = kwargs.pop('background_color', None)
        self.background_colors = kwargs.pop('background_colors', None)
        self.border_color = kwargs.pop('border_color', None)
        self.border_radius = kwargs.pop('border_radius', None)
        self.border_width = kwargs.pop('border_width', None)
        self.bottom_band = kwargs.pop('bottom_band', None)
        self.circle = kwargs.pop('circle', None)
        self.clear_filter = kwargs.pop('clear_filter', None)
        self.color = kwargs.pop('color', None)
        self.connector = kwargs.pop('connector', None)
        self.crooked3 = kwargs.pop('crooked3', None)
        self.crooked5 = kwargs.pop('crooked5', None)
        self.crosshairX = kwargs.pop('crosshairX', None)
        self.crosshairY = kwargs.pop('crosshairY', None)
        self.decimals = kwargs.pop('decimals', None)
        self.deviation = kwargs.pop('deviation', None)
        self.edit_button = kwargs.pop('edit_button', None)
        self.elliott3 = kwargs.pop('elliott3', None)
        self.elliott5 = kwargs.pop('elliott5', None)
        self.ellipse = kwargs.pop('ellipse', None)
        self.factor = kwargs.pop('factor', None)
        self.fast_avg_period = kwargs.pop('fast_avg_period', None)
        self.fibonacci = kwargs.pop('fibonacci', None)
        self.fibonacci_time_zones = kwargs.pop('fibonacci_time_zones', None)
        self.fill = kwargs.pop('fill', None)
        self.flags = kwargs.pop('flags', None)
        self.font_size = kwargs.pop('font_size', None)
        self.format = kwargs.pop('format', None)
        self.height = kwargs.pop('height', None)
        self.high_index = kwargs.pop('high_index', None)
        self.horizontal_line = kwargs.pop('horizontal_line', None)
        self.increment = kwargs.pop('increment', None)
        self.index = kwargs.pop('index', None)
        self.infinity_line = kwargs.pop('infinity_line', None)
        self.initial_acceleration_factor = kwargs.pop('initial_acceleration_factor', None)
        self.inner_background = kwargs.pop('inner_background', None)
        self.label = kwargs.pop('label', None)
        self.label_options = kwargs.pop('label_options', None)
        self.labels = kwargs.pop('labels', None)
        self.line = kwargs.pop('line', None)
        self.lines = kwargs.pop('lines', None)
        self.long_period = kwargs.pop('long_period', None)
        self.low_index = kwargs.pop('low_index', None)
        self.max_acceleration_factor = kwargs.pop('max_acceleration_factor', None)
        self.measure = kwargs.pop('measure', None)
        self.measure_x = kwargs.pop('measure_x', None)
        self.measure_xy = kwargs.pop('measure_xy', None)
        self.measure_y = kwargs.pop('measure_y', None)
        self.multiplier = kwargs.pop('multiplier', None)
        self.multiplier_atr = kwargs.pop('multiplier_atr', None)
        self.name = kwargs.pop('name', None)
        self.no_filter_match = kwargs.pop('no_filter_match', None)
        self.outer_background = kwargs.pop('outer_background', None)
        self.padding = kwargs.pop('padding', None)
        self.parallel_channel = kwargs.pop('parallel_channel', None)
        self.period = kwargs.pop('period', None)
        self.period_atr = kwargs.pop('period_atr', None)
        self.periods = kwargs.pop('periods', None)
        self.period_senkou_span_b = kwargs.pop('period_senkou_span_b', None)
        self.period_tenkan = kwargs.pop('period_tenkan', None)
        self.pitchfork = kwargs.pop('pitchfork', None)
        self.ranges = kwargs.pop('ranges', None)
        self.ray = kwargs.pop('ray', None)
        self.rectangle = kwargs.pop('rectangle', None)
        self.remove_button = kwargs.pop('remove_button', None)
        self.save_button = kwargs.pop('save_button', None)
        self.search_indicators = kwargs.pop('search_indicators', None)
        self.segment = kwargs.pop('segment', None)
        self.series = kwargs.pop('series', None)
        self.shape_options = kwargs.pop('shape_options', None)
        self.shapes = kwargs.pop('shapes', None)
        self.short_period = kwargs.pop('short_period', None)
        self.signal_period = kwargs.pop('signal_period', None)
        self.simple_shapes = kwargs.pop('simple_shapes', None)
        self.slow_avg_period = kwargs.pop('slow_avg_period', None)
        self.standard_deviation = kwargs.pop('standard_deviation', None)
        self.stroke = kwargs.pop('stroke', None)
        self.stroke_width = kwargs.pop('stroke_width', None)
        self.style = kwargs.pop('style', None)
        self.time_cycles = kwargs.pop('time_cycles', None)
        self.title = kwargs.pop('title', None)
        self.top_band = kwargs.pop('top_band', None)
        self.tunnel = kwargs.pop('tunnel', None)
        self.type_options = kwargs.pop('type_options', None)
        self.vertical_arrow = kwargs.pop('vertical_arrow', None)
        self.vertical_counter = kwargs.pop('vertical_counter', None)
        self.vertical_label = kwargs.pop('vertical_label', None)
        self.vertical_line = kwargs.pop('vertical_line', None)
        self.volume = kwargs.pop('volume', None)
        self.x_axis_unit = kwargs.pop('x_axis_unit', None)

    @property
    def add_button(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('add_button')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._add_button

    @add_button.setter
    def add_button(self, value):
        self._add_button = validators.string(value, allow_empty = True)

    @property
    def algorithm(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('algorithm')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        self._algorithm = validators.string(value, allow_empty = True)

    @property
    def arrow_infinity_line(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('arrow_infinity_line')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._arrow_infinity_line

    @arrow_infinity_line.setter
    def arrow_infinity_line(self, value):
        self._arrow_infinity_line = validators.string(value, allow_empty = True)

    @property
    def arrow_ray(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('arrow_ray')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._arrow_ray

    @arrow_ray.setter
    def arrow_ray(self, value):
        self._arrow_ray = validators.string(value, allow_empty = True)

    @property
    def arrow_segment(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('arrow_segment')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._arrow_segment

    @arrow_segment.setter
    def arrow_segment(self, value):
        self._arrow_segment = validators.string(value, allow_empty = True)

    @property
    def average(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('average')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._average

    @average.setter
    def average(self, value):
        self._average = validators.string(value, allow_empty = True)

    @property
    def background(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('background')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._background

    @background.setter
    def background(self, value):
        self._background = validators.string(value, allow_empty = True)

    @property
    def background_color(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('background_color')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = validators.string(value, allow_empty = True)

    @property
    def background_colors(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('background_colors')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._background_colors

    @background_colors.setter
    def background_colors(self, value):
        self._background_colors = validators.string(value, allow_empty = True)

    @property
    def border_color(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('border_color')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = validators.string(value, allow_empty = True)

    @property
    def border_radius(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('border_radius')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.string(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('border_width')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.string(value, allow_empty = True)

    @property
    def bottom_band(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('bottom_band')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._bottom_band

    @bottom_band.setter
    def bottom_band(self, value):
        self._bottom_band = validators.string(value, allow_empty = True)

    @property
    def circle(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('circle')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._circle

    @circle.setter
    def circle(self, value):
        self._circle = validators.string(value, allow_empty = True)

    @property
    def clear_filter(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('clear_filter')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._clear_filter

    @clear_filter.setter
    def clear_filter(self, value):
        self._clear_filter = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('color')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def connector(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('connector')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._connector

    @connector.setter
    def connector(self, value):
        self._connector = validators.string(value, allow_empty = True)

    @property
    def crooked3(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crooked3')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._crooked3

    @crooked3.setter
    def crooked3(self, value):
        self._crooked3 = validators.string(value, allow_empty = True)

    @property
    def crooked5(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crooked5')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._crooked5

    @crooked5.setter
    def crooked5(self, value):
        self._crooked5 = validators.string(value, allow_empty = True)

    @property
    def crosshairX(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crosshairX')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._crosshairX

    @crosshairX.setter
    def crosshairX(self, value):
        self._crosshairX = validators.string(value, allow_empty = True)

    @property
    def crosshairY(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crosshairY')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._crosshairY

    @crosshairY.setter
    def crosshairY(self, value):
        self._crosshairY = validators.string(value, allow_empty = True)

    @property
    def decimals(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('decimals')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._decimals

    @decimals.setter
    def decimals(self, value):
        self._decimals = validators.string(value, allow_empty = True)

    @property
    def deviation(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('deviation')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._deviation

    @deviation.setter
    def deviation(self, value):
        self._deviation = validators.string(value, allow_empty = True)

    @property
    def edit_button(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('edit_button')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._edit_button

    @edit_button.setter
    def edit_button(self, value):
        self._edit_button = validators.string(value, allow_empty = True)

    @property
    def elliott3(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('elliott3')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._elliott3

    @elliott3.setter
    def elliott3(self, value):
        self._elliott3 = validators.string(value, allow_empty = True)

    @property
    def elliott5(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('elliott5')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._elliott5

    @elliott5.setter
    def elliott5(self, value):
        self._elliott5 = validators.string(value, allow_empty = True)

    @property
    def ellipse(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('ellipse')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._ellipse

    @ellipse.setter
    def ellipse(self, value):
        self._ellipse = validators.string(value, allow_empty = True)

    @property
    def factor(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('factor')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._factor

    @factor.setter
    def factor(self, value):
        self._factor = validators.string(value, allow_empty = True)

    @property
    def fast_avg_period(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('fast_avg_period')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._fast_avg_period

    @fast_avg_period.setter
    def fast_avg_period(self, value):
        self._fast_avg_period = validators.string(value, allow_empty = True)

    @property
    def fibonacci(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('fibonacci')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._fibonacci

    @fibonacci.setter
    def fibonacci(self, value):
        self._fibonacci = validators.string(value, allow_empty = True)

    @property
    def fibonacci_time_zones(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('fibonacci_time_zones')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._fibonacci_time_zones

    @fibonacci_time_zones.setter
    def fibonacci_time_zones(self, value):
        self._fibonacci_time_zones = validators.string(value, allow_empty = True)

    @property
    def fill(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('fill')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = validators.string(value, allow_empty = True)

    @property
    def flags(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('flags')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._flags

    @flags.setter
    def flags(self, value):
        self._flags = validators.string(value, allow_empty = True)

    @property
    def font_size(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('font_size')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = validators.string(value, allow_empty = True)

    @property
    def format(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('format')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._format

    @format.setter
    def format(self, value):
        self._format = validators.string(value, allow_empty = True)

    @property
    def height(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('height')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.string(value, allow_empty = True)

    @property
    def high_index(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('high_index')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._high_index

    @high_index.setter
    def high_index(self, value):
        self._high_index = validators.string(value, allow_empty = True)

    @property
    def horizontal_line(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('horizontal_line')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._horizontal_line

    @horizontal_line.setter
    def horizontal_line(self, value):
        self._horizontal_line = validators.string(value, allow_empty = True)

    @property
    def increment(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('increment')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._increment

    @increment.setter
    def increment(self, value):
        self._increment = validators.string(value, allow_empty = True)

    @property
    def index(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('index')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._index

    @index.setter
    def index(self, value):
        self._index = validators.string(value, allow_empty = True)

    @property
    def infinity_line(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('infinity_line')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._infinity_line

    @infinity_line.setter
    def infinity_line(self, value):
        self._infinity_line = validators.string(value, allow_empty = True)

    @property
    def initial_acceleration_factor(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('initial_acceleration_factor')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._initial_acceleration_factor

    @initial_acceleration_factor.setter
    def initial_acceleration_factor(self, value):
        self._initial_acceleration_factor = validators.string(value, allow_empty = True)

    @property
    def inner_background(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('inner_background')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._inner_background

    @inner_background.setter
    def inner_background(self, value):
        self._inner_background = validators.string(value, allow_empty = True)

    @property
    def label(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('label')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._label

    @label.setter
    def label(self, value):
        self._label = validators.string(value, allow_empty = True)

    @property
    def label_options(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('label_options')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._label_options

    @label_options.setter
    def label_options(self, value):
        self._label_options = validators.string(value, allow_empty = True)

    @property
    def labels(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('labels')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._labels

    @labels.setter
    def labels(self, value):
        self._labels = validators.string(value, allow_empty = True)

    @property
    def line(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('line')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._line

    @line.setter
    def line(self, value):
        self._line = validators.string(value, allow_empty = True)

    @property
    def lines(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('lines')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = validators.string(value, allow_empty = True)

    @property
    def long_period(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('long_period')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._long_period

    @long_period.setter
    def long_period(self, value):
        self._long_period = validators.string(value, allow_empty = True)

    @property
    def low_index(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('low_index')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._low_index

    @low_index.setter
    def low_index(self, value):
        self._low_index = validators.string(value, allow_empty = True)

    @property
    def max_acceleration_factor(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('max_acceleration_factor')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._max_acceleration_factor

    @max_acceleration_factor.setter
    def max_acceleration_factor(self, value):
        self._max_acceleration_factor = validators.string(value, allow_empty = True)

    @property
    def measure(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._measure

    @measure.setter
    def measure(self, value):
        self._measure = validators.string(value, allow_empty = True)

    @property
    def measure_x(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure_x')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._measure_x

    @measure_x.setter
    def measure_x(self, value):
        self._measure_x = validators.string(value, allow_empty = True)

    @property
    def measure_xy(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure_xy')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._measure_xy

    @measure_xy.setter
    def measure_xy(self, value):
        self._measure_xy = validators.string(value, allow_empty = True)

    @property
    def measure_y(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure_y')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._measure_y

    @measure_y.setter
    def measure_y(self, value):
        self._measure_y = validators.string(value, allow_empty = True)

    @property
    def multiplier(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('multiplier')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, value):
        self._multiplier = validators.string(value, allow_empty = True)

    @property
    def multiplier_atr(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('multiplier_atr')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._multiplier_atr

    @multiplier_atr.setter
    def multiplier_atr(self, value):
        self._multiplier_atr = validators.string(value, allow_empty = True)

    @property
    def name(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('name')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def no_filter_match(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('no_filter_match')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._no_filter_match

    @no_filter_match.setter
    def no_filter_match(self, value):
        self._no_filter_match = validators.string(value, allow_empty = True)

    @property
    def outer_background(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('outer_background')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._outer_background

    @outer_background.setter
    def outer_background(self, value):
        self._outer_background = validators.string(value, allow_empty = True)

    @property
    def padding(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('padding')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validators.string(value, allow_empty = True)

    @property
    def parallel_channel(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('parallel_channel')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._parallel_channel

    @parallel_channel.setter
    def parallel_channel(self, value):
        self._parallel_channel = validators.string(value, allow_empty = True)

    @property
    def period(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('period')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._period

    @period.setter
    def period(self, value):
        self._period = validators.string(value, allow_empty = True)

    @property
    def period_atr(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('period_atr')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._period_atr

    @period_atr.setter
    def period_atr(self, value):
        self._period_atr = validators.string(value, allow_empty = True)

    @property
    def periods(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('periods')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._periods

    @periods.setter
    def periods(self, value):
        self._periods = validators.string(value, allow_empty = True)

    @property
    def period_senkou_span_b(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('period_senkou_span_b')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._period_senkou_span_b

    @period_senkou_span_b.setter
    def period_senkou_span_b(self, value):
        self._period_senkou_span_b = validators.string(value, allow_empty = True)

    @property
    def period_tenkan(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('period_tenkan')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._period_tenkan

    @period_tenkan.setter
    def period_tenkan(self, value):
        self._period_tenkan = validators.string(value, allow_empty = True)

    @property
    def pitchfork(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('pitchfork')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._pitchfork

    @pitchfork.setter
    def pitchfork(self, value):
        self._pitchfork = validators.string(value, allow_empty = True)

    @property
    def ranges(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('ranges')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._ranges

    @ranges.setter
    def ranges(self, value):
        self._ranges = validators.string(value, allow_empty = True)

    @property
    def ray(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('ray')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._ray

    @ray.setter
    def ray(self, value):
        self._ray = validators.string(value, allow_empty = True)

    @property
    def rectangle(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('rectangle')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, value):
        self._rectangle = validators.string(value, allow_empty = True)

    @property
    def remove_button(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('remove_button')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._remove_button

    @remove_button.setter
    def remove_button(self, value):
        self._remove_button = validators.string(value, allow_empty = True)

    @property
    def save_button(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('save_button')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._save_button

    @save_button.setter
    def save_button(self, value):
        self._save_button = validators.string(value, allow_empty = True)

    @property
    def search_indicators(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('search_indicators')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._search_indicators

    @search_indicators.setter
    def search_indicators(self, value):
        self._search_indicators = validators.string(value, allow_empty = True)

    @property
    def segment(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('segment')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._segment

    @segment.setter
    def segment(self, value):
        self._segment = validators.string(value, allow_empty = True)

    @property
    def series(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('series')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._series

    @series.setter
    def series(self, value):
        self._series = validators.string(value, allow_empty = True)

    @property
    def shape_options(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('shape_options')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._shape_options

    @shape_options.setter
    def shape_options(self, value):
        self._shape_options = validators.string(value, allow_empty = True)

    @property
    def shapes(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('shapes')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._shapes

    @shapes.setter
    def shapes(self, value):
        self._shapes = validators.string(value, allow_empty = True)

    @property
    def short_period(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('short_period')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._short_period

    @short_period.setter
    def short_period(self, value):
        self._short_period = validators.string(value, allow_empty = True)

    @property
    def signal_period(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('signal_period')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._signal_period

    @signal_period.setter
    def signal_period(self, value):
        self._signal_period = validators.string(value, allow_empty = True)

    @property
    def simple_shapes(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('simple_shapes')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._simple_shapes

    @simple_shapes.setter
    def simple_shapes(self, value):
        self._simple_shapes = validators.string(value, allow_empty = True)

    @property
    def slow_avg_period(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('slow_avg_period')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._slow_avg_period

    @slow_avg_period.setter
    def slow_avg_period(self, value):
        self._slow_avg_period = validators.string(value, allow_empty = True)

    @property
    def standard_deviation(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_NAVIGATION.get('standard_deviation')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._standard_deviation

    @standard_deviation.setter
    def standard_deviation(self, value):
        self._standard_deviation = validators.string(value, allow_empty = True)

    @property
    def stroke(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('stroke')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        self._stroke = validators.string(value, allow_empty = True)

    @property
    def stroke_width(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('stroke_width')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        self._stroke_width = validators.string(value, allow_empty = True)

    @property
    def style(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('style')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @property
    def time_cycles(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('time_cycles')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._time_cycles

    @time_cycles.setter
    def time_cycles(self, value):
        self._time_cycles = validators.string(value, allow_empty = True)

    @property
    def title(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('title')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._title

    @title.setter
    def title(self, value):
        self._title = validators.string(value, allow_empty = True)

    @property
    def top_band(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('top_band')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._top_band

    @top_band.setter
    def top_band(self, value):
        self._top_band = validators.string(value, allow_empty = True)

    @property
    def tunnel(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('tunnel')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._tunnel

    @tunnel.setter
    def tunnel(self, value):
        self._tunnel = validators.string(value, allow_empty = True)

    @property
    def type_options(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('type_options')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._type_options

    @type_options.setter
    def type_options(self, value):
        self._type_options = validators.string(value, allow_empty = True)

    @property
    def vertical_arrow(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_arrow')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._vertical_arrow

    @vertical_arrow.setter
    def vertical_arrow(self, value):
        self._vertical_arrow = validators.string(value, allow_empty = True)

    @property
    def vertical_counter(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_counter')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._vertical_counter

    @vertical_counter.setter
    def vertical_counter(self, value):
        self._vertical_counter = validators.string(value, allow_empty = True)

    @property
    def vertical_label(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_label')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._vertical_label

    @vertical_label.setter
    def vertical_label(self, value):
        self._vertical_label = validators.string(value, allow_empty = True)

    @property
    def vertical_line(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_line')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._vertical_line

    @vertical_line.setter
    def vertical_line(self, value):
        self._vertical_line = validators.string(value, allow_empty = True)

    @property
    def volume(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('volume')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = validators.string(value, allow_empty = True)

    @property
    def x_axis_unit(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('x_axis_unit')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._x_axis_unit

    @x_axis_unit.setter
    def x_axis_unit(self, value):
        self._x_axis_unit = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'add_button': as_dict.pop('addButton', None),
            'algorithm': as_dict.pop('algorithm', None),
            'arrow_infinity_line': as_dict.pop('arrowInfinityLine', None),
            'arrow_ray': as_dict.pop('arrowRay', None),
            'arrow_segment': as_dict.pop('arrowSegment', None),
            'average': as_dict.pop('average', None),
            'background': as_dict.pop('background', None),
            'background_color': as_dict.pop('backgroundColor', None),
            'background_colors': as_dict.pop('backgroundColors', None),
            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'bottom_band': as_dict.pop('bottomBand', None),
            'circle': as_dict.pop('circle', None),
            'clear_filter': as_dict.pop('clearFilter', None),
            'color': as_dict.pop('color', None),
            'connector': as_dict.pop('connector', None),
            'crooked3': as_dict.pop('crooked3', None),
            'crooked5': as_dict.pop('crooked5', None),
            'crosshairX': as_dict.pop('crosshairX', None),
            'crosshairY': as_dict.pop('crosshairY', None),
            'decimals': as_dict.pop('decimals', None),
            'deviation': as_dict.pop('deviation', None),
            'edit_button': as_dict.pop('editButton', None),
            'elliott3': as_dict.pop('elliott3', None),
            'elliott5': as_dict.pop('elliott5', None),
            'ellipse': as_dict.pop('ellipse', None),
            'factor': as_dict.pop('factor', None),
            'fast_avg_period': as_dict.pop('fastAvgPeriod', None),
            'fibonacci': as_dict.pop('fibonacci', None),
            'fibonacci_time_zones': as_dict.pop('fibonacciTimeZones', None),
            'fill': as_dict.pop('fill', None),
            'flags': as_dict.pop('flags', None),
            'font_size': as_dict.pop('fontSize', None),
            'format': as_dict.pop('format', None),
            'height': as_dict.pop('height', None),
            'high_index': as_dict.pop('highIndex', None),
            'horizontal_line': as_dict.pop('horizontalLine', None),
            'increment': as_dict.pop('increment', None),
            'index': as_dict.pop('index', None),
            'infinity_line': as_dict.pop('infinityLine', None),
            'initial_acceleration_factor': as_dict.pop('initialAccelerationFactor', None),
            'inner_background': as_dict.pop('innerBackground', None),
            'label': as_dict.pop('label', None),
            'label_options': as_dict.pop('labelOptions', None),
            'labels': as_dict.pop('labels', None),
            'line': as_dict.pop('line', None),
            'lines': as_dict.pop('lines', None),
            'long_period': as_dict.pop('longPeriod', None),
            'low_index': as_dict.pop('lowIndex', None),
            'max_acceleration_factor': as_dict.pop('maxAccelerationFactor', None),
            'measure': as_dict.pop('measure', None),
            'measure_x': as_dict.pop('measureX', None),
            'measure_xy': as_dict.pop('measureXY', None),
            'measure_y': as_dict.pop('measureY', None),
            'multiplier': as_dict.pop('multiplier', None),
            'multiplier_atr': as_dict.pop('multiplierATR', None),
            'name': as_dict.pop('name', None),
            'no_filter_match': as_dict.pop('noFilterMatch', None),
            'outer_background': as_dict.pop('outerBackground', None),
            'padding': as_dict.pop('padding', None),
            'parallel_channel': as_dict.pop('parallelChannel', None),
            'period': as_dict.pop('period', None),
            'period_atr': as_dict.pop('periodATR', None),
            'periods': as_dict.pop('periods', None),
            'period_senkou_span_b': as_dict.pop('periodSenkouSpanB', None),
            'period_tenkan': as_dict.pop('periodTenkan', None),
            'pitchfork': as_dict.pop('pitchfork', None),
            'ranges': as_dict.pop('ranges', None),
            'ray': as_dict.pop('ray', None),
            'rectangle': as_dict.pop('rectangle', None),
            'remove_button': as_dict.pop('removeButton', None),
            'save_button': as_dict.pop('saveButton', None),
            'search_indicators': as_dict.pop('searchIndicators', None),
            'segment': as_dict.pop('segment', None),
            'series': as_dict.pop('series', None),
            'shape_options': as_dict.pop('shapeOptions', None),
            'shapes': as_dict.pop('shapes', None),
            'short_period': as_dict.pop('shortPeriod', None),
            'signal_period': as_dict.pop('signalPeriod', None),
            'simple_shapes': as_dict.pop('simpleShapes', None),
            'slow_avg_period': as_dict.pop('slowAvgPeriod', None),
            'standard_deviation': as_dict.pop('standardDeviation', None),
            'stroke': as_dict.pop('stroke', None),
            'stroke_width': as_dict.pop('strokeWidth', None),
            'style': as_dict.pop('style', None),
            'time_cycles': as_dict.pop('timeCycles', None),
            'title': as_dict.pop('title', None),
            'top_band': as_dict.pop('topBand', None),
            'tunnel': as_dict.pop('tunnel', None),
            'type_options': as_dict.pop('typeOptions', None),
            'vertical_arrow': as_dict.pop('verticalArrow', None),
            'vertical_counter': as_dict.pop('verticalCounter', None),
            'vertical_label': as_dict.pop('verticalLabel', None),
            'vertical_line': as_dict.pop('verticalLine', None),
            'volume': as_dict.pop('volume', None),
            'x_axis_unit': as_dict.pop('xAxisUnit', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'addButton': self.add_button,
            'algorithm': self.algorithm,
            'arrowInfinityLine': self.arrow_infinity_line,
            'arrowRay': self.arrow_ray,
            'arrowSegment': self.arrow_segment,
            'average': self.average,
            'background': self.background,
            'backgroundColor': self.background_color,
            'backgroundColors': self.background_colors,
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'bottomBand': self.bottom_band,
            'circle': self.circle,
            'clearFilter': self.clear_filter,
            'color': self.color,
            'connector': self.connector,
            'crooked3': self.crooked3,
            'crooked5': self.crooked5,
            'crosshairX': self.crosshairX,
            'crosshairY': self.crosshairY,
            'decimals': self.decimals,
            'deviation': self.deviation,
            'editButton': self.edit_button,
            'elliott3': self.elliott3,
            'elliott5': self.elliott5,
            'ellipse': self.ellipse,
            'factor': self.factor,
            'fast_avg_period': self.fast_avg_period,
            'fibonacci': self.fibonacci,
            'fibonacciTimeZones': self.fibonacci_time_zones,
            'fill': self.fill,
            'flags': self.flags,
            'fontSize': self.font_size,
            'format': self.format,
            'height': self.height,
            'highIndex': self.high_index,
            'horizontalLine': self.horizontal_line,
            'increment': self.increment,
            'index': self.index,
            'infinityLine': self.infinity_line,
            'initialAccelerationFactor': self.initial_acceleration_factor,
            'innerBackground': self.inner_background,
            'label': self.label,
            'labelOptions': self.label_options,
            'labels': self.labels,
            'line': self.line,
            'lines': self.lines,
            'longPeriod': self.long_period,
            'lowIndex': self.low_index,
            'maxAccelerationFactor': self.max_acceleration_factor,
            'measure': self.measure,
            'measureX': self.measure_x,
            'measureXY': self.measure_xy,
            'measureY': self.measure_y,
            'multiplier': self.multiplier,
            'multiplierATR': self.multiplier_atr,
            'name': self.name,
            'noFilterMatch': self.no_filter_match,
            'outerBackground': self.outer_background,
            'padding': self.padding,
            'parallelChannel': self.parallel_channel,
            'period': self.period,
            'periodATR': self.period_atr,
            'periods': self.periods,
            'periodSenkouSpanB': self.period_senkou_span_b,
            'periodTenkan': self.period_tenkan,
            'pitchfork': self.pitchfork,
            'ranges': self.ranges,
            'ray': self.ray,
            'rectangle': self.rectangle,
            'removeButton': self.remove_button,
            'saveButton': self.save_button,
            'searchIndicators': self.search_indicators,
            'segment': self.segment,
            'series': self.series,
            'shapeOptions': self.shape_options,
            'shapes': self.shapes,
            'shortPeriod': self.short_period,
            'signalPeriod': self.signal_period,
            'simpleShapes': self.simple_shapes,
            'slowAvgPeriod': self.slow_avg_period,
            'standardDeviation': self.standard_deviation,
            'stroke': self.stroke,
            'strokeWidth': self.stroke_width,
            'style': self.style,
            'timeCycles': self.time_cycles,
            'title': self.title,
            'topBand': self.top_band,
            'tunnel': self.tunnel,
            'typeOptions': self.type_options,
            'verticalArrow': self.vertical_arrow,
            'verticalCounter': self.vertical_counter,
            'verticalLabel': self.vertical_label,
            'verticalLine': self.vertical_line,
            'volume': self.volume,
            'xAxisUnit': self.x_axis_unit
        }

        return untrimmed


class NavigationLanguageOptions(HighchartsMeta):
    """The Popup strings used in the chart.

    .. note::

      Requires the ``annotations.js`` or ``annotations-advanced.src.js`` module to be
      loaded.

    """

    def __init__(self, **kwargs):
        self._popup = None

        self.popup = kwargs.pop('popup', None)

    @property
    def popup(self) -> Optional[PopupLanguageOptions]:
        """Translations for all field names used in popup.

        :rtype: :class:`PopupLanguageOptions` or :obj:`None <python:None>`
        """
        return self._popup

    @popup.setter
    @class_sensitive(PopupLanguageOptions)
    def popup(self, value):
        self._popup = value

    @classmethod
    def from_dict(cls, as_dict):
        return cls(popup = as_dict.pop('popup', None))

    def _to_untrimmed_dict(self) -> dict:
        return {
            'popup': self.popup
        }
