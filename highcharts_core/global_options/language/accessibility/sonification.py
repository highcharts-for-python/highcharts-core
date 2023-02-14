from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class SonificationLanguageOptions(HighchartsMeta):
    """Language options for the sonification functionality when used in accessibility
    mode."""

    def __init__(self, **kwargs):
        self._play_as_sound_button_text = None
        self._play_as_sound_click_announcement = None

        self.play_as_sound_button_text = kwargs.get('play_as_sound_button_text', None)
        self.play_as_sound_click_announcement = kwargs.get(
            'play_as_sound_click_announcement',
            None
        )

    @property
    def play_as_sound_button_text(self) -> Optional[str]:
        """Defaults to
        ``'Play as sound, {chartTitle}'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._play_as_sound_button_text

    @play_as_sound_button_text.setter
    def play_as_sound_button_text(self, value):
        self._play_as_sound_button_text = validators.string(value, allow_empty = True)

    @property
    def play_as_sound_click_announcement(self) -> Optional[str]:
        """Defaults to
        ``'Play'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._play_as_sound_click_announcement

    @play_as_sound_click_announcement.setter
    def play_as_sound_click_announcement(self, value):
        self._play_as_sound_click_announcement = validators.string(value,
                                                                   allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'play_as_sound_button_text': as_dict.get('playAsSoundButtonText', None),
            'play_as_sound_click_announcement': as_dict.get(
                'playAsSoundClickAnnouncement',
                None
            ),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'playAsSoundButtonText': self.play_as_sound_button_text,
            'playAsSoundClickAnnouncement': self.play_as_sound_click_announcement
        }

        return untrimmed
