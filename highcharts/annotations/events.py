from typing import Optional

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class AnnotationEvent(HighchartsMeta):
    """JavaScript callback functions that fire in response to annotation-related
    events."""

    def __init__(self, **kwargs):
        self._add = None
        self._after_update = None
        self._click = None
        self._remove = None

        self.add = kwargs.pop('add', None)
        self.after_update = kwargs.pop('after_update', None)
        self.click = kwargs.pop('click', None)
        self.remove = kwargs.pop('remove', None)

    @property
    def add(self) -> Optional[str]:
        """JavaScript callback function called when an annotation is added to a chart.

        :returns: JavaScript callback function.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._add

    @add.setter
    def add(self, value):
        self._add = validators.string(value, allow_empty = True)

    @property
    def after_update(self) -> Optional[str]:
        """JavaScript callback function called when an annotation is updated (e.g. drag
        and dropped or resized by control points).

        :returns: JavaScript callback function.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._after_update

    @after_update.setter
    def after_update(self, value):
        self._after_update = validators.string(value, allow_empty = True)

    @property
    def click(self) -> Optional[str]:
        """JavaScript callback function called when an annotation is clicked.

        :returns: JavaScript callback function.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    def click(self, value):
        self._click = validators.string(value, allow_empty = True)

    @property
    def remove(self) -> Optional[str]:
        """JavaScript callback function called when an annotation is removed from the
        chart.

        :returns: JavaScript callback function.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._remove

    @remove.setter
    def remove(self, value):
        self._remove = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'add': as_dict.pop('add', None),
            'after_update': as_dict.pop('afterUpdate', None),
            'click': as_dict.pop('click', None),
            'remove': as_dict.pop('remove', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'add': self.add,
            'afterUpdate': self.after_update,
            'click': self.click,
            'remove': self.remove
        }

        as_dict = self.trim_dict(untrimmed)

        return as_dict
