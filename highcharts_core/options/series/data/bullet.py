from typing import Optional, List, Dict
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.data.bar import BarData
from highcharts_core.options.series.data.cartesian import CartesianDataCollection
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
    def from_list(cls, value):
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
                if checkers.is_string(as_obj.x) and not as_obj.name:
                    as_obj.name = as_obj.x
                    as_obj.x = None
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Bullet Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return BulletDataCollection.from_ndarray(value)

    @classmethod
    def _get_props_from_array(cls, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        prop_list = {
            None: ['x', 'y', 'target', 'name'],
            3: ['x', 'y', 'target'],
            2: ['y', 'target'],
        }
        return cls._get_props_from_array_helper(prop_list, length)

    def to_array(self, force_object = False) -> List | Dict:
        """Generate the array representation of the data point (the inversion 
        of 
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`).
        
        .. warning::
        
          If the data point *cannot* be serialized to a JavaScript array,
          this method will instead return the untrimmed :class:`dict <python:dict>`
          representation of the data point as a fallback.
          
        :param force_object: if ``True``, forces the return of the instance's
          untrimmed :class:`dict <python:dict>` representation. Defaults to ``False``.
        :type force_object: :class:`bool <python:bool>`

        :returns: The array representation of the data point.
        :rtype: :class:`list <python:list>` of values or :class:`dict <python:dict>`
        """
        if self.requires_js_object or force_object:
            return self._to_untrimmed_dict()
        
        if self.x is not None:
            x = self.x
        elif self.name is not None:
            x = self.name
        else:
            x = constants.EnforcedNull
            
        if self.y is not None:
            y = self.y
        else:
            y = constants.EnforcedNull
        
        if self.target is not None:
            target = self.target
        else:
            target = constants.EnforcedNull
        
        if self.x is None and self.name is None:
            return [y, target]

        return [x, y, target]

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


class BulletDataCollection(CartesianDataCollection):
    """A collection of :class:`BulletData` objects.

    .. note::
    
      When serializing to JS literals, if possible, the collection is serialized to a primitive
      array to boost performance within Python *and* JavaScript. However, this may not always be
      possible if data points have non-array-compliant properties configured (e.g. adjusting their 
      style, names, identifiers, etc.). If serializing to a primitive array is not possible, the
      results are serialized as JS literal objects.

    """

    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return BulletData
