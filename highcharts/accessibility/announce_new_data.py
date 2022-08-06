from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class AnnounceNewData(HighchartsMeta):
    """Options for announcing new data to screen reader users.

    .. tip::

      Useful for dynamic data applications and drilldown.

      Keep in mind that frequent announcements will not be useful to users, as they
      won't have time to explore the new data. For these applications, consider making
      snapshots of the data accessible, and do the announcements in batches.

    :returns: Configuration for the announcement of new data to screen reader users.
    :rtype: :class:`AnnounceNewData` or :obj:`None <python:None>`
    """

    def __init__(self, **kwargs):
        self._announcement_formatter = None
        self._enabled = None
        self._interrupt_user = None
        self._minimum_announcement_interval = None

        self.announcement_formatter = kwargs.pop('announcement_formatter', None)
        self.enabled = kwargs.pop('enabled', None)
        self.interrupt_user = kwargs.pop('interrupt_user', None)
        self.minimum_announcement_interval = kwargs.pop('minimum_announcement_interval',
                                                        None)

    @property
    def announcement_formatter(self) -> Optional[str]:
        """Optional JavaScript formatter callback for the announcement.

        Expects a string containing JavaScript code. This code should be a JavaScript
        function that up to three arguments:

          #. The first argument is always an array of all series that received updates.
             If an announcement is already queued, the series that received updates for
             that announcement are also included in this array.
          #. The second argument is provided if ``chart.addSeries`` was called
             (in JavaScript), and there is a new series. In that case, this argument is a
             reference to the new series.
          #. The third argument, similarly, is provided if ``series.addPoint`` was called
             (in JavaScript), and there is a new point. In that case, this argument is a
             reference to the new point.

        The JavaScript function should return a string with the text to announce to the
        user. Return an empty string to not announce anything. Return ``false`` to use the
        default announcement format.

        :returns: The code of the JavaScript function ot use as the formatter callback for
          the new data announcement.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._announcement_formatter

    @announcement_formatter.setter
    def announcement_formatter(self, value: Optional[str]):
        self._announcement_formatter = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable the announcement of new data to screen reader users.

        Defaults to ``False``.

        :returns: Flag indicating whether new data announcements are enabled for the
          chart.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def interrupt_user(self) -> Optional[bool]:
        """Choose whether or not the announcements should interrupt the screen reader.
        Defaults to ``False``.

        If not enabled, the user will be notified once idle.

        .. hint::

          It is recommended **not** to enable this setting unless there is a specific
          reason to do so.

        :returns: Flag indicating whether new data announcements should interrupt the
          screen reader.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._interrupt_user

    @interrupt_user.setter
    def interrupt_user(self, value):
        if value is None:
            self._interrupt_user = None
        else:
            self._interrupt_user = bool(value)

    @property
    def minimum_announcement_interval(self) -> Optional[int]:
        """Minimum interval between announcements in milliseconds. Defaults to ``5000``.

        .. warning::

          Non-integer values will be coerced to an :class:`int <python:int>`.

        If new data arrives before this amount of time has passed, it is queued for
        announcement.

        If another new data event happens while an announcement is queued, the queued
        announcement is dropped, and the latest announcement is queued instead. Set to 0
        to allow all announcements, but be warned that frequent announcements are
        disturbing to users.

        :returns: The minimum interval between announcements, expressed in milliseconds.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`

        :raises ValueError: if a negative value is supplied
        """
        return self._minimum_announcement_interval

    @minimum_announcement_interval.setter
    def minimum_announcement_interval(self, value: int | float | Decimal):
        value = validators.integer(value,
                                   allow_empty = True,
                                   coerce_value = True,
                                   minimum = 0)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'announcement_formatter': as_dict.pop('announcementFormatter', None),
            'enabled': as_dict.pop('enabled', None),
            'interrupt_user': as_dict.pop('interruptUser', None),
            'minimum_announcement_interval': as_dict.pop('minimumAnnouncementInterval',
                                                            None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'announcementFormatter': self.announcement_formatter,
            'enabled': self.enabled,
            'interruptUser': self.interrupt_user,
            'minimumAnnouncementInterval': self.minimum_announcement_interval
        }

        return untrimmed
