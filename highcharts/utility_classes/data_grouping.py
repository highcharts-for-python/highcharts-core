from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.date_time_label_formats import DateTimeLabelFormats


class DataGroupingOptions(HighchartsMeta):
    """Data grouping options for the wind barbs. Defaults to
    :obj:`None <python:None>`.

    .. warning::

      In Highcharts, this requires the ``modules/datagrouping.js`` module to be
      loaded. In Highcharts Stock, data grouping is included.

    """

    def __init__(self, **kwargs):
        self._anchor = None
        self._approximation = None
        self._date_time_label_formats = None
        self._enabled = None
        self._first_anchor = None
        self._forced = None
        self._group_all = None
        self._group_pixel_width = None
        self._last_anchor = None
        self._units = None

        self.anchor = kwargs.pop('anchor', None)
        self.approximation = kwargs.pop('approximation', None)
        self.date_time_label_formats = kwargs.pop('date_time_label_formats', None)
        self.enabled = kwargs.pop('enabled', None)
        self.first_anchor = kwargs.pop('first_anchor', None)
        self.forced = kwargs.pop('forced', None)
        self.group_all = kwargs.pop('group_all', None)
        self.group_pixel_width = kwargs.pop('group_pixel_width', None)
        self.last_anchor = kwargs.pop('last_anchor', None)
        self.units = kwargs.pop('units', None)

    @property
    def anchor(self) -> Optional[str]:
        """Specifies how the points should be located on the X axis inside the group.
        Defaults to ``'start'``.

        Available options:

          * ``'start'`` places the point at the beginning of the group (e.g. range
            00:00:00 - 23:59:59 -> 00:00:00)
          * ``'middle'`` places the point in the middle of the group (e.g. range 00:00:00
            - 23:59:59 -> 12:00:00)
          * ``'end'`` places the point at the end of the group (e.g. range 00:00:00 -
            23:59:59 -> 23:59:59)

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._anchor

    @anchor.setter
    def anchor(self, value):
        if not value:
            self._anchor = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['start', 'middle', 'end']:
                raise errors.HighchartsValueError(f'anchor expects "start", "middle", '
                                                  f'or "end". Received: {value}')

            self._anchor = value

    @property
    def approximation(self) -> Optional[str]:
        """Approximation function for the data grouping. The default (``'windbarb'``)
        returns an average of wind speed and a vector average direction weighted by wind
        speed.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._approximation

    @approximation.setter
    def approximation(self, value):
        self._approximation = validators.string(value, allow_empty = True)

    @property
    def date_time_label_formats(self) -> Optional[DateTimeLabelFormats]:
        """Datetime formats for the header of the tooltip in a stock chart. Defaults to
        :obj:`None <python:None>`.

        .. seealso::

          * :class:`DateTimeLabelFormats`

        :rtype: :class:`DateTimeLabelFormats` or :obj:`None <python:None>`
        """
        return self._date_time_label_formats

    @date_time_label_formats.setter
    @class_sensitive(DateTimeLabelFormats)
    def date_time_label_formats(self, value):
        self._date_time_label_formats = value

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables data grouping. Defaults to ``True``.

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
    def first_anchor(self) -> Optional[str]:
        """Specifies how the first grouped point is positioned on the xAxis. Defaults to
        ``'start'``.

        If :meth:`first_anchor <DataGroupingOptions.first_anchor>` and/or
        :meth:`last_anchor <DataGroupingOptions.last_anchor>` are provided, then those
        options take precedence over
        :meth:`anchor <DataGroupingOptions.anchor>` for the first and/or last grouped
        points.

        Supported values are:

          * ``'start'`` places the point at the beginning of the group (e.g. range
            00:00:00 - 23:59:59 -> 00:00:00)
          * ``'middle'`` places the point in the middle of the group (e.g. range 00:00:00
            - 23:59:59 -> 12:00:00)
          * ``'end'`` places the point at the end of the group (e.g. range 00:00:00 -
            23:59:59 -> 23:59:59)
          * ``'firstPoint'`` places the point at the first point in the group (e.g. points
            at 00:13, 00:35, 00:59 -> 00:13)
          * ``'lastPoint'`` places the point at the last point in the group (e.g. points
            at 00:13, 00:35, 00:59 -> 00:59)

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._first_anchor

    @first_anchor.setter
    def first_anchor(self, value):
        if not value:
            self._first_anchor = None
        else:
            value = validators.string(value)
            if value not in ['start', 'middle', 'end', 'firstPoint', 'lastPoint']:
                raise errors.HighchartsValueError(f'first_anchor expects a supported '
                                                  f'value. Received: {value}')

            self._first_anchor = value

    @property
    def forced(self) -> Optional[bool]:
        """If ``True``, data grouping is applied no matter how small the intervals are.
        Defaults to ``False``.

        .. hint::

          This can be handy for example when the sum should be calculated for values
          appearing at random times within each hour.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._forced

    @forced.setter
    def forced(self, value):
        if value is None:
            self._forced = None
        else:
            self._forced = bool(value)

    @property
    def group_all(self) -> Optional[bool]:
        """If ``True``, will force data grouping to calculate all grouped points for a
        given dataset even if not visible. If ``False``, data grouping is calculated only
        for visible points. Defaults to ``False``.

        .. note::

          Setting this option to ``True`` prevents for example a column series from
          calculating a grouped point only for part of the dataset. The effect is similar
          to :meth:`SeriesOptions.get_extremes_for_all` but does not affect yAxis
          extremes.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._group_all

    @group_all.setter
    def group_all(self, value):
        if value is None:
            self._group_all = None
        else:
            self._group_all = bool(value)

    @property
    def group_pixel_width(self) -> Optional[int | float | Decimal]:
        """The approximate data group width, expressed in pixels. Defaults to ``30``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_pixel_width

    @group_pixel_width.setter
    def group_pixel_width(self, value):
        self._group_pixel_width = validators.numeric(value,
                                                     allow_empty = True,
                                                     minimum = 0)

    @property
    def last_anchor(self) -> Optional[str]:
        """Specifies how the last grouped point is positioned on the xAxis. Defaults to
        ``'start'``.

        If :meth:`first_anchor <DataGroupingOptions.first_anchor>` and/or
        :meth:`last_anchor <DataGroupingOptions.last_anchor>` are provided, then those
        options take precedence over
        :meth:`anchor <DataGroupingOptions.anchor>` for the first and/or last grouped
        points.

        Supported values are:

          * ``'start'`` places the point at the beginning of the group (e.g. range
            00:00:00 - 23:59:59 -> 00:00:00)
          * ``'middle'`` places the point in the middle of the group (e.g. range 00:00:00
            - 23:59:59 -> 12:00:00)
          * ``'end'`` places the point at the end of the group (e.g. range 00:00:00 -
            23:59:59 -> 23:59:59)
          * ``'firstPoint'`` places the point at the first point in the group (e.g. points
            at 00:13, 00:35, 00:59 -> 00:13)
          * ``'lastPoint'`` places the point at the last point in the group (e.g. points
            at 00:13, 00:35, 00:59 -> 00:59)

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._last_anchor

    @last_anchor.setter
    def last_anchor(self, value):
        if not value:
            self._last_anchor = None
        else:
            value = validators.string(value)
            if value not in ['start', 'middle', 'end', 'firstPoint', 'lastPoint']:
                raise errors.HighchartsValueError(f'last_anchor expects a supported '
                                                  f'value. Received: {value}')

            self._last_anchor = value

    @property
    def units(self) -> Optional[List[List[str | List[int | float | Decimal | constants.EnforcedNullType | type(None)]]]]:
        """An array determining what time intervals the data is allowed to be grouped to.
        Each array item is an array where the first value is the time unit expressed as a
        :class:`str <python:str>` and the second value is another array of allowed
        multiples.

        Defaults to :obj:`None <python:None>`, which behaves as:

        .. code-block:: python

          {
              'units': [
                  [
                      'millisecond', # unit name
                      [1, 2, 5, 10, 20, 25, 50, 100, 200, 500] # allowed multiples
                  ],
                  [
                      'second',
                      [1, 2, 5, 10, 15, 30]
                  ],
                  [
                      'minute',
                      [1, 2, 5, 10, 15, 30]
                  ],
                  [
                      'hour',
                      [1, 2, 3, 4, 6, 8, 12]
                  ],
                  [
                      'day',
                      [1]
                  ],
                  [
                      'week',
                      [1]
                  ],
                  [
                      'month',
                      [1, 3, 6]
                  ],
                  [
                      'year',
                      None
                  ]
              ]
          }

        :rtype: :class:`list <python:list>` of :class:`list <python:list>` of
          :class:`str <python:str>` and :class:`list <python:list>` of numerics, or
          :obj:`None <python:None>`
        """
        return self._units

    @units.setter
    def units(self, value):
        if not value:
            self._units = None
        else:
            value = validators.iterable(value)
            value = [validators.iterable(x) for x in value]
            for item in value:
                if len(item) != 2:
                    raise errors.HighchartsValueError(f'Each entry in the units list '
                                                      f'is expected to be a 2-member '
                                                      f'list. However, was a {value}-'
                                                      f'member list.')
                validators.string(item[0])
                if item[1] and not isinstance(item[1], constants.EnforcedNullType):
                    [validators.numeric(x) for x in item[1]]

            self._units = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'anchor': as_dict.pop('anchor', None),
            'approximation': as_dict.pop('approximation', None),
            'date_time_label_formats': as_dict.pop('dateTimeLabelFormats', None),
            'enabled': as_dict.pop('enabled', None),
            'first_anchor': as_dict.pop('firstAnchor', None),
            'forced': as_dict.pop('forced', None),
            'group_all': as_dict.pop('groupAll', None),
            'group_pixel_width': as_dict.pop('groupPixelWidth', None),
            'last_anchor': as_dict.pop('lastAnchor', None),
            'units': as_dict.pop('units', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'anchor': self.anchor,
            'approximation': self.approximation,
            'dateTimeLabelFormats': self.date_time_label_formats,
            'enabled': self.enabled,
            'firstAnchor': self.first_anchor,
            'forced': self.forced,
            'groupAll': self.group_all,
            'groupPixelWidth': self.group_pixel_width,
            'lastAnchor': self.last_anchor,
            'units': self.units
        }

        return self.trim_dict(untrimmed)