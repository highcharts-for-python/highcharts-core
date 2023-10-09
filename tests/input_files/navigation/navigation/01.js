{
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
  bindingsClassName: 'some-class-name',
  buttonOptions: {
    enabled: true,
    text: 'Button Label',
    theme: {
        'fill': '#fff',
        'stroke': '#ccc'
    },
    y: 0
  },
  events: {
    closePopup: function (event) { return true; },
    selectButton: function (event) {return true;},
    showPopup: function(event) {return true;}
  },
  iconsURL: 'https://www.somewhere.com/',
  menuItemHoverStyle: {
    'color': '#5f5e5e',
    'fontFamily': 'Roboto',
    'fontSize': '12px',
    'fontWeight': '400'
  },
  menuItemStyle: {
    'color': '#5f5e5e',
    'fontFamily': 'Roboto',
    'fontSize': '12px',
    'fontWeight': '400'
  },
  menuStyle: {
    'color': '#5f5e5e',
    'fontFamily': 'Roboto',
    'fontSize': '12px',
    'fontWeight': '400'
  }
}
