from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.animation import AnimationOptions


class LegendNavigation(HighchartsMeta):
    """Options for paging or navigation within the legend when the legend overflows
    the available space.

    .. hint::

      Navigation works well on screen, but not in static exported images. One way of
      working around that is to increase the chart height in export.

    """

    def __init__(self, **kwargs):
        self._active_color = None
        self._animation = True
        self._arrow_size = None
        self._enabled = True
        self._inactive_color = None
        self._style = None

        self.active_color = kwargs.pop('active_color',
                                       constants.DEFAULT_LEGEND.get('navigation', {}).get('active_color'))
        self.animation = kwargs.pop('animation',
                                    True)
        self.arrow_size = kwargs.pop('arrow_size',
                                     constants.DEFAULT_LEGEND.get('navigation', {}).get('arrow_size'))
        self.enabled = kwargs.pop('enabled', True)
        self.inactive_color = kwargs.pop('inactive_color',
                                       constants.DEFAULT_LEGEND.get('navigation', {}).get('inactive_color'))
        self.style = kwargs.pop('style',
                                constants.DEFAULT_LEGEND.get('navigation', {}).get('style'))

    @property
    def active_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The color or gradient of the active up or down arrow in the legend page
        navigation. Defaults to
        ``'{constants.DEFAULT_LEGEND.get('navigation', {}).get('active_color')}'``.

        :returns: The color of the active up or down arrow in the legend page navigation.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._active_color

    @active_color.setter
    def active_color(self, value):
        if not value:
            self._active_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._active_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._active_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._active_color = Gradient.from_dict(value)
                else:
                    self._active_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._active_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._active_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._active_color = Pattern.from_dict(value)
                else:
                    self._active_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._active_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def animation(self) -> bool | AnimationOptions:
        """Determines how to animate the legend items when navigating up or down.

        A value of ``True`` applies the default navigation given in the
        :meth:`Chart.animation`` setting. Additional options can be given as an object
        containing values for easing and duration.

        :returns: The configuration settings for the annotation animation.
        :rtype: :class:`AnnotationAnimation`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if value is True:
            self._animation = True
        else:
            self._animation = validate_types(value, types = AnimationOptions)

    @property
    def arrow_size(self) -> Optional[int | float | Decimal]:
        f"""The pixel size of the up and down arrows in the legend paging navigation.
        Defaults to ``{constants.DEFAULT_LEGEND.get('navigation', {}).get('arrow_size')}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._arrow_size

    @arrow_size.setter
    def arrow_size(self, value):
        self._arrow_size = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> bool:
        """If ``True``, enables keyboard navigation for the legend. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @property
    def inactive_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The color or gradient of the inactive up or down arrow in the legend page
        navigation. Defaults to
        ``'{constants.DEFAULT_LEGEND.get('navigation', {}).get('inactive_color')}'``.

        :returns: The color of the active up or down arrow in the legend page navigation.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._inactive_color

    @inactive_color.setter
    def inactive_color(self, value):
        if not value:
            self._inactive_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._inactive_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._inactive_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._inactive_color = Gradient.from_dict(value)
                else:
                    self._inactive_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._inactive_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._inactive_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._inactive_color = Pattern.from_dict(value)
                else:
                    self._inactive_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._inactive_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the legend page navigation.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'active_color': as_dict.pop('activeColor',
                                        constants.DEFAULT_LEGEND.get('navigation', {}).get('active_color')),
            'animation': as_dict.pop('animation', True),
            'arrow_size': as_dict.pop('arrowSize',
                                      constants.DEFAULT_LEGEND.get('navigation', {}).get('arrow_size')),
            'enabled': as_dict.pop('enabled', True),
            'inactive_color': as_dict.pop('inactiveColor',
                                          constants.DEFAULT_LEGEND.get('navigation', {}).get('inactive_color')),
            'style': as_dict.pop('style',
                                 constants.DEFAULT_LEGEND.get('navigation', {}).get('style'))
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'activeColor': self.active_color,
            'animation': self.animation,
            'arrowSize': self.arrow_size,
            'enabled': self.enabled,
            'inactiveColor': self.inactive_color,
            'style': self.style
        }
        return self.trim_dict(untrimmed)
