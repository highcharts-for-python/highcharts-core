from typing import Optional

from validator_collection import validators

from highcharts.decorators import class_sensitive, validate_types
from highcharts.plot_options.generic import GenericTypeOptions
from highcharts.plot_options.drag_drop import DragDropOptions
from highcharts.utility_classes.shadows import ShadowOptions


class TimelineOptions(GenericTypeOptions):
    """General options to apply to all Timeline series types.

    The timeline series presents given events along a drawn line.

    .. tabs::

      .. tab:: Standard Timeline

        .. figure:: _static/timeline-example.png
          :alt: Timeline Example Chart
          :align: center

      .. tab:: Inverted Timeline

        .. figure:: _static/timeline-example-inverted.png
          :alt: Inverted Timeline Example Chart
          :align: center

      .. tab:: With True Datetime Axis

        .. figure:: _static/timeline-example-datetime.png
          :alt: Timeline Example Chart with Datetime Axis
          :align: center

    """

    def __init__(self, **kwargs):
        self._color_axis = None
        self._color_by_point = None
        self._color_index = None
        self._color_key = None
        self._crisp = True
        self._drag_drop = None
        self._ignore_hidden_point = None
        self._linecap = None
        self._relative_x_value = None
        self._shadow = None

        self.color_axis = kwargs.pop('color_axis', None)
        self.color_by_point = kwargs.pop('color_by_point', None)
        self.color_index = kwargs.pop('color_index', None)
        self.color_key = kwargs.pop('color_key', None)
        self.crisp = kwargs.pop('crisp', True)
        self.drag_drop = kwargs.pop('drag_drop', None)
        self.ignore_hidden_point = kwargs.pop('ignore_hidden_point', None)
        self.linecap = kwargs.pop('linecap', None)
        self.relative_x_value = kwargs.pop('relative_x_value', None)
        self.shadow = kwargs.pop('shadow', None)

        super().__init__(**kwargs)

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
    def color_by_point(self) -> bool:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        self._color_by_point = bool(value)

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
        :meth:`AreaOptions.color_axis` is used.

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
    def crisp(self) -> Optional[bool]:
        """If ``True``, each point or column edge is rounded to its nearest pixel in order
        to render sharp on screen. Defaults to ``True``.

        .. hint::

          In some cases, when there are a lot of densely packed columns, this leads to
          visible difference in column widths or distance between columns. In these cases,
          setting ``crisp`` to ``False`` may look better, even though each column is
          rendered blurry.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crisp

    @crisp.setter
    def crisp(self, value):
        if value is None:
            self._crisp = None
        else:
            self._crisp = bool(value)

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
    def relative_x_value(self) -> Optional[bool]:
        """When ``True``, X values in the data set are relative to the current
        :meth:`point_start <AreaOptions.point_start>`,
        :meth:`point_interval <AreaOptions.point_interval>`, and
        :meth:`point_interval_unit <AreaOptions.point_interval_unit>` settings. This
        allows compression of the data for datasets with irregular X values. Defaults to
        ``False``.

        The real X values are computed on the formula ``f(x) = ax + b``, where ``a`` is
        the :meth:`point_interval <AreaOptions.point_interval>` (optionally with a time
        unit given by :meth:`point_interval_unit <AreaOptions.point_interval_unit>`), and
        ``b`` is the :meth:`point_start <AreaOptions.point_start>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._relative_x_value

    @relative_x_value.setter
    def relative_x_value(self, value):
        if value is None:
            self._relative_x_value = None
        else:
            self._relative_x_value = bool(value)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
        """Configuration for the shadow to apply to the tooltip. Defaults to
        ``False``.

        If ``False``, no shadow is applied.

        :returns: The shadow configuration to apply or a boolean setting which hides the
          shadow or displays the default shadow.
        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if isinstance(value, bool):
            self._shadow = value
        elif not value:
            self._shadow = None
        else:
            value = validate_types(value,
                                   types = ShadowOptions)
            self._shadow = value

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
            'sticky_tracking': as_dict.pop('stickyTracking', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'color_axis': as_dict.pop('colorAxis', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'crisp': as_dict.pop('crisp', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', None),
            'linecap': as_dict.pop('linecap', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None)
        }

        return kwargs

    def to_dict(self):
        untrimmed = {
            'colorAxis': self.color_axis,
            'colorByPoint': self.color_by_point,
            'colorIndex': self.color_index,
            'colorKey': self.color_key,
            'crisp': self.crisp,
            'dragDrop': self.drag_drop,
            'ignoreHiddenPoint': self.ignore_hidden_point,
            'linecap': self.linecap,
            'relative_XValue': self.relative_x_value,
            'shadow': self.shadow
        }
        parent_as_dict = super().to_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
