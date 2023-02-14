from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class DateTimeLabelFormats(HighchartsMeta):
    """For series on datetime axes, the date format in the tooltip's header will by default be
    guessed based on the closest data points. This class gives the default string
    representations used for each unit.
    """

    def __init__(self, **kwargs):
        self._day = None
        self._hour = None
        self._millisecond = None
        self._minute = None
        self._month = None
        self._second = None
        self._week = None
        self._year = None

        self.day = kwargs.get('day', None)
        self.hour = kwargs.get('hour', None)
        self.millisecond = kwargs.get('millisecond', None)
        self.minute = kwargs.get('minute', None)
        self.month = kwargs.get('month', None)
        self.second = kwargs.get('second', None)
        self.week = kwargs.get('week', None)
        self.year = kwargs.get('year', None)

    @property
    def day(self) -> Optional[str]:
        """Label format to apply to days. Defaults to
        ``'%A, %b %e, %Y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._day

    @day.setter
    def day(self, value):
        self._day = validators.string(value, allow_empty = True)

    @property
    def hour(self) -> Optional[str]:
        """Label format to apply to hours. Defaults to
        ``'%A, %b %e, %H:%M'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = validators.string(value, allow_empty = True)

    @property
    def millisecond(self) -> Optional[str]:
        """Label format to apply to milliseconds. Defaults to
        ``'%A, %b %e, %H:%M:%S.%L'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._millisecond

    @millisecond.setter
    def millisecond(self, value):
        self._millisecond = validators.string(value, allow_empty = True)

    @property
    def minute(self) -> Optional[str]:
        """Label format to apply to minutes. Defaults to
        ``'%A, %b %e, %H:%M'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute = validators.string(value, allow_empty = True)

    @property
    def month(self) -> Optional[str]:
        """Label format to apply to months. Defaults to
        ``'%B %Y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._month

    @month.setter
    def month(self, value):
        self._month = validators.string(value, allow_empty = True)

    @property
    def second(self) -> Optional[str]:
        """Label format to apply to seconds. Defaults to
        ``'%A, %b %e, %H:%M:%S'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._second

    @second.setter
    def second(self, value):
        self._second = validators.string(value, allow_empty = True)

    @property
    def week(self) -> Optional[str]:
        """Label format to apply to weeks. Defaults to
        ``'Week from %A, %b %e, %Y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._week

    @week.setter
    def week(self, value):
        self._week = validators.string(value, allow_empty = True)

    @property
    def year(self) -> Optional[str]:
        """Label format to apply to years. Defaults to
        ``'%Y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._year

    @year.setter
    def year(self, value):
        self._year = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'day': as_dict.get('day', None),
            'hour': as_dict.get('hour', None),
            'millisecond': as_dict.get('millisecond', None),
            'minute': as_dict.get('minute', None),
            'month': as_dict.get('month', None),
            'second': as_dict.get('second', None),
            'week': as_dict.get('week', None),
            'year': as_dict.get('year', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'day': self.day,
            'hour': self.hour,
            'millisecond': self.millisecond,
            'minute': self.minute,
            'month': self.month,
            'second': self.second,
            'week': self.week,
            'year': self.year
        }

        return untrimmed
