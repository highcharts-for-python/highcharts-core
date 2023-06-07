from typing import Optional, List

from highcharts_core.options.series.bar import BarSeries
from highcharts_core.options.series.data.boxplot import BoxPlotData
from highcharts_core.options.series.data.range import RangeData
from highcharts_core.options.plot_options.boxplot import BoxPlotOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict


class BoxPlotSeries(BarSeries, BoxPlotOptions):
    """Options to configure a Box Plot series.

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
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[BoxPlotData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`BoxPlotData` instances,
        it accepts as input different types of data:

        .. tabs::

          .. tab:: 5D Collection

            .. code-block::

              series = BoxPlotSeries()

              series.data = [
                  [3, 0, 10, 3, 5],
                  [7, 8, 7, 2, 9],
                  [6, 9, 5, 1, 3]
              ]

            A collection of five-dimensional numerical values. Each member of the
            collection will be interpreted as :meth:`low <BoxPlotData.low>`,
            :meth:`q1 <BoxPlotData.q1>`, :meth:`median <BoxPlotData.median>`,
            :meth:`q3 <BoxPlotData.q3>`, and :meth:`high <BoxPlotData.high>`,
            respectively.

            The :meth:`x <BoxPlotData.x>` value will be automatically inferred. If
            :meth:`BoxPlotSeries.point_start` is :obj:`None <python:None>`, ``x`` values
            will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`BoxPlotSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              series = BoxPlotSeries()

              # Categorical X-axis
              series.data = [
                  ['Category A', 3, 0, 10, 3, 5],
                  ['Category B', 7, 8, 7, 2, 9],
                  ['Category C', 6, 9, 5, 1, 3]
              ]

              # Numerical X-axis
              series.data = [
                  [0, 3, 0, 10, 3, 5],
                  [1, 7, 8, 7, 2, 9],
                  [2, 6, 9, 5, 1, 3]
              ]

            A collection of six-dimensional numerical values. Each member of the
            collection will be interpreted as :meth:`x <BoxPlotData.x>`,
            :meth:`low <BoxPlotData.low>`, :meth:`q1 <BoxPlotData.q1>`,
            :meth:`median <BoxPlotData.median>`, :meth:`q3 <BoxPlotData.q3>`, and
            :meth:`high <BoxPlotData.high>`, respectively.

            The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`BoxPlotData` objects.

        :rtype: :class:`list <python:list>` of :class:`BoxPlotData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = BoxPlotData.from_array(value)

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
            'whisker_width': as_dict.get('whiskerWidth', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        return untrimmed


class ErrorBarSeries(BoxPlotSeries):
    """Options to configure an Error Bar series.

    Error bars are a graphical representation of the variability of data and are used
    on graphs to indicate the error, or uncertainty in a reported measurement.

    .. figure:: ../../../_static/errorbar-example.png
      :alt: Error Bar Example Chart
      :align: center

    """

    @property
    def data(self) -> Optional[List[RangeData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`RangeData` instances,
        it accepts as input two different types of data:

        .. tabs::

          .. tab:: 3D Collection

            .. code-block::

              series = ErrorBarSeries()

              # Category X-axis
              series.data = [
                  ['Category A', 8, 3],
                  ['Category B', 1, 1],
                  ['Category C', 6, 8]
              ]

              # Numerical X-axis
              series.data = [
                  [0, 8, 3],
                  [1, 1, 1],
                  [2, 6, 8]
              ]

            A three-dimensional collection of numerical values. Each member of the
            collection will be interpreted as an ``x`` value, a ``low`` value, and a
            ``high`` value.

            The ``x`` value can be a :class:`str <python:str>`,
            :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: 2D Collection

            .. code-block::

              series = ErrorBarSeries()
              series.data = [
                  [8, 3],
                  [1, 1],
                  [6, 8]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``low`` and ``high`` value. The ``x`` values are
            automatically inferred:

              If :meth:`ErrorBarSeries.point_start` is :obj:`None <python:None>`, ``x``
              values will begin at ``0``. Otherwise, they will start at ``point_start``.

              If :meth:`ErrorBarSeries.point_interval` is :obj:`None <python:None>`, ``x``
              values will be incremented by ``1``. Otherwise, they will be incremented
              by the value of ``point_interval``.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`RangeData` objects.

        :rtype: :class:`list <python:list>` of :class:`RangeData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = RangeData.from_array(value)
