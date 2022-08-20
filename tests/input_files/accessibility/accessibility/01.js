{
    announceNewData: {
        announcementFormatter: function() { return true; },
        enabled: true,
        interruptUser: true,
        minimumAnnouncementInterval: 3
    },
    customComponents: {
        'item1': 'some-value-goes-here',
        'item2': 'some_other_value_goes_here'
    },
    description: 'Description goes here',
    enabled: true,
    highContrastTheme: 'something goes here',
    keyboardNavigation: {
        enabled: true,
        focusBorder: {
            enabled: true,
            hideBrowserFocusOutline: false,
            margin: 20,
            style: {
                borderRadius: 2,
                color: '#ccc',
                lineWidth: 1
            }
        },
        order: [
            'series',
            'item1',
            'zoom',
            'container'
        ],
        seriesNavigation: {
            mode: 'normal',
            pointNavigationEnabledThreshold: 20,
            rememberPointFocus: true,
            skipNullPoints: false
        },
        wrapAround: true
    },
    landmarkVerbosity: 'all',
    linkedDescription: 'some-item-goes-here',
    point: {
        dateFormat: 'format string',
        dateFormatter: function() { return true; },
        describeNull: false,
        descriptionFormatter: function() { return true; },
        valueDecimals: 2,
        valueDescriptionFormat: 'format string',
        valuePrefix: '$',
        valueSuffix: 'USD'
    },
    screenReaderSection: {
        afterChartFormat: 'format string',
        afterChartFormatter: function() { return true; },
        axisRangeDateFormat: 'format string',
        beforeChartFormat: 'format string',
        beforeChartFormatter: function() { return true; },
        onPlayAsSoundClick: function() { return true; },
        onViewDataTableClick: function() { return true; }
    },
    series: {
        describeSingleSeries: true,
        descriptionFormat: 'format string goes here',
        descriptionFormatter: function() { return true; },
        pointDescriptionEnabledThreshold: 100
    },
    typeDescription: 'some description goes here'
  }
