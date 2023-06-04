from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class PanelOptions(HighchartsMeta):
    """Configuration of a panel used in 3D charts."""

    def __init__(self, **kwargs):
        self._color = None
        self._size = None
        self._visible = None

        self.color = kwargs.get('color', None)
        self.size = kwargs.get('size', None)
        self.visible = kwargs.get('visible', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'chart.options3d.side'

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or gradient for the 3D panel. Defaults to
        ``'transparent'``.

        :returns: The backgorund color for the 3D panel
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

    @property
    def size(self) -> Optional[int | float | Decimal]:
        """The thickness of the panel. Defaults to ``1``.

        :rtype: numeric
        """
        return self._size

    @size.setter
    def size(self, value):
        self._size = validators.numeric(value,
                                        allow_empty = True,
                                        minimum = 0)

    @property
    def visible(self) -> Optional[bool | str]:
        """Indicates whether to display the panel in the frame. Defaults to ``'default'``.

        Accepts:

          * ``True`` to always display
          * ``False`` to not display
          * ``'auto'`` to display the panel when it is behind data
          * ``'default'`` to display the panel it is behind data based on the axis layout,
            ignoring the user's point of view

        :rtype: :class:`bool <python:bool>` or :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is None:
            self._visible = None
        elif isinstance(value, bool):
            self._visible = value
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['auto', 'default']:
                raise errors.HighchartsValueError(f'visible access either True, False, '
                                                  f'"auto", or "default". Received: '
                                                  f'{value}')
            self._visible = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'size': as_dict.get('size', None),
            'visible': as_dict.get('visible', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'color': self.color,
            'size': self.size,
            'visible': self.visible
        }


class Frame(HighchartsMeta):
    """Provides the option to draw a frame around the charts by defining a bottom, front,
    and back panel."""

    def __init__(self, **kwargs):
        self._back = None
        self._bottom = None
        self._front = None
        self._left = None
        self._right = None
        self._side = None
        self._size = None
        self._top = None
        self._visible = None

        self.back = kwargs.get('back', None)
        self.bottom = kwargs.get('bottom', None)
        self.front = kwargs.get('front', None)
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)
        self.size = kwargs.get('size', None)
        self.top = kwargs.get('top', None)
        self.visible = kwargs.get('visible', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'chart.options3d.frame'

    @property
    def back(self) -> Optional[PanelOptions]:
        """The back side of the frame around a 3D chart.

        :rtype: :class:`PanelOptions`
        """
        return self._back

    @back.setter
    @class_sensitive(PanelOptions)
    def back(self, value):
        self._back = value

    @property
    def bottom(self) -> Optional[PanelOptions]:
        """The bottom side of the frame around a 3D chart.

        :rtype: :class:`PanelOptions`
        """
        return self._bottom

    @bottom.setter
    @class_sensitive(PanelOptions)
    def bottom(self, value):
        self._bottom = value

    @property
    def front(self) -> Optional[PanelOptions]:
        """The front side of the frame around a 3D chart.

        :rtype: :class:`PanelOptions`
        """
        return self._front

    @front.setter
    @class_sensitive(PanelOptions)
    def front(self, value):
        self._front = value

    @property
    def left(self) -> Optional[PanelOptions]:
        """The left side of the frame around a 3D chart.

        :rtype: :class:`PanelOptions`
        """
        return self._left

    @left.setter
    @class_sensitive(PanelOptions)
    def left(self, value):
        self._left = value

    @property
    def right(self) -> Optional[PanelOptions]:
        """The right side of the frame around a 3D chart.

        :rtype: :class:`PanelOptions`
        """
        return self._right

    @right.setter
    @class_sensitive(PanelOptions)
    def right(self, value):
        self._right = value

    @property
    def top(self) -> Optional[PanelOptions]:
        """The top side of the frame around a 3D chart.

        :rtype: :class:`PanelOptions`
        """
        return self._top

    @top.setter
    @class_sensitive(PanelOptions)
    def top(self, value):
        self._top = value

    @property
    def size(self) -> Optional[int | float | Decimal]:
        """The thickness of the frame. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._size

    @size.setter
    def size(self, value):
        self._size = validators.numeric(value,
                                        allow_empty = True,
                                        minimum = 0)

    @property
    def visible(self) -> Optional[bool | str]:
        """Indicates whether to display the frame. Defaults to ``'default'``.

        Accepts:

          * ``True`` to always display
          * ``False`` to not display
          * ``'auto'`` to display the frame when it is behind data
          * ``'default'`` to display the panel it is behind data based on the axis layout,
            ignoring the user's point of view

        :rtype: :class:`bool <python:bool>` or :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is None:
            self._visible = None
        elif isinstance(value, bool):
            self._visible = value
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['auto', 'default']:
                raise errors.HighchartsValueError(f'visible access either True, False, '
                                                  f'"auto", or "default". Received: '
                                                  f'{value}')

            self._visible = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'back': as_dict.get('back', None),
            'bottom': as_dict.get('bottom', None),
            'front': as_dict.get('front', None),
            'left': as_dict.get('left', None),
            'right': as_dict.get('right', None),
            'size': as_dict.get('size', None),
            'top': as_dict.get('top', None),
            'visible': as_dict.get('visible', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'back': self.back,
            'bottom': self.bottom,
            'front': self.front,
            'left': self.left,
            'right': self.right,
            'size': self.size,
            'top': self.top,
            'visible': self.visible
        }


class Options3D(HighchartsMeta):
    """Options to render charts in three dimensions.

    .. note::

      This feature requires the JavaScript ``highcharts-3d.js`` module, found in the
      download package or online at
      `code.highcharts.com/highcharts-3d.js <https://code.highcharts.com/highcharts-3d.js>`_.

    """

    def __init__(self, **kwargs):
        self._alpha = None
        self._axis_label_position = None
        self._beta = None
        self._depth = None
        self._enabled = None
        self._fit_to_plot = None
        self._frame = None
        self._view_distance = None

        self.alpha = kwargs.get('alpha', None)
        self.axis_label_position = kwargs.get('axis_label_position', None)
        self.beta = kwargs.get('beta', None)
        self.depth = kwargs.get('depth', None)
        self.enabled = kwargs.get('enabled', None)
        self.fit_to_plot = kwargs.get('fit_to_plot', None)
        self.frame = kwargs.get('frame', None)
        self.view_distance = kwargs.get('view_distance', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'chart.options3d'

    @property
    def alpha(self) -> Optional[int | float | Decimal]:
        """One of two rotation angles for the chart. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = validators.numeric(value, allow_empty = True)

    @property
    def axis_label_position(self) -> Optional[constants.EnforcedNullType | str]:
        """Set to ``'auto'`` to automatically move the labels to the best edge.

        Defaults to :class:`EnforcedNull <EnforcedNullType>`` which indicates
        a JavaScript value of ``null`` (as opposed to :obj:`None <python:None>`) which
        results in ``undefined`` when converted JavaScript.

        :rtype: :class:`str` or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._axis_label_position

    @axis_label_position.setter
    def axis_label_position(self, value):
        if not value:
            self._axis_label_position = None
        elif isinstance(value, constants.EnforcedNullType):
            self._axis_label_position = constants.EnforcedNull
        else:
            value = validators.string(value)
            value = value.lower()
            if value != 'auto':
                raise errors.HighchartsValueError(f'axis_label_position accepts an empty '
                                                  f'value or "auto". Received: {value}')

            self._axis_label_position = value

    @property
    def beta(self) -> Optional[int | float | Decimal]:
        """One of two rotation angles for the chart. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._beta

    @beta.setter
    def beta(self, value):
        self._beta = validators.numeric(value, allow_empty = True)

    @property
    def depth(self) -> Optional[int | float | Decimal]:
        """The total depth of the chart. Defaults to ``25``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, renders the chart using the 3D functionality. Defaults to
        ``False``.

        :returns: Flag enabling or disabling 3D rendering.
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
    def fit_to_plot(self) -> Optional[bool]:
        """If ``True``, automatically adjusts the 3d box to the chart plot area. Defaults
        to ``True``.

        :returns: Flag controlling the auto-adjustment of the 3d box to the chart plot
          area.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._fit_to_plot

    @fit_to_plot.setter
    def fit_to_plot(self, value):
        if value is None:
            self._fit_to_plot = None
        else:
            self._fit_to_plot = bool(value)

    @property
    def frame(self) -> Optional[Frame]:
        """Settings to draw a frame around the 3d box.

        :rtype: :class:`Frame`
        """
        return self._frame

    @frame.setter
    @class_sensitive(Frame)
    def frame(self, value):
        self._frame = value

    @property
    def view_distance(self) -> Optional[int | float | Decimal]:
        """Defines the distance the viewer is standing in front of the chart. Defaults
        to ``25``.

        .. note::

          This setting is important to calculate the perspective effect in column and
          scatter charts. It is not used for 3D pie charts.

        :rtype: numeric
        """
        return self._view_distance

    @view_distance.setter
    def view_distance(self, value):
        self._view_distance = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'alpha': as_dict.get('alpha', None),
            'axis_label_position': as_dict.get('axisLabelPosition', None),
            'beta': as_dict.get('beta', None),
            'depth': as_dict.get('depth', None),
            'enabled': as_dict.get('enabled', None),
            'fit_to_plot': as_dict.get('fitToPlot', None),
            'frame': as_dict.get('frame', None),
            'view_distance': as_dict.get('viewDistance', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'alpha': self.alpha,
            'axisLabelPosition': self.axis_label_position,
            'beta': self.beta,
            'depth': self.depth,
            'enabled': self.enabled,
            'fitToPlot': self.fit_to_plot,
            'frame': self.frame,
            'viewDistance': self.view_distance
        }

        return untrimmed
