from typing import Optional, List

from highcharts_core.decorators import class_sensitive
from highcharts_core.options.series.base import SeriesBase
from highcharts_core.options.series.data.range import ConnectedRangeData, ConnectedRangeDataCollection
from highcharts_core.options.plot_options.dumbbell import LollipopOptions, DumbbellOptions
from highcharts_core.options.plot_options.drag_drop import HighLowDragDropOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict, is_ndarray


class DumbbellSeries(SeriesBase, DumbbellOptions):
    """Options to configure a Dumbbell series.

    The dumbbell series is a cartesian series with higher and lower values for each
    point along an X axis, connected with a line between the values.

    .. figure:: ../../../_static/dumbbell-example.png
      :alt: Dumbbell Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return ConnectedRangeDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return ConnectedRangeData

    @property
    def data(self) -> Optional[List[ConnectedRangeData] | ConnectedRangeDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`ConnectedRangeData`
        instances, it accepts as input two different types of data:

        .. tabs::

          .. tab:: 3D Collection

            .. code-block::

              series = DumbbellSeries()

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

              series = DumbbellSeries()
              series.data = [
                  [8, 3],
                  [1, 1],
                  [6, 8]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``low`` and ``high`` value. The ``x`` values are
            automatically inferred:

              If :meth:`DumbbellSeries.point_start` is :obj:`None <python:None>`, ``x``
              values will begin at ``0``. Otherwise, they will start at ``point_start``.

              If :meth:`DumbbellSeries.point_interval` is :obj:`None <python:None>`, ``x``
              values will be incremented by ``1``. Otherwise, they will be incremented
              by the value of ``point_interval``.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`ConnectedRangeData` objects.

        :rtype: :class:`list <python:list>` of :class:`ConnectedRangeData` or
          :class:`ConnectedRangeDataCollection` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = ConnectedRangeData.from_array(value)

    @property
    def drag_drop(self) -> Optional[HighLowDragDropOptions]:
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
    @class_sensitive(HighLowDragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value


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
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'connector_color': as_dict.get('connectorColor', None),
            'connector_width': as_dict.get('connectorWidth', None),
            'group_padding': as_dict.get('groupPadding', None),
            'line_color': as_dict.get('lineColor', None),
            'low_color': as_dict.get('lowColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_padding': as_dict.get('pointPadding', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        return untrimmed


class LollipopSeries(DumbbellSeries, LollipopOptions):
    """Options to configure a Lollipop series.

    The lollipop series is a carteseian series with a line anchored from the x axis
    and a dot at the end to mark the value.

    .. warning::

      Requires ``highcharts-more.js``, ``modules/dumbbell.js``, and
      ``modules/lollipop.js`` to be loaded client-side.

    .. figure:: ../../../_static/lollipop-example.png
      :alt: Lollipop Example Chart
      :align: center

    """
    pass
