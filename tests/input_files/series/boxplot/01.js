{
  boxDashStyle: 'Solid',
  dragDrop: {
      draggableHigh: true,
      draggableLow: true,
      draggableQ1: true,
      draggableQ3: true,
      draggableX: true,
      draggableY: true,
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
      liveRedraw: true
  },
  medianColor: '#ccc',
  medianDashStyle: 'Dash',
  medianWidth: 2,
  stemDashStyle: 'Solid',
  stemWidth: 1,
  whiskerColor: '#999',
  whiskerDashStyle: 'Solid',
  whiskerLength: 12,
  whiskerWidth: 2
}
