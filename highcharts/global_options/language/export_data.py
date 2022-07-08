from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class ExportDataLanguageOptions(HighchartsMeta):
    """Language strings used in the exported data table."""

    def __init__(self, **kwargs):
        self._annotation_header = None
        self._category_datetime_header = None
        self._category_header = None

        self.annotation_header = kwargs.pop('annotation_header',
                                            constants.DEFAULT_LANG_EXPORT_DATA.get('annotation_header'))
        self.category_datetime_header = kwargs.pop('category_datetime_header',
                                                   constants.DEFAULT_LANG_EXPORT_DATA.get('category_datetime_header'))
        self.category_header = kwargs.pop('category_header',
                                          constants.DEFAULT_LANG_EXPORT_DATA.get('category_header'))

    @property
    def annotation_header(self) -> str:
        f"""The annotation column title. Defaults to
        ``'{constants.DEFAULT_LANG_EXPORT_DATA.get('annotation_header')}'.

        :rtype: :class:`str <python:str>`
        """
        return self._annotation_header

    @annotation_header.setter
    def annotation_header(self, value):
        if value == '':
            self._annotation_header = ''
        else:
            self._annotation_header = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_EXPORT_DATA.get('annotation_header')

    @property
    def category_datetime_header(self) -> str:
        f"""The category column title when axis type set to "datetime". Defaults to
        ``'{constants.DEFAULT_LANG_EXPORT_DATA.get('category_datetime_header')}'.

        :rtype: :class:`str <python:str>`
        """
        return self._category_datetime_header

    @category_datetime_header.setter
    def category_datetime_header(self, value):
        if value == '':
            self._category_datetime_header = ''
        else:
            self._category_datetime_header = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_EXPORT_DATA.get('annotations_header')

    @property
    def category_header(self) -> str:
        f"""The category column title. Defaults to
        ``'{constants.DEFAULT_LANG_EXPORT_DATA.get('category_header')}'.

        :rtype: :class:`str <python:str>`
        """
        return self._category_header

    @category_header.setter
    def category_header(self, value):
        if value == '':
            self._category_header = ''
        else:
            self._category_header = validators.string(value, allow_empty = True) or \
                constants.DEFAULT_LANG_EXPORT_DATA.get('annotations_header')

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'annotation_header': as_dict.pop('annotationHeader',
                                             constants.DEFAULT_LANG_EXPORT_DATA.get('annotation_header')),
            'category_datetime_header': as_dict.pop('categoryDatetimeHeader',
                                                    constants.DEFAULT_LANG_EXPORT_DATA.get('category_datetime_header')),
            'category_header': as_dict.pop('categoryHeader',
                                           constants.DEFAULT_LANG_EXPORT_DATA.get('category_header'))
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'annotationHeader': self.annotation_header,
            'categoryDatetimeHeader': self.category_datetime_header,
            'categoryHeader': self.category_header
        }

        return self.trim_dict(untrimmed)
