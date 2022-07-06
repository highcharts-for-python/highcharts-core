"""Implements the :class:`HighchartOptions` class."""
from typing import Optional, Any

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta
from highcharts.decorators import class_sensitive
from highcharts.constants import DEFAULT_COLORS

from highcharts.accessibility import Accessibility
from highcharts.annotations import Annotation
from highcharts.boost import Boost
from highcharts.caption import Caption
from highcharts.chart import Chart
from highcharts.axes.color_access import ColorAxis
from highcharts.credits import Credits
from highcharts.data import Data
from highcharts.defs import MarkerDefinition
from highcharts.drilldown import Drilldown
from highcharts.exporting import Exporting
from highcharts.lang import Language
from highcharts.legend import Legend
from highcharts.loading import Loading
from highcharts.loading import Navigation
from highcharts.no_data import NoData
from highcharts.pane import Pane
from highcharts.plot_options import PlotOptions
from highcharts.responsive import Responsive
from highcharts.series import Series
from highcharts.subtitle import Subtitle
from highcharts.time import Time
from highcharts.title import Title
from highcharts.tooltip import Tooltip
from highcharts.x_axis import XAxis
from highcharts.y_axis import YAxis
from highcharts.z_axis import ZAxis

# Highcharts Stock Classes
from highcharts.navigator import Navigator
from highcharts.range_selector import RangeSelector
from highcharts.scrollbar import Scrollbar
from highcharts.stock_tools import StockTools

# Highcharts Maps Classes
from highcharts.map_navigation import MapNavigation
from highcharts.map_view import MapView


class Options(HighchartsMeta):
    """Metaclass which establishes properties shared across different variations of the
    Highcharts configuration objects."""

    def __init__(self, **kwargs):
        self._accessibility = None
        self._annotations = None
        self._caption = None
        self._chart = None
        self._color_axis = None
        self._colors = None
        self._credits = None
        self._data = None
        self._defs = None
        self._exporting = None
        self._language = None
        self._legend = None
        self._loading = None
        self._navigation = None
        self._plot_options = None
        self._responsive = None
        self._series = None
        self._subtitle = None
        self._time = None
        self._title = None
        self._tooltip = None
        self._x_axis = None
        self._y_axis = None

        self.accessibility = kwargs.pop('accessibility', None)
        self.annotations = kwargs.pop('annotations', None)
        self.caption = kwargs.pop('caption', None)
        self.chart = kwargs.pop('chart', None)
        self.color_axis = kwargs.pop('color_axis', None)
        self.colors = kwargs.pop('colors', DEFAULT_COLORS)
        self.credits = kwargs.pop('credits', None)
        self.data = kwargs.pop('data', None)
        self.defs = kwargs.pop('defs', None)
        self.exporting = kwargs.pop('exporting', None)
        self.language = kwargs.pop('language', None)
        self.legend = kwargs.pop('legend', None)
        self.loading = kwargs.pop('loading', None)
        self.navigation = kwargs.pop('navigation', None)
        self.plot_options = kwargs.pop('plot_options', None)
        self.responsive = kwargs.pop('responsive', None)
        self.series = kwargs.pop('series', None)
        self.subtitle = kwargs.pop('subtitle', None)
        self.time = kwargs.pop('time', None)
        self.title = kwargs.pop('title', None)
        self.tooltip = kwargs.pop('tooltip', None)
        self.x_axis = kwargs.pop('x_axis', None)
        self.y_axis = kwargs.pop('y_axis', None)

    @property
    def accessibility(self) -> Optional[Accessibility]:
        """Options for configuring accessibility for the chart.

        .. note::

          Requires the accessibility module to be loaded in the browser. For a description
          of the module and information on its features, see
          `Highcharts Accessibility <https://www.highcharts.com/docs/accessibility/accessibility-module>`_.

        :returns: The accessibility configuration for the chart or :obj:`None <python:None>`
        :rtype: :class:`Accessibility <highcharts.accessibility.Accessibility>` /
          :obj:`None <python:None>`

        :raise HighchartsError: if setting the value to an incompatible type

        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(Accessibility)
    def accessibility(self, value: Optional[Any[Accessibility, dict, str]]):
        self._accessibility = value

    @property
    def annotations(self) -> Optional[Annotation]:
        """A basic type of an annotation. It allows adding custom labels or shapes. The
        items can be tied to points, axis coordinates or chart pixel coordinates.

        :returns: A collection of the annotations applied to the chart.
        :rtype: :class:`list <python:list>` of :class:`Annotation` objects or
          :obj:`None <python:None>` if no annotations are applied

        """
        return self._annotations

    @annotations.setter
    @class_sensitive(Annotation, force_iterable = True)
    def annotations(self, value):
        self._annotations = value

    @property
    def caption(self):
        """The chart's caption, which will render below the chart and will be part of
        exported charts.

        .. note::

          The caption can be updated after chart initialization through the
          ``Chart.update`` or ``Chart.caption.update`` JavaScript methods.

        :returns: The chart's caption or :obj:`None <python:None>`
        :rtype: :class:`Caption` / :obj:`None <python:None>`
        """
        return self._caption

    @caption.setter
    @class_sensitive(Caption)
    def caption(self, value):
        self._caption = value

    @property
    def chart(self):
        """General options for the chart.

        .. note::

          This property is perhaps one of the most important properties you will use when
          configuring your Highcharts data visualization.

        :returns: A :class:`Chart` configuration object or :obj:`None <python:None>`
        :rtype: :class:`Chart` or :obj:`None <python:None>`
        """
        return self._chart

    @chart.setter
    @class_sensitive(Chart)
    def chart(self, value):
        self._chart = value

    @property
    def color_axis(self):
        """A color axis for series.

        Visually, the color axis will appear as a gradient or as separate items inside the
        legend, depending on whether the axis is scalar or based on data classes.

        A scalar color axis is represented by a gradient. The colors either range between
        the ``minimum_color`` and the ``maximum_color``, or for more fine grained control
        the colors can be defined in :ref:`stops <ColorAxis.stops>`. Often times, the
        color axis needs to be  adjusted to get the right color spread for the data. In
        addition to stops, consider using a logarithmic axis type, or setting min and max
        to avoid the colors being determined by outliers.

        For supported color formats, please see
        `the documentation article about colors <https://www.highcharts.com/docs/chart-design-and-style/colors>`_.


        When :ref:`data_classes <ColorAxis.data_classes>` are used, the ranges are
        subdivided into separate classes like categories based on their values. This can
        be used for ranges between two values, but also for a true category. However, when
        your data is categorized, it may be as convenient to add each category to a
        separate series.

        .. warning::

          Color axis does not work with: ``sankey``, ``sunburst``, ``dependencywheel``,
          ``networkgraph``, ``wordcloud``, ``venn``, ``gauge`` and ``solidgauge`` series types.

        See the :ref:`Axis` object for programmatic access to the axis.

        :returns: A collection of :class:`ColorAxis` objects defining the color axis to
          apply, or :obj:`None <python:None>`.
        :rtype: :class:`list <python:list>` of :class:`ColorAxis` or
          :obj:`None <python:None>`
        """
        return self._color_axis

    @color_axis.setter
    @class_sensitive(ColorAxis, force_iterable = True)
    def color_axis(self, value):
        self._color_axis = value

    @property
    def colors(self):
        """An array containing the default colors for the chart's series.

        When all colors are used, new colors are pulled from the start again.

        Default colors can also be set on a series or ``series.type`` basis, see
        :ref:`Column.colors` and :ref:`Pie.colors`.

        .. warning::

          In styled mode, the colors option does not exist.

          Instead, colors are defined in CSS and applied either through series or point
          class names, or through the :ref:`Chart.color_count` option.

          Defaults to:

          .. code-block:: python

            ["#7cb5ec", "#434348", "#90ed7d", "#f7a35c", "#8085e9", "#f15c80", "#e4d354", "#2b908f", "#f45b5b", "#91e8e1"]

        :returns: A collection of hex color strings.
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        return self._colors

    @colors.setter
    @class_sensitive(str, force_iterable = True)
    def colors(self, value):
        self._colors = value

    @property
    def credits(self):
        """Highchart by default puts a credits label in the lower right corner of the
        chart. This can be changed using these options.

        :returns: :class:`Credits` configuration or :obj:`None <python:None>`
        :rtype: :class:`Credits` or :obj:`None <python:None>`
        """
        return self._credits

    @credits.setter
    @class_sensitive(Credits)
    def credits(self, value):
        self._credits = value

    @property
    def data(self):
        """The ``data`` property provides a simplified interface for adding data to a
        chart from sources like CVS, HTML tables, or grid views. See also
        `the tutorial article on the Data module <https://www.highcharts.com/docs/working-with-data/data-module>`_.

        .. warning::

          It requires the ``modules/data.js`` file to be loaded in the browser / client.

        .. warning::

          Please note that the default way of adding data in Highcharts, without the need
          of a module, is through the ``series.type.data`` property.

        :returns: The :class:`Data` object or :obj:`None <python:None>`
        :rtype: :class:`Data` object or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    @class_sensitive(Data)
    def data(self, value):
        self._data = value

    @property
    def defs(self):
        """Options for configuring markers for annotations.

        :returns: A collection of :class:`MarkerDefinition` objects, or
          :obj:`None <python:None>`
        :rtype: :class:`list <python:list>` of :class:`MarkerDefinition`
        """
        return self._defs

    @defs.setter
    @class_sensitive(MarkerDefinition, force_iterable = True)
    def defs(self, value):
        self._defs = value

    @property
    def exporting(self):
        """Options to configure the export functionality enabled for the chart.

        :returns: The configuration of the chart's exporting functionality.
        :rtype: :class:`Exporting` or :obj:`None <python:None>`
        """
        return self._exporting

    @exporting.setter
    @class_sensitive(Exporting)
    def exporting(self, value):
        self._exporting = value

    @property
    def language(self):
        """Language object which can be used to configure the specific text to use in the
        chart.

        .. note::

          When working in JavaScript, the ``lang`` configuration is global and it can't be
          set on each chart initialization.

          Instead, use ``Highcharts.setOptions()`` to set it before any chart is
          initialized.

        :returns: A :class:`Language` object or :obj:`None <python:None>`
        :rtype: :class:`Language` or :obj:`None <python:None>`
        """
        return self._language

    @language.setter
    @class_sensitive(Language)
    def language(self, value):
        self._language = value

    @property
    def legend(self):
        """The legend is a box containing a symbol and name for each series item or point
        item in the chart. Each series (or points in case of pie charts) is represented by
        a symbol and its name in the legend.

        .. seealso::

          It is possible to override the symbol creator function and create
          `custom legend symbols <https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/studies/legend-custom-symbol/>`_.

        :returns: The :class:`Legend` configuration or :obj:`None <python:None>`
        :rtype: :class:`Legend` or :obj:`None <python:None>`
        """
        return self._legend

    @legend.setter
    @class_sensitive(Legend)
    def legend(self, value):
        self._legend = value

    @property
    def loading(self):
        """The loading options control the appearance of the loading screen that covers
        the plot area on chart operations.

        This screen only appears after an explicit call to ``chart.showLoading()`` in the
        browser. It is a utility for developers to communicate to the end user that
        something is going on, for example while retrieving new data via an XHR
        connection.

        .. hint::

          The "Loading..." text itself is **not** part of this configuration object, but
          is instead part of the :meth:`.language <Options.language>` configuration.

        :returns: The configuration of the loading screen or :obj:`None <python:None>`
        :rtype: :class:`Loading` or :obj:`None <python:None>`
        """
        return self._loading

    @loading.setter
    @class_sensitive(Loading)
    def loading(self, value):
        self._loading = value

    @property
    def navigation(self):
        """A collection of options for buttons and menus appearing in the exporting
        module or in Stock Tools.

        :returns: The configuration of the navigation buttons.
        :rtype: ;class:`Navigation` or :obj:`None <python:None>`
        """
        return self._navigation

    @navigation.setter
    @class_sensitive(Navigation)
    def navigation(self, value):
        self._navigation = value

    @property
    def plot_options(self):
        """A wrapper object for configurations applied to each series type.

        The config objects for each series can also be overridden for each series item as
        given in the series array.

        Configuration options for the series are given in three levels:

          * Options for all series in a chart are given in the
            :meth:`series <PlotOptions.series>` property.
          * Options for all series of a specific type are given in the corresponding
            property for that type, for example
            :meth:`plot_options.line <PlotOptions.line>`.
          * Finally, options for one single series are given in the
            :meth:`series <Options.series>` array.

        :returns: Configurations for how series should be plotted / displayed.
        :rtype: :class:`PlotOptions` or :obj:`None <python:None>`
        """
        return self._plot_options

    @plot_options.setter
    @class_sensitive(PlotOptions)
    def plot_options(self, value):
        self._plot_options = value

    @property
    def responsive(self):
        """Rules to apply for different screen or chart sizes.

        .. note::

          Each rule specifies additional chart options.

        :returns: Rules to apply for different screen or chart sizes.
        :rtype: :class:`Responsive` or :obj:`None <python:None>`
        """
        return self._responsive

    @responsive.setter
    @class_sensitive(Responsive)
    def responsive(self, value):
        self._responsive = value

    @property
    def series(self):
        """Series options for specific data and the data itself.

        :returns: The series to display along with configuration and data.
        :rtype: :class:`Series` or :obj:`None <python:None>`
        """
        return self._series

    @series.setter
    @class_sensitive(Series, force_iterable = True)
    def series(self, value):
        self._series = value

    @property
    def subtitle(self):
        """The chart's subtitle.

        .. note::

          This can be used both to display a subtitle below the main title, and to display
          random text anywhere in the chart.

        .. warning::

          The subtitle can be updated after chart initialization through the
          ``Chart.setTitle`` JavaScript method.

        :returns: Configuration of the chart's subtitle.
        :rtype: :class:`Subtitle` or :obj:`None <python:None>`
        """
        return self._subtitle

    @subtitle.setter
    @class_sensitive(Subtitle)
    def subtitle(self, value):
        self._subtitle = value

    @property
    def time(self):
        """Time options that can apply globally or to individual charts. These settings
        affect how datetime axes are laid out, how tooltips are formatted, how series
        :meth:`point_interval_unit <Series.point_interval_unit` works and how the
        Highcharts Stock range selector handles time.

        :returns: Configuration of applicable Time options.
        :rtype: :class:`Time` or :obj:`None <python:None>`
        """
        return self._time

    @time.setter
    @class_sensitive(Time)
    def time(self, value):
        self._time = value

    @property
    def title(self):
        """Options for configuring the chart's main title.

        :returns: Configuration of the chart's main title.
        :rtype: :class:`Title` or :obj:`None <python:None>`
        """
        return self._title

    @title.setter
    @class_sensitive(Title)
    def title(self, value):
        self._title = value

    @property
    def tooltip(self):
        """Options for the tooltip that appears when the user hovers over a series or point.

        :returns: Configuration settings for tooltips to display above the chart.
        :rtype: :class:`Tooltip` or :obj:`None <python:None>`
        """
        return self._tooltip

    @tooltip.setter
    @class_sensitive(Tooltip)
    def tooltip(self, value):
        self._tooltip = value

    @property
    def x_axis(self):
        """The X axis or category axis.

        Normally this is the horizontal axis, though if the chart is inverted this is the
        vertical axis.

        :returns: A collection of :class:`XAxis` objects
        :rtype: :class:`list <python:list>` of :class:`XAxis` or :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    @class_sensitive(XAxis, force_iterable = True)
    def x_axis(self, value):
        self._x_axis = value

    @property
    def y_axis(self):
        """The Y axis or value axis.

        Normally this is the vertical axis, though if the chart is inverted this is the
        horizontal axis.

        :returns: A collection of :class:`YAxis` objects
        :rtype: :class:`list <python:list>` of :class:`YAxis` or :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    @class_sensitive(YAxis, force_iterable = True)
    def y_axis(self, value):
        self._y_axis = value


class HighchartOptions(HighchartsMeta):
    """The Python representation of the `Highcharts <https://highcharts.com>`_
    ``options`` `configuration object <https://api.highcharts.com/highcharts/>`_."""

    def __init__(self, **kwargs):
        self._boost = None
        self._drilldown = None
        self._no_data = None
        self._pane = None
        self._z_axis = None

        self.boost = kwargs.pop('boost', None)
        self.drilldown = kwargs.pop('drilldown', None)
        self.no_data = kwargs.pop('no_data', None)
        self.pane = kwargs.pop('pane', None)
        self.z_axis = kwargs.pop('z_axis', None)

        super().__init__(**kwargs)

    @property
    def boost(self) -> Optional[Boost]:
        """Options for the Boost module.

        The Boost module allows certain series types to be rendered by WebGL instead of
        the default SVG. This allows hundreds of thousands of data points to be rendered
        in milliseconds. In addition to the WebGL rendering it saves time by skipping
        processing and inspection of the data wherever possible.

        .. warning::

          This introduces some limitations to what features are available in boost mode.
          See
          `the docs <https://www.highcharts.com/docs/advanced-chart-features/boost-module>`_
          for details.

        .. note:

          In addition to the global boost option, each series has a ``boostThreshold``
          that defines when the boost should kick in.

        :returns: The :class:`Boost <Boost>` object.
        :rtype: :class:`Boost <highcharts.boost.Boost>`

        """
        return self._boost

    @boost.setter
    @class_sensitive(Boost)
    def boost(self, value):
        self._boost = value

    @property
    def drilldown(self):
        """Options to configure :term:`drill down` functionality in the chart, which
        enables users to inspect increasingly high resolution data by clicking on chart
        items like columns or pie slices.

        .. note::

          The drilldown feature requires the ``drilldown.js`` file to be loaded in the
          browser/client. This file is found in the modules directory of the download
          package, or online at
          `code.highcharts.com/modules/drilldown.js <code.highcharts.com/modules/drilldown.js>`_.

        :returns: The options to configure the chart's drill down functionality.
        :rtype: :class:`Drilldown` or :obj:`None <python:None>`
        """
        return self._drilldown

    @drilldown.setter
    @class_sensitive(Drilldown)
    def drilldown(self, value):
        self._drilldown = value

    @property
    def no_data(self):
        """Options for displaying a message like "No data to display".

        .. warning::

          This feature requires the file ``no-data-to-display.js`` to be loaded in the
          page.

        .. tip::

          The actual text to display is set in the :meth:`language <Options.language>`
          options.

        :returns: Configuration of how to display a no data message.
        :rtype: :class:`NoData` or :obj:`None <python:None>`
        """
        return self._no_data

    @no_data.setter
    @class_sensitive(NoData)
    def no_data(self, value):
        self._no_data = value

    @property
    def pane(self):
        """The pane serves as a container for axes and backgrounds for circular gauges and
        polar charts.

        :returns: The Pane configuration options.
        :rtype: :class:`Pane` or :obj:`None <python:None>`
        """
        return self._pane

    @pane.setter
    @class_sensitive(Pane)
    def pane(self, value):
        self._pane = value

    @property
    def z_axis(self):
        """The Z axis or depth axis for 3D plots.

        :returns: A collection of :class:`ZAxis` objects
        :rtype: :class:`list <python:list>` of :class:`ZAxis` or :obj:`None <python:None>`
        """
        return self._z_axis

    @z_axis.setter
    @class_sensitive(ZAxis, force_iterable = True)
    def z_axis(self, value):
        self._z_axis = value

    @classmethod
    def from_dict(cls, as_dict):
        as_dict = validators.dict(as_dict, allow_empty = True)
        kwargs_dict = {
            'accessibility': as_dict.pop('accessibility', None),
            'annotations': as_dict.pop('annotations', None),
            'boost': as_dict.pop('boost', None),
            'caption': as_dict.pop('caption', None),
            'chart': as_dict.pop('chart', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'colors': as_dict.pop('colors', DEFAULT_COLORS),
            'credits': as_dict.pop('credits', None),
            'data': as_dict.pop('data', None),
            'defs': as_dict.pop('defs', None),
            'drilldown': as_dict.pop('drilldown', None),
            'exporting': as_dict.pop('exporting', None),
            'language': as_dict.pop('lang', None),
            'legend': as_dict.pop('legend', None),
            'loading': as_dict.pop('loading', None),
            'navigation': as_dict.pop('navigation', None),
            'no_data': as_dict.pop('noData', None),
            'pane': as_dict.pop('pane', None),
            'plot_options': as_dict.pop('plotOptions', None),
            'responsive': as_dict.pop('responsive', None),
            'series': as_dict.pop('series', None),
            'subtitle': as_dict.pop('subtitle', None),
            'time': as_dict.pop('time', None),
            'title': as_dict.pop('title', None),
            'tooltip': as_dict.pop('tooltip', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_axis': as_dict.pop('zAxis', None)
        }

        return cls(**kwargs_dict)

    def to_dict(self):
        untrimmed = {
            'accessibility': self.accessibility,
            'annotations': self.annotations,
            'boost': self.boost,
            'caption': self.caption,
            'chart': self.chart,
            'colorAxis': self.color_axis,
            'colors': self.colors,
            'credits': self.credits,
            'data': self.data,
            'defs': self.defs,
            'drilldown': self.drilldown,
            'exporting': self.exporting,
            'lang': self.language,
            'legend': self.legend,
            'loading': self.loading,
            'navigation': self.naviation,
            'noData': self.no_data,
            'pane': self.pane,
            'plotOptions': self.plot_options,
            'responsive': self.responsive,
            'series': self.series,
            'subtitle': self.subtitle,
            'time': self.time,
            'title': self.title,
            'tooltip': self.tooltip,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
            'zAxis': self.z_axis
        }

        return self.trim_dict(untrimmed)


class HighchartsStockOptions(Options):
    """The Python representation of the
    `Highcharts Stock <https://api.highcharts.com/highstock/>`_ configuration object."""

    def __init__(self, **kwargs):
        self._boost = None
        self._navigator = None
        self._no_data = None
        self._range_selector = None
        self._scrollbar = None
        self._stock_tools = None

        self.boost = kwargs.pop('boost', None)
        self.navigator = kwargs.pop('navigator', None)
        self.no_data = kwargs.pop('no_data', None)
        self.range_selector = kwargs.pop('range_selector', None)
        self.scrollbar = kwargs.pop('scrollbar', None)
        self.stock_tools = kwargs.pop('stock_tools', None)

        super().__init__(**kwargs)

    @property
    def boost(self) -> Optional[Boost]:
        """Options for the Boost module.

        The Boost module allows certain series types to be rendered by WebGL instead of
        the default SVG. This allows hundreds of thousands of data points to be rendered
        in milliseconds. In addition to the WebGL rendering it saves time by skipping
        processing and inspection of the data wherever possible.

        .. warning::

          This introduces some limitations to what features are available in boost mode.
          See
          `the docs <https://www.highcharts.com/docs/advanced-chart-features/boost-module>`_
          for details.

        .. note:

          In addition to the global boost option, each series has a ``boostThreshold``
          that defines when the boost should kick in.

        :returns: The :class:`Boost <Boost>` object.
        :rtype: :class:`Boost <highcharts.boost.Boost>`

        """
        return self._boost

    @boost.setter
    @class_sensitive(Boost)
    def boost(self, value):
        self._boost = value

    @property
    def navigator(self):
        """The navigator is a small series below the main series, displaying a view of the
        entire data set. It provides tools to zoom in and out on parts of the data as well
        as panning across the dataset.

        :returns: Configuration instructions for the :class:`Navigator` functionality.
        :rtype: :class:`Navigator` or :obj:`None <python:None>`
        """
        return self._navigator

    @navigator.setter
    @class_sensitive(Navigator)
    def navigator(self, value):
        self._navigator = value

    @property
    def no_data(self):
        """Options for displaying a message like "No data to display".

        .. warning::

          This feature requires the file ``no-data-to-display.js`` to be loaded in the
          page.

        .. tip::

          The actual text to display is set in the :meth:`language <Options.language>`
          options.

        :returns: Configuration of how to display a no data message.
        :rtype: :class:`NoData` or :obj:`None <python:None>`
        """
        return self._no_data

    @no_data.setter
    @class_sensitive(NoData)
    def no_data(self, value):
        self._no_data = value

    @property
    def range_selector(self):
        """The range selector is a tool for selecting ranges to display within the chart.
        It provides buttons to select preconfigured ranges in the chart, like 1 day, 1
        week, 1 month etc. It also provides input boxes where min and max dates can be
        manually input.

        :returns: Configuration instructions for the Range Selector functionality.
        :rtype: :class:`RangeSelector` or :obj:`None <python:None>`
        """
        return self._range_selector

    @range_selector.setter
    @class_sensitive(RangeSelector)
    def range_selector(self, value):
        self._range_selector = value

    @property
    def scrollbar(self):
        """The scrollbar is a means of panning over the X axis of a stock chart.

        .. note::

          Scrollbars can also be applied to other types of axes.

        .. note::

          Another approach to scrollable charts is the :meth:`Chart.scrollable_plot_area`
          option that is especially suitable for simpler cartesian charts on mobile.

        In styled mode, all the presentational options for the scrollbar are replaced by
        the classes ``.highcharts-scrollbar-thumb``, ``.highcharts-scrollbar-arrow``,
        ``.highcharts-scrollbar-button``, ``.highcharts-scrollbar-rifles`` and
        ``.highcharts-scrollbar-track``.

        :returns: The configuration options for the Scrollbar functionality.
        :rtype: :class:`Scrollbar` or :obj:`None <python:None>`
        """
        return self._scrollbar

    @scrollbar.setter
    @class_sensitive(Scrollbar)
    def scrollbar(self, value):
        self._scrollbar = value

    @property
    def stock_tools(self):
        """Configure the **stockTools** GUI strings in the chart.

        .. warning::

          Requires the `stockTools module <https://api.highcharts.com/highstock/>`_` to be
          loaded in the client/browser.

        .. seealso::

          For a description of the module and information on its features, see
          `Highcharts StockTools <https://api.highcharts.com/highstock/>`_.

        :returns: The configuration options for the StockTools functionality.
        :rtype: :class:`StockTools` or :obj:`None <python:None>`
        """
        return self._stock_tools

    @stock_tools.setter
    @class_sensitive(StockTools)
    def stock_tools(self, value):
        self._stock_tools = value

    @classmethod
    def from_dict(cls, as_dict):
        as_dict = validators.dict(as_dict, allow_empty = True)
        kwargs_dict = {
            'accessibility': as_dict.pop('accessibility', None),
            'annotations': as_dict.pop('annotations', None),
            'boost': as_dict.pop('boost', None),
            'caption': as_dict.pop('caption', None),
            'chart': as_dict.pop('chart', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'colors': as_dict.pop('colors', DEFAULT_COLORS),
            'credits': as_dict.pop('credits', None),
            'data': as_dict.pop('data', None),
            'defs': as_dict.pop('defs', None),
            'exporting': as_dict.pop('exporting', None),
            'language': as_dict.pop('lang', None),
            'legend': as_dict.pop('legend', None),
            'loading': as_dict.pop('loading', None),
            'navigation': as_dict.pop('navigation', None),
            'navigator': as_dict.pop('navigator', None),
            'no_data': as_dict.pop('noData', None),
            'plot_options': as_dict.pop('plotOptions', None),
            'range_selector': as_dict.pop('rangeSelector', None),
            'responsive': as_dict.pop('responsive', None),
            'scrollbar': as_dict.pop('scrollbar', None),
            'series': as_dict.pop('series', None),
            'stock_tools': as_dict.pop('stockTools', None),
            'subtitle': as_dict.pop('subtitle', None),
            'time': as_dict.pop('time', None),
            'title': as_dict.pop('title', None),
            'tooltip': as_dict.pop('tooltip', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None)
        }

        return cls(**kwargs_dict)

    def to_dict(self):
        untrimmed = {
            'accessibility': self.accessibility,
            'annotations': self.annotations,
            'boost': self.boost,
            'caption': self.caption,
            'chart': self.chart,
            'colorAxis': self.color_axis,
            'colors': self.colors,
            'credits': self.credits,
            'data': self.data,
            'defs': self.defs,
            'exporting': self.exporting,
            'lang': self.language,
            'legend': self.legend,
            'loading': self.loading,
            'navigation': self.naviation,
            'navigator': self.navigator,
            'noData': self.no_data,
            'plotOptions': self.plot_options,
            'rangeSelector': self.range_selector,
            'responsive': self.responsive,
            'scrollbar': self.scrollbar,
            'series': self.series,
            'stockTools': self.stock_tools,
            'subtitle': self.subtitle,
            'time': self.time,
            'title': self.title,
            'tooltip': self.tooltip,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return self.trim_dict(untrimmed)


class HighchartsMapsOptions(HighchartsMeta):
    """The Python representation of the
    `Highcharts Maps <https://api.highcharts.com/highmaps/>`_ configuration object."""

    def __init__(self, **kwargs):
        self._drilldown = None
        self._map_navigation = None
        self._map_view = None

        self.drilldown = kwargs.pop('drilldown', None)
        self.map_navigation = kwargs.pop('map_navigation', None)
        self.map_view = kwargs.pop('map_view', None)

    @property
    def drilldown(self):
        """Options to configure :term:`drill down` functionality in the chart, which
        enables users to inspect increasingly high resolution data by clicking on chart
        items like columns or pie slices.

        .. note::

          The drilldown feature requires the ``drilldown.js`` file to be loaded in the
          browser/client. This file is found in the modules directory of the download
          package, or online at
          `code.highcharts.com/modules/drilldown.js <code.highcharts.com/modules/drilldown.js>`_.

        :returns: The options to configure the chart's drill down functionality.
        :rtype: :class:`Drilldown` or :obj:`None <python:None>`
        """
        return self._drilldown

    @drilldown.setter
    @class_sensitive(Drilldown)
    def drilldown(self, value):
        self._drilldown = value

    @property
    def map_navigation(self):
        """The map navigation option handles buttons for navigation in addition to
        ``mousewheel`` and ``doubleclick`` handlers for map zooming.

        :returns: Configuration settings for map navigation.
        :rtype: :class:`MapNavigation` or :obj:`None <python:None>`
        """
        return self._map_navigation

    @map_navigation.setter
    @class_sensitive(MapNavigation)
    def map_navigation(self, value):
        self._map_navigation = value

    @property
    def map_view(self):
        """The map view options control the initial view of the chart, and how projection
        is set up for raw geoJSON maps.

        :returns: Configuration of the initial map view settings.
        :rtype: :class:`MapView` or :obj:`None <python:None>`
        """
        return self._map_view

    @map_view.setter
    @class_sensitive(MapView)
    def map_view(self, value):
        self._map_view = value

    @classmethod
    def from_dict(cls, as_dict):
        as_dict = validators.dict(as_dict, allow_empty = True)
        kwargs_dict = {
            'accessibility': as_dict.pop('accessibility', None),
            'annotations': as_dict.pop('annotations', None),
            'caption': as_dict.pop('caption', None),
            'chart': as_dict.pop('chart', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'colors': as_dict.pop('colors', DEFAULT_COLORS),
            'credits': as_dict.pop('credits', None),
            'data': as_dict.pop('data', None),
            'defs': as_dict.pop('defs', None),
            'drilldown': as_dict.pop('drilldown', None),
            'exporting': as_dict.pop('exporting', None),
            'language': as_dict.pop('lang', None),
            'legend': as_dict.pop('legend', None),
            'loading': as_dict.pop('loading', None),
            'map_navigation': as_dict.pop('mapNavigation', None),
            'map_view': as_dict.pop('mapView', None),
            'navigation': as_dict.pop('navigation', None),
            'plot_options': as_dict.pop('plotOptions', None),
            'responsive': as_dict.pop('responsive', None),
            'series': as_dict.pop('series', None),
            'subtitle': as_dict.pop('subtitle', None),
            'time': as_dict.pop('time', None),
            'title': as_dict.pop('title', None),
            'tooltip': as_dict.pop('tooltip', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None)
        }

        return cls(**kwargs_dict)

    def to_dict(self):
        untrimmed = {
            'accessibility': self.accessibility,
            'annotations': self.annotations,
            'caption': self.caption,
            'chart': self.chart,
            'colorAxis': self.color_axis,
            'colors': self.colors,
            'credits': self.credits,
            'data': self.data,
            'defs': self.defs,
            'drilldown': self.drilldown,
            'exporting': self.exporting,
            'lang': self.language,
            'legend': self.legend,
            'loading': self.loading,
            'mapNavigation': self.map_navigation,
            'mapView': self.map_view,
            'navigation': self.naviation,
            'plotOptions': self.plot_options,
            'responsive': self.responsive,
            'series': self.series,
            'subtitle': self.subtitle,
            'time': self.time,
            'title': self.title,
            'tooltip': self.tooltip,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis
        }

        return self.trim_dict(untrimmed)
