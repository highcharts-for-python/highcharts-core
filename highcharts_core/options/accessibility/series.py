from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class SeriesAccessibility(HighchartsMeta):
    """Accessibility options global to all data series.

    .. hint::

      Individual series can also have specific accessibility options set.

    """

    def __init__(self, **kwargs):
        self._describe_single_series = None
        self._description_format = None
        self._description_formatter = None
        self._point_description_enabled_threshold = None

        self.describe_single_series = kwargs.get('describe_single_series', None)
        self.description_format = kwargs.get('description_format', None)
        self.description_formatter = kwargs.get('description_formatter', None)
        self.point_description_enabled_threshold = kwargs.get(
            'point_description_enabled_threshold',
            None
        )

    @property
    def describe_single_series(self) -> Optional[bool]:
        """If ``True``, will add series descriptions to charts with a single series.
        Defaults to ``False``.

        :returns: Flag indicating whether to add series descriptions to charts with a
          single series.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._describe_single_series

    @describe_single_series.setter
    def describe_single_series(self, value):
        if value is None:
            self._describe_single_series = None
        else:
            self._describe_single_series = bool(value)

    @property
    def description_format(self) -> Optional[str]:
        """Format to use for describing the data series group to assistive technology -
        including screen readers.

        Defaults to ``'{seriesDescription}{authorDescription}{axisDescription}'``.

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
    def description_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript formatter function to use instead of the default for series
        descriptions.

        Should receives one argument, series, referring to the series to describe. Should
        return a string with the description of the series for a screen reader user. If
        ``false`` is returned, the default formatter will be used for that series.

        :returns: JavaScript formatter function
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._description_formatter

    @description_formatter.setter
    @class_sensitive(CallbackFunction)
    def description_formatter(self, value):
        self._description_formatter = value

    @property
    def point_description_enabled_threshold(self) -> Optional[bool | int]:
        """When a series contains more points than the value set for this property,
        Highcharts will no longer expose information about individual points to screen
        readers.

        Defaults to ``200``.

        .. hint::

          If set to ``False``, the threshold will be disabled and all points will be
          described.

        :returns: The threshold for number of data points above which point description
          information wlil not be provided.
        :rtype: :class:`int <python:int>` or :class:`bool <python:bool>` or
          :obj:`None <python:None>`
        """
        return self._point_description_enabled_threshold

    @point_description_enabled_threshold.setter
    def point_description_enabled_threshold(self, value):
        if value is None:
            self._point_description_enabled_threshold = None
        elif isinstance(value, bool) and value is False:
            self._point_description_enabled_threshold = False
        else:
            self._point_description_enabled_threshold = validators.integer(
                value,
                allow_empty = False,
                coerce_value = True,
                minimum = 1
            )

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'describe_single_series': as_dict.get('describeSingleSeries', None),
            'description_format': as_dict.get('descriptionFormat', None),
            'description_formatter': as_dict.get('descriptionFormatter', None),
            'point_description_enabled_threshold': as_dict.get(
                'pointDescriptionEnabledThreshold',
                None
            ),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'describeSingleSeries': self.describe_single_series,
            'descriptionFormat': self.description_format,
            'descriptionFormatter': self.description_formatter,
            'pointDescriptionEnabledThreshold': self.point_description_enabled_threshold
        }

        return untrimmed
