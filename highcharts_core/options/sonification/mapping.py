from typing import Optional, List
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_core import errors
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.utility_classes.javascript_functions import CallbackFunction


class AudioParameter(HighchartsMeta):
    """Configuration of an audio parameter's settings."""
    
    def __init__(self, **kwargs):
        self._map_function = None
        self._map_to = None
        self._max = None
        self._min = None
        self._value = None
        self._within = None
        
        self.map_function = kwargs.get('map_function', None)
        self.map_to = kwargs.get('map_to', None)
        self.max = kwargs.get('max', None)
        self.min = kwargs.get('min', None)
        self.value = kwargs.get('value', None)
        self.within = kwargs.get('within', None)
        
    @property
    def map_function(self) -> Optional[str]:
        """The name of the mapping function to apply. Accepts either ``'linear'`` or ``'logarithmic'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map_function
    
    @map_function.setter
    def map_function(self, value):
        if not value:
            self._map_function = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['linear', 'logarithmic']:
                raise errors.HighchartsValueError(f'.map_function expects either "linear" or "logarithmic". '
                                                  f'Received: "{value}"')
            self._map_function = value

    @property
    def map_to(self) -> Optional[str]:
        """The name of the point property to map to determine the audio setting.
        
        .. tip::
        
          A negative sign (``'-'``) can be placed *before* the name of the property to invert
          the mapping.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map_to
    
    @map_to.setter
    def map_to(self, value):
        self._map_to = validators.string(value, allow_empty = True)
    
    @property
    def max(self) -> Optional[int | float | Decimal]:
        """The maximum value for the audio parameter. This is the highest value the audio parameter will be 
        mapped to.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max
    
    @max.setter
    def max(self, value):
        self._max = validators.numeric(value, allow_empty = True)
        
    @property
    def min(self) -> Optional[int | float | Decimal]:
        """The minimum value for the audio parameter. This is the lowest value the audio parameter will be 
        mapped to.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min
    
    @min.setter
    def min(self, value):
        self._min = validators.numeric(value, allow_empty = True)
        
    @property
    def value(self) -> Optional[int | float | Decimal]:
        """A fixed value to use in place of the mapped ``prop`` when mapping.
        
        .. note::
        
          For example, if mapping to ``'y'``, setting ``.value = 4`` will map as if all
          points had a ``y`` value equal of ``4``.
          
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = validators.numeric(value, allow_empty = True)
        
    @property
    def within(self) -> Optional[str]:
        """The data values within which to map the audio parameter. Accepts ``'series'``, ``'chart'``, ``'yAxis'``, 
        ``'xAxis'``. Defaults to :obj:`None <python:None>`.
        
        .. note::
        
          Mapping within ``'series'`` will make the lowest value point in the *series* map to the 
          :meth:`.min <highcharts_core.options.sonification.mapping.AudioParameter.min>` audio parameter value, and the 
          highest value will map to the :meth:`.max <highcharts_core.options.sonification.mapping.AudioParameter.max>` 
          audio parameter.
          
          Mapping within ``'chart'`` will make the lowest value point in the *chart* (across all series) map to the 
          :meth:`.min <highcharts_core.options.sonification.mapping.AudioParameter.min>` audio parameter value, and the 
          highest value will map to the :meth:`.max <highcharts_core.options.sonification.mapping.AudioParameter.max>` 
          audio parameter.
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._within

    @within.setter
    def within(self, value):
        if not value:
            self._within = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['series', 'chart', 'xaxis', 'yaxis']:
                raise errors.HighchartsValueError(f'.within expects a value of either "series", "chart", '
                                                  f'"xAxis", or "yAxis". Received: "{value}"')
            if value == 'xaxis':
                value = 'xAxis'
            elif value == 'yaxis':
                value = 'yAxis'
                
            self._within = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'map_function': as_dict.get('mapFunction', None),
            'map_to': as_dict.get('mapTo', None),
            'max': as_dict.get('max', None),
            'min': as_dict.get('min', None),
            'value': as_dict.get('value', None),
            'within': as_dict.get('within', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'mapFunction': self.map_function,
            'mapTo': self.map_to,
            'max': self.max,
            'min': self.min,
            'value': self.value,
            'within': self.within,
        }

        return untrimmed


class PitchParameter(AudioParameter):
    """The configuration settings to configure :term:`pitch`.
    
    By default, this object maps to ``'y'``, so low ``'y'`` values are played with a lower pitch
    and high ``'y'`` values are played with a higher pitch.
    
    .. note::
    
      The properties for configuring pitch accept :class:`str <python:str>` values as well as 
      numerical values, specifically allowing you to indicate the musical note that you wish the
      audio track to play. These notes are expressed in the form ``<note><octave>``, such as ``'c6'`` or
      ``'F#2'``.
      
    .. tip::
    
      You configure the pitch to map to an array of notes, with the delay between notes determined by the
      :meth:`SonificationMapping.gap_between_notes <highcharts_core.options.sonification.mapping.SonificationMapping.gap_between_notes>`
      property.
      
    .. tip::
    
      You can also define a musical :meth:`.scale <highcharts_core.options.sonification.mapping.PitchParameter.scale>`
      to follow when mapping.
    
    """
    
    def __init__(self, **kwargs):
        self._scale = None
        
        self.scale = kwargs.get('scale', None)
        
        super().__init__(**kwargs)

    @property
    def map_to(self) -> Optional[str]:
        """The name of the point property to map to determine the audio setting. Defaults to ``'y'``.
        
        .. tip::
        
          A negative sign (``'-'``) can be placed *before* the name of the property to invert
          the mapping.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._map_to
    
    @map_to.setter
    def map_to(self, value):
        self._map_to = validators.string(value, allow_empty = True)
    
    @property
    def max(self) -> Optional[str | int | float | Decimal]:
        """The maximum value for the audio parameter. This is the highest value the audio parameter will be 
        mapped to. Defaults to ``'c6'``.
        
        :rtype: numeric, :class:`str <python:str>`, or :obj:`None <python:None>`
        """
        return self._max
    
    @max.setter
    def max(self, value):
        if value is None:
            self._max = None
        else:
            try:
                self._max = validators.numeric(value)
            except (ValueError, TypeError):
                self._max = validators.string(value)
        
    @property
    def min(self) -> Optional[str | int | float | Decimal]:
        """The minimum value for the audio parameter. This is the lowest value the audio parameter will be 
        mapped to. Defaults to ``'c2'``.
        
        :rtype: numeric, :class:`str <python:str>`, or :obj:`None <python:None>`
        """
        return self._min
    
    @min.setter
    def min(self, value):
        if value is None:
            self._min = None
        else:
            try:
                self._min = validators.numeric(value)
            except (ValueError, TypeError):
                self._min = validators.string(value)
        
    @property
    def scale(self) -> Optional[List[str | int | float | Decimal]]:
        """The scale to map pitches against, defined as an array of semitone offsets from the root note.
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>` in the form ``'<note><octave>'`` 
          (e.g. ``'c2'``, ``'F#2'``, etc.) or numeric values, or :obj:`None <python:None>`
        """
        return self._scale
    
    @scale.setter
    def scale(self, value):
        if not value:
            self._scale = None
        else:
            value = validators.iterable(value, forbid_literals = (str, bytes, dict))
            validated = []
            for item in value:
                try:
                    item = validators.numeric(item)
                except (ValueError, TypeError):
                    item = validators.string(item)
                    
                validated.append(item)

            self._scale = [x for x in validated]

    @property
    def value(self) -> Optional[int | float | Decimal | str]:
        """A fixed value to use in place of the mapped ``prop`` when mapping. Defaults to
        :obj:`None <python:None>`.
        
        .. note::
        
          For example, if mapping to ``'y'``, setting ``.value = 4`` will map as if all
          points had a ``y`` value equal of ``4``.
          
        :rtype: :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._value
    
    @value.setter
    def value(self, value):
        if value is None:
            self._value = None
        else:
            try:
                self._value = validators.numeric(value)
            except (ValueError, TypeError):
                self._value = validators.string(value)
        
    @property
    def within(self) -> Optional[str]:
        """The data values within which to map the audio parameter. Accepts ``'series'``, ``'chart'``, ``'yAxis'``, 
        ``'xAxis'``. Defaults to ``'yAxis'``.
        
        .. note::
        
          Mapping within ``'series'`` will make the lowest value point in the *series* map to the 
          :meth:`.min <highcharts_core.options.sonification.mapping.AudioParameter.min>` audio parameter value, and the 
          highest value will map to the :meth:`.max <highcharts_core.options.sonification.mapping.AudioParameter.max>` 
          audio parameter.
          
          Mapping within ``'chart'`` will make the lowest value point in the *chart* (across all series) map to the 
          :meth:`.min <highcharts_core.options.sonification.mapping.AudioParameter.min>` audio parameter value, and the 
          highest value will map to the :meth:`.max <highcharts_core.options.sonification.mapping.AudioParameter.max>` 
          audio parameter.
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._within

    @within.setter
    def within(self, value):
        if not value:
            self._within = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['series', 'chart', 'xaxis', 'yaxis']:
                raise errors.HighchartsValueError(f'.within expects a value of either "series", "chart", '
                                                  f'"xAxis", or "yAxis". Received: "{value}"')
            if value == 'xaxis':
                value = 'xAxis'
            elif value == 'yaxis':
                value = 'yAxis'
                
            self._within = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'map_function': as_dict.get('mapFunction', None),
            'map_to': as_dict.get('mapTo', None),
            'max': as_dict.get('max', None),
            'min': as_dict.get('min', None),
            'scale': as_dict.get('scale', None),
            'value': as_dict.get('value', None),
            'within': as_dict.get('within', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'mapFunction': self.map_function,
            'mapTo': self.map_to,
            'max': self.max,
            'min': self.min,
            'scale': self.scale,
            'value': self.value,
            'within': self.within,
        }

        return untrimmed


class AudioFilter(HighchartsMeta):
    """Configuration of an audio filter, such as a :term:`highpass` or :term:`lowpass` filter.
    """

    def __init__(self, **kwargs):
        self._frequency = None
        self._resonance = None
        
        self.frequency = kwargs.get('frequency', None)
        self.resonance = kwargs.get('resonance', None)

    @property
    def frequency(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The frequency, expressed in Hertz, between 1 to 20,000 Hz.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._frequency
    
    @frequency.setter
    def frequency(self, value):
        if value is None:
            self._frequency = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value,
                                                   minimum = 1,
                                                   maximum = 20000)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._frequency = value

    @property
    def resonance(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The resonance, expressed in Db. Can be negative to cause a dip, or positive to cause a bump.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._resonance
    
    @resonance.setter
    def resonance(self, value):
        if value is None:
            self._resonance = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._resonance = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'frequency': as_dict.get('frequency', None),
            'resonance': as_dict.get('resonance', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'frequency': self.frequency,
            'resonance': self.resonance,
        }

        return untrimmed


class TremoloEffect(HighchartsMeta):
    """Configuration of a :term:`tremolo` effect."""
    
    def __init__(self, **kwargs):
        self._depth = None
        self._speed = None
        
        self.depth = kwargs.get('depth', None)
        self.speed = kwargs.get('speed', None)

    @property
    def depth(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The intensity of the :term:`tremolo` effect over time, mapped from ``0`` to ``1``.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._depth
    
    @depth.setter
    def depth(self, value):
        if value is None:
            self._depth = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value,
                                                   minimum = 0,
                                                   maximum = 1)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._depth = value

    @property
    def speed(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The speed of the :term:`tremolo` effect, mapped from ``0`` to ``1``, which determines how rapidly
        the volume changes.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        if value is None:
            self._speed = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value,
                                                   minimum = 0,
                                                   maximum = 1)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._speed = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'depth': as_dict.get('depth', None),
            'speed': as_dict.get('speed', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'depth': self.depth,
            'speed': self.speed,
        }

        return untrimmed


class SonificationMapping(HighchartsMeta):
    """Mapping options for audio parameters.
    
    All properties in this object accept either:
    
      * an object instance (or coercable to an object instance) as outlined in the documentation
      * a :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
      * a :class:`str <python:str>`
      * a numeric value
      
    If supplying a :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`,
    the function is expected to:
      
      * be called for each audio event to be played
      * receive a context object parameter containing ``time``, and potentially ``point`` and ``value`` depending on the
        track being played (``point`` provided if the audio event is related to a data point, and ``value`` if the 
        track is used as a context track with 
        :meth:`.value_interval <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration.value_interval>` set).
        
    """
    
    def __init__(self, **kwargs):
        self._frequency = None
        self._gap_between_notes = None
        self._highpass = None
        self._lowpass = None
        self._note_duration = None
        self._pan = None
        self._pitch = None
        self._play_delay = None
        self._rate = None
        self._text = None
        self._time = None
        self._tremolo = None
        self._volume = None
        
        self.frequency = kwargs.get('frequency', None)
        self.gap_between_notes = kwargs.get('gap_between_notes', None)
        self.highpass = kwargs.get('highpass', None)
        self.lowpass = kwargs.get('lowpass', None)
        self.note_duration = kwargs.get('note_duration', None)
        self.pan = kwargs.get('pan', None)
        self.pitch = kwargs.get('pitch', None)
        self.play_delay = kwargs.get('play_delay', None)
        self.rate = kwargs.get('rate', None)
        self.text = kwargs.get('text', None)
        self.time = kwargs.get('time', None)
        self.tremolo = kwargs.get('tremolo', None)
        self.volume = kwargs.get('volume', None)
        
    @property
    def frequency(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The frequency, expressed in Hertz, of notes. 
        
        Overrides :meth:`.pitch <highcharts_core.options.sonification.mapping.SonificationMapping.pitch>` if set.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._frequency
    
    @frequency.setter
    def frequency(self, value):
        if value is None:
            self._frequency = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._frequency = value
    
    @property
    def gap_between_notes(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The gap in milliseconds between notes if 
        :meth:`.pitch <highcharts_core.options.sonification.mapping.SonificationMapping.pitch>` is mapped to an
        array of notes.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._gap_between_notes
    
    @gap_between_notes.setter
    def gap_between_notes(self, value):
        if value is None:
            self._gap_between_notes = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._gap_between_notes = value

    @property
    def highpass(self) -> Optional[AudioFilter]:
        """Configuration for the :term:`highpass` filter.
        
        :rtype: :class:`AudioFilter <highcharts_core.options.sonification.mapping.AudioFilter>` or 
          :obj:`None <python:None>`
        """
        return self._highpass
    
    @highpass.setter
    @class_sensitive(AudioFilter)
    def highpass(self, value):
        self._highpass = value
        
    @property
    def lowpass(self) -> Optional[AudioFilter]:
        """Configuration for the :term:`lowpass` filter.
        
        :rtype: :class:`AudioFilter <highcharts_core.options.sonification.mapping.AudioFilter>` or 
          :obj:`None <python:None>`
        """
        return self._lowpass
    
    @lowpass.setter
    @class_sensitive(AudioFilter)
    def lowpass(self, value):
        self._lowpass = value

    @property
    def note_duration(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """How long a note plays in a sustained fashion, expressed in milliseconds.
        
        .. note::
        
          It only affects instruments that are able to play continuous sustained notes. Examples of these instruments 
          from the presets include: ``'flute'``, ``'saxophone'``, ``'trumpet'``, ``'sawsynth'``, ``'wobble'``, 
          ``'basic1'``, ``'basic2'``, ``'sine'``, ``'sineGlide'``, ``'triangle'``, ``'square'``, ``'sawtooth'``, 
          ``'noise'``, ``'filteredNoise'``, and ``'wind'``.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._note_duration
    
    @note_duration.setter
    def note_duration(self, value):
        if value is None:
            self._note_duration = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._note_duration = value
    
    @property
    def pan(self)  -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The stereo panning position of the sound, defined between left (``-1``) and right (``1``).
        Defaults to a mapping object which maps to the ``'x'`` property, which causes the sound to move 
        from left to right as the chart plays.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._pan
    
    @pan.setter
    def pan(self, value):
        if value is None:
            self._pan = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value,
                                                   minimum = -1,
                                                   maximum = 1)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._pan = value
    
    @property
    def pitch(self) -> Optional[List[PitchParameter | CallbackFunction | str | int | float | Decimal] | PitchParameter | CallbackFunction | str | int | float | Decimal]:
        """Configuration of :term:`pitch` for the audio track.
        
        By default, this object maps to ``'y'``, so low ``'y'`` values are played with a lower pitch
        and high ``'y'`` values are played with a higher pitch.
        
        .. note::
        
          The properties for configuring pitch accept :class:`str <python:str>` values as well as 
          numerical values, specifically allowing you to indicate the musical note that you wish the
          audio track to play. These notes are expressed in the form ``<note><octave>``, such as ``'c6'`` or
          ``'F#2'``.
        
        .. tip::
        
          You configure the pitch to map to an array of notes, with the delay between notes determined by the
          :meth:`SonificationMapping.gap_between_notes <highcharts_core.options.sonification.mapping.SonificationMapping.gap_between_notes>`
          property.
        
        .. tip::
        
          You can also define a musical 
          :meth:`.scale <highcharts_core.options.sonification.mapping.PitchParameter.scale>`
          to follow when mapping.
        
        :rtype: iterable of :class:`PitchParameter <highcharts_core.options.sonification.mapping.PitchParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric, or :class:`PitchParameter <highcharts_core.options.sonification.mapping.PitchParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric, or:obj:`None <python:None>`
        """
        return self._pitch
    
    @pitch.setter
    def pitch(self, value):
        def check_pitch_values(item):
            try:
                item = validate_types(item, types = (PitchParameter))
            except (ValueError, TypeError):
                try:
                    item = validate_types(item, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        item = validators.numeric(item)
                    except (ValueError, TypeError):
                        item = validators.string(item)
            
            return item
            
        if value is None:
            self._pitch = None
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
            self._pitch = [check_pitch_values(x) for x in value]
        else:
            self._pitch = check_pitch_values(value)
    
    @property
    def play_delay(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The number of milliseconds to wait before playing, which comes in addition to the time determined by
        the :meth:`.time <highcharts_core.options.sonification.mapping.SonificationMapping.time>` property.
        
        .. tip::
        
          Can also be negative, which can cause the audio to play *before* the mapped time.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._play_delay
    
    @play_delay.setter
    def play_delay(self, value):
        if value is None:
            self._play_delay = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._play_delay = value
    
    @property
    def rate(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """Mapping configuration for the speech rate multiplier.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._rate
    
    @rate.setter
    def rate(self, value):
        if value is None:
            self._rate = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._rate = value
    
    @property
    def text(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """Mapping configuration for the text parameter for speech tracks.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._text
    
    @text.setter
    def text(self, value):
        if value is None:
            self._text = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._text = value
    
    @property
    def time(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The offset, expressed in milliseconds, which determines when audio for a point is played (e.g. a value of 
        ``'0'`` means it plays immediately when the chart is sonified).
        
        By default, it is mapped to the ``'x'`` property, which means that points with the lowest ``'x'`` values will 
        play first, while points with the highest value will play last.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._time
    
    @time.setter
    def time(self, value):
        if value is None:
            self._time = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._time = value
    
    @property
    def tremolo(self) -> Optional[TremoloEffect]:
        """Mapping options for a :term:`tremolo` effect.
        
        :rtype: :class:`TremoloEffect <highcharts_core.options.sonification.mapping.TremoloEffect>` or 
          :obj:`None <python:None>`
        """
        return self._tremolo

    @tremolo.setter
    def tremolo(self, value):
        if value is None:
            self._tremolo = None
        else:
            try:
                value = validate_types(value, types = (TremoloEffect))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        value = validators.string(value)

            self._tremolo = value

    @property
    def volume(self) -> Optional[AudioParameter | CallbackFunction | str | int | float | Decimal]:
        """The volume at which to play notes, expressed from ``0`` (muted) to ``1``.
        
        :rtype: :class:`AudioParameter <highcharts_core.options.sonification.mapping.AudioParameter>` or
          :class:`CallbackFunction <highcharts_core.utility_functions.javascript_functions.CallbackFunction>` or
          :class:`str <python:str>` or numeric or :obj:`None <python:None>`
        """
        return self._volume
    
    @volume.setter
    def volume(self, value):
        if value is None:
            self._volume = None
        else:
            try:
                value = validate_types(value, types = (AudioParameter))
            except (ValueError, TypeError):
                try:
                    value = validate_types(value, types = (CallbackFunction))
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value,
                                                   minimum = 0,
                                                   maximum = 1)
                    except (ValueError, TypeError):
                        value = validators.string(value)
                        
            self._volume = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'frequency': as_dict.get('frequency', None),
            'gap_between_notes': as_dict.get('gapBetweenNotes', None),
            'highpass': as_dict.get('highpass', None),
            'lowpass': as_dict.get('lowpass', None),
            'note_duration': as_dict.get('noteDuration', None),
            'pan': as_dict.get('pan', None),
            'pitch': as_dict.get('pitch', None),
            'play_delay': as_dict.get('playDelay', None),
            'rate': as_dict.get('rate', None),
            'text': as_dict.get('text', None),
            'time': as_dict.get('time', None),
            'tremolo': as_dict.get('tremolo', None),
            'volume': as_dict.get('volume', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'frequency': self.frequency,
            'gapBetweenNotes': self.gap_between_notes,
            'highpass': self.highpass,
            'lowpass': self.lowpass,
            'noteDuration': self.note_duration,
            'pan': self.pan,
            'pitch': self.pitch,
            'playDelay': self.play_delay,
            'rate': self.rate,
            'text': self.text,
            'time': self.time,
            'tremolo': self.tremolo,
            'volume': self.volume,
        }

        return untrimmed
