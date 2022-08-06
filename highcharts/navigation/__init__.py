from typing import Optional

from validator_collection import validators

from highchart import constants
from highchart.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.annotations import Annotation
from highcharts.navigation.bindings import Bindings
from highcharts.utility_classes.breadcrumbs import Breadcrumbs
from highcharts.utility_classes.buttons import ButtonConfiguration
from highcharts.utility_classes.events import NavigationEvents


class Navigation(HighchartsMeta):
    """A collection of options for buttons and menus appearing in the exporting
    module or in Stock Tools.
    """

    def __init__(self, **kwargs):
        self._annotation_options = None
        self._bindings = None
        self._bindings_class_name = None
        self._breadcrumbs = None
        self._button_options = None
        self._events = None
        self._icons_url = None

        self.annotation_options = kwargs.pop('annotation_options', None)
        self.bindings = kwargs.pop('bindings', None)
        self.bindings_class_name = kwargs.pop('bindings_class_name', None)
        self.breadcrumbs = kwargs.pop('breadcrumbs', None)
        self.button_options = kwargs.pop('button_options', None)
        self.events = kwargs.pop('events', None)
        self.icons_url = kwargs.pop('icons_url', None)

    @property
    def annotation_options(self) -> Optional[Annotation]:
        """Additional options to be applied to all annotations.

        :rtype: :class:`NavigationAnnotationOptions` or :obj:`None <python:None>`
        """
        return self._annotation_options

    @annotation_options.setter
    @class_sensitive(Annotation)
    def annotation_options(self, value):
        self._annotation_options = value

    @property
    def bindings(self) -> Optional[Bindings]:
        """JavaScript event bindings for custom HTML buttons.

        :rtype: :class:`Bindings` or :obj:`None <python:None>`
        """
        return self._bindings

    @bindings.setter
    @class_sensitive(Bindings)
    def bindings(self, value):
        self._bindings = value

    @property
    def bindings_class_name(self) -> Optional[str]:
        f"""A CSS class name where all bindings will be attached to. Defaults to
        ``'{constants.DEFAULT_NAVIGATION.get('bindings_class_name')}'``.

        .. hint::

          Multiple charts on the same page should have separate class names to prevent
          duplicating events.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bindings_class_name

    @bindings_class_name.setter
    def bindings_class_name(self, value):
        self._bindings_class_name = validators.string(value, allow_empty = True)

    @property
    def breadcrumbs(self) -> Optional[Breadcrumbs]:
        """Options for breadcrumbs.

        .. note::

          Breadcrumbs general options are defined in :meth:`Navigation.breadcrumbs`.

          Specific options for drilldown are set in `:meth:Drilldown.breadcrumbs` and for
          tree-like series traversing, in
          :meth:`PlotOptions[series].breadbrumbs <Series.breadcrumbs>`.

        :rtype: :class:`Breadcrumbs` or :obj:`None <python:None>`
        """
        return self._breadcrumbs

    @breadcrumbs.setter
    @class_sensitive(Breadcrumbs)
    def breadcrumbs(self, value):
        self._breadcrumbs = value

    @property
    def button_options(self) -> Optional[ButtonConfiguration]:
        """Configuration options for navigation buttons.

        :rtype: :class:`ButtonOptions`
        """
        return self._button_options

    @button_options.setter
    @class_sensitive(ButtonConfiguration)
    def button_options(self, value):
        self._button_options = value

    @property
    def events(self) -> Optional[NavigationEvents]:
        """Events to communicate between Stock Tools and custom GUI.

        :rtype: :class:`NavigationEvents` or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(NavigationEvents)
    def events(self, value):
        self._events = value

    @property
    def icons_url(self) -> Optional[str]:
        f"""Path where Highcharts will look for icons. Defaults to
        ``'{constants.DEFAULT_NAVIGATION.get('icons_url')}'``.

        Change this to use icons from a different server.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._icons_url

    @icons_url.setter
    def icons_url(self, value):
        self._icons_url = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'annotation_options': as_dict.pop('annotationOptions', None),
            'bindings': as_dict.pop('bindings', None),
            'bindings_class_name': as_dict.pop('bindingsClassName', None),
            'breadcrumbs': as_dict.pop('breadcrumbs', None),
            'button_options': as_dict.pop('buttonOptions', None),
            'events': as_dict.pop('events', None),
            'icons_url': as_dict.pop('iconsURL', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'annotationOptions': self.annotation_options,
            'bindings': self.bindings,
            'bindingsClassName': self.bindings_class_name,
            'breadcrumbs': self.breadcrumbs,
            'buttonOptions': self.button_options,
            'events': self.events,
            'iconsURL': self.icons_url
        }

        return untrimmed
