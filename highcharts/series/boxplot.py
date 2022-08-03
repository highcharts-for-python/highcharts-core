from typing import Optional, List

from highcharts import constants
from highcharts.series.bar import BarSeries
from highcharts.series.data.boxplot import BoxPlotData
from highcharts.series.data.range import RangeData
from highcharts.plot_options.boxplot import BoxPlotOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class BoxPlotSeries(BarSeries, BoxPlotOptions):
    """Options to configure a Box Plot series.

    A box plot is a convenient way of depicting groups of data through their
    five-number summaries:

      * the smallest observation (sample minimum),
      * lower quartile (Q1),
      * median (Q2),
      * upper quartile (Q3), and
      * largest observation (sample maximum).

    .. figure:: _static/boxplot-example.png
      :alt: Box Plot Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

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
            self._data = BoxPlotData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', 0.75),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', False),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', '#ffffff'),
            'border_radius': as_dict.pop('borderRadius', 0),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', False),
            'color_by_point': as_dict.pop('colorByPoint', False),
            'depth': as_dict.pop('depth', 25),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', 1),
            'grouping': as_dict.pop('grouping', True),
            'group_padding': as_dict.pop('groupPadding', 0.2),
            'group_z_padding': as_dict.pop('groupZPadding', 1),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', 0),
            'point_padding': as_dict.pop('pointPadding', 0.1),
            'point_range': as_dict.pop('pointRange', constants.EnforcedNull),
            'point_width': as_dict.pop('pointWidth', None),

            'box_dash_style': as_dict.pop('boxDashStyle', 'Solid'),
            'median_color': as_dict.pop('medianColor', None),
            'median_dash_style': as_dict.pop('medianDashStyle', 'Solid'),
            'median_width': as_dict.pop('medianWidth', 2),
            'stem_dash_style': as_dict.pop('stemDashStyle', 'Solid'),
            'stem_width': as_dict.pop('stemWidth', None),
            'whisker_color': as_dict.pop('whiskerColor', None),
            'whisker_dash_style': as_dict.pop('whiskerDashStyle', 'Solid'),
            'whisker_length': as_dict.pop('whiskerLength', '50%'),
            'whisker_width': as_dict.pop('whiskerWidth', 2),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)


class ErrorBarSeries(BoxPlotSeries):
    """Options to configure an Error Bar series.

    Error bars are a graphical representation of the variability of data and are used
    on graphs to indicate the error, or uncertainty in a reported measurement.

    .. figure:: _static/errorbar-example.png
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
            self._data = RangeData.from_setter(value)
