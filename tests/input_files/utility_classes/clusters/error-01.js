{
    allow_overlap: true,
    animation: {
        defer: 5
    },
    data_labels: {
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
      borderRadius: 'invalid number',
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
    drill_to_cluster: true,
    enabled: true,
    events: {
      drillToCluster: function(event) { return true; }
    },
    layout_algorithm: {
        distance: '20%',
        gridSize: 'not a number',
        iterations: 5,
        kmeansThreshold: 1000
    },
    marker: {
      fillColor: '#cccccc',
      enabled: true,
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
    minimum_cluster_size: 5,
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
         to: 'not a number'
        }
    }
  }
