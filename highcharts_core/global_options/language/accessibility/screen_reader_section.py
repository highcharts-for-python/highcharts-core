from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class ScreenReaderSectionAnnotationLanguage(HighchartsMeta):
    """Language options for annotation descriptions."""

    def __init__(self, **kwargs):
        self._description_multiple_points = None
        self._description_no_points = None
        self._description_single_point = None
        self._heading = None

        self.description_multiple_points = kwargs.get('description_multiple_points', None)
        self.description_no_points = kwargs.get('description_no_points', None)
        self.description_single_point = kwargs.get('description_single_point', None)
        self.heading = kwargs.get('heading', None)

    @property
    def description_multiple_points(self) -> Optional[str]:
        """Defaults to
        ``'{annotationText}. Related to {annotationPoint}{ Also related to, #each(additionalAnnotationPoints)}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_multiple_points

    @description_multiple_points.setter
    def description_multiple_points(self, value):
        self._description_multiple_points = validators.string(value, allow_empty = True)

    @property
    def description_no_points(self) -> Optional[str]:
        """Defaults to
        ``'{annotationText}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_no_points

    @description_no_points.setter
    def description_no_points(self, value):
        self._description_no_points = validators.string(value,
                                                        allow_empty = True)

    @property
    def description_single_point(self) -> Optional[str]:
        """Defaults to
        ``'{annotationText}. Related to {annotationPoint}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_single_point

    @description_single_point.setter
    def description_single_point(self, value):
        self._description_single_point = validators.string(value, allow_empty = True)

    @property
    def heading(self) -> Optional[str]:
        """Defaults to
        ``'Chart annotations summary'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'description_multiple_points': as_dict.get('descriptionMultiplePoints', None),
            'description_no_points': as_dict.get('descriptionNoPoints', None),
            'description_single_point': as_dict.get('descriptionSinglePoint', None),
            'heading': as_dict.get('heading', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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

        self.after_region_label = kwargs.get('after_region_label', None)
        self.annotations = kwargs.get('annotations', None)
        self.before_region_label = kwargs.get('before_region_label', None)
        self.end_of_chart_marker = kwargs.get('end_of_chart_marker', None)

    @property
    def after_region_label(self) -> Optional[str]:
        """Defaults to ``''`` (empty
        string).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
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
        """Defaults to ``''`` (empty
        string).

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._before_region_label

    @before_region_label.setter
    def before_region_label(self, value):
        self._before_region_label = validators.string(value, allow_empty = True)

    @property
    def end_of_chart_marker(self) -> Optional[str]:
        """Defaults to ``'End of interactive chart.'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._end_of_chart_marker

    @end_of_chart_marker.setter
    def end_of_chart_marker(self, value):
        self._end_of_chart_marker = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'after_region_label': as_dict.get('afterRegionLabel', None),
            'annotations': as_dict.get('annotations', None),
            'before_region_label': as_dict.get('beforeRegionLabel', None),
            'end_of_chart_marker': as_dict.get('endOfChartMarker', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'afterRegionLabel': self.after_region_label,
            'annotations': self.annotations,
            'beforeRegionLabel': self.before_region_label,
            'endOfChartMarker': self.end_of_chart_marker
        }

        return untrimmed
