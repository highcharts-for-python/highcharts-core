from typing import Optional, List

from highcharts.series.base import SeriesBase
from highcharts.series.data.cartesian import CartesianData
from highcharts.series.data.range import RangeData
from highcharts.plot_options.area import AreaOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class AreaSeries(SeriesBase, AreaOptions):
    """Options for a specific Area series.

    .. figure:: _static/area-example.png
      :alt: Area Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[CartesianData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`CartesianData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              area_series = AreaSeries()
              area_series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`AreaSeries.point_start` is :obj:`None <python:None>`, ``x`` values
            will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`AreaSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              area_series = AreaSeries()
              # Category X-axis
              area_series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              area_series.data = [
                  [9, 0],
                  [1, 5],
                  [2, 3],
                  [7, 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``x`` and ``y`` pair. The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`CartesianData` objects.

        :rtype: :class:`list <python:list>` of :class:`CartesianData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = CartesianData.from_setter(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
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
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

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

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro_to_dict(self)

        return untrimmed


class AreaRangeSeries(AreaSeries):
    """Options to apply to an AreaRange series. The area range series
    is a carteseian series with higher and lower values for each point along an X
    axis, where the area between the values is shaded.

    .. figure:: _static/arearange-example.png
      :alt: AreaRange Example Chart
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

              area_range_series = AreaRangeSeries()

              # Category X-axis
              area_range_series.data = [
                  ['Category A', 8, 3],
                  ['Category B', 1, 1],
                  ['Category C', 6, 8]
              ]

              # Numerical X-axis
              area_range_series.data = [
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

              area_range_series = AreaRangeSeries()
              area_series.data = [
                  [8, 3],
                  [1, 1],
                  [6, 8]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``low`` and ``high`` value. The ``x`` values are
            automatically inferred:

              If :meth:`AreaSeries.point_start` is :obj:`None <python:None>`, ``x`` values
              will begin at ``0``. Otherwise, they will start at ``point_start``.

              If :meth:`AreaSeries.point_interval` is :obj:`None <python:None>`, ``x``
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


class AreaSplineSeries(AreaSeries):
    """Options to apply to an AreaSpline series. The area spline series
    is an area series where the graph between the points is smoothed into a spline.

    .. figure:: _static/areaspline-example.png
      :alt: AreaSpline Example Chart
      :align: center

    """
    pass


class AreaSplineRangeSeries(AreaRangeSeries):
    """Options to apply to an AreaSplineRange series. The area spline
    range series is a carteseian series type with higher and lower Y values along an X
    axis. The area inside the range is colored, and the graph outlining the area is a
    smoothed spline."""
    pass


class LineSeries(AreaSeries):
    """Options to apply to a Line series.

    A line series displays information as a series of data points connected by
    straight line segments.

    .. figure:: _static/line-example.png
      :alt: Line Example Chart
      :align: center

    """
    pass


class StreamGraphSeries(AreaSeries):
    """Options to apply to a Stream Graph series.

    A streamgraph is a type of stacked area graph which is displaced around a central
    axis, resulting in a flowing, organic shape.

    .. figure:: _static/streamgraph-example.png
      :alt: StreamGraph Example Chart
      :align: center

    """
    pass
