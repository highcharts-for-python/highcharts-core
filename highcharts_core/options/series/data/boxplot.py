from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.options.series.data.cartesian import CartesianData


class BoxPlotData(CartesianData):
    """Variant of :class:`CartesianData` which is used for data points in a boxplot."""

    def __init__(self, **kwargs):
        self._box_dash_style = None
        self._high = None
        self._low = None
        self._median = None
        self._median_dash_style = None
        self._q1 = None
        self._q3 = None
        self._stem_dash_style = None
        self._whisker_dash_style = None

        self.box_dash_style = kwargs.get('box_dash_style', None)
        self.high = kwargs.get('high', None)
        self.low = kwargs.get('low', None)
        self.median = kwargs.get('median', None)
        self.median_dash_style = kwargs.get('median_dash_style', None)
        self.q1 = kwargs.get('q1', None)
        self.q3 = kwargs.get('q3', None)
        self.stem_dash_style = kwargs.get('stem_dash_style', None)
        self.whisker_dash_style = kwargs.get('whisker_dash_style', None)

        super().__init__(**kwargs)

    @property
    def box_dash_style(self) -> Optional[str]:
        """The dash style of the box.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._box_dash_style

    @box_dash_style.setter
    def box_dash_style(self, value):
        if not value:
            self._box_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'box_dash_style expects a recognized '
                                                  f'value, but received: {value}')
            self._box_dash_style = value

    @property
    def high(self) -> Optional[int | float | Decimal]:
        """The highest value in the sample set. The top whisker is drawn here. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._high

    @high.setter
    def high(self, value):
        self._high = validators.numeric(value, allow_empty = True)

    @property
    def low(self) -> Optional[int | float | Decimal]:
        """The lowest value in the sample set. The bottom whisker is drawn here. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._low

    @low.setter
    def low(self, value):
        self._low = validators.numeric(value, allow_empty = True)

    @property
    def median(self) -> Optional[int | float | Decimal]:
        """The median value in the sample set. This is drawn as a line through the middle
        of the box. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._median

    @median.setter
    def median(self, value):
        self._median = validators.numeric(value, allow_empty = True)

    @property
    def median_dash_style(self) -> Optional[str]:
        """The dash style of the median. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._median_dash_style

    @median_dash_style.setter
    def median_dash_style(self, value):
        if not value:
            self._median_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'median_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._median_dash_style = value

    @property
    def q1(self) -> Optional[int | float | Decimal]:
        """The lower quartile in the sample set. This is the bottom of the box. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._q1

    @q1.setter
    def q1(self, value):
        self._q1 = validators.numeric(value, allow_empty = True)

    @property
    def q3(self) -> Optional[int | float | Decimal]:
        """The higher quartile in the sample set. This is the top of the box. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._q3

    @q3.setter
    def q3(self, value):
        self._q3 = validators.numeric(value, allow_empty = True)

    @property
    def stem_dash_style(self) -> Optional[str]:
        """The dash style of the :term:`stem`, the vertical line extending from the box to
        the whiskers. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stem_dash_style

    @stem_dash_style.setter
    def stem_dash_style(self, value):
        if not value:
            self._stem_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'stem_dash_style expects a recognized'
                                                  f' value, but received: {value}')
            self._stem_dash_style = value

    @property
    def whisker_dash_style(self) -> Optional[str]:
        """The dash style of the whiskers. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._whisker_dash_style

    @whisker_dash_style.setter
    def whisker_dash_style(self, value):
        if not value:
            self._whisker_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'whisker_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._whisker_dash_style = value

    @classmethod
    def from_array(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'BoxPlotData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            elif checkers.is_iterable(item):
                if len(item) == 6:
                    as_dict = {
                        'x': item[0],
                        'low': item[1],
                        'q1': item[2],
                        'median': item[3],
                        'q3': item[4],
                        'high': item[5]
                    }
                elif len(item) == 5:
                    as_dict = {
                        'x': None,
                        'low': item[0],
                        'q1': item[1],
                        'median': item[2],
                        'q3': item[3],
                        'high': item[4]
                    }
                else:
                    raise errors.HighchartsValueError(f'data expects either a 6D or 5D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')

                as_obj = cls.from_dict(as_dict)
                if checkers.is_string(as_obj.x):
                    as_obj.name = as_obj.x
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a BoxPlot Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelrank', None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'marker': as_dict.get('marker', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),

            'box_dash_style': as_dict.get('boxDashStyle', None),
            'high': as_dict.get('high', None),
            'low': as_dict.get('low', None),
            'median': as_dict.get('median', None),
            'median_dash_style': as_dict.get('medianDashStyle', None),
            'q1': as_dict.get('q1', None),
            'q3': as_dict.get('q3', None),
            'stem_dash_style': as_dict.get('stemDashStyle', None),
            'whisker_dash_style': as_dict.get('whiskerDashStyle', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'boxDashStyle': self.box_dash_style,
            'high': self.high,
            'low': self.low,
            'median': self.median,
            'medianDashStyle': self.median_dash_style,
            'q1': self.q1,
            'q3': self.q3,
            'stemDashStyle': self.stem_dash_style,
            'whiskerDashStyle': self.whisker_dash_style,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
