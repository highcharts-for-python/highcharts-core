from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class ScreenReaderSectionAnnotationLanguage(HighchartsMeta):
    """Language options for annotation descriptions."""

    def __init__(self, **kwargs):
        self._description_multiple_points = None
        self._description_no_points = None
        self._description_single_point = None
        self._heading = None

        self.description_multiple_points = kwargs.pop('description_multiple_points', None)
        self.description_no_points = kwargs.pop('description_no_points', None)
        self.description_single_point = kwargs.pop('description_single_point', None)
        self.heading = kwargs.pop('heading', None)

    @property
    def description_multiple_points(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SRS_ANNOTATION_DESCRIPTION_MULTIPLE_PTS}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._description_multiple_points

    @description_multiple_points.setter
    def description_multiple_points(self, value):
        self._description_multiple_points = validators.string(value, allow_empty = True)

    @property
    def description_no_points(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SRS_ANNOTATION_DESCRIPTION_NO_PTS}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._description_no_points

    @description_no_points.setter
    def description_no_points(self, value):
        self._description_no_points = validators.string(value,
                                                        allow_empty = True)

    @property
    def description_single_point(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SRS_ANNOTATION_DESCRIPTION_SINGLE_PT}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._description_single_point

    @description_single_point.setter
    def description_single_point(self, value):
        self._description_single_point = validators.string(value, allow_empty = True)

    @property
    def heading(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_SRS_ANNOTATION_HEADING}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'description_multiple_points': as_dict.pop('descriptionMultiplePoints', None),
            'description_no_points': as_dict.pop('descriptionNoPoints', None),
            'description_single_point': as_dict.pop('descriptionSinglePoint', None),
            'heading': as_dict.pop('heading', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'descriptionMultiplePoints': self.description_multiple_points,
            'descriptionNoPoints': self.description_no_points,
            'descriptionSinglePoint': self.description_single_point,
            'heading': self.heading
        }

        return untrimmed


class ScreenReaderSectionLanguageOptions(HighchartsMeta):
    """Language options for the screen reader information sections added before and
    after the chart when used in accessibility mode."""

    def __init__(self, **kwargs):
        self._after_region_label = None
        self._annotations = None
        self._before_region_label = None
        self._end_of_chart_marker = None

        self.after_region_label = kwargs.pop('after_region_label', None)
        self.annotations = kwargs.pop('annotations', None)
        self.before_region_label = kwargs.pop('before_region_label', None)
        self.end_of_chart_marker = kwargs.pop('end_of_chart_marker', None)

    @property
    def after_region_label(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SRS_AFTER_REGION_LBL}'`` (empty
        string).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._after_region_label

    @after_region_label.setter
    def after_region_label(self, value):
        self._after_region_label = validators.string(value, allow_empty = True)

    @property
    def annotations(self) -> Optional[ScreenReaderSectionAnnotationLanguage]:
        """Language options for annotation descriptions.

        :rtype: :class:`ScreenReaderSectionAnnotationLanguage` or
          :obj:`None <python:None>`
        """
        return self._annotations

    @annotations.setter
    @class_sensitive(ScreenReaderSectionAnnotationLanguage)
    def annotations(self, value):
        self._annotations = value

    @property
    def before_region_label(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SRS_BEFORE_REGION_LBL}'`` (empty
        string).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._before_region_label

    @before_region_label.setter
    def before_region_label(self, value):
        self._before_region_label = validators.string(value, allow_empty = True)

    @property
    def end_of_chart_marker(self) -> Optional[str]:
        f"""Defaults to ``'{constants.DEFAULT_LANG_ACS_SRS_END_OF_CHART_MRKR}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._end_of_chart_marker

    @end_of_chart_marker.setter
    def end_of_chart_marker(self, value):
        self._end_of_chart_marker = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'after_region_label': as_dict.pop('afterRegionLabel', None),
            'annotations': as_dict.pop('annotations', None),
            'before_region_label': as_dict.pop('beforeRegionLabel', None),
            'end_of_chart_marker': as_dict.pop('endOfChartMarker', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'afterRegionLabel': self.after_region_label,
            'annotations': self.annotations,
            'beforeRegionLabel': self.before_region_label,
            'endOfChartMarker': self.end_of_chart_marker
        }

        return untrimmed
