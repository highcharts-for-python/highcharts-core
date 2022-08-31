{
  data: [
      {
        borderColor: '#ccc',
        borderWidth: 2,
        dashStyle: 'Solid',
        pointWidth: 12
      },
      {
        borderColor: '#ccc',
        borderWidth: 2,
        dashStyle: 'Solid',
        pointWidth: 12,

        dataLabels: {
          align: 'center',
          allowOverlap: True,
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
          crop: True,
          defer: False,
          enabled: True,
          filter: {
              operator: '>=',
              property: 'some_property',
              value: 123
          },
          format: 'some format',
          formatter: """function() { return true; }""",
          inside: True,
          nullFormat: 'some format',
          nullFormatter: """function() { return true; }""",
          overflow: 'none',
          padding: 12,
          position: 'center',
          rotation: 0,
          shadow: False,
          shape: 'rect',
          style: 'style goes here',
          useHTML: False,
          verticalAlign: 'top',
          x: 10,
          y: 20,
          z: 0
        },
        dragDrop: {
            draggableX: True,
            draggableY: True,
            dragHandle: {
                className: 'draghandle-classname-goes-here',
                color: '#ccc',
                cursor: 'alias',
                lineColor: '#ddd',
                lineWidth: 2,
                pathFormatter: """function() { return true; }""",
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
            liveRedraw: True
        },
        drilldown: 'some-id-goes-here',
        marker: {
          enabled: True,
          fillColor: '#cccccc',
          height: 24,
          lineWidth: 2,
          radius: 2,
          states: {
              hover: {
                  enabled: True
              }
          },
          symbol: 'circle',
          width: 48
        },
        x: 'some category',
        y: 123
      }
  ],
  id: 'some-id-goes-here',
  index: 'invalid value',
  legendIndex: 3,
  name: 'Series Name Goes Here',
  stack: 'stack-id',
  xAxis: 'some-id',
  yAxis: 0,
  zIndex: 3,

  borderColor: '#ccc',
  borderRadius: 4,
  borderWidth: 2,
  centerInCategory: true,
  colorByPoint: true,
  colors: [
      '#fff',
      '#ccc',
      {
        linearGradient: {
            x1: 0.123,
            x2: 0.567,
            y1: 0.891,
            y2: 0.987
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
      },
      {
        animation: {
            defer: 5
        },
        patternOptions: {
            aspectRatio: 0.5,
            backgroundColor: '#999999',
            id: 'some_id_goes_here',
            opacity: 0.5,
            width: 120,
            x: 5,
            y: 10
        },
        patternIndex: 2
      }
  ],
  grouping: false,
  groupPadding: 6,
  maxPointWidth: 12,
  minPointLength: 12,
  pointPadding: 6,
  pointRange: 24,
  pointWidth: 12
}
