from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import JavaScriptClass, \
  CallbackFunction


class Time(HighchartsMeta):
    """Time options that can apply globally or to individual charts. These settings
    affect how datetime axes are laid out, how tooltips are formatted, how series
    :meth:`point_interval_unit <Series.point_interval_unit` works and how the
    Highcharts Stock range selector handles time."""

    def __init__(self, **kwargs):
        self._Date = None
        self._get_timezone_offset = None
        self._moment = None
        self._timezone = None
        self._timezone_offset = None
        self._use_utc = None

        self.Date = kwargs.get('Date', None)
        self.get_timezone_offset = kwargs.get('get_timezone_offset', None)
        self.moment = kwargs.get('moment', None)
        self.timezone = kwargs.get('timezone', None)
        self.timezone_offset = kwargs.get('timezone_offset', None)
        self.use_utc = kwargs.get('use_utc', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'time'

    @property
    def Date(self) -> Optional[JavaScriptClass]:
        """A custom JavaScript ``Date`` class for more sophisticated date handling. For
        example, `JDate <https://github.com/tahajahangir/jdate>`_ can be used to handle
        Jalali dates. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`JavaScriptClass` or :obj:`None <python:None>`
        """
        return self._Date

    @Date.setter
    @class_sensitive(JavaScriptClass)
    def Date(self, value):
        self._Date = value

    @property
    def get_timezone_offset(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function that returns the time zone offset for a given
        datetime. Defaults to :obj:`None <python:None>`.

        The function is expected to take a Unix timestamp (as number of milliseconds since
        January 1, 1970) as an argument and return the timezone offset in minutes.

        .. hint::

          This provides a hook for drawing time based charts in specific time zones using
          their local DST crossover dates, with the help of external libraries.

        .. warning::

          If :meth:`Time.timezone` is specified, then this custom function will be
          overridden by an automatic function leveraging the
          `moment.js <https://momentjs.com>`_ library.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._get_timezone_offset

    @get_timezone_offset.setter
    @class_sensitive(CallbackFunction)
    def get_timezone_offset(self, value):
        self._get_timezone_offset = value

    @property
    def moment(self) -> Optional[CallbackFunction]:
        """A JavaScript function that can be used to manually load the
        `moment.js <https://momentjs.com>`_ library when initializing a chart, rather than
        loading it from within ``window`` or a ``<script/>`` tag. Defaults to
        :obj:`None <python:None>`.

        .. note::

          The function expects no arguments and returns no result.

        .. warning::

          If loading ``moment.js`` is loaded from within a ``<script/>`` tag on the page,
          this setting can be left as :obj:`None <python:None>`. Highcharts will still be
          able to access and use the library.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._moment

    @moment.setter
    @class_sensitive(CallbackFunction)
    def moment(self, value):
        self._moment = value

    @property
    def timezone(self) -> Optional[str]:
        """Indicates the timezone in which to render the chart. Defaults to
        :obj:`None <python:None>`.

        If this value is provided, Highcharts will override the setting for
        :meth:`Time.get_timezone_offset` with a default function leveraging the
        `moment.js <https://momentjs.com>`_ library.

        .. warning::

          Requires `moment.js <https://momentjs.com>`_ to work properly. If ``moment.js``
          is not available, this will throw a Highcharts error in the JavaScript console
          but will *not* prevent the chart from rendering.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        self._timezone = validators.string(value, allow_empty = True)

    @property
    def timezone_offset(self) -> Optional[int]:
        """The timezone offset to apply in minutes. Defaults to ``0``.

        .. hint::

          Use this to display UTC data in a predefined timezone.

        .. note::

          Positive values are west of UTC. Negative values are east of UTC, as in the
          ECMAScript
          `getTimezoneOffset() <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset>`_
          method.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, value):
        self._timezone_offset = validators.integer(value, allow_empty = True)

    @property
    def use_utc(self) -> Optional[bool]:
        """If ``True``, use UTC time for axis scaling, tickmark placement, and time
        display. Defaults to ``True``.

        .. hint::

          The advantage of using UTC is that the time displays equally regardless of the
          user agent's time zone settings. Local time can be used when the data is loaded
          in real time or when correct Daylight Saving Time transitions are required.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_utc

    @use_utc.setter
    def use_utc(self, value):
        if value is None:
            self._use_utc = None
        else:
            self._use_utc = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'Date': as_dict.get('Date', None),
            'get_timezone_offset': as_dict.get('getTimezoneOffset', None),
            'moment': as_dict.get('moment', None),
            'timezone': as_dict.get('timezone', None),
            'timezone_offset': as_dict.get('timezoneOffset', None),
            'use_utc': as_dict.get('useUTC', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'Date': self.Date,
            'getTimezoneOffset': self.get_timezone_offset,
            'moment': self.moment,
            'timezone': self.timezone,
            'timezoneOffset': self.timezone_offset,
            'useUTC': self.use_utc
        }

        return untrimmed
