{
    data: [
        {
          accessibility: {
              description: 'Some description goes here',
              enabled: true
          },
          className: 'some-class-name',
          color: '#ccc',
          colorIndex: 2,
          custom: {
              'some_key': 123,
              'other_key': 456
          },
          description: 'Some description goes here',
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          },
          id: 'some-id-goes-here',
          labelrank: 3,
          name: 'Some Name Goes here',
          selected: false
        },
        {
          accessibility: {
              description: 'Some description goes here',
              enabled: true
          },
          className: 'some-class-name',
          color: '#ccc',
          colorIndex: 2,
          custom: {
              'some_key': 123,
              'other_key': 456
          },
          description: 'Some description goes here',
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          },
          id: 'some-id-goes-here',
          labelrank: 3,
          name: 'Some Name Goes here',
          selected: false
        }
    ],
    id: 'some-id-goes-here',
    index: 3,
    legendIndex: 3,
    name: 'Series Name Goes Here',
    stack: 'stack-id',
    xAxis: 'some-id',
    yAxis: 0,
    zIndex: 3,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',
    
    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ]
}
