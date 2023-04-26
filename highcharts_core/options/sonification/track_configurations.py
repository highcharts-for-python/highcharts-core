from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors, constants
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.utility_functions import mro__to_untrimmed_dict
from highcharts_core.utility_classes.javascript_functions import CallbackFunction
from highcharts_core.options.sonification.mapping import SonificationMapping
from highcharts_core.options.sonification.grouping import SonificationGrouping


class ActiveWhen(HighchartsMeta):
    """Definition of the condition for when a track should be active or not."""
    
    def __init__(self, **kwargs):
        self._crossing_down = None
        self._crossing_up = None
        self._max = None
        self._min = None
        self._prop = None
        
        self.crossing_down = kwargs.get('crossing_down', None)
        self.crossing_up = kwargs.get('crossing_up', None)
        self.max = kwargs.get('max', None)
        self.min = kwargs.get('min', None)
        self.prop = kwargs.get('prop', None)
        
    @property
    def crossing_down(self) -> Optional[int | float | Decimal]:
        """Track will be active when the property indicated by
        :meth:`.prop <highcharts_core.options.sonification.track_configurations.ActiveWhen.prop>` is
        at or *below* this value. Defaults to :obj:`None <python:None>`.
        
        .. warning::
        
          If both ``.crossing_down`` and 
          :meth:`.crossing_up <highcharts_core.options.sonification.track_configurations.ActiveWhen.crossing_up>` are 
          defined, the track will be active if either condition is met.
          
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._crossing_down
    
    @crossing_down.setter
    def crossing_down(self, value):
        self._crossing_down = validators.numeric(value, allow_empty = True)
        
    @property
    def crossing_up(self) -> Optional[int | float | Decimal]:
        """Track will be active when the property indicated by
        :meth:`.prop <highcharts_core.options.sonification.track_configurations.ActiveWhen.prop>` is
        at or *above* this value. Defaults to :obj:`None <python:None>`.
        
        .. warning::
        
          If both ``.crossing_up`` and 
          :meth:`.crossing_down <highcharts_core.options.sonification.track_configurations.ActiveWhen.crossing_down>` 
          are defined, the track will be active if either condition is met.
          
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._crossing_up
    
    @crossing_up.setter
    def crossing_up(self, value):
        self._crossing_up = validators.numeric(value, allow_empty = True)
    
    @property
    def max(self) -> Optional[int | float | Decimal]:
        """Track will be active when the property indicated by
        :meth:`.prop <highcharts_core.options.sonification.track_configurations.ActiveWhen.prop>` is
        at or *below* this value. Defaults to :obj:`None <python:None>`.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max
    
    @max.setter
    def max(self, value):
        self._max = validators.numeric(value, allow_empty = True)
        
    @property
    def min(self) -> Optional[int | float | Decimal]:
        """Track will be active when the property indicated by
        :meth:`.prop <highcharts_core.options.sonification.track_configurations.ActiveWhen.prop>` is
        at or *above* this value. Defaults to :obj:`None <python:None>`.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min
    
    @min.setter
    def min(self, value):
        self._min = validators.numeric(value, allow_empty = True)
        
    @property
    def prop(self) -> Optional[str]:
        """The data point property to use when evaluating the condition, for example ``'y'`` or ``'x'``.
        Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._prop
    
    @prop.setter
    def prop(self, value):
        self._prop = validators.string(value, allow_empty = True)
        
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'crossing_down': as_dict.get('crossingDown', None),
            'crossing_up': as_dict.get('crossingUp', None),
            'max': as_dict.get('max', None),
            'min': as_dict.get('min', None),
            'prop': as_dict.get('prop', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'crossingDown': self.crossing_down,
            'crossingUp': self.crossing_up,
            'max': self.max,
            'min': self.min,
            'prop': self.prop,
        }

        return untrimmed


class TrackConfigurationBase(HighchartsMeta):
    """Base class for use in configuring Sonification tracks."""
    
    def __init__(self, **kwargs):
        self._active_when = None
        self._mapping = None
        self._midi_name = None
        self._point_grouping = None
        self._show_play_marker = None
        self._type = None
        
        self.active_when = kwargs.get('active_when', None)
        self.mapping = kwargs.get('mapping', None)
        self.midi_name = kwargs.get('midi_name', None)
        self.point_grouping = kwargs.get('point_grouping', None)
        self.show_play_marker = kwargs.get('show_play_marker', None)
        self.type = kwargs.get('type', None)
        
    @property
    def active_when(self) -> Optional[ActiveWhen | CallbackFunction]:
        """The condition for when a track should be active or not.
        
        Accepts either a (Javascript) 
        :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or an
        :class:`ActiveWhen <highcharts_core.options.sonification.track_configurations.ActiveWhen>` configuration object.
        
        .. note::

          If a callback function is used, it should return a boolean for whether or not the track should be active. 
          
          The function is called for each audio event, and receives a parameter object with ``time``, and potentially 
          ``point`` and ``value`` properties depending on the track. 
          
          ``point`` is available if the audio event is related to a data point. 
          
          ``value`` is available if the track is used as a context track, and 
          :meth:`.value_interval <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration.value_interval>` 
          is used.
          
        :rtype: :class:`ActiveWhen <highcharts_core.options.sonification.track_configurations.ActiveWhen>` or
          :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>` or
          :obj:`None <python:None>`.
        """
        return self._active_when
    
    @active_when.setter
    def active_when(self, value):
        if not value:
            self._active_when = None
        else:
            try:
                value = validate_types(value, types = (ActiveWhen))
            except (ValueError, TypeError):
                value = validate_types(value, types = (CallbackFunction))
            
            self._active_when = value

    @property
    def mapping(self) -> Optional[SonificationMapping]:
        """Mapping options for the audio parameter.
        
        :rtype: :class:`SonificationMapping <highcharts_core.options.sonification.mapping.SonificationMapping>` or
          :obj:`None <python:None>`
        """
        return self._mapping
    
    @mapping.setter
    @class_sensitive(SonificationMapping)
    def mapping(self, value):
        self._mapping = value
        
    @property
    def point_grouping(self) -> Optional[SonificationGrouping]:
        """Options for configurign the grouping of points.
        
        :rtype: :class:`SonificationGrouping <highcharts_core.options.sonification.grouping.SonificationGrouping>` or
          :obj:`None <python:None>`
        """
        return self._point_grouping
    
    @point_grouping.setter
    @class_sensitive(SonificationGrouping)
    def point_grouping(self, value):
        self._point_grouping = value
        
    @property
    def show_play_marker(self) -> Optional[bool]:
        """If ``True``, displays the play marker (tooltip and/or crosshair) for a track. Defaults to ``True``.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_play_marker
    
    @show_play_marker.setter
    def show_play_marker(self, value):
        if value is None:
            self._show_play_marker = None
        else:
            self._show_play_marker = bool(value)
            
    @property
    def type(self) -> Optional[str]:
        """The type of track. Accepts either ``'instrument'`` or ``'speech'``. Defaults to ``'instrument'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type
    
    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['instrument', 'speech']:
                raise errors.HighchartsValueError(f'type expects either "instrument" or "speech". '
                                                  f'Received: "{value}"')
            self._type = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'active_when': as_dict.get('activeWhen', None),
            'mapping': as_dict.get('mapping', None),
            'midi_name': as_dict.get('midiName', None) or as_dict.get('MIDIName', None),
            'point_grouping': as_dict.get('pointGrouping', None),
            'show_play_marker': as_dict.get('showPlayMarker', None),
            'type': as_dict.get('type', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'activeWhen': self.active_when,
            'mapping': self.mapping,
            'midiName': self.midi_name,
            'pointGrouping': self.point_grouping,
            'showPlayMarker': self.show_play_marker,
            'type': self.type,
        }

        return untrimmed


class InstrumentTrackConfiguration(TrackConfigurationBase):
    """Configuration of an Instrument Track for use in sonification."""
    
    def __init__(self, **kwargs):
        self._instrument = None
        self._round_to_musical_notes = None
        
        self.instrument = kwargs.get('instrument', None)
        self.round_to_musical_notes = kwargs.get('round_to_musical_notes', None)
        
        super().__init__(**kwargs)
        
    @property
    def instrument(self) -> Optional[str]:
        """The instrument to use for playing. Defaults to ``'piano'``.
        
        Accepts:

          * ``'flute'``
          * ``'saxophone'``
          * ``'trumpet'``
          * ``'sawsynth'``
          * ``'wobble'``
          * ``'basic1'``
          * ``'basic2'``
          * ``'sine'``
          * ``'sineGlide'``
          * ``'triangle'``
          * ``'square'``
          * ``'sawtooth'``
          * ``'noise'``
          * ``'filteredNoise'``
          * ``'wind'``
          
        :rtype: :class:`str <python:str>`
        """
        return self._instrument
    
    @instrument.setter
    def instrument(self, value):
        if not value:
            self._instrument = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.INSTRUMENT_PRESETS:
                raise errors.HighchartsValueError(f'.instrument expects a predefined instrument name. Did not '
                                                  f'recognize: "{value}".')
            self._instrument = value

    @property
    def midi_name(self) -> Optional[str]:
        """The name to use for a track when exporting it to MIDI. If :obj:`None <python:None>`, will
        use the series name if the track is related to a series. Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._midi_name
    
    @midi_name.setter
    def midi_name(self, value):
        self._midi_name = validators.string(value, allow_empty = True)
        
    @property
    def round_to_musical_notes(self) -> Optional[bool]:
        """If ``True``, will round pitch matching to musical notes in 440Hz standard tuning. If ``False``,
        will play the exact mapped/configured note even if it is out of tune as per standard tuning. Defaults to ``True``.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._round_to_musical_notes
    
    @round_to_musical_notes.setter
    def round_to_musical_notes(self, value):
        if value is None:
            self._round_to_musical_notes = None
        else:
            self._round_to_musical_notes = bool(value)
            
    @property
    def type(self) -> Optional[str]:
        """The type of track.
        
        .. note::
        
          In the context of an :class:`InstrumentTrackConfiguration`, this will *always* return ``'instrument'`` if
          not :obj:`None <python:None>`.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if self._instrument:
            return 'instrument'
        
        return None
    
    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['instrument', 'speech']:
                raise errors.HighchartsValueError(f'type expects either "instrument" or "speech". '
                                                  f'Received: "{value}"')
            self._type = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'active_when': as_dict.get('activeWhen', None),
            'mapping': as_dict.get('mapping', None),
            'point_grouping': as_dict.get('pointGrouping', None),
            'show_play_marker': as_dict.get('showPlayMarker', None),
            'type': as_dict.get('type', None),
            
            'instrument': as_dict.get('instrument', None),
            'midi_name': as_dict.get('midiName', None) or as_dict.get('MIDIName', None),
            'round_to_musical_notes': as_dict.get('roundToMusicalNotes', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'instrument': self.instrument,
            'midiName': self.midi_name,
            'roundToMusicalNotes': self.round_to_musical_notes,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class SpeechTrackConfiguration(TrackConfigurationBase):
    """Configuration of a Speech Track for use in sonification."""
    
    def __init__(self, **kwargs):
        self._language = None
        self._preferred_voice = None
        
        self.language = kwargs.get('language', None)
        self.preferred_voice = kwargs.get('preferred_voice', None)
        
        super().__init__(**kwargs)
        
    @property
    def language(self) -> Optional[str]:
        """The language to speak in for speech tracks, as an `IETF BCP 47 <https://www.rfc-editor.org/info/bcp47>`__ 
        language tag. Defaults to ``'en-US'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._language
    
    @language.setter
    def language(self, value):
        self._language = validators.string(value, allow_empty = True)
        
    @property
    def preferred_voice(self) -> Optional[str]:
        """The name of the voice synthesis to prefer for speech tracks. If :obj:`None <python:None>` or
        unavabilable, will fall back to the default voice for the selected language. Defaults to 
        :obj:`None <python:None>`.
          
        .. warning::
        
          Different platforms (operating systems in which your users will view your visualizations)
          provide different voices for web speech synthesis.
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._preferred_voice
    
    @preferred_voice.setter
    def preferred_voice(self, value):
        self._preferred_voice = validators.string(value, allow_empty = True)
        
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'active_when': as_dict.get('activeWhen', None),
            'mapping': as_dict.get('mapping', None),
            'point_grouping': as_dict.get('pointGrouping', None),
            'show_play_marker': as_dict.get('showPlayMarker', None),
            'type': as_dict.get('type', None),
            
            'language': as_dict.get('language', None),
            'preferred_voice': as_dict.get('preferredVoice', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'language': self.language,
            'preferredVoice': self.preferred_voice,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class ContextTrackConfiguration(InstrumentTrackConfiguration, SpeechTrackConfiguration):
    """Configuration of a Context Track for use in sonification."""
    
    def __init__(self, **kwargs):
        self._time_interval = None
        self._value_interval = None
        self._value_map_function = None
        self._value_prop = None
        
        self.time_interval = kwargs.get('time_interval', None)
        self.value_interval = kwargs.get('value_interval', None)
        self.value_map_function = kwargs.get('value_map_function', None)
        self.value_prop = kwargs.get('value_prop', None)
        
        super().__init__(**kwargs)
        
    @property
    def time_interval(self) -> Optional[int | float | Decimal]:
        """Determines the number of milliseconds between playback of a context track. Defaults to 
        :obj:`None <python:None>`.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._time_interval
    
    @time_interval.setter
    def time_interval(self, value):
        self._time_interval = validators.numeric(value, allow_empty = True)

    @property
    def value_interval(self) -> Optional[int | float | Decimal]:
        """Determines the number of units between playback of a context track, where
        units are determined by :meth:`.value_prop <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration.value_prop>`.
        
        For example, setting 
        :meth:`.value_prop <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration.value_prop>` 
        to ``'x'`` and ``.value_interval`` to ``5`` means the context track
        should be played for every 5th value of ``'x'``.
        
        .. note::
        
          The context audio events will be mapped to time according to the prop value relative to the min/max values 
          for that prop.
          
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value_interval
    
    @value_interval.setter
    def value_interval(self, value):
        self._value_interval = validators.numeric(value, allow_empty = True)
        
    @property
    def value_map_function(self) -> Optional[str]:
        """Determines how to map context events to time when using the 
        :meth:`.value_interval <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration.value_interval>`
        property. Accepts either ``'linear'`` or ``'logarithmic'``. Defaults to ``'linear'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value_map_function
    
    @value_map_function.setter
    def value_map_function(self, value):
        if not value:
            self._value_map_function = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['linear', 'logarithmic']:
                raise errors.HighchartsValueError(f'value_map_function expects either "linear" or '
                                                  f'"logarithmic. Received: "{value}"')
            
            self._value_map_function = value
            
    @property
    def value_prop(self) -> Optional[str]:
        """The data point property to use when evaluating whether to play the context track in conjunction with 
        :meth:`.value_interval <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration.value_interval>`
        Defaults to :obj:`None <python:None>`.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._value_prop
    
    @value_prop.setter
    def value_prop(self, value):
        self._value_prop = validators.string(value, allow_empty = True)

    @property
    def type(self) -> Optional[str]:
        """The type of track. Accepts either ``'instrument'`` or ``'speech'``. Defaults to ``'instrument'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['instrument', 'speech']:
                raise errors.HighchartsValueError(f'type expects either "instrument" or "speech". '
                                                  f'Received: "{value}"')
            self._type = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'active_when': as_dict.get('activeWhen', None),
            'mapping': as_dict.get('mapping', None),
            'point_grouping': as_dict.get('pointGrouping', None),
            'show_play_marker': as_dict.get('showPlayMarker', None),
            'type': as_dict.get('type', None),
            
            'instrument': as_dict.get('instrument', None),
            'midi_name': as_dict.get('midiName', None) or as_dict.get('MIDIName', None),
            'round_to_musical_notes': as_dict.get('roundToMusicalNotes', None),

            'language': as_dict.get('language', None),
            'preferred_voice': as_dict.get('preferredVoice', None),
            
            'time_interval': as_dict.get('timeInterval', None),
            'value_interval': as_dict.get('valueInterval', None),
            'value_map_function': as_dict.get('valueMapFunction', None),
            'value_prop': as_dict.get('valueProp', None),
            
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'timeInterval': self.time_interval,
            'valueInterval': self.value_interval,
            'valueMapFunction': self.value_map_function,
            'valueProp': self.value_prop,
        }

        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed