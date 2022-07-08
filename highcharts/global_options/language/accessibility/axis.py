from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class AxisLanguageOptions(HighchartsMeta):
    """Axis description strings."""

    def __init__(self, **kwargs):
        self._range_categories = None
        self._range_from_to = None
        self._time_range_days = None
        self._time_range_hours = None
        self._time_range_minutes = None
        self._time_range_seconds = None
        self._x_axis_description_plural = None
        self._x_axis_description_singular = None
        self._y_axis_description_plural = None
        self._y_axis_description_singular = None

        self.range_categories = kwargs.pop('range_categories',
                                           constants.DEFAULT_LANG_ACS_AXIS_RANGE_CATEGORIES)
        self.range_from_to = kwargs.pop('range_from_to',
                                        constants.DEFAULT_LANG_ACS_AXIS_RANGE_FROM_TO)
        self.time_range_days = kwargs.pop('time_range_days',
                                          constants.DEFAULT_LANG_ACS_TIME_RANGE_DAYS)
        self.time_range_hours = kwargs.pop('time_range_hours',
                                           constants.DEFAULT_LANG_ACS_TIME_RANGE_HOURS)
        self.time_range_minutes = kwargs.pop('time_range_minutes',
                                             constants.DEFAULT_LANG_ACS_TIME_RANGE_MINUTES)
        self.time_range_seconds = kwargs.pop('time_range_seconds',
                                             constants.DEFAULT_LANG_ACS_TIME_RANGE_SECONDS)
        self.x_axis_description_plural = kwargs.pop('x_axis_description_plural',
                                                    constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_PLURAL)
        self.x_axis_description_singular = kwargs.pop('x_axis_description_singular',
                                                      constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_SINGULAR)
        self.y_axis_description_plural = kwargs.pop('y_axis_description_plural',
                                                    constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_PLURAL)
        self.y_axis_description_singular = kwargs.pop('y_axis_description_singular',
                                                      constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_SINGULAR)

    @property
    def range_categories(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_AXIS_RANGE_CATEGORIES}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._range_categories

    @range_categories.setter
    def range_categories(self, value):
        if value == '':
            self._range_categories = ''
        else:
            self._range_categories = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_AXIS_RANGE_CATEGORIES

    @property
    def range_from_to(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_AXIS_RANGE_FROM_TO}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._range_from_to

    @range_from_to.setter
    def range_from_to(self, value):
        if value == '':
            self._range_from_to = ''
        else:
            self._range_from_to = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_AXIS_RANGE_FROM_TO

    @property
    def time_range_days(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_DAYS}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._time_range_days

    @time_range_days.setter
    def time_range_days(self, value):
        if value == '':
            self._time_range_days = ''
        else:
            self._time_range_days = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_DAYS

    @property
    def time_range_hours(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_HOURS}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._time_range_hours

    @time_range_hours.setter
    def time_range_hours(self, value):
        if value == '':
            self._time_range_hours = ''
        else:
            self._time_range_hours = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_HOURS

    @property
    def time_range_minutes(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_MINUTES}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._time_range_minutes

    @time_range_minutes.setter
    def time_range_minutes(self, value):
        if value == '':
            self._time_range_minutes = ''
        else:
            self._time_range_minutes = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_MINUTES

    @property
    def time_range_seconds(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_SECONDS}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._time_range_seconds

    @time_range_seconds.setter
    def time_range_seconds(self, value):
        if value == '':
            self._time_range_seconds = ''
        else:
            self._time_range_seconds = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_AXIS_TIME_RANGE_SECONDS

    @property
    def x_axis_description_plural(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_PLURAL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._x_axis_description_plural

    @x_axis_description_plural.setter
    def x_axis_description_plural(self, value):
        if value == '':
            self._x_axis_description_plural = ''
        else:
            self._x_axis_description_plural = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_PLURAL

    @property
    def x_axis_description_singular(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_SINGULAR}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._x_axis_description_singular

    @x_axis_description_singular.setter
    def x_axis_description_singular(self, value):
        if value == '':
            self._x_axis_description_singular = ''
        else:
            self._x_axis_description_singular = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_SINGULAR

    @property
    def y_axis_description_plural(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_PLURAL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._y_axis_description_plural

    @y_axis_description_plural.setter
    def y_axis_description_plural(self, value):
        if value == '':
            self._y_axis_description_plural = ''
        else:
            self._y_axis_description_plural = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_PLURAL

    @property
    def y_axis_description_singular(self) -> str:
        """Defaults to ``'{constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_SINGULAR}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._y_axis_description_singular

    @y_axis_description_singular.setter
    def y_axis_description_singular(self, value):
        if value == '':
            self._y_axis_description_singular = ''
        else:
            self._y_axis_description_singular = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_SINGULAR

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'range_categories': as_dict.pop('rangeCategories',
                                            constants.DEFAULT_LANG_ACS_AXIS_RANGE_CATEGORIES),
            'range_from_to': as_dict.pop('rangeFromTo',
                                         constants.DEFAULT_LANG_ACS_AXIS_RANGE_FROM_TO),
            'time_range_days': as_dict.pop('timeRangeDays',
                                           constants.DEFAULT_LANG_ACS_TIME_RANGE_DAYS),
            'time_range_hours': as_dict.pop('timeRangeHours',
                                            constants.DEFAULT_LANG_ACS_TIME_RANGE_HOURS),
            'time_range_minutes': as_dict.pop('timeRangeMinutes',
                                              constants.DEFAULT_LANG_ACS_TIME_RANGE_MINUTES),
            'time_range_seconds': as_dict.pop('timeRangeSeconds',
                                              constants.DEFAULT_LANG_ACS_TIME_RANGE_SECONDS),
            'x_axis_description_plural': as_dict.pop('xAxisDescriptionPlural',
                                                     constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_PLURAL),
            'x_axis_description_singular': as_dict.pop('xAxisDescriptionSingular',
                                                       constants.DEFAULT_LANG_ACS_X_AXIS_DESCRIPTION_SINGULAR),
            'y_axis_description_plural': as_dict.pop('yAxisDescriptionPlural',
                                                     constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_PLURAL),
            'y_axis_description_singular': as_dict.pop('yAxisDescriptionSingular',
                                                       constants.DEFAULT_LANG_ACS_Y_AXIS_DESCRIPTION_SINGULAR)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'rangeCategories': self.range_categories,
            'rangeFromTo': self.range_from_to,
            'timeRangeDays': self.time_range_days,
            'timeRangeHours': self.time_range_hours,
            'timeRangeMinutes': self.time_range_minutes,
            'timeRangeSeconds': self.time_range_seconds,
            'xAxisDescriptionPlural': self.x_axis_description_plural,
            'xAxisDescriptionSingular': self.x_axis_description_singular,
            'yAxisDescriptionPlural': self.y_axis_description_plural,
            'yAxisDescriptionSingular': self.y_axis_description_singular
        }

        return self.trim_dict(untrimmed)
