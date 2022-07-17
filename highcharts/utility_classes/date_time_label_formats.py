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

        self.day = kwargs.pop('day',
                              constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('day'))
        self.hour = kwargs.pop('hour',
                               constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('hour'))
        self.millisecond = kwargs.pop('millisecond',
                                      constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('millisecond'))
        self.minute = kwargs.pop('minute',
                                 constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('minute'))
        self.month = kwargs.pop('month',
                                constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('month'))
        self.second = kwargs.pop('second',
                                 constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('second'))
        self.week = kwargs.pop('week',
                               constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('week'))
        self.year = kwargs.pop('year',
                               constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('year'))

    @property
    def day(self) -> str:
        f"""Label format to apply to days. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('day')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._day

    @day.setter
    def day(self, value):
        self._day = validators.string(value)

    @property
    def hour(self) -> str:
        f"""Label format to apply to hours. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('hour')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = validators.string(value)

    @property
    def millisecond(self) -> str:
        f"""Label format to apply to milliseconds. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('millisecond')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._millisecond

    @millisecond.setter
    def millisecond(self, value):
        self._millisecond = validators.string(value)

    @property
    def minute(self) -> str:
        f"""Label format to apply to minutes. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('minute')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute = validators.string(value)

    @property
    def month(self) -> str:
        f"""Label format to apply to months. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('month')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._month

    @month.setter
    def month(self, value):
        self._month = validators.string(value)

    @property
    def second(self) -> str:
        f"""Label format to apply to seconds. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('second')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._second

    @second.setter
    def second(self, value):
        self._second = validators.string(value)

    @property
    def week(self) -> str:
        f"""Label format to apply to weeks. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('week')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._week

    @week.setter
    def week(self, value):
        self._week = validators.string(value)

    @property
    def year(self) -> str:
        f"""Label format to apply to years. Defaults to
        ``{constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('year')}``.

        :rtype: :class:`str <python:str>`
        """
        return self._year

    @year.setter
    def year(self, value):
        self._year = validators.string(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'day': as_dict.pop('day',
                               constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('day')),
            'hour': as_dict.pop('hour',
                                constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('hour')),
            'millisecond': as_dict.pop('millisecond',
                                       constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('millisecond')),
            'minute': as_dict.pop('minute',
                                  constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('minute')),
            'month': as_dict.pop('month',
                                 constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('month')),
            'second': as_dict.pop('second',
                                  constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('second')),
            'week': as_dict.pop('week',
                                constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('week')),
            'year': as_dict.pop('year',
                                constants.DEFAULT_DATE_TIME_LABEL_FORMATS.get('year'))
        }

        return cls(**kwargs)

    def to_dict(self):
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

        return self.trim_dict(untrimmed)
