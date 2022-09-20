{
  data: [
    {
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
      sets: [
        'item 1',
        'item 2',
        'item 3'
      ],
      value: 123,

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
  animationLimit: 10,
  colorIndex: 2,
  colorKey: 'some-key-goes-here',
  crisp: true,
  relativeXValue: true,

  borderDashStyle: 'Solid',
  brighten: 10,
  cluster: {
    allowOverlap: true,
    animation: {
        defer: 5
    },
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
    drillToCluster: true,
    enabled: true,
    events: {
      drillToCluster: function(event) { return true; }
    },
    layoutAlgorithm: {
        distance: '20%',
        gridSize: 123,
        iterations: 5,
        kmeansThreshold: 1000
    },
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
    minimumClusterSize: 5,
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
          enabled: true,
      }
    },
    zones: [
        {
         className: 'classname-1',
         from: 0,
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
         to: 123
        },
        {
         className: 'classname-1',
         from: 0,
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
         to: 123
        },
        {
         className: 'classname-1',
         from: 0,
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
         to: 123
        }
    ]
  }
}
