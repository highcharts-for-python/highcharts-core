{
  data: [
    {
      outgoing: true,
      weight: 0.75,

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
  ],
  colorIndex: 3,
  borderColor: '#ccc',
  borderWidth: 2,
  center: ['50%', '30%'],
  centerInCategory: true,
  colorByPoint: false,
  colors: [
      '#fff',
      'ccc',
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
  curveFactor: 0.6,
  levels: [
      {
       colorByPoint: false,
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
       linkOpacity: 0.5,
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
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1
      },
      {
       colorByPoint: false,
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
       linkOpacity: 0.5,
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
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1
      },
      {
       colorByPoint: false,
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
       linkOpacity: 0.5,
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
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1
      }
  ],
  linkOpacity: 0.7,
  minLinkWidth: 1,
  nodePadding: 6,
  nodeWidth: 12,
  startAngle: 45,
  type: 'sankey',
  nodes: [
    {
      column: 2,
      level: 2,
      color: '#cccccc',
      colorIndex: 123,
      dataLabels: {
        align: 'center',
        allowOverlap: false,
        backgroundColor: '#cccccc',
        enabled: true,
        overflow: 'justify',
        shadow: false
      },
      id: 'some-id-goes-here',
      name: 'My Node Name',
      offsetHorizontal: 10,
      offsetVertical: '5%'
    }
  ]
}
