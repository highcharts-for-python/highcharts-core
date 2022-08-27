{
  colorIndex: 'invalid value',
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
  ]
}
