from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class ZoomLanguageOptions(HighchartsMeta):
    """Chart and map zoom accessibility language options."""

    def __init__(self, **kwargs):
        self._map_zoom_in = None
        self._map_zoom_out = None
        self._reset_zoom_button = None

        self.map_zoom_in = kwargs.get('map_zoom_in', None)
        self.map_zoom_out = kwargs.get('map_zoom_out', None)
        self.reset_zoom_button = kwargs.get('reset_zoom_button', None)

    @property
    def map_zoom_in(self) -> Optional[str]:
        """Defaults to
        ``'Zoom chart'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map_zoom_in

    @map_zoom_in.setter
    def map_zoom_in(self, value):
        self._map_zoom_in = validators.string(value, allow_empty = True)

    @property
    def map_zoom_out(self) -> Optional[str]:
        """Defaults to
        ``'Zoom out chart'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map_zoom_out

    @map_zoom_out.setter
    def map_zoom_out(self, value):
        self._map_zoom_out = validators.string(value, allow_empty = True)

    @property
    def reset_zoom_button(self) -> Optional[str]:
        """Defaults to
        ``'Reset zoom'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._reset_zoom_button

    @reset_zoom_button.setter
    def reset_zoom_button(self, value):
        self._reset_zoom_button = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'map_zoom_in': as_dict.get('mapZoomIn', None),
            'map_zoom_out': as_dict.get('mapZoomOut', None),
            'reset_zoom_button': as_dict.get('resetZoomButton', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'mapZoomIn': self.map_zoom_in,
            'mapZoomOut': self.map_zoom_out,
            'resetZoomButton': self.reset_zoom_button
        }

        return untrimmed
