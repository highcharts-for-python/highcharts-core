from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.constants import EnforcedNullType
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.animation import AnimationOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class Halo(HighchartsMeta):
    """Options for configuring the halo state of a series or data point."""

    def __init__(self, **kwargs):
        self._attributes = None
        self._opacity = None
        self._size = None

        self.attributes = kwargs.get("attributes", None)
        self.opacity = kwargs.get("opacity", None)
        self.size = kwargs.get("size", None)

    @property
    def attributes(self) -> Optional[dict]:
        """A collection of SVG attributes to override the appearance of the halo, for example
        ``fill``, ``stroke`` and ``stroke-width``.

        Attribute names should be provided as keys, and values should be provided as values.

        :rtype: :class:`dict <python:dict>`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, value: Optional[dict] = None):
        if not value:
            self._attributes = None
        else:
            value = validate_types(value, dict)
            self._attributes = value

    @property
    def opacity(self) -> Optional[int | float | Decimal]:
        """Opacity for the halo unless a specific fill is overridden using the
        :attr:`.attributes <highcharts_core.utility_classes.states.Halo.attributes>` setting.
        Defaults to ``0.25``.

        .. note::

          Highcharts is only able to apply opacity to colors of hex or rgb(a) formats.

        :rtype: numeric

        """
        return self._opacity

    @opacity.setter
    def opacity(self, value: Optional[int | float | Decimal] = None):
        self._opacity = validators.numeric(value, allow_empty=True)

    @property
    def size(self) -> Optional[int | float | Decimal]:
        """The pixel size of the halo (or radius for point markers and width of the halo outside the bubble for bubbles). Defaults to ``10``, except for bubbles where it defaults to ``5``.

        :rtype: numeric
        """
        return self._size

    @size.setter
    def size(self, value: Optional[int | float | Decimal] = None):
        self._size = validators.numeric(value, allow_empty=True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "attributes": as_dict.get("attributes", None),
            "opacity": as_dict.get("opacity", None),
            "size": as_dict.get("size", None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "attributes": self.attributes,
            "opacity": self.opacity,
            "size": self.size,
        }

        return untrimmed


class HoverState(HighchartsMeta):
    """Options for the hovered point/series."""

    def __init__(self, **kwargs):
        self._animation = None
        self._border_color = None
        self._brightness = None
        self._color = None
        self._enabled = None
        self._halo = None
        self._line_width = None
        self._line_width_plus = None
        self._link_opacity = None
        self._opacity = None

        self.animation = kwargs.get("animation", None)
        self.border_color = kwargs.get("border_color", None)
        self.brightness = kwargs.get("brightness", None)
        self.color = kwargs.get("color", None)
        self.enabled = kwargs.get("enabled", None)
        self.halo = kwargs.get("halo", None)
        self.line_width = kwargs.get("line_width", None)
        self.line_width_plus = kwargs.get("line_width_plus", None)
        self.opacity = kwargs.get("opacity", None)
        self.link_opacity = kwargs.get("link_opacity", None)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Animation setting for hovering the graph in line-type series.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """A specific border color for the hovered point. If :obj:`None <python:None>`,
        defaults to inherit the normal state border color.

        :returns: The border color for the hovered point.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions

        self._border_color = utility_functions.validate_color(value)

    @property
    def brightness(self) -> Optional[int | float | Decimal]:
        """How much to brighten the point on interaction. Defaults to ``0.1``.

        Requires the main color to be defined in hex or rgb(a) format.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = validators.numeric(value, allow_empty=True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """A specific color for the hovered point.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern`, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions

        self._color = utility_functions.validate_color(value)

    @property
    def color(self) -> Optional[str]:
        """A specific color for the hovered point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty=True)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable separate styles for the hovered series to visualize that the user hovers
        either the series itself or the legend. Defaults to ``True``.

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
    def halo(self) -> Optional[Halo | EnforcedNullType]:
        """Options for configuring the halo that appears around the hovered point.

        .. note::

          By default, the halo is filled by the current point or series color with an opacity of
          ``0.25``. The halo can be disabled by setting the ``.halo`` property to :obj:`EnforcedNull <constants.EnforcedNull>`.

        """
        return self._halo

    @halo.setter
    @class_sensitive(types=(Halo, EnforcedNullType))
    def halo(self, value: Optional[Halo | EnforcedNullType] = None):
        self._halo = value

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the graph line. By default this property is :obj:`None <python:None>`,
        and the :attr:`.line_width_plus <highcharts_core.utility_classes.states.HoverState.line_width_plus>`
        property dictates how much to increase the line width from normal state.

        :rtype: numeric
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value: Optional[int | float | Decimal] = None):
        self._line_width = validators.numeric(value, allow_empty=True)

    @property
    def line_width_plus(self) -> Optional[int | float | Decimal]:
        """The additional line width for the graph line. Defaults to ``1``.

        :rtype: numeric
        """
        return self._line_width_plus

    @line_width_plus.setter
    def line_width_plus(self, value: Optional[int | float | Decimal] = None):
        self._line_width_plus = validators.numeric(value, allow_empty=True)

    @property
    def opacity(self) -> Optional[int | float | Decimal]:
        """Opacity for nodes in the Sankey or related diagrams in hover mode. Defaults to
        ``1``.

        :rtype: numeric
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value: Optional[int | float | Decimal] = None):
        self._opacity = validators.numeric(value, allow_empty=True)

    @property
    def link_opacity(self) -> Optional[int | float | Decimal]:
        """Opacity for the links between nodes in Sankey or related diagrams in hover mode.

        Defaults to ``1``.

        :rtype: numeric
        """
        return self._link_opacity

    @link_opacity.setter
    def link_opacity(self, value: Optional[int | float | Decimal] = None):
        self._link_opacity = validators.numeric(value, allow_empty=True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "animation": as_dict.get("animation", None),
            "border_color": as_dict.get("borderColor", None),
            "brightness": as_dict.get("brightness", None),
            "color": as_dict.get("color", None),
            "enabled": as_dict.get("enabled", None),
            "halo": as_dict.get("halo", None),
            "line_width": as_dict.get("lineWidth", None),
            "line_width_plus": as_dict.get("lineWidthPlus", None),
            "opacity": as_dict.get("opacity", None),
            "link_opacity": as_dict.get("linkOpacity", None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "animation": self.animation,
            "borderColor": self.border_color,
            "brightness": self.brightness,
            "color": self.color,
            "enabled": self.enabled,
            "halo": self.halo,
            "lineWidth": self.line_width,
            "lineWidthPlus": self.line_width_plus,
            "opacity": self.opacity,
            "linkOpacity": self.link_opacity,
        }

        return untrimmed


class InactiveState(HighchartsMeta):
    """Options for the oppositive of a hovered point/series."""

    def __init__(self, **kwargs):
        self._animation = None
        self._enabled = None
        self._opacity = None

        self.animation = kwargs.get("animation", None)
        self.enabled = kwargs.get("enabled", None)
        self.opacity = kwargs.get("opacity", None)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Animation setting when not hovering over the marker.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def enabled(self) -> Optional[bool]:
        """Enable or disable the inactive state for the series. Defaults to ``True``.

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
    def opacity(self) -> Optional[int | float | Decimal]:
        """Opacity of series elements (dataLabels, line, area). Defaults to ``0.2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.numeric(value, allow_empty=True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "animation": as_dict.get("animation", None),
            "enabled": as_dict.get("enabled", None),
            "opacity": as_dict.get("opacity", None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "animation": self.animation,
            "enabled": self.enabled,
            "opacity": self.opacity,
        }

        return untrimmed


class NormalState(HighchartsMeta):
    """Options for returning to a normal state after hovering"""

    def __init__(self, **kwargs):
        self._animation = None

        self.animation = kwargs.get("animation", None)

    @property
    def animation(self) -> Optional[bool | AnimationOptions]:
        """Animation setting when returning to a normal state after hovering. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :class:`AnimationOptions` or
          :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if isinstance(value, bool):
            self._animation = value
        else:
            self._animation = validate_types(value, types=AnimationOptions)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {"animation": as_dict.get("animation", None)}

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {"animation": self.animation}

        return untrimmed


class SelectState(HighchartsMeta):
    """Options for the selected point. These settings override the normal state options
    when a point is selected."""

    def __init__(self, **kwargs):
        self._animation = None
        self._border_color = None
        self._color = None
        self._enabled = None

        self.animation = kwargs.get("animation", None)
        self.border_color = kwargs.get("border_color", None)
        self.color = kwargs.get("color", None)
        self.enabled = kwargs.get("enabled", None)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Animation setting for hovering the graph in line-type series.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """A specific border color for the selected point. Defaults to ``'#000000'``.

        :returns: The border color for the hovered point.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions

        self._border_color = utility_functions.validate_color(value)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """A specific color for the selected point. Defaults to ``'#cccccc'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern`, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions

        self._color = utility_functions.validate_color(value)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable separate styles for the hovered series to visualize that the user hovers
        either the series itself or the legend. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "animation": as_dict.get("animation", None),
            "border_color": as_dict.get("borderColor", None),
            "color": as_dict.get("color", None),
            "enabled": as_dict.get("enabled", None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "animation": self.animation,
            "borderColor": self.border_color,
            "color": self.color,
            "enabled": self.enabled,
        }

        return untrimmed


class States(HighchartsMeta):
    """Collection of state configuration settings that can be applied to series or
    markers."""

    def __init__(self, **kwargs):
        self._hover = None
        self._inactive = None
        self._normal = None
        self._select = None

        self.hover = kwargs.get("hover", None)
        self.inactive = kwargs.get("inactive", None)
        self.normal = kwargs.get("normal", None)
        self.select = kwargs.get("select", None)

    @property
    def hover(self) -> Optional[HoverState]:
        """Options for the hovered point/series.

        .. note::

          These settings override the normal state  options when a point/series is moused
          over or touched.

        :rtype: :class:`HoverState` or :obj:`None <python:None>`
        """
        return self._hover

    @hover.setter
    @class_sensitive(HoverState)
    def hover(self, value):
        self._hover = value

    @property
    def inactive(self) -> Optional[InactiveState]:
        """The opposite state of a hover for a series/point.

        :rtype: :class:`InactiveState` or :obj:`None <python:None>`
        """
        return self._inactive

    @inactive.setter
    @class_sensitive(InactiveState)
    def inactive(self, value):
        self._inactive = value

    @property
    def normal(self) -> Optional[NormalState]:
        """The normal state of a series, or for point items in column, pie and similar
        series.

        Currently only used for setting animation when returning to normal state from
        hover.

        :rtype: :class:`NormalState` or :obj:`None <python:None>`
        """
        return self._normal

    @normal.setter
    @class_sensitive(NormalState)
    def normal(self, value):
        self._normal = value

    @property
    def select(self) -> Optional[SelectState]:
        """Options for the selected point.

        These settings override the normal state options when a point is selected.

        :rtype: :class:`SelectState` or :obj:`None <python:None>`
        """
        return self._select

    @select.setter
    @class_sensitive(SelectState)
    def select(self, value):
        self._select = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "hover": as_dict.get("hover", None),
            "inactive": as_dict.get("inactive", None),
            "normal": as_dict.get("normal", None),
            "select": as_dict.get("select", None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "hover": self.hover,
            "inactive": self.inactive,
            "normal": self.normal,
            "select": self.select,
        }

        return untrimmed
