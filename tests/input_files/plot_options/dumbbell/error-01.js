{
    animationLimit: 'invalid value',
    colorAxis: 'some-id-goes-here',
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    connectEnds: true,
    connectNulls: false,
    connectorColor: '#777',
    connectorWidth: 1,
    crisp: true,
    cropThreshold: 500,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    dragDrop: {
        draggableHigh: true,
        draggableLow: true,
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
    findNearestPointBy: 'xy',
    getExtremesFromAll: true,
    groupPadding: 12,
    linecap: 'round',
    lineColor: '#ccc',
    lowColor: '#eee',
    negativeColor: '#ee0000',
    negativeFillColor: '#990000',
    pointInterval: 5,
    pointIntervalUnit: 'days',
    pointPadding: 6,
    pointPlacement: 'on',
    pointStart: 12,
    relativeXValue: true,
    shadow: {
      color: '#cccccc',
      offsetX: 10,
      offsetY: 5,
      width: 4
    },
    softThreshold: true,
    stacking: 'normal',
    step: 'right',
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
