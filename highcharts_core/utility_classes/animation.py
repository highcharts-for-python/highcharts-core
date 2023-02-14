from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class AnimationOptions(HighchartsMeta):
    """An animation configuration.

    .. note::

      Animation configurations can also be defined as :class:`bool <python:bool>`, where
      ``False`` turns off animation and ``True`` defaults to a duration of 500ms and defer
      of 0ms.

    """

    def __init__(self, **kwargs):
        self._complete = None
        self._defer = None
        self._duration = None
        self._easing = None
        self._step = None

        self.complete = kwargs.get('complete', None)
        self.defer = kwargs.get('defer', None)
        self.duration = kwargs.get('duration', None)
        self.easing = kwargs.get('easing', None)
        self.step = kwargs.get('step', None)

    @property
    def complete(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function to execute when the animation finishes.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._complete

    @complete.setter
    @class_sensitive(CallbackFunction)
    def complete(self, value):
        self._complete = value

    @property
    def defer(self) -> Optional[int]:
        """The number of milliseconds to defer the animation. Defaults to ``0``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`

        :raises ValueError: if set to a negative number
        """
        return self._defer

    @defer.setter
    def defer(self, value):
        self._defer = validators.integer(value,
                                         allow_empty = True,
                                         minimum = 0,
                                         coerce_value = True)

    @property
    def duration(self) -> Optional[int]:
        """The animation duration, expressed in milliseconds. Defaults to ``500``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`

        :raises ValueError: if set to a negative number
        """
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = validators.integer(value,
                                            allow_empty = True,
                                            minimum = 0,
                                            coerce_value = True)

    @property
    def easing(self) -> Optional[str]:
        """The name of an easing function as defined on the JavaScript ``Math`` object.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._easing

    @easing.setter
    def easing(self, value):
        self._easing = validators.string(value, allow_empty = True)

    @property
    def step(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function to execute on each step of each attribute or
        CSS property that is being animated.

        The first argument contains information about the animation and progress.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._step

    @step.setter
    @class_sensitive(CallbackFunction)
    def step(self, value):
        self._step = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'complete': as_dict.get('complete', None),
            'defer': as_dict.get('defer', None),
            'duration': as_dict.get('duration', None),
            'easing': as_dict.get('easing', None),
            'step': as_dict.get('step', None)
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'complete': self.complete,
            'defer': self.defer,
            'duration': self.duration,
            'easing': self.easing,
            'step': self.step
        }

        return untrimmed
