from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class BubbleLegendLabelOptions(HighchartsMeta):
    """Options to configure the bubble legend's labels."""

    def __init__(self, **kwargs):
        self._align = None
        self._allow_overlap = None
        self._class_name = None
        self._format = None
        self._formatter = None
        self._style = None
        self._x = None
        self._y = None

        self.align = kwargs.get('align', None)
        self.allow_overlap = kwargs.get('allow_overlap', None)
        self.class_name = kwargs.get('class_name', None)
        self.format = kwargs.get('format', None)
        self.formatter = kwargs.get('formatter', None)
        self.style = kwargs.get('style', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'legend.bubbleLegend'

    @property
    def align(self) -> Optional[str]:
        """The alignment of the labels relative to the bubble legend. Defaults to
        ``'right'``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :returns: The alignment of the annotation's label.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._align

    @align.setter
    def align(self, value):
        if not value:
            self._align = None
        else:
            value = validators.string(value, allow_empty = True)
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'align must be either "left", "center"'
                                                  f', or "right". Was: {value}')

        self._align = value

    @property
    def allow_overlap(self) -> Optional[bool]:
        """If ``True``, data labels are allowed to overlap each other.

        Defaults to ``False``.

        :returns: Flag indicating whether to allow data labels to overlap.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_overlap

    @allow_overlap.setter
    def allow_overlap(self, value):
        if value is None:
            self._allow_overlap = None
        else:
            self._allow_overlap = bool(value)

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS. Defaults to
        ``'None'``.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def format(self) -> Optional[str]:
        """A format string to apply to the label.

        :returns: The format string to apply to the labels.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format

    @format.setter
    def format(self, value):
        self._format = validators.string(value, allow_empty = True)

    @property
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format the bubble legend's data labels.

        .. hint::

          In the JavaScript callback function, the ``this`` properties available are:

            * ``this.value`` - the bubble value
            * ``this.radius`` - the bubble radius
            * ``this.center`` - the y position of the bubble's center

        :returns: A JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @property
    def style(self) -> Optional[str | dict]:
        """CSS styling to apply to the data labels.

        :rtype: :class:`str <python:str>` or :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        try:
            self._style = validators.dict(value, allow_empty = True)
        except (ValueError, TypeError):
            self._style = validators.string(value, 
                                            allow_empty = True,
                                            coerce_value = True)

    @property
    def x(self) -> Optional[int]:
        """The x position offset of the label relative to the connector. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int]:
        """The y position offset of the label relative to the connector. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'class_name': as_dict.get('className', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'style': as_dict.get('style', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'allowOverlap': self.allow_overlap,
            'className': self.class_name,
            'format': self.format,
            'formatter': self.formatter,
            'style': self.style,
            'x': self.x,
            'y': self.y
        }

        return untrimmed


class BubbleLegendRange(HighchartsMeta):
    """Options for specific range. One range consists of bubble, label and connector."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._color = None
        self._connector_color = None
        self._value = None

        self.border_color = kwargs.get('border_color', None)
        self.color = kwargs.get('color', None)
        self.connector_color = kwargs.get('connector_color', None)
        self.value = kwargs.get('value', None)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the range's border. Defaults to :obj:`None <python:None>`.

        :returns: The color of the range borders.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The main color of the bubble for the range. Defaults to
        :obj:`None <python:None>`.

        :returns: The main color of the bubble legend.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def connector_color(self) -> Optional[str | Gradient | Pattern]:
        """The color applied to the connector for the range. Defaults to
        :obj:`None <python:None>`.

        :returns: The color applied to the connector.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._connector_color

    @connector_color.setter
    def connector_color(self, value):
        from highcharts_core import utility_functions
        self._connector_color = utility_functions.validate_color(value)

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The range size value, similar to the bubble's Z-value. Defaults to
        :obj:`None <python:None>`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        self._value = validators.numeric(value_, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.get('borderColor', None),
            'color': as_dict.get('color', None),
            'connector_color': as_dict.get('connectorColor', None),
            'value': as_dict.get('value', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'color': self.color,
            'connectorColor': self.connector_color,
            'value': self.value
        }

        return untrimmed


class BubbleLegend(HighchartsMeta):
    """The bubble legend is an additional element in legend which presents the scale
    of the bubble series.

    Individual bubble ranges can be defined by user or calculated from series. In the
    case of automatically calculated ranges, a 1px margin of error is permitted.

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._class_name = None
        self._color = None
        self._connector_class_name = None
        self._connector_color = None
        self._connector_distance = None
        self._connector_width = None
        self._enabled = None
        self._labels = None
        self._legend_index = None
        self._max_size = None
        self._min_size = None
        self._ranges = None
        self._size_by = None
        self._size_by_absolute_value = None
        self._z_index = None
        self._z_threshold = None

        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.connector_class_name = kwargs.get('connector_class_name', None)
        self.connector_color = kwargs.get('connector_color', None)
        self.connector_distance = kwargs.get('connector_distance', None)
        self.connector_width = kwargs.get('connector_width', None)
        self.enabled = kwargs.get('enabled', None)
        self.labels = kwargs.get('labels', None)
        self.legend_index = kwargs.get('legend_index', None)
        self.max_size = kwargs.get('max_size', None)
        self.min_size = kwargs.get('min_size', None)
        self.ranges = kwargs.get('ranges', None)
        self.size_by = kwargs.get('size_by', None)
        self.size_by_absolute_value = kwargs.get('size_by_absolute_value', None)
        self.z_index = kwargs.get('z_index', None)
        self.z_threshold = kwargs.get('z_threshold', None)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the ranges border. Can also be defined for an individual range.
        Defaults to :obj:`None <python:None>`.

        :returns: The color of the range borders.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width (in pixels) applied to the range borders. Can also be defined
        for an individual range. Defaults to :obj:`None <python:None>`

        :returns: The border width to apply to the range borders.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The main color of the bubble legend. Applies to ranges, if individual ranges
        are not given a color. Defaults to :obj:`None <python:None>`.

        :returns: The main color of the bubble legend.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def connector_class_name(self) -> Optional[str]:
        """An additional class name to apply to the bubble legend's connector graphical
        elements. This option does not replace default class names of the graphical
        element. Defaults to :obj:`None <python:None>`.

        :returns: The class name applied to the bubble legend's connector graphical
          elements.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._connector_class_name

    @connector_class_name.setter
    def connector_class_name(self, value):
        self._connector_class_name = validators.string(value, allow_empty = True)

    @property
    def connector_color(self) -> Optional[str | Gradient | Pattern]:
        """The color applied to the connector. Can also be defined for individual ranges.
        Defaults to :obj:`None <python:None>`.

        :returns: The color applied to the connector.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._connector_color

    @connector_color.setter
    def connector_color(self, value):
        from highcharts_core import utility_functions
        self._connector_color = utility_functions.validate_color(value)

    @property
    def connector_distance(self) -> Optional[int | float | Decimal]:
        """The length of the connector in pixels. Defaults to
        ``60``.

        .. note::

          If labels are centered, the distance is automatically reduced to ``0``.

        :returns: The border width to apply to the range borders.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._connector_distance

    @connector_distance.setter
    def connector_distance(self, value):
        self._connector_distance = validators.numeric(value, allow_empty = True)

    @property
    def connector_width(self) -> Optional[int | float | Decimal]:
        """The width of the connector in pixels. Defaults to
        ``1``.

        :returns: The border width to apply to the range borders.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._connector_width

    @connector_width.setter
    def connector_width(self, value):
        self._connector_width = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the bubble legend. If ``False``, hides the legend.
        Defaults to ``False``.

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
    def labels(self) -> Optional[BubbleLegendLabelOptions]:
        """Options to configure the bubble legend's labels. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`BubbleLegendLabelOptions` or :obj:`None <python:None>`
        """
        return self._labels

    @labels.setter
    @class_sensitive(BubbleLegendLabelOptions)
    def labels(self, value):
        self._labels = value

    @property
    def legend_index(self) -> Optional[int]:
        """The position of the bubble legend within the legend. Defaults to
        ``0``.

        :returns: The position of the bubble legend within the legend.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._legend_index

    @legend_index.setter
    def legend_index(self, value):
        self._legend_index = validators.integer(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def max_size(self) -> Optional[int | float | Decimal]:
        """The maximum bubble legend range size, in pixels. Defaults to
        ``60``.

        .. note::

          If not specified, the maximum size is determined automatically.

        :returns: The maximum bubble legend range size.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        self._max_size = validators.numeric(value, allow_empty = True)

    @property
    def min_size(self) -> Optional[int | float | Decimal]:
        """The minimum bubble legend range size, in pixels. Defaults to
        ``10``.

        .. note::

          If not specified, the minimum size is determined automatically.

        :returns: The minimum bubble legend range size.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value):
        self._min_size = validators.numeric(value, allow_empty = True)

    @property
    def ranges(self) -> Optional[List[BubbleLegendRange]]:
        """Options for specific range. One range consists of bubble, label and connector.

        Defaults to :obj:`None <python:None>`

        :rtype: :class:`list <python:list>` of :class:`BubbleLegendRange`, or
          :obj:`None <python:None>`
        """
        return self._ranges

    @ranges.setter
    @class_sensitive(BubbleLegendRange, force_iterable = True)
    def ranges(self, value):
        self._ranges = value

    @property
    def size_by(self) -> Optional[str]:
        """Indicates whether the bubble legend range should be represented by the area
        or the width of the bubble. The default
        (``'area'``) corresponds best to the
        human perception of the size of each bubble.

        Accepts one of two possible values:

          * ``'area'``
          * ``'width'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._size_by

    @size_by.setter
    def size_by(self, value):
        if not value:
            self._size_by = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['area', 'width']:
                raise errors.HighchartsValueError(f'size_by expects either "area" or '
                                                  f'"width". Received: {value}')
            self._size_by = value

    @property
    def size_by_absolute_value(self) -> Optional[bool]:
        """If ``True``, the absolute value of z determines the size of the bubble. This
        means that with the default :meth:`BubbleLegend.z_threshold` of ``0``, a bubble of
        value ``-1`` will have the same size as a bubble of value ``1``, while a bubble of
        value 0 will have a smaller size according to :meth:`BubbleLegend.min_size`.

        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._size_by_absolute_value

    @size_by_absolute_value.setter
    def size_by_absolute_value(self, value):
        if value is None:
            self._size_by_absolute_value = None
        else:
            self._size_by_absolute_value = bool(value)

    @property
    def z_index(self) -> Optional[int]:
        """The visual z index of the bubble legend. Defaults to
        ``1``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.integer(value, allow_empty = True)

    @property
    def z_threshold(self) -> Optional[int | float | Decimal]:
        """Ranges with a lower z-value are skipped in the legend. Defaults to
        ``0``.

        :rtype: numeric
        """
        return self._z_threshold

    @z_threshold.setter
    def z_threshold(self, value):
        self._z_threshold = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'connector_class_name': as_dict.get('connectorClassName', None),
            'connector_color': as_dict.get('connectorColor', None),
            'connector_distance': as_dict.get('connectorDistance', None),
            'connector_width': as_dict.get('connectorWidth', None),
            'enabled': as_dict.get('enabled', None),
            'labels': as_dict.get('labels', None),
            'legend_index': as_dict.get('legendIndex', None),
            'max_size': as_dict.get('maxSize', None),
            'min_size': as_dict.get('minSize', None),
            'ranges': as_dict.get('ranges', None),
            'size_by': as_dict.get('sizeBy', None),
            'size_by_absolute_value': as_dict.get('sizeByAbsoluteValue', None),
            'z_index': as_dict.get('zIndex', None),
            'z_threshold': as_dict.get('zThreshold', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'color': self.color,
            'connectorClassName': self.connector_class_name,
            'connectorColor': self.connector_color,
            'connectorDistance': self.connector_distance,
            'connectorWidth': self.connector_width,
            'enabled': self.enabled,
            'labels': self.labels,
            'legendIndex': self.legend_index,
            'maxSize': self.max_size,
            'minSize': self.min_size,
            'ranges': self.ranges,
            'sizeBy': self.size_by,
            'sizeByAbsoluteValue': self.size_by_absolute_value,
            'zIndex': self.z_index,
            'zThreshold': self.z_threshold
        }

        return untrimmed
