from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class AnnotationEvent(HighchartsMeta):
    """JavaScript callback functions that fire in response to annotation-related
    events."""

    def __init__(self, **kwargs):
        self._add = None
        self._after_update = None
        self._click = None
        self._remove = None

        self.add = kwargs.get('add', None)
        self.after_update = kwargs.get('after_update', None)
        self.click = kwargs.get('click', None)
        self.remove = kwargs.get('remove', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations.events'

    @property
    def add(self) -> Optional[CallbackFunction]:
        """JavaScript callback function called when an annotation is added to a chart.

        :returns: JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._add

    @add.setter
    @class_sensitive(CallbackFunction)
    def add(self, value):
        self._add = value

    @property
    def after_update(self) -> Optional[CallbackFunction]:
        """JavaScript callback function called when an annotation is updated (e.g. drag
        and dropped or resized by control points).

        :returns: JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._after_update

    @after_update.setter
    @class_sensitive(CallbackFunction)
    def after_update(self, value):
        self._after_update = value

    @property
    def click(self) -> Optional[CallbackFunction]:
        """JavaScript callback function called when an annotation is clicked.

        :returns: JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    @class_sensitive(CallbackFunction)
    def click(self, value):
        self._click = value

    @property
    def remove(self) -> Optional[CallbackFunction]:
        """JavaScript callback function called when an annotation is removed from the
        chart.

        :returns: JavaScript callback function.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._remove

    @remove.setter
    @class_sensitive(CallbackFunction)
    def remove(self, value):
        self._remove = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'add': as_dict.get('add', None),
            'after_update': as_dict.get('afterUpdate', None),
            'click': as_dict.get('click', None),
            'remove': as_dict.get('remove', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'add': self.add,
            'afterUpdate': self.after_update,
            'click': self.click,
            'remove': self.remove
        }

        return untrimmed
