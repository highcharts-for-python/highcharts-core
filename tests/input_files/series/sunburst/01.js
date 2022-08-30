{
  allowTraversingTree: true,
  borderColor: '#ccc',
  borderWidth: 2,
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
  center: ['50%', '50%'],
  colorByPoint: true,
  colorIndex: 2,
  crisp: true,
  fillColor: '#999',
  levelIsConstant: true,
  levels: [
      {
       borderDashStyle: 'Solid',
       color: '#ccc',
       colorVariation: {
           key: 'brightness',
           to: 50
       },
       levelSize: {
           unit: 'percentage',
           value: 10
       },
       borderColor: '#ccc',
       borderWidth: 1,
       level: 1,
      }
  ],
  levelSize: {
      unit: 'percentage',
      value: 123
  },
  rootId: 'some-id-goes-here',
  shadow: false,
  size: '50%',
  slicedOffset: 12.3,
  startAngle: 0
}
