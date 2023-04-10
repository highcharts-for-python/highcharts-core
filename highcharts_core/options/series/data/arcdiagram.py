from typing import Optional
from decimal import Decimal
from collections import UserDict

from validator_collection import validators, checkers

from highcharts_core import utility_functions, constants
from highcharts_core.options.series.data.base import DataBase
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class ArcDiagramData(DataBase):
    """The definition of a data point for use in an :class:`ArcDiagramSeries`."""

    def __init__(self, **kwargs):
        self._from_ = None
        self._to = None
        self._weight = None

        self.from_ = kwargs.get('from_', None)
        self.to = kwargs.get('to', None)
        self.weight = kwargs.get('weight', None)

        super().__init__(**kwargs)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color for the individual link. Defaults to :obj:`None <python:None>`, which
        sets the link color the same as the node it extends from.

        .. hint::

          The ``series.fillOpacity`` option also applies to the points, so when setting a
          specific link color, consider setting the ``fillOpacity`` to 1.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        else:
            self._color = utility_functions.validate_color(value)

    @property
    def from_(self) -> Optional[str]:
        """The :meth:`ArcDiagramData.id` or :meth:`ArcDiagramData.name` of the node that
        the link runs from. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        self._from_ = validators.string(value, allow_empty = True)

    @property
    def to(self) -> Optional[str]:
        """The :meth:`ArcDiagramData.id` or :meth:`ArcDiagramData.name` of the node that
        the link runs to. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.string(value, allow_empty = True)

    @property
    def weight(self) -> Optional[int | float | Decimal]:
        """The weight of the link between the nodes. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = validators.numeric(value, allow_empty = True)

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
            if checkers.is_type(item, 'SinglePointData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls(y = None)
            elif checkers.is_numeric(item):
                as_obj = cls(y = item)
            elif checkers.is_iterable(item, forbid_literals = (str, bytes, dict, UserDict)):
                if len(item) == 3:
                    as_obj = cls(from_ = item[0],
                                 to = item[1],
                                 weight = item[2])
                else:
                    raise errors.HighchartsValueError(f'each data point supplied must either '
                                                    f'be an Arc Diagram Data Point or be '
                                                    f'coercable to one. Could not coerce: '
                                                    f'{item}')
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be an Arc Diagram Data Point or be '
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

            'from_': as_dict.get('from', None),
            'to': as_dict.get('to', None),
            'weight': as_dict.get('weight', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'from': self.from_,
            'to': self.to,
            'weight': self.weight,

            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,
        }

        return untrimmed
