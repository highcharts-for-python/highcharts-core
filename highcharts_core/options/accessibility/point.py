from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class AccessibilityPoint(HighchartsMeta):
    """Options for describing individual points."""

    def __init__(self, **kwargs):
        self._date_format = None
        self._date_formatter = None
        self._describe_null = None
        self._description_format = None
        self._description_formatter = None
        self._value_decimals = None
        self._value_description_format = None
        self._value_prefix = None
        self._value_suffix = None

        self.date_format = kwargs.get('date_format', None)
        self.date_formatter = kwargs.get('date_formatter', None)
        self.describe_null = kwargs.get('describe_null', None)
        self.description_format = kwargs.get('description_format', None)
        self.description_formatter = kwargs.get('description_formatter', None)
        self.value_decimals = kwargs.get('value_decimals', None)
        self.value_description_format = kwargs.get('value_description_format', None)
        self.value_prefix = kwargs.get('value_prefix', None)
        self.value_suffix = kwargs.get('value_suffix', None)

    @property
    def date_format(self) -> Optional[str]:
        """Date format to use for points on datetime axes when describing them to screen
        reader users.

        Defaults to the same format as in tooltip.

        .. seealso::

          * Detailed documentation on supported format replacement codes:
            https://api.highcharts.com/class-reference/Highcharts.Time#dateFormat

        :returns: The date format to use for points on datetime axes when describing them
          to screen reader users.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._date_format

    @date_format.setter
    def date_format(self, value):
        self._date_format = validators.string(value, allow_empty = True)

    @property
    def date_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript formatter function to determine the date/time format used with
        points on datetime axes when describing them to screen reader users.

        The formatter function should receive one argument, ``point``, referring to the
        point to describe. Should return a date format string compatible with
        :meth:`AccessibilityPoint.date_format`.

        :returns: Formatter function to determine date/time format used.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._date_formatter

    @date_formatter.setter
    @class_sensitive(CallbackFunction)
    def date_formatter(self, value):
        self._date_formatter = value

    @property
    def describe_null(self) -> Optional[bool]:
        """If ``True``, will describe points with the value ``null`` to assistive
        technology (e.g. screen readers).

        Defaults to ``True``.

        :returns: Flag indicating whether to describe points with the value ``null`` to
          assistive technology.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._describe_null

    @describe_null.setter
    def describe_null(self, value):
        if value is None:
            self._describe_null = None
        else:
            self._describe_null = bool(value)

    @property
    def description_format(self) -> Optional[str]:
        """A :term:`format string` to use instead of the default for 
        point descriptions.
        
        The context of the format string is the point instance, but as opposed to 
        :meth:`.value_description_format <highcharts_core.options.accessibility.point.AccessibilityPoint.value_description_format>`, this option replaces the entire description.
        
        Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_format
    
    @description_format.setter
    def description_format(self, value):
        self._description_format = validators.string(value, allow_empty = True)

    @property
    def description_formatter(self) -> Optional[CallbackFunction]:
        """JavaScript formatter function to use instead of the default for point
        descriptions.

        The JavaScript formatter function should receive one argument, ``point``,
        referring to the point to describe. Should return a string with the description of
        the point for a screen reader user. If ``false`` is returned, the default
        formatter will be used for that point.

        .. tip::

            Best practice is to use :meth:`Accessibility.value_description_format` instead
            if possible, as default functionality such as describing annotations will be
            preserved.

        :returns: The JavaScript formatter function to use for point descriptions.
        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._description_formatter

    @description_formatter.setter
    @class_sensitive(CallbackFunction)
    def description_formatter(self, value):
        self._description_formatter = value

    @property
    def value_decimals(self) -> Optional[int]:
        """Number of digits after the decimal point to use for the values in the point
        description. Uses :meth:`Tooltip.value_decimals` if not provided here.

        :returns: Number of digits to use after the decimal point.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`

        :raises ValueError: if a negative number is provided
        """
        return self._value_decimals

    @value_decimals.setter
    def value_decimals(self, value):
        self._value_decimals = validators.integer(value,
                                                  allow_empty = True,
                                                  coerce_value = True,
                                                  minimum = 0)

    @property
    def value_description_format(self) -> Optional[str]:
        """Format to use for describing the values of data points to assistive technology
        - including screen readers. The point context is available as ``{{point}}``.

        Defaults to ``{xDescription}{separator}{value}``

        Other available context variables include ``{{index}}``, ``{{value}}``, and
        ``{{xDescription}}``.

        .. note::

          Additionally, the series name, annotation info, and description added in
          :meth:`Point.accessibility.description` is added by default if relevant.
          To override this, use the :meth:`AccessibilityPoint.description_formatter`
          option.

        :returns: Format to use for describing the values of data points to assistive
          technology.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value_description_format

    @value_description_format.setter
    def value_description_format(self, value):
        self._value_description_format = validators.string(value, allow_empty = True)

    @property
    def value_prefix(self) -> Optional[str]:
        """Prefix to add to the values in the point descriptions.

        .. note::

          Uses :meth:`Tooltip.value_prefix` if not defined.

        :returns: Prefix to add to the values in the point description.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value_prefix

    @value_prefix.setter
    def value_prefix(self, value):
        self._value_prefix = validators.string(value, allow_empty = True)

    @property
    def value_suffix(self) -> Optional[str]:
        """Suffix to add to the values in the point descriptions.

        .. note::

          Uses :meth:`Tooltip.value_suffix` if not defined.

        :returns: Suffix to add to the values in the point description.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value_suffix

    @value_suffix.setter
    def value_suffix(self, value):
        self._value_suffix = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'date_format': as_dict.get('dateFormat', None),
            'date_formatter': as_dict.get('dateFormatter', None),
            'describe_null': as_dict.get('describeNull', None),
            'description_format': as_dict.get('descriptionFormat', None),
            'description_formatter': as_dict.get('descriptionFormatter', None),
            'value_decimals': as_dict.get('valueDecimals', None),
            'value_description_format': as_dict.get('valueDescriptionFormat', None),
            'value_prefix': as_dict.get('valuePrefix', None),
            'value_suffix': as_dict.get('valueSuffix', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dateFormat': self.date_format,
            'dateFormatter': self.date_formatter,
            'describeNull': self.describe_null,
            'descriptionFormat': self.description_format,
            'descriptionFormatter': self.description_formatter,
            'valueDecimals': self.value_decimals,
            'valueDescriptionFormat': self.value_description_format,
            'valuePrefix': self.value_prefix,
            'valueSuffix': self.value_suffix
        }

        return untrimmed
