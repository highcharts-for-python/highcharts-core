{
    alignThresholds: true,
    alignTicks: true,
    allowMutatingData: true,
    animation: false,
    backgroundColor: '#fff',
    borderColor: '#ccc',
    borderRadius: 3,
    borderWidth: 1,
    className: 123,
    colorCount: 10,
    displayErrors: true,
    events: {
      addSeries: function(event) { return true;},
      afterPrint: function(event) {return true;},
      click: function(event) { return true; },
      selection: function(event) { return true; }
    },
    height: 120,
    ignoreHiddenSeries: false,
    inverted: false,
    margin: 20,
    numberFormatter: function(value) { return true; },
    panKey: 'ctrl',
    panning: {
        enabled: true,
        type: 'x'
    },
    parallelCoordinates: false,
    pinchType: 'x',
    plotBackgroundColor: '#ccc',
    plotBackgroundImage: 'http://www.somewhere.com',
    plotBorderColor: '#999',
    plotBorderWidth: 1,
    plotShadow: false,
    polar: false,
    reflow: false,
    renderTo: 'some-id',
    resetZoomButton: {
        position: {
          align: 'center',
          verticalAlign: 'top',
          x: -10,
          y: 10
        },
        relativeTo: 'plot',
        theme: {
            'fill': '#ccc'
        }
    },
    scrollablePlotArea: {
        minHeight: 120,
        minWidth: 300,
        opacity: 0.6,
        scrollPositionX: 0,
        scrollPositionY: 0
    },
    selectionMarkerFill: '#ccc',
    shadow: false,
    showAxes: true,
    spacing: [5, 5, 5, 5],
    style: 'style-string-goes-here',
    styledMode: false,
    type: 'line',
    width: 50,
    zoomBySingleTouch: false,
    zoomKey: 'alt',
    zoomType: 'xy'
}
