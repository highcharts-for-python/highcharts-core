from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.data.bar import BarData
from highcharts_core.options.plot_options.bullet import TargetOptions


class BulletData(BarData):
    """Variant of :class:`BarCartesianData` which is used for data points in a bullet
    chart."""

    def __init__(self, **kwargs):
        self._target = None
        self._target_options = None

        self.target = kwargs.get('target', None)
        self.target_options = kwargs.get('target_options', None)

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
                if checkers.is_string(as_obj.x):
                    as_obj.name = as_obj.x
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

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'dash_style': as_dict.get('dashStyle', None),
            'point_width': as_dict.get('pointWidth', None),

            'target': as_dict.get('target', None),
            'target_options': as_dict.get('targetOptions', None),

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
