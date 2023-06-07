from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class Condition(HighchartsMeta):
    """Setting controls when to apply the
    :meth:`chart_options <ResponsiveRules.chart_options>`."""

    def __init__(self, **kwargs):
        self._callback = None
        self._max_height = None
        self._max_width = None
        self._min_height = None
        self._min_width = None

        self.callback = kwargs.get('callback', None)
        self.max_height = kwargs.get('max_height', None)
        self.max_width = kwargs.get('max_width', None)
        self.min_height = kwargs.get('min_height', None)
        self.min_width = kwargs.get('min_width', None)

    @property
    def callback(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function to gain complete control on when the responsive
        rule applies. Return ``true`` if it applies.

        .. hint::

          This feature enables you to use information besides the chart size to determine
          whether to enforce a set of :class:`ResponsiveRules` or not. Typical use cases
          might be to make the determination based on document size, available container
          size, or other other element on the page.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._callback

    @callback.setter
    @class_sensitive(CallbackFunction)
    def callback(self, value):
        self._callback = value

    @property
    def max_height(self) -> Optional[int | float | Decimal]:
        """The responsive rule applies if the chart height is less than this. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_height

    @max_height.setter
    def max_height(self, value):
        if value is None:
            self._max_height = None
        else:
            self._max_height = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def max_width(self) -> Optional[int | float | Decimal]:
        """The responsive rule applies if the chart width is less than this. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_width

    @max_width.setter
    def max_width(self, value):
        if value is None:
            self._max_width = None
        else:
            self._max_width = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def min_height(self) -> Optional[int | float | Decimal]:
        """The responsive rule applies if the chart height is greater than this. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_height

    @min_height.setter
    def min_height(self, value):
        if value is None:
            self._min_height = None
        else:
            self._min_height = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def min_width(self) -> Optional[int | float | Decimal]:
        """The responsive rule applies if the chart width is greater than this. Defaults
        to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_width

    @min_width.setter
    def min_width(self, value):
        if value is None:
            self._min_width = None
        else:
            self._min_width = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'callback': as_dict.get('callback', None),
            'max_height': as_dict.get('maxHeight', None),
            'max_width': as_dict.get('maxWidth', None),
            'min_height': as_dict.get('minHeight', None),
            'min_width': as_dict.get('minWidth', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'callback': self.callback,
            'maxHeight': self.max_height,
            'maxWidth': self.max_width,
            'minHeight': self.min_height,
            'minWidth': self.min_width
        }

        return untrimmed


class ResponsiveRules(HighchartsMeta):
    """A set of rules for responsive settings."""

    def __init__(self, **kwargs):
        self._chart_options = None
        self._condition = None

        self.chart_options = kwargs.get('chart_options', None)
        self.condition = kwargs.get('condition', None)

    @property
    def chart_options(self) -> Optional[HighchartsMeta]:
        """A full set of chart :class:`HighchartsOptions` to apply as overrides to the general chart
        :class:`HighchartsOptions`. The chart options are applied when the given rule is active, as
        per :meth:`ResponsiveRules.condition`.

        .. note::

          A special case is configuration objects that take arrays, for example
          :meth:`Options.x_axis`, :meth:`Options.y_axis`, or :meth:`Options.series`. For
          these collections, an ``id`` option is used to map the new option set to an
          existing object. If an existing object of the same ``id`` is not found, the item
          of the same index is updated. So for example, setting :meth:`Options.series`
          with two series without an ``id``, will cause the existing chart's two series to
          be updated with respective options.

        :rtype: :class:`HighchartsOptions` or :obj:`None <python:None>`
        """
        return self._chart_options

    @chart_options.setter
    def chart_options(self, value):
        from highcharts_core.options import HighchartsOptions

        self._chart_options = validate_types(value, types = HighchartsOptions)

    @property
    def condition(self) -> Optional[Condition]:
        """Setting controls when to apply the
        :meth:`chart_options <ResponsiveRules.chart_options>`.

        :rtype: :class:`Condition` or :obj:`None <python:None>`
        """
        return self._condition

    @condition.setter
    @class_sensitive(Condition)
    def condition(self, value):
        self._condition = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'chart_options': as_dict.get('chartOptions', None),
            'condition': as_dict.get('condition', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'chartOptions': self.chart_options,
            'condition': self.condition
        }

        return untrimmed


class Responsive(HighchartsMeta):
    """Rules to apply for different screen or chart sizes.

    .. note::

      Each rule specifies additional chart options.

    """

    def __init__(self, **kwargs):
        self._rules = None

        self.rules = kwargs.get('rules', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'responsive'

    @property
    def rules(self) -> Optional[List[ResponsiveRules]]:
        """A set of rules for responsive settings.

        .. note::

          The rules are applied in the order provided.

        :rtype: :class:`list <python:list>` of :class:`ResponsiveRules` or
          :obj:`None <python:None>`
        """
        return self._rules

    @rules.setter
    @class_sensitive(ResponsiveRules, force_iterable = True)
    def rules(self, value):
        self._rules = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return {
            'rules': as_dict.get('rules', None)
        }

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'rules': self.rules
        }

        return untrimmed
