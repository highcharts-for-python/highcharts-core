{
  data: [
    'invalid value',
    {
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
  displayNegative: false,
  maxSize: 'invalid value',
  minSize: 12,
  parentNode: {
      allowPointSelect: true
  },
  sizeBy: 'area',
  useSimulation: true,
  zThreshold: 246

  colorIndex: 3,
  crisp: true,
  draggable: true,
  findNearestPointBy: 'xy',
  layoutAlgorithm: {
      approximation: 'barnes-hut',
      attractiveForce: function() { return true; },
      enableSimulation: true,
      friction: 0.98,
      gravitationalConstant: 0.0625,
      initialPositionRadius: 1,
      initialPositions: 'circle',
      integration: 'euler',
      linkLength: 12,
      maxIterations: 1000,
      maxSpeed: 10,
      repulsiveForce: function() { return true; },
      theta: 0.5,
      type: 'reingold-fruchterman'
  },
  lineWidth: 2,
  link: {
      color: '#ccc',
      dashStyle: 'Solid',
      width: 1
  },
  relativeXValue: true,
  shadow: false,
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

  accessibility: {
      description: 'Description goes here',
      enabled: true,
      exposeAsGroupOnly: true,
      keyboardNavigation: {
          enabled: true
      },
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
  },
  allowPointSelect: true,
  animation: {
      defer: 5
  },
  className: 'some-class-name',
  clip: false,
  color: '#fff',
  cursor: 'alias',
  custom: {
      'item1': 'some value',
      'item2': 'some value'
  },
  dashStyle: 'Dash',
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
  description: 'Description goes here',
  enableMouseTracking: true,
  events: {
    afterAnimate: function(event) { return true; },
    click: function(event) { return true; },
    hide: function(event) { return true; },
    mouseOut: function(event) { return true; },
    show: function(event) { return true; }
  },
  includeInDataExport: true,
  keys: [
      'somevalue',
      'somevalue',
      'somevalue'
  ],
  label: {
      boxesToAvoid: [
          {
           bottom: 12,
           left: -46,
           right: 84,
           top: 24
          },
          {
           bottom: 48,
           left: -46,
           right: 84,
           top: 86
          }
      ],
      connectorAllowed: true,
      connectorNeighbourDistance: 12,
      enabled: true,
      format: 'format string',
      formatter: function() { return true; },
      maxFontSize: 18,
      minFontSize: 6,
      onArea: false,
      style: 'some style string'
  },
  linkedTo: 'some_id',
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
  onPoint: {
      connectorOptions: {
          dashstyle: 'Dash',
          stroke: '#ccc',
          width: 2
      },
      id: 'some-id',
      position: {
          align: 'left',
          verticalAlign: 'top',
          x: 15,
          y: -46
      }
  },
  opacity: 0.2,
  point: {
      events: {
        click: function(event) { return true; },
        drag: function(event) { return true; },
        drop: function(event) { return true; },
        mouseOut: function(event) { return true; }
      }
  },
  pointDescriptionFormatter: function (point) { return true; },
  selected: false,
  showCheckbox: true,
  showInLegend: true,
  skipKeyboardNavigation: false,
  states: {
    hover: {
        animation: {
            duration: 123
        },
        borderColor: '#cccccc',
        brightness: 0.3,
        enabled: true
    },
    inactive: {
        enabled: true,
        opacity: 0.5
    },
    normal: {
        animation: {
            defer: 24
        }
    },
    select: {
        color: '#ff0000',
        enabled: true
    }
  },
  stickyTracking: true,
  threshold: 123,
  tooltip: {
    animation: true,
    backgroundColor: '#ccc',
    borderColor: '#999',
    borderRadius: 4,
    borderWidth: 1,
    className: 'some-class-name',
    clusterFormat: 'format string',
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
    distance: 12,
    enabled: true,
    followPointer: true,
    followTouchMove: true,
    footerFormat: 'format string',
    formatter: function() { return true; },
    headerFormat: 'format string',
    headerShape: 'circle',
    hideDelay: 3,
    nullFormat: 'format string',
    nullFormatter: function() { return true; },
    outside: false,
    padding: 6,
    pointFormat: 'format string',
    pointFormatter: function() { return true; },
    positioner: function() { return true; },
    shadow: false,
    shape: 'rect',
    shared: false,
    snap: 4,
    split: false,
    stickOnContact: true,
    style: 'style string goes here',
    useHTML: false,
    valueDecimals: 2,
    valuePrefix: '$',
    valueSuffix: ' USD',
    xDateFormat: 'format string'
   },
  turboThreshold: 456,
  visible: true
}
