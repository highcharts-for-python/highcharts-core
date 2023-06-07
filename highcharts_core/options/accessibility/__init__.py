"""Implements the Python representation of the Accessibility module."""
from typing import Optional, Any
from copy import deepcopy

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta, JavaScriptDict
from highcharts_core.decorators import class_sensitive
from highcharts_core import constants, errors

from highcharts_core.options.accessibility.announce_new_data import AnnounceNewData
from highcharts_core.options.accessibility.high_contrast_theme import HighContrastTheme
from highcharts_core.options.accessibility.keyboard_navigation import KeyboardNavigation
from highcharts_core.options.accessibility.point import AccessibilityPoint
from highcharts_core.options.accessibility.screen_reader_section import ScreenReaderSection
from highcharts_core.options.accessibility.series import SeriesAccessibility


class CustomAccessibilityComponents(JavaScriptDict):
    """JavaScript object which contains a map of component names to instances of classes
    inheriting from the (JavaScript)
    `Highcharts.AccessibilityComponent <https://api.highcharts.com/class-reference/Highcharts.AccessibilityComponent>`_
    base class.

    .. tip::

      Remember to add the component to the :meth:`keyboard_navigation.order`
      for the keyboard navigation to be usable.

    """
    _valid_value_types = str
    _allow_empty_value = True


class Accessibility(HighchartsMeta):
    """Options for configuring accessibility for the chart."""

    def __init__(self, **kwargs):
        self._announce_new_data = None
        self._custom_components = None
        self._description = None
        self._enabled = True
        self._high_contrast_theme = None
        self._keyboard_navigation = None
        self._landmark_verbosity = None
        self._linked_description = None
        self._point = None
        self._screen_reader_section = None
        self._series = None
        self._type_description = None

        self.announce_new_data = kwargs.get('announce_new_data', None)
        self.custom_components = kwargs.get('custom_components', None)
        self.description = kwargs.get('description', None)
        self.enabled = kwargs.get('enabled', None)
        self.high_contrast_theme = kwargs.get('high_contrast_theme', None)
        self.keyboard_navigation = kwargs.get('keyboard_navigation', None)
        self.landmark_verbosity = kwargs.get('landmark_verbosity', None)
        self.linked_description = kwargs.get('linked_description', None)
        self.point = kwargs.get('point', None)
        self.screen_reader_section = kwargs.get('screen_reader_section', None)
        self.series = kwargs.get('series', None)
        self.type_description = kwargs.get('type_description', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'accessibility'

    @property
    def announce_new_data(self) -> Optional[AnnounceNewData]:
        """Options for announcing new data to screen reader users.

        .. tip::

          Useful for dynamic data applications and drilldown.

          Keep in mind that frequent announcements will not be useful to users, as they
          won't have time to explore the new data. For these applications, consider making
          snapshots of the data accessible, and do the announcements in batches.

        :returns: Configuration for the announcement of new data to screen reader users.
        :rtype: :class:`AnnounceNewData` or :obj:`None <python:None>`
        """
        return self._announce_new_data

    @announce_new_data.setter
    @class_sensitive(AnnounceNewData)
    def announce_new_data(self, value):
        self._announce_new_data = value

    @property
    def custom_components(self) -> Optional[CustomAccessibilityComponents]:
        """Property which supports the definition of custom components added to the
        accessibility module. Defaults to :obj:`None <python:None>`.

        .. tip::

          Remember to add the component to the :meth:`keyboard_navigation.order`
          for the keyboard navigation to be usable.

        :returns: Custom components that have been added to the accessibility module.
        :rtype: :class:`CustomAccessibilityComponents` or :obj:`None <python:None>`

        """
        return self._custom_components

    @custom_components.setter
    @class_sensitive(CustomAccessibilityComponents)
    def custom_components(self, value):
        self._custom_components = value

    @property
    def description(self) -> Optional[str]:
        """A text description of the chart.

        If the Accessibility module is loaded, this option is included by default as a
        long description of the chart in the hidden screen reader information region.

        .. warning::

          Prefer using :meth:`Accessibility.linked_description` and
          :meth:`Options.caption` instead.

          Since Highcharts now supports captions and linked descriptions, it is preferred
          to define the description using those methods, as a visible caption/description
          benefits all users. If the ``accessibility.description`` option is defined, the
          linked description is ignored, and the caption is hidden from screen reader
          users.

        :returns: The description of the chart or :obj:`None <python:None>`
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        value = validators.string(value, allow_empty = True)
        self._description = value

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables accessibility functionality for the chart. Defaults to
        ``True``.

        .. seealso::

          For more information on how to include these features, and why this is
          recommended, see
          `Highcharts Accessibility <https://www.highcharts.com/docs/accessibility/accessibility-module>`_

        .. note::

          Highcharts will by default emit a warning to the console if the accessibility
          module is not loaded. Setting this option to false will override and silence the
          warning.

          Once the module is loaded, setting this option to false will disable the module
          for this chart.

        :returns: Flag indicating whether the :class:`Accessibility` module is enabled
          for the chart.
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
    def high_contrast_theme(self) -> Any:
        """Theme to apply to the chart when Windows High Contrast Mode is detected.

        By default, a high contrast theme matching the high contrast system system colors
        is used.

        :returns: Theme to apply to the chart when high contrast mode is detected.
        :rtype: :class:`HighContrastTheme` or :obj:`None <python:None>`
        """
        return self._high_contrast_theme

    @high_contrast_theme.setter
    def high_contrast_theme(self, value):
        self._high_contrast_theme = value

    @property
    def keyboard_navigation(self) -> Optional[KeyboardNavigation]:
        """Options for keyboard navigation.

        :returns: Configuration for keyboard navigation.
        :rtype: :class:`KeyboardNavigation` or :obj:`None <python:None>`
        """
        return self._keyboard_navigation

    @keyboard_navigation.setter
    @class_sensitive(KeyboardNavigation)
    def keyboard_navigation(self, value):
        self._keyboard_navigation = value

    @property
    def landmark_verbosity(self) -> Optional[str]:
        """Amount of landmarks/regions to create for screen reader users.

        More landmarks can make navigation with screen readers easier, but can be
        distracting if there are lots of charts on the page.

        Three modes are available:

          * ``'all'``: Adds regions for all series, legend, information region.
          * ``'one'``: Adds a single landmark per chart.
          * ``'disabled'``: No landmarks are added.

        Defaults to ``'all'``.

        :returns: The landmark verbosity for screen readers to use.
        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._landmark_verbosity

    @landmark_verbosity.setter
    def landmark_verbosity(self, value):
        if not value:
            self._landmark_verbosity = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.LANDMARK_VERBOSITY_VALUES:
                raise errors.HighchartsValueError(f'landmark_verbosity must be "all", '
                                                  f'"one", or "disabled". Was: {value}')
            self._landmark_verbosity = value

    @property
    def linked_description(self) -> Optional[str]:
        """Link the chart to an HTML element describing the contents of the chart.

        .. hint::

          It is always recommended to describe charts using visible text, to improve SEO
          as well as accessibility for users with disabilities.

          This option lets an HTML element with a description be linked to the chart, so
          that screen reader users can connect the two.

        By setting this option to a string, Highcharts runs the string as an HTML selector
        query on the entire document. If there is only a single match, this element is
        linked to the chart. The content of the linked element will be included in the
        chart description for screen reader users.

        By default, the chart looks for an adjacent sibling element with the
        ``highcharts-description`` (CSS) class.

        The feature can be disabled by setting the option to an empty string, or
        overridden by providing the :meth`Accessibility.description` option.
        Alternatively, the HTML element to link can be passed in directly as an HTML node.

        .. hint::

          If you need the description to be part of the exported image, consider using the
          caption feature.

          If you need the description to be hidden visually, use the
          :meth:`Accessibility.description` option.

        Defaults to ``'*[data-highcharts-chart="{index}"] + .highcharts-description'``.

        :returns: The CSS selector used to indicate the HTML element containing a
          description of the chart.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        """
        return self._linked_description

    @linked_description.setter
    def linked_description(self, value):
        self._linked_description = validators.string(value, allow_empty = True)

    @property
    def point(self) -> Optional[AccessibilityPoint]:
        """Options for describing individual points.

        :returns: Configuration for how to describe individual points on the chart.
        :rtype: :class:`AccessibilityPoint` or :obj:`None <python:None>`
        """
        return self._point

    @point.setter
    @class_sensitive(AccessibilityPoint)
    def point(self, value):
        self._point = value

    @property
    def screen_reader_section(self) -> Optional[ScreenReaderSection]:
        """Accessibility options for the screen reader information sections added before
        and after the chart.

        :returns: Configuration for the screen reader sections before and after the chart.
        :rtype: :class:`ScreenReaderSection` or :obj:`None <python:None>`
        """
        return self._screen_reader_section

    @screen_reader_section.setter
    @class_sensitive(ScreenReaderSection)
    def screen_reader_section(self, value):
        self._screen_reader_section = value

    @property
    def series(self) -> Optional[SeriesAccessibility]:
        """Accessibility options global to all data series.

        .. hint::

          Individual series can also have specific accessibility options set.

        :returns: Global accessibility options applied to all data series.
        :rtype: :class:`SeriesAccessibility` or :obj:`None <python:None>`
        """
        return self._series

    @series.setter
    @class_sensitive(SeriesAccessibility)
    def series(self, value):
        self._series = value

    @property
    def type_description(self) -> Optional[str]:
        """A text description of the chart type.

        If the Accessibility module is loaded, this will be included in the description
        of the chart in the screen reader information region.

        .. note::

          Highcharts will by default attempt to guess the chart type, but for more complex
          charts it is recommended to specify this property for clarity.

        :returns: A description fo the chart type.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_description

    @type_description.setter
    def type_description(self, value):
        self._type_description = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'announce_new_data': as_dict.get('announceNewData', None),
            'custom_components': as_dict.get('customComponents', None),
            'description': as_dict.get('description', None),
            'enabled': as_dict.get('enabled', None),
            'high_contrast_theme': as_dict.get('highContrastTheme', None),
            'keyboard_navigation': as_dict.get('keyboardNavigation', None),
            'landmark_verbosity': as_dict.get('landmarkVerbosity', None),
            'linked_description': as_dict.get('linkedDescription', None),
            'point': as_dict.get('point', None),
            'screen_reader_section': as_dict.get('screenReaderSection', None),
            'series': as_dict.get('series', None),
            'type_description': as_dict.get('typeDescription', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'announceNewData': self.announce_new_data,
            'customComponents': self.custom_components,
            'description': self.description,
            'enabled': self.enabled,
            'highContrastTheme': self.high_contrast_theme,
            'keyboardNavigation': self.keyboard_navigation,
            'landmarkVerbosity': self.landmark_verbosity,
            'linkedDescription': self.linked_description,
            'point': self.point,
            'screenReaderSection': self.screen_reader_section,
            'series': self.series,
            'typeDescription': self.type_description
        }

        return untrimmed


__all__ = [
    'Accessibility',
    'AnnounceNewData',
    'HighContrastTheme',
    'KeyboardNavigation',
    'AccessibilityPoint',
    'ScreenReaderSection',
    'SeriesAccessibility'
]
