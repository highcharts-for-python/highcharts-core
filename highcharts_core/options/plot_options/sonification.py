from typing import Optional, List

from validator_collection import validators, checkers

from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core.options.sonification.track_configurations import (InstrumentTrackConfiguration,
                                                                       SpeechTrackConfiguration,
                                                                       ContextTrackConfiguration)
from highcharts_core.options.sonification.grouping import SonificationGrouping


class SeriesSonification(HighchartsMeta):
    """Sonification/audio chart options for a series."""
    
    def __init__(self, **kwargs):
        self._context_tracks = None
        self._default_instrument_options = None
        self._default_speech_options = None
        self._enabled = None
        self._point_grouping = None
        self._tracks = None
        
        self.context_tracks = kwargs.get('context_tracks', None)
        self.default_instrument_options = kwargs.get('default_instrument_options', None)
        self.default_speech_options = kwargs.get('default_speech_options', None)
        self.enabled = kwargs.get('enabled', None)
        self.point_grouping = kwargs.get('point_grouping', None)
        self.tracks = kwargs.get('tracks', None)
        
    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.series.sonification'

    @property
    def context_tracks(self) -> Optional[ContextTrackConfiguration | List[ContextTrackConfiguration]]:
        """Context tracks for the series. Context tracks are not tied to data points.
        
        :rtype: :class:`ContextTrackConfiguration <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration>` 
          or :class:`list <python:list>` of track configuration types
        """
        return self._context_tracks
    
    @context_tracks.setter
    def context_tracks(self, value):
        if not value:
            self._context_tracks = None
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
                self._context_tracks = [validate_types(x, types = (ContextTrackConfiguration)) for x in value]
        else:
            value = validate_types(value, types = ContextTrackConfiguration)
            self._context_tracks = value
    
    @property
    def default_instrument_options(self) -> Optional[InstrumentTrackConfiguration]:
        """Default sonification options for all instrument tracks.

        .. warning::
        
          If specific options are also set on individual tracks or per-series, this configuration will be *overridden*.
        
        :rtype: :class:`InstrumentTrackConfiguration <highcharts_core.options.sonification.track_configurations.InstrumentTrackConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._default_instrument_options
    
    @default_instrument_options.setter
    @class_sensitive(InstrumentTrackConfiguration)
    def default_instrument_options(self, value):
        self._default_instrument_options = value
        
    @property
    def default_speech_options(self) -> Optional[SpeechTrackConfiguration]:
        """Default sonification options for all speech tracks.
        .. warning::
        
          If specific options are also set on individual tracks or per-series, this configuration will be *overridden*.
        
        :rtype: :class:`SpeechTrackConfiguration <highcharts_core.options.sonification.track_configurations.SpeechTrackConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._default_speech_options
    
    @default_speech_options.setter
    @class_sensitive(SpeechTrackConfiguration)
    def default_speech_options(self, value):
        self._default_speech_options = value
        
    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, sonification will be enabled for the series.
        
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
    def point_grouping(self) -> Optional[SonificationGrouping]:
        """Options for grouping data points together when sonifying. 
        
        This allows for the visual presentation to contain more points than what is being played. 
        
        If not enabled, all visible / uncropped points are played.
        
        :rtype: :class:`SonificationGrouping <highcharts_core.options.sonification.grouping.SonificationGrouping>` or
          :obj:`None <python:None>`
        """
        return self._point_grouping
    
    @point_grouping.setter
    @class_sensitive(SonificationGrouping)
    def point_grouping(self, value):
        self._point_grouping = value
        
    @property
    def tracks(self) -> Optional[ContextTrackConfiguration | List[ContextTrackConfiguration]]:
        """Tracks for the series.
        
        :rtype: :class:`ContextTrackConfiguration <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration>` 
          or :class:`list <python:list>` of 
          :class:`ContextTrackConfiguration <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._tracks
    
    @tracks.setter
    def tracks(self, value):
        if not value:
            self._tracks = None
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
            self._tracks = [validate_types(x, types = (ContextTrackConfiguration)) for x in value]
        else:
            self._tracks = validate_types(value, types = (ContextTrackConfiguration))

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'context_tracks': as_dict.get('contextTracks', None),
            'default_instrument_options': as_dict.get('defaultInstrumentOptions', None),
            'default_speech_options': as_dict.get('defaultSpeechOptions', None),
            'enabled': as_dict.get('enabled', None),
            'point_grouping': as_dict.get('pointGrouping', None),
            'tracks': as_dict.get('tracks', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'contextTracks': self.context_tracks,
            'defaultInstrumentOptions': self.default_instrument_options,
            'defaultSpeechOptions': self.default_speech_options,
            'enabled': self.enabled,
            'pointGrouping': self.point_grouping,
            'tracks': self.tracks,
        }

        return untrimmed
