from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import validate_types
from highcharts.plot_options.generic import GenericTypeOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class PieOptions(GenericTypeOptions):
    """General options to apply to all Pie series types.

    A pie chart is a circular graphic which is divided into slices to illustrate
    numerical proportion.

    .. tabs::

      .. tab:: Pie Chart

        .. figure:: _static/pie-example.png
          :alt: Pie Example Chart
          :align: center

      .. tab:: Donut Chart

        .. figure:: _static/pie-example-donut.png
          :alt: Donut Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._center = None
        self._color_axis = None
        self._color_index = None
        self._color_key = None
        self._colors = None
        self._depth = 0
        self._end_angle = None
        self._fill_color = None
        self._ignore_hidden_point = True
        self._inner_size = 0
        self._linecap = None
        self._min_size = 80
        self._size = None
        self._sliced_offset = None
        self._start_angle = 0
        self._thickness = None

        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', 1)
        self.center = kwargs.pop('center', ['50%', '50%'])
        self.color_axis = kwargs.pop('color_axis', 0)
        self.color_index = kwargs.pop('color_index', None)
        self.color_key = kwargs.pop('color_key', 'y')
        self.colors = kwargs.pop('colors', None)
        self.depth = kwargs.pop('depth', 0)
        self.end_angle = kwargs.pop('end_angle', None)
        self.fill_color = kwargs.pop('fill_color', None)
        self.ignore_hidden_point = kwargs.pop('ignore_hidden_point', True)
        self.inner_size = kwargs.pop('inner_size', 0)
        self.linecap = kwargs.pop('linecap', 'round')
        self.min_size = kwargs.pop('min_size', 80)
        self.size = kwargs.pop('size', None)
        self.sliced_offset = kwargs.pop('sliced_offset', 10)
        self.start_angle = kwargs.pop('start_angle', 0)
        self.thickness = kwargs.pop('thickness', None)

        super(self).__init__(**kwargs)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each slice. When :obj:`None <python:None>`,
        the border takes the same color as the slice fill. This can be used together with
        a :meth:`border_width <PieOptions.border_width>` to fill drawing gaps created by
        antialiazing artefacts in borderless pies. Defaults to ``'#ffffff'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
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
        """The width of the border surrounding each slice. Defaults to ``1``.

        When setting the border width to ``0``, there may be small gaps between the slices
        due to SVG antialiasing artefacts. To work around this, keep the border width at
        ``0.5`` or ``1``, but set the :meth:`border_color <PieOptions.border_color>` to
        :obj:`None <python:None>` instead.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def center(self) -> Optional[List[str | int | float | Decimal | constants.EnforcedNullType]]:
        """The center of the pie chart relative to the plot area.

        Can be percentages or pixel values. The default behaviour if
        :obj:`None <python:None>` is to center the pie so that all slices and data labels
        are within the plot area. As a consequence, the pie may actually jump around in a
        chart with dynamic values, as the data labels move. In that case, the center
        should be explicitly set, for example to ``["50%", "50%"]``.

        Defaults to ``['50%', '50%']``.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of numeric or
          :class:`str <python:str>` values
        """
        return self._center

    @center.setter
    def center(self, value):
        if not value:
            self._center = None
        else:
            value = validators.iterable(value)
            if len(value) != 2:
                raise errors.HighchartsValueError(f'center expects a 2-member array. '
                                                  f'Received a {len(value)}-member array.')
            processed_values = []
            for item in value:
                try:
                    item = validators.string(value)
                    if '%' not in item:
                        raise ValueError
                except ValueError:
                    item = validators.numeric(value)

                processed_values.append(item)

            self._center = processed_values

    @property
    def color_axis(self) -> Optional[str | int | bool]:
        """When using dual or multiple color axes, this setting defines which
        :term:`color axis` the particular series is connected to. It refers to either the
        :meth:`ColorAxis.id` or the index of the axis in the :class:`ColorAxis` array,
        with ``0`` being the first. Set this option to ``False`` to prevent a series from
        connecting to the default color axis.

        Defaults to ``0``.

        :rtype: :obj:`None <python:None>` or :class:`str <python:str>` or
          :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._color_axis

    @color_axis.setter
    def color_axis(self, value):
        if value is None:
            self._color_axis = None
        elif value is False:
            self._color_axis = False
        else:
            try:
                self._color_axis = validators.string(value)
            except ValueError:
                self._color_axis = validators.integer(value,
                                                      minimum = 0)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def color_key(self) -> Optional[str]:
        """Determines what data value should be used to calculate point color if
        :meth:`PieOptions.color_axis` is used.

        .. note::

          Requires to set ``min`` and ``max`` if some custom point property is used or if
          approximation for data grouping is set to ``'sum'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color_key

    @color_key.setter
    def color_key(self, value):
        self._color_key = validators.string(value, allow_empty = True)

    @property
    def colors(self) -> Optional[List[str | Gradient | Pattern]]:
        """A series-specific or series type-specific color set to apply instead of the
        global colors when :meth:`ArcDiagramOptions.color_by_point` is ``True``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`,
          :class:`Gradient`, or :class:`Pattern` OR :obj:`None <python:None>`
        """
        return self._colors

    @colors.setter
    def colors(self, value):
        if not value:
            self._colors = None
        else:
            value = validators.iterable(value)
            checked_values = []
            for item in value:
                if isinstance(value, str):
                    checked_values.append(item)
                else:
                    processed_item = validate_types(item,
                                                    types = (Gradient, Pattern))
                    checked_values.append(processed_item)

            self._colors = checked_values

    @property
    def depth(self) -> Optional[int | float | Decimal]:
        """The thickness of a 3D pie. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = validators.numeric(value, allow_empty = True)

    @property
    def end_angle(self) -> Optional[int | float | Decimal]:
        """The end angle of the pie in degrees where 0 is top and 90 is right.
        Defaults to :obj:`None <python:None>`, which is equivalent to
        :meth:`start_angle <PieOptions.start_angle>` plus ``360``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._end_angle

    @end_angle.setter
    def end_angle(self, value):
        self._end_angle = validators.numeric(value,
                                             allow_empty = True,
                                             minimum = 0)

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """If the total sum of the pie's values is ``0``, the series is represented as an
        empty circle . The ``fill_color`` setting defines the color of that circle.
        Use :meth:`PieOptions.border_width` to set the border thickness.

        Defaults to :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, or :class:`Pattern`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        if not value:
            self._fill_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._fill_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._fill_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Gradient.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._fill_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._fill_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Pattern.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._fill_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def ignore_hidden_point(self) -> Optional[bool]:
        """If ``True``, the series shall be redrawn as if the hidden points were ``null``.
        If ``False``, hidden points will not be displayed but the slice will still be
        drawn as a gap in the pie.

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._ignore_hidden_point

    @ignore_hidden_point.setter
    def ignore_hidden_point(self, value):
        if value is None:
            self._ignore_hidden_point = None
        else:
            self._ignore_hidden_point = bool(value)

    @property
    def inner_size(self) -> Optional[str | int]:
        """The size of the inner diameter for the pie, expressed as a percentage or pixel
        value. Defaults to ``0``.

        .. hint::

          A size greater than 0 renders a donut chart.

        .. note::

          Percentages are relative to the pie size. Pixel values are given as integers.

        .. warning::

          If :meth:`PieOptions.thickness` is set, this value will be overridden by the
          ``thickness`` setting.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._inner_size

    @inner_size.setter
    def inner_size(self, value):
        if value is None:
            self._inner_size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.integer(value, minimum = 0)

            self._inner_size = value

    @property
    def linecap(self) -> Optional[str]:
        """The SVG value used for the ``stroke-linecap`` and ``stroke-linejoin`` of a line
        graph. Defaults to ``'round'``, which means that lines are rounded in the ends and
        bends.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._linecap

    @linecap.setter
    def linecap(self, value):
        self._linecap = validators.string(value, allow_empty = True)

    @property
    def min_size(self) -> Optional[str | int | float | Decimal]:
        """The minimum size for a pie in response to auto margins, expressed in pixels or
        percentages. Defaults to ``80``.

        .. note::

          The pie will try to shrink to make room for data labels in side the plot area,
          but only to this size.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
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
                value = validators.numeric(value, minimum = 0)

            self._min_size = value

    @property
    def size(self) -> Optional[str | int]:
        """The diameter of the pie relative to the plot area, expressed as a percentage or
        pixel value given as an integer.

        If :obj:`None <python:None>`, scales the pie to the plot area and gives room for
        data labels within the plot area.

        .. note::

          :meth:`PieOptions.sliced_offset` is also included in the default size
          calculation. As a consequence, the size of the pie may vary when points are
          updated and data labels more around. In that case it is best to set a fixed
          value, for example ``"75%"``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._size

    @size.setter
    def size(self, value):
        if value is None:
            self._size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.integer(value, minimum = 0)

            self._size = value

    @property
    def sliced_offset(self) -> Optional[int | float | Decimal]:
        """If a point is sliced, moved out from the center, how many pixels should it be
        moved? Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._sliced_offset

    @sliced_offset.setter
    def sliced_offset(self, value):
        self._sliced_offset = validators.numeric(value, allow_empty = True)

    @property
    def start_angle(self) -> Optional[int | float | Decimal]:
        """The start angle of the dependency wheel, in degrees where ``0`` is up. Defaults
        to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._start_angle

    @start_angle.setter
    def start_angle(self, value):
        self._start_angle = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0,
                                               maximum = 360)

    @property
    def thickness(self) -> Optional[int]:
        """Thickness describing the ring size for a donut type chart, overriding
        :meth:`PieOptions.inner_size`. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        self._thickness = validators.integer(value,
                                             allow_empty = True,
                                             minimum = 0)

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

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center': as_dict.pop('center', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'colors': as_dict.pop('colors', None),
            'depth': as_dict.pop('depth', 0),
            'end_angle': as_dict.pop('endAngle', None),
            'fill_color': as_dict.pop('fillColor', None),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', True),
            'inner_size': as_dict.pop('innerSize', 0),
            'linecap': as_dict.pop('linecap', 'round'),
            'min_size': as_dict.pop('minSize', 80),
            'size': as_dict.pop('size', None),
            'sliced_offset': as_dict.pop('slicedOffset', 10),
            'start_angle': as_dict.pop('startAngle', 0)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'center': self.center,
            'colorAxis': self.color_axis,
            'colorIndex': self.color_index,
            'colorKey': self.color_key,
            'colors': self.colors,
            'depth': self.depth,
            'endAngle': self.end_angle,
            'fillColor': self.fill_color,
            'ignoreHiddenPoint': self.ignore_hidden_point,
            'innerSize': self.inner_size,
            'linecap': self.linecap,
            'minSize': self.min_size,
            'size': self.size,
            'slicedOffset': self.sliced_offset,
            'startAngle': self.start_angle
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
