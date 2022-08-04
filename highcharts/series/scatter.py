from typing import Optional, List

from highcharts.series.base import SeriesBase
from highcharts.series.data.cartesian import CartesianData, Cartesian3DData
from highcharts.plot_options.scatter import ScatterOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class ScatterSeries(SeriesBase, ScatterOptions):
    """Options to configure a Scatter series.

    A scatter plot uses cartesian coordinates to display values for two variables for
    a set of data.

    .. figure:: _static/scatter-example.png
      :alt: Scatter Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[List[CartesianData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`CartesianData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = ScatterSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`ScatterSeries.point_start` is :obj:`None <python:None>`, ``x``
            values will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`ScatterSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              series = ScatterSeries()
              # Category X-axis
              series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              series.data = [
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
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
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

            'jitter': as_dict.pop('jitter', None),
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)


class Scatter3DSeries(ScatterSeries):
    """Options to configure a Scatter 3D series.

    A 3D scatter plot uses x, y and z coordinates to display values for three
    variables for a set of data.

    .. figure:: _static/scatter_3d-example.png
      :alt: Scatter 3D Example Chart
      :align: center

    """

    @property
    def data(self) -> Optional[List[Cartesian3DData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`Cartesian3DData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = Scatter3DSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`Scatter3DSeries.point_start` is :obj:`None <python:None>`, ``x``
            values will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`Scatter3DSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              series = Scatter3DSeries()
              # Category X-axis
              series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              series.data = [
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

            A one-dimensional collection of :class:`Cartesian3DData` objects.

        :rtype: :class:`list <python:list>` of :class:`Cartesian3DData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = Cartesian3DData.from_setter(value)
