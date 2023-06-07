from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class AnnotationControlPointOption(HighchartsMeta):
    """Options for annotation's control points."""

    def __init__(self, **kwargs):
        self._positioner = None

        self.positioner = kwargs.get('positioner', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations.controlPointOptions'

    @property
    def positioner(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function to modify annotation's positioner controls.

        The JavaScript function should receive two arguments, ``this`` being the
        annotation's control point and ``target`` being the annotation's controllable.

        :returns: A JavaScript callback function to modify the annotation's positioner
          controls.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._positioner

    @positioner.setter
    @class_sensitive(CallbackFunction)
    def positioner(self, value):
        self._positioner = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'positioner': as_dict.get('positioner', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'positioner': self.positioner
        }

        return untrimmed
