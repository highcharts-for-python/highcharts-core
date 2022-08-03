from typing import Optional, List

from highcharts import constants
from highcharts.series.bar import BarSeries
from highcharts.series.data.bullet import BulletData
from highcharts.plot_options.bullet import BulletOptions
from highchrats.utility_functions import mro_init, mro_to_dict


class BulletSeries(BarSeries, BulletOptions):
    """Options to configure a Bullet series.

    A bullet graph is a variation of a bar graph. The bullet graph features a single
    measure, compares it to a target, and displays it in the context of qualitative
    ranges of performance that could be set using :meth:`YAxis.plot_bands`.

    .. figure:: _static/bullet-example.png
      :alt: Bullet Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[List[BulletData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`BarData` instances,
        it accepts as input different types of data:

        .. tabs::

          .. tab:: 3D Collection

            .. code-block::

              series = BulletSeries()

              # Numerical X-axis
              series.data = [
                  [0, 40, 75],
                  [1, 50, 50],
                  [2, 60, 40]
              ]

              # Categorical X-axis
              series.data = [
                  ['Category A', 40, 75],
                  ['Category B', 50, 50],
                  ['Category C', 60, 40]
              ]

            A three-dimensional collection of values. Each member corresponds to the
            :meth:`x <BulletData.x>`, :meth:`y <BulletData.y>`, and
            :meth:`target <BulletData.target>` values, respectively. The ``x`` value can
            be a :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: 2D Collection

            .. code-block::

              series = BulletSeries()
              series.data = [
                  [40, 75],
                  [50, 50],
                  [60, 40]
              ]

            A two-dimensional collection of numerical values. Each member of the
            collection will be interpreted as the :meth:`y <BulletData.y>` and
            :meth:`target <BulletData.target>` values, respectively. The
            :meth:`x <BulletData.x>` value will be inferred according to the following
            rules:

              If :meth:`BulletSeries.point_start` is :obj:`None <python:None>`, ``x``
              values will begin at ``0``. Otherwise, they will start at ``point_start``.

              If :meth:`BulletSeries.point_interval` is :obj:`None <python:None>`, ``x``
              values will be incremented by ``1``. Otherwise, they will be incremented
              by the value of ``point_interval``.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`BulletData` objects.

        :rtype: :class:`list <python:list>` of :class:`BulletData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = BulletData.from_setter(value)

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

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),

            'target_options': as_dict.pop('targetOptions', None),

        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = mro_to_dict(self)

        return self.trim_dict(untrimmed)
