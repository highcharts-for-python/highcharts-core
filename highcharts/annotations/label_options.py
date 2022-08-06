from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.annotations.points import AnnotationPoint
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.shadows import ShadowOptions


class AnnotationLabelOptionAccessibility(HighchartsMeta):
    """Accessibility options applied to an annotation label."""

    def __init__(self, **kwargs):
        self._description = None

        self.description = kwargs.pop('description', None)

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
        self._value = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.pop('description', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
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
        self._text = None
        self._use_html = None
        self._vertical_align = None
        self._x = None
        self._y = None

        self.accessibility = kwargs.pop('accessibility', None)
        self.align = kwargs.pop('align', None)
        self.allow_overlap = kwargs.pop('allow_overlap', None)
        self.background_color = kwargs.pop('background_color', None)
        self.border_color = kwargs.pop('border_color', None)
        self.border_radius = kwargs.pop('border_radius', None)
        self.border_width = kwargs.pop('border_width', None)
        self.class_name = kwargs.pop('class_name', None)
        self.crop = kwargs.pop('crop', None)
        self.distance = kwargs.pop('distance', None)
        self.format = kwargs.pop('format', None)
        self.formatter = kwargs.pop('formatter', None)
        self.include_in_data_export = kwargs.pop('include_in_data_export', None)
        self.overflow = kwargs.pop('overflow', None)
        self.padding = kwargs.pop('padding', None)
        self.shadow = kwargs.pop('shadow', None)
        self.shape = kwargs.pop('shape', None)
        self.style = kwargs.pop('style', None)
        self.text = kwargs.pop('text', None)
        self.use_html = kwargs.pop('use_html', None)
        self.vertical_align = kwargs.pop('vertical_align', None)
        self.x = kwargs.pop('x', None)
        self.y = kwargs.pop('y', None)

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
        f"""The alignment of the annotation's label. Defaults to
        ``'{constants.DEFAULT_LABEL_ALIGN}'``.

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
        f"""The background color or gradient for the annotation's label. Defaults to
        ``'{constants.DEFAULT_LABEL_BACKGROUND_COLOR}'``.

        :returns: The backgorund color for the annotation's label.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if not value:
            self._background_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._background_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._background_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Gradient.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._background_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._background_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Pattern.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._background_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_color(self) -> Optional[str]:
        f"""The border color for the annotation's label. Defaults to
        ``'{constants.DEFAULT_LABEL_BORDER_COLOR}'``.

        :returns: The border color for the annotation's label.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = validators.string(value, allow_empty = True)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        f"""The border radius (in pixels) applied to the annotation's label. Defaults to
        ``{constants.DEFAULT_LABEL_BORDER_RADIUS}``.

        :returns: The border radius to apply to the annotation's label.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        f"""The border width (in pixels) applied to the annotation's label. Defaults to
        ``{constants.DEFAULT_LABEL_BORDER_WIDTH}``.

        :returns: The border width to apply to the annotation's label.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        f"""A classname to apply styling using CSS. Defaults to
        ``'{constants.DEFAULT_LABEL_CLASS_NAME}'``.

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
    def formatter(self) -> Optional[str]:
        f"""JavaScript callback function to format the annotation's label.

        Defaults to {constants.DEFAULT_LABEL_FORMATTER}.

        .. note::

          If a :meth:`LabelOptions.format` or :meth:`LabelOptions.text` value are
          specified, the formatter will be ignored.

        .. hint::

          In the callback function, the use of ``this`` refers to a point object.

        :returns: A JavaScript callback function.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    def formatter(self, value):
        self._formatter = validators.string(value, allow_empty = True)

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
        f"""Configuration on how to handle an annotation label that overflows outside of
        the plot area.  Defaults to {constants.DEFAULT_LABEL_OVERFLOW}.

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
        f"""The padding within the border box when either
        :meth:`LabelOptions.border_width` or :meth:`LabelOptions.background_color` is set.

        Defaults to ``{constants.DEFAULT_LABEL_PADDING}``.

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
        f"""The name of the symbol to use for the border around the label. Defaults to
        ``'{constants.DEFAULT_LABEL_SHAPE}'``.

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
        self._style = validators.string(value, allow_empty = True)

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
        f"""The vertical alignment of the annotation's label. Defaults to
        {constants.DEFAULT_LABEL_VERTICAL_ALIGN}

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
        f"""The x position offset of the label relative to the point. Defaults to
        ``{constants.DEFAULT_LABEL_X}``.

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
        f"""The y position offset of the label relative to the point. Defaults to
        ``{constants.DEFAULT_LABEL_Y}``.

        .. note::

          If a :meth:`LabelOptions.distance` is defined, the distance takes precedence.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'align': as_dict.pop('align', None),
            'allow_overlap': as_dict.pop('allowOverlap', None),
            'background_color': as_dict.pop('backgroundColor', None),
            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'class_name': as_dict.pop('className', None),
            'crop': as_dict.pop('crop', None),
            'distance': as_dict.pop('distance', None),
            'format': as_dict.pop('format', None),
            'formatter': as_dict.pop('formatter', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'overflow': as_dict.pop('overflow', None),
            'padding': as_dict.pop('padding', None),
            'shadow': as_dict.pop('shadow', None),
            'shape': as_dict.pop('shape', None),
            'style': as_dict.pop('style', None),
            'text': as_dict.pop('text', None),
            'use_html': as_dict.pop('useHTML', None),
            'vertical_align': as_dict.pop('verticalAlign', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
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

        self.point = kwargs.pop('point', None)

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
    def from_dict(cls, as_dict):
        kwargs = {
            # from LabelOptions
            'accessibility': as_dict.pop('accessibility', None),
            'align': as_dict.pop('align', None),
            'allow_overlap': as_dict.pop('allowOverlap', None),
            'background_color': as_dict.pop('backgroundColor', None),
            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'class_name': as_dict.pop('className', None),
            'crop': as_dict.pop('crop', None),
            'distance': as_dict.pop('distance', None),
            'format': as_dict.pop('format', None),
            'formatter': as_dict.pop('formatter', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'overflow': as_dict.pop('overflow', None),
            'padding': as_dict.pop('padding', None),
            'shadow': as_dict.pop('shadow', None),
            'shape': as_dict.pop('shape', None),
            'style': as_dict.pop('style', None),
            'text': as_dict.pop('text', None),
            'use_html': as_dict.pop('useHTML', None),
            'vertical_align': as_dict.pop('verticalAlign', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            # from AnnotationLabel
            'point': as_dict.pop('point', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'point': self.point
        }
        parent_as_dict = super()._to_untrimmed_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


__all__ = [
    'LabelOptions',
    'AnnotationLabelOptionAccessibility',
    'ShadowOptions',
    'AnnotationLabel'
]
