from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors, utility_functions
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.events import PointEvents
from highcharts.series.data.accessibility import DataPointAccessibility


class DataBase(HighchartsMeta):
    """Generic base class for describing a data point."""

    def __init__(self, **kwargs):
        self._accessibility = None
        self._class_name = None
        self._color = None
        self._color_index = None
        self._custom = None
        self._description = None
        self._events = None
        self._id = None
        self._label_rank = None
        self._name = None
        self._selected = None

        self.accessibility = kwargs.get('accessibility', None)
        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.color_index = kwargs.get('color_index', None)
        self.custom = kwargs.get('custom', None)
        self.description = kwargs.get('description', None)
        self.events = kwargs.get('events', None)
        self.id = kwargs.get('id', None)
        self.label_rank = kwargs.get('label_rank', None) or kwargs.get('labelrank', None)
        self.name = kwargs.get('name', None)
        self.selected = kwargs.get('selected', None)

    @property
    def accessibility(self) -> Optional[DataPointAccessibility]:
        """Accessibility options for a data point.

        :rtype: :class:`DataPointAccessibility` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(DataPointAccessibility)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def class_name(self) -> Optional[str]:
        """The additional CSS class name to apply to the data point's graphical elements.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the individual data point. Defaults to :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = utility_functions.validate_color(value)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        point, so its graphic representations are given the class name
        ``highcharts-color-{n}``. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def custom(self) -> Optional[JavaScriptDict]:
        """A reserved subspace to store options and values for customized functionality.

        Here you can add additional data for your own event callbacks and formatter
        callbacks.

        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._custom

    @custom.setter
    @class_sensitive(JavaScriptDict)
    def custom(self, value):
        self._custom = value

    @property
    def description(self) -> Optional[str]:
        """A description of the data point to add to the screen reader information about
        the data point.

        :rtype: :class:`str <python:str>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def events(self) -> Optional[PointEvents]:
        """Event handlers for individual data points.

        :rtype: :class:`PointEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(PointEvents)
    def events(self, value):
        self._events = value

    @property
    def id(self) -> Optional[str]:
        """The id of the data point. Defaults to :obj:`None <python:None>`.

        .. note::

          This can be used (in JavaScript) after render time to get a pointer to the point
          object through ``chart.get()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def label_rank(self) -> Optional[int | float | Decimal]:
        """The rank for this point's data label in the case of collision. Defaults to
        :obj:`None <python:None>`.

        .. note::

          If two data labels are about to overlap, the data label for the point with the
          highest ``label_rank`` will be shown.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._label_rank

    @label_rank.setter
    def label_rank(self, value):
        self._label_rank = validators.numeric(value, allow_empty = True)

    @property
    def name(self) -> Optional[str]:
        """The name to display for the point in data labels, tooltips, in legends, etc.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def selected(self) -> Optional[bool]:
        """If ``True``, indicates that the data point is initially selected. Defaults to
        :obj:`None <python:None>`, which behaves as ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._selected

    @selected.setter
    def selected(self, value):
        if value is None:
            self._selected = None
        else:
            self._selected = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = cls._get_kwargs_from_dict(as_dict)

        return kwargs

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
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
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
