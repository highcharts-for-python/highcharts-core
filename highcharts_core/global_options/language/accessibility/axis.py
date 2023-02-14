from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


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

        self.range_categories = kwargs.get('range_categories', None)
        self.range_from_to = kwargs.get('range_from_to', None)
        self.time_range_days = kwargs.get('time_range_days', None)
        self.time_range_hours = kwargs.get('time_range_hours', None)
        self.time_range_minutes = kwargs.get('time_range_minutes', None)
        self.time_range_seconds = kwargs.get('time_range_seconds', None)
        self.x_axis_description_plural = kwargs.get('x_axis_description_plural', None)
        self.x_axis_description_singular = kwargs.get('x_axis_description_singular', None)
        self.y_axis_description_plural = kwargs.get('y_axis_description_plural', None)
        self.y_axis_description_singular = kwargs.get('y_axis_description_singular', None)

    @property
    def range_categories(self) -> Optional[str]:
        """Defaults to ``'Data range: {numCategories} categories.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._range_categories

    @range_categories.setter
    def range_categories(self, value):
        self._range_categories = validators.string(value, allow_empty = True)

    @property
    def range_from_to(self) -> Optional[str]:
        """Defaults to ``'Data ranges from {rangeFrom} to {rangeTo}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._range_from_to

    @range_from_to.setter
    def range_from_to(self, value):
        self._range_from_to = validators.string(value, allow_empty = True)

    @property
    def time_range_days(self) -> Optional[str]:
        """Defaults to ``'Data range: {range} days.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._time_range_days

    @time_range_days.setter
    def time_range_days(self, value):
        self._time_range_days = validators.string(value, allow_empty = True)

    @property
    def time_range_hours(self) -> Optional[str]:
        """Defaults to ``'Data range: {range} hours.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._time_range_hours

    @time_range_hours.setter
    def time_range_hours(self, value):
        self._time_range_hours = validators.string(value, allow_empty = True)

    @property
    def time_range_minutes(self) -> Optional[str]:
        """Defaults to ``'Data range: {range} minutes.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._time_range_minutes

    @time_range_minutes.setter
    def time_range_minutes(self, value):
        self._time_range_minutes = validators.string(value, allow_empty = True)

    @property
    def time_range_seconds(self) -> Optional[str]:
        """Defaults to ``'Data range: {range} seconds.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._time_range_seconds

    @time_range_seconds.setter
    def time_range_seconds(self, value):
        self._time_range_seconds = validators.string(value, allow_empty = True)

    @property
    def x_axis_description_plural(self) -> Optional[str]:
        """Defaults to ``'The chart has {numAxes} X axes displaying {#each(names, -1), }and {names[-1]}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._x_axis_description_plural

    @x_axis_description_plural.setter
    def x_axis_description_plural(self, value):
        self._x_axis_description_plural = validators.string(value, allow_empty = True)

    @property
    def x_axis_description_singular(self) -> Optional[str]:
        """Defaults to ``'The chart has 1 X axis displaying {names[0]}. {ranges[0]}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._x_axis_description_singular

    @x_axis_description_singular.setter
    def x_axis_description_singular(self, value):
        self._x_axis_description_singular = validators.string(value, allow_empty = True)

    @property
    def y_axis_description_plural(self) -> Optional[str]:
        """Defaults to ``'The chart has {numAxes} Y axes displaying {#each(names, -1), }and {names[-1]}.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._y_axis_description_plural

    @y_axis_description_plural.setter
    def y_axis_description_plural(self, value):
        self._y_axis_description_plural = validators.string(value, allow_empty = True)

    @property
    def y_axis_description_singular(self) -> Optional[str]:
        """Defaults to ``'The chart has 1 Y axis displaying {names[0]}. {ranges[0]}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._y_axis_description_singular

    @y_axis_description_singular.setter
    def y_axis_description_singular(self, value):
        self._y_axis_description_singular = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'range_categories': as_dict.get('rangeCategories', None),
            'range_from_to': as_dict.get('rangeFromTo', None),
            'time_range_days': as_dict.get('timeRangeDays', None),
            'time_range_hours': as_dict.get('timeRangeHours', None),
            'time_range_minutes': as_dict.get('timeRangeMinutes', None),
            'time_range_seconds': as_dict.get('timeRangeSeconds', None),
            'x_axis_description_plural': as_dict.get('xAxisDescriptionPlural', None),
            'x_axis_description_singular': as_dict.get('xAxisDescriptionSingular', None),
            'y_axis_description_plural': as_dict.get('yAxisDescriptionPlural', None),
            'y_axis_description_singular': as_dict.get('yAxisDescriptionSingular', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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

        return untrimmed
