from typing import Optional

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class DataSorting(HighchartsMeta):
    """Options for the series data sorting."""

    def __init__(self, **kwargs):
        self._enabled = None
        self._match_by_name = None
        self._sort_key = None

        self.enabled = kwargs.pop('enabled', None)
        self.match_by_name = kwargs.pop('match_by_name', None)
        self.sort_key = kwargs.pop('sort_key', None)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable or disable data sorting for the series. Defaults to
        :obj:`None <python:None>` (equivalent to ``False``).

        .. hint::

          Use :meth:`XAxis.reversed` to change the sorting order.

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
    def match_by_name(self) -> Optional[bool]:
        """If ``True``, allow matching points by name in an update. If ``False``, points
        will be matched by order. Defaults to :obj:`None <python:None>` (equivalent to
        ``False``).

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._match_by_name

    @match_by_name.setter
    def match_by_name(self, value):
        if value is None:
            self._match_by_name = None
        else:
            self._match_by_name = bool(value)

    @property
    def sort_key(self) -> Optional[str]:
        """Determines what data value should be used to sort by. Defaults to
        :obj:`None <python:None>`, which behaves as if the value were ``'y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, value):
        self._sort_key = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.pop('enabled', None),
            'match_by_name': as_dict.pop('matchByName', None),
            'sort_key': as_dict.pop('sortKey', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'matchByName': self.match_by_name,
            'sortKey': self.sort_key
        }

        return untrimmed
