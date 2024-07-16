from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class BorderRadius(HighchartsMeta):
    """Precise configuration of Border Radius behavior."""

    def __init__(self, **kwargs):
        self._radius = None
        self._scope = None
        self._where = None
        
        self.radius = kwargs.get('radius', None)
        self.scope = kwargs.get('scope', None)
        self.where = kwargs.get('where', None)
        
    @property
    def radius(self) -> Optional[str | int | float | Decimal]:
        """The border radius. 
        
        A number signifies pixels. 
        
        A percentage string, like for example 50%, signifies a relative size. 
        
        .. note::

          For columns this is relative to the column width, for pies it is relative to the radius 
          and the inner radius.
        
        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value is None:
            self._radius = None
        else:
            try:
                self._radius = validators.numeric(value, allow_empty = None)
            except (ValueError, TypeError):
                if not isinstance(value, str):
                    raise errors.HighchartsValueError(f'radius expects a number or string. '
                                                      f'Received: {value.__class__.__name__}')
                self._radius = value
                
    @property
    def scope(self) -> Optional[str]:
        """The scope of the rounding for column charts. 
        
        .. note::
        
          In a stacked column chart:
          
            * the value ``'point'`` means each single point will get rounded corners
            * the value ``'stack'`` means the rounding will apply to the full stack, so that 
              only points close to the top or bottom will receive rounding.
              
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._scope
    
    @scope.setter
    def scope(self, value):
        if not value:
            self._scope = None
        else:
            value = value.lower()
            if value not in ['point', 'stack']:
                raise errors.HighchartsValueError(f'scope expects either "point" or "stack". '
                                                  f'Received: {value}')
            self._scope = value

    @property
    def where(self) -> Optional[str]:
        """For column charts, where in the point or stack to apply rounding. 
        
        * The value ``'end'`` means only those corners at the point value will be rounded, 
          leaving the corners at the base or threshold unrounded. This is the most intuitive behaviour. 
        * The value ``'all'`` means the base will be rounded, in addition to the corners at the point value.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._where
    
    @where.setter
    def where(self, value):
        if not value:
            self._where = None
        else:
            value = value.lower()
            if value not in ['end', 'all']:
                raise errors.HighchartsValueError(f'where expects either "end" or "all". '
                                                  f'Received: {value}')
            self._where = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'radius': as_dict.get('radius', None),
            'scope': as_dict.get('scope', None),
            'where': as_dict.get('where', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'radius': self.radius,
            'scope': self.scope,
            'where': self.where
        }

        return untrimmed
