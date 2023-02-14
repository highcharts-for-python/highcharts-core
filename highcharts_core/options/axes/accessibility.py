from typing import Optional

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class AxisAccessibility(HighchartsMeta):
    """Accessibility options for an axis object."""

    def __init__(self, **kwargs):
        self._description = None
        self._enabled = None
        self._range_description = None

        self.description = kwargs.get('description', None)
        self.enabled = kwargs.get('enabled', None)
        self.range_description = kwargs.get('range_description', None)

    @property
    def description(self) -> Optional[str]:
        """Description for an axis that is exposed to screen reader users. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables axis accessibility features, including axis information in
        the screen reader information region. Defaults to :obj:`None <python:None>`.

        If this is ``False`` on the x-axis, by default, the x values will not be exposed
        to screen readers for the individual data points.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def range_description(self) -> Optional[str]:
        """Range description for an axis that is exposed to screen reader users. Overrides
        the default range description. Defaults to :obj:`None <python:None>`, which
        applies the default range description.

        .. hint::

          Set to an empty string to completely disable range descriptions for the axis.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._range_description

    @range_description.setter
    def range_description(self, value):
        if value is None:
            self._range_description = None
        elif value == '':
            self._range_description = ''
        else:
            self._range_description = validators.string(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.get('description', None),
            'enabled': as_dict.get('enabled', None),
            'range_description': as_dict.get('rangeDescription', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'description': self.description,
            'enabled': self.enabled,
            'rangeDescription': self.range_description
        }

        return untrimmed
