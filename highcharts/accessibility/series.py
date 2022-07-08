from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class AccessibilitySeries(HighchartsMeta):
    """Accessibility options global to all data series.

    .. hint::

      Individual series can also have specific accessibility options set.

    """

    def __init__(self, **kwargs):
        self._describe_single_series = False
        self._description_format = constants.DEFAULT_DESCRIPTION_FORMAT
        self._description_formatter = None
        self._point_description_enabled_threshold = 200

        self.describe_single_series = kwargs.pop('describe_single_series', False)
        self.description_format = kwargs.pop('description_format',
                                             constants.DEFAULT_DESCRIPTION_FORMAT)
        self.description_formatter = kwargs.pop('description_formatter', None)
        self.point_description_enabled_threshold = kwargs.pop(
            'point_description_enabled_threshold',
            200
        )

    @property
    def describe_single_series(self) -> bool:
        """If ``True``, will add series descriptions to charts with a single series.
        Defaults to ``False``.

        :returns: Flag indicating whether to add series descriptions to charts with a
          single series.
        :rtype: :class:`bool <python:bool>`
        """
        return self._describe_single_series

    @describe_single_series.setter
    def describe_single_series(self, value):
        self._describe_single_series = bool(value)

    @property
    def description_format(self) -> Optional[str]:
        f"""Format to use for describing the data series group to assistive technology -
        including screen readers.

        Defaults to ``'{constants.DEFAULT_DESCRIPTION_FORMAT}'``.

        The series context and its subproperties are available under the variable
        ``{{series}}``, for example ``{{series.name}}`` for the series name, and
        ``{{series.points.length}}`` for the number of data points.

        The chart context and its subproperties are available under the variable
        ``{{chart}}``, for example ``{{chart.series.length}}`` for the number of series in
        the chart.

        ``{{seriesDescription}}`` refers to the automatic description of the series type
        and number of points added by Highcharts by default.

        ``{{authorDescription}}`` refers to the description added in
        ``series.description`` if one is present.

        ``{{axisDescription}}`` refers to the description added if the chart has multiple
        X or Y axes.

        Note that if :meth:`Series.description_formatter` is not :obj:`None <python:None>`
        it will take precedence, and this option will be overridden.

        :returns: Format string that applies to the description produced for the data
          series.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_format

    @description_format.setter
    def description_format(self, value):
        self._description_format = validators.string(value, allow_empty = True)

    @property
    def description_formatter(self) -> Optional[str]:
        """JavaScript formatter function to use instead of the default for series
        descriptions.

        Should receives one argument, series, referring to the series to describe. Should
        return a string with the description of the series for a screen reader user. If
        ``false`` is returned, the default formatter will be used for that series.

        :returns: JavaScript formatter function
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_formatter

    @description_formatter.setter
    def description_formatter(self, value):
        self._description_formatter = validators.string(value, allow_empty = True)

    @property
    def point_description_enabled_threshold(self) -> bool | int:
        """When a series contains more points than the value set for this property,
        Highcharts will no longer expose information about individual points to screen
        readers.

        Defaults to ``200``.

        .. hint::

          If set to ``False``, the threshold will be disabled and all points will be
          described.

        :returns: The threshold for number of data points above which point description
          information wlil not be provided.
        :rtype: :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._point_description_enabled_threshold

    @point_description_enabled_threshold.setter
    def point_description_enabled_threshold(self, value):
        if isinstance(value, bool) and value is False:
            self._point_description_enabled_threshold = False
        else:
            self._point_description_enabled_threshold = validators.integer(
                value,
                allow_empty = False,
                coerce_value = True,
                minimum = 1
            )

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'describe_single_series': as_dict.pop('describeSingleSeries', False),
            'description_format': as_dict.pop('descriptionFormat',
                                              constants.DEFAULT_DESCRIPTION_FORMAT),
            'description_formatter': as_dict.pop('descriptionFormatter', None),
            'point_description_enabled_threshold': as_dict.pop(
                'pointDescriptionEnabledThreshold',
                200
            )
        }

        return cls(**kwargs)

    def to_json(self, encoding = 'utf-8'):
        untrimmed = {
            'describeSingleSeries': self.describe_single_series,
            'descriptionFormat': self.descriptionFormat,
            'descriptionFormatter': self.descriptionFormatter,
            'pointDescriptionEnabledThreshold': self.point_description_enabled_threshold
        }
        as_dict = self.trim_dict(untrimmed)

        return as_dict
