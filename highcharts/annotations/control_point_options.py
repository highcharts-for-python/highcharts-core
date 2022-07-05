from typing import Optional

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class AnnotationControlPointOption(HighchartsMeta):
    """Options for annotation's control points."""

    def __init__(self, **kwargs):
        self._positioner = None

        self.positioner = kwargs.pop('positioner', None)

    @property
    def positioner(self) -> Optional[str]:
        """A JavaScript callback function to modify annotation's positioner controls.

        The JavaScript function should receive two arguments, ``this`` being the
        annotation's control point and ``target`` being the annotation's controllable.

        :returns: A JavaScript callback function to modify the annotation's positioner
          controls.
        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._positioner

    @positioner.setter
    def positioner(self, value):
        self._positioner = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'positioner': as_dict.pop('positioner', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'positioner': self.positioner
        }
        as_dict = self.trim_dict(untrimmed)

        return as_dict
