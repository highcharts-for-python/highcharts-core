from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.options.plot_options.generic import GenericTypeOptions
from highcharts_core.options.plot_options.levels import SunburstLevelOptions, LevelSize
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.breadcrumbs import BreadcrumbOptions
from highcharts_core.utility_classes.shadows import ShadowOptions
from highcharts_core.utility_classes.data_labels import SunburstDataLabel


class SunburstOptions(GenericTypeOptions):
    """General options to apply to all Sunburst series types.

    A Sunburst displays hierarchical data, where a level in the hierarchy is
    represented by a circle. The center represents the root node of the tree. The
    visualization bears a resemblance to both treemap and pie charts.

    .. figure:: ../../../_static/sunburst-example.png
      :alt: Sunburst Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._color_index = None
        self._crisp = None
        self._shadow = None
        self._allow_traversing_tree = None
        self._border_color = None
        self._border_width = None
        self._breadcrumbs = None
        self._center = None
        self._color_by_point = None
        self._fill_color = None
        self._level_is_constant = None
        self._levels = None
        self._level_size = None
        self._root_id = None
        self._size = None
        self._sliced_offset = None
        self._start_angle = None

        self.color_index = kwargs.get('color_index', None)
        self.crisp = kwargs.get('crisp', None)
        self.shadow = kwargs.get('shadow', None)
        self.allow_traversing_tree = kwargs.get('allow_traversing_tree', None)
        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.breadcrumbs = kwargs.get('breadcrumbs', None)
        self.center = kwargs.get('center', None)
        self.color_by_point = kwargs.get('color_by_point', None)
        self.fill_color = kwargs.get('fill_color', None)
        self.level_is_constant = kwargs.get('level_is_constant', None)
        self.levels = kwargs.get('levels', None)
        self.level_size = kwargs.get('level_size', None)
        self.root_id = kwargs.get('root_id', None)
        self.size = kwargs.get('size', None)
        self.sliced_offset = kwargs.get('sliced_offset', None)
        self.start_angle = kwargs.get('start_angle', None)

        super().__init__(**kwargs)

    @property
    def allow_traversing_tree(self) -> Optional[bool]:
        """If ``True``, the user can click on a point which is a parent and zoom in on its
        children. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_traversing_tree

    @allow_traversing_tree.setter
    def allow_traversing_tree(self, value):
        if value is None:
            self._allow_traversing_tree = None
        else:
            self._allow_traversing_tree = bool(value)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each slice. When :obj:`None <python:None>`,
        the border takes the same color as the slice fill. This can be used together with
        a :meth:`border_width <SunburstOptions.border_width>` to fill drawing gaps created by
        antialiazing artefacts in borderless pies. Defaults to ``'#ffffff'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts_core import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding each slice. Defaults to ``1``.

        When setting the border width to ``0``, there may be small gaps between the slices
        due to SVG antialiasing artefacts. To work around this, keep the border width at
        ``0.5`` or ``1``, but set the :meth:`border_color <SunburstOptions.border_color>` to
        :obj:`None <python:None>` instead.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def breadcrumbs(self) -> Optional[BreadcrumbOptions]:
        """Options for the breadcrumbs, the navigation at the top leading the way up
        through the traversed levels. Defaults to :obj:`None <python:None>`.

        """
        return self._breadcrumbs

    @breadcrumbs.setter
    @class_sensitive(BreadcrumbOptions)
    def breadcrumbs(self, value):
        self._breadcrumbs = value

    @property
    def center(self) -> Optional[List[str | int | float | Decimal | constants.EnforcedNullType]]:
        """The center of the sunburst chart relative to the plot area.

        Can be percentages or pixel values. The default behaviour if
        :obj:`None <python:None>` is to center the pie so that all slices and data labels
        are within the plot area. As a consequence, the pie may actually jump around in a
        chart with dynamic values, as the data labels move. In that case, the center
        should be explicitly set, for example to ``["50%", "50%"]``.

        Defaults to ``['50%', '50%']``.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of numeric or
          :class:`str <python:str>` values
        """
        return self._center

    @center.setter
    def center(self, value):
        if not value:
            self._center = None
        else:
            value = validators.iterable(value)
            if len(value) != 2:
                raise errors.HighchartsValueError(f'center expects a 2-member array. '
                                                  f'Received a {len(value)}-member '
                                                  f'array.')
            processed_values = []
            for item in value:
                try:
                    item = validators.string(item)
                    if '%' not in item:
                        raise errors.HighchartsValueError('center expects either numbers '
                                                          'or percentage strings. No "%" '
                                                          'character found in string '
                                                          'received.')
                except TypeError:
                    item = validators.numeric(item)

                processed_values.append(item)

            self._center = processed_values

    @property
    def color_by_point(self) -> Optional[bool]:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        if value is None:
            self._color_by_point = None
        else:
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
    def data_labels(self) -> Optional[SunburstDataLabel | List[SunburstDataLabel]]:
        """Options for the series data labels, appearing next to each data point.

        .. note::

          To have multiple data labels per data point, you can also supply a collection of
          :class:`DataLabel` configuration settings.

        :rtype: :class:`SunburstDataLabel <highcharts_core.utility_classes.data_labels.SunburstDataLabel>`, 
          :class:`list <python:list>` of 
            :class:`SunburstDataLabel <highcharts_core.utility_classes.data_labels.SunburstDataLabel>` or
            :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    def data_labels(self, value):
        if not value:
            self._data_labels = None
        else:
            if checkers.is_iterable(value):
                self._data_labels = validate_types(value,
                                                   types = SunburstDataLabel,
                                                   allow_none = False,
                                                   force_iterable = True)
            else:
                self._data_labels = validate_types(value,
                                                   types = SunburstDataLabel,
                                                   allow_none = False)

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """If the total sum of the pie's values is ``0``, the series is represented as an
        empty circle . The ``fill_color`` setting defines the color of that circle.
        Use :meth:`SunburstOptions.border_width` to set the border thickness.

        Defaults to :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, or :class:`Pattern`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        from highcharts_core import utility_functions
        self._fill_color = utility_functions.validate_color(value)

    @property
    def level_is_constant(self) -> Optional[bool]:
        """If ``True``, the level will be the same as the tree structure. If ``False``,
        the first level visible when drilling is considered to be level one. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._level_is_constant

    @level_is_constant.setter
    def level_is_constant(self, value):
        if value is None:
            self._level_is_constant = None
        else:
            self._level_is_constant = bool(value)

    @property
    def levels(self) -> Optional[List[SunburstLevelOptions]]:
        """Set options on specific levels. Takes precedence over series options, but not
        node and link options.

        :rtype: :obj:`None <python:None>`, or :class:`list <python:list>` of
          :class:`SunburstLevelOptions`
        """
        return self._levels

    @levels.setter
    @class_sensitive(SunburstLevelOptions, force_iterable = True)
    def levels(self, value):
        self._levels = value

    @property
    def level_size(self) -> Optional[LevelSize]:
        """Determines the width of the ring per level.

        :rtype: :class:`LevelSize` or :obj:`None <python:None>`
        """
        return self._level_size

    @level_size.setter
    @class_sensitive(LevelSize)
    def level_size(self, value):
        self._level_size = value

    @property
    def root_id(self) -> Optional[str]:
        """Indicates which point to use as a root in the visualization. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._root_id

    @root_id.setter
    def root_id(self, value):
        self._root_id = validators.string(value, allow_empty = True)

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

    @property
    def size(self) -> Optional[str | int]:
        """The diameter of the pie relative to the plot area, expressed as a percentage or
        pixel value given as an integer.

        If :obj:`None <python:None>`, scales the pie to the plot area and gives room for
        data labels within the plot area.

        .. note::

          :meth:`SunburstOptions.sliced_offset` is also included in the default size
          calculation. As a consequence, the size of the pie may vary when points are
          updated and data labels more around. In that case it is best to set a fixed
          value, for example ``"75%"``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._size

    @size.setter
    def size(self, value):
        if value is None:
            self._size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError(f'size expects either a number or '
                                                      f'a % string. Received: {value}')
            except TypeError:
                value = validators.integer(value, minimum = 0)

            self._size = value

    @property
    def sliced_offset(self) -> Optional[int | float | Decimal]:
        """If a point is sliced, moved out from the center, how many pixels should it be
        moved? Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._sliced_offset

    @sliced_offset.setter
    def sliced_offset(self, value):
        self._sliced_offset = validators.numeric(value, allow_empty = True)

    @property
    def start_angle(self) -> Optional[int | float | Decimal]:
        """The start angle of the dependency wheel, in degrees where ``0`` is up. Defaults
        to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._start_angle

    @start_angle.setter
    def start_angle(self, value):
        self._start_angle = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0,
                                               maximum = 360)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'allow_traversing_tree': as_dict.get('allowTraversingTree', None),
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'breadcrumbs': as_dict.get('breadcrumbs', None),
            'center': as_dict.get('center', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'color_index': as_dict.get('colorIndex', None),
            'crisp': as_dict.get('crisp', None),
            'fill_color': as_dict.get('fillColor', None),
            'level_is_constant': as_dict.get('levelIsConstant', None),
            'levels': as_dict.get('levels', None),
            'level_size': as_dict.get('levelSize', None),
            'root_id': as_dict.get('rootId', None),
            'shadow': as_dict.get('shadow', None),
            'size': as_dict.get('size', None),
            'sliced_offset': as_dict.get('slicedOffset', None),
            'start_angle': as_dict.get('startAngle', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allowTraversingTree': self.allow_traversing_tree,
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'breadcrumbs': self.breadcrumbs,
            'center': self.center,
            'colorByPoint': self.color_by_point,
            'colorIndex': self.color_index,
            'crisp': self.crisp,
            'fillColor': self.fill_color,
            'levelIsConstant': self.level_is_constant,
            'levels': self.levels,
            'levelSize': self.level_size,
            'rootId': self.root_id,
            'shadow': self.shadow,
            'size': self.size,
            'slicedOffset': self.sliced_offset,
            'startAngle': self.start_angle
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
