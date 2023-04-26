{
    afterSeriesWait: 300,
    defaultInstrumentOptions: {
        instrument: 'piano',
        midiName: 'some-value',
        roundToMusicalNotes: true,
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
                depth: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'
                },
                speed: 0.5
            },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
        pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
        },
        showPlayMarker: true,
        type: 'instrument'
    },
    defaultSpeechOptions: {
        language: 'en-US',
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
                depth: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'
                },
                speed: 0.5
            },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
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
        valueInterval: 5,
        valueMapFunction: 'linear',
        valueProp: 'y',
        midiName: 'some-value',
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
                depth: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'
                },
                speed: 0.5
            },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
        pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
        },
        showPlayMarker: true,
        type: 'instrument'
    },
    globalTracks: {
        instrument: 'piano',
        midiName: 'some-value',
        roundToMusicalNotes: true,
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
                depth: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'
                },
                speed: 0.5
            },
            volume: {
                    mapFunction: 'linear',
                    mapTo: 'y',
                    max: 12345,
                    min: 0,
                    within: 'series'    
                }
        },
        pointGrouping: {
            algorithm: 'minmax',
            enabled: true,
            groupTimespan: 15,
            prop: 'y'
        },
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