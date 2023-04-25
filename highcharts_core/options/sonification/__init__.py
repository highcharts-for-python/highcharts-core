from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.decorators import class_sensitive
from highcharts_core.options.sonification.track_configurations import (InstrumentTrackConfiguration,
                                                                       SpeechTrackConfiguration,
                                                                       ContextTrackConfiguration)
from highcharts_core.options.sonification.grouping import SonificationGrouping
from highcharts_core.utility_classes.events import SonificationEvents


class SonificationOptions(HighchartsMeta):
    """Options for configuring sonification and audio charts."""
    
    def __init__(self, **kwargs):
        self._after_series_wait = None
        self._default_instrument_options = None
        self._default_speech_options = None
        self._duration = None
        self._enabled = None
        self._events = None
        self._global_context_tracks = None
        self._global_tracks = None
        self._master_volume = None
        self._order = None
        self._point_grouping = None
        self._show_crosshair = None
        self._show_tooltip = None
        self._update_interval = None
        
        self.after_series_wait = kwargs.get('after_series_wait', None)
        self.default_instrument_options = kwargs.get('default_instrument_options', None)
        self.default_speech_options = kwargs.get('default_speech_options', None)
        self.duration = kwargs.get('duration', None)
        self.enabled = kwargs.get('enabled', None)
        self.events = kwargs.get('events', None)
        self.global_context_tracks = kwargs.get('global_context_tracks', None)
        self.global_tracks = kwargs.get('global_tracks', None)
        self.master_volume = kwargs.get('master_volume', None)
        self.order = kwargs.get('order', None)
        self.point_grouping = kwargs.get('point_grouping', None)
        self.show_crosshair = kwargs.get('show_crosshair', None)
        self.show_tooltip = kwargs.get('show_tooltip', None)
        self.update_interval = kwargs.get('update_interval', None)
        
    @property
    def after_series_wait(self) -> Optional[int | float | Decimal]:
        """The time to wait in milliseconds after each data series when playing the visualization's data series 
        in sequence. Defaults to ``700``.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._after_series_wait
    
    @after_series_wait.setter
    def after_series_wait(self, value):
        self._after_series_wait = validators.numeric(value,
                                                     allow_empty = True,
                                                     minimum = 0)
    
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
    def duration(self) -> Optional[int | float | Decimal]:
        """The total duration of the sonification, expressed in milliseconds. Defaults to ``6000``.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._duration
    
    @duration.setter
    def duration(self, value):
        self._duration = validators.numeric(value, allow_empty = True, minimum = 0)
        
    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables sonification functionality on the chart. Defaults to ``True``.
        
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
    def events(self) -> Optional[SonificationEvents]:
        """Event handlers for sonification.
        
        :rtype: :class:`SonificationEvents <highcharts_core.utility_classes.events.SonificationEvents>` or
          :obj:`None <python:None>`
        """
        return self._events
    
    @events.setter
    @class_sensitive(SonificationEvents)
    def events(self, value):
        self._events = value
        
    @property
    def global_context_tracks(self) -> Optional[ContextTrackConfiguration]:
        """Context tracks to add globally, an array of either instrument tracks, speech tracks, or a mix.
        
        .. note::
        
          Context tracks are not tied to data points, but play at a set interval - either based on ``time`` or on 
          ``prop`` values.
          
        :rtype: :class:`ContextTrackConfiguration <highcharts_core.options.sonification.track_configurations.ContextTrackConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._global_context_tracks
    
    @global_context_tracks.setter
    @class_sensitive(ContextTrackConfiguration)
    def global_context_tracks(self, value):
        self._global_context_tracks = value
        
    @property
    def global_tracks(self) -> Optional[InstrumentTrackConfiguration]:
        """Global tracks to add to every series.
        
        :rtype: :class:`InstrumentTrackConfiguration <highcharts_core.options.sonification.track_configurations.InstrumentTrackConfiguration>`
          or :obj:`None <python:None>`
        """
        return self._global_tracks
    
    @global_tracks.setter
    @class_sensitive(InstrumentTrackConfiguration)
    def global_tracks(self, value):
        self._global_tracks = value

    @property
    def master_volume(self) -> Optional[int | float | Decimal]:
        """The overall/master volume for the sonification, from ``0`` to ``1``. Defaults to ``0.7``.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._master_volume
    
    @master_volume.setter
    def master_volume(self, value):
        self._master_volume = validators.numeric(value, 
                                                 allow_empty = True,
                                                 minimum = 0,
                                                 maximum = 1)
    
    @property
    def order(self) -> Optional[str]:
        """The order in which to play the sonification for data series. Accepts either:
        
          * ``'sequential'`` where the series play individually one after the other or
          * ``'simultaneous'`` where the series play at the same time
          
        Defaults to ``'sequential'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._order
    
    @order.setter
    def order(self, value):
        if not value:
            self._order = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['sequential', 'simultaneous']:
                raise errors.HighchartsValueError(f'.order expects either "sequential" or "simultaenous". '
                                                  f'Received: "{value}"')
            
            self._order = value
            
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
    def show_crosshair(self) -> Optional[bool]:
        """If ``True``, show X and Y crosshairs (if defined on the chart) as the sonification plays. Defaults to 
        ``True``.
        
        .. warning::
        
           If multiple tracks that play at different times try to show crosshairs, it can be glitchy. Therefore,
           it is recommended in those cases to turn this on/off for individual tracks using the ``.show_play_marker`` 
           property.
           
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_crosshair
    
    @show_crosshair.setter
    def show_crosshair(self, value):
        if value is None:
            self._show_crosshair = None
        else:
            self._show_crosshair = bool(value)
            
    @property
    def show_tooltip(self) -> Optional[bool]:
        """If ``True``, show tooltips as the sonification plays. Defaults to ``True``.
        
        .. warning::
        
           If multiple tracks that play at different times try to show tooltips, it can be glitchy. Therefore,
           it is recommended in those cases to turn this on/off for individual tracks using the ``.show_play_marker`` 
           property.
           
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_tooltip
    
    @show_tooltip.setter
    def show_tooltip(self, value):
        if value is None:
            self._show_tooltip = None
        else:
            self._show_tooltip = bool(value)
    
    @property
    def update_interval(self) -> Optional[int | float | Decimal]:
        """The number of milliseconds to wait between each recomputation of the sonification, if the chart updates 
        rapidly. 
        
        .. tip::
        
          This avoids slowing down processes like panning.
          
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._update_interval
    
    @update_interval.setter
    def update_interval(self, value):
        self._update_interval = validators.numeric(value, allow_empty = True, minimum = 0)
        
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'after_series_wait': as_dict.get('afterSeriesWait', None),
            'default_instrument_options': as_dict.get('defaultInstrumentOptions', None),
            'default_speech_options': as_dict.get('defaultSpeechOptions', None),
            'duration': as_dict.get('duration', None),
            'enabled': as_dict.get('enabled', None),
            'events': as_dict.get('events', None),
            'global_context_tracks': as_dict.get('globalContextTracks', None),
            'global_tracks': as_dict.get('globalTracks', None),
            'master_volume': as_dict.get('masterVolume', None),
            'order': as_dict.get('order', None),
            'point_grouping': as_dict.get('pointGrouping', None),
            'show_crosshair': as_dict.get('showCrosshair', None),
            'show_tooltip': as_dict.get('showTooltip', None),
            'update_interval': as_dict.get('updateInterval', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'afterSeriesWait': self.after_series_wait,
            'defaultInstrumentOptions': self.default_instrument_options,
            'defaultSpeechOptions': self.default_speech_options,
            'duration': self.duration,
            'enabled': self.enabled,
            'events': self.events,
            'globalContextTracks': self.global_context_tracks,
            'globalTracks': self.global_tracks,
            'masterVolume': self.master_volume,
            'order': self.order,
            'pointGrouping': self.point_grouping,
            'showCrosshair': self.show_crosshair,
            'showTooltip': self.show_tooltip,
            'updateInterval': self.update_interval,
        }

        return untrimmed
