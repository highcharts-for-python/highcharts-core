from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.data.base import DataBase
from highcharts_core.options.plot_options.drag_drop import DragDropOptions
from highcharts_core.utility_classes.data_labels import DataLabel
from highcharts_core.utility_classes.buttons import CollapseButtonConfiguration


class TreegraphData(DataBase):
    """Data point that can feature a ``parent``."""

    def __init__(self, **kwargs):
        self._collapse_button = None
        self._collapsed = None
        self._color_value = None
        self._data_labels = None
        self._drag_drop = None
        self._drilldown = None
        self._parent = None

        self.color_value = kwargs.get('color_value', None)
        self.data_labels = kwargs.get('data_labels', None)
        self.drag_drop = kwargs.get('drag_drop', None)
        self.drilldown = kwargs.get('drilldown', None)
        self.parent = kwargs.get('parent', None)

        super().__init__(**kwargs)

    @property
    def collapse_button(self) -> Optional[CollapseButtonConfiguration]:
        """Options applied to the Collapse Button, which is the small button that indicates the node is collapsible.
        
        :rtype: :class:`CollapseButtonConfiguration <highcharts_core.utility_classes.buttons.CollapseButtonConfiguration>` 
          or :obj:`None <python:None>`
        """
        return self._collapse_button
    
    @collapse_button.setter
    @class_sensitive(CollapseButtonConfiguration)
    def collapse_button(self, value):
        self._collapse_button = value

    @property
    def collapsed(self) -> Optional[bool]:
        """If ``True``, the point's children should be hidden. Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._collapsed
    
    @property
    def color_value(self) -> Optional[int]:
        """If :meth:`SunburstOptions.color_axis` is set, this property determines which
        color should be applied to the data point from the scale of the color axis.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_value

    @color_value.setter
    def color_value(self, value):
        self._color_value = validators.integer(value, allow_empty = True)

    @property
    def data_labels(self) -> Optional[DataLabel]:
        """Individual data label for the data point.

        :rtype: :class:`DataLabel` or :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    @class_sensitive(DataLabel)
    def data_labels(self, value):
        self._data_labels = value

    @property
    def drag_drop(self) -> Optional[DragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(DragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def drilldown(self) -> Optional[str]:
        """The :meth:`id <SeriesBase.id>` of a series in the ``drilldown.series`` array
        to use as a drilldown destination for this point. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._drilldown

    @drilldown.setter
    def drilldown(self, value):
        self._drilldown = validators.string(value, allow_empty = True)

    @property
    def parent(self) -> Optional[str]:
        """The :meth:`id <SunburstData.id>` of the parent data point. If no points match
        the value provided, or if set to :obj:`None <python:None>`, the parent will be set
        to the root. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = validators.string(value, allow_empty = True)

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
            if checkers.is_type(item, 
                                'TreegraphData') or checkers.is_iterable(item, 
                                                                         forbid_literals = (str, bytes, dict)):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Treemap Data Point or be '
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

            'collapse_button': as_dict.get('collapseButton', None),
            'color_value': as_dict.get('colorValue', None),
            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'parent': as_dict.get('parent', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'collapseButton': self.collapse_button,
            'collapsed': self.collapsed,
            'colorValue': self.color_value,
            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'parent': self.parent,

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
            'selected': self.selected
        }

        return untrimmed
