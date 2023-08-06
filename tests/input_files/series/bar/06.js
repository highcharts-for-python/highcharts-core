{
  data: [
    {
      direction: 45,
      value: 123,

      dataLabels: {
        align: 'center',
        allowOverlap: true,
        animation: {
            defer: 5
        },
        backgroundColor: {
            linearGradient: {
                x1: 0.123,
                x2: 0.234,
                y1: 0.345,
                y2: 0.456
            },
            stops: [
                [0.12, '#999'],
                [0.34, '#fff']
            ]
        },
        borderColor: '#999999',
        borderRadius: 24,
        borderWidth: 1,
        className: 'some-class-name',
        color: '#000000',
        crop: true,
        defer: false,
        enabled: true,
        filter: {
            operator: '>=',
            property: 'some_property',
            value: 123
        },
        format: 'some format',
        formatter: function() { return true; },
        inside: true,
        nullFormat: 'some format',
        nullFormatter: function() { return true; },
        overflow: 'none',
        padding: 12,
        position: 'center',
        rotation: 0,
        shadow: false,
        shape: 'rect',
        style: 'style goes here',
        useHTML: false,
        verticalAlign: 'top',
        x: 10,
        y: 20,
        z: 0
      },
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
      drilldown: 'some-id-goes-here',
      marker: {
        enabled: true,
        fillColor: '#cccccc',
        height: 24,
        lineWidth: 2,
        radius: 2,
        states: {
            hover: {
                enabled: true
            }
        },
        symbol: 'circle',
        width: 48
      },
      y: 123,
      name: 'some category'
    },
    {
      direction: 45,
      value: 123,

      dataLabels: {
        align: 'center',
        allowOverlap: true,
        animation: {
            defer: 5
        },
        backgroundColor: {
            linearGradient: {
                x1: 0.123,
                x2: 0.234,
                y1: 0.345,
                y2: 0.456
            },
            stops: [
                [0.12, '#999'],
                [0.34, '#fff']
            ]
        },
        borderColor: '#999999',
        borderRadius: 24,
        borderWidth: 1,
        className: 'some-class-name',
        color: '#000000',
        crop: true,
        defer: false,
        enabled: true,
        filter: {
            operator: '>=',
            property: 'some_property',
            value: 123
        },
        format: 'some format',
        formatter: function() { return true; },
        inside: true,
        nullFormat: 'some format',
        nullFormatter: function() { return true; },
        overflow: 'none',
        padding: 12,
        position: 'center',
        rotation: 0,
        shadow: false,
        shape: 'rect',
        style: 'style goes here',
        useHTML: false,
        verticalAlign: 'top',
        x: 10,
        y: 20,
        z: 0
      },
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
      drilldown: 'some-id-goes-here',
      marker: {
        enabled: true,
        fillColor: '#cccccc',
        height: 24,
        lineWidth: 2,
        radius: 2,
        states: {
            hover: {
                enabled: true
            }
        },
        symbol: 'circle',
        width: 48
      },
      y: 123,
      name: 'some category'
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

  dataGrouping: {
    anchor: 'start',
    approximation: 'windbarb',
    dateTimeLabelFormats: {
      day: 'test',
      hour: 'test',
      millisecond: 'test',
      minute: 'test',
      month: 'test',
      second: 'test',
      week: 'test',
      year: 'test'
    },
    enabled: true,
    firstAnchor: 'start',
    forced: true,
    groupAll: true,
    groupPixelWidth: 10,
    lastAnchor: 'end',
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
    ]
  },
  onSeries: 'some-id-goes-here',
  vectorLength: 10,
  xOffset: 5,
  yOffset: 2
}
