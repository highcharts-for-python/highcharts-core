from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class PanelOptions(HighchartsMeta):
    """Configuration of a panel used in 3D charts."""

    def __init__(self, **kwargs):
        self._color = 'transparent'
        self._size = 1
        self._visible = 'default'

        self.color = kwargs.pop('color', 'transparent')
        self.size = kwargs.pop('size', 1)
        self.visible = kwargs.pop('default')

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
    def size(self) -> int | float | Decimal:
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
    def visible(self) -> bool | str:
        """Indicates whether to display the panel in the frame. Defaults to ``'default'``.

        Accepts:

          * ``True`` to always display
          * ``False`` to not display
          * ``'auto'`` to display the panel when it is behind data
          * ``'default'`` to display the panel it is behind data based on the axis layout,
            ignoring the user's point of view

        :rtype: :class:`bool <python:bool>` or :class:`str <python:str>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is False:
            self._visible = False
        elif value is True:
            self._visible = True
        elif not value:
            self._visible = 'default'
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['auto', 'default']:
                raise errors.HighchartsValueError(f'visible access either True, False, '
                                                  f'"auto", or "default". Received: '
                                                  f'{value}')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.pop('color', 'transparent'),
            'size': as_dict.pop('size', 1),
            'visible': as_dict.pop('visible', 'default')
        }

        return cls(**kwargs)

    def to_dict(self):
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
        self._size = 1
        self._top = None
        self._visible = 'default'

        self.back = kwargs.pop('back', None)
        self.bottom = kwargs.pop('bottom', None)
        self.front = kwargs.pop('front', None)
        self.left = kwargs.pop('left', None)
        self.right = kwargs.pop('right', None)
        self.size = kwargs.pop('size', 1)
        self.top = kwargs.pop('top', None)
        self.visible = kwargs.pop('visible', 'default')

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
    def size(self) -> int | float | Decimal:
        """The thickness of the frame. Defaults to ``1``.

        :rtype: numeric
        """
        return self._size

    @size.setter
    def size(self, value):
        self._size = validators.numeric(value,
                                        allow_empty = True,
                                        minimum = 0)

    @property
    def visible(self) -> bool | str:
        """Indicates whether to display the frame. Defaults to ``'default'``.

        Accepts:

          * ``True`` to always display
          * ``False`` to not display
          * ``'auto'`` to display the frame when it is behind data
          * ``'default'`` to display the panel it is behind data based on the axis layout,
            ignoring the user's point of view

        :rtype: :class:`bool <python:bool>` or :class:`str <python:str>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is False:
            self._visible = False
        elif value is True:
            self._visible = True
        elif not value:
            self._visible = 'default'
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['auto', 'default']:
                raise errors.HighchartsValueError(f'visible access either True, False, '
                                                  f'"auto", or "default". Received: '
                                                  f'{value}')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'back': as_dict.pop('back', None),
            'bottom': as_dict.pop('bottom', None),
            'front': as_dict.pop('front', None),
            'left': as_dict.pop('left', None),
            'right': as_dict.pop('right', None),
            'size': as_dict.pop('size', 1),
            'top': as_dict.pop('top', None),
            'visible': as_dict.pop('visible', 'default')
        }

        return cls(**kwargs)

    def to_dict(self):
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
        self._alpha = 0
        self._axis_label_position = constants.enforcedNull
        self._beta = 0
        self._depth = 100
        self._enabled = False
        self._fit_to_plot = True
        self._frame = None
        self._view_distance = 25

        self.alpha = kwargs.pop('alpha', 0)
        self.axis_label_position = kwargs.pop('axis_label_position',
                                              constants.enforcedNull)
        self.beta = kwargs.pop('beta', 0)
        self.depth = kwargs.pop('depth', 100)
        self.enabled = kwargs.pop('enabled', False)
        self.fit_to_plot = kwargs.pop('fit_to_plot', True)
        self.frame = kwargs.pop('frame', None)
        self.view_distance = kwargs.pop('view_distance', 25)

    @property
    def alpha(self) -> int | float | Decimal:
        """One of two rotation angles for the chart. Defaults to ``0``.

        :rtype: numeric
        """
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = validators.integer(value, allow_empty = False)

    @property
    def axis_label_position(self) -> constants.EnforcedNullType | str:
        """Set to ``'auto'`` to automatically move the labels to the best edge.

        Defaults to :class:`EnforcedNull <EnforcedNullType>`` which indicates
        a JavaScript value of ``null`` (as opposed to :obj:`None <python:None>`) which
        results in ``undefined`` when converted JavaScript.

        :rtype: :class:`str` or :class:`EnforcedNullType`
        """
        return self._axis_label_position

    @axis_label_position.setter
    def axis_label_position(self, value):
        if not value:
            self._axis_label_position = constants.EnforcedNull
        else:
            value = validators.string(value)
            value = value.lower()
            if value != 'auto':
                raise errors.HighchartsValueError(f'axis_label_position accepts an empty '
                                                  f'value or "auto". Received: {value}')

            self._axis_label_position = value

    @property
    def beta(self) -> int | float | Decimal:
        """One of two rotation angles for the chart. Defaults to ``0``.

        :rtype: numeric
        """
        return self._beta

    @beta.setter
    def beta(self, value):
        self._beta = validators.integer(value, allow_empty = False)

    @property
    def depth(self) -> int | float | Decimal:
        """The total depth of the chart. Defaults to ``25``.

        :rtype: numeric
        """
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = validators.integer(value, allow_empty = False)

    @property
    def enabled(self) -> bool:
        """If ``True``, renders the chart using the 3D functionality. Defaults to
        ``False``.

        :returns: Flag enabling or disabling 3D rendering.
        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @property
    def fit_to_plot(self) -> bool:
        """If ``True``, automatically adjusts the 3d box to the chart plot area. Defaults
        to ``True``.

        :returns: Flag controlling the auto-adjustment of the 3d box to the chart plot
          area.
        :rtype: :class:`bool <python:bool>`
        """
        return self._fit_to_plot

    @fit_to_plot.setter
    def fit_to_plot(self, value):
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
    def from_dict(cls, as_dict):
        kwargs = {
            'alpha': as_dict.pop('alpha', 0),
            'axis_label_position': as_dict.pop('axisLabelPosition',
                                               constants.EnforcedNull),
            'beta': as_dict.pop('beta', 0),
            'depth': as_dict.pop('depth', 100),
            'enabled': as_dict.pop('enabled', False),
            'fit_to_plot': as_dict.pop('fitToPlot', True),
            'frame': as_dict.pop('frame', None),
            'view_distance': as_dict.pop('viewDistance', 25)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'alpha': self.alpha,
            'axisLabelPositin': self.axis_label_position,
            'beta': self.beta,
            'depth': self.depth,
            'enabled': self.enabled,
            'fitToPlot': self.fit_to_plot,
            'frame': self.frame,
            'viewDistance': self.view_distance
        }

        return self.trim_dict(untrimmed)
