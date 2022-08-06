from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class AnnounceNewDataLanguageOptions(HighchartsMeta):
    """Default announcement for new data in charts.

    .. note::

      If (JavaScript) ``addPoint()`` or ``addSeries()`` is used, and only one
      series/point is added, the
      :meth:`AnnounceNewDataLanguageOptions.new_point_announce` and
      :meth:`AnnounceNewdata.new_series_announce` strings are used.

      The ``...single`` versions will be used if there is only one chart on the page,
      and the ``...multiple`` versions will be used if there are multiple charts on the
      page. For all other new data events, the
      :meth:`AnnounceNewData.new_data_announce` string will be used.

    """

    def __init__(self, **kwargs):
        self._new_data_announce = None
        self._new_point_announce_multiple = None
        self._new_point_announce_single = None
        self._new_series_announce_multiple = None
        self._new_series_announce_single = None

        self.new_data_announce = kwargs.pop('new_data_announce', None)
        self.new_point_announce_multiple = kwargs.pop('new_point_announce_multiple', None)
        self.new_point_announce_single = kwargs.pop('new_point_announce_single', None)
        self.new_series_announce_multiple = kwargs.pop('new_series_announce_multiple',
                                                       None)
        self.new_series_announce_single = kwargs.pop('new_series_announce_single', None)

    @property
    def new_data_announce(self) -> Optional[str]:
        """Announcement for any new data. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_ANNOUNCE_NEW_DATA}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._new_data_announce

    @new_data_announce.setter
    def new_data_announce(self, value):
        self._new_data_announce = validators.string(value, allow_empty = True)

    @property
    def new_point_announce_multiple(self) -> Optional[str]:
        """Announcement when multiple new points have been added. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_ANNOUNCE_NEW_POINT_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._new_point_announce_multiple

    @new_point_announce_multiple.setter
    def new_point_announce_multiple(self, value):
        self._new_point_announce_multiple = validators.string(value, allow_empty = True)

    @property
    def new_point_announce_single(self) -> Optional[str]:
        """Announcement when a single new point has been added. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_ANNOUNCE_NEW_POINT_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._new_point_announce_single

    @new_point_announce_single.setter
    def new_point_announce_single(self, value):
        self._new_point_announce_single = validators.string(value, allow_empty = True)

    @property
    def new_series_announce_multiple(self) -> Optional[str]:
        """Announcement when multiple new series have been added. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_ANNOUNCE_NEW_SERIES_MULTIPLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._new_series_announce_multiple

    @new_series_announce_multiple.setter
    def new_series_announce_multiple(self, value):
        self._new_series_announce_multiple = validators.string(value, allow_empty = True)

    @property
    def new_series_announce_single(self) -> Optional[str]:
        """Announcement when a single new series has been added. Defaults to:
        ``'{constants.DEFAULT_LANG_ACS_ANNOUNCE_NEW_SERIES_SINGLE}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._new_series_announce_single

    @new_series_announce_single.setter
    def new_series_announce_single(self, value):
        self._new_series_announce_single = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'new_data_announce': as_dict.pop('newDataAnnounce', None),
            'new_point_announce_multiple': as_dict.pop('newPointAnnounceMultiple', None),
            'new_point_announce_single': as_dict.pop('newPointAnnounceSingle', None),
            'new_series_announce_multiple': as_dict.pop('newSeriesAnnounceMultiple',
                                                        None),
            'new_series_announce_single': as_dict.pop('newSeriesAnnounceSingle', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'newDataAnnounce': self.new_data_announce,
            'newPointAnnounceMultiple': self.new_point_announce_multiple,
            'newPointAnnounceSingle': self.new_point_announce_single,
            'newSeriesAnnounceMultiple': self.new_series_announce_multiple,
            'newSeriesAnnounceSingle': self.new_series_announce_single
        }

        return untrimmed
