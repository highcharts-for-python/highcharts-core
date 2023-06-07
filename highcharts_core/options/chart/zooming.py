from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.chart.reset_zoom_button import ResetZoomButtonOptions

from highcharts_core import errors


class MouseWheelOptions(HighchartsMeta):
    """Configuration of zooming via the mouse wheel."""
    
    def __init__(self, **kwargs):
        self._enabled = None
        self._sensitivity = None
        self._type = None
        
        self.enabled = kwargs.get('enabled', None)
        self.sensitivity = kwargs.get('sensitivity', None)
        self.type = kwargs.get('type', None)
        
    @property
    def enabled(self) -> Optional[bool]:
        """Enables or disables zooming via the mouse wheel. Defaults to ``True``.
        
        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)
            
    @property
    def sensitivity(self) -> Optional[int | float | Decimal]:
        """Adjust the sensitivity of mouse wheel when controlling zoom. 
        
        A value of ``1`` is no sensitivity, while a value of ``2``, one mouse wheel 
        rotation will in ``50%``.
        
        Defaults to ``1.1``.
        
        :rtype: numeric
        """
        return self._sensitivity
    
    @sensitivity.setter
    def sensitivity(self, value):
        self._sensitivity = validators.numeric(value, allow_empty = True)
        
    @property
    def type(self) -> Optional[str]:
        """Decides in what dimensions the user can zoom scrolling the mouse wheel.
        Accepts one of ``'x'``, ``'y'`` or ``'xy'``. 
        
        If :obj:`None <python:None>`, it will inherit from
        :meth:`ZoomingOptions.type <highcharts_core.options.chart.zooming.ZoomingOptions.type>`.
        
        .. warning::
        
          Note that particularly when zooming via the mouse wheel in the ``'y'`` direction, 
          the zoom is affected by the default 
          :meth:`YAxisOptions.start_on_tick <highcharts_core.options.axes.YAxisOptions.start_on_tick>`
          and
          :meth:`YAxisOptions.end_on_tick <highcharts_core.options.axes.YAxisOptions.end_on_tick>`
          settings. 
          
          In order to respect these settings, the zoom level will adjust after the user has stopped 
          zooming. To prevent this, consider setting both those properties to ``False``.
          
        :rtype: :class:`str <python:str>`
        '"""
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['x', 'y', 'xy']:
                raise errors.HighchartsValueError(f'MouseWheelOptions.type expects a value '
                                                  f'of "x", "y", or "xy". Received: "{value}".')
            self._type = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'sensitivity': as_dict.get('sensitivity', None),
            'type': as_dict.get('type', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'sensitivity': self.sensitivity,
            'type': self.type,
        }

        return untrimmed


class ZoomingOptions(HighchartsMeta):
    """Chart zooming configuration."""

    def __init__(self, **kwargs):
        self._key = None
        self._mouse_wheel = None
        self._pinch_type = None
        self._reset_button = None
        self._single_touch = None
        self._type = None

        self.key = kwargs.get('key', None)
        self.mouse_wheel = kwargs.get('mouse_wheel', None)
        self.pinch_type = kwargs.get('pinch_type', None)
        self.reset_button = kwargs.get('reset_button', None)
        self.single_touch = kwargs.get('single_touch', None)
        self.type = kwargs.get('type', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'chart.zooming'

    @property
    def key(self) -> Optional[str]:
        """Sets a key to hold when dragging to zoom the chart.

        .. hint::

          This is useful to avoid zooming while moving points.

        .. hint::

          This should be set to a different key than
          :meth:`ChartOptions.pan_key <highcharts_core.options.chart.ChartOptions.pan_key>`.

        Accepts the following values:

          * ``'alt'``
          * ``'ctrl'``
          * ``'meta'`` (the command key on Mac and Windows key on Windows)
          * ``'shift'``.

        The keys are mapped directly to the key properties of the click event argument
        (``event.altKey``, ``event.ctrlKey``, ``event.metaKey``, and ``event.shiftKey``).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._key

    @key.setter
    def key(self, value):
        if not value:
            self._key = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['alt', 'ctrl', 'meta', 'shift']:
                raise errors.HighchartsValueError(f'pan_key expects a value of "alt", '
                                                  f'"ctrl", "meta", or "shift". Was: '
                                                  f'{value}')

            self._key = value

    @property
    def mouse_wheel(self) -> Optional[bool | MouseWheelOptions]:
        """Configuration of how users can use the mouse wheel to control zooming within the chart.
        
        .. note::
        
          Zooming via the mouse wheel is enabled by default. To disable, set this option to ``False``.
        
        .. note::
        
          Zooming via the mouse wheel is a feature included in 
          `Highcharts Stock <https://highcharts.com/products/stock>`__, but is also available 
          in `Highcharts Core <https://highcharts.com/products/highcharts>`__ by loading
          ``modules/mouse-wheel-zoom.js``.
          
        :rtype: :class:`bool <python:bool>`
        """
        return self._mouse_wheel
    
    @mouse_wheel.setter
    def mouse_wheel(self, value):
        if value is None:
            self._mouse_wheel = None
        else:
            try:
                value = validate_types(value, MouseWheelOptions)
            except (ValueError, TypeError):
                value = bool(value)
                
            if value is True:
                value = MouseWheelOptions(enabled = True)
                
            self._mouse_wheel = value

    @property
    def pinch_type(self) -> Optional[str]:
        """Equivalent to :meth:`.type <ZoomingOptions.type>` but for multi-touch gestures
        only. Defaults to ``'x'``.

        Accepts:

          * ``'x'``
          * ``'y'``
          * ``'xy'``
          * :obj:`None <python:None>`

        If not specified explicitly, the pinch type is the same as the
        :meth:`.type <ZoomingOptions.type>`. However, pinching can be enabled separately
        in some cases, for example in stock charts where a mouse drag pans the chart,
        while pinching is enabled. When :meth:`Tooltip.follow_touch_move` is ``True``,
        pinch type only applies to two-finger touches.

        :returns: The configuration of the pinch directional support.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pinch_type

    @pinch_type.setter
    def pinch_type(self, value):
        if not value:
            self._pinch_type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['x', 'y', 'xy']:
                raise errors.HighchartsValueError(f'pinch_type is expected to be either '
                                                  f'"x", "y", "xy", or None. Was: '
                                                  f'{value}')
            self._pinch_type = value

    @property
    def reset_button(self) -> Optional[ResetZoomButtonOptions]:
        """Configuration settings for the button that appears after a selection zoom,
        allowing the user to reset zoom.

        :rtype: :class:`ResetZoomButtonOptions` or :obj:`None <python:None>`
        """
        return self._reset_button

    @reset_button.setter
    @class_sensitive(ResetZoomButtonOptions)
    def reset_button(self, value):
        self._reset_button = value

    @property
    def single_touch(self) -> Optional[bool]:
        """If ``True``, enables zooming with a single touch (in combination with
        :meth:`.type <ZoomingOptions.type>`) while two-finger pinch will still work as per
        :meth:`.pinch_type <ZoomingOptions.pinch_type>`. Defaults to ``False``.

        .. warning::

          Enabling zoom by single touch will interfere with touch-dragging the chart to
          read the tooltip, and if vertical zooming is enabled will make it hard to scroll
          vertically on the page.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._single_touch

    @single_touch.setter
    def single_touch(self, value):
        if value is None:
            self._single_touch = None
        else:
            self._single_touch = bool(value)

    @property
    def type(self) -> Optional[str]:
        """Determines in which dimensions the user can zoom by dragging the mouse. By
        default, not set.

        Accepts:

          * ``'x'``
          * ``'y'``
          * ``'xy'``
          * :obj:`None <python:None>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['x', 'y', 'xy']:
                raise errors.HighchartsValueError(f'type is expected to be either '
                                                  f'"x", "y", "xy", or None. Was: '
                                                  f'{value}')
            self._type = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'key': as_dict.get('key', None),
            'mouse_wheel': as_dict.get('mouseWheel', None),
            'pinch_type': as_dict.get('pinchType', None),
            'reset_button': as_dict.get('resetButton', None),
            'single_touch': as_dict.get('singleTouch', None),
            'type': as_dict.get('type', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'key': self.key,
            'mouseWheel': self.mouse_wheel,
            'pinchType': self.pinch_type,
            'resetButton': self.reset_button,
            'singleTouch': self.single_touch,
            'type': self.type
        }

        return untrimmed
