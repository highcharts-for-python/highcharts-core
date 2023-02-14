from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class RangeSelectorLanguageOptions(HighchartsMeta):
    """Language options for range selectors when used in accessibility mode."""

    def __init__(self, **kwargs):
        self._click_button_announcement = None
        self._dropdown_label = None
        self._max_input_label = None
        self._min_input_label = None

        self.click_button_announcement = kwargs.get('click_button_announcement', None)
        self.dropdown_label = kwargs.get('dropdown_label', None)
        self.max_input_label = kwargs.get('max_input_label', None)
        self.min_input_label = kwargs.get('min_input_label', None)

    @property
    def click_button_announcement(self) -> Optional[str]:
        """Defaults to
        ``'Viewing {axisRangeDescription}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._click_button_announcement

    @click_button_announcement.setter
    def click_button_announcement(self, value):
        self._click_button_announcement = validators.string(value, allow_empty = True)

    @property
    def dropdown_label(self) -> Optional[str]:
        """Defaults to
        ``'{rangeTitle}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dropdown_label

    @dropdown_label.setter
    def dropdown_label(self, value):
        self._dropdown_label = validators.string(value, allow_empty = True)

    @property
    def max_input_label(self) -> Optional[str]:
        """Defaults to
        ``'Select end date.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._max_input_label

    @max_input_label.setter
    def max_input_label(self, value):
        self._max_input_label = validators.string(value, allow_empty = True)

    @property
    def min_input_label(self) -> Optional[str]:
        """Defaults to
        ``'Select start date.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._min_input_label

    @min_input_label.setter
    def min_input_label(self, value):
        self._min_input_label = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'click_button_announcement': as_dict.get('clickButtonAnnouncement', None),
            'dropdown_label': as_dict.get('dropdownLabel', None),
            'max_input_label': as_dict.get('maxInputLabel', None),
            'min_input_label': as_dict.get('minInputLabel', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'clickButtonAnnouncement': self.click_button_announcement,
            'dropdownLabel': self.dropdown_label,
            'maxInputLabel': self.max_input_label,
            'minInputLabel': self.min_input_label
        }

        return untrimmed
