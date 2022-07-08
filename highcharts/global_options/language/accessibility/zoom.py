from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class ZoomLanguageOptions(HighchartsMeta):
    """Chart and map zoom accessibility language options."""

    def __init__(self, **kwargs):
        self._map_zoom_in = None
        self._map_zoom_out = None
        self._reset_zoom_button = None

        self.map_zoom_in = kwargs.pop('map_zoom_in',
                                      constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_IN)
        self.map_zoom_out = kwargs.pop('map_zoom_out',
                                       constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_OUT)
        self.reset_zoom_button = kwargs.pop('reset_zoom_button',
                                            constants.DEFAULT_LANG_ACS_ZOOM_RESET_ZOOM_BTN)

    @property
    def map_zoom_in(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_IN}'``

        :rtype: :class:`str <python:str>`
        """
        return self._map_zoom_in

    @map_zoom_in.setter
    def map_zoom_in(self, value):
        if value == '':
            self._map_zoom_in = ''
        else:
            self._map_zoom_in = validators.string(value, allow_empty = True) \
                or constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_IN

    @property
    def map_zoom_out(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_OUT}'``

        :rtype: :class:`str <python:str>`
        """
        return self._map_zoom_out

    @map_zoom_out.setter
    def map_zoom_out(self, value):
        if value == '':
            self._map_zoom_out = ''
        else:
            self._map_zoom_out = validators.string(value, allow_empty = True)\
                or constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_OUT

    @property
    def reset_zoom_button(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_ZOOM_RESET_ZOOM_BTN}'``

        :rtype: :class:`str <python:str>`
        """
        return self._reset_zoom_button

    @reset_zoom_button.setter
    def reset_zoom_button(self, value):
        if value == '':
            self._reset_zoom_button = ''
        else:
            self._reset_zoom_button = validators.string(value, allow_empty = True)\
                or constants.DEFAULT_LANG_ACS_ZOOM_RESET_ZOOM_BTN

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'map_zoom_in': as_dict.pop('mapZoomIn',
                                       constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_IN),
            'map_zoom_out': as_dict.pop('mapZoomOut',
                                        constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_OUT),
            'reset_zoom_button': as_dict.pop('resetZoomButton',
                                             constants.DEFAULT_LANG_ACS_ZOOM_RESET_ZOOM_BTN)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'mapZoomIn': self.map_zoom_in,
            'mapZoomOut': self.map_zoom_out,
            'resetZoomButton': self.reset_zoom_button
        }

        return self.trim_dict(untrimmed)
