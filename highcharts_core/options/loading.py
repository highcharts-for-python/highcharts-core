from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class Loading(HighchartsMeta):
    """The loading options control the appearance of the loading screen that covers
    the plot area on chart operations.

    This screen only appears after an explicit call to ``chart.showLoading()`` in the
    browser. It is a utility for developers to communicate to the end user that
    something is going on, for example while retrieving new data via an XHR
    connection.

    .. hint::

      The "Loading..." text itself is **not** part of this configuration object, but
      is instead part of the :meth:`.language <Options.language>` configuration.

    """

    def __init__(self, **kwargs):
        self._hide_duration = None
        self._label_style = None
        self._show_duration = None
        self._style = None

        self.hide_duration = kwargs.get('hide_duration', None)
        self.label_style = kwargs.get('label_style', None)
        self.show_duration = kwargs.get('show_duration', None)
        self.style = kwargs.get('style', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'loading'

    @property
    def hide_duration(self) -> Optional[int]:
        """The duration in milliseconds of the fade out effect. Defaults to
        ``100``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._hide_duration

    @hide_duration.setter
    def hide_duration(self, value):
        self._hide_duration = validators.integer(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def label_style(self) -> Optional[str | dict]:
        """CSS styles applied to the loading label's ``<span>``. Defaults to
        ``'{"fontWeight": "bold", "position": "relative", "top": "45%"}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._label_style

    @label_style.setter
    def label_style(self, value):
        try:
            self._style = validators.dict(value, allow_empty = True)
        except (ValueError, TypeError):
            self._style = validators.string(value, 
                                            allow_empty = True,
                                            coerce_value = True)

    @property
    def show_duration(self) -> Optional[int]:
        """The duration in milliseconds of the fade in effect. Defaults to
        ``100``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._show_duration

    @show_duration.setter
    def show_duration(self, value):
        self._show_duration = validators.integer(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def style(self) -> Optional[str | dict]:
        """CSS styles for the loading screen that covers the plot area. Defaults to
        ``'{"position": "absolute", "backgroundColor": "#ffffff", "opacity": 0.5, "textAlign": "center"}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        try:
            self._style = validators.dict(value, allow_empty = True)
        except (ValueError, TypeError):
            self._style = validators.string(value, 
                                            allow_empty = True,
                                            coerce_value = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'hide_duration': as_dict.get('hideDuration', None),
            'label_style': as_dict.get('labelStyle', None),
            'show_duration': as_dict.get('showDuration', None),
            'style': as_dict.get('style', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'hideDuration': self.hide_duration,
            'labelStyle': self.label_style,
            'showDuration': self.show_duration,
            'style': self.style
        }

        return untrimmed
