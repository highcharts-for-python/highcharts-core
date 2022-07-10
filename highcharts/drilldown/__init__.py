from typing import Optional, List

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import validate_types, class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.animation import AnimationOptions
from highcharts.utility_classes.breadcrumbs import BreadcrumbOptions
from highcharts.series import Series


class Drilldown(HighchartsMeta):
    """Options to configure :term:`drilldown` functionality in the chart, which
    enables users to inspect increasingly high resolution data by clicking on chart
    items like columns or pie slices.

    .. note::

      The drilldown feature requires the ``drilldown.js`` file to be loaded in the
      browser/client. This file is found in the modules directory of the download
      package, or online at
      `code.highcharts.com/modules/drilldown.js <code.highcharts.com/modules/drilldown.js>`_.

    """

    def __init__(self, **kwargs):
        self._active_axis_label_style = None
        self._active_data_label_style = None
        self._allow_point_drilldown = True
        self._animation = None
        self._breadcrumbs = None
        self._drillup_button = None
        self._series = None

        self.active_axis_label_style = kwargs.pop('active_axis_label_style',
                                                  constants.DEFAULT_DRILLDOWN_ACTIVE_AXIS_LABEL_STYLE)
        self.active_data_label_style = kwargs.pop('active_data_label_style',
                                                  constants.DEFAULT_DRILLDOWN_ACTIVE_DATA_LABEL_STYLE)
        self.allow_point_drilldown = kwargs.pop('allow_point_drilldown', True)
        self.animation = kwargs.pop('animation', None)
        self.breadcrumbs = kwargs.pop('breadcrumbs', None)
        self.drillup_button = kwargs.pop('drillup_button', None)
        self.series = kwargs.pop('series', None)

    @property
    def active_axis_label_style(self) -> Optional[dict]:
        f"""Additional styles to apply to the X axis label for a point that has drilldown
        data. By default, it is underlined and blue to invite to interaction.

        Defaults to:

        .. code-block:: python

          {constants.DEFAULT_DRILLDOWN_ACTIVE_AXIS_LABEL_STYLE}

        In styled mode, active label styles can be set with the
        ``.highcharts-drilldown-axis-label`` class.

        :rtype: :class:`dict <python:dict>`
        """
        return self._active_axis_label_style

    @active_axis_label_style.setter
    def active_axis_label_style(self, value):
        self._active_axis_label_style = validators.dict(value, allow_empty = True)

    @property
    def active_data_label_style(self) -> Optional[dict]:
        f"""Additional styles to apply to the data label of a point that has drilldown
        data. By default, it is underlined and blue to invite to interaction.

        Defaults to:

        .. code-block:: python

          {constants.DEFAULT_DRILLDOWN_ACTIVE_DATA_LABEL_STYLE}

        In styled mode, active label styles can be set with the
        ``.highcharts-drilldown-data-label`` class.

        :rtype: :class:`dict <python:dict>`
        """
        return self._active_data_label_style

    @active_data_label_style.setter
    def active_data_label_style(self, value):
        self._value = validators.dict(value, allow_empty = True)

    @property
    def allow_point_drilldown(self) -> bool:
        """If ``False``, clicking a single point will drill down all points in the same
        category, equivalent to clicking the X axis label. If ``True``, clicking a single
        point will drill down on that specific point.

        Defaults to ``True``.

        :returns: Flag which determines whether to enable or disable point drilldown.
        :rtype: :class:`bool <python:bool>`
        """
        return self._allow_point_drilldown

    @allow_point_drilldown.setter
    def allow_point_drilldown(self, value):
        self._allow_point_drilldown = bool(value)

    @property
    def animation(self) -> Optional[bool | AnimationOptions]:
        """Configures the animation for all drilldown. Animation of a drilldown occurs
        when drilling between a column point and a column series, or a pie slice and a
        full pie series. Drilldown can still be used between series and points of
        different types, but animation will not occur.

        The animation can be configured as either a boolean or a :class:`AnimationOptions`
        object. If ``True``, it will apply the ``'swing'`` jQuery easing and a duration of
        500 ms by default. If used as a :class:`AnimationOptions` instance, you have more
        fine-grianed configuration control.

        :returns: Settings for the animation of image patterns.
        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if value is None:
            self._animation = None
        elif value is False:
            self._animation = False
        elif value is True:
            self._animation = True
        else:
            self._animation = validate_types(value,
                                             types = AnimationOptions)

    @property
    def breadcrumbs(self) -> Optional[BreadcrumbOptions]:
        """Configuration for the breadcrumbs, the navigation at the top leading the way
        up through the drilldown levels.

        :rtype: :class:`BreadcrumbOptions` or :obj:`None <python:None>`
        """
        return self._breadcrumbs

    @breadcrumbs.setter
    @class_sensitive(BreadcrumbOptions)
    def breadcrumbs(self, value):
        self._breadcrumbs = value

    @property
    def series(self) -> Optional[List[Series]]:
        """An array of series configurations for the drilldown. These drilldown series are
        hidden by default. The drilldown series is linked to the parent series' point by
        its id.

        :rtype: :class:`list <python:list>` of :class:`Series`
        """
        return self._series

    @series.setter
    @class_sensitive(Series, force_iterable = True)
    def series(self, value):
        self._series = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'active_axis_label_style': as_dict.pop('activeAxisLabelStyle',
                                                   constants.DEFAULT_DRILLDOWN_ACTIVE_AXIS_LABEL_STYLE),
            'active_data_label_style': as_dict.pop('activeDataLabelStyle',
                                                   constants.DEFAULT_DRILLDOWN_ACTIVE_DATA_LABEL_STYLE),
            'allow_point_drilldown': as_dict.pop('allowPointDrilldown', True),
            'animation': as_dict.pop('animation', None),
            'breadcrumbs': as_dict.pop('breadcrumbs', None),
            'series': as_dict.pop('series', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'activeAxisLabelStyle': self.active_axis_label_style,
            'activeDataLabelStyle': self.active_data_label_style,
            'allowPointDrilldown': self.allowPointDrilldown,
            'animation': self.animation,
            'breadcrumbs': self.breadcrumbs,
            'series': self.series
        }

        return self.trim_dict(untrimmed)
