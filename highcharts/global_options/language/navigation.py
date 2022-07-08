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

        self.add_button = kwargs.pop('add_button',
                                     constants.DEFAULT_LANG_NAVIGATION.get('add_button'))
        self.algorithm = kwargs.pop('algorithm',
                                    constants.DEFAULT_LANG_NAVIGATION.get('algorithm'))
        self.arrow_infinity_line = kwargs.pop('arrow_infinity_line',
                                              constants.DEFAULT_LANG_NAVIGATION.get('arrow_infinity_line'))
        self.arrow_ray = kwargs.pop('arrow_ray',
                                    constants.DEFAULT_LANG_NAVIGATION.get('arrow_ray'))
        self.arrow_segment = kwargs.pop('arrow_segment',
                                        constants.DEFAULT_LANG_NAVIGATION.get('arrow_segment'))
        self.average = kwargs.pop('average',
                                  constants.DEFAULT_LANG_NAVIGATION.get('average'))
        self.background = kwargs.pop('background',
                                     constants.DEFAULT_LANG_NAVIGATION.get('background'))
        self.background_color = kwargs.pop('background_color',
                                           constants.DEFAULT_LANG_NAVIGATION.get('background_color'))
        self.background_colors = kwargs.pop('background_colors',
                                            constants.DEFAULT_LANG_NAVIGATION.get('background_colors'))
        self.border_color = kwargs.pop('border_color',
                                       constants.DEFAULT_LANG_NAVIGATION.get('border_color'))
        self.border_radius = kwargs.pop('border_radius',
                                        constants.DEFAULT_LANG_NAVIGATION.get('border_radius'))
        self.border_width = kwargs.pop('border_width',
                                       constants.DEFAULT_LANG_NAVIGATION.get('border_width'))
        self.bottom_band = kwargs.pop('bottom_band',
                                      constants.DEFAULT_LANG_NAVIGATION.get('bottom_band'))
        self.circle = kwargs.pop('circle',
                                 constants.DEFAULT_LANG_NAVIGATION.get('circle'))
        self.clear_filter = kwargs.pop('clear_filter',
                                       constants.DEFAULT_LANG_NAVIGATION.get('clear_filter'))
        self.color = kwargs.pop('color',
                                constants.DEFAULT_LANG_NAVIGATION.get('color'))
        self.connector = kwargs.pop('connector',
                                    constants.DEFAULT_LANG_NAVIGATION.get('connector'))
        self.crooked3 = kwargs.pop('crooked3',
                                   constants.DEFAULT_LANG_NAVIGATION.get('crooked3'))
        self.crooked5 = kwargs.pop('crooked5',
                                   constants.DEFAULT_LANG_NAVIGATION.get('crooked5'))
        self.crosshairX = kwargs.pop('crosshairX',
                                     constants.DEFAULT_LANG_NAVIGATION.get('crosshairX'))
        self.crosshairY = kwargs.pop('crosshairY',
                                     constants.DEFAULT_LANG_NAVIGATION.get('crosshairY'))
        self.decimals = kwargs.pop('decimals',
                                   constants.DEFAULT_LANG_NAVIGATION.get('decimals'))
        self.deviation = kwargs.pop('deviation',
                                    constants.DEFAULT_LANG_NAVIGATION.get('deviation'))
        self.edit_button = kwargs.pop('edit_button',
                                      constants.DEFAULT_LANG_NAVIGATION.get('edit_button'))
        self.elliott3 = kwargs.pop('elliott3',
                                   constants.DEFAULT_LANG_NAVIGATION.get('elliott3'))
        self.elliott5 = kwargs.pop('elliott5',
                                   constants.DEFAULT_LANG_NAVIGATION.get('elliott5'))
        self.ellipse = kwargs.pop('ellipse',
                                  constants.DEFAULT_LANG_NAVIGATION.get('ellipse'))
        self.factor = kwargs.pop('factor',
                                 constants.DEFAULT_LANG_NAVIGATION.get('factor'))
        self.fast_avg_period = kwargs.pop('fast_avg_period',
                                          constants.DEFAULT_LANG_NAVIGATION.get('fast_avg_period'))
        self.fibonacci = kwargs.pop('fibonacci',
                                    constants.DEFAULT_LANG_NAVIGATION.get('fibonacci'))
        self.fibonacci_time_zones = kwargs.pop('fibonacci_time_zones',
                                             constants.DEFAULT_LANG_NAVIGATION.get('fibonacci_time_zones'))
        self.fill = kwargs.pop('fill',
                               constants.DEFAULT_LANG_NAVIGATION.get('fill'))
        self.flags = kwargs.pop('flags',
                                constants.DEFAULT_LANG_NAVIGATION.get('flags'))
        self.font_size = kwargs.pop('font_size',
                                    constants.DEFAULT_LANG_NAVIGATION.get('font_size'))
        self.format = kwargs.pop('format',
                                 constants.DEFAULT_LANG_NAVIGATION.get('format'))
        self.height = kwargs.pop('height',
                                 constants.DEFAULT_LANG_NAVIGATION.get('height'))
        self.high_index = kwargs.pop('high_index',
                                     constants.DEFAULT_LANG_NAVIGATION.get('high_index'))
        self.horizontal_line = kwargs.pop('horizontal_line',
                                          constants.DEFAULT_LANG_NAVIGATION.get('horizontal_line'))
        self.increment = kwargs.pop('increment',
                                    constants.DEFAULT_LANG_NAVIGATION.get('increment'))
        self.index = kwargs.pop('index',
                                constants.DEFAULT_LANG_NAVIGATION.get('index'))
        self.infinity_line = kwargs.pop('infinity_line',
                                        constants.DEFAULT_LANG_NAVIGATION.get('infinity_line'))
        self.initial_acceleration_factor = kwargs.pop('initial_acceleration_factor',
                                                      constants.DEFAULT_LANG_NAVIGATION.get('initial_acceleration_factor'))
        self.inner_background = kwargs.pop('inner_background',
                                           constants.DEFAULT_LANG_NAVIGATION.get('inner_background'))
        self.label = kwargs.pop('label',
                                constants.DEFAULT_LANG_NAVIGATION.get('label'))
        self.label_options = kwargs.pop('label_options',
                                        constants.DEFAULT_LANG_NAVIGATION.get('label_options'))
        self.labels = kwargs.pop('labels',
                                 constants.DEFAULT_LANG_NAVIGATION.get('labels'))
        self.line = kwargs.pop('line',
                               constants.DEFAULT_LANG_NAVIGATION.get('line'))
        self.lines = kwargs.pop('lines',
                                constants.DEFAULT_LANG_NAVIGATION.get('lines'))
        self.long_period = kwargs.pop('long_period',
                                      constants.DEFAULT_LANG_NAVIGATION.get('long_period'))
        self.low_index = kwargs.pop('low_index',
                                    constants.DEFAULT_LANG_NAVIGATION.get('low_index'))
        self.max_acceleration_factor = kwargs.pop('max_acceleration_factor',
                                                  constants.DEFAULT_LANG_NAVIGATION.get('max_acceleration_factor'))
        self.measure = kwargs.pop('measure',
                                  constants.DEFAULT_LANG_NAVIGATION.get('measure'))
        self.measure_x = kwargs.pop('measure_x',
                                    constants.DEFAULT_LANG_NAVIGATION.get('measure_x'))
        self.measure_xy = kwargs.pop('measure_xy',
                                     constants.DEFAULT_LANG_NAVIGATION.get('measure_xy'))
        self.measure_y = kwargs.pop('measure_y',
                                    constants.DEFAULT_LANG_NAVIGATION.get('measure_y'))
        self.multiplier = kwargs.pop('multiplier',
                                     constants.DEFAULT_LANG_NAVIGATION.get('multiplier'))
        self.multiplier_atr = kwargs.pop('multiplier_atr',
                                         constants.DEFAULT_LANG_NAVIGATION.get('multiplier_atr'))
        self.name = kwargs.pop('name',
                               constants.DEFAULT_LANG_NAVIGATION.get('name'))
        self.no_filter_match = kwargs.pop('no_filter_match',
                                          constants.DEFAULT_LANG_NAVIGATION.get('no_filter_match'))
        self.outer_background = kwargs.pop('outer_background',
                                           constants.DEFAULT_LANG_NAVIGATION.get('outer_background'))
        self.padding = kwargs.pop('padding',
                                  constants.DEFAULT_LANG_NAVIGATION.get('padding'))
        self.parallel_channel = kwargs.pop('parallel_channel',
                                           constants.DEFAULT_LANG_NAVIGATION.get('parallel_channel'))
        self.period = kwargs.pop('period',
                                 constants.DEFAULT_LANG_NAVIGATION.get('period'))
        self.period_atr = kwargs.pop('period_atr',
                                     constants.DEFAULT_LANG_NAVIGATION.get('period_atr'))
        self.periods = kwargs.pop('periods',
                                  constants.DEFAULT_LANG_NAVIGATION.get('periods'))
        self.period_senkou_span_b = kwargs.pop('period_senkou_span_b',
                                               constants.DEFAULT_LANG_NAVIGATION.get('period_senkou_span_b'))
        self.period_tenkan = kwargs.pop('period_tenkan',
                                        constants.DEFAULT_LANG_NAVIGATION.get('period_tenkan'))
        self.pitchfork = kwargs.pop('pitchfork',
                                    constants.DEFAULT_LANG_NAVIGATION.get('pitchfork'))
        self.ranges = kwargs.pop('ranges',
                                 constants.DEFAULT_LANG_NAVIGATION.get('ranges'))
        self.ray = kwargs.pop('ray',
                              constants.DEFAULT_LANG_NAVIGATION.get('ray'))
        self.rectangle = kwargs.pop('rectangle',
                                    constants.DEFAULT_LANG_NAVIGATION.get('rectangle'))
        self.remove_button = kwargs.pop('remove_button',
                                        constants.DEFAULT_LANG_NAVIGATION.get('remove_button'))
        self.save_button = kwargs.pop('save_button',
                                      constants.DEFAULT_LANG_NAVIGATION.get('save_button'))
        self.search_indicators = kwargs.pop('search_indicators',
                                            constants.DEFAULT_LANG_NAVIGATION.get('search_indicators'))
        self.segment = kwargs.pop('segment',
                                  constants.DEFAULT_LANG_NAVIGATION.get('segment'))
        self.series = kwargs.pop('series',
                                 constants.DEFAULT_LANG_NAVIGATION.get('series'))
        self.shape_options = kwargs.pop('shape_options',
                                        constants.DEFAULT_LANG_NAVIGATION.get('shape_options'))
        self.shapes = kwargs.pop('shapes',
                                 constants.DEFAULT_LANG_NAVIGATION.get('shapes'))
        self.short_period = kwargs.pop('short_period',
                                       constants.DEFAULT_LANG_NAVIGATION.get('short_period'))
        self.signal_period = kwargs.pop('signal_period',
                                        constants.DEFAULT_LANG_NAVIGATION.get('signal_period'))
        self.simple_shapes = kwargs.pop('simple_shapes',
                                        constants.DEFAULT_LANG_NAVIGATION.get('simple_shapes'))
        self.slow_avg_period = kwargs.pop('slow_avg_period',
                                          constants.DEFAULT_LANG_NAVIGATION.get('slow_avg_period'))
        self.standard_deviation = kwargs.pop('standard_deviation',
                                             constants.DEFAULT_LANG_NAVIGATION.get('standard_deviation'))
        self.stroke = kwargs.pop('stroke',
                                 constants.DEFAULT_LANG_NAVIGATION.get('stroke'))
        self.stroke_width = kwargs.pop('stroke_width',
                                       constants.DEFAULT_LANG_NAVIGATION.get('stroke_width'))
        self.style = kwargs.pop('style',
                                constants.DEFAULT_LANG_NAVIGATION.get('style'))
        self.time_cycles = kwargs.pop('time_cycles',
                                      constants.DEFAULT_LANG_NAVIGATION.get('time_cycles'))
        self.title = kwargs.pop('title',
                                constants.DEFAULT_LANG_NAVIGATION.get('title'))
        self.top_band = kwargs.pop('top_band',
                                   constants.DEFAULT_LANG_NAVIGATION.get('top_band'))
        self.tunnel = kwargs.pop('tunnel',
                                 constants.DEFAULT_LANG_NAVIGATION.get('tunnel'))
        self.type_options = kwargs.pop('type_options',
                                       constants.DEFAULT_LANG_NAVIGATION.get('type_options'))
        self.vertical_arrow = kwargs.pop('vertical_arrow',
                                         constants.DEFAULT_LANG_NAVIGATION.get('vertical_arrow'))
        self.vertical_counter = kwargs.pop('vertical_counter',
                                           constants.DEFAULT_LANG_NAVIGATION.get('vertical_counter'))
        self.vertical_label = kwargs.pop('vertical_label',
                                         constants.DEFAULT_LANG_NAVIGATION.get('vertical_label'))
        self.vertical_line = kwargs.pop('vertical_line',
                                        constants.DEFAULT_LANG_NAVIGATION.get('vertical_line'))
        self.volume = kwargs.pop('volume',
                                 constants.DEFAULT_LANG_NAVIGATION.get('volume'))
        self.x_axis_unit = kwargs.pop('x_axis_unit',
                                      constants.DEFAULT_LANG_NAVIGATION.get('x_axis_unit'))

    @property
    def add_button(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('add_button')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._add_button

    @add_button.setter
    def add_button(self, value):
        if value == '':
            self._add_button = ''
        else:
            self._add_button = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('add_button')

    @property
    def algorithm(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('algorithm')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        if value == '':
            self._algorithm = ''
        else:
            self._algorithm = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('algorithm')

    @property
    def arrow_infinity_line(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('arrow_infinity_line')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._arrow_infinity_line

    @arrow_infinity_line.setter
    def arrow_infinity_line(self, value):
        if value == '':
            self._arrow_infinity_line = ''
        else:
            self._arrow_infinity_line = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('arrow_infinity_line')

    @property
    def arrow_ray(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('arrow_ray')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._arrow_ray

    @arrow_ray.setter
    def arrow_ray(self, value):
        if value == '':
            self._arrow_ray = ''
        else:
            self._arrow_ray = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('arrow_ray')

    @property
    def arrow_segment(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('arrow_segment')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._arrow_segment

    @arrow_segment.setter
    def arrow_segment(self, value):
        if value == '':
            self._arrow_segment = ''
        else:
            self._arrow_segment = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('arrow_segment')

    @property
    def average(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('average')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._average

    @average.setter
    def average(self, value):
        if value == '':
            self._average = ''
        else:
            self._average = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('average')

    @property
    def background(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('background')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._background

    @background.setter
    def background(self, value):
        if value == '':
            self._background = ''
        else:
            self._background = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('background')

    @property
    def background_color(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('background_color')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if value == '':
            self._background_color = ''
        else:
            self._background_color = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('background_color')

    @property
    def background_colors(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('background_colors')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._background_colors

    @background_colors.setter
    def background_colors(self, value):
        if value == '':
            self._background_colors = ''
        else:
            self._background_colors = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('background_colors')

    @property
    def border_color(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('border_color')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if value == '':
            self._border_color = ''
        else:
            self._border_color = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('border_color')

    @property
    def border_radius(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('border_radius')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        if value == '':
            self._border_radius = ''
        else:
            self._border_radius = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('border_radius')

    @property
    def border_width(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('border_width')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        if value == '':
            self._border_width = ''
        else:
            self._border_width = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('border_width')

    @property
    def bottom_band(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('bottom_band')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._bottom_band

    @bottom_band.setter
    def bottom_band(self, value):
        if value == '':
            self._bottom_band = ''
        else:
            self._bottom_band = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('bottom_band')

    @property
    def circle(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('circle')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._circle

    @circle.setter
    def circle(self, value):
        if value == '':
            self._circle = ''
        else:
            self._circle = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('circle')

    @property
    def clear_filter(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('clear_filter')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._clear_filter

    @clear_filter.setter
    def clear_filter(self, value):
        if value == '':
            self._clear_filter = ''
        else:
            self._clear_filter = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('clear_filter')

    @property
    def color(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('color')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if value == '':
            self._color = ''
        else:
            self._color = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('color')

    @property
    def connector(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('connector')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._connector

    @connector.setter
    def connector(self, value):
        if value == '':
            self._connector = ''
        else:
            self._connector = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('connector')

    @property
    def crooked3(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crooked3')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._crooked3

    @crooked3.setter
    def crooked3(self, value):
        if value == '':
            self._crooked3 = ''
        else:
            self._crooked3 = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('crooked3')

    @property
    def crooked5(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crooked5')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._crooked5

    @crooked5.setter
    def crooked5(self, value):
        if value == '':
            self._crooked5 = ''
        else:
            self._crooked5 = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('crooked5')

    @property
    def crosshairX(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crosshairX')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._crosshairX

    @crosshairX.setter
    def crosshairX(self, value):
        if value == '':
            self._crosshairX = ''
        else:
            self._crosshairX = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('crosshairX')

    @property
    def crosshairY(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('crosshairY')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._crosshairY

    @crosshairY.setter
    def crosshairY(self, value):
        if value == '':
            self._crosshairY = ''
        else:
            self._crosshairY = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('crosshairY')

    @property
    def decimals(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('decimals')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._decimals

    @decimals.setter
    def decimals(self, value):
        if value == '':
            self._decimals = ''
        else:
            self._decimals = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('decimals')

    @property
    def deviation(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('deviation')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._deviation

    @deviation.setter
    def deviation(self, value):
        if value == '':
            self._deviation = ''
        else:
            self._deviation = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('deviation')

    @property
    def edit_button(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('edit_button')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._edit_button

    @edit_button.setter
    def edit_button(self, value):
        if value == '':
            self._edit_button = ''
        else:
            self._edit_button = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('edit_button')

    @property
    def elliott3(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('elliott3')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._elliott3

    @elliott3.setter
    def elliott3(self, value):
        if value == '':
            self._elliott3 = ''
        else:
            self._elliott3 = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('elliott3')

    @property
    def elliott5(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('elliott5')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._elliott5

    @elliott5.setter
    def elliott5(self, value):
        if value == '':
            self._elliott5 = ''
        else:
            self._elliott5 = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('elliott5')

    @property
    def ellipse(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('ellipse')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._ellipse

    @ellipse.setter
    def ellipse(self, value):
        if value == '':
            self._ellipse = ''
        else:
            self._ellipse = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('ellipse')

    @property
    def factor(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('factor')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._factor

    @factor.setter
    def factor(self, value):
        if value == '':
            self._factor = ''
        else:
            self._factor = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('factor')

    @property
    def fast_avg_period(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('fast_avg_period')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._fast_avg_period

    @fast_avg_period.setter
    def fast_avg_period(self, value):
        if value == '':
            self._fast_avg_period = ''
        else:
            self._fast_avg_period = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('fast_avg_period')

    @property
    def fibonacci(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('fibonacci')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._fibonacci

    @fibonacci.setter
    def fibonacci(self, value):
        if value == '':
            self._fibonacci = ''
        else:
            self._fibonacci = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('fibonacci')

    @property
    def fibonacci_time_zones(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('fibonacci_time_zones')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._fibonacci_time_zones

    @fibonacci_time_zones.setter
    def fibonacci_time_zones(self, value):
        if value == '':
            self._fibonacci_time_zones = ''
        else:
            self._fibonacci_time_zones = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('fibonacci_time_zones')

    @property
    def fill(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('fill')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        if value == '':
            self._fill = ''
        else:
            self._fill = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('fill')

    @property
    def flags(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('flags')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._flags

    @flags.setter
    def flags(self, value):
        if value == '':
            self._flags = ''
        else:
            self._flags = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('flags')

    @property
    def font_size(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('font_size')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        if value == '':
            self._font_size = ''
        else:
            self._font_size = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('font_size')

    @property
    def format(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('format')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._format

    @format.setter
    def format(self, value):
        if value == '':
            self._format = ''
        else:
            self._format = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('format')

    @property
    def height(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('height')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._height

    @height.setter
    def height(self, value):
        if value == '':
            self._height = ''
        else:
            self._height = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('height')

    @property
    def high_index(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('high_index')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._high_index

    @high_index.setter
    def high_index(self, value):
        if value == '':
            self._high_index = ''
        else:
            self._high_index = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('high_index')

    @property
    def horizontal_line(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('horizontal_line')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._horizontal_line

    @horizontal_line.setter
    def horizontal_line(self, value):
        if value == '':
            self._horizontal_line = ''
        else:
            self._horizontal_line = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('horizontal_line')

    @property
    def increment(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('increment')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._increment

    @increment.setter
    def increment(self, value):
        if value == '':
            self._increment = ''
        else:
            self._increment = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('increment')

    @property
    def index(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('index')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._index

    @index.setter
    def index(self, value):
        if value == '':
            self._index = ''
        else:
            self._index = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('index')

    @property
    def infinity_line(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('infinity_line')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._infinity_line

    @infinity_line.setter
    def infinity_line(self, value):
        if value == '':
            self._infinity_line = ''
        else:
            self._infinity_line = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('infinity_line')

    @property
    def initial_acceleration_factor(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('initial_acceleration_factor')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._initial_acceleration_factor

    @initial_acceleration_factor.setter
    def initial_acceleration_factor(self, value):
        if value == '':
            self._initial_acceleration_factor = ''
        else:
            self._initial_acceleration_factor = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('initial_acceleration_factor')

    @property
    def inner_background(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('inner_background')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._inner_background

    @inner_background.setter
    def inner_background(self, value):
        if value == '':
            self._inner_background = ''
        else:
            self._inner_background = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('inner_background')

    @property
    def label(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('label')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._label

    @label.setter
    def label(self, value):
        if value == '':
            self._label = ''
        else:
            self._label = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('label')

    @property
    def label_options(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('label_options')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._label_options

    @label_options.setter
    def label_options(self, value):
        if value == '':
            self._label_options = ''
        else:
            self._label_options = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('label_options')

    @property
    def labels(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('labels')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._labels

    @labels.setter
    def labels(self, value):
        if value == '':
            self._labels = ''
        else:
            self._labels = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('labels')

    @property
    def line(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('line')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._line

    @line.setter
    def line(self, value):
        if value == '':
            self._line = ''
        else:
            self._line = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('line')

    @property
    def lines(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('lines')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._lines

    @lines.setter
    def lines(self, value):
        if value == '':
            self._lines = ''
        else:
            self._lines = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('lines')

    @property
    def long_period(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('long_period')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._long_period

    @long_period.setter
    def long_period(self, value):
        if value == '':
            self._long_period = ''
        else:
            self._long_period = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('long_period')

    @property
    def low_index(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('low_index')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._low_index

    @low_index.setter
    def low_index(self, value):
        if value == '':
            self._low_index = ''
        else:
            self._low_index = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('low_index')

    @property
    def max_acceleration_factor(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('max_acceleration_factor')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._max_acceleration_factor

    @max_acceleration_factor.setter
    def max_acceleration_factor(self, value):
        if value == '':
            self._max_acceleration_factor = ''
        else:
            self._max_acceleration_factor = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('max_acceleration_factor')

    @property
    def measure(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._measure

    @measure.setter
    def measure(self, value):
        if value == '':
            self._measure = ''
        else:
            self._measure = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('measure')

    @property
    def measure_x(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure_x')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._measure_x

    @measure_x.setter
    def measure_x(self, value):
        if value == '':
            self._measure_x = ''
        else:
            self._measure_x = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('measure_x')

    @property
    def measure_xy(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure_xy')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._measure_xy

    @measure_xy.setter
    def measure_xy(self, value):
        if value == '':
            self._measure_xy = ''
        else:
            self._measure_xy = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('measure_xy')

    @property
    def measure_y(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('measure_y')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._measure_y

    @measure_y.setter
    def measure_y(self, value):
        if value == '':
            self._measure_y = ''
        else:
            self._measure_y = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('measure_y')

    @property
    def multiplier(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('multiplier')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, value):
        if value == '':
            self._multiplier = ''
        else:
            self._multiplier = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('multiplier')

    @property
    def multiplier_atr(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('multiplier_atr')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._multiplier_atr

    @multiplier_atr.setter
    def multiplier_atr(self, value):
        if value == '':
            self._multiplier_atr = ''
        else:
            self._multiplier_atr = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('multiplier_atr')

    @property
    def name(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('name')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            self._name = ''
        else:
            self._name = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('name')

    @property
    def no_filter_match(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('no_filter_match')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._no_filter_match

    @no_filter_match.setter
    def no_filter_match(self, value):
        if value == '':
            self._no_filter_match = ''
        else:
            self._no_filter_match = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('no_filter_match')

    @property
    def outer_background(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('outer_background')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._outer_background

    @outer_background.setter
    def outer_background(self, value):
        if value == '':
            self._outer_background = ''
        else:
            self._outer_background = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('outer_background')

    @property
    def padding(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('padding')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        if value == '':
            self._padding = ''
        else:
            self._padding = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('padding')

    @property
    def parallel_channel(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('parallel_channel')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._parallel_channel

    @parallel_channel.setter
    def parallel_channel(self, value):
        if value == '':
            self._parallel_channel = ''
        else:
            self._parallel_channel = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('parallel_channel')

    @property
    def period(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('period')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._period

    @period.setter
    def period(self, value):
        if value == '':
            self._period = ''
        else:
            self._period = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('period')

    @property
    def period_atr(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('period_atr')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._period_atr

    @period_atr.setter
    def period_atr(self, value):
        if value == '':
            self._period_atr = ''
        else:
            self._period_atr = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('period_atr')

    @property
    def periods(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('periods')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._periods

    @periods.setter
    def periods(self, value):
        if value == '':
            self._periods = ''
        else:
            self._periods = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('periods')

    @property
    def period_senkou_span_b(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('period_senkou_span_b')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._period_senkou_span_b

    @period_senkou_span_b.setter
    def period_senkou_span_b(self, value):
        if value == '':
            self._period_senkou_span_b = ''
        else:
            self._period_senkou_span_b = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('period_senkou_span_b')

    @property
    def period_tenkan(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('period_tenkan')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._period_tenkan

    @period_tenkan.setter
    def period_tenkan(self, value):
        if value == '':
            self._period_tenkan = ''
        else:
            self._period_tenkan = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('period_tenkan')

    @property
    def pitchfork(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('pitchfork')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._pitchfork

    @pitchfork.setter
    def pitchfork(self, value):
        if value == '':
            self._pitchfork = ''
        else:
            self._pitchfork = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('pitchfork')

    @property
    def ranges(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('ranges')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._ranges

    @ranges.setter
    def ranges(self, value):
        if value == '':
            self._ranges = ''
        else:
            self._ranges = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('ranges')

    @property
    def ray(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('ray')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._ray

    @ray.setter
    def ray(self, value):
        if value == '':
            self._ray = ''
        else:
            self._ray = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('ray')

    @property
    def rectangle(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('rectangle')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, value):
        if value == '':
            self._rectangle = ''
        else:
            self._rectangle = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('rectangle')

    @property
    def remove_button(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('remove_button')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._remove_button

    @remove_button.setter
    def remove_button(self, value):
        if value == '':
            self._remove_button = ''
        else:
            self._remove_button = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('remove_button')

    @property
    def save_button(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('save_button')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._save_button

    @save_button.setter
    def save_button(self, value):
        if value == '':
            self._save_button = ''
        else:
            self._save_button = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('save_button')

    @property
    def search_indicators(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('search_indicators')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._search_indicators

    @search_indicators.setter
    def search_indicators(self, value):
        if value == '':
            self._search_indicators = ''
        else:
            self._search_indicators = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('search_indicators')

    @property
    def segment(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('segment')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._segment

    @segment.setter
    def segment(self, value):
        if value == '':
            self._segment = ''
        else:
            self._segment = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('segment')

    @property
    def series(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('series')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._series

    @series.setter
    def series(self, value):
        if value == '':
            self._series = ''
        else:
            self._series = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('series')

    @property
    def shape_options(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('shape_options')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._shape_options

    @shape_options.setter
    def shape_options(self, value):
        if value == '':
            self._shape_options = ''
        else:
            self._shape_options = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('shape_options')

    @property
    def shapes(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('shapes')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._shapes

    @shapes.setter
    def shapes(self, value):
        if value == '':
            self._shapes = ''
        else:
            self._shapes = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('shapes')

    @property
    def short_period(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('short_period')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._short_period

    @short_period.setter
    def short_period(self, value):
        if value == '':
            self._short_period = ''
        else:
            self._short_period = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('short_period')

    @property
    def signal_period(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('signal_period')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._signal_period

    @signal_period.setter
    def signal_period(self, value):
        if value == '':
            self._signal_period = ''
        else:
            self._signal_period = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('signal_period')

    @property
    def simple_shapes(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('simple_shapes')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._simple_shapes

    @simple_shapes.setter
    def simple_shapes(self, value):
        if value == '':
            self._simple_shapes = ''
        else:
            self._simple_shapes = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('simple_shapes')

    @property
    def slow_avg_period(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('slow_avg_period')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._slow_avg_period

    @slow_avg_period.setter
    def slow_avg_period(self, value):
        if value == '':
            self._slow_avg_period = ''
        else:
            self._slow_avg_period = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('slow_avg_period')

    @property
    def standard_deviation(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('standard_deviation')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._standard_deviation

    @standard_deviation.setter
    def standard_deviation(self, value):
        if value == '':
            self._standard_deviation = ''
        else:
            self._standard_deviation = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('standard_deviation')

    @property
    def stroke(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('stroke')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        if value == '':
            self._stroke = ''
        else:
            self._stroke = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('stroke')

    @property
    def stroke_width(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('stroke_width')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        if value == '':
            self._stroke_width = ''
        else:
            self._stroke_width = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('stroke_width')

    @property
    def style(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('style')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._style

    @style.setter
    def style(self, value):
        if value == '':
            self._style = ''
        else:
            self._style = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('style')

    @property
    def time_cycles(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('time_cycles')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._time_cycles

    @time_cycles.setter
    def time_cycles(self, value):
        if value == '':
            self._time_cycles = ''
        else:
            self._time_cycles = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('time_cycles')

    @property
    def title(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('title')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._title

    @title.setter
    def title(self, value):
        if value == '':
            self._title = ''
        else:
            self._title = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('title')

    @property
    def top_band(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('top_band')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._top_band

    @top_band.setter
    def top_band(self, value):
        if value == '':
            self._top_band = ''
        else:
            self._top_band = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('top_band')

    @property
    def tunnel(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('tunnel')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._tunnel

    @tunnel.setter
    def tunnel(self, value):
        if value == '':
            self._tunnel = ''
        else:
            self._tunnel = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('tunnel')

    @property
    def type_options(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('type_options')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._type_options

    @type_options.setter
    def type_options(self, value):
        if value == '':
            self._type_options = ''
        else:
            self._type_options = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('type_options')

    @property
    def vertical_arrow(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_arrow')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._vertical_arrow

    @vertical_arrow.setter
    def vertical_arrow(self, value):
        if value == '':
            self._vertical_arrow = ''
        else:
            self._vertical_arrow = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('vertical_arrow')

    @property
    def vertical_counter(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_counter')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._vertical_counter

    @vertical_counter.setter
    def vertical_counter(self, value):
        if value == '':
            self._vertical_counter = ''
        else:
            self._vertical_counter = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('vertical_counter')

    @property
    def vertical_label(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_label')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._vertical_label

    @vertical_label.setter
    def vertical_label(self, value):
        if value == '':
            self._vertical_label = ''
        else:
            self._vertical_label = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('vertical_label')

    @property
    def vertical_line(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('vertical_line')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._vertical_line

    @vertical_line.setter
    def vertical_line(self, value):
        if value == '':
            self._vertical_line = ''
        else:
            self._vertical_line = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('vertical_line')

    @property
    def volume(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('volume')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._volume

    @volume.setter
    def volume(self, value):
        if value == '':
            self._volume = ''
        else:
            self._volume = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('volume')

    @property
    def x_axis_unit(self) -> str:
        f"""Defaults to ``'{constants.DEFAULT_LANG_NAVIGATION.get('x_axis_unit')}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._x_axis_unit

    @x_axis_unit.setter
    def x_axis_unit(self, value):
        if value == '':
            self._x_axis_unit = ''
        else:
            self._x_axis_unit = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_NAVIGATION.get('x_axis_unit')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'add_button': as_dict.pop('addButton',
                                      constants.DEFAULT_LANG_NAVIGATION.get('add_button')),
            'algorithm': as_dict.pop('algorithm',
                                     constants.DEFAULT_LANG_NAVIGATION.get('algorithm')),
            'arrow_infinity_line': as_dict.pop('arrowInfinityLine',
                                               constants.DEFAULT_LANG_NAVIGATION.get('arrow_infinity_line')),
            'arrow_ray': as_dict.pop('arrowRay',
                                     constants.DEFAULT_LANG_NAVIGATION.get('arrow_ray')),
            'arrow_segment': as_dict.pop('arrowSegment',
                                         constants.DEFAULT_LANG_NAVIGATION.get('arrow_segment')),
            'average': as_dict.pop('average',
                                   constants.DEFAULT_LANG_NAVIGATION.get('average')),
            'background': as_dict.pop('background',
                                      constants.DEFAULT_LANG_NAVIGATION.get('background')),
            'background_color': as_dict.pop('backgroundColor',
                                            constants.DEFAULT_LANG_NAVIGATION.get('background_color')),
            'background_colors': as_dict.pop('backgroundColors',
                                            constants.DEFAULT_LANG_NAVIGATION.get('background_colors')),
            'border_color': as_dict.pop('borderColor',
                                        constants.DEFAULT_LANG_NAVIGATION.get('border_color')),
            'border_radius': as_dict.pop('borderRadius',
                                         constants.DEFAULT_LANG_NAVIGATION.get('border_radius')),
            'border_width': as_dict.pop('borderWidth',
                                        constants.DEFAULT_LANG_NAVIGATION.get('border_width')),
            'bottom_band': as_dict.pop('bottomBand',
                                       constants.DEFAULT_LANG_NAVIGATION.get('bottom_band')),
            'circle': as_dict.pop('circle',
                                  constants.DEFAULT_LANG_NAVIGATION.get('circle')),
            'clear_filter': as_dict.pop('clearFilter',
                                        constants.DEFAULT_LANG_NAVIGATION.get('clear_filter')),
            'color': as_dict.pop('color',
                                 constants.DEFAULT_LANG_NAVIGATION.get('color')),
            'connector': as_dict.pop('connector',
                                     constants.DEFAULT_LANG_NAVIGATION.get('connector')),
            'crooked3': as_dict.pop('crooked3',
                                    constants.DEFAULT_LANG_NAVIGATION.get('crooked3')),
            'crooked5': as_dict.pop('crooked5',
                                    constants.DEFAULT_LANG_NAVIGATION.get('crooked5')),
            'crosshairX': as_dict.pop('crosshairX',
                                      constants.DEFAULT_LANG_NAVIGATION.get('crosshairX')),
            'crosshairY': as_dict.pop('crosshairY',
                                      constants.DEFAULT_LANG_NAVIGATION.get('crosshairY')),
            'decimals': as_dict.pop('decimals',
                                    constants.DEFAULT_LANG_NAVIGATION.get('decimals')),
            'deviation': as_dict.pop('deviation',
                                     constants.DEFAULT_LANG_NAVIGATION.get('deviation')),
            'edit_button': as_dict.pop('editButton',
                                       constants.DEFAULT_LANG_NAVIGATION.get('edit_button')),
            'elliott3': as_dict.pop('elliott3',
                                    constants.DEFAULT_LANG_NAVIGATION.get('elliott3')),
            'elliott5': as_dict.pop('elliott5',
                                    constants.DEFAULT_LANG_NAVIGATION.get('elliott5')),
            'ellipse': as_dict.pop('ellipse',
                                   constants.DEFAULT_LANG_NAVIGATION.get('ellipse')),
            'factor': as_dict.pop('factor',
                                  constants.DEFAULT_LANG_NAVIGATION.get('factor')),
            'fast_avg_period': as_dict.pop('fastAvgPeriod',
                                           constants.DEFAULT_LANG_NAVIGATION.get('fast_avg_period')),
            'fibonacci': as_dict.pop('fibonacci',
                                     constants.DEFAULT_LANG_NAVIGATION.get('fibonacci')),
            'fibonacci_time_zones': as_dict.pop('fibonacciTimeZones',
                                                constants.DEFAULT_LANG_NAVIGATION.get('fibonacci_time_zones')),
            'fill': as_dict.pop('fill',
                                constants.DEFAULT_LANG_NAVIGATION.get('fill')),
            'flags': as_dict.pop('flags',
                                 constants.DEFAULT_LANG_NAVIGATION.get('flags')),
            'font_size': as_dict.pop('fontSize',
                                     constants.DEFAULT_LANG_NAVIGATION.get('font_size')),
            'format': as_dict.pop('format',
                                  constants.DEFAULT_LANG_NAVIGATION.get('format')),
            'height': as_dict.pop('height',
                                  constants.DEFAULT_LANG_NAVIGATION.get('height')),
            'high_index': as_dict.pop('highIndex',
                                      constants.DEFAULT_LANG_NAVIGATION.get('high_index')),
            'horizontal_line': as_dict.pop('horizontalLine',
                                           constants.DEFAULT_LANG_NAVIGATION.get('horizontal_line')),
            'increment': as_dict.pop('increment',
                                     constants.DEFAULT_LANG_NAVIGATION.get('increment')),
            'index': as_dict.pop('index',
                                 constants.DEFAULT_LANG_NAVIGATION.get('index')),
            'infinity_line': as_dict.pop('infinityLine',
                                         constants.DEFAULT_LANG_NAVIGATION.get('infinity_line')),
            'initial_acceleration_factor': as_dict.pop('initialAccelerationFactor',
                                                       constants.DEFAULT_LANG_NAVIGATION.get('initial_acceleration_factor')),
            'inner_background': as_dict.pop('innerBackground',
                                            constants.DEFAULT_LANG_NAVIGATION.get('inner_background')),
            'label': as_dict.pop('label',
                                 constants.DEFAULT_LANG_NAVIGATION.get('label')),
            'label_options': as_dict.pop('labelOptions',
                                         constants.DEFAULT_LANG_NAVIGATION.get('label_options')),
            'labels': as_dict.pop('labels',
                                  constants.DEFAULT_LANG_NAVIGATION.get('labels')),
            'line': as_dict.pop('line',
                                constants.DEFAULT_LANG_NAVIGATION.get('line')),
            'lines': as_dict.pop('lines',
                                 constants.DEFAULT_LANG_NAVIGATION.get('lines')),
            'long_period': as_dict.pop('longPeriod',
                                       constants.DEFAULT_LANG_NAVIGATION.get('long_period')),
            'low_index': as_dict.pop('lowIndex',
                                     constants.DEFAULT_LANG_NAVIGATION.get('low_index')),
            'max_acceleration_factor': as_dict.pop('maxAccelerationFactor',
                                                   constants.DEFAULT_LANG_NAVIGATION.get('max_acceleration_factor')),
            'measure': as_dict.pop('measure',
                                   constants.DEFAULT_LANG_NAVIGATION.get('measure')),
            'measure_x': as_dict.pop('measureX',
                                     constants.DEFAULT_LANG_NAVIGATION.get('measure_x')),
            'measure_xy': as_dict.pop('measureXY',
                                      constants.DEFAULT_LANG_NAVIGATION.get('measure_xy')),
            'measure_y': as_dict.pop('measureY',
                                     constants.DEFAULT_LANG_NAVIGATION.get('measure_y')),
            'multiplier': as_dict.pop('multiplier',
                                      constants.DEFAULT_LANG_NAVIGATION.get('multiplier')),
            'multiplier_atr': as_dict.pop('multiplierATR',
                                          constants.DEFAULT_LANG_NAVIGATION.get('multiplier_atr')),
            'name': as_dict.pop('name',
                                constants.DEFAULT_LANG_NAVIGATION.get('name')),
            'no_filter_match': as_dict.pop('noFilterMatch',
                                           constants.DEFAULT_LANG_NAVIGATION.get('no_filter_match')),
            'outer_background': as_dict.pop('outerBackground',
                                            constants.DEFAULT_LANG_NAVIGATION.get('outer_background')),
            'padding': as_dict.pop('padding',
                                   constants.DEFAULT_LANG_NAVIGATION.get('padding')),
            'parallel_channel': as_dict.pop('parallelChannel',
                                            constants.DEFAULT_LANG_NAVIGATION.get('parallel_channel')),
            'period': as_dict.pop('period',
                                  constants.DEFAULT_LANG_NAVIGATION.get('period')),
            'period_atr': as_dict.pop('periodATR',
                                      constants.DEFAULT_LANG_NAVIGATION.get('period_atr')),
            'periods': as_dict.pop('periods',
                                   constants.DEFAULT_LANG_NAVIGATION.get('periods')),
            'period_senkou_span_b': as_dict.pop('periodSenkouSpanB',
                                                constants.DEFAULT_LANG_NAVIGATION.get('period_senkou_span_b')),
            'period_tenkan': as_dict.pop('periodTenkan',
                                         constants.DEFAULT_LANG_NAVIGATION.get('period_tenkan')),
            'pitchfork': as_dict.pop('pitchfork',
                                     constants.DEFAULT_LANG_NAVIGATION.get('pitchfork')),
            'ranges': as_dict.pop('ranges',
                                  constants.DEFAULT_LANG_NAVIGATION.get('ranges')),
            'ray': as_dict.pop('ray',
                               constants.DEFAULT_LANG_NAVIGATION.get('ray')),
            'rectangle': as_dict.pop('rectangle',
                                     constants.DEFAULT_LANG_NAVIGATION.get('rectangle')),
            'remove_button': as_dict.pop('removeButton',
                                         constants.DEFAULT_LANG_NAVIGATION.get('remove_button')),
            'save_button': as_dict.pop('saveButton',
                                       constants.DEFAULT_LANG_NAVIGATION.get('save_button')),
            'search_indicators': as_dict.pop('searchIndicators',
                                             constants.DEFAULT_LANG_NAVIGATION.get('search_indicators')),
            'segment': as_dict.pop('segment',
                                   constants.DEFAULT_LANG_NAVIGATION.get('segment')),
            'series': as_dict.pop('series',
                                  constants.DEFAULT_LANG_NAVIGATION.get('series')),
            'shape_options': as_dict.pop('shapeOptions',
                                         constants.DEFAULT_LANG_NAVIGATION.get('shape_options')),
            'shapes': as_dict.pop('shapes',
                                  constants.DEFAULT_LANG_NAVIGATION.get('shapes')),
            'short_period': as_dict.pop('shortPeriod',
                                        constants.DEFAULT_LANG_NAVIGATION.get('short_period')),
            'signal_period': as_dict.pop('signalPeriod',
                                         constants.DEFAULT_LANG_NAVIGATION.get('signal_period')),
            'simple_shapes': as_dict.pop('simpleShapes',
                                         constants.DEFAULT_LANG_NAVIGATION.get('simple_shapes')),
            'slow_avg_period': as_dict.pop('slowAvgPeriod',
                                           constants.DEFAULT_LANG_NAVIGATION.get('slow_avg_period')),
            'standard_deviation': as_dict.pop('standardDeviation',
                                              constants.DEFAULT_LANG_NAVIGATION.get('standard_deviation')),
            'stroke': as_dict.pop('stroke',
                                  constants.DEFAULT_LANG_NAVIGATION.get('stroke')),
            'stroke_width': as_dict.pop('strokeWidth',
                                        constants.DEFAULT_LANG_NAVIGATION.get('stroke_width')),
            'style': as_dict.pop('style',
                                 constants.DEFAULT_LANG_NAVIGATION.get('style')),
            'time_cycles': as_dict.pop('timeCycles',
                                       constants.DEFAULT_LANG_NAVIGATION.get('time_cycles')),
            'title': as_dict.pop('title',
                                 constants.DEFAULT_LANG_NAVIGATION.get('title')),
            'top_band': as_dict.pop('topBand',
                                    constants.DEFAULT_LANG_NAVIGATION.get('top_band')),
            'tunnel': as_dict.pop('tunnel',
                                  constants.DEFAULT_LANG_NAVIGATION.get('tunnel')),
            'type_options': as_dict.pop('typeOptions',
                                        constants.DEFAULT_LANG_NAVIGATION.get('type_options')),
            'vertical_arrow': as_dict.pop('verticalArrow',
                                          constants.DEFAULT_LANG_NAVIGATION.get('vertical_arrow')),
            'vertical_counter': as_dict.pop('verticalCounter',
                                            constants.DEFAULT_LANG_NAVIGATION.get('vertical_counter')),
            'vertical_label': as_dict.pop('verticalLabel',
                                          constants.DEFAULT_LANG_NAVIGATION.get('vertical_label')),
            'vertical_line': as_dict.pop('verticalLine',
                                         constants.DEFAULT_LANG_NAVIGATION.get('vertical_line')),
            'volume': as_dict.pop('volume',
                                  constants.DEFAULT_LANG_NAVIGATION.get('volume')),
            'x_axis_unit': as_dict.pop('xAxisUnit',
                                       constants.DEFAULT_LANG_NAVIGATION.get('x_axis_unit'))
        }

        return cls(**kwargs)

    def to_dict(self):
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

        return self.trim_dict(untrimmed)


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

    def to_dict(self):
        return self.trim_dict({
            'popup': self.popup
        })
