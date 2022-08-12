from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class DataClass(HighchartsMeta):
    """Definition of ranges for use in a choropleth map."""

    def __init__(self, **kwargs):
        self._color = None
        self._from_ = None
        self._name = None
        self._to = None

        self.color = kwargs.pop('color', None)
        self.from_ = kwargs.pop('from_', None)
        self.name = kwargs.pop('name', None)
        self.to = kwargs.pop('to', None)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the data class. Defaults to :obj:`None <python:None>`.

        If :obj:`None <python:None>`, the color is pulled from the global or
        chart-specific colors array.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def from_(self) -> Optional[int | float | Decimal]:
        """The point value at which the data class' value range begins. Defaults to
        :obj:`None <python:None>`.

        .. note::

          The range of each :class:`DataClass` is closed at both ends, but can be
          overridden by a subsequent :class:`DataClass` instance included in the
          :meth:`ColorAxis.data_classes` collection.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        self._from_ = validators.numeric(value, allow_empty = True)

    @property
    def name(self) -> Optional[str]:
        """The name of the data class as it should apear in the legend. Defaults to
        :obj:`None <python:None>`.

        If :obj:`None <python:None>`, it is automatically created based on the
        :meth:`from_ <DataClass.from_>` and :meth:`to <DataClass.to>` values.

        .. hint::

          For full programmatic control, :meth:`Legend.label_formatter` can be used. In
          the formatter (JavaScript) function, ``this.from`` and ``this.to`` can be
          accessed.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def to(self) -> Optional[int | float | Decimal]:
        """The point value at which the data class' value range ends. Defaults to
        :obj:`None <python:None>`.

        .. note::

          The range of each :class:`DataClass` is closed at both ends, but can be
          overridden by a subsequent :class:`DataClass` instance included in the
          :meth:`ColorAxis.data_classes` collection.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.pop('color', None),
            'from_': as_dict.pop('from', None),
            'name': as_dict.pop('name', None),
            'to': as_dict.pop('to', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'color': self.color,
            'from': self.from_,
            'name': self.name,
            'to': self.to
        }

        return untrimmed
