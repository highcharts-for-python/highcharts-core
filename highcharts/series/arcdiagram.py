from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.series.base import SeriesBase
from highcharts.series.data.base import DataBase
from highcharts.plot_options.arcdiagram import ArcDiagramOptions
from highcharts.utility_functions import mro_to_dict, mro_init
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.labels import DataLabel
from highcharts.utility_classes.nodes import NodeOptions


class NodeOptions(HighchartsMeta):
    """Configuration of options for nodes in an Arc Diagram that are associated with a
    specific :class:`ArcDiagramSeries` by the :meth:`ArcDiagramSeries.id`."""

    def __init__(self, **kwargs):
        self._color = None
        self._color_index = None
        self._data_labels = None
        self._id = None
        self._name = None
        self._offset_horizontal = None
        self._offset_vertical = None

        self.color = kwargs.pop('color', None)
        self.color_index = kwargs.pop('color_index', None)
        self.data_labels = kwargs.pop('data_labels', None)
        self.id = kwargs.pop('id', None)
        self.name = kwargs.pop('name', None)
        self.offset_horizontal = kwargs.pop('offset_horizontal', None)
        self.offset_vertical = kwargs.pop('offset_vertical', None)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the auto-generated node. Defaults to :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        auto-generated node. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def data_labels(self) -> Optional[DataLabel]:
        """Options for the node's data label.

        :rtype: :class:`DataLabel`, :class:`list <python:list>` of :class:`DataLabel`, or
          :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    @class_sensitive(DataLabel)
    def data_labels(self, value):
        self._data_labels = value

    @property
    def id(self) -> Optional[str]:
        """The id of the auto-generated node, refering to the ``from`` or ``to`` setting
        of the link. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def name(self) -> Optional[str]:
        """The name to display for the node in data labels and tooltips. Defaults to
        :obj:`None <python:None>`.

        .. hint::

          Use this when the name is different from the :meth:`NodeOptions.id`. Where the
          ``id`` must be unique for each node, this is not necessary for the name.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def offset_horizontal(self) -> Optional[str | int | float | Decimal]:
        """The horizontal offset of a node, expressed in either pixels or as a percentage
        of the node size. Defaults to :obj:`None <python:None>`.

        .. hint::

          Positive values shift the node right, negative shift it left.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._offset_horizontal

    @offset_horizontal.setter
    def offset_horizontal(self, value):
        if value is None:
            self._offset_horizontal = None
        else:
            if isinstance(value, str):
                value = value.lower()
                if '%' not in value:
                    raise errors.HighchartsValueError(f'offset_horizontal must be either '
                                                      f'a numeric value, or a percentage '
                                                      f'string. "%" was not found in: '
                                                      f'{value}')
            else:
                value = validators.numeric(value)

            self._offset_horizontal = value

    @property
    def offset_vertical(self) -> Optional[str | int | float | Decimal]:
        """The vertical offset of a node, expressed in either pixels or as a percentage
        of the node size. Defaults to :obj:`None <python:None>`.

        .. hint::

          Positive values shift the node down, negative shift it up.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._offset_vertical

    @offset_vertical.setter
    def offset_vertical(self, value):
        if value is None:
            self._offset_vertical = None
        else:
            if isinstance(value, str):
                value = value.lower()
                if '%' not in value:
                    raise errors.HighchartsValueError(f'offset_vertical must be either '
                                                      f'a numeric value, or a percentage '
                                                      f'string. "%" was not found in: '
                                                      f'{value}')
            else:
                value = validators.numeric(value)

            self._offset_vertical = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'id': as_dict.pop('id', None),
            'name': as_dict.pop('name', None),
            'offset_horizontal': as_dict.pop('offsetHorizontal', None),
            'offset_vertical': as_dict.pop('offsetVertical', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'color': self.color,
            'colorIndex': self.color_index,
            'dataLabels': self.data_labels,
            'id': self.id,
            'name': self.name,
            'offsetHorizontal': self.offset_horizontal,
            'offsetVertical': self.offset_vertical,
        }

        return untrimmed


class ArcDiagramData(DataBase):
    """The definition of a data point for use in an :class:`ArcDiagramSeries`."""

    def __init__(self, **kwargs):
        self._from_ = None
        self._to = None
        self._weight = None

        self.from_ = kwargs.pop('from_', None)
        self.to = kwargs.pop('to', None)
        self.weight = kwargs.pop('weight', None)

        super().__init__(**kwargs)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color for the individual link. Defaults to :obj:`None <python:None>`, which
        sets the link color the same as the node it extends from.

        .. hint::

          The ``series.fillOpacity`` option also applies to the points, so when setting a
          specific link color, consider setting the ``fillOpacity`` to 1.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._color

    @property
    def from_(self) -> Optional[str]:
        """The :meth:`ArcDiagramData.id` or :meth:`ArcDiagramData.name` of the node that
        the link runs from. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._from_

    @from_.setter
    def from_(self, value):
        self._from_ = validators.string(value, allow_empty = True)

    @property
    def to(self) -> Optional[str]:
        """The :meth:`ArcDiagramData.id` or :meth:`ArcDiagramData.name` of the node that
        the link runs to. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.string(value, allow_empty = True)

    @property
    def weight(self) -> Optional[int | float | Decimal]:
        """The weight of the link between the nodes. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'from_': as_dict.pop('from', None),
            'to': as_dict.pop('to', None),
            'weight': as_dict.pop('weight', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,

            'from': self.from_,
            'to': self.to,
            'weight': self.weight,
        }

        return untrimmed


class ArcDiagramSeries(SeriesBase, ArcDiagramOptions):
    """Arc diagram series is a chart drawing style in which the vertices of the chart
    are positioned along a line on the Euclidean plane and the edges are drawn as a
    semicircle in one of the two half-planes delimited by the line, or as smooth
    curves formed by sequences of semicircles.

    .. figure:: _static/arcdiagram-example.png
      :alt: Arc Diagram Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._link_weight = None
        self._nodes = None
        self._offset = None

        self.link_weight = kwargs.pop('link_weight', None)
        self.nodes = kwargs.pop('nodes', None)
        self.offset = kwargs.pop('offset', None)

        mro_init(self, kwargs)

    @property
    def data(self) -> Optional[ArcDiagramData]:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`ArcDiagramData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    @class_sensitive(ArcDiagramData, force_iterable = True)
    def data(self, value):
        self._data = value

    @property
    def link_weight(self) -> Optional[int | float | Decimal]:
        """The global link weight. Defaults to :obj:`None <python:None>`.

        If :obj:`None <python:None>`, width is calculated per link, depending on the
        weight value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._link_weight

    @link_weight.setter
    def link_weight(self, value):
        if value is None:
            self._link_weight = None
        else:
            self._link_weight = validators.numeric(value,
                                                   minimum = 0)

    @property
    def nodes(self) -> Optional[List[NodeOptions]]:
        """A collection of options for configuring individual nodes. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of :class:`NodeOptions` or
          :obj:`None <python:None>`
        """
        return self._nodes

    @nodes.setter
    @class_sensitive(NodeOptions, force_iterable = True)
    def nodes(self, value):
        self._nodes = value

    @property
    def offset(self) -> Optional[str]:
        """The offset of an arc diagram nodes column in relation to the plot area,
        expressed as a percentage of the plot area. If :obj:`None <python:None>`, the
        series is placed so that the biggest node is touching the bottom border of the
        plot area (equivalent to ``'100%'``). Defaults to :obj:`None <python:None>`.

        .. hint::

          For example, setting the offset to ``'50%'`` will place the nodes in the center
          of the chart.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._offset

    @offset.setter
    def offset(self, value):
        if not value:
            self._offset = None
        else:
            value = validators.string(value)
            value = value.lower()
            if '%' not in value:
                raise errors.HighchartsValueError(f'offset expects a percentage string. '
                                                  f'No "%" character found in: {value}')
            self._offset = value

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

            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'centered_links': as_dict.pop('centeredLinks', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'color_index': as_dict.pop('colorIndex', None),
            'colors': as_dict.pop('colors', None),
            'equal_nodes': as_dict.pop('equalNodes', None),
            'levels': as_dict.pop('levels', None),
            'link_opacity': as_dict.pop('linkOpacity', None),
            'min_link_width': as_dict.pop('minLinkWidth', None),
            'node_width': as_dict.pop('nodeWidth', None),
            'reversed': as_dict.pop('reversed', None),
            'sticky_tracking': as_dict.pop('stickyTracking', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),

            'link_weight': as_dict.pop('linkWeight', None),
            'nodes': as_dict.pop('nodes', None),
            'offset': as_dict.pop('offset', None),
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'linkWeight': self.link_weight,
            'nodes': self.nodes,
            'offset': self.offset
        }
        parent_as_dict = mro_to_dict(self)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
