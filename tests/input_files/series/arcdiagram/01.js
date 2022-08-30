{
    borderColor: '#fff',
    borderWidth: 2,
    centeredLinks: true,
    colorByPoint: false,
    colorIndex: 2,
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
    equalNodes: true,
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
    nodeWidth: 6,
    reversed: false
}
