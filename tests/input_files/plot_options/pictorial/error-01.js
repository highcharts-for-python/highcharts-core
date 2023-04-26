{
  borderColor: '#ccc',
  borderRadius: 'invalid value',
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
  pointRange: 'invalid value',
  pointWidth: 'invalid-value'
}
