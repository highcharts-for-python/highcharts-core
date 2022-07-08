from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class RangeSelectorLanguageOptions(HighchartsMeta):
    """Language options for range selectors when used in accessibility mode."""

    def __init__(self, **kwargs):
        self._click_button_announcement = None
        self._dropdown_label = None
        self._max_input_label = None
        self._min_input_label = None

        self.click_button_announcement = kwargs.pop('click_button_announcement',
                                                    constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_CLICK_BTN_ANNOUNCEMENT)
        self.dropdown_label = kwargs.pop('dropdown_label',
                                         constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_DROPDOWN_LBL)
        self.max_input_label = kwargs.pop('max_input_label',
                                          constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MAX_INPUT_LBL)
        self.min_input_label = kwargs.pop('min_input_label',
                                          constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MIN_INPUT_LBL)

    @property
    def click_button_announcement(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_CLICK_BTN_ANNOUNCEMENT}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._click_button_announcement

    @click_button_announcement.setter
    def click_button_announcement(self, value):
        if value == '':
            self._click_button_announcement = ''
        else:
            self._click_button_announcement = validators.string(value, allow_empty = True) \
                or constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_CLICK_BTN_ANNOUNCEMENT

    @property
    def dropdown_label(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_DROPDOWN_LBL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._dropdown_label

    @dropdown_label.setter
    def dropdown_label(self, value):
        if value == '':
            self._dropdown_label = ''
        else:
            self._dropdown_label = validators.string(value, allow_empty = True) \
                or constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_DROPDOWN_LBL

    @property
    def max_input_label(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MAX_INPUT_LBL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._max_input_label

    @max_input_label.setter
    def max_input_label(self, value):
        if value == '':
            self._max_input_label = ''
        else:
            self._max_input_label = validators.string(value, allow_empty = True) \
                or constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MAX_INPUT_LBL

    @property
    def min_input_label(self) -> str:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MIN_INPUT_LBL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._min_input_label

    @min_input_label.setter
    def min_input_label(self, value):
        if value == '':
            self._min_input_label = ''
        else:
            self._min_input_label = validators.string(value, allow_empty = True) \
                or constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MIN_INPUT_LBL

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'click_button_announcement': as_dict.pop('clickButtonAnnouncement',
                                                     constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_CLICK_BTN_ANNOUNCEMENT),
            'dropdown_label': as_dict.pop('dropdownLabel',
                                          constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_DROPDOWN_LBL),
            'max_input_label': as_dict.pop('maxInputLabel',
                                           constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MAX_INPUT_LBL),
            'min_input_label': as_dict.pop('minInputLabel',
                                           constants.DEFAULT_LANG_ACS_RANGE_SELECTOR_MIN_INPUT_LBL)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'clickButtonAnnouncement': self.click_button_announcement,
            'dropdownLabel': self.dropdown_label,
            'maxInputLabel': self.max_input_label,
            'minInputLabel': self.min_input_label
        }

        return self.trim_dict(untrimmed)
