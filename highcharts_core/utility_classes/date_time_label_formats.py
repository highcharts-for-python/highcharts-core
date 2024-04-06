from typing import Optional, List

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.decorators import validate_types


class DateTimeLabelUnitOptions(HighchartsMeta):
    """Options for the datetime labels for a particular unit type."""
    
    def __init__(self, **kwargs):
        self._list = None
        self._main = None
        
        self.list = kwargs.get('list', None)
        self.main = kwargs.get('main', None)
        
    @property
    def list(self) -> Optional[List[str]]:
        """List of possible values for the datetime unit label. Defaults to
        :obj:`None <python:None>`.
        
        :rtype: :class:`List <python:list>` of :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._list
    
    @list.setter
    def list(self, value):
        if not value:
            self._list = None
        else:
            self._list = [str(x) for x in value]
    
    @property
    def main(self) -> Optional[str]:
        """Label format to apply to the unit. The default varies by unit:
        
          * ``'day'``: ``'%e %b'``
          * ``'hour`':: ``%H:%M'``
          * ``'millisecond'``: ``'%H:%M:%S.%L'``
          * ``'minute'``: ``'%H:%M'``
          * ``'month'``: ``"%b '%Y"``
          * ``'second'``: ``'%H:%M:%S'``
          * ``'week'``: ``'%e %b'``
          * ``'year'``: ``'%Y'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._main

    @main.setter
    def main(self, value):
        self._main = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "list": as_dict.get("list", None),
            "main": as_dict.get("main", None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "list": self.list,
            "main": self.main,
        }

        return untrimmed


class DateTimeLabelRangedUnitOptions(DateTimeLabelUnitOptions):
    """Options for the datetime labels for unit types that support a range."""
    
    def __init__(self, **kwargs):
        self._range = None

        self.range = kwargs.get("range", None)

        super().__init__(**kwargs)
        
    @property
    def range(self) -> Optional[bool]:
        """Whether the unit supports a range. Defaults to :obj:`False <python:False>`.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._range

    @range.setter
    def range(self, value):
        if value is None:
            self._range = None
        else:
            self._range = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "list": as_dict.get("list", None),
            "main": as_dict.get("main", None),
            
            'range': as_dict.get('range', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "list": self.list,
            "main": self.main,
            'range': self.range,
        }

        return untrimmed


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
    def day(self) -> Optional[str | DateTimeLabelUnitOptions]:
        """Label format to apply to days. Defaults to
        ``'%A, %b %e, %Y'``.

        :rtype: :class:`str <python:str>` or 
          :class:`DateTimeLabelUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelUnitOptions>` or 
          :obj:`None <python:None>`
        """
        return self._day

    @day.setter
    def day(self, value):
        if not value:
            self._day = None
        elif isinstance(value, str):
            self._day = value
        else:
            self._day = validate_types(value, DateTimeLabelUnitOptions)

    @property
    def hour(self) -> Optional[str | DateTimeLabelRangedUnitOptions]:
        """Label format to apply to hours. Defaults to
        ``'%A, %b %e, %H:%M'``.

        :rtype: :class:`str <python:str>` or
          :class:`DateTimeLabelRangedUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelRangedUnitOptions>` or
          :obj:`None <python:None>`
        """
        return self._hour

    @hour.setter
    def hour(self, value):
        if not value:
            self._hour = None
        elif isinstance(value, str):
            self._hour = value
        else:
            self._hour = validate_types(value, DateTimeLabelRangedUnitOptions)

    @property
    def millisecond(self) -> Optional[str | DateTimeLabelRangedUnitOptions]:
        """Label format to apply to milliseconds. Defaults to
        ``'%A, %b %e, %H:%M:%S.%L'``.

        :rtype: :class:`str <python:str>` or
          :class:`DateTimeLabelRangedUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelRangedUnitOptions>` or
          :obj:`None <python:None>`
        """
        return self._millisecond

    @millisecond.setter
    def millisecond(self, value):
        if not value:
            self._millisecond = None
        elif isinstance(value, str):
            self._millisecond = value
        else:
            self._millisecond = validate_types(value, DateTimeLabelRangedUnitOptions)

    @property
    def minute(self) -> Optional[str | DateTimeLabelRangedUnitOptions]:
        """Label format to apply to minutes. Defaults to
        ``'%A, %b %e, %H:%M'``.

        :rtype: :class:`str <python:str>` or
          :class:`DateTimeLabelRangedUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelRangedUnitOptions>` or
          :obj:`None <python:None>`
        """
        return self._minute

    @minute.setter
    def minute(self, value):
        if not value:
            self._minute = None
        elif isinstance(value, str):
            self._minute = value
        else:
            self._minute = validate_types(value, DateTimeLabelRangedUnitOptions)

    @property
    def month(self) -> Optional[str | DateTimeLabelUnitOptions]:
        """Label format to apply to months. Defaults to
        ``'%B %Y'``.

        :rtype: :class:`str <python:str>` or
          :class:`DateTimeLabelUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelUnitOptions>` or
          :obj:`None <python:None>`
        """
        return self._month

    @month.setter
    def month(self, value):
        if not value:
            self._month = None
        elif isinstance(value, str):
            self._month = value
        else:
            self._month = validate_types(value, DateTimeLabelUnitOptions)

    @property
    def second(self) -> Optional[str | DateTimeLabelRangedUnitOptions]:
        """Label format to apply to seconds. Defaults to
        ``'%A, %b %e, %H:%M:%S'``.

        :rtype: :class:`str <python:str>` or
          :class:`DateTimeLabelRangedUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelRangedUnitOptions>` or
          :obj:`None <python:None>`
        """
        return self._second

    @second.setter
    def second(self, value):
        if not value:
            self._second = None
        elif isinstance(value, str):
            self._second = value
        else:
            self._second = validate_types(value, DateTimeLabelRangedUnitOptions)

    @property
    def week(self) -> Optional[str | DateTimeLabelUnitOptions]:
        """Label format to apply to weeks. Defaults to
        ``'Week from %A, %b %e, %Y'``.

        :rtype: :class:`str <python:str>` or
          :class:`DateTimeLabelUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelUnitOptions>` or
          :obj:`None <python:None>`
        """
        return self._week

    @week.setter
    def week(self, value):
        if not value:
            self._week = None
        elif isinstance(value, str):
            self._week = value
        else:
            self._week = validate_types(value, DateTimeLabelUnitOptions)

    @property
    def year(self) -> Optional[str | DateTimeLabelUnitOptions]:
        """Label format to apply to years. Defaults to
        ``'%Y'``.

        :rtype: :class:`str <python:str>` or
          :class:`DateTimeLabelUnitOptions <highcharts_core.utility_classes.date_time_label_formats.DateTimeLabelUnitOptions>` or
          :obj:`None <python:None>`
        """
        return self._year

    @year.setter
    def year(self, value):
        if not value:
            self._year = None
        elif isinstance(value, str):
            self._year = value
        else:
            self._year = validate_types(value, DateTimeLabelUnitOptions)

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
