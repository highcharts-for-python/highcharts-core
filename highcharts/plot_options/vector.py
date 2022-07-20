from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.plot_options.series import SeriesOptions
from highcharts.utility_classes.clusters import ClusterOptions


class VectorOptions(SeriesOptions):
    """General options to apply to all Vector series types.

    A vector plot is a type of cartesian chart where each point has an X and Y
    position, a length and a direction. Vectors are drawn as arrows.

    .. figure:: _static/vector-example.png
      :alt: Vector Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._cluster = None
        self._rotation_origin = None
        self._vector_length = None

        self.cluster = kwargs.pop('cluster', None)
        self.rotation_origin = kwargs.pop('rotation_origin', None)
        self.vector_length = kwargs.pop('vector_length', None)

        super().__init__(**kwargs)

    @property
    def cluster(self) -> Optional[ClusterOptions]:
        """Options for marker clusters, the concept of sampling the data values into
        larger blocks in order to ease readability and increase performance of the
        JavaScript charts.

        .. warning::

          The marker clusters module does not work with ``boost`` and ``draggable-points``
          modules.

        .. note::

          The marker clusters feature requires the ``marker-clusters.js`` file to be
          loaded, found in the modules directory of the download package, or online at
          `code.highcharts.com/modules/marker-clusters.js <code.highcharts.com/modules/marker-clusters.js>`_.

        :rtype: :class:`ClusterOptions` or :obj:`None <python:None>`
        """
        return self._cluster

    @cluster.setter
    @class_sensitive(ClusterOptions)
    def cluster(self, value):
        self._cluster = value

    @property
    def rotation_origin(self) -> Optional[str]:
        """What part of the vector it should be rotated around. Defaults to ``'center'``.

        Supports the following values:

          * ``'start'``
          * ``'center'``
          * ``'end'``

        If ``'start'``, the vectors will start from the given [x, y] position, and when
        ``'end'`` the vectors will end in the [x, y] position.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._rotation_origin

    @rotation_origin.setter
    def rotation_origin(self, value):
        if not value:
            self._rotation_origin = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['start', 'center', 'end']:
                raise errors.HighchartsValueError(f'rotation_origin expects either '
                                                  f'"start", "center", or "end". '
                                                  f'Received: {value}')

            self._rotation_origin = value

    @property
    def vector_length(self) -> Optional[int | float | Decimal]:
        """Maximum length of the arrows in the vector plot. Defaults to ``20``.

        .. note::

          The individual arrow length is computed between 0 and this value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._vector_length

    @vector_length.setter
    def vector_length(self, value):
        self._vector_length = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

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

            'cluster': as_dict.pop('cluster', None),
            'rotation_origin': as_dict.pop('rotationOrigin', None),
            'vector_length': as_dict.pop('vectorLength', None)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'cluster': self.cluster,
            'rotationOrigin': self.rotation_origin,
            'vectorLength': self.vector_length
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
