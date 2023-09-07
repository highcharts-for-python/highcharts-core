from typing import Optional, List

from highcharts_core.options.series.base import SeriesBase
from highcharts_core.options.series.data.treegraph import TreegraphData, TreegraphDataCollection
from highcharts_core.options.plot_options.treegraph import TreegraphOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict, is_ndarray


class TreegraphSeries(SeriesBase, TreegraphOptions):
    """General options to apply to all :term:`Treegraph` series types.
    
    A treegraph visualizes a relationship between ancestors and descendants with a clear parent-child relationship,
    e.g. a family tree or a directory structure.
    
    .. figure:: ../../../_static/treegraph-example.png
      :alt: Treegraph Example Chart
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
        return TreegraphDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return TreegraphData

    @property
    def data(self) -> Optional[List[TreegraphData] | TreegraphDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`TreegraphData` instances,
        it accepts as input:

        .. tabs::

          .. tab:: 1D Array of Arrays
          
            A one-dimensional collection where each member of the collection is itself
            a collection of data points.
            
            .. note::
            
              If using the Array of Arrays pattern you *must* set 
              :meth:`.keys <highcharts_core.options.series.treegraph.TreegraphSeries.keys>` to indicate
              which value in the inner array corresponds to 
              :meth:`.id <highcharts_core.options.series.treegraph.TreegraphSeries.id>`, 
              :meth:`.parent <highcharts_core.options.series.treegraph.TreegraphSeries.parent>`, or
              :meth:`.name <highcharts_core.options.series.treegraph.TreegraphSeries.name>`.
              
          .. tab:: Object Collection

            A one-dimensional collection of :class:`TreegraphData` objects or
            :class:`dict <python:dict>` instances coercable to :class:`TreegraphData`

        :rtype: :class:`list <python:list>` of :class:`TreegraphData` or
          :class:`TreegraphDataCollection` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = TreegraphData.from_array(value)
            
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
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_index': as_dict.get('colorIndex', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'step': as_dict.get('step', None),

            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_start': as_dict.get('pointStart', None),
            'stacking': as_dict.get('stacking', None),

            'allow_traversing_tree': as_dict.get('allowTraversingTree', None),
            'collapse_button': as_dict.get('collapseButton', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'fill_space': as_dict.get('fillSpace', None),
            'link': as_dict.get('link', None),
            'reversed': as_dict.get('reversed', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed
