{
  dataLabels: 'invalid value',
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

  from: 'some-id-goes-here',
  to: 'some-id-goes-here',

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
