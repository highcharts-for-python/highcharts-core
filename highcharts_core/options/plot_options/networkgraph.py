from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.plot_options.generic import GenericTypeOptions
from highcharts_core.options.plot_options.link import LinkOptions
from highcharts_core.utility_classes.zones import Zone
from highcharts_core.utility_classes.shadows import ShadowOptions
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.utility_classes.events import SimulationEvents


class LayoutAlgorithm(HighchartsMeta):
    """Configuration of how to lay out the Network Graph."""

    def __init__(self, **kwargs):
        self._approximation = None
        self._attractive_force = None
        self._enable_simulation = None
        self._friction = None
        self._gravitational_constant = None
        self._initial_position_radius = None
        self._initial_positions = None
        self._integration = None
        self._link_length = None
        self._max_iterations = None
        self._max_speed = None
        self._repulsive_force = None
        self._theta = None
        self._type = None

        self.approximation = kwargs.get('approximation', None)
        self.attractive_force = kwargs.get('attractive_force', None)
        self.enable_simulation = kwargs.get('enable_simulation', None)
        self.friction = kwargs.get('friction', None)
        self.gravitational_constant = kwargs.get('gravitational_constant', None)
        self.initial_position_radius = kwargs.get('initial_position_radius', None)
        self.initial_positions = kwargs.get('initial_positions', None)
        self.integration = kwargs.get('integration', None)
        self.link_length = kwargs.get('link_length', None)
        self.max_iterations = kwargs.get('max_iterations', None)
        self.max_speed = kwargs.get('max_speed', None)
        self.repulsive_force = kwargs.get('repulsive_force', None)
        self.theta = kwargs.get('theta', None)
        self.type = kwargs.get('type', None)

    @property
    def approximation(self) -> Optional[str]:
        """Approximation used to calculate repulsive forces affecting nodes.

        When :obj:`None <python:None>`, when calculateing net force, nodes are compared
        against each other, which gives ``O(N^2)`` complexity. Using ``barnes-hut``
        approximation, we decrease this to ``O(N log N)``, but the resulting graph will
        have a different layout.

        .. note::

          Barnes-Hut approximation divides space into rectangles via quad tree, where
          forces exerted on nodes are calculated directly for nearby cells, and for all
          others, cells are treated as a separate node with center of mass.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._approximation

    @approximation.setter
    def approximation(self, value):
        self._approximation = validators.string(value, allow_empty = True)

    @property
    def attractive_force(self) -> Optional[CallbackFunction]:
        """JavaScript function which calculates the attraction force applied on a node
        which is conected to another node by a link.

        The (JavaScript) function should be passed two arguments:

          * ``d`` - which is the current distance between two nodes
          * ``k`` - which is the desired distance between two nodes

        If :obj:`None <python:None>`, defaults to:

          .. code-block:: javascript

            function (d, k) {
                return k * k / d;
            }

        If :meth:`LayoutAlgorithm.integration` is ``'verlet'``, then if
        :obj:`None <python:None>` defaults to:

          .. code-block:: javascript

            function (d, k) {
                return (k - d) / d;
            }

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._attractive_force

    @attractive_force.setter
    @class_sensitive(CallbackFunction)
    def attractive_force(self, value):
        self._attractive_force = value

    @property
    def enable_simulation(self) -> Optional[bool]:
        """If ``True``, enables live simulation of the algorithm's implementation. All
        nodes are animated as the force applies to them. Defaults to ``False``.

        .. warning::

          EXPERIMENTAL!

        :rtype: :class:`bool <python:bool>`
        """
        return self._enable_simulation

    @enable_simulation.setter
    def enable_simulation(self, value):
        if value is None:
            self._enable_simulation = None
        else:
            self._enable_simulation = bool(value)

    @property
    def friction(self) -> Optional[int | float | Decimal]:
        """Friction applied on forces to prevent nodes rushing to fast to the desired
        positions. Defaults to ``-0.981``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._friction

    @friction.setter
    def friction(self, value):
        self._friction = validators.numeric(value, allow_empty = True)

    @property
    def gravitational_constant(self) -> Optional[int | float | Decimal]:
        """Gravitational const used in the barycenter force of the algorithm. Defaults to
        ``0.0625``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._gravitational_constant

    @gravitational_constant.setter
    def gravitational_constant(self, value):
        self._gravitational_constant = validators.numeric(value, allow_empty = True)

    @property
    def initial_position_radius(self) -> Optional[int | float | Decimal]:
        """When :meth:`LayoutAlgorithm.initial_positions` is set to ``'circle'``, this
        setting is the distance from the center of the circle at which nodes will be
        created. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._initial_position_radius

    @initial_position_radius.setter
    def initial_position_radius(self, value):
        self._initial_position_radius = validators.numeric(value, allow_empty = True)

    @property
    def initial_positions(self) -> Optional[str]:
        """Initial layout algorithm for positioning nodes. Defaults to ``'circle'``.

        Accepts the following options:

          * ``"circle"``
          * ``"random"``
          * a JavaScript function where positions should be set on each node
            (``this.nodes``) as ``node.plotX`` and ``node.plotY``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._initial_positions

    @initial_positions.setter
    def initial_positions(self, value):
        self._initial_positions = validators.string(value, allow_empty = True)

    @property
    def integration(self) -> Optional[str]:
        """Integration type. Defaults to ``'euler'``.

        Available options are:

          * ``'euler'``
          * ``'verlet'``

        Integration determines how forces are applied on particles. In Euler integration,
        force is applied directly as ``newPosition += velocity``;. In Verlet integration,
        new position is based on the previous posittion without velocity:
        ``newPosition += previousPosition - newPosition``.

        Note that different integrations give different results as forces are different.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._integration

    @integration.setter
    def integration(self, value):
        if not value:
            self._integration = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['euler', 'verlet']:
                raise errors.HighchartsValueError(f'integration expects either "euler" '
                                                  f'or "verlet". Was: {value}')
            self._integration = value

    @property
    def link_length(self) -> Optional[int | float | Decimal]:
        """Ideal length (px) of the link between two nodes. When
        :obj:`None <python:None>`, length is calculated (in JavaScript) as:
        ``Math.pow(availableWidth * availableHeight / nodesLength, 0.4);``

        .. note::

          Because of the algorithm specification, length of each link might be not exactly
          as specified.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._link_length

    @link_length.setter
    def link_length(self, value):
        self._link_length = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def max_iterations(self) -> Optional[int]:
        """Maximum number of iterations before algorithm will stop. In general, the
        algorithm should find positions sooner, but when rendering huge number of nodes,
        it is recommended to increase this value as finding perfect graph positions can
        require more time.

        Defaults to ``1000``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, value):
        self._max_iterations = validators.integer(value,
                                                  allow_empty = True,
                                                  minimum = 1)

    @property
    def max_speed(self) -> Optional[int | float | Decimal]:
        """Maximum speed that a node can attain in one iteration. Defaults to ``10``.

        In terms of simulation, it's a maximum translation (in pixels) that a node can
        move (in both x and y dimensions). While friction is applied on all nodes,
        ``max_speed`` is applied only for nodes that move very fast, for example, small or
        disconnected ones.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value):
        self._max_speed = validators.numeric(value,
                                             allow_empty = True,
                                             minimum = 0)

    @property
    def repulsive_force(self) -> Optional[CallbackFunction]:
        """JavaScript function which calculates the repulsive force applied on a node
        which is conected to another node by a link.

        The (JavaScript) function should be passed two arguments:

          * ``d`` - which is the current distance between two nodes
          * ``k`` - which is the desired distance between two nodes

        If :obj:`None <python:None>`, defaults to:

          .. code-block:: javascript

            function (d, k) {
                return k * k / d;
            }

        If :meth:`LayoutAlgorithm.integration` is ``'verlet'``, then if
        :obj:`None <python:None>` defaults to:

          .. code-block:: javascript

            function (d, k) {
                return (k - d) / d * (k > d ? 1 : 0)
            }

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._repulsive_force

    @repulsive_force.setter
    @class_sensitive(CallbackFunction)
    def repulsive_force(self, value):
        self._repulsive_force = value

    @property
    def theta(self) -> Optional[int | float | Decimal]:
        """Deteremines when distance between cell and node is small enough to caculate
        forces. Defaults to ``0.5``.

        The value of theta is compared directly with quotient ``s / d``, where ``s`` is
        the size of the cell, and ``d`` is the distance between the center of the cell's
        mass and the currently compared node.

        .. warning::

          Applies only to the ``barnes-hut`` :meth:`LayoutAlgorithm.approximation`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._theta

    @theta.setter
    def theta(self, value):
        self._theta = validators.numeric(value, allow_empty = True)

    @property
    def type(self) -> Optional[str]:
        """Type of algorithm used when positioning nodes. Defaults to
        ``'reingold-fruchterman'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'approximation': as_dict.get('approximation', None),
            'attractive_force': as_dict.get('attractiveForce', None),
            'enable_simulation': as_dict.get('enableSimulation', None),
            'friction': as_dict.get('friction', None),
            'gravitational_constant': as_dict.get('gravitationalConstant', None),
            'initial_position_radius': as_dict.get('initialPositionRadius', None),
            'initial_positions': as_dict.get('initialPositions', None),
            'integration': as_dict.get('integration', None),
            'link_length': as_dict.get('linkLength', None),
            'max_iterations': as_dict.get('maxIterations', None),
            'max_speed': as_dict.get('maxSpeed', None),
            'repulsive_force': as_dict.get('repulsiveForce', None),
            'theta': as_dict.get('theta', None),
            'type': as_dict.get('type', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'approximation': self.approximation,
            'attractiveForce': self.attractive_force,
            'enableSimulation': self.enable_simulation,
            'friction': self.friction,
            'gravitationalConstant': self.gravitational_constant,
            'initialPositionRadius': self.initial_position_radius,
            'initialPositions': self.initial_positions,
            'integration': self.integration,
            'linkLength': self.link_length,
            'maxIterations': self.max_iterations,
            'maxSpeed': self.max_speed,
            'repulsiveForce': self.repulsive_force,
            'theta': self.theta,
            'type': self.type
        }

        return untrimmed


class NetworkGraphOptions(GenericTypeOptions):
    """General options to apply to all Network Graph series types.

    A network graph is a type of relationship chart, where connnections (links)
    attract nodes (points) and other nodes repulse each other.

    .. figure:: ../../../_static/networkgraph-example.png
      :alt: NetworkGraph Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._color_index = None
        self._crisp = None
        self._draggable = None
        self._find_nearest_point_by = None
        self._layout_algorithm = None
        self._line_width = None
        self._link = None
        self._relative_x_value = None
        self._shadow = None
        self._zones = None

        self.color_index = kwargs.get('color_index', None)
        self.crisp = kwargs.get('crisp', None)
        self.draggable = kwargs.get('draggable', None)
        self.find_nearest_point_by = kwargs.get('find_nearest_point_by', None)
        self.layout_algorithm = kwargs.get('layout_algorithm', None)
        self.line_width = kwargs.get('line_width', None)
        self.link = kwargs.get('link', None)
        self.relative_x_value = kwargs.get('relative_x_value', None)
        self.shadow = kwargs.get('shadow', None)
        self.zones = kwargs.get('zones', None)

        super().__init__(**kwargs)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def crisp(self) -> Optional[bool]:
        """If ``True``, each point or column edge is rounded to its nearest pixel in order
        to render sharp on screen. Defaults to ``True``.

        .. hint::

          In some cases, when there are a lot of densely packed columns, this leads to
          visible difference in column widths or distance between columns. In these cases,
          setting ``crisp`` to ``False`` may look better, even though each column is
          rendered blurry.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crisp

    @crisp.setter
    def crisp(self, value):
        if value is None:
            self._crisp = None
        else:
            self._crisp = bool(value)

    @property
    def draggable(self) -> Optional[bool]:
        """If ``True``, indicates that the nodes are draggable. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable

    @draggable.setter
    def draggable(self, value):
        if value is None:
            self._draggable = None
        else:
            self._draggable = bool(value)

    @property
    def events(self) -> Optional[SimulationEvents]:
        """Event handlers for a network graph series.

        .. note::

          These event hooks can also be attached to the series at run time using the
          (JavaScript) ``Highcharts.addEvent()`` function.

        :rtype: :class:`SimulationEvents <highcharts_core.utility_classes.events.SimulationEvents>` or 
          :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(SimulationEvents)
    def events(self, value):
        self._events = value

    @property
    def find_nearest_point_by(self) -> Optional[str]:
        """Determines whether the series should look for the nearest point in both
        dimensions or just the x-dimension when hovering the series.

        If :obj:`None <python:None>`, defaults to ``'xy'`` for scatter series and ``'x'``
        for most other series. If the data has duplicate x-values, it is recommended to
        set this to ``'xy'`` to allow hovering over all points.

        Applies only to series types using nearest neighbor search (not direct hover) for
        tooltip.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._find_nearest_point_by

    @find_nearest_point_by.setter
    def find_nearest_point_by(self, value):
        self._find_nearest_point_by = validators.string(value, allow_empty = True)

    @property
    def layout_algorithm(self) -> Optional[LayoutAlgorithm]:
        """Configuration of how to lay out the Network Graph.

        :rtype: :class:`LayoutAlgorithm` or :obj:`None <python:None>`
        """
        return self._layout_algorithm

    @layout_algorithm.setter
    @class_sensitive(LayoutAlgorithm)
    def layout_algorithm(self, value):
        self._layout_algorithm = value

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the graph line. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def link(self) -> Optional[LinkOptions]:
        """Link style options.

        :rtype: :class:`LinkOptions` or :obj:`None <python:None>`
        """
        return self._link

    @link.setter
    @class_sensitive(LinkOptions)
    def link(self, value):
        self._link = value

    @property
    def relative_x_value(self) -> Optional[bool]:
        """When ``True``, X values in the data set are relative to the current
        :meth:`point_start <AreaOptions.point_start>`,
        :meth:`point_interval <AreaOptions.point_interval>`, and
        :meth:`point_interval_unit <AreaOptions.point_interval_unit>` settings. This
        allows compression of the data for datasets with irregular X values. Defaults to
        ``False``.

        The real X values are computed on the formula ``f(x) = ax + b``, where ``a`` is
        the :meth:`point_interval <AreaOptions.point_interval>` (optionally with a time
        unit given by :meth:`point_interval_unit <AreaOptions.point_interval_unit>`), and
        ``b`` is the :meth:`point_start <AreaOptions.point_start>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._relative_x_value

    @relative_x_value.setter
    def relative_x_value(self, value):
        if value is None:
            self._relative_x_value = None
        else:
            self._relative_x_value = bool(value)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
        """Configuration for the shadow to apply to the tooltip. Defaults to
        ``False``.

        If ``False``, no shadow is applied.

        :returns: The shadow configuration to apply or a boolean setting which hides the
          shadow or displays the default shadow.
        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if isinstance(value, bool):
            self._shadow = value
        elif not value:
            self._shadow = None
        else:
            value = validate_types(value,
                                   types = ShadowOptions)
            self._shadow = value

    @property
    def zones(self) -> Optional[List[Zone]]:
        """An array defining zones within a series. Defaults to :obj:`None <python:None>`.

        Zones can be applied to the X axis, Y axis or Z axis for bubbles, according to the
        :meth:`zone_axis <AreaOptions.zone_axis>` setting.

        .. warning::

          The zone definitions have to be in ascending order regarding to the value.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of
          :class:`Zone` instances
        """
        return self._zones

    @zones.setter
    @class_sensitive(Zone,
                     force_iterable = True)
    def zones(self, value):
        self._zones = value

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

            'color_index': as_dict.get('colorIndex', None),
            'crisp': as_dict.get('crisp', None),
            'draggable': as_dict.get('draggable', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'layout_algorithm': as_dict.get('layoutAlgorithm', None),
            'line_width': as_dict.get('lineWidth', None),
            'link': as_dict.get('link', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'zones': as_dict.get('zones', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'colorIndex': self.color_index,
            'crisp': self.crisp,
            'draggable': self.draggable,
            'findNearestPointBy': self.find_nearest_point_by,
            'layoutAlgorithm': self.layout_algorithm,
            'lineWidth': self.line_width,
            'link': self.link,
            'relativeXValue': self.relative_x_value,
            'shadow': self.shadow,
            'zones': self.zones
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
