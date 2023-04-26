from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.metaclasses import HighchartsMeta


class SonificationGrouping(HighchartsMeta):
    """Options for grouping data points together when sonifying. 
    
    This allows for the visual presentation to contain more points than what is being played. 
    
    .. tip::
    
      If not enabled, all visible / uncropped points are played.
      
    """
    def __init__(self, **kwargs):
        self._algorithm = None
        self._enabled = None
        self._group_timespan = None
        self._prop = None
        
        self.algorithm = kwargs.get('algorithm', None)
        self.enabled = kwargs.get('enabled', None)
        self.group_timespan = kwargs.get('group_timespan', None)
        self.prop = kwargs.get('prop', None)
        
    @property
    def algorithm(self) -> Optional[str]:
        """The grouping algorithm, which determines which points to keep when grouping a set of points together. Accepts
        ``'minmax'``, ``'first'``, ``'last'``, ``'middle'``, and ``'firstLast'``.
        
        By default ``'minmax'`` is used, which keeps both the minimum and maximum points.

        The other algorithms will either keep the first point in the group (time wise), last point, middle point, or both the first and the last point.

        The timing of the resulting point(s) is then adjusted to play evenly, regardless of its original position within the group.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._algorithm
    
    @algorithm.setter
    def algorithm(self, value):
        if not value:
            self._algorithm = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['minmax', 'first', 'last', 'middle', 'firstlast']:
                raise errors.HighchartsValueError(f'.algorithm expects either "minmax", "first", '
                                                  f'"last", "middle", or "firstLast". Received: '
                                                  f'"{value}"')
            if value == 'firstlast':
                value = 'firstLast'
            
            self._algorithm = value
            
    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, points should be grouped. Defaults to ``True``.
        
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
    def group_timespan(self) -> Optional[int | float | Decimal]:
        """The size of each group, expressed in milliseconds. Audio events closer than this value are grouped together.
        Defaults to ``15``.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_timespan
    
    @group_timespan.setter
    def group_timespan(self, value):
        self._group_timespan = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)
    
    @property
    def prop(self) -> Optional[str]:
        """The data point property to use when evaluating which points to keep in the group. Defaults to ``'y'``,
        which means that when the ``'minmax'`` algorithm is applied, the two points with the lowest and highest ``'y'``
        values will be kept and the others not played.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._prop
    
    @prop.setter
    def prop(self, value):
        self._prop = validators.string(value, allow_empty = True)
        
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'algorithm': as_dict.get('algorithm', None),
            'enabled': as_dict.get('enabled', None),
            'group_timespan': as_dict.get('groupTimespan', None),
            'prop': as_dict.get('prop', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'algorithm': self.algorithm,
            'enabled': self.enabled,
            'groupTimespan': self.group_timespan,
            'prop': self.prop,
        }

        return untrimmed
