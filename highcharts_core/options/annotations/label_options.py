from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.options.annotations.points import AnnotationPoint
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.shadows import ShadowOptions
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class AnnotationLabelOptionAccessibility(HighchartsMeta):
    """Accessibility options applied to an annotation label."""

    def __init__(self, **kwargs):
        self._description = None

        self.description = kwargs.get('description', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations.labelOptions.accessibility'

    @property
    def description(self) -> Optional[str]:
        """Description of an annotation label for screen readers and other assistive
        technology.

        :returns: Description of an annotation label
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.get('description', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'description': self.description
        }

        return untrimmed


class LabelOptions(HighchartsMeta):
    """Options applied to all annotation labels."""

    def __init__(self, **kwargs):
        self._accessibility = None
        self._align = None
        self._allow_overlap = None
        self._background_color = None
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._class_name = None
        self._crop = None
        self._distance = None
        self._format = None
        self._formatter = None
        self._include_in_data_export = None
        self._overflow = None
        self._padding = None
        self._shadow = None
        self._shape = None
        self._style = None
        self._use_html = None
        self._vertical_align = None
        self._x = None
        self._y = None

        self.accessibility = kwargs.get('accessibility', None)
        self.align = kwargs.get('align', None)
        self.allow_overlap = kwargs.get('allow_overlap', None)
        self.background_color = kwargs.get('background_color', None)
        self.border_color = kwargs.get('border_color', None)
        self.border_radius = kwargs.get('border_radius', None)
        self.border_width = kwargs.get('border_width', None)
        self.class_name = kwargs.get('class_name', None)
        self.crop = kwargs.get('crop', None)
        self.distance = kwargs.get('distance', None)
        self.format = kwargs.get('format', None)
        self.formatter = kwargs.get('formatter', None)
        self.include_in_data_export = kwargs.get('include_in_data_export', None)
        self.overflow = kwargs.get('overflow', None)
        self.padding = kwargs.get('padding', None)
        self.shadow = kwargs.get('shadow', None)
        self.shape = kwargs.get('shape', None)
        self.style = kwargs.get('style', None)
        self.text = kwargs.get('text', None)
        self.use_html = kwargs.get('use_html', None)
        self.vertical_align = kwargs.get('vertical_align', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations.labelOptions'

    @property
    def accessibility(self) -> Optional[AnnotationLabelOptionAccessibility]:
        """Accessibility options applied to an annotation label.

        :returns: Accessibility options applied to an annotation label.
        :rtype: :class:`AnnotationLabelOptionAccessibility` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(AnnotationLabelOptionAccessibility)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def align(self) -> Optional[str]:
        """The alignment of the annotation's label. Defaults to
        ``'center'``.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        .. hint::

          If right, the right side of the label should be touching the point.

        :returns: The alignment of the annotation's label.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._align

    @align.setter
    def align(self, value):
        if not value:
            self._align = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'align must be either "left", '
                                                  f'"center", or "right". Was: {value}')

            self._align = value

    @property
    def allow_overlap(self) -> Optional[bool]:
        """If ``True``, annotation labels are allowed to overlap each other.

        Defaults to ``False``.

        :returns: Flag indicating whether to allow annotation labels to overlap.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_overlap

    @allow_overlap.setter
    def allow_overlap(self, value):
        if value is None:
            self._allow_overlap = None
        else:
            self._allow_overlap = bool(value)

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or gradient for the annotation's label. Defaults to
        ``'rgba(0, 0, 0, 0.75)'``.

        :returns: The backgorund color for the annotation's label.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        from highcharts_core import utility_functions
        self._background_color = utility_functions.validate_color(value)

    @property
    def border_color(self) -> Optional[str]:
        """The border color for the annotation's label. Defaults to
        ``'#000000'``.

        :returns: The border color for the annotation's label.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = validators.string(value, allow_empty = True)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The border radius (in pixels) applied to the annotation's label. Defaults to
        ``3``.

        :returns: The border radius to apply to the annotation's label.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width (in pixels) applied to the annotation's label. Defaults to
        ``1``.

        :returns: The border width to apply to the annotation's label.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS. Defaults to
        ``'highcharts-no-tooltip'``.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def crop(self) -> Optional[bool]:
        """If ``True``, hide part of the annotation label that falls outside the plot
        area. Defaults to ``False``.

        :returns: Flag indicating whether to clip an annotation label that extends beyond
          the plot area.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crop

    @crop.setter
    def crop(self, value):
        if value is None:
            self._crop = None
        else:
            self._crop = bool(value)

    @property
    def distance(self) -> Optional[int | float | Decimal]:
        """The label's distance in pixels from the point.

        :returns: The label's distance in pixels from the point.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = validators.numeric(value,
                                            allow_empty = True)

    @property
    def format(self) -> Optional[str]:
        """A format string to apply to the label.

        .. seealso:

          * :meth:`PlotOptions.series.data_labels`

        :returns: The format string to apply to the labels.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format

    @format.setter
    def format(self, value):
        self._format = validators.string(value, allow_empty = True)

    @property
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript callback function to format the annotation's label.

        Defaults to ``function () { return defined(this.y) ? this.y : 'Annotation label'; }``.

        .. note::

          If a :meth:`LabelOptions.format` or :meth:`LabelOptions.text` value are
          specified, the formatter will be ignored.

        .. hint::

          In the callback function, the use of ``this`` refers to a point object.

        :returns: A JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @property
    def include_in_data_export(self) -> Optional[bool]:
        """If ``True``, the annotation is visible in the exported data table. Defaults to
        ``True``.

        :returns: Flag indicating whether to include the annotation label in the chart's
          exported data table.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._include_in_data_export

    @include_in_data_export.setter
    def include_in_data_export(self, value):
        if value is None:
            self._include_in_data_export = None
        else:
            self._include_in_data_export = bool(value)

    @property
    def overflow(self) -> Optional[str]:
        """Configuration on how to handle an annotation label that overflows outside of
        the plot area.  Defaults to ``'justify'``.

        Accepts:

          * ``'justify'`` - which forces the label back into the plot area
          * ``'none'`` - which applies no change

        .. note::

          The overflow treatment is also affected by the :meth:`LabelOptions.crop`
          setting.

        :returns: Configuration of overflow setting.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._overflow

    @overflow.setter
    def overflow(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._overflow = None
        else:
            value = value.lower()
            if value not in ['justify', 'none']:
                raise errors.HighchartsValueError(f'overflow accepts "justify" or "none".'
                                                  f' Was: {value}')
            self._overflow = value

    @property
    def padding(self) -> Optional[int]:
        """The padding within the border box when either
        :meth:`LabelOptions.border_width` or :meth:`LabelOptions.background_color` is set.

        Defaults to ``5``.

        :returns: The padding to apply to the annotation label.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validators.numeric(value, allow_empty = True)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
        """Configuration for the shadow to apply to the annotation box. Defaults to
        ``False``.

        If ``False``, no shadow is applied.

        :returns: The shadow configuration to apply or ``False``.
        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions` or
          :obj:`None <python:None>`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if value is None:
            self._shadow = None
        elif isinstance(value, bool) and value is False:
            self._shadow = False
        else:
            value = validate_types(value,
                                   types = ShadowOptions)
            self._shadow = value

    @property
    def shape(self) -> Optional[str]:
        """The name of the symbol to use for the border around the label. Defaults to
        ``'callout'``.

        Accepts:

          * ``'connector'``
          * ``'rect'``
          * ``'circle'``
          * ``'diamond'``
          * ``'triangle'``
          * ``'callout'``

        :returns: The shape to use for the border around the label.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._shape

    @shape.setter
    def shape(self, value):
        if not value:
            self._shape = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['callout',
                             'connector',
                             'rect',
                             'circle',
                             'diamond',
                             'triangle']:
                raise errors.HighchartsValueError(f'shape expects a supported annotation '
                                                  f'label shape. Was: {value}')
            self._shape = value

    @property
    def style(self) -> Optional[str]:
        """CSS styling to apply to the annotation's label.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True, coerce_value = True)

    @property
    def text(self) -> Optional[str]:
        """Alias for the :meth:`LabelOptions.format` property.

        :returns: The format string to apply to the labels.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._format

    @text.setter
    def text(self, value):
        self.format = value

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the annotation's label. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render annotation labels using HTML.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        if value is None:
            self._use_html = None
        else:
            self._use_html = bool(value)

    @property
    def vertical_align(self) -> Optional[str]:
        """The vertical alignment of the annotation's label. Defaults to
        ``'bottom'``

        Accepts:

          * ``'bottom'``
          * ``'middle'``
          * ``'top'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._vertical_align = None
        else:
            value = value.lower()
            if value not in ['bottom', 'middle', 'top']:
                raise errors.HighchartsValueError(f'vertical_align expects either "top", '
                                                  f'"middle", or "bottom". Was: {value}')
            self._vertical_align = value

    @property
    def x(self) -> Optional[int]:
        """The x position offset of the label relative to the point. Defaults to
        ``0``.

        .. note::

          If a :meth:`LabelOptions.distance` is defined, the distance takes precedence.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int]:
        """The y position offset of the label relative to the point. Defaults to
        ``-16``.

        .. note::

          If a :meth:`LabelOptions.distance` is defined, the distance takes precedence.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'crop': as_dict.get('crop', None),
            'distance': as_dict.get('distance', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'overflow': as_dict.get('overflow', None),
            'padding': as_dict.get('padding', None),
            'shadow': as_dict.get('shadow', None),
            'shape': as_dict.get('shape', None),
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'align': self.align,
            'allowOverlap': self.allow_overlap,
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'crop': self.crop,
            'distance': self.distance,
            'format': self.format,
            'formatter': self.formatter,
            'includeInDataExport': self.include_in_data_export,
            'overflow': self.overflow,
            'padding': self.padding,
            'shadow': self.shadow,
            'shape': self.shape,
            'style': self.style,
            'text': self.text,
            'useHTML': self.use_html,
            'verticalAlign': self.vertical_align,
            'x': self.x,
            'y': self.y
        }

        return untrimmed


class AnnotationLabel(LabelOptions):
    """Configuration for an annotation label applied to a specific point.

    Used to override the global settings configured in :class:`LabelOptions` and applied
    via :meth:`Annotation.label_options`.

    """

    def __init__(self, **kwargs):
        self._point = None

        self.point = kwargs.get('point', None)

        super().__init__(**kwargs)

    @property
    def point(self) -> Optional[str | AnnotationPoint]:
        """Determines the point to which the label will be connected.

        It can be either the ID of the point which exists in the series, or a new point
        with defined x, y properties and optionally axes.

        :rtype: :class:`str <python:str>` or :class:`AnnotationPoint` or
          :obj:`None <python:None>`

        :raises HighchartsValueError: if cannot resolve the value to an allowed type
        """
        return self._point

    @point.setter
    def point(self, value):
        if not value:
            self._point = None
        elif isinstance(value, AnnotationPoint):
            self._point = value
        elif isinstance(value, str):
            try:
                self._point = AnnotationPoint.from_json(value)
            except ValueError:
                self._point = validators.string(value)
        elif isinstance(value, dict):
            self._point = AnnotationPoint.from_dict(value)
        else:
            raise errors.HighchartsValueError('Unable to resolve the value supplied to a '
                                              'supported type.')

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            # from LabelOptions
            'accessibility': as_dict.get('accessibility', None),
            'align': as_dict.get('align', None),
            'allow_overlap': as_dict.get('allowOverlap', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'crop': as_dict.get('crop', None),
            'distance': as_dict.get('distance', None),
            'format': as_dict.get('format', None),
            'formatter': as_dict.get('formatter', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'overflow': as_dict.get('overflow', None),
            'padding': as_dict.get('padding', None),
            'shadow': as_dict.get('shadow', None),
            'shape': as_dict.get('shape', None),
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None),
            'use_html': as_dict.get('useHTML', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),

            # from AnnotationLabel
            'point': as_dict.get('point', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'point': self.point
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


__all__ = [
    'LabelOptions',
    'AnnotationLabelOptionAccessibility',
    'ShadowOptions',
    'AnnotationLabel'
]
