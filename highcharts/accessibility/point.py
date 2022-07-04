from typing import Optional, Any

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta
from highcharts import errors, constants


class AccessibilityPoint(HighchartsMeta):
    """Options for describing individual points."""

    def __init__(self, **kwargs):
        self._date_format = None
        self._date_formatter = None
        self._describe_null = True
        self._description_formatter = None
        self._value_decimals = None
        self._value_description_format = constants.DEFAULT_ACCESSIBILITY_POINT_VALUE_FORMAT
        self._value_prefix = None
        self._value_suffix = None

        self.date_format = kwargs.pop('date_format', None)
        self.date_formatter = kwargs.pop('date_formatter', None)
        self.describe_null = kwargs.pop('describe_null', True)
        self.description_formatter = kwargs.pop('description_formatter', None)
        self.value_decimals = kwargs.pop('value_decimals', None)
        self.value_description_format = kwargs.pop('value_description_format',
                                                   constants.DEFAULT_ACCESSIBILITY_POINT_VALUE)
        self.value_prefix = kwargs.pop('value_prefix', None)
        self.value_suffix = kwargs.pop('value_suffix', None)

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
    def date_formatter(self) -> Optional[str]:
        """JavaScript formatter function to determine the date/time format used with
        points on datetime axes when describing them to screen reader users.

        The formatter function should receive one argument, ``point``, referring to the
        point to describe. Should return a date format string compatible with
        :meth:`AccessibilityPoint.date_format`.

        :returns: Formatter function to determine date/time format used.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._date_formatter

    @date_formatter.setter
    def date_formatter(self, value):
        self._date_formatter = validators.string(value, allow_empty = True)

    @property
    def describe_null(self) -> bool:
        """If ``True``, will describe points with the value ``null`` to assistive
        technology (e.g. screen readers).

        Defaults to ``True``.

        :returns: Flag indicating whether to describe points with the value ``null`` to
          assistive technology.
        :rtype: :class:`bool <python:bool>`
        """
        return self._describe_null

    @describe_null.setter
    def describe_null(self, value):
        self._describe_null = bool(value)

    @property
    def description_formatter(self) -> Optional[str]:
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
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description_formatter

    @description_formatter.setter
    def description_formatter(self, value):
        self._value = validators.string(value, allow_empty = True)

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
        f"""Format to use for describing the values of data points to assistive technology
        - including screen readers. The point context is available as ``{{point}}``.

        Defaults to ``{constants.DEFAULT_ACCESSIBILITY_POINT_VALUE_FORMAT}``

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
    def from_dict(cls, as_dict):
        kwargs = {
            'date_format': as_dict.pop('dateFormat', None),
            'date_formatter': as_dict.pop('dateFormatter', None),
            'describe_null': as_dict.pop('describeNull', True),
            'description_formatter': as_dict.pop('descriptionFormatter', None),
            'value_decimals': as_dict.pop('valueDecimals', None),
            'value_description_format': as_dict.pop('valueDescriptionFormat',
                                                    constants.DEFAULT_ACCESSIBILITY_POINT_VALUE_FORMAT),
            'value_prefix': as_dict.pop('valuePrefix', None),
            'value_suffix': as_dict.pop('valueSuffix', None)
        }
        return cls(**kwargs)

    def to_dict(self, encoding = 'utf-8'):
        untrimmed = {
            'dateFormat': self.date_format,
            'dateFormatter': self.date_formatter,
            'describeNull': self.describe_null,
            'descriptionFormatter': self.description_formatter,
            'valueDecimals': self.valueDecimals,
            'valueDescriptionFormat': self.value_description_format,
            'valuePrefix': self.value_prefix,
            'valueSuffix': self.value_suffix
        }
        as_dict = self.trim_dict(untrimmed)

        return as_dict
