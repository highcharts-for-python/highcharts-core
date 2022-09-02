{
  activeAxisLabelStyle: {
      'cursor': 'style string',
      'color': '#999'
  },
  activeDataLabelStyle: {
      'cursor': 'style string',
      'color': '#999'
  },
  allowPointDrilldown: true,
  animation: false,
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
        text: '>',
    },
    useHTML: false,
    zIndex: 3
  }
}
