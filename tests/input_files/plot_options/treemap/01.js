{
  allowTraversingTree: true,
  alternateStartingDirection: false,
  animationLimit: 10,
  boostBlending: 'some-value-goes-here',
  boostThreshold: 5000,
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
  colorAxis: 'some-id-goes-here',
  colorByPoint: true,
  colorIndex: 2,
  colorKey: 'some-key-goes-here',
  colors: [
      '#ccc',
      '#fff',
      '000000'
  ],
  crisp: true,
  cropThreshold: 500,
  findNearestPointBy: 'xy',
  getExtremesFromAll: true,
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
  linecap: 'round',
  lineWidth: 1,
  negativeColor: '#ccc',
  pointInterval: 5,
  pointIntervalUnit: 'day',
  pointStart: 1,
  relativeXValue: true,
  softThreshold: true,
  sortIndex: 2,
  stacking: 'normal',
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
  ]
}
