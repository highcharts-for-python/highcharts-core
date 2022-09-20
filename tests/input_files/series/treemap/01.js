{
  data: [
    {
      colorValue: 2,
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
      parent: 'some-id-goes-here',
      value: 123.45,

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
  colorAxis: 'some-id-goes-here',
  negativeColor: '#ccc',
  pointInterval: 5,
  pointIntervalUnit: 'day',
  pointStart: 1,
  stacking: 'normal',
  animationLimit: 10,
  boostBlending: 'some-value-goes-here',
  boostThreshold: 5000,
  colorIndex: 2,
  colorKey: 'some-key-goes-here',
  crisp: true,
  cropThreshold: 500,
  findNearestPointBy: 'xy',
  getExtremesFromAll: true,
  linecap: 'round',
  lineWidth: 1,
  relativeXValue: true,
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
  ],

  allowTraversingTree: true,
  alternateStartingDirection: false,
  breadcrumbs: {
    buttonSpacing: 6,
    buttonTheme: {
        'fill': '#fff'
    },
    events: {
      click: function(event) { return true; }
    },
    floating: true,
    format: 'some format string',
    formatter: function () { return true; },
    relativeTo: 'plot',
    rtl: false,
    separator: {
        style: {
            'some-key': 'some-value'
        },
        text: '>'
    },
    useHTML: false,
    zIndex: 3
  },
  colorByPoint: true,
  colors: [
      '#ccc',
      '#fff',
      '000000'
  ],
  ignoreHiddenPoint: true,
  interactByLeaf: true,
  layoutAlgorithm: 'sliceAndDice',
  layoutStartingDirection: 'vertical',
  levelIsConstant: true,
  levels: [
      {
       borderDashStyle: 'Solid',
       color: '#ccc',
       colorVariation: {
           key: 'brightness',
           to: 50
       },
       layoutAlgorithm: 'sliceAndDice',
       layoutStartingDirection: 'vertical',
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1,
      }
  ],
  sortIndex: 2

}
