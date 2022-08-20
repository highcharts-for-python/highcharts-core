{
    crosshair: {
        className: 'some-class-name',
        color: '#ccc',
        dashStyle: 'Dash',
        snap: True,
        width: 40,
        zIndex: 6
    },
    height: 60,
    left: 'not a valid value',
    lineColor: '#999',
    lineWidth: 1,
    showEmpty: True,
    top: 340,
    width: 300,

    accessibility: {
         description: 'Description goes here',
         enabled: true,
         rangeDescription: 'Range description goes here'
     },
     angle: 15,
     ceiling: 120,
     className: 'some-class-name',
     endOnTick: false,
     events: {
       afterBreaks: function(event) { return true; },
       afterSetExtremes: function(event) { return true; },
       pointBreak: function(event) { return true; },
       setExtremes: function(event) { return true; }
     },
     floor: 0,
     gridLineColor: '#ccc',
     gridLineDashStyle: 'Solid',
     gridLineInterpolation: 'circle',
     gridLineWidth: 1,
     gridZIndex: 3,
     id: 'some-id',
     labels: {
         align: 'center',
         allowOverlap: false,
         autoRotation: [-45],
         autoRotationLimit: 80,
         distance: 12,
         enabled: true,
         format: 'some format string',
         formatter: function () { return true; },
         overflow: 'allow',
         padding: 12,
         position3d: 'offset',
         reserveSpace: true,
         rotation: 24,
         skew3d: false,
         staggerLines: 0,
         step: 2,
         style: 'some-style-string',
         useHTML: false,
         x: 5,
         y: -10,
         zIndex: 6
     },
     margin: 12,
     max: 1000,
     maxPadding: 12,
     min: 0,
     minorGridLineColor: '#999',
     minorGridLineDashStyle: 'Dash',
     minorGridLineWidth: 1,
     minorTickColor: '#ccc',
     minorTickInterval: 0.1,
     minorTickPosition: 'outside',
     minorTicks: true,
     minorTickWidth: 1,
     minPadding: 8,
     panningEnabled: true,
     reversed: false,
     showFirstLabel: true,
     showLastLabel: true,
     softMax: 10,
     softMin: 6,
     startOfWeek: 1,
     startOnTick: false,
     tickAmount: 5,
     tickColor: '#000',
     tickInterval: 5,
     tickLength: 8,
     tickmarkPlacement: 'on',
     tickPixelInterval: 8,
     tickPosition: 'outside',
     tickPositioner: function() { return true; },
     tickWidth: 1,
     type: 'linear',
     uniqueNames: true,
     units: [
         [
             'millisecond',
             [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
         ],
         [
             'second',
             [1, 2, 5, 10, 15, 30]
         ],
         [
             'minute',
             [1, 2, 5, 10, 15, 30]
         ],
         [
             'hour',
             [1, 2, 3, 4, 6, 8, 12]
         ],
         [
             'day',
             [1]
         ],
         [
             'week',
             [1]
         ],
         [
             'month',
             [1, 3, 6]
         ],
         [
             'year',
             null
         ]
     ],
     visible: true,
     zIndex: 3
}
