from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.plot_options.area import AreaOptions
from highcharts.utility_classes.jitter import Jitter


class BubbleOptions(AreaOptions):
    """General options to apply to all Bubble series types.

    A bubble series is a three dimensional series type where each point renders an X,
    Y, and Z value. Each points is drawn as a bubble where the position along the X
    and Y axes mark the X and Y values, and the size of the bubble relates to the Z
    value.

    .. figure:: _static/bubble-example.png
      :alt: Bubble Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._display_negative = True
        self._jitter = None
        self._max_size = None
        self._min_size = None
        self._size_by = None
        self._size_by_absolute_value = False
        self._z_max = None
        self._z_min = None
        self._z_threshold = None

        self.display_negative = kwargs.pop('display_negative', True)
        self.jitter = kwargs.pop('jitter', None)
        self.max_size = kwargs.pop('max_size', '20%')
        self.min_size = kwargs.pop('min_size', 8)
        self.size_by = kwargs.pop('size_by', 'area')
        self.size_by_absolute_value = kwargs.pop('size_by_absolute_value', False)
        self.z_max = kwargs.pop('z_max', None)
        self.z_min = kwargs.pop('z_min', None)
        self.z_threshold = kwargs.pop('z_threshold', 0)

        super(self).__init__(**kwargs)

    @property
    def display_negative(self) -> Optional[bool]:
        """If ``True``, display negative sized bubbles.

        The threshold is given by the :meth:`z_threshold <BubbleOptions.z_threshold>`
        setting, and negative bubbles can be visualized by setting
        :meth:`negative_color <BubbleOptions.negative_color>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._display_negative

    @display_negative.setter
    def display_negative(self, value):
        if value is None:
            self._display_negative = None
        else:
            self._display_negative = bool(value)

    @property
    def jitter(self) -> Optional[Jitter]:
        """Apply a jitter effect for the rendered markers.

        When plotting discrete values, a little random noise may help telling the points
        apart. The jitter setting applies a random displacement of up to n axis units in
        either direction.

        So for example on a horizontal X axis, setting the ``jitter.x`` to ``0.24`` will
        render the point in a random position between 0.24 units to the left and 0.24
        units to the right of the true axis position. On a category axis, setting it to
        ``0.5`` will fill up the bin and make the data appear continuous.

        When rendered on top of a box plot or a column series, a jitter value of 0.24 will
        correspond to the underlying series' default ``group_padding`` and
        ``point_padding`` settings.

        :rtype: :class:`Jitter` or :obj:`None <python:None>`
        """
        return self._jitter

    @jitter.setter
    @class_sensitive(Jitter)
    def jitter(self, value):
        self._jitter = value

    @property
    def max_size(self) -> Optional[str | int | float | Decimal]:
        """Maximum bubble size. Defaults to ``'20%'``.

        If :obj:`None <python:None>`, bubbles will automatically size between the
        :meth:`min_size <BubbleOptions.min_size>` and ``max_size``, to reflect the z value
        of each bubble. Can be either pixels (when no unit is given), or a percentage of
        the smallest one of the plot width and height.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if value is None:
            self._max_size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                self._max_size = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def min_size(self) -> Optional[str | int | float | Decimal]:
        """Minimum bubble size. Defaults to ``8``.

        If :obj:`None <python:None>`, bubbles will automatically size between the
        :meth:`max_size <BubbleOptions.max_size>` and ``min_size``, to reflect the z value
        of each bubble. Can be either pixels (when no unit is given), or a percentage of
        the smallest one of the plot width and height.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value):
        if value is None:
            self._min_size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                self._min_size = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def size_by(self) -> Optional[str]:
        """Whether the bubble's value should be represented by the ``'area'`` or the
        ``'width'`` of the bubble. The default, ``'area'``, corresponds best to the human
        perception of the size of each bubble.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._size_by

    @size_by.setter
    def size_by(self, value):
        if not value:
            self._size_by = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['area', 'width']:
                raise errors.HighchartsValueError(f'size_by expects either "area", '
                                                  f'or "width". Received: {value}')
            self._size_by = value

    @property
    def size_by_absolute_value(self) -> Optional[bool]:
        """If ``True``, the absolute value of z determines the size of the bubble. This
        means that with the default :meth:`z_threshold <BubbleOptions.z_threshold>` of
        ``0``, a bubble of value ``-1`` will have the same size as a bubble of value
        ``1``, while a bubble of value ``0`` will have a smaller size according to
        :meth:`min_size <BubbleOptions.min_size>`.

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
    def z_max(self) -> Optional[int | float | Decimal]:
        """The maximum for the Z value range. When :obj:`None <python:None>`, defaults to
        the highest Z value in the data. Defaults to :obj:`None <python:None>``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_max

    @z_max.setter
    def z_max(self, value):
        self._z_max = validators.numeric(value, allow_empty = True)

    @property
    def z_min(self) -> Optional[int | float | Decimal]:
        """The minimum for the Z value range. When :obj:`None <python:None>`, defaults to
        the lowest Z value in the data. Defaults to :obj:`None <python:None>``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_min

    @z_min.setter
    def z_min(self, value):
        self._z_min = validators.numeric(value, allow_empty = True)

    @property
    def z_threshold(self) -> Optional[int | float | Decimal]:
        """When :meth:`display_negative <BubbleOptions.display_negative>` is ``False``,
        then bubbles with a Z value lower than ``z_threshold`` are not rendered. When
        :meth:`display_negative <BubbleOptions.display_negative>` is ``True`` and
        :meth:`negative_color <BubbleOptions.negative_color>` is set, then points
        with a Z value lower than ``z_threshold`` are rendered with the negative coloring.

        Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_threshold

    @z_threshold.setter
    def z_threshold(self, value):
        self._z_threshold = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', 0.75),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', False),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'display_negative': as_dict.pop('displayNegative', True),
            'jitter': as_dict.pop('jitter', None),
            'max_size': as_dict.pop('maxSize', '20%'),
            'min_size': as_dict.pop('minSize', 8),
            'size_by': as_dict.pop('sizeBy', 'area'),
            'size_by_absolute_value': as_dict.pop('sizeByAbsoluteValue', False),
            'z_max': as_dict.pop('zMax', None),
            'z_min': as_dict.pop('zMin', None),
            'z_threshold': as_dict.pop('zThreshold', 0),
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'display_negative': self.display_negative,
            'jitter': self.jitter,
            'max_size': self.max_size,
            'min_size': self.min_size,
            'size_by': self.size_by,
            'size_by_absolute_value': self.size_by_absolute_value,
            'z_max': self.z_max,
            'z_min': self.z_min,
            'z_threshold': self.z_threshold
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
