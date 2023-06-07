from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.annotations import Annotation
from highcharts_core.options.navigation.bindings import Bindings
from highcharts_core.utility_classes.breadcrumbs import BreadcrumbOptions
from highcharts_core.utility_classes.buttons import ButtonConfiguration
from highcharts_core.utility_classes.events import NavigationEvents


class NavigationBase(HighchartsMeta):
    """A collection of options for buttons and menus appearing in the exporting
    module or in Stock Tools.
    """

    def __init__(self, **kwargs):
        self._annotation_options = None
        self._bindings = None
        self._bindings_class_name = None
        self._button_options = None
        self._events = None
        self._icons_url = None

        self.annotation_options = kwargs.get('annotation_options', None)
        self.bindings = kwargs.get('bindings', None)
        self.bindings_class_name = kwargs.get('bindings_class_name', None)
        self.button_options = kwargs.get('button_options', None)
        self.events = kwargs.get('events', None)
        self.icons_url = kwargs.get('icons_url', None)

        super().__init__(**kwargs)

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
        """A CSS class name where all bindings will be attached to. Defaults to
        ``'highcharts-bindings-container'``.

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
        """Path where Highcharts will look for icons. Defaults to
        ``'https://code.highcharts.com/@product.version@/gfx/stock-icons/'``.

        Change this to use icons from a different server.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._icons_url

    @icons_url.setter
    def icons_url(self, value):
        self._icons_url = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'annotation_options': as_dict.get('annotationOptions', None),
            'bindings': as_dict.get('bindings', None),
            'bindings_class_name': as_dict.get('bindingsClassName', None),
            'button_options': as_dict.get('buttonOptions', None),
            'events': as_dict.get('events', None),
            'icons_url': as_dict.get('iconsURL', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'annotationOptions': self.annotation_options,
            'bindings': self.bindings,
            'bindingsClassName': self.bindings_class_name,
            'buttonOptions': self.button_options,
            'events': self.events,
            'iconsURL': self.icons_url
        }

        return untrimmed


class Navigation(NavigationBase):
    """A collection of options for buttons and menus appearing in the exporting
    module or in Stock Tools.
    """

    def __init__(self, **kwargs):
        self._breadcrumbs = None

        self.breadcrumbs = kwargs.get('breadcrumbs', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'navigation'

    @property
    def breadcrumbs(self) -> Optional[BreadcrumbOptions]:
        """Options for breadcrumbs.

        .. note::

          Breadcrumbs general options are defined in :meth:`Navigation.breadcrumbs`.

          Specific options for drilldown are set in `:meth:Drilldown.breadcrumbs` and for
          tree-like series traversing, in
          :meth:`PlotOptions[series].breadbrumbs <Series.breadcrumbs>`.

        :rtype: :class:`BreadcrumbOptions` or :obj:`None <python:None>`
        """
        return self._breadcrumbs

    @breadcrumbs.setter
    @class_sensitive(BreadcrumbOptions)
    def breadcrumbs(self, value):
        self._breadcrumbs = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'annotation_options': as_dict.get('annotationOptions', None),
            'bindings': as_dict.get('bindings', None),
            'bindings_class_name': as_dict.get('bindingsClassName', None),
            'button_options': as_dict.get('buttonOptions', None),
            'events': as_dict.get('events', None),
            'icons_url': as_dict.get('iconsURL', None),

            'breadcrumbs': as_dict.get('breadcrumbs', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'breadcrumbs': self.breadcrumbs,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
