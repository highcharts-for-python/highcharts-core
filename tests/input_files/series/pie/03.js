{
  maxPointSize: '15%',
  minPointSize: '5%',
  sizeBy: 'area',
  zMax: 30,
  zMin: 2,

  borderColor: '#ccc',
  borderWidth: 1,
  center: ['50%', '50%'],
  colorAxis: 1,
  colorIndex: 3,
  colorKey: 'some-key-goes-here',
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
  depth: 10,
  endAngle: 90,
  fillColor: '#fff',
  ignoreHiddenPoint: true,
  innerSize: '30%',
  linecap: 'round',
  minSize: '20%',
  size: 80,
  slicedOffset: 24,
  startAngle: 45,
  thickness: 2
}
