from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.animation import AnimationOptions


class LegendNavigation(HighchartsMeta):
    """Options for paging or navigation within the legend when the legend overflows
    the available space.

    .. hint::

      Navigation works well on screen, but not in static exported images. One way of
      working around that is to increase the chart height in export.

    """

    def __init__(self, **kwargs):
        self._active_color = None
        self._animation = None
        self._arrow_size = None
        self._enabled = None
        self._inactive_color = None
        self._style = None

        self.active_color = kwargs.get('active_color', None)
        self.animation = kwargs.get('animation', None)
        self.arrow_size = kwargs.get('arrow_size', None)
        self.enabled = kwargs.get('enabled', None)
        self.inactive_color = kwargs.get('inactive_color', None)
        self.style = kwargs.get('style', None)

    @property
    def active_color(self) -> Optional[str | Gradient | Pattern]:
        """The color or gradient of the active up or down arrow in the legend page
        navigation. Defaults to
        ``'#003399'``.

        :returns: The color of the active up or down arrow in the legend page navigation.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._active_color

    @active_color.setter
    def active_color(self, value):
        from highcharts_core import utility_functions
        self._active_color = utility_functions.validate_color(value)

    @property
    def animation(self) -> Optional[bool | AnimationOptions]:
        """Determines how to animate the legend items when navigating up or down.

        A value of ``True`` applies the default navigation given in the
        :meth:`Chart.animation`` setting. Additional options can be given as an object
        containing values for easing and duration.

        :returns: The configuration settings for the annotation animation.
        :rtype: :class:`AnnotationAnimation` or :class:`bool <python:bool>` or
          :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if not value:
            self._animation = None
        elif value is True:
            self._animation = True
        else:
            self._animation = validate_types(value, types = AnimationOptions)

    @property
    def arrow_size(self) -> Optional[int | float | Decimal]:
        """The pixel size of the up and down arrows in the legend paging navigation.
        Defaults to ``12``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._arrow_size

    @arrow_size.setter
    def arrow_size(self, value):
        self._arrow_size = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables keyboard navigation for the legend. Defaults to ``True``.

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
    def inactive_color(self) -> Optional[str | Gradient | Pattern]:
        """The color or gradient of the inactive up or down arrow in the legend page
        navigation. Defaults to
        ``'#cccccc'``.

        :returns: The color of the active up or down arrow in the legend page navigation.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._inactive_color

    @inactive_color.setter
    def inactive_color(self, value):
        from highcharts_core import utility_functions
        self._inactive_color = utility_functions.validate_color(value)

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the legend page navigation.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True, coerce_value = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'active_color': as_dict.get('activeColor', None),
            'animation': as_dict.get('animation', None),
            'arrow_size': as_dict.get('arrowSize', None),
            'enabled': as_dict.get('enabled', None),
            'inactive_color': as_dict.get('inactiveColor', None),
            'style': as_dict.get('style', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'activeColor': self.active_color,
            'animation': self.animation,
            'arrowSize': self.arrow_size,
            'enabled': self.enabled,
            'inactiveColor': self.inactive_color,
            'style': self.style
        }
        return untrimmed
