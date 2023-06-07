from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.plot_options.bar import BarOptions
from highcharts_core.options.plot_options.drag_drop import BoxPlotDragDropOptions
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern


class BoxPlotOptions(BarOptions):
    """General options to apply to all Box Plot series types.

    A box plot is a convenient way of depicting groups of data through their
    five-number summaries:

      * the smallest observation (sample minimum),
      * lower quartile (Q1),
      * median (Q2),
      * upper quartile (Q3), and
      * largest observation (sample maximum).

    .. figure:: ../../../_static/boxplot-example.png
      :alt: Box Plot Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._box_dash_style = None
        self._median_color = None
        self._median_dash_style = None
        self._median_width = None
        self._stem_dash_style = None
        self._stem_width = None
        self._whisker_color = None
        self._whisker_dash_style = None
        self._whisker_length = None
        self._whisker_width = None

        self.box_dash_style = kwargs.get('box_dash_style', None)
        self.median_color = kwargs.get('median_color', None)
        self.median_dash_style = kwargs.get('median_dash_style', None)
        self.median_width = kwargs.get('median_width', None)
        self.stem_dash_style = kwargs.get('stem_dash_style', None)
        self.stem_width = kwargs.get('stem_width', None)
        self.whisker_color = kwargs.get('whisker_color', None)
        self.whisker_dash_style = kwargs.get('whisker_dash_style', None)
        self.whisker_length = kwargs.get('whisker_length', None)
        self.whisker_width = kwargs.get('whisker_width', None)

        super().__init__(**kwargs)

    @property
    def box_dash_style(self) -> Optional[str]:
        """The dash style of the box.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._box_dash_style

    @box_dash_style.setter
    def box_dash_style(self, value):
        if not value:
            self._box_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'box_dash_style expects a recognized '
                                                  f'value, but received: {value}')
            self._box_dash_style = value

    @property
    def drag_drop(self) -> Optional[BoxPlotDragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(BoxPlotDragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def median_color(self) -> Optional[str | Gradient]:
        """The color of the median line. If :obj:`None <python:None>`, the general series
        color applies. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, or :obj:`None <python:None>`
        """
        return self._median_color

    @median_color.setter
    def median_color(self, value):
        from highcharts_core import utility_functions
        self._median_color = utility_functions.validate_color(value)

    @property
    def median_dash_style(self) -> Optional[str]:
        """The dash style of the median. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._median_dash_style

    @median_dash_style.setter
    def median_dash_style(self, value):
        if not value:
            self._median_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'median_dash_style expects a '
                                                  f' recognized value, but received: '
                                                  f'{value}')
            self._median_dash_style = value

    @property
    def median_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of the median line. If :obj:`None <python:None>`, the
        :meth:`line_width <BoxPlotOptions.line_width>` is used. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._median_width

    @median_width.setter
    def median_width(self, value):
        self._median_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def stem_dash_style(self) -> Optional[str]:
        """The dash style of the :term:`stem`, the vertical line extending from the box to
        the whiskers. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stem_dash_style

    @stem_dash_style.setter
    def stem_dash_style(self, value):
        if not value:
            self._stem_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'stem_dash_style expects a recognized'
                                                  f' value, but received: {value}')
            self._stem_dash_style = value

    @property
    def stem_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of the stem line. If :obj:`None <python:None>`, the
        :meth:`line_width <BoxPlotOptions.line_width>` is used. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._stem_width

    @stem_width.setter
    def stem_width(self, value):
        self._stem_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def whisker_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the :term:`whiskers <whisker>`, the horizontal lines marking low
        and high values. When :obj:`None <python:None>`, the general series color is used.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern`, or
          :obj:`None <python:None>`
        """
        return self._whisker_color

    @whisker_color.setter
    def whisker_color(self, value):
        from highcharts_core import utility_functions
        self._whisker_color = utility_functions.validate_color(value)

    @property
    def whisker_dash_style(self) -> Optional[str]:
        """The dash style of the whiskers. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._whisker_dash_style

    @whisker_dash_style.setter
    def whisker_dash_style(self, value):
        if not value:
            self._whisker_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'whisker_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._whisker_dash_style = value

    @property
    def whisker_length(self) -> Optional[str | int | float | Decimal]:
        """The length of the whiskers, the horizontal lines marking low and high values.
        It can be a numerical pixel value, or a percentage value of the box width. Set to
        ``0`` to disable whiskers entirely.

        Defaults to ``'50%'``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._whisker_length

    @whisker_length.setter
    def whisker_length(self, value):
        if value is None:
            self._whisker_length = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('whisker_length expects either a '
                                                      'number of pixels or a percentage '
                                                      'string. No "%" character was '
                                                      'found.')
            except TypeError:
                value = validators.numeric(value,
                                           allow_empty = True,
                                           minimum = 0)
            self._whisker_length = value

    @property
    def whisker_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of the whisker line. If :obj:`None <python:None>`, the
        :meth:`line_width <BoxPlotOptions.line_width>` is used. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._whisker_width

    @whisker_width.setter
    def whisker_width(self, value):
        self._whisker_width = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

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

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'track_by_area': as_dict.get('trackByArea', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'grouping': as_dict.get('grouping', None),
            'group_padding': as_dict.get('groupPadding', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'point_padding': as_dict.get('pointPadding', None),
            'point_range': as_dict.get('pointRange', None),
            'point_width': as_dict.get('pointWidth', None),

            'depth': as_dict.get('depth', None),
            'edge_color': as_dict.get('edgeColor', None),
            'edge_width': as_dict.get('edgeWidth', None),
            'group_z_padding': as_dict.get('groupZPadding', None),

            'box_dash_style': as_dict.get('boxDashStyle', None),
            'median_color': as_dict.get('medianColor', None),
            'median_dash_style': as_dict.get('medianDashStyle', None),
            'median_width': as_dict.get('medianWidth', None),
            'stem_dash_style': as_dict.get('stemDashStyle', None),
            'stem_width': as_dict.get('stemWidth', None),
            'whisker_color': as_dict.get('whiskerColor', None),
            'whisker_dash_style': as_dict.get('whiskerDashStyle', None),
            'whisker_length': as_dict.get('whiskerLength', None),
            'whisker_width': as_dict.get('whiskerWidth', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'boxDashStyle': self.box_dash_style,
            'medianColor': self.median_color,
            'medianDashStyle': self.median_dash_style,
            'medianWidth': self.median_width,
            'stemDashStyle': self.stem_dash_style,
            'stemWidth': self.stem_width,
            'whiskerColor': self.whisker_color,
            'whiskerDashStyle': self.whisker_dash_style,
            'whiskerLength': self.whisker_length,
            'whiskerWidth': self.whisker_width
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class ErrorBarOptions(BoxPlotOptions):
    """General options to apply to all Error Bar series types.

    Error bars are a graphical representation of the variability of data and are used
    on graphs to indicate the error, or uncertainty in a reported measurement.

    .. figure:: ../../../_static/errorbar-example.png
      :alt: Error Bar Example Chart
      :align: center

    """
    pass
