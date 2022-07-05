from typing import Optional

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class AnimationOptions(HighchartsMeta):
    """An animation configuration.

    .. note::

      Animation configurations can also be defined as :class:`bool <python:bool>`, where
      ``False`` turns off animation and ``True`` defaults to a duration of 500ms and defer
      of 0ms.

    """

    def __init__(self, **kwargs):
        self._complete = None
        self._defer = 0
        self._duration = 500
        self._easing = None
        self._step = None

        self.complete = kwargs.pop('complete', None)
        self.defer = kwargs.pop('defer', 0)
        self.duration = kwargs.pop('duration', 500)
        self.easing = kwargs.pop('easing', None)
        self.step = kwargs.pop('step', None)

    @property
    def complete(self) -> Optional[str]:
        """A JavaScript callback function to execute when the animation finishes.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._complete

    @complete.setter
    def complete(self, value):
        self._complete = validators.string(value, allow_empty = True)

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
    def step(self) -> Optional[str]:
        """A JavaScript callback function to execute on each step of each attribute or
        CSS property that is being animated.

        The first argument contains information about the animation and progress.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._step

    @step.setter
    def step(self, value):
        self._step = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'complete': as_dict.pop('complete', None),
            'defer': as_dict.pop('defer', 0),
            'duration': as_dict.pop('duration', 500),
            'easing': as_dict.pop('easing', None),
            'step': as_dict.pop('step', None)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'complete': self.complete,
            'defer': self.defer,
            'duration': self.duration,
            'easing': self.easing,
            'step': self.step
        }

        return self.trim_dict(untrimmed)
