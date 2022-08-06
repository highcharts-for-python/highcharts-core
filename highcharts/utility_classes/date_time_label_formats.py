from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


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

        self.day = kwargs.pop('day', None)
        self.hour = kwargs.pop('hour', None)
        self.millisecond = kwargs.pop('millisecond', None)
        self.minute = kwargs.pop('minute', None)
        self.month = kwargs.pop('month', None)
        self.second = kwargs.pop('second', None)
        self.week = kwargs.pop('week', None)
        self.year = kwargs.pop('year', None)

    @property
    def day(self) -> Optional[str]:
        f"""Label format to apply to days. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('day')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._day

    @day.setter
    def day(self, value):
        self._day = validators.string(value, allow_empty = True)

    @property
    def hour(self) -> Optional[str]:
        f"""Label format to apply to hours. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('hour')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = validators.string(value, allow_empty = True)

    @property
    def millisecond(self) -> Optional[str]:
        f"""Label format to apply to milliseconds. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('millisecond')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._millisecond

    @millisecond.setter
    def millisecond(self, value):
        self._millisecond = validators.string(value, allow_empty = True)

    @property
    def minute(self) -> Optional[str]:
        f"""Label format to apply to minutes. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('minute')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute = validators.string(value, allow_empty = True)

    @property
    def month(self) -> Optional[str]:
        f"""Label format to apply to months. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('month')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._month

    @month.setter
    def month(self, value):
        self._month = validators.string(value, allow_empty = True)

    @property
    def second(self) -> Optional[str]:
        f"""Label format to apply to seconds. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('second')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._second

    @second.setter
    def second(self, value):
        self._second = validators.string(value, allow_empty = True)

    @property
    def week(self) -> Optional[str]:
        f"""Label format to apply to weeks. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('week')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._week

    @week.setter
    def week(self, value):
        self._week = validators.string(value, allow_empty = True)

    @property
    def year(self) -> Optional[str]:
        f"""Label format to apply to years. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('year')}``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._year

    @year.setter
    def year(self, value):
        self._year = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'day': as_dict.pop('day', None),
            'hour': as_dict.pop('hour', None),
            'millisecond': as_dict.pop('millisecond', None),
            'minute': as_dict.pop('minute', None),
            'month': as_dict.pop('month', None),
            'second': as_dict.pop('second', None),
            'week': as_dict.pop('week', None),
            'year': as_dict.pop('year', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
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
