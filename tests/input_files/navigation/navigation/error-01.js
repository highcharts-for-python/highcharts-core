{
    bindingsClassName: 123,
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
          text: '>',
          style: {
              'some-key': 'some-value'
          }
      },
      useHTML: false,
      zIndex: 3
    },
    buttonOptions: {
      enabled: true,
      text: 'Button Label',
      theme: {
          fill: '#fff',
          stroke: '#ccc'
      },
      y: 0
    },
    events: {
      closePopup: function (event) { return true; },
      selectButton: function (event) {return true;},
      showPopup: function(event) {return true;}
    },
    iconsURL: 'https://www.somewhere.com/'
  }
