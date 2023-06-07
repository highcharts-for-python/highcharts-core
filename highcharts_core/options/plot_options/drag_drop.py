from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class DragHandle(HighchartsMeta):
    """Options for the drag handles available in column series."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._cursor = None
        self._line_color = None
        self._line_width = None
        self._path_formatter = None
        self._z_index = None

        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.cursor = kwargs.get('cursor', None)
        self.line_color = kwargs.get('line_color', None)
        self.line_width = kwargs.get('line_width', None)
        self.path_formatter = kwargs.get('path_formatter', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def class_name(self) -> Optional[str]:
        """CSS class name of the guide box in this state. Defaults to
        ``'highcharts-drag-handle'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The fill color of the drag handles. Defaults to ``'#fff'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def cursor(self) -> Optional[str]:
        """The mouse cursor to use for the drag handles. By default (when
        :obj:`None <python:None>`), this intelligently switches between ``'ew-resize'``
        and ``'ns-resize'`` depending on the direction the point is being dragged.

        Acceptable values are:

          * ``'alias'``
          * ``'all-scroll'``
          * ``'auto'``
          * ``'cell'``
          * ``'col-resize'``
          * ``'context-menu'``
          * ``'copy'``
          * ``'crosshair'``
          * ``'default'``
          * ``'e-resize'``
          * ``'ew-resize'``
          * ``'grab'``
          * ``'grabbing'``
          * ``'help'``
          * ``'move'``
          * ``'n-resize'``
          * ``'ne-resize'``
          * ``'nesw-resize'``
          * ``'no-drop'``
          * ``'none'``
          * ``'not-allowed'``
          * ``'ns-resize'``
          * ``'nw-resize'``
          * ``'nwse-resize'``
          * ``'pointer'``
          * ``'progress'``
          * ``'row-resize'``
          * ``'s-resize'``
          * ``'se-resize'``
          * ``'sw-resize'``
          * ``'text'``
          * ``'vertical-text'``
          * ``'w-resize'``
          * ``'wait'``
          * ``'zoom-in'``
          * ``'zoom-out'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        if not value:
            self._cursor = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.SUPPORTED_CURSOR_VALUES:
                raise errors.HighchartsValueError(f'cursor expects a valid cursor value. '
                                                  f'Received: {value}')
            self._cursor = value

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """The line color of the drag handles. Defaults to ``'rgba(0, 0, 0, 0.6)'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        from highcharts_core import utility_functions
        self._line_color = utility_functions.validate_color(value)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The line width for the drag handles. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def path_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript function to define the SVG path to use for the drag handles. Takes
        the ``point`` as a (JavaScript) argument. Should return an SVG path in array
        format. The SVG path is automatically positioned on the point.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._path_formatter

    @path_formatter.setter
    @class_sensitive(CallbackFunction)
    def path_formatter(self, value):
        self._path_formatter = value

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """Drag handles' zIndex position. Defaults to ``901``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'path_formatter': as_dict.get('pathFormatter', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'cursor': self.cursor,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
            'pathFormatter': self.path_formatter,
            'zIndex': self.z_index
        }

        return untrimmed


class GuideBoxOptions(HighchartsMeta):
    """Style options for the guide box default state."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._cursor = None
        self._line_color = None
        self._line_width = None
        self._z_index = None

        self.class_name = kwargs.get('class_name', None)
        self.color = kwargs.get('color', None)
        self.cursor = kwargs.get('cursor', None)
        self.line_color = kwargs.get('line_color', None)
        self.line_width = kwargs.get('line_width', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def class_name(self) -> Optional[str]:
        """CSS class name of the guide box in this state. Defaults to
        ``'highcharts-drag-box-default'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """Guide box fill color. Defaults to ``'rgba(0, 0, 0, 0.1)'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def cursor(self) -> Optional[str]:
        """The style of cursor to use when the user's mouse hovers over the data series.
        Defaults to ``'move'``.

        Acceptable values are:

          * ``'alias'``
          * ``'all-scroll'``
          * ``'auto'``
          * ``'cell'``
          * ``'col-resize'``
          * ``'context-menu'``
          * ``'copy'``
          * ``'crosshair'``
          * ``'default'``
          * ``'e-resize'``
          * ``'ew-resize'``
          * ``'grab'``
          * ``'grabbing'``
          * ``'help'``
          * ``'move'``
          * ``'n-resize'``
          * ``'ne-resize'``
          * ``'nesw-resize'``
          * ``'no-drop'``
          * ``'none'``
          * ``'not-allowed'``
          * ``'ns-resize'``
          * ``'nw-resize'``
          * ``'nwse-resize'``
          * ``'pointer'``
          * ``'progress'``
          * ``'row-resize'``
          * ``'s-resize'``
          * ``'se-resize'``
          * ``'sw-resize'``
          * ``'text'``
          * ``'vertical-text'``
          * ``'w-resize'``
          * ``'wait'``
          * ``'zoom-in'``
          * ``'zoom-out'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        if not value:
            self._cursor = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.SUPPORTED_CURSOR_VALUES:
                raise errors.HighchartsValueError(f'cursor expects a valid cursor value. '
                                                  f'Received: {value}')
            self._cursor = value

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the border around the guide box. Defaults to ``'#888'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        from highcharts_core import utility_functions
        self._line_color = utility_functions.validate_color(value)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the line around the guide box. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """Guide box zIndex position. Defaults to ``900``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'cursor': self.cursor,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
            'zIndex': self.z_index
        }

        return untrimmed


class GuideBox(HighchartsMeta):
    """Style options for the guide box. The guide box has one state by default, the
    ``default`` state."""

    def __init__(self, **kwargs):
        self._default = None
        self.default = kwargs.get('default', None)

    @property
    def default(self) -> Optional[GuideBoxOptions]:
        """Style options for the guide box default state.

        :rtype: :class:`GuideBoxOptions` or :obj:`None <python:None>`
        """
        return self._default

    @default.setter
    @class_sensitive(GuideBoxOptions)
    def default(self, value):
        self._default = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return {
            'default': as_dict.get('default', None)
        }

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'default': self.default
        }

        return untrimmed


class DragDropOptions(HighchartsMeta):
    """The draggable-points module allows points to be moved around or modified in the
    chart.

    In addition to the options mentioned under the dragDrop API structure, the module
    fires three (JavaScript) events:

      * ``point.dragStart``
      * ``point.drag``
      * ``point.drop``

    """

    def __init__(self, **kwargs):
        self._draggable_x = None
        self._draggable_y = None
        self._drag_handle = None
        self._drag_max_x = None
        self._drag_max_y = None
        self._drag_min_x = None
        self._drag_min_y = None
        self._drag_precision_x = None
        self._drag_precision_y = None
        self._drag_sensitivity = 2
        self._group_by = None
        self._guide_box = None
        self._live_redraw = True

        self.draggable_x = kwargs.get('draggable_x', None)
        self.draggable_y = kwargs.get('draggable_y', None)
        self.drag_handle = kwargs.get('drag_handle', None)
        self.drag_max_x = kwargs.get('drag_max_x', None)
        self.drag_max_y = kwargs.get('drag_max_y', None)
        self.drag_min_x = kwargs.get('drag_min_x', None)
        self.drag_min_y = kwargs.get('drag_min_y', None)
        self.drag_precision_x = kwargs.get('drag_precision_x', None)
        self.drag_precision_y = kwargs.get('drag_precision_y', None)
        self.drag_sensitivity = kwargs.get('drag_sensitivity', None)
        self.group_by = kwargs.get('group_by', None)
        self.guide_box = kwargs.get('guide_box', None)
        self.live_redraw = kwargs.get('live_redraw', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.series.dragDrop'

    @property
    def draggable_x(self) -> Optional[bool]:
        """If ``True``, enables dragging along the X dimension. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_x

    @draggable_x.setter
    def draggable_x(self, value):
        if value is None:
            self._draggable_x = None
        else:
            self._draggable_x = bool(value)

    @property
    def draggable_y(self) -> Optional[bool]:
        """If ``True``, enables dragging along the Y dimension. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``False``.

        .. warning::

          This is not supported for TreeGrid axes (the default axis type in Gantt charts).

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_y

    @draggable_y.setter
    def draggable_y(self, value):
        if value is None:
            self._draggable_y = None
        else:
            self._draggable_y = bool(value)

    @property
    def drag_handle(self) -> Optional[DragHandle]:
        """Options for the drag handles available in column series.

        :rtype: :class:`DragHandle` or :obj:`None <python:None>`
        """
        return self._drag_handle

    @drag_handle.setter
    @class_sensitive(DragHandle)
    def drag_handle(self, value):
        self._drag_handle = value

    @property
    def drag_max_x(self) -> Optional[int | float | Decimal]:
        """The maximum X value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_max_x

    @drag_max_x.setter
    def drag_max_x(self, value):
        self._drag_max_x = validators.numeric(value, allow_empty = True)

    @property
    def drag_max_y(self) -> Optional[int | float | Decimal]:
        """The maximum Y value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_max_y

    @drag_max_y.setter
    def drag_max_y(self, value):
        self._drag_max_y = validators.numeric(value, allow_empty = True)

    @property
    def drag_min_x(self) -> Optional[int | float | Decimal]:
        """The minimum X value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_min_x

    @drag_min_x.setter
    def drag_min_x(self, value):
        self._drag_min_x = validators.numeric(value, allow_empty = True)

    @property
    def drag_min_y(self) -> Optional[int | float | Decimal]:
        """The minimum Y value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_min_y

    @drag_min_y.setter
    def drag_min_y(self, value):
        self._drag_min_y = validators.numeric(value, allow_empty = True)

    @property
    def drag_precision_x(self) -> Optional[int | float | Decimal]:
        """The X precision value to drag to for this series. Defaults to
        :obj:`None <python:None>`, which is equivalent to disabling for most axes except
        for category axes where the default is ``1``.

        Set to ``0`` to disable for all axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_precision_x

    @drag_precision_x.setter
    def drag_precision_x(self, value):
        self._drag_precision_x = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def drag_precision_y(self) -> Optional[int | float | Decimal]:
        """The Y precision value to drag to for this series. Defaults to
        :obj:`None <python:None>`, which is equivalent to disabling for most axes except
        for category axes where the default is ``1``.

        Set to ``0`` to disable for all axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_precision_y

    @drag_precision_y.setter
    def drag_precision_y(self, value):
        self._drag_precision_y = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def drag_sensitivity(self) -> Optional[int | float | Decimal]:
        """The number of pixels to drag the pointer before it counts as a drag operation.
        Defaults to ``2``.

        .. note::

          This prevents drag/drop to fire when just clicking or selecting points.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_sensitivity

    @drag_sensitivity.setter
    def drag_sensitivity(self, value):
        self._drag_sensitivity = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def group_by(self) -> Optional[str]:
        """Group the points by a property. Points with the same property value will be
        grouped together when moving. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._group_by

    @group_by.setter
    def group_by(self, value):
        self._group_by = validators.string(value, allow_empty = True)

    @property
    def guide_box(self) -> Optional[GuideBox]:
        """Style options for the guide box. The guide box has one state by default, the
        ``default`` state.

        :rtype: :class:`GuideBox` or :obj:`None <python:None>`
        """
        return self._guide_box

    @guide_box.setter
    @class_sensitive(GuideBox)
    def guide_box(self, value):
        self._guide_box = value

    @property
    def live_redraw(self) -> Optional[bool]:
        """If ``True``, update points as they are dragged. If ``False``, a guide box is
        drawn to illustrate the new point size. Defaults to :obj:`None <python:None>`,
        which behaves as ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`.
        """
        return self._live_redraw

    @live_redraw.setter
    def live_redraw(self, value):
        if value is None:
            self._live_redraw = None
        else:
            self._live_redraw = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'draggable_x': as_dict.get('draggableX', None),
            'draggable_y': as_dict.get('draggableY', None),
            'drag_handle': as_dict.get('dragHandle', None),
            'drag_max_x': as_dict.get('dragMaxX', None),
            'drag_max_y': as_dict.get('dragMaxY', None),
            'drag_min_x': as_dict.get('dragMinX', None),
            'drag_min_y': as_dict.get('dragMinY', None),
            'drag_precision_x': as_dict.get('dragPrecisionX', None),
            'drag_precision_y': as_dict.get('dragPrecisionY', None),
            'drag_sensitivity': as_dict.get('dragSensitivity', None),
            'group_by': as_dict.get('groupBy', None),
            'guide_box': as_dict.get('guideBox', None),
            'live_redraw': as_dict.get('liveRedraw', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'draggableX': self.draggable_x,
            'draggableY': self.draggable_y,
            'dragHandle': self.drag_handle,
            'dragMaxX': self.drag_max_x,
            'dragMaxY': self.drag_max_y,
            'dragMinX': self.drag_min_x,
            'dragMinY': self.drag_min_y,
            'dragPrecisionX': self.drag_precision_x,
            'dragPrecisionY': self.drag_precision_y,
            'dragSensitivity': self.drag_sensitivity,
            'groupBy': self.group_by,
            'guideBox': self.guide_box,
            'liveRedraw': self.live_redraw
        }

        return untrimmed


class HighLowDragDropOptions(DragDropOptions):
    """The draggable-points module allows points to be moved around or modified in the
    chart."""

    def __init__(self, **kwargs):
        self._draggable_high = None
        self._draggable_low = None

        self.draggable_high = kwargs.get('draggable_high', None)
        self.draggable_low = kwargs.get('draggable_low', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.boxplot.dragDrop'

    @property
    def draggable_high(self) -> Optional[bool]:
        """If ``True``, enables high value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_high

    @draggable_high.setter
    def draggable_high(self, value):
        if value is None:
            self._draggable_high = None
        else:
            self._draggable_high = bool(value)

    @property
    def draggable_low(self) -> Optional[bool]:
        """If ``True``, enables the low value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_low

    @draggable_low.setter
    def draggable_low(self, value):
        if value is None:
            self._draggable_low = None
        else:
            self._draggable_low = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'draggable_x': as_dict.get('draggableX', None),
            'draggable_y': as_dict.get('draggableY', None),
            'drag_handle': as_dict.get('dragHandle', None),
            'drag_max_x': as_dict.get('dragMaxX', None),
            'drag_max_y': as_dict.get('dragMaxY', None),
            'drag_min_x': as_dict.get('dragMinX', None),
            'drag_min_y': as_dict.get('dragMinY', None),
            'drag_precision_x': as_dict.get('dragPrecisionX', None),
            'drag_precision_y': as_dict.get('dragPrecisionY', None),
            'drag_sensitivity': as_dict.get('dragSensitivity', None),
            'group_by': as_dict.get('groupBy', None),
            'guide_box': as_dict.get('guideBox', None),
            'live_redraw': as_dict.get('liveRedraw', None),

            'draggable_high': as_dict.get('draggableHigh', None),
            'draggable_low': as_dict.get('draggableLow', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'draggableHigh': self.draggable_high,
            'draggableLow': self.draggable_low,
            'draggableX': self.draggable_x,
            'draggableY': self.draggable_y,
            'dragHandle': self.drag_handle,
            'dragMaxX': self.drag_max_x,
            'dragMaxY': self.drag_max_y,
            'dragMinX': self.drag_min_x,
            'dragMinY': self.drag_min_y,
            'dragPrecisionX': self.drag_precision_x,
            'dragPrecisionY': self.drag_precision_y,
            'dragSensitivity': self.drag_sensitivity,
            'groupBy': self.group_by,
            'guideBox': self.guide_box,
            'liveRedraw': self.live_redraw
        }

        return untrimmed


class BoxPlotDragDropOptions(HighLowDragDropOptions):
    """The draggable-points module allows points to be moved around or modified in the
    chart."""

    def __init__(self, **kwargs):
        self._draggable_high = None
        self._draggable_low = None
        self._draggable_q1 = None
        self._draggable_q3 = None

        self.draggable_high = kwargs.get('draggable_high', None)
        self.draggable_low = kwargs.get('draggable_low', None)
        self.draggable_q1 = kwargs.get('draggable_q1', None)
        self.draggable_q3 = kwargs.get('draggable_q3', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.boxplot.dragDrop'

    @property
    def draggable_q1(self) -> Optional[bool]:
        """If ``True``, enables the Q1 value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_q1

    @draggable_q1.setter
    def draggable_q1(self, value):
        if value is None:
            self._draggable_q1 = None
        else:
            self._draggable_q1 = bool(value)

    @property
    def draggable_q3(self) -> Optional[bool]:
        """If ``True``, enables the Q3 value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_q3

    @draggable_q3.setter
    def draggable_q3(self, value):
        if value is None:
            self._draggable_q3 = None
        else:
            self._draggable_q3 = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'draggable_x': as_dict.get('draggableX', None),
            'draggable_y': as_dict.get('draggableY', None),
            'drag_handle': as_dict.get('dragHandle', None),
            'drag_max_x': as_dict.get('dragMaxX', None),
            'drag_max_y': as_dict.get('dragMaxY', None),
            'drag_min_x': as_dict.get('dragMinX', None),
            'drag_min_y': as_dict.get('dragMinY', None),
            'drag_precision_x': as_dict.get('dragPrecisionX', None),
            'drag_precision_y': as_dict.get('dragPrecisionY', None),
            'drag_sensitivity': as_dict.get('dragSensitivity', None),
            'group_by': as_dict.get('groupBy', None),
            'guide_box': as_dict.get('guideBox', None),
            'live_redraw': as_dict.get('liveRedraw', None),

            'draggable_high': as_dict.get('draggableHigh', None),
            'draggable_low': as_dict.get('draggableLow', None),
            'draggable_q1': as_dict.get('draggableQ1', None),
            'draggable_q3': as_dict.get('draggableQ3', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'draggableX': self.draggable_x,
            'draggableY': self.draggable_y,
            'dragHandle': self.drag_handle,
            'dragMaxX': self.drag_max_x,
            'dragMaxY': self.drag_max_y,
            'dragMinX': self.drag_min_x,
            'dragMinY': self.drag_min_y,
            'dragPrecisionX': self.drag_precision_x,
            'dragPrecisionY': self.drag_precision_y,
            'dragSensitivity': self.drag_sensitivity,
            'groupBy': self.group_by,
            'guideBox': self.guide_box,
            'liveRedraw': self.live_redraw,

            'draggableHigh': self.draggable_high,
            'draggableLow': self.draggable_low,
            'draggableQ1': self.draggable_q1,
            'draggableQ3': self.draggable_q3
        }

        return untrimmed


class BulletDragDropOptions(DragDropOptions):
    """The draggable-points module allows points to be moved around or modified in the
    chart."""

    def __init__(self, **kwargs):
        self._draggable_target = None

        self.draggable_target = kwargs.get('draggable_target', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.bullet.dragDrop'

    @property
    def draggable_target(self) -> Optional[bool]:
        """If ``True``, enables the target to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_target

    @draggable_target.setter
    def draggable_target(self, value):
        if value is None:
            self._draggable_target = None
        else:
            self._draggable_target = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'draggable_x': as_dict.get('draggableX', None),
            'draggable_y': as_dict.get('draggableY', None),
            'drag_handle': as_dict.get('dragHandle', None),
            'drag_max_x': as_dict.get('dragMaxX', None),
            'drag_max_y': as_dict.get('dragMaxY', None),
            'drag_min_x': as_dict.get('dragMinX', None),
            'drag_min_y': as_dict.get('dragMinY', None),
            'drag_precision_x': as_dict.get('dragPrecisionX', None),
            'drag_precision_y': as_dict.get('dragPrecisionY', None),
            'drag_sensitivity': as_dict.get('dragSensitivity', None),
            'group_by': as_dict.get('groupBy', None),
            'guide_box': as_dict.get('guideBox', None),
            'live_redraw': as_dict.get('liveRedraw', None),

            'draggable_target': as_dict.get('draggableTarget', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'draggableX': self.draggable_x,
            'draggableY': self.draggable_y,
            'dragHandle': self.drag_handle,
            'dragMaxX': self.drag_max_x,
            'dragMaxY': self.drag_max_y,
            'dragMinX': self.drag_min_x,
            'dragMinY': self.drag_min_y,
            'dragPrecisionX': self.drag_precision_x,
            'dragPrecisionY': self.drag_precision_y,
            'dragSensitivity': self.drag_sensitivity,
            'groupBy': self.group_by,
            'guideBox': self.guide_box,
            'liveRedraw': self.live_redraw,

            'draggableTarget': self.draggable_target
        }

        return untrimmed
