from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_classes.data_labels import DataLabel, NodeDataLabel


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

        self.color = kwargs.get('color', None)
        self.color_index = kwargs.get('color_index', None)
        self.data_labels = kwargs.get('data_labels', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.offset_horizontal = kwargs.get('offset_horizontal', None)
        self.offset_vertical = kwargs.get('offset_vertical', None)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the auto-generated node. Defaults to :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._color

    @color.setter
    def color(self, value):
        from highcharts_core import utility_functions
        self._color = utility_functions.validate_color(value)

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
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'data_labels': as_dict.get('dataLabels', None),
            'id': as_dict.get('id', None),
            'name': as_dict.get('name', None),
            'offset_horizontal': as_dict.get('offsetHorizontal', None),
            'offset_vertical': as_dict.get('offsetVertical', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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


class DependencyWheelNodeOptions(NodeOptions):
    """Variant of :class:`NodeOptions` for use in :class:`DependencyWheelSeries`."""

    def __init__(self, **kwargs):
        self._column = None
        self._level = None

        self.column = kwargs.get('column', None)
        self.level = kwargs.get('level', None)

        super().__init__(**kwargs)

    @property
    def column(self) -> Optional[int]:
        """An optional column index of where to place the node. Defaults to
        :obj:`None <python:None>`, which places it next to the preceding node.

        .. warning::

          This option name is counter-intuitive in inverted charts, like for example an
          organization chart rendered top-down. In this case the "columns" are rendered
          horizontally, more like "rows".

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._column

    @column.setter
    def column(self, value):
        self._column = validators.integer(value, allow_empty = True)

    @property
    def data_labels(self) -> Optional[NodeDataLabel]:
        """Options for the node's data label.

        :rtype: :class:`NodeDataLabel` or :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    @class_sensitive(NodeDataLabel)
    def data_labels(self, value):
        self._data_labels = value

    @property
    def level(self) -> Optional[int]:
        """An optional level index of where to place the node. Defaults to
        :obj:`None <python:None>`, which places it next to the preceding node.

        .. notes:

          Alias of :meth:`DependencyWheelNodeOptions.column`, but in inverted sankeys and
          org charts, the levels are laid out as rows.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._level

    @level.setter
    def level(self, value):
        self._level = validators.integer(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'data_labels': as_dict.get('dataLabels', None),
            'id': as_dict.get('id', None),
            'name': as_dict.get('name', None),
            'offset_horizontal': as_dict.get('offsetHorizontal', None),
            'offset_vertical': as_dict.get('offsetVertical', None),

            'column': as_dict.get('column', None),
            'level': as_dict.get('level', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'column': self.column,
            'level': self.level,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class OrganizationNodeOptions(DependencyWheelNodeOptions):
    """Variant of :class:`NodeOptions` for use in :class:`OrganizationSeries`."""

    def __init__(self, **kwargs):
        self._image = None
        self._layout = None
        self._title = None

        self.image = kwargs.get('image', None)
        self.layout = kwargs.get('layout', None)
        self.title = kwargs.get('title', None)

        super().__init__(**kwargs)

    @property
    def image(self) -> Optional[str]:
        """The URL of an image for the node card, which will be inserted by the default
        :meth:`DataLabel.node_formatter`. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._image

    @image.setter
    def image(self, value):
        if not value:
            self._image = None
        else:
            try:
                value = validators.url(value)
            except ValueError:
                value = validators.path(value)

            self._image = value

    @property
    def layout(self) -> Optional[str]:
        """The layout for the node's children. Defaults to :obj:`None <python:None>`,
        which behaves as ``'normal'``.

        Accepts:

          * ``'normal'`` - renders children spaced evenly below the node
          * ``'hanging'`` - renders children condensed in a vertical hanging fashion below
            the node, allowing for tighter packing of nodes in the resulting diagram

        .. note::

          Unless explicitly overridden, nodes whose parent use a ``'hanging'`` layout will
          *also* apply a ``'hanging'`` layout.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._layout

    @layout.setter
    def layout(self, value):
        if not value:
            self._layout = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['normal', 'hanging']:
                raise errors.HighchartsValueError(f'layout expects either "normal" or '
                                                  f'"hanging". Received: {value}')

            self._layout = value

    @property
    def title(self) -> Optional[str]:
        """The job title for the node card. Defaults to :obj:`None <python:None>`.

        .. note::

          Will be inserted by the default :meth:`DataLabel.node_formatter`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._title

    @title.setter
    def title(self, value):
        self._title = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'data_labels': as_dict.get('dataLabels', None),
            'id': as_dict.get('id', None),
            'name': as_dict.get('name', None),
            'offset_horizontal': as_dict.get('offsetHorizontal', None),
            'offset_vertical': as_dict.get('offsetVertical', None),

            'column': as_dict.get('column', None),
            'level': as_dict.get('level', None),

            'image': as_dict.get('image', None),
            'layout': as_dict.get('layout', None),
            'title': as_dict.get('title', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'image': self.image,
            'layout': self.layout,
            'title': self.title,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
