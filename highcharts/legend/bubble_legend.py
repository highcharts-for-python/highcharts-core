from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class BubbleLegendLabelOptions(HighchartsMeta):
    """Options to configure the bubble legend's labels."""

    def __init__(self, **kwargs):
        self._align = None
        self._allow_overlap = False
        self._class_name = None
        self._format = None
        self._formatter = None
        self._style = None
        self._x = None
        self._y = None

        self.align = kwargs.pop('align', constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('align'))
        self.allow_overlap = kwargs.pop('allow_overlap', constants.BUBBLE_LEGEND.get('label', {}).get('allow_overlap'))
        self.class_name = kwargs.pop('class_name', constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('class_name'))
        self.format = kwargs.pop('format', constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('format'))
        self.formatter = kwargs.pop('formatter', None)
        self.style = kwargs.pop('style', constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('style'))
        self.x = kwargs.pop('x', constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('x'))
        self.y = kwargs.pop('y', constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('y'))

    @property
    def align(self) -> str:
        f"""The alignment of the labels relative to the bubble legend. Defaults to
        ``'{constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('align')}'``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :returns: The alignment of the annotation's label.
        :rtype: :class:`str <python:str>`
        """
        return self._align

    @align.setter
    def align(self, value):
        value = validators.string(value, allow_empty = False)
        value = value.lower()
        if value not in ['left', 'center', 'right']:
            raise errors.HighchartsValueError(f'align must be either "left", "center", or'
                                              f' "right". Was: {value}')

        self._align = value

    @property
    def allow_overlap(self) -> bool:
        """If ``True``, data labels are allowed to overlap each other.

        Defaults to ``False``.

        :returns: Flag indicating whether to allow data labels to overlap.
        :rtype: :class:`bool <python:bool>`
        """
        return self._allow_overlap

    @allow_overlap.setter
    def allow_overlap(self, value):
        self._allow_overlap = bool(value)

    @property
    def class_name(self) -> Optional[str]:
        f"""A classname to apply styling using CSS. Defaults to
        ``'{constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('class_name')}'``.

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
    def formatter(self) -> Optional[str]:
        """JavaScript callback function to format the bubble legend's data labels.

        .. hint::

          In the JavaScript callback function, the ``this`` properties available are:

            * ``this.value`` - the bubble value
            * ``this.radius`` - the bubble radius
            * ``this.center`` - the y position of the bubble's center

        :returns: A JavaScript callback function.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    def formatter(self, value):
        self._formatter = validators.string(value, allow_empty = True)

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the data labels.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @property
    def x(self) -> int:
        f"""The x position offset of the label relative to the connector. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('x')}``.

        :rtype: numeric
        """
        return self._x

    @x.setter
    def x(self, value):
        value = validators.numeric(value, allow_empty = True)
        if value is None:
            self._x = 0
        else:
            self._x = value

    @property
    def y(self) -> int:
        f"""The y position offset of the label relative to the connector. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('y')}``.

        :rtype: numeric
        """
        return self._y

    @y.setter
    def y(self, value):
        value = validators.numeric(value, allow_empty = True)
        if value is None:
            self._y = 0
        else:
            self._y = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.pop('align',
                                 constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('align')),
            'allow_overlap': as_dict.pop('allowOverlap',
                                         constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('allow_overlap')),
            'class_name': as_dict.pop('className',
                                      constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('class_name')),
            'format': as_dict.pop('format',
                                  constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('format')),
            'formatter': as_dict.pop('formatter', None),
            'style': as_dict.pop('style',
                                 constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('style')),
            'x': as_dict.pop('x',
                             constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('x')),
            'y': as_dict.pop('y',
                             constants.DEFAULT_BUBBLE_LEGEND.get('labels', {}).get('y'))
        }

        return cls(**kwargs)

    def to_dict(self):
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
        as_dict = self.trim_dict(untrimmed)

        return as_dict


class BubbleLegendRange(HighchartsMeta):
    """Options for specific range. One range consists of bubble, label and connector."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._color = None
        self._connector_color = None
        self._value = None

        self.border_color = kwargs.pop('border_color', None)
        self.color = kwargs.pop('color', None)
        self.connector_color = kwargs.pop('connector_color', None)
        self.value = kwargs.pop('value', None)

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
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
        if not value:
            self._connector_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._connector_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._connector_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._connector_color = Gradient.from_dict(value)
                else:
                    self._connector_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._connector_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._connector_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._connector_color = Pattern.from_dict(value)
                else:
                    self._connector_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._connector_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
    def from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.pop('borderColor', None),
            'color': as_dict.pop('color', None),
            'connector_color': as_dict.pop('connectorColor', None),
            'value': as_dict.pop('value', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'border_color': self.border_color,
            'color': self.color,
            'connector_color': self.connector_color,
            'value': self.value
        }

        return self.trim_dict(untrimmed)



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
        self._size_by_absolute_value = False
        self._z_index = None
        self._z_threshold = None

        self.border_color = kwargs.pop('border_color',
                                       constants.DEFAULT_BUBBLE_LEGEND.get('border_color'))
        self.border_width = kwargs.pop('border_width',
                                       constants.DEFAULT_BUBBLE_LEGEND.get('border_width'))
        self.class_name = kwargs.pop('class_name',
                                     constants.DEFAULT_BUBBLE_LEGEND.get('class_name'))
        self.color = kwargs.pop('color', constants.DEFAULT_BUBBLE_LEGEND.get('color'))
        self.connector_class_name = kwargs.pop('connector_class_name',
                                               constants.DEFAULT_BUBBLE_LEGEND.get('connector_class_name'))
        self.connector_color = kwargs.pop('connector_color',
                                          constants.DEFAULT_BUBBLE_LEGEND.get('connector_color'))
        self.connector_distance = kwargs.pop('connector_distance',
                                             constants.DEFUALT_BUBBLE_LEGEND.get('connector_distance'))
        self.connector_width = kwargs.pop('connector_width',
                                          constants.DEFAULT_BUBBLE_LEGEND.get('connector_width'))
        self.enabled = kwargs.pop('enabled',
                                  constants.DEFAULT_BUBBLE_LEGEND.get('enabled'))
        self.labels = kwargs.pop('labels', None)
        self.legend_index = kwargs.pop('legend_index',
                                       constants.DEFAULT_BUBBLE_LEGEND.get('legend_index'))
        self.max_size = kwargs.pop('max_size',
                                   constants.DEFAULT_BUBBLE_LEGEND.get('max_size'))
        self.min_size = kwargs.pop('min_size',
                                   constants.DEFAULT_BUBBLE_LEGEND.get('min_size'))
        self.ranges = kwargs.pop('ranges', None)
        self.size_by = kwargs.pop('size_by',
                                  constants.DEFAULT_BUBBLE_LEGEND.get('size_by'))
        self.size_by_absolute_value = kwargs.pop('size_by_absolute_value',
                                                 constants.DEFAULT_BUBBLE_LEGEND.get('size_by_absolute_value'))
        self.z_index = kwargs.pop('z_index',
                                  constants.DEFAULT_BUBBLE_LEGEND.get('z_index'))
        self.z_threshold = kwargs.pop('z_threshold',
                                      constants.DEFAULT_BUBBLE_LEGEND.get('z_threshold'))

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
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

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
        if not value:
            self._connector_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._connector_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._connector_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._connector_color = Gradient.from_dict(value)
                else:
                    self._connector_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._connector_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._connector_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._connector_color = Pattern.from_dict(value)
                else:
                    self._connector_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._connector_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def connector_distance(self) -> Optional[int | float | Decimal]:
        f"""The length of the connector in pixels. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('connector_distance', 60)}``.

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
        f"""The width of the connector in pixels. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('connector_width', 1)}``.

        :returns: The border width to apply to the range borders.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._connector_width

    @connector_width.setter
    def connector_width(self, value):
        self._connector_width = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> bool:
        f"""If ``True``, displays the bubble legend. If ``False``, hides the legend.
        Defaults to ``{constants.DEFAULT_LEGEND.get('enabled')}``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
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
        f"""The position of the bubble legend within the legend. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('legend_index', 0)}``.

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
        f"""The maximum bubble legend range size, in pixels. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('max_size', 60)}``.

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
        f"""The minimum bubble legend range size, in pixels. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('min_size', 10)}``.

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
    def size_by(self) -> str:
        f"""Indicates whether the bubble legend range should be represented by the area
        or the width of the bubble. The default
        (``'{constants.DEFAULT_BUBBLE_LEGEND.get('size_by')}'``) corresponds best to the
        human perception of the size of each bubble.

        Accepts one of two possible values:

          * ``'area'``
          * ``'width'``

        :rtype: :class:`str <python:str>`
        """
        return self._size_by

    @size_by.setter
    def size_by(self, value):
        if not value:
            self._size_by = constants.DEFAULT_BUBBLE_LEGEND.get('size_by', 'area')
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['area', 'width']:
                raise errors.HighchartsValueError(f'size_by expects either "area" or '
                                                  f'"width". Received: {value}')
            self._size_by = value

    @property
    def size_by_absolute_value(self) -> bool:
        """If ``True``, the absolute value of z determines the size of the bubble. This
        means that with the default :meth:`BubbleLegend.z_threshold` of ``0``, a bubble of
        value ``-1`` will have the same size as a bubble of value ``1``, while a bubble of
        value 0 will have a smaller size according to :meth:`BubbleLegend.min_size`.

        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._size_by_absolute_value

    @size_by_absolute_value.setter
    def size_by_absolute_value(self, value):
        self._size_by_absolute_value = bool(value)

    @property
    def z_index(self) -> int:
        f"""The visual z index of the bubble legend. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('z_index')}``.

        :rtype: :class:`int <python:int>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.integer(value, allow_empty = True) or \
            constants.DEFAULT_BUBBLE_LEGEND.get('z_index', 1)

    @property
    def z_threshold(self) -> Optional[int | float | Decimal]:
        f"""Ranges with a lower z-value are skipped in the legend. Defaults to
        ``{constants.DEFAULT_BUBBLE_LEGEND.get('z_threshold')}``.

        :rtype: numeric
        """
        return self._z_threshold

    @z_threshold.setter
    def z_threshold(self, value):
        self._z_threshold = validators.numeric(value, allow_empty = True) or \
            constants.DEFAULT_BUBBLE_LEGEND.get('z_threshold', 0)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'border_color': as_dict.pop('borderColor',
                                        constants.DEFAULT_BUBBLE_LEGEND.get('border_color')),
            'border_width': as_dict.pop('borderWidth',
                                        constants.DEFAULT_BUBBLE_LEGEND.get('border_width')),
            'class_name': as_dict.pop('className',
                                      constants.DEFAULT_BUBBLE_LEGEND.get('class_name')),
            'color': as_dict.pop('color', constants.DEFAULT_BUBBLE_LEGEND.get('color')),
            'connector_class_name': as_dict.pop('connectorClassName',
                                                constants.DEFAULT_BUBBLE_LEGEND.get('connector_class_name')),
            'connector_color': as_dict.pop('connectorColor',
                                           constants.DEFAULT_BUBBLE_LEGEND.get('connector_color')),
            'connector_distance': as_dict.pop('connectorDistance',
                                              constants.DEFUALT_BUBBLE_LEGEND.get('connector_distance')),
            'connector_width': as_dict.pop('connectorWidth',
                                           constants.DEFAULT_BUBBLE_LEGEND.get('connector_width')),
            'enabled': as_dict.pop('enabled',
                                   constants.DEFAULT_BUBBLE_LEGEND.get('enabled')),
            'labels': as_dict.pop('labels', None),
            'legend_index': as_dict.pop('legendIndex',
                                        constants.DEFAULT_BUBBLE_LEGEND.get('legend_index')),
            'max_size': as_dict.pop('maxSize',
                                    constants.DEFAULT_BUBBLE_LEGEND.get('max_size')),
            'min_size': as_dict.pop('minSize',
                                    constants.DEFAULT_BUBBLE_LEGEND.get('min_size')),
            'ranges': as_dict.pop('ranges', None),
            'size_by': as_dict.pop('sizeBy',
                                   constants.DEFAULT_BUBBLE_LEGEND.get('size_by')),
            'size_by_absolute_value': as_dict.pop('sizeByAbsoluteValue',
                                                  constants.DEFAULT_BUBBLE_LEGEND.get('size_by_absolute_value')),
            'z_index': as_dict.pop('zIndex',
                                   constants.DEFAULT_BUBBLE_LEGEND.get('z_index')),
            'z_threshold': as_dict.pop('zThreshold',
                                       constants.DEFAULT_BUBBLE_LEGEND.get('z_threshold'))
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'border_color': self.border_color,
            'border_width': self.border_width,
            'class_name': self.class_name,
            'color': self.color,
            'connector_class_name': self.connector_class_name,
            'connector_color': self.connector_color,
            'connector_distance': self.connector_distance,
            'connector_width': self.connector_width,
            'enabled': self.enabled,
            'labels': self.labels,
            'legend_index': self.legend_index,
            'max_size': self.max_size,
            'min_size': self.min_size,
            'ranges': self.ranges,
            'size_by': self.size_by,
            'size_by_absolute_value': self.size_by_absolute_value,
            'z_index': self.z_index,
            'z_threshold': self.z_threshold
        }

        return self.trim_dict(untrimmed)
