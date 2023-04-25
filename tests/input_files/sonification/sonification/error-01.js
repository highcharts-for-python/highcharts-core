{
    afterSeriesWait: 'invalid-value',
    defaultInstrumentOptions: {
        activeWhen: {
            crossingDown: 2,
            crossingUp: 3,
            max: 5,
            min: 1,
            prop: 'y'    
        },
        instrument: 'piano',
        mapping: {
            frequency: 3,
            gapBetweenNotes: 5,
            highpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            lowpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            noteDuration: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pan: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pitch: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            playDelay: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            time: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            tremolo: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
        midiName: 'some-value',
        pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
        },
        roundToMusicalNotes: true,
        showPlayMarker: true,
        type: 'instrument'
    },
    defaultSpeechOptions: {
        activeWhen: {
            crossingDown: 2,
            crossingUp: 3,
            max: 5,
            min: 1,
            prop: 'y'    
        },
        language: 'en-US',
        mapping: {
            frequency: 3,
            gapBetweenNotes: 5,
            highpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            lowpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            noteDuration: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pan: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pitch: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            playDelay: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            time: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            tremolo: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
        midiName: 'some-value',
        pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
        },
        showPlayMarker: true,
        type: 'speech'
    },
    duration: 6000,
    enabled: true,
    events: {
        afterUpdate: function() { return true; },
        beforePlay: function() { return true; },
        beforeUpdate: function() { return true; },
        onBoundaryHit: function() { return true; },
        onEnd: function() { return true; },
        onPlay: function() { return true; },
        onSeriesEnd: function() { return true; },
        onSeriesStart: function() { return true; },
        onStop: function() { return true; }
    },
    globalContextTracks: {
        activeWhen: {
            crossingDown: 2,
            crossingUp: 3,
            max: 5,
            min: 1,
            prop: 'y'    
        },
        mapping: {
            frequency: 3,
            gapBetweenNotes: 5,
            highpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            lowpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            noteDuration: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pan: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pitch: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            playDelay: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            time: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            tremolo: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
        midiName: 'some-value',
        pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
        },
        showPlayMarker: true,
        type: 'instrument',
        value_interval: 5,
        valueMapFunction: 'linear',
        valueProp: 'y'    
    },
    globalTracks: {
        activeWhen: {
            crossingDown: 2,
            crossingUp: 3,
            max: 5,
            min: 1,
            prop: 'y'    
        },
        instrument: 'piano',
        mapping: {
            frequency: 3,
            gapBetweenNotes: 5,
            highpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            lowpass: {
                frequency: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
                resonance: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
            },
            noteDuration: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pan: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            pitch: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            playDelay: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            time: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            tremolo: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
        midiName: 'some-value',
        pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
        },
        roundToMusicalNotes: true,
        showPlayMarker: true,
        type: 'instrument'
    },
    masterVolume: 0.5,
    order: 'sequential',
    pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
    },
    showCrosshair: true,
    showTooltip: true,
    updateInterval: 200
}