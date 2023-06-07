from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.utility_classes.clusters import ClusterOptions


class VectorOptions(SeriesOptions):
    """General options to apply to all Vector series types.

    A vector plot is a type of cartesian chart where each point has an X and Y
    position, a length and a direction. Vectors are drawn as arrows.

    .. figure:: ../../../_static/vector-example.png
      :alt: Vector Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._cluster = None
        self._rotation_origin = None
        self._vector_length = None

        self.cluster = kwargs.get('cluster', None)
        self.rotation_origin = kwargs.get('rotation_origin', None)
        self.vector_length = kwargs.get('vector_length', None)

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

            'cluster': as_dict.get('cluster', None),
            'rotation_origin': as_dict.get('rotationOrigin', None),
            'vector_length': as_dict.get('vectorLength', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'cluster': self.cluster,
            'rotationOrigin': self.rotation_origin,
            'vectorLength': self.vector_length
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
