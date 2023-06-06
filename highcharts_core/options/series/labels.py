from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class Box(HighchartsMeta):
    """Containing the position of a box that should be avoided by labels."""

    def __init__(self, **kwargs):
        self._bottom = None
        self._left = None
        self._right = None
        self._top = None

        self.bottom = kwargs.get('bottom', None)
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)
        self.top = kwargs.get('top', None)

    @property
    def bottom(self) -> Optional[int | float | Decimal]:
        """Bottom Position

        :rtype: numeric
        """
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        self._bottom = validators.numeric(value)

    @property
    def left(self) -> Optional[int | float | Decimal]:
        """Left Position

        :rtype: numeric
        """
        return self._left

    @left.setter
    def left(self, value):
        self._left = validators.numeric(value)

    @property
    def right(self) -> Optional[int | float | Decimal]:
        """Right Position

        :rtype: numeric
        """
        return self._right

    @right.setter
    def right(self, value):
        self._right = validators.numeric(value)

    @property
    def top(self) -> Optional[int | float | Decimal]:
        """Top Position

        :rtype: numeric
        """
        return self._top

    @top.setter
    def top(self, value):
        self._top = validators.numeric(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'bottom': as_dict.get('bottom', None),
            'left': as_dict.get('left', None),
            'right': as_dict.get('right', None),
            'top': as_dict.get('top', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'bottom': self.bottom,
            'left': self.left,
            'right': self.right,
            'top': self.top
        }

        return untrimmed


class SeriesLabel(HighchartsMeta):
    """Series labels are placed as close to the series as possible in a natural way,
    seeking to avoid other series.

    The goal of this feature is to make the chart more easily readable, like if a human
    designer placed the labels in the optimal position.
    """

    def __init__(self, **kwargs):
        self._boxes_to_avoid = None
        self._connector_allowed = None
        self._connector_neighbour_distance = None
        self._enabled = None
        self._format = None
        self._formatter = None
        self._max_font_size = None
        self._min_font_size = None
        self._on_area = None
        self._style = None

        self.boxes_to_avoid = kwargs.get('boxes_to_avoid', None)
        self.connector_allowed = kwargs.get('connector_allowed', None)
        self.connector_neighbour_distance = kwargs.get('connector_neighbour_distance',
                                                       None)
        self.enabled = kwargs.get('enabled', None)
        self.format = kwargs.get('format', None)
        self.formatter = kwargs.get('formatter', None)
        self.max_font_size = kwargs.get('max_font_size', None)
        self.min_font_size = kwargs.get('min_font_size', None)
        self.on_area = kwargs.get('on_area', None)
        self.style = kwargs.get('style', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.boxplot.dragDrop'

    @property
    def boxes_to_avoid(self) -> Optional[List[Box]]:
        """An array of boxes to avoid when laying out the labels.
        Each item has a :meth:`left <Box.left>`, :meth:`right <Box.right>`,
        :meth:`top <Box.top>`, and :meth:`bottom <Box.bottom>` property.

        :rtype: :class:`list <python:list>` of :class:`Box`
        """
        return self._boxes_to_avoid

    @boxes_to_avoid.setter
    @class_sensitive(Box, force_iterable = True)
    def boxes_to_avoid(self, value):
        self._boxes_to_avoid = value

    @property
    def connector_allowed(self) -> Optional[bool]:
        """Allow labels to be placed distant to the graph if necessary, and draw a
        connector line to the graph. Defaults to ``False``.

        .. warning::

          Setting this option to ``True`` may decrease the performance significantly,
          since the algorithm with systematically search for open spaces in the whole plot
          area. Visually, it may also result in a more cluttered chart, though more of the
          series will be labeled.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._connector_allowed

    @connector_allowed.setter
    def connector_allowed(self, value):
        if value is None:
            self._connector_allowed = None
        else:
            self._connector_allowed = bool(value)

    @property
    def connector_neighbour_distance(self) -> Optional[int | float | Decimal]:
        """If the label is closer than this to a neighbour graph, draw a connector.
        Defaults to ``24``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._connector_neighbour_distance

    @connector_neighbour_distance.setter
    def connector_neighbour_distance(self, value):
        self._connector_neighbour_distance = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enable the series labels for the series. Defaults to ``True``.

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
    def format(self) -> Optional[str]:
        """A format string for the label, with support for a subset of HTML.

        Variables are enclosed by curly brackets. Available variables are ``name``,
        ``options.xxx``, ``color``, and other members from the ``series`` object.
        Use this option also to set a static text for the label.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format

    @format.setter
    def format(self, value):
        self._format = validators.string(value, allow_empty = True)

    @property
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format each of the series' labels.

        The ``this`` keyword refers to the ``series`` object. By default the formatter is
        :obj:`None <python:None>` and the ``series.name`` is rendered.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @property
    def max_font_size(self) -> Optional[int | float | Decimal | constants.EnforcedNullType]:
        """For area-like series, allow the font size to vary so that small areas get a
        smaller font size. The default applies this effect to area-like series but not
        line-like series.

        Defaults to ``EnforcedNull``.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._max_font_size

    @max_font_size.setter
    def max_font_size(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._max_font_size = constants.EnforcedNull
        else:
            self._max_font_size = validators.numeric(value, allow_empty = True)

    @property
    def min_font_size(self) -> Optional[int | float | Decimal | constants.EnforcedNullType]:
        """For area-like series, allow the font size to vary so that small areas get a
        smaller font size. The default applies this effect to area-like series but not
        line-like series.

        Defaults to ``EnforcedNull``.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._min_font_size

    @min_font_size.setter
    def min_font_size(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._min_font_size = constants.EnforcedNull
        else:
            self._min_font_size = validators.numeric(value, allow_empty = True)

    @property
    def on_area(self) -> Optional[bool | constants.EnforcedNullType]:
        """Draw the label on the area of an area series.

        By default it is drawn on the area. Set it to ``False`` to draw it next to the
        graph instead.

        :rtype: :class:`bool <python:bool>` or :class:`EnforcedNullType` or
          :obj:`None <python:None>`
        """
        return self._on_area

    @on_area.setter
    def on_area(self, value):
        if value is None:
            self._on_area = None
        elif value is False:
            self._on_area = False
        elif isinstance(value, constants.EnforcedNullType):
            self._on_area = constants.EnforcedNull
        else:
            self._on_area = bool(value)

    @property
    def style(self) -> Optional[dict | str]:
        """Styles for the series label. The color defaults to the series color, or a
        contrast color if ``on_area``.

        :rtype: :class:`dict <python:dict>` or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        try:
            self._style = validators.dict(value, allow_empty = True)
        except (ValueError, TypeError):
            self._style = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'boxes_to_avoid': as_dict.get('boxesToAvoid', None),
            'connector_allowed': as_dict.get('connectorAllowed', None),
            'connector_neighbour_distance': as_dict.get('connectorNeighbourDistance',
                                                        None),
            'enabled': as_dict.get('enabled', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'max_font_size': as_dict.get('maxFontSize', None),
            'min_font_size': as_dict.get('minFontSize', None),
            'on_area': as_dict.get('onArea', None),
            'style': as_dict.get('style', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'boxesToAvoid': self.boxes_to_avoid,
            'connectorAllowed': self.connector_allowed,
            'connectorNeighbourDistance': self.connector_neighbour_distance,
            'enabled': self.enabled,
            'format': self.format,
            'formatter': self.formatter,
            'maxFontSize': self.max_font_size,
            'minFontSize': self.min_font_size,
            'onArea': self.on_area,
            'style': self.style
        }

        return untrimmed
