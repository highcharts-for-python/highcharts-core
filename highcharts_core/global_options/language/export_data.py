from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class ExportDataLanguageOptions(HighchartsMeta):
    """Language strings used in the exported data table."""

    def __init__(self, **kwargs):
        self._annotation_header = None
        self._category_datetime_header = None
        self._category_header = None

        self.annotation_header = kwargs.get('annotation_header', None)
        self.category_datetime_header = kwargs.get('category_datetime_header', None)
        self.category_header = kwargs.get('category_header', None)

    @property
    def annotation_header(self) -> Optional[str]:
        """The annotation column title. Defaults to
        ``'Annotations'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._annotation_header

    @annotation_header.setter
    def annotation_header(self, value):
        self._annotation_header = validators.string(value, allow_empty = True)

    @property
    def category_datetime_header(self) -> Optional[str]:
        """The category column title when axis type set to "datetime". Defaults to
        ``'DateTime'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._category_datetime_header

    @category_datetime_header.setter
    def category_datetime_header(self, value):
        self._category_datetime_header = validators.string(value, allow_empty = True)

    @property
    def category_header(self) -> Optional[str]:
        """The category column title. Defaults to
        ``'Category'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._category_header

    @category_header.setter
    def category_header(self, value):
        self._category_header = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'annotation_header': as_dict.get('annotationHeader', None),
            'category_datetime_header': as_dict.get('categoryDatetimeHeader', None),
            'category_header': as_dict.get('categoryHeader', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'annotationHeader': self.annotation_header,
            'categoryDatetimeHeader': self.category_datetime_header,
            'categoryHeader': self.category_header
        }

        return untrimmed
