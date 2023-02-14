from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


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

        self.new_data_announce = kwargs.get('new_data_announce', None)
        self.new_point_announce_multiple = kwargs.get('new_point_announce_multiple', None)
        self.new_point_announce_single = kwargs.get('new_point_announce_single', None)
        self.new_series_announce_multiple = kwargs.get('new_series_announce_multiple',
                                                       None)
        self.new_series_announce_single = kwargs.get('new_series_announce_single', None)

    @property
    def new_data_announce(self) -> Optional[str]:
        """Announcement for any new data. Defaults to:
        ``'Updated data for chart {chartTitle}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._new_data_announce

    @new_data_announce.setter
    def new_data_announce(self, value):
        self._new_data_announce = validators.string(value, allow_empty = True)

    @property
    def new_point_announce_multiple(self) -> Optional[str]:
        """Announcement when multiple new points have been added. Defaults to:
        ``'New data point in chart {chartTitle}: {pointDesc}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._new_point_announce_multiple

    @new_point_announce_multiple.setter
    def new_point_announce_multiple(self, value):
        self._new_point_announce_multiple = validators.string(value, allow_empty = True)

    @property
    def new_point_announce_single(self) -> Optional[str]:
        """Announcement when a single new point has been added. Defaults to:
        ``'New data point: {pointDesc}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._new_point_announce_single

    @new_point_announce_single.setter
    def new_point_announce_single(self, value):
        self._new_point_announce_single = validators.string(value, allow_empty = True)

    @property
    def new_series_announce_multiple(self) -> Optional[str]:
        """Announcement when multiple new series have been added. Defaults to:
        ``'New data series in chart {chartTitle}: {seriesDesc}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._new_series_announce_multiple

    @new_series_announce_multiple.setter
    def new_series_announce_multiple(self, value):
        self._new_series_announce_multiple = validators.string(value, allow_empty = True)

    @property
    def new_series_announce_single(self) -> Optional[str]:
        """Announcement when a single new series has been added. Defaults to:
        ``'New data series: {seriesDesc}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._new_series_announce_single

    @new_series_announce_single.setter
    def new_series_announce_single(self, value):
        self._new_series_announce_single = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'new_data_announce': as_dict.get('newDataAnnounce', None),
            'new_point_announce_multiple': as_dict.get('newPointAnnounceMultiple', None),
            'new_point_announce_single': as_dict.get('newPointAnnounceSingle', None),
            'new_series_announce_multiple': as_dict.get('newSeriesAnnounceMultiple',
                                                        None),
            'new_series_announce_single': as_dict.get('newSeriesAnnounceSingle', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'newDataAnnounce': self.new_data_announce,
            'newPointAnnounceMultiple': self.new_point_announce_multiple,
            'newPointAnnounceSingle': self.new_point_announce_single,
            'newSeriesAnnounceMultiple': self.new_series_announce_multiple,
            'newSeriesAnnounceSingle': self.new_series_announce_single
        }

        return untrimmed
