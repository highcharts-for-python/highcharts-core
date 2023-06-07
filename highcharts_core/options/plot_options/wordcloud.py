from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors, utility_functions
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.plot_options.generic import GenericTypeOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class RotationOptions(HighchartsMeta):
    """Configuration of the allowed rotations for words in the wordcloud."""

    def __init__(self, **kwargs):
        self._from = None
        self._orientations = None
        self._to = None

        self.from_ = kwargs.get('from_', None)
        self.orientations = kwargs.get('orientations', None)
        self.to = kwargs.get('to', None)

    @property
    def from_(self) -> Optional[int | float | Decimal]:
        """The smallest degree of rotation allowed for a word. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._from

    @from_.setter
    def from_(self, value):
        self._from = validators.numeric(value,
                                        allow_empty = True,
                                        minimum = 0)

    @property
    def orientations(self) -> Optional[int]:
        """The number of possible orientations for a word, within the range of
        :meth:`RotationOptions.from_` and :meth:`RotationOptions.to`. Defaults to ``2``.

        .. warning::

          Must be a number larger than 0.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._orientations

    @orientations.setter
    def orientations(self, value):
        self._orientations = validators.integer(value,
                                                allow_empty = True,
                                                minimum = self.from_,
                                                maximum = self.to)

    @property
    def to(self) -> Optional[int | float | Decimal]:
        """The largest degree of rotation allowed for a word. Defaults to ``90``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.numeric(value,
                                      allow_empty = True,
                                      minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'from_': as_dict.get('from', None),
            'orientations': as_dict.get('orientations', None),
            'to': as_dict.get('to', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'from': self.from_,
            'orientations': self.orientations,
            'to': self.to
        }

        return untrimmed


class WordcloudOptions(GenericTypeOptions):
    """General options to apply to all Wordcloud series types.

    A word cloud is a visualization of a set of words, where the size and placement of
    a word is determined by how it is weighted.

    .. figure:: ../../../_static/wordcloud-example.png
      :alt: Wordcloud Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        # Copied From SeriesOptions
        self._animation_limit = None
        self._color_index = None
        self._color_key = None
        self._relative_x_value = None

        # Copied from BaseBarOptions
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._center_in_category = None
        self._color_by_point = None
        self._colors = None
        self._edge_width = None

        # Native to WordcloudOptions
        self._allow_extend_playing_field = None
        self._max_font_size = None
        self._min_font_size = None
        self._placement_strategy = None
        self._rotation = None
        self._spiral = None

        # Copied from SeriesOptions
        self.animation_limit = kwargs.get('animation_limit', None)
        self.color_index = kwargs.get('color_index', None)
        self.color_key = kwargs.get('color_key', None)
        self.relative_x_value = kwargs.get('relative_x_value', None)

        # Copied from BaseBarOptions
        self.border_color = kwargs.get('border_color', None)
        self.border_radius = kwargs.get('border_radius', None)
        self.border_width = kwargs.get('border_width', None)
        self.center_in_category = kwargs.get('center_in_category', None)
        self.color_by_point = kwargs.get('color_by_point', None)
        self.colors = kwargs.get('colors', None)
        self.edge_width = kwargs.get('edge_width', None)

        # Native to WordcloudOptions
        self.allow_extend_playing_field = kwargs.get('allow_extend_playing_field', None)
        self.max_font_size = kwargs.get('max_font_size', None)
        self.min_font_size = kwargs.get('min_font_size', None)
        self.placement_strategy = kwargs.get('placement_strategy', None)
        self.rotation = kwargs.get('rotation', None)
        self.spiral = kwargs.get('spiral', None)

        super().__init__(**kwargs)

    @property
    def allow_extend_playing_field(self) -> Optional[bool]:
        """If there is no space for a word on the playing field, then setting this option
        to ``True`` will allow the playing field to be extended to fit the word. If
        ``False``, then the word will be dropped from the visualization. Defaults to
        ``True``.

        .. error::

          This option is currently not decided to be published in the API, and is
          therefore marked as/considered private.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_extend_playing_field

    @allow_extend_playing_field.setter
    def allow_extend_playing_field(self, value):
        if value is None:
            self._allow_extend_playing_field = None
        else:
            self._allow_extend_playing_field = bool(value)

    @property
    def animation_limit(self) -> Optional[int | float | Decimal]:
        """For some series, there is a limit that shuts down initial animation by default
        when the total number of points in the chart is too high. Defaults to
        :obj:`None <python:None>`.

        For example, for a column chart and its derivatives, animation does not run if
        there is more than 250 points totally. To disable this cap, set
        ``animation_limit`` to ``float("inf")`` (which represents infinity).

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._animation_limit

    @animation_limit.setter
    def animation_limit(self, value):
        if value == float('inf'):
            self._animation_limit = float('inf')
        else:
            self._animation_limit = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each column or bar. Defaults to
        ``'#ffffff'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The corner radius of the border surrounding each column or bar. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding each column or bar. If
        :obj:`None <python:None>`, defaults to ``1`` when there is room for a border, but
        to ``0`` when the columns are so dense that a border would cover the next column.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def center_in_category(self) -> Optional[bool]:
        """If ``True``, the columns will center in the category, ignoring null or missing
        points. When ``False``, space will be reserved for null or missing points.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._center_in_category

    @center_in_category.setter
    def center_in_category(self, value):
        if value is None:
            self._center_in_category = None
        else:
            self._center_in_category = bool(value)

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
    def color_key(self) -> Optional[str]:
        """Determines what data value should be used to calculate point color if
        :meth:`AreaOptions.color_axis` is used.

        .. note::

          Requires to set ``min`` and ``max`` if some custom point property is used or if
          approximation for data grouping is set to ``'sum'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color_key

    @color_key.setter
    def color_key(self, value):
        self._color_key = validators.string(value, allow_empty = True)

    @property
    def colors(self) -> Optional[List[str | Gradient | Pattern]]:
        """A series-specific or series type-specific color set to apply instead of the
        global colors when :meth:`BarOptions.color_by_point` is ``True``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`,
          :class:`Gradient`, or :class:`Pattern` OR :obj:`None <python:None>`
        """
        return self._colors

    @colors.setter
    def colors(self, value):
        if not value:
            self._colors = None
        else:
            value = validators.iterable(value)

            self._colors = [utility_functions.validate_color(x) for x in value]

    @property
    def edge_width(self) -> Optional[int | float | Decimal]:
        """The width of the colored edges applied to a 3D column. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._edge_width

    @edge_width.setter
    def edge_width(self, value):
        self._edge_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def max_font_size(self) -> Optional[int | float | Decimal]:
        """The word with the largest weight will have a font size equal to this value.
        Defaults to ``25``.

        .. note::

          The font size of a word is the ratio between its weight and the largest occuring
          weight, multiplied with the value of ``max_font_size``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_font_size

    @max_font_size.setter
    def max_font_size(self, value):
        self._max_font_size = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def min_font_size(self) -> Optional[int | float | Decimal]:
        """A threshold determining the minimum font size that can be applied to a word.
        Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_font_size

    @min_font_size.setter
    def min_font_size(self, value):
        self._min_font_size = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def placement_strategy(self) -> Optional[str]:
        """This option decides which algorithm is used for the placement and rotation of
        a word in the wordcloud. Defaults to ``'center'``.

        .. note::

          It is possible for users to add their own custom placement strategies as
          described in the
          `JavaScript documentation <https://www.highcharts.com/docs/chart-and-series-types/word-cloud-series#custom-placement-strategies>`__

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._placement_strategy

    @placement_strategy.setter
    def placement_strategy(self, value):
        self._placement_strategy = validators.string(value, allow_empty = True)

    @property
    def rotation(self) -> Optional[RotationOptions]:
        """Configuration of the allowed rotations for words in the wordcloud.

        :rtype: :class:`RotationOptions` or :obj:`None <python:None>`
        """
        return self._rotation

    @rotation.setter
    @class_sensitive(RotationOptions)
    def rotation(self, value):
        self._rotation = value

    @property
    def spiral(self) -> Optional[str]:
        """Spiralling algorithm used for placing a word after the initial position
        experienced a collision with either another word or the borders. Defaults to
        ``'rectangular'``.

        .. note::

          It is possible for users to add their own custom spiralling algorithms for use
          in wordclouds. For more information, please see the
          `JavaScript documentation <https://www.highcharts.com/docs/chart-and-series-types/word-cloud-series#custom-spiralling-algorithm>`__

        :rtype: :class:`str <python:str>`
        """
        return self._spiral

    @spiral.setter
    def spiral(self, value):
        self._spiral = validators.string(value, allow_empty = True)

    @property
    def relative_x_value(self) -> Optional[bool]:
        """When ``True``, X values in the data set are relative to the current
        :meth:`point_start <AreaOptions.point_start>`,
        :meth:`point_interval <AreaOptions.point_interval>`, and
        :meth:`point_interval_unit <AreaOptions.point_interval_unit>` settings. This
        allows compression of the data for datasets with irregular X values. Defaults to
        ``False``.

        The real X values are computed on the formula ``f(x) = ax + b``, where ``a`` is
        the :meth:`point_interval <AreaOptions.point_interval>` (optionally with a time
        unit given by :meth:`point_interval_unit <AreaOptions.point_interval_unit>`), and
        ``b`` is the :meth:`point_start <AreaOptions.point_start>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._relative_x_value

    @relative_x_value.setter
    def relative_x_value(self, value):
        if value is None:
            self._relative_x_value = None
        else:
            self._relative_x_value = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
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

            # Copied from SeriesOptions
            'animation_limit': as_dict.get('animationLimit', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'relative_x_value': as_dict.get('relativeXValue', None),

            # Copied from BaseBarOptions
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'edge_width': as_dict.get('edgeWidth', None),

            # Native to WordcloudOptions
            'allow_extend_playing_field': as_dict.get('allowExtendPlayingField', None),
            'max_font_size': as_dict.get('maxFontSize', None),
            'min_font_size': as_dict.get('minFontSize', None),
            'placement_strategy': as_dict.get('placementStrategy', None),
            'rotation': as_dict.get('rotation', None),
            'spiral': as_dict.get('spiral', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allowExtendPlayingField': self.allow_extend_playing_field,
            'animationLimit': self.animation_limit,
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'centerInCategory': self.center_in_category,
            'colorByPoint': self.color_by_point,
            'colorIndex': self.color_index,
            'colorKey': self.color_key,
            'colors': self.colors,
            'edgeWidth': self.edge_width,
            'maxFontSize': self.max_font_size,
            'minFontSize': self.min_font_size,
            'placementStrategy': self.placement_strategy,
            'relativeXValue': self.relative_x_value,
            'rotation': self.rotation,
            'spiral': self.spiral
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
