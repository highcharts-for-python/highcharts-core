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

        self.play_as_sound_button_text = kwargs.pop('play_as_sound_button_text',
                                                    constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_BTN_TXT)
        self.play_as_sound_click_announcement = kwargs.pop('play_as_sound_click_announcement',
                                                           constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_CLK_ANNOUNCEMENT)

    @property
    def play_as_sound_button_text(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_BTN_TXT}'``

        :rtype: :class:`str <python:str>`
        """
        return self._play_as_sound_button_text

    @play_as_sound_button_text.setter
    def play_as_sound_button_text(self, value):
        if value == '':
            self._play_as_sound_button_text = ''
        else:
            self._play_as_sound_button_text = validators.string(value, allow_empty = True)\
                or constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_BTN_TXT

    @property
    def play_as_sound_click_announcement(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_CLK_ANNOUNCEMENT}'``

        :rtype: :class:`str <python:str>`
        """
        return self._play_as_sound_click_announcement

    @play_as_sound_click_announcement.setter
    def play_as_sound_click_announcement(self, value):
        if value == '':
            self._play_as_sound_click_announcement = ''
        else:
            self._play_as_sound_click_announcement = validators.string(value, allow_empty = True)\
                or constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_CLK_ANNOUNCEMENT

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'play_as_sound_button_text': as_dict.pop('playAsSoundButtonText',
                                                        constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_BTN_TXT),
            'play_as_sound_click_announcement': as_dict.pop('playAsSoundClickAnnouncement',
                                                               constants.DEFAULT_LANG_ACS_SONIFICATION_PLAY_AS_SOUND_CLK_ANNOUNCEMENT)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'playAsSoundButtonText': self.play_as_sound_button_text,
            'playAsSoundClickAnnouncement': self.play_as_sound_click_announcement
        }

        return self.trim_dict(untrimmed)
