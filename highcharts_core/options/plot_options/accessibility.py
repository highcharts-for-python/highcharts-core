from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.accessibility.point import AccessibilityPoint


class SeriesKeyboardNavigation(HighchartsMeta):
    """Keyboard navigation support for the series."""

    def __init__(self, **kwargs):
        self._enabled = None

        self.enabled = kwargs.get('enabled', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.series.accessibility.keyboardNavigation'

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enable accessibility functionality for the series.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled
        }

        return untrimmed


class TypeOptionsAccessibility(HighchartsMeta):
    """Accessibility options for a series."""

    def __init__(self, **kwargs):
        self._description = None
        self._description_format = None
        self._enabled = None
        self._expose_as_group_only = None
        self._keyboard_navigation = None
        self._point = None

        self.description = kwargs.get('description', None)
        self.description_format = kwargs.get('description_format', None)
        self.enabled = kwargs.get('enabled', None)
        self.expose_as_group_only = kwargs.get('expose_as_group_only', None)
        self.keyboard_navigation = kwargs.get('keyboard_navigation', None)
        self.point = kwargs.get('point', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.series.accessibility'

    @property
    def description(self) -> Optional[str]:
        """Provide a description of the series, announced to screen readers.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def description_format(self) -> Optional[str]:
        """Format to use for describing the data series group to assistive technology -
        including screen readers.

        Defaults to ``'{seriesDescription}{authorDescription}{axisDescription}'``.

        The series context and its subproperties are available under the variable
        ``{{series}}``, for example ``{{series.name}}`` for the series name, and
        ``{{series.points.length}}`` for the number of data points.

        The chart context and its subproperties are available under the variable
        ``{{chart}}``, for example ``{{chart.series.length}}`` for the number of series in
        the chart.

        ``{{seriesDescription}}`` refers to the automatic description of the series type
        and number of points added by Highcharts by default.

        ``{{authorDescription}}`` refers to the description added in
        ``series.description`` if one is present.

        ``{{axisDescription}}`` refers to the description added if the chart has multiple
        X or Y axes.

        :returns: Format string that applies to the description produced for the data
          series.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_format

    @description_format.setter
    def description_format(self, value):
        self._description_format = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enable accessibility functionality for the series.

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
    def expose_as_group_only(self) -> Optional[bool]:
        """If ``True``, expose only the series element to screen readers, not its points.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._expose_as_group_only

    @expose_as_group_only.setter
    def expose_as_group_only(self, value):
        if value is None:
            self._expose_as_group_only = None
        else:
            self._expose_as_group_only = bool(value)

    @property
    def keyboard_navigation(self) -> Optional[SeriesKeyboardNavigation]:
        """Keyboard navigation support for the series.

        :rtype: :class:`SeriesKeyboardNavigation` or :obj:`None <python:None>`
        """
        return self._keyboard_navigation

    @keyboard_navigation.setter
    @class_sensitive(SeriesKeyboardNavigation)
    def keyboard_navigation(self, value):
        self._keyboard_navigation = value

    @property
    def point(self) -> Optional[AccessibilityPoint]:
        """Point accessibility options for the series.

        :rtype: :class:`SeriesPoint` or :obj:`None <python:None>`
        """
        return self._point

    @point.setter
    @class_sensitive(AccessibilityPoint)
    def point(self, value):
        self._point = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.get('description', None),
            'description_format': as_dict.get('description_format', None),
            'enabled': as_dict.get('enabled', None),
            'expose_as_group_only': as_dict.get('exposeAsGroupOnly', None),
            'keyboard_navigation': as_dict.get('keyboardNavigation', None),
            'point': as_dict.get('point', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'description': self.description,
            'descriptionFormat': self.description_format,
            'enabled': self.enabled,
            'exposeAsGroupOnly': self.expose_as_group_only,
            'keyboardNavigation': self.keyboard_navigation,
            'point': self.point
        }

        return untrimmed
