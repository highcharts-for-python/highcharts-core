from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class SonificationLanguageOptions(HighchartsMeta):
    """Language options for the sonification functionality when used in accessibility
    mode."""

    def __init__(self, **kwargs):
        self._play_as_sound_button_text = None
        self._play_as_sound_click_announcement = None

        self.play_as_sound_button_text = kwargs.pop('play_as_sound_button_text', None)
        self.play_as_sound_click_announcement = kwargs.pop(
            'play_as_sound_click_announcement',
            None
        )

    @property
    def play_as_sound_button_text(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_BTN_TXT}'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._play_as_sound_button_text

    @play_as_sound_button_text.setter
    def play_as_sound_button_text(self, value):
        self._play_as_sound_button_text = validators.string(value, allow_empty = True)

    @property
    def play_as_sound_click_announcement(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_CLK_ANNOUNCEMENT}'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._play_as_sound_click_announcement

    @play_as_sound_click_announcement.setter
    def play_as_sound_click_announcement(self, value):
        self._play_as_sound_click_announcement = validators.string(value,
                                                                   allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'play_as_sound_button_text': as_dict.pop('playAsSoundButtonText', None),
            'play_as_sound_click_announcement': as_dict.pop(
                'playAsSoundClickAnnouncement',
                None
            ),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'playAsSoundButtonText': self.play_as_sound_button_text,
            'playAsSoundClickAnnouncement': self.play_as_sound_click_announcement
        }

        return untrimmed
