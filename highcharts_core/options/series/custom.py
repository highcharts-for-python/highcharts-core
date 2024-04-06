from typing import Optional, List

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core import errors
from highcharts_core.options.series.base import SeriesBase
from highcharts_core.options.series.data.base import DataBase
from highcharts_core.options.series.data.collections import DataPointCollection
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core import utility_functions
from highcharts_core.js_literal_functions import (
    assemble_js_literal,
    serialize_to_js_literal,
)

try:
    from highcharts_gantt.options.series.series_generator import SERIES_CLASSES
except ImportError:
    try:
        from highcharts_maps.options.series.series_generator import SERIES_CLASSES
    except ImportError:
        try:
            from highcharts_stock.options.series.series_generator import SERIES_CLASSES
        except ImportError:
            from highcharts_core.options.series.series_generator import SERIES_CLASSES


class CustomSeries(SeriesBase):
    """Class used to define a custom Highcharts series type."""

    def __init__(self, **kwargs):
        self._data_cls = None
        self._data_collection_cls = None
        self._data = None
        self._draw_points = None
        self.__parent_instance = None
        self._parent_type = None
        self._type = None

        self.data_cls = kwargs.get("data_cls", None)
        self.data_collection_cls = kwargs.get("data_collection_cls", None)
        self.data = kwargs.get("data", None)
        self.draw_points = kwargs.get("draw_points", None)
        self._parent_instance = kwargs.get("parent_instance", None)
        self.parent_type = kwargs.get("parent_type", None)
        self.type = kwargs.get("type", None)

        if not self._parent_instance and self.parent_type:
            del kwargs["data"]
            self._parent_instance = self._parent_cls(**kwargs)

        super().__init__(**kwargs)

    @property
    def data_cls(self):
        """The class object of the data type used by this custom series type.

        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`-descendant
          or :obj:`None <python:None>`
        """
        return self._data_cls

    @data_cls.setter
    def data_cls(self, value):
        if not value:
            self._data_cls = None
        elif isinstance(value, type):
            self._data_cls = value
        else:
            raise errors.HighchartsValueError(
                f".data_cls expects a subclass of DataBase. "
                f"Received: {value.__class__.__name__}"
            )

    @property
    def data_collection_cls(self):
        """The class object of the data point collection type used by this custom series.

        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`-descendent
          or :obj:`None <python:None>`
        """
        return self._data_collection_cls

    @data_collection_cls.setter
    def data_collection_cls(self, value):
        if not value:
            self._data_collection_cls = None
        elif isinstance(value, type):
            self._data_collection_cls = value
        else:
            raise errors.HighchartsValueError(
                f".data_cls expects a subclass of DataPointCollection. "
                f"Received: {value.__class__.__name__}"
            )

    @property
    def data(self) -> Optional[List[DataBase] | DataPointCollection]:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`DataBase` or
          :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not utility_functions.is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = self._data_cls.from_array(value)

    @property
    def _parent_cls(self):
        """The class object of the parent series type.

        :rtype: :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descendant
          or :obj:`None <python:None>`
        """
        if not self.parent_type:
            return None

        return SERIES_CLASSES[self.parent_type]

    @property
    def _parent_instance(self) -> Optional[SeriesBase]:
        """Container property which stores an instance of the parent type.

        Used to provide access to the parent series type's methods and properties.

        :rtype: :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
        """
        return self.__parent_instance

    @_parent_instance.setter
    def _parent_instance(self, value):
        if not value:
            self.__parent_instance = None
        elif isinstance(value, SeriesBase):
            self.__parent_instance = value
            self.parent_type = value.type
        elif isinstance(value, dict) and self._parent_cls:
            self.__parent_instance = self._parent_cls.from_dict(value)
        else:
            raise errors.HighchartsTypeError(
                f"_parent_instance must be a SeriesBase instance, not {value.__class__.__name__}"
            )

    @property
    def draw_points(self) -> CallbackFunction:
        """The ``drawPoints()`` (JS) function that is used to
        render the series points. Defaults to :obj:`None <python:None>`,
        which will inherit from the parent series type.

        Expects a JS function that accepts accepts no arguments,
        but which receives the series object as ``this``.

        :returns:

        :rtype: :class:`CallbackFunction <highcharts_core.js_literal_functions.CallbackFunction>`
        """
        return self._draw_points

    @draw_points.setter
    @class_sensitive(CallbackFunction)
    def draw_points(self, value):
        if not value:
            self._draw_points = None
        else:
            self._draw_points = value

    @property
    def parent_type(self) -> str:
        """The series type on which this custom series is based.

        Expects a :class:`str <python:str>` value that corresponds to the
        name of the series type (that series type's read-only ``.type``
        property, e.g. ``'line'`` for a line series, etc.

        :rtype: :class:`str <python:str>`
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, value):
        if not value:
            self._parent_type = None
        elif isinstance(value, SeriesBase):
            self._parent_type = value.type
        elif isinstance(value, str):
            if value not in SERIES_CLASSES:
                raise errors.HighchartsValueError(
                    f"Received a type value that was not recognized: '{value}'"
                )

            self._parent_type = value
        else:
            raise errors.HighchartsValueError(
                f"parent_type must be a str or SeriesBase descendent instance "
                f"or class, not {value.__class__.__name__}"
            )

    @property
    def type(self) -> str:
        """The name given to the custom series type.

        :rtype: :class:`str <python:str>`
        """
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        elif isinstance(value, str):
            value = value.lower()
            value = validators.variable_name(value, allow_empty=False)

            self._type = value
        else:
            raise errors.HighchartsValueError(
                f"type must be a str. Received: {value.__class__.__name__}"
            )

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            "accessibility": as_dict.get("accessibility", None),
            "allow_point_select": as_dict.get("allowPointSelect", None),
            "animation": as_dict.get("animation", None),
            "class_name": as_dict.get("className", None),
            "clip": as_dict.get("clip", None),
            "color": as_dict.get("color", None),
            "cursor": as_dict.get("cursor", None),
            "custom": as_dict.get("custom", None),
            "dash_style": as_dict.get("dashStyle", None),
            "data_labels": as_dict.get("dataLabels", None),
            "description": as_dict.get("description", None),
            "enable_mouse_tracking": as_dict.get("enableMouseTracking", None),
            "events": as_dict.get("events", None),
            "include_in_data_export": as_dict.get("includeInDataExport", None),
            "keys": as_dict.get("keys", None),
            "label": as_dict.get("label", None),
            "legend_symbol": as_dict.get("legendSymbol", None),
            "linked_to": as_dict.get("linkedTo", None),
            "marker": as_dict.get("marker", None),
            "on_point": as_dict.get("onPoint", None),
            "opacity": as_dict.get("opacity", None),
            "point": as_dict.get("point", None),
            "point_description_formatter": as_dict.get(
                "pointDescriptionFormatter", None
            ),
            "selected": as_dict.get("selected", None),
            "show_checkbox": as_dict.get("showCheckbox", None),
            "show_in_legend": as_dict.get("showInLegend", None),
            "skip_keyboard_navigation": as_dict.get("skipKeyboardNavigation", None),
            "sonification": as_dict.get("sonification", None),
            "states": as_dict.get("states", None),
            "sticky_tracking": as_dict.get("stickyTracking", None),
            "threshold": as_dict.get("threshold", None),
            "tooltip": as_dict.get("tooltip", None),
            "turbo_threshold": as_dict.get("turboThreshold", None),
            "visible": as_dict.get("visible", None),
            "animation_limit": as_dict.get("animationLimit", None),
            "boost_blending": as_dict.get("boostBlending", None),
            "boost_threshold": as_dict.get("boostThreshold", None),
            "color_axis": as_dict.get("colorAxis", None),
            "color_index": as_dict.get("colorIndex", None),
            "color_key": as_dict.get("colorKey", None),
            "connect_ends": as_dict.get("connectEnds", None),
            "connect_nulls": as_dict.get("connectNulls", None),
            "crisp": as_dict.get("crisp", None),
            "crop_threshold": as_dict.get("cropThreshold", None),
            "data_sorting": as_dict.get("dataSorting", None),
            "drag_drop": as_dict.get("dragDrop", None),
            "find_nearest_point_by": as_dict.get("findNearestPointBy", None),
            "get_extremes_from_all": as_dict.get("getExtremesFromAll", None),
            "inactive_other_points": as_dict.get("inactiveOtherPoints", None),
            "linecap": as_dict.get("linecap", None),
            "line_width": as_dict.get("lineWidth", None),
            "negative_color": as_dict.get("negativeColor", None),
            "point_description_format": as_dict.get("pointDescriptionFormat", None),
            "point_interval": as_dict.get("pointInterval", None),
            "point_interval_unit": as_dict.get("pointIntervalUnit", None),
            "point_placement": as_dict.get("pointPlacement", None),
            "point_start": as_dict.get("pointStart", None),
            "relative_x_value": as_dict.get("relativeXValue", None),
            "shadow": as_dict.get("shadow", None),
            "soft_threshold": as_dict.get("softThreshold", None),
            "stacking": as_dict.get("stacking", None),
            "step": as_dict.get("step", None),
            "zone_axis": as_dict.get("zoneAxis", None),
            "zones": as_dict.get("zones", None),
            "data": as_dict.get("data", None),
            "id": as_dict.get("id", None),
            "index": as_dict.get("index", None),
            "legend_index": as_dict.get("legendIndex", None),
            "name": as_dict.get("name", None),
            "stack": as_dict.get("stack", None),
            "x_axis": as_dict.get("xAxis", None),
            "y_axis": as_dict.get("yAxis", None),
            "z_index": as_dict.get("zIndex", None),

            "draw_points": as_dict.get("drawPoints", None),
            "parent_type": as_dict.get("parentType", None),
            "type": as_dict.get("type", None),
            "parent_instance": as_dict.get("parentInstance", None),
            "data_cls": as_dict.get("dataCls", None),
            "data_collection_cls": as_dict.get("dataCollectionCls", None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls=None) -> dict:
        untrimmed = {
            "drawPoints": self.draw_points,
            "parentType": self.parent_type,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls=in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        if self._parent_instance:
            parent_instance_untrimmed = self._parent_instance._to_untrimmed_dict(
                in_cls=in_cls
            )
        else:
            parent_instance_untrimmed = {}

        for key in untrimmed:
            parent_instance_untrimmed[key] = untrimmed[key]

        return parent_instance_untrimmed

    def to_registration_js_literal(
        self, filename=None, encoding="utf-8", careful_validation=False
    ) -> Optional[str]:
        """Return the JS literal string that is used to register the custom series
        type within Highcharts prior to its rendering in the chart.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :param careful_validation: if ``True``, will carefully validate JavaScript values
        along the way using the
        `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
        to ``False``.

        .. warning::

            Setting this value to ``True`` will significantly degrade serialization
            performance, though it may prove useful for debugging purposes.

        :type careful_validation: :class:`bool <python:bool>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        prefix_as_str = (
            f"""Highcharts.seriesType('{self.type}', '{self.parent_type}', """
        )

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            if key in ["type", "parentType"]:
                continue
            item = untrimmed[key]
            serialized = serialize_to_js_literal(
                item, encoding=encoding, careful_validation=careful_validation
            )
            if serialized is not None:
                as_dict[key] = serialized

        as_str = assemble_js_literal(as_dict, careful_validation=careful_validation)

        as_str = prefix_as_str + as_str + "\n);"

        if filename:
            with open(filename, "w", encoding=encoding) as file_:
                file_.write(as_str)

        return as_str
