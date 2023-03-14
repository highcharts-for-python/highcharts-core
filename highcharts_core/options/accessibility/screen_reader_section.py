from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class ScreenReaderSection(HighchartsMeta):
    """Accessibility options for the screen reader information sections added before
    and after the chart."""

    def __init__(self, **kwargs):
        self._after_chart_format = None
        self._after_chart_formatter = None
        self._axis_range_date_format = None
        self._before_chart_format = None
        self._before_chart_formatter = None
        self._on_play_as_sound_click = None
        self._on_view_data_table_click = None

        self.after_chart_format = kwargs.get('after_chart_format', None)
        self.after_chart_formatter = kwargs.get('after_chart_formatter', None)
        self.axis_range_date_format = kwargs.get('axis_range_date_format', None)
        self.before_chart_format = kwargs.get('before_chart_format', None)
        self.before_chart_formatter = kwargs.get('before_chart_formatter', None)
        self.on_play_as_sound_click = kwargs.get('on_play_as_sound_click', None)
        self.on_view_data_table_click = kwargs.get('on_view_data_table_click', None)

    @property
    def after_chart_format(self) -> Optional[str]:
        """Format for the screen reader information region after the chart. Defaults to
        ``'{endOfChartMarker}'``.

        Supported HTML tags are:
          * ``<h1-6>``
          * ``<p>``
          * ``<div>``
          * ``<a>``
          * ``<ul>``
          * ``<ol>``
          * ``<li>``
          * ``<button>``

        Attributes are not supported, except for ``id`` on ``<div>``, ``<a>``, and
        ``<button>``.

        ``id`` is required on ``<a>`` and ``<button>`` in the format
        ``<tag id="abcd">``. Numbers, lower- and uppercase letters, ``"-"`` and ``"#"``
        are valid characters in IDs.

        The ``headingTagName`` is an auto-detected heading (``h1-h6``) that corresponds to
        the heading level below the previous heading in the DOM.

        .. tip::

          Set to empty string to remove the region altogether.

        :returns: Content to render in the screen reader information region after the
          chart.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._after_chart_format

    @after_chart_format.setter
    def after_chart_format(self, value):
        if value is None:
            self._after_chart_format = None
        elif not value:
            self._after_chart_format = ''
        else:
            self._after_chart_format = validators.string(value, allow_empty = False)

    @property
    def after_chart_formatter(self) -> Optional[CallbackFunction]:
        """A JavaScript formatter function to create the HTML contents of the hidden
        screen reader information region after the chart.

        The formatter function should receive one argument, ``chart``, referring to the
        chart object. It should return a string with the HTML content of the region.

        If :obj:`None <python:None>`, will returns an automatic description of the chart
        based on :meth:`ScreenReaderSection.after_chart_format`.

        :returns: JavaScript formatter function for the screen reader information region
          after the chart.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._after_chart_formatter

    @after_chart_formatter.setter
    @class_sensitive(CallbackFunction)
    def after_chart_formatter(self, value):
        self._after_chart_formatter = value

    @property
    def axis_range_date_format(self) -> Optional[str]:
        """Date format to use to describe range of datetime axes. Defaults to
        ``%Y-%m-%d %H:%M:%S``.

        .. seealso::

          * Detailed documentation on supported format replacement codes:
            https://api.highcharts.com/class-reference/Highcharts.Time#dateFormat

        :returns: Date format to use to describe range of datetime axes.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._axis_range_date_format

    @axis_range_date_format.setter
    def axis_range_date_format(self, value):
        self._axis_range_date_format = validators.string(value, allow_empty = True)

    @property
    def before_chart_format(self) -> Optional[str]:
        """Format for the screen reader information region before the chart. Defaults to

        .. code-block::

          '<{headingTagName}>{chartTitle}</{headingTagName}>
           <div>{typeDescription}</div><div>{chartSubtitle}</div>
           <div>{chartLongdesc}</div><div>{playAsSoundButton}</div>
           <div>{viewTableButton}</div><div>{xAxisDescription}</div>
           <div>{yAxisDescription}</div>
           <div>{annotationsTitle}{annotationsList}</div>'

        Supported HTML tags are:
          * ``<h1-6>``
          * ``<p>``
          * ``<div>``
          * ``<a>``
          * ``<ul>``
          * ``<ol>``
          * ``<li>``
          * ``<button>``

        Attributes are not supported, except for ``id`` on ``<div>``, ``<a>``, and
        ``<button>``.

        ``id`` is required on ``<a>`` and ``<button>`` in the format
        ``<tag id="abcd">``. Numbers, lower- and uppercase letters, ``"-"`` and ``"#"``
        are valid characters in IDs.

        The ``headingTagName`` is an auto-detected heading (``h1-h6``) that corresponds to
        the heading level below the previous heading in the DOM.

        .. tip::

          Set to empty string to remove the region altogether.

        :returns: Content to render in the screen reader information region before the
          chart.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._before_chart_format

    @before_chart_format.setter
    def before_chart_format(self, value):
        if value is None:
            self._before_chart_format = None
        elif not value:
            self._before_chart_format = ''
        else:
            self._before_chart_format = validators.string(value, allow_empty = False)

    @property
    def before_chart_formatter(self) -> Optional[CallbackFunction]:
        """A JavaScript formatter function to create the HTML contents of the hidden
        screen reader information region before the chart.

        The formatter function should receive one argument, ``chart``, referring to the
        chart object. It should return a string with the HTML content of the region.

        If :obj:`None <python:None>`, will returns an automatic description of the chart
        based on :meth:`ScreenReaderSection.before_chart_format`.

        :returns: JavaScript formatter function for the screen reader information region
          before the chart.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._before_chart_formatter

    @before_chart_formatter.setter
    @class_sensitive(CallbackFunction)
    def before_chart_formatter(self, value):
        self._before_chart_formatter = value

    @property
    def on_play_as_sound_click(self) -> Optional[CallbackFunction]:
        """JavaScript function to run upon clicking the "Play as sound" button in the
        screen reader region.

        By default Highcharts will call the ``chart.sonify`` JavaScript function.

        :returns: JavaScript function to run upon clicking the "Play as sound" button in
          the screen reader region.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._on_play_as_sound_click

    @on_play_as_sound_click.setter
    @class_sensitive(CallbackFunction)
    def on_play_as_sound_click(self, value):
        self._on_play_as_sound_click = value

    @property
    def on_view_data_table_click(self) -> Optional[CallbackFunction]:
        """JavaScript function to run upon clicking the "View as Data Table" link in the
        screen reader region.

        By default Highcharts will insert and set focus to a data table representation of
        the chart.

        :returns: JavaScript function to run upon clicking the "View as Data Table" link
          in the screen reader region.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._on_view_data_table_click

    @on_view_data_table_click.setter
    @class_sensitive(CallbackFunction)
    def on_view_data_table_click(self, value):
        self._on_view_data_table_click = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'after_chart_format': as_dict.get('afterChartFormat', None),
            'after_chart_formatter': as_dict.get('afterChartFormatter', None),
            'axis_range_date_format': as_dict.get('axisRangeDateFormat', None),
            'before_chart_format': as_dict.get('beforeChartFormat', None),
            'before_chart_formatter': as_dict.get('beforeChartFormatter', None),
            'on_play_as_sound_click': as_dict.get('onPlayAsSoundClick', None),
            'on_view_data_table_click': as_dict.get('onViewDataTableClick', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'afterChartFormat': self.after_chart_format,
            'afterChartFormatter': self.after_chart_formatter,
            'axisRangeDateFormat': self.axis_range_date_format,
            'beforeChartFormat': self.before_chart_format,
            'beforeChartFormatter': self.before_chart_formatter,
            'onPlayAsSoundClick': self.on_play_as_sound_click,
            'onViewDataTableClick': self.on_view_data_table_click
        }

        return untrimmed
