from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.series.data.single_point import SinglePointData
from highcharts.plot_options.drag_drop import DragDropOptions
from highcharts.utility_classes.data_labels import DataLabel


class PieData(SinglePointData):
    """Data point that can be represented as a slice on a :class:`PieSeries` with a single
    ``y`` value."""

    def __init__(self, **kwargs):
        self._sliced = None

        self.sliced = kwargs.pop('sliced', None)

        super().__init__(**kwargs)

    @property
    def sliced(self) -> Optional[bool]:
        """If ``True``, displays the slice offset from the center. Defaults to
        :obj:`None <python:None>`

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._sliced

    @sliced.setter
    def sliced(self, value):
        if value is None:
            self._sliced = None
        else:
            self._sliced = bool(value)

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
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'sliced': as_dict.pop('sliced', None),
            'y': as_dict.pop('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'sliced': self.sliced,
        }

        parent_as_dict = super()._to_untrimmed_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class VariablePieData(PieData):
    """Variant of :class:`PieData` suited for :class:`VariablePieSeries`."""

    def __init__(self, **kwargs):
        self._sliced = None
        self._z = None

        self.sliced = kwargs.pop('sliced', None)
        self.z = kwargs.pop('z', None)

        super().__init__(**kwargs)

    @property
    def z(self) -> Optional[int | float | Decimal | type(None) | constants.EnforcedNullType]:
        """The position of the data point on the Z-axis. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._z

    @z.setter
    def z(self, value):
        if value is None or isinstance(value, constants.EnforcedNullType):
            self._z = None
        else:
            self._z = validators.numeric(value)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`VariablePieData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`PieData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'VariablePieData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls(y = None,
                             z = None)
            elif len(item) == 2:
                as_obj = cls(y = item[0],
                             z = item[1])
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Variable Pie Data Point or be '
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
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'sliced': as_dict.pop('sliced', None),
            'y': as_dict.pop('y', None),

            'z': as_dict.pop('z', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'z': self.z,
        }

        parent_as_dict = super()._to_untrimmed_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
