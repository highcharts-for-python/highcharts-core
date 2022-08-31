from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.series.data.bar import BarCartesianData
from highcharts.plot_options.bullet import TargetOptions


class BulletData(BarCartesianData):
    """Variant of :class:`BarCartesianData` which is used for data points in a bullet
    chart."""

    def __init__(self, **kwargs):
        self._target = None
        self._target_options = None

        self.target = kwargs.pop('target', None)
        self.target_options = kwargs.pop('target_options', None)

        super().__init__(**kwargs)

    @property
    def target(self) -> Optional[int | float | Decimal]:
        """The target value of a data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._target

    @target.setter
    def target(self, value):
        self._target = validators.numeric(value, allow_empty = True)

    @property
    def target_options(self) -> Optional[TargetOptions]:
        """Options related to the look and positioning of the
        :meth:`target <BulletData.target>`.

        :rtype: :class:`TargetOptions` or :obj:`None <python:None>`
        """
        return self._target_options

    @target_options.setter
    @class_sensitive(TargetOptions)
    def target_options(self, value):
        self._target_options = value

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`BulletData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`BulletData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'BulletData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            elif checkers.is_iterable(item):
                if len(item) == 3:
                    as_dict = {
                        'x': item[0],
                        'y': item[1],
                        'target': item[2]
                    }
                elif len(item) == 2:
                    as_dict = {
                        'x': None,
                        'y': item[0],
                        'target': item[1]
                    }
                else:
                    raise errors.HighchartsValueError(f'data expects either a 3D or 2D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')

                as_obj = cls.from_dict(as_dict)
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Bullet Data Point or be '
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
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'point_width': as_dict.pop('pointWidth', None),

            'target': as_dict.pop('target', None),
            'target_options': as_dict.pop('targetOptions', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'target': self.target,
            'targetOptions': self.target_options
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
