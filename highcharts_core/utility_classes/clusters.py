from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.animation import AnimationOptions
from highcharts_core.utility_classes.data_labels import DataLabel
from highcharts_core.utility_classes.events import ClusterEvents
from highcharts_core.utility_classes.markers import Marker
from highcharts_core.utility_classes.states import States
from highcharts_core.utility_classes.zones import ClusterZone


class VectorLayoutAlgorithm(HighchartsMeta):
    """Options for the layout algorithm to apply to the Vector chart."""

    def __init__(self, **kwargs):
        self._distance = None
        self._grid_size = None
        self._iterations = None
        self._kmeans_threshold = None
        self._type = None

        self.distance = kwargs.get('distance', None)
        self.grid_size = kwargs.get('grid_size', None)
        self.iterations = kwargs.get('iterations', None)
        self.kmeans_threshold = kwargs.get('kmeans_threshold', None)
        self.type = kwargs.get('type', None)

    @property
    def distance(self) -> Optional[str | int | float | Decimal]:
        """When :meth:`VectorLayoutAlgorithm.type` is set to ``'kmeans'``, ``distance``
        is a maximum distance between point and cluster center so that this point will be
        inside the cluster. Defaults to ``40``.

        The distance is either a number expressed in pixels or a percentage defining a
        percentage of the plot area width.

        :rtype: :class:`str <python:str>`, numeric, or :obj:`None <python:None>`
        """
        return self._distance

    @distance.setter
    def distance(self, value):
        if value is None:
            self._distance = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._distance = value

    @property
    def grid_size(self) -> Optional[str | int | float | Decimal]:
        """When :meth:`VectorLayoutAlgorithm.type` is set to ``'grid'``, ``grid_size``
        is  is a size of a grid square element. Defaults to ``50``.

        The ``grid_size`` is either a number expressed in pixels or a percentage defining
        a percentage of the plot area width.

        :rtype: :class:`str <python:str>`, numeric, or :obj:`None <python:None>`
        """
        return self._grid_size

    @grid_size.setter
    def grid_size(self, value):
        if value is None:
            self._grid_size = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except (TypeError, ValueError):
                value = validators.numeric(value, minimum = 0)

            self._grid_size = value

    @property
    def iterations(self) -> Optional[int]:
        """When :meth:`VectorLayoutAlgorithm.type` is set to ``'kmeans'``, the
        ``iterations`` indicates the number of times that the algorithm will be repeated
        to find cluster positions. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._iterations

    @iterations.setter
    def iterations(self, value):
        self._iterations = validators.integer(value,
                                              allow_empty = True,
                                              minimum = 1)

    @property
    def kmeans_threshold(self) -> Optional[int]:
        """When :meth:`VectorLayoutAlgorithm.type` is set to :obj:`None <python:None>` and
        the number of visible points is less than or equal to ``kmeans_threshold``, the
        ``'kmeans'`` algorithm is used by default to find clusters. When the number of
        visible points exceeds the ``kmeans_threshold``, the ``'grid'`` algorithm is used.
        Defaults to ``100``.

        .. hint::

          This threshold is a powerful tool to ensure good performance on large datasets
          and better cluster arrangemnet after zoom.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._kmeans_threshold

    @kmeans_threshold.setter
    def kmeans_threshold(self, value):
        self._kmeans_threshold = validators.integer(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def type(self) -> Optional[str]:
        """Type of algorithm to use to combine points into a cluster. Defaults to
        :obj:`None <python:None>`.

        There are three available algorithms:

          * ``'grid'`` - grid-based clustering technique. Points are assigned to squares
            of set size depending on their position on the plot area. Points inside the
            grid square are combined into a cluster. The grid size can be controlled by
            :meth:`VectorLayoutAlgorithm.grid_size` (grid size changes at certain zoom
            levels).
          * ``'kmeans'`` - based on K-Means clustering technique. In the first step,
            points are divided using the grid method (applying
            :meth:`VectorLayoutAlgorithm.distance` as the grid size) to find the initial
            amount of clusters. Next, each point is classified by computing the distance
            between each cluster center and that point. When the closest cluster distance
            is lower than :meth:`VectorLayoutAlgorithm.distance`, the point is added to
            this cluster otherwise is classified as noise. The algorithm is repeated until
            each cluster center does not change its previous position more than one pixel.
            This technique is more accurate but also more time consuming than the
            ``'grid'`` algorithm, especially for big datasets.
          * ``'optimizedKmeans'`` - based on K-Means clustering technique. This algorithm
            uses k-means algorithm only on the chart initialization or when chart extremes
            have greater range than on initialization. When a chart is redrawn the
            algorithm checks only clustered points distance from the cluster center and
            rebuilds it when the point is spaced enough to be outside the cluster. It
            provides a performance improvement and more stable clusters position so that
            it can be used rather on small and sparse datasets.

        When :obj:`None <python:None>`, the algorithm applied depends on
        :meth:`VectorLayoutAlgorithm.kmeans_threshold` such that if there are more visible
        points than the :meth:`kmeans_threshold <VectorLayoutAlgorithm.kmeans_threshold>`
        the ``'grid'`` algorithm is applied. If fewer, then ``'kmeans'`` is applied.

        A custom clustering algorithm can be applied by setting ``type`` to a
        JavaScript callback function. This function takes an array of ``processedXData``,
        ``processedYData``, ``processedXData`` indexes, and :class:`VectorLayoutAlgorithm`
        options as arguments and should return an object with grouped data.

        A custom algorithm should return an object similar to:

        .. code-block:: javascript

          {
           clusterId1: [{
               x: 573,
               y: 285,
               index: 1 // point index in the data array
           }, {
               x: 521,
               y: 197,
               index: 2
           }],
           clusterId2: [{
               ...
           }]
           ...
          }

        Where ``clusterId*`` (in the example above - a unique id of a cluster or noise) is
        an array of points belonging to a cluster. If the array has only one point or
        fewer points than set in :class:`Cluster.minimum_cluster_size`, it won't be
        combined into a cluster.

        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'distance': as_dict.get('distance', None),
            'grid_size': as_dict.get('gridSize', None),
            'iterations': as_dict.get('iterations', None),
            'kmeans_threshold': as_dict.get('kmeansThreshold', None),
            'type': as_dict.get('type', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'distance': self.distance,
            'gridSize': self.grid_size,
            'iterations': self.iterations,
            'kmeansThreshold': self.kmeans_threshold,
            'type': self.type
        }

        return untrimmed


class ClusterOptions(HighchartsMeta):
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

    """

    def __init__(self, **kwargs):
        self._allow_overlap = None
        self._animation = None
        self._data_labels = None
        self._drill_to_cluster = None
        self._enabled = None
        self._events = None
        self._layout_algorithm = None
        self._marker = None
        self._minimum_cluster_size = None
        self._states = None
        self._zones = None

        self.allow_overlap = kwargs.get('allow_overlap', None)
        self.animation = kwargs.get('animation', None)
        self.data_labels = kwargs.get('data_labels', None)
        self.drill_to_cluster = kwargs.get('drill_to_cluster', None)
        self.enabled = kwargs.get('enabled', None)
        self.events = kwargs.get('events', None)
        self.layout_algorithm = kwargs.get('layout_algorithm', None)
        self.marker = kwargs.get('marker', None)
        self.minimum_cluster_size = kwargs.get('minimum_cluster_size', None)
        self.states = kwargs.get('states', None)
        self.zones = kwargs.get('zones', None)

    @property
    def allow_overlap(self) -> Optional[bool]:
        """If ``True``, clusters are allowed to overlap. Otherwise, overlapping is
        prevented. Defaults to ``True``.

        .. warning::

          Preventing overlapping only works if
          :meth:`layout_algorithm.type <VectorLayoutAlgorithm.type>` is set to ``'grid'``.

        :returns: Flag indicating whether to allow clusters to overlap.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_overlap

    @allow_overlap.setter
    def allow_overlap(self, value):
        if value is None:
            self._allow_overlap = None
        else:
            self._allow_overlap = bool(value)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Options for the cluster marker animation.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def data_labels(self) -> Optional[DataLabel]:
        """Options for the cluster data labels.

        :rtype: :class:`DataLabel` or :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    @class_sensitive(DataLabel)
    def data_labels(self, value):
        self._data_labels = value

    @property
    def drill_to_cluster(self) -> Optional[bool]:
        """If ``True``, zoom the plot area to the cluster points range when a cluster is
        clicked. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._drill_to_cluster

    @drill_to_cluster.setter
    def drill_to_cluster(self, value):
        if value is None:
            self._drill_to_cluster = None
        else:
            self._drill_to_cluster = bool(value)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the marker-clusters module. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def events(self) -> Optional[ClusterEvents]:
        """General event handlers for marker clusters.

        :rtype: :class:`SeriesEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(ClusterEvents)
    def events(self, value):
        self._events = value

    @property
    def layout_algorithm(self) -> Optional[VectorLayoutAlgorithm]:
        """Options for the layout algorithm to apply to the Vector chart.

        :rtype: :class:`VectorLayoutAlgorithm` or :obj:`None <python:None>`
        """
        return self._layout_algorithm

    @layout_algorithm.setter
    @class_sensitive(VectorLayoutAlgorithm)
    def layout_algorithm(self, value):
        self._layout_algorithm = value

    @property
    def marker(self) -> Optional[Marker]:
        """Options for the point markers of line-like series.

        Properties like ``fill_color``, ``line_color`` and ``line_width`` define the
        visual appearance of the markers. Other series types, like column series, don't
        have markers, but have visual options on the series level instead.

        :rtype: :class:`Marker` or :obj:`None <python:None>`
        """
        return self._marker

    @marker.setter
    @class_sensitive(Marker)
    def marker(self, value):
        self._marker = value

    @property
    def minimum_cluster_size(self) -> Optional[int]:
        """The minimum number of points to be combined into a cluster. Defaults to ``2``.

        .. note::

          This value has to be greater or equal to ``2``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._minimum_cluster_size

    @minimum_cluster_size.setter
    def minimum_cluster_size(self, value):
        self._minimum_cluster_size = validators.integer(value,
                                                        allow_empty = True,
                                                        minimum = 2)

    @property
    def states(self) -> Optional[States]:
        """Configuration for state-specific configuration to apply to all clusters.

        :rtype: :class:`States` or :obj:`None <python:None>`
        """
        return self._states

    @states.setter
    @class_sensitive(States)
    def states(self, value):
        self._states = value

    @property
    def zones(self) -> Optional[List[ClusterZone]]:
        """An array defining zones within marker clusters.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of
          :class:`ClusterZone` instances
        """
        return self._zones

    @zones.setter
    @class_sensitive(ClusterZone, force_iterable = True)
    def zones(self, value):
        self._zones = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'allow_overlap': as_dict.get('allowOverlap', None),
            'animation': as_dict.get('animation', None),
            'data_labels': as_dict.get('dataLabels', None),
            'drill_to_cluster': as_dict.get('drillToCluster', None),
            'enabled': as_dict.get('enabled', None),
            'events': as_dict.get('events', None),
            'layout_algorithm': as_dict.get('layoutAlgorithm', None),
            'marker': as_dict.get('marker', None),
            'minimum_cluster_size': as_dict.get('minimumClusterSize', None),
            'states': as_dict.get('states', None),
            'zones': as_dict.get('zones', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allowOverlap': self.allow_overlap,
            'animation': self.animation,
            'dataLabels': self.data_labels,
            'drillToCluster': self.drill_to_cluster,
            'enabled': self.enabled,
            'events': self.events,
            'layoutAlgorithm': self.layout_algorithm,
            'marker': self.marker,
            'minimumClusterSize': self.minimum_cluster_size,
            'states': self.states,
            'zones': self.zones
        }

        return untrimmed
