Highcharts.setOptions({
  accessibility: {
      announceNewData: {
          announcementFormatter: function() { return true; },
          enabled: true,
          interruptUser: true,
          minimumAnnouncementInterval: 3
      },
      customComponents: {
          'item1': 'some-value-goes-here',
          'item2': 'some_other_value_goes_here'
      },
      description: 'Description goes here',
      enabled: true,
      highContrastTheme: 'something goes here',
      keyboardNavigation: {
          enabled: true,
          focusBorder: {
              enabled: true,
              hideBrowserFocusOutline: false,
              margin: 20,
              style: {
                  borderRadius: 2,
                  color: '#ccc',
                  lineWidth: 1
              }
          },
          order: [
              'series',
              'item1',
              'zoom',
              'container'
          ],
          seriesNavigation: {
              mode: 'normal',
              pointNavigationEnabledThreshold: 20,
              rememberPointFocus: true,
              skipNullPoints: false
          },
          wrapAround: true
      },
      landmarkVerbosity: 'all',
      linkedDescription: 'some-item-goes-here',
      point: {
          dateFormat: 'format string',
          dateFormatter: function() { return true; },
          describeNull: false,
          descriptionFormatter: function() { return true; },
          valueDecimals: 2,
          valueDescriptionFormat: 'format string',
          valuePrefix: '$',
          valueSuffix: 'USD'
      },
      screenReaderSection: {
          afterChartFormat: 'format string',
          afterChartFormatter: function() { return true; },
          axisRangeDateFormat: 'format string',
          beforeChartFormat: 'format string',
          beforeChartFormatter: function() { return true; },
          onPlayAsSoundClick: function() { return true; },
          onViewDataTableClick: function() { return true; }
      },
      series: {
          describeSingleSeries: true,
          descriptionFormat: 'format string goes here',
          descriptionFormatter: function() { return true; },
          pointDescriptionEnabledThreshold: 100
      },
      typeDescription: 'some description goes here'
    },
  annotations: {
      animation: {
          defer: 5
      },
      controlPointOptions: {
          positioner: function(x, target) { return true; }
      },
      crop: true,
      draggable: 'xy',
      events: {
          add: function(event) { return true; },
          afterUpdate: function(event) { return true; },
          click: function(event) { return true; },
          remove: function(event) { return true; }
      },
      id: 'some-id',
      labelOptions: {
          accessibility: {
              description: 'Description goes here'
          },
          align: 'center',
          allowOverlap: false,
          backgroundColor: '#ccc',
          borderColor: '#999',
          borderRadius: 4,
          borderWidth: 1,
          className: 'some-class-name',
          crop: false,
          distance: 10,
          format: 'format string',
          formatter: function() { return true; },
          includeInDataExport: true,
          overflow: 'justify',
          padding: 12,
          shadow: false,
          shape: 'callout',
          style: 'style-string-goes-here',
          text: 'format string',
          useHTML: false,
          verticalAlign: 'top',
          x: 5,
          y: 10
      },
      labels: [
          {
              point: {
                  x: 123,
                  xAxis: 1,
                  y: 456,
                  yAxis: 1
              },
              accessibility: {
                  description: 'Description goes here'
              },
              align: 'center',
              allowOverlap: false,
              backgroundColor: '#ccc',
              borderColor: '#999',
              borderRadius: 4,
              borderWidth: 1,
              className: 'some-class-name',
              crop: false,
              distance: 10,
              format: 'format string',
              formatter: function() { return true; },
              includeInDataExport: true,
              overflow: 'justify',
              padding: 12,
              shadow: false,
              shape: 'callout',
              style: 'style-string-goes-here',
              text: 'format string',
              useHTML: false,
              verticalAlign: 'top',
              x: 5,
              y: 10
          },
          {
              point: 'point-id-goes-here',
              accessibility: {
                  description: 'Description goes here'
              },
              align: 'center',
              allowOverlap: false,
              backgroundColor: '#ccc',
              borderColor: '#999',
              borderRadius: 4,
              borderWidth: 1,
              className: 'some-class-name',
              crop: false,
              distance: 10,
              format: 'format string',
              formatter: function() { return true; },
              includeInDataExport: true,
              overflow: 'justify',
              padding: 12,
              shadow: false,
              shape: 'callout',
              style: 'style-string-goes-here',
              text: 'format string',
              useHTML: false,
              verticalAlign: 'top',
              x: 5,
              y: 10
          },
          {
              point: {
                  x: 123,
                  xAxis: 'axis-id',
                  y: 456,
                  yAxis: 'axis-id'
              },
              accessibility: {
                  description: 'Description goes here'
              },
              align: 'center',
              allowOverlap: false,
              backgroundColor: '#ccc',
              borderColor: '#999',
              borderRadius: 4,
              borderWidth: 1,
              className: 'some-class-name',
              crop: false,
              distance: 10,
              format: 'format string',
              formatter: function() { return true; },
              includeInDataExport: true,
              overflow: 'justify',
              padding: 12,
              shadow: false,
              shape: 'callout',
              style: 'style-string-goes-here',
              text: 'format string',
              useHTML: false,
              verticalAlign: 'top',
              x: 5,
              y: 10
          }
      ],
      shapeOptions: {
          dashStyle: 'Solid',
          fill: '#000',
          height: 123,
          r: 12,
          ry: 24,
          snap: 5,
          src: 'https://www.somewhere.com',
          stroke: '#ccc',
          strokeWidth: 1,
          type: 'rect',
          width: 12,
          xAxis: 1,
          yAxis: 1
      },
      shapes: [
          {
           markerEnd: 'some-id-goes-here',
           markerStart: 'some-id-goes-here',
           point: {
               x: 123,
               xAxis: 1,
               y: 456,
               yAxis: 1
           },
           points: [
               {
                x: 123,
                xAxis: 1,
                y: 456,
                yAxis: 1
               },
               'some-id-goes-here',
               function() { return true; }
           ]
          }
      ],
      visible: true,
      zIndex: 3
  },
  boost: {
      allowForce: true,
      debug: {
          showSkipSummary: false,
          timeBufferCopy: true,
          timeKDTree: true,
          timeRendering: false,
          timeSeriesProcessing: true,
          timeSetup: true
      },
      enabled: true,
      pixelRatio: 2,
      seriesThreshold: 5000,
      useGPUTranslations: true,
      usePreallocated: true
  },
  caption: {
      align: 'center',
      floating: true,
      margin: 20,
      text: 'Test Text for the Caption',
      verticalAlign: 'top',
      x: 123,
      y: -123
  },
  chart: {
      alignThresholds: true,
      alignTicks: true,
      allowMutatingData: true,
      animation: false,
      backgroundColor: '#fff',
      borderColor: '#ccc',
      borderRadius: 3,
      borderWidth: 1,
      className: 'some-class-name',
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
      margin: [20, 20, 20, 20],
      marginBottom: 20,
      marginLeft: 20,
      marginRight: 20,
      marginTop: 20,
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
      spacingBottom: 5,
      spacingLeft: 5,
      spacingRight: 5,
      spacingTop: 5,
      style: 'style-string-goes-here',
      styledMode: false,
      type: 'line',
      width: 50,
      zoomBySingleTouch: false,
      zoomKey: 'alt',
      zoomType: 'xy'
  },
  colorAxis: {
    accessibility: {
         description: 'Description goes here',
         enabled: true,
         rangeDescription: 'Range description goes here'
     },
     angle: 15,
     ceiling: 120,
     className: 'some-class-name',
     endOnTick: false,
     events: {
       afterBreaks: function(event) { return true; },
       afterSetExtremes: function(event) { return true; },
       pointBreak: function(event) { return true; },
       setExtremes: function(event) { return true; }
     },
     floor: 0,
     gridLineColor: '#ccc',
     gridLineDashStyle: 'Solid',
     gridLineInterpolation: 'circle',
     gridLineWidth: 1,
     gridZIndex: 3,
     id: 'some-id',
     labels: {
         align: 'center',
         allowOverlap: false,
         autoRotation: [-45],
         autoRotationLimit: 80,
         distance: 12,
         enabled: true,
         format: 'some format string',
         formatter: function () { return true; },
         overflow: 'allow',
         padding: 12,
         position3d: 'offset',
         reserveSpace: true,
         rotation: 24,
         skew3d: false,
         staggerLines: 0,
         step: 2,
         style: 'some-style-string',
         useHTML: false,
         x: 5,
         y: -10,
         zIndex: 6
     },
     margin: 12,
     max: 1000,
     maxPadding: 12,
     min: 0,
     minorGridLineColor: '#999',
     minorGridLineDashStyle: 'Dash',
     minorGridLineWidth: 1,
     minorTickColor: '#ccc',
     minorTickInterval: 0.1,
     minorTickPosition: 'outside',
     minorTicks: true,
     minorTickWidth: 1,
     minPadding: 8,
     panningEnabled: true,
     reversed: false,
     showFirstLabel: true,
     showLastLabel: true,
     softMax: 10,
     softMin: 6,
     startOfWeek: 1,
     startOnTick: false,
     tickAmount: 5,
     tickColor: '#000',
     tickInterval: 5,
     tickLength: 8,
     tickmarkPlacement: 'on',
     tickPixelInterval: 8,
     tickPosition: 'outside',
     tickPositioner: function() { return true; },
     tickWidth: 1,
     type: 'linear',
     uniqueNames: true,
     units: [
         [
             'millisecond',
             [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
         ],
         [
             'second',
             [1, 2, 5, 10, 15, 30]
         ],
         [
             'minute',
             [1, 2, 5, 10, 15, 30]
         ],
         [
             'hour',
             [1, 2, 3, 4, 6, 8, 12]
         ],
         [
             'day',
             [1]
         ],
         [
             'week',
             [1]
         ],
         [
             'month',
             [1, 3, 6]
         ],
         [
             'year',
             null
         ]
     ],
     visible: true,
     zIndex: 3,

    dataClassColor: 'tween',
    dataClasses: [
        {
         color: '#ccc',
         from: 0,
         name: 'My Data Class',
         to: 100
        },
        {
         color: '#fff',
         from: 100,
         name: 'My Second Data Class',
         to: 200
        }
    ],
    layout: 'horizontal',
    lineColor: '#fff',
    marker: {
        animation: {
            defer: 5
        },
        color: '#ff0000',
        width: 10
    },
    maxColor: '#999',
    minColor: '#ccc',
    showInLegend: true,
    stops: [
        [0.0, '#ccc'],
        [0.1, '#fff'],
        [0.25, '#999'],
        [1.0, '#ff0000']
    ]
  },
  colors: [
      '#ccc',
      '#fff',
      '#000000'
  ],
  credits: {
      enabled: true,
      href: 'https://www.somewhere.com',
      style: {
          color: '#cccccc',
          fontSize: '12px'
      },
      text: 'Test Text for the Credits label'
  },
  data: {
      csvURL: '/test.csv',
      dataRefreshRate: 3,
      decimalPoint: '.',
      enablePolling: true,
      firstRowAsNames: true,
      itemDelimiter: ','
  },
  drilldown: {
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
  },
  exporting: {
    accessibility: {
        enabled: true
    },
    allowHTML: false,
    buttons: {
        'test_key': {
            enabled: true,
            text: 'Test Text'
        },
        'test_key2': {
            enabled: true,
            text: 'Test Text 2'
        }
    },
    enabled: true,
    error: function() { return true; },
    fallbackToExportServer: true,
    filename: 'test-filename',
    formAttributes: {
        'test_attr': 'value-123',
        'test_attr2': 'value-345'
    },
    libURL: 'http://www.somewhere.com/',
    menuItemDefinitions: {
        'menu1': {
          onclick: function() { return true; },
          text: 'My Menu Item',
          textKey: 'my-menu-item',
          separator: false
        },
        'menu2': {
          onclick: function() { return true; },
          text: 'My Menu Item',
          textKey: 'my-menu-item',
          separator: false
        }
    },
    pdfFont: {
        bold: 'http://www.somefile.com/flie.otf',
        bolditalic: 'http://www.somefile.com/flie.otf',
        italic: 'http://www.somefile.com/flie.otf',
        normal: 'http://www.somefile.com/flie.otf',
    },
    printMaxWidth: 300,
    scale: 1200,
    showTable: true,
    sourceHeight: 120,
    sourceWidth: 300,
    tableCaption: 'Caption goes here',
    type: 'image/png',
    url: 'http://www.somewhere.com/',
    useMultiLevelHeaders: false,
    useRowspanHeaders: false,
    width: 300
  },
  lang: {
    contextButtonTitle: 'some title goes here',
    decimalPoint: '--',
    downloadCSV: 'Download CSV',
    downloadJPEG: 'Download JPEG',
    downloadPDF: 'Download PDF',
    downloadPNG: 'Download PNG',
    downloadSVG: 'Download SVG',
    downloadXLS: 'Download Excel',
    drillUpText: 'Backup',
    exitFullscreen: 'Exit Fullscreen Mode',
    hideData: 'Hide',
    invalidDate: 'Invalid Time Period',
    loading: 'Loading...',
    mainBreadcrumb: 'Home',
    months: [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec'
    ],
    noData: 'No data available.',
    numericSymbolMagnitude: 1,
    numericSymbols: ['#', 'k', 'm'],
    printChart: 'Print',
    resetZoom: 'Reset',
    resetZoomTitle: 'Reset Zoom',
    shortMonths: [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec'
    ],
    shortWeekdays: [
        'Mon',
        'Tue',
        'Wed',
        'Thurs',
        'Fri',
        'Sat',
        'Sun'
    ],
    thousandsSep: ',',
    viewData: 'View Data',
    viewFullscreen: 'Fullscreen',
    weekdays: [
        'Mon',
        'Tue',
        'Wed',
        'Thurs',
        'Fri',
        'Sat',
        'Sun'
    ]
  },
  legend: {
      accessibility: {
          enabled: true,
          keyboardNavigation: {
              enabled: true
          }
      },
      align: 'right',
      alignColumns: true,
      backgroundColor: '#fff',
      borderColor: '#ccc',
      borderRadius: 4,
      className: 'some-class-name',
      enabled: true,
      floating: false,
      itemCheckboxStyle: 'some-style-setting',
      itemDistance: 12,
      itemHiddenStyle: 'some-style-setting',
      itemHoverStyle: 'some-style-setting',
      itemMarginBottom: 7,
      itemMarginTop: 7,
      itemStyle: 'some-style-setting',
      itemWidth: 36,
      labelFormat: 'format string',
      labelFormatter: function () { return true; },
      layout: 'vertical',
      margin: 7,
      maxHeight: 120,
      padding: 8,
      reversed: false,
      rtl: false,
      shadow: false,
      squareSymbol: false,
      symbolHeight: 12,
      symbolPadding: 2,
      symbolRadius: 0,
      symbolWidth: 12,
      title: {
          style: 'some-style-string',
          text: 'Legend Title Goes Here'
      },
      useHTML: false,
      verticalAlign: 'top',
      width: 120,
      x: 0,
      y: 0
  },
  loading: {
    hideDuration: 100,
    showDuration: 150
  },
  navigation: {
    bindingsClassName: 'some-class-name',
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
  },
  noData: {
    attr: {
        'stroke': '#ff0000',
        'stroke-width': 2,
        'rotation': 45,
        'd': ['M', 10, 10, 'L', 30, 30, 'z']
    },
    useHTML: true
  },
  pane: {
    background: [
        {
          className: 'test-class-name',
          innerRadius: '24%',
          shape: 'circle'
        },
        {
          innerRadius: '35%',
        }
    ],
    center: ['50%', '50%'],
    size: 120,
    startAngle: 0
  },
  plotOptions: {
    arcdiagram: {
      borderColor: '#fff',
      borderWidth: 2,
      centeredLinks: true,
      colorByPoint: false,
      colorIndex: 2,
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
      equalNodes: true,
      levels: [
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          }
      ],
      linkOpacity: 0.7,
      minLinkWidth: 1,
      nodeWidth: 6,
      reversed: false,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'arcdiagram'
    },
    area: {
      fillColor: '#ccc',
      fillOpacity: 0.7,
      lineColor: {
          radialGradient: {
              cx: 0.123,
              cy: 0.456,
              r: 0.789
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      negativeFillColor: '#ccc',
      trackByArea: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'area'
    },
    arearange: {
      fillColor: '#ccc',
      fillOpacity: 0.7,
      lineColor: {
          radialGradient: {
              cx: 0.123,
              cy: 0.456,
              r: 0.789
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      negativeFillColor: '#ccc',
      trackByArea: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'arearange'
    },
    areaspline: {
      fillColor: '#ccc',
      fillOpacity: 0.7,
      lineColor: {
          radialGradient: {
              cx: 0.123,
              cy: 0.456,
              r: 0.789
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      negativeFillColor: '#ccc',
      trackByArea: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'areaspline'
    },
    areasplinerange: {
      fillColor: '#ccc',
      fillOpacity: 0.7,
      lineColor: {
          radialGradient: {
              cx: 0.123,
              cy: 0.456,
              r: 0.789
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      negativeFillColor: '#ccc',
      trackByArea: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'areasplinerange'
    },
    bar: {
      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'bar'
    },
    bellcurve: {
      intervals: 3,

      fillColor: '#ccc',
      fillOpacity: 0.7,
      lineColor: {
          radialGradient: {
              cx: 0.123,
              cy: 0.456,
              r: 0.789
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      negativeFillColor: '#ccc',
      trackByArea: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'bellcurve'
    },
    boxplot: {
      boxDashStyle: 'Solid',
      medianColor: '#ccc',
      medianDashStyle: 'Dash',
      medianWidth: 2,
      stemDashStyle: 'Solid',
      stemWidth: 1,
      whiskerColor: '#999',
      whiskerDashStyle: 'Solid',
      whiskerLength: 12,
      whiskerWidth: 2,

      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true,
          draggableHigh: true,
          draggableLow: true,
          draggableQ1: true,
          draggableQ3: true
      },

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'boxplot'
    },
    bubble: {
      displayNegative: false,
      jitter: {
        x: 123,
        y: 456
      },
      maxSize: 24,
      minSize: 6,
      sizeBy: 'width',
      sizeByAbsoluteValue: true,
      zMax: 6,
      zMin: 3,
      zThreshold: 50,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'bubble'
    },
    bullet: {
      targetOptions: {
          borderColor: '#999',
          borderRadius: 2,
          borderWidth: 1,
          color: '#ccc',
          height: 12,
          width: '5%'
      },

      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true,
          draggableTarget: true
      },

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'bullet'
    },
    column: {
      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'column'
    },
    columnpyramid: {
      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'columnpyramid'
    },
    columnrange: {
      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'columnrange'
    },
    cylinder: {
      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'cylinder'
    },
    dependencywheel: {
      borderColor: '#ccc',
      borderWidth: 2,
      center: ['50%', '30%'],
      centerInCategory: true,
      colorByPoint: false,
      colorIndex: 3,
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
      curveFactor: 0.6,
      levels: [
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          }
      ],
      linkOpacity: 0.7,
      minLinkWidth: 1,
      nodePadding: 6,
      nodeWidth: 12,
      startAngle: 45,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'dependencywheel'
    },
    dumbbell: {
        animationLimit: 10,
        colorAxis: 'some-id-goes-here',
        colorIndex: 3,
        colorKey: 'some-key-goes-here',
        connectEnds: true,
        connectNulls: false,
        connectorColor: '#777',
        connectorWidth: 1,
        crisp: true,
        cropThreshold: 500,
        dataSorting: {
            enabled: true,
            matchByName: true,
            sortKey: 'some-key-value'
        },
        dragDrop: {
            draggableHigh: true,
            draggableLow: true,
            draggableX: true,
            draggableY: true,
            dragHandle: {
                className: 'draghandle-classname-goes-here',
                color: '#ccc',
                cursor: 'alias',
                lineColor: '#ddd',
                lineWidth: 2,
                pathFormatter: function() { return true; },
                zIndex: 10
            },
            dragMaxX: 3456,
            dragMaxY: 6532,
            dragMinX: 123,
            dragMinY: 321,
            dragPrecisionX: 5,
            dragPrecisionY: 5,
            dragSensitivity: 2,
            groupBy: 'some-property-name',
            guideBox: {
                default: {
                    className: 'some-classname-goes-here',
                    color: '#999',
                    cursor: 'pointer',
                    lineColor: '#ccc',
                    lineWidth: 2,
                    zIndex: 100
                }
            },
            liveRedraw: true
        },
        findNearestPointBy: 'xy',
        getExtremesForAll: true,
        groupPadding: 12,
        linecap: 'round',
        lineColor: '#ccc',
        lowColor: '#eee',
        negativeColor: '#ee0000',
        negativeFillColor: '#990000',
        pointInterval: 5,
        pointIntervalUnit: 'days',
        pointPadding: 6,
        pointPlacement: 'on',
        pointStart: 12,
        relativeXValue: true,
        shadow: {
          color: '#cccccc',
          offsetX: 10,
          offsetY: 5,
          width: 4
        },
        softThreshold: true,
        stacking: 'normal',
        step: 'right',
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
        ],
        type: 'dumbbell'
    },
    errorbar: {
      boxDashStyle: 'Solid',
      medianColor: '#ccc',
      medianDashStyle: 'Dash',
      medianWidth: 2,
      stemDashStyle: 'Solid',
      stemWidth: 1,
      whiskerColor: '#999',
      whiskerDashStyle: 'Solid',
      whiskerLength: 12,
      whiskerWidth: 2,

      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true,
          draggableHigh: true,
          draggableLow: true,
          draggableQ1: true,
          draggableQ3: true
      },

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'errorbar'
    },
    funnel: {
      height: '60%',
      neckHeight: '15%',
      neckWidth: 36,
      reversed: false,
      width: 320,

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
      thickness: 2,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'funnel'
    },
    funnel3d: {
      gradientForSides: true,

      height: '60%',
      neckHeight: '15%',
      neckWidth: 36,
      reversed: false,
      width: 320,

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
      thickness: 2,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'funnel3d'
    },
    gauge: {
      colorIndex: 3,
      crisp: true,
      dial: {
          backgroundColor: '#ccc',
          baseLength: '80%',
          baseWidth: 120,
          borderColor: '#fff',
          borderWidth: 1,
          path: [1, 2, 3],
          radius: '80%',
          rearLength: '10%',
          topWidth: 80
      },
      linecap: 'round',
      lineWidth: 1,
      overshoot: 12.5,
      pivot: {
          backgroundColor: '#ccc',
          borderColor: '#eee',
          borderWidth: 2,
          radius: 60
      },
      pointInterval: 5,
      pointIntervalUnit: 'day',
      pointStart: 5,
      relativeXValue: true,
      shadow: false,
      wrap: false,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'gauge'
    },
    heatmap: {
      borderRadius: 4,
      colsize: 1,
      nullColor: '#ccc',
      pointPadding: 6,
      rowsize: 1,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'heatmap'
    },
    histogram: {
      binsNumber: 'square-root',
      binWidth: 24,

      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'histogram'
    },
    item: {
      itemPadding: 12,
      layout: 'horizontal',
      rows: 3,

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
      thickness: 2,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'item'
    },
    line: {
      fillColor: '#ccc',
      fillOpacity: 0.7,
      lineColor: {
          radialGradient: {
              cx: 0.123,
              cy: 0.456,
              r: 0.789
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      negativeFillColor: '#ccc',
      trackByArea: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'line'
    },
    lollipop: {
        animationLimit: 10,
        colorAxis: 'some-id-goes-here',
        colorIndex: 3,
        colorKey: 'some-key-goes-here',
        connectEnds: true,
        connectNulls: false,
        connectorColor: '#777',
        connectorWidth: 1,
        crisp: true,
        cropThreshold: 500,
        dataSorting: {
            enabled: true,
            matchByName: true,
            sortKey: 'some-key-value'
        },
        dragDrop: {
            draggableHigh: true,
            draggableLow: true,
            draggableX: true,
            draggableY: true,
            dragHandle: {
                className: 'draghandle-classname-goes-here',
                color: '#ccc',
                cursor: 'alias',
                lineColor: '#ddd',
                lineWidth: 2,
                pathFormatter: function() { return true; },
                zIndex: 10
            },
            dragMaxX: 3456,
            dragMaxY: 6532,
            dragMinX: 123,
            dragMinY: 321,
            dragPrecisionX: 5,
            dragPrecisionY: 5,
            dragSensitivity: 2,
            groupBy: 'some-property-name',
            guideBox: {
                default: {
                    className: 'some-classname-goes-here',
                    color: '#999',
                    cursor: 'pointer',
                    lineColor: '#ccc',
                    lineWidth: 2,
                    zIndex: 100
                }
            },
            liveRedraw: true
        },
        findNearestPointBy: 'xy',
        getExtremesForAll: true,
        groupPadding: 12,
        linecap: 'round',
        lineColor: '#ccc',
        lowColor: '#eee',
        negativeColor: '#ee0000',
        negativeFillColor: '#990000',
        pointInterval: 5,
        pointIntervalUnit: 'days',
        pointPadding: 6,
        pointPlacement: 'on',
        pointStart: 12,
        relativeXValue: true,
        shadow: {
          color: '#cccccc',
          offsetX: 10,
          offsetY: 5,
          width: 4
        },
        softThreshold: true,
        stacking: 'normal',
        step: 'right',
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
        ],
        type: 'lollipop'
    },
    networkgraph: {
      colorIndex: 3,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'networkgraph'
    },
    organization: {
      hangingIndent: 24,
      hangingIndentTranslation: 'inherit',
      levels: [
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          }
      ],
      linkColor: '#999',
      linkLineWidth: 1,
      linkOpacity: 0.7,
      linkRadius: 4,
      minLinkWidth: 1,
      minNodeLength: 12,
      nodePadding: 6,
      nodeWidth: 24,

      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'organization'
    },
    packedbubble: {
      displayNegative: false,
      maxSize: 36,
      minSize: 12,
      parentNode: {
          allowPointSelect: true
      },
      sizeBy: 'area',
      useSimulation: true,
      zThreshold: 246,

      colorIndex: 3,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'packedbubble'
    },
    pareto: {
      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'pareto'
    },
    pie: {
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
      thickness: 2,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'pie'
    },
    polygon: {
      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'polygon'
    },
    pyramid: {
      height: '60%',
      neckHeight: '15%',
      neckWidth: 36,
      reversed: false,
      width: 320,

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
      thickness: 2,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'pyramid'
    },
    pyramid3d: {
      gradientForSides: true,

      height: '60%',
      neckHeight: '15%',
      neckWidth: 36,
      reversed: false,
      width: 320,

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
      thickness: 2,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'pyramid3d'
    },
    sankey: {
      borderColor: '#ccc',
      borderWidth: 2,
      center: ['50%', '30%'],
      centerInCategory: true,
      colorByPoint: false,
      colorIndex: 3,
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
      curveFactor: 0.6,
      levels: [
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          },
          {
           colorByPoint: false,
           dataLabels: {
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
             borderRadius: 24,
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
           linkOpacity: 0.5,
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
                 enabled: true
             }
           },
           borderColor: '#ccc',
           borderWidth: 1,
           level: 1
          }
      ],
      linkOpacity: 0.7,
      minLinkWidth: 1,
      nodePadding: 6,
      nodeWidth: 12,
      startAngle: 45,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'sankey'
    },
    scatter: {
      jitter: {
        x: 123,
        y: 456
      },
      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'scatter'
    },
    scatter3d: {
      jitter: {
        x: 123,
        y: 456
      },
      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'scatter3d'
    },
    series: {
      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'series'
    },
    solidgauge: {
      innerRadius: 123,
      overshoot: 12.5,
      radius: 246,
      rounded: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'solidgauge'
    },
    spline: {
      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'spline'
    },
    streamgraph: {
      fillColor: '#ccc',
      fillOpacity: 0.7,
      lineColor: {
          radialGradient: {
              cx: 0.123,
              cy: 0.456,
              r: 0.789
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
      },
      negativeFillColor: '#ccc',
      trackByArea: true,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'streamgraph'
    },
    sunburst: {
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
      startAngle: 0,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'sunburst'
    },
    tilemap: {
      tileShape: 'hexagon',

      borderRadius: 4,
      colsize: 1,
      nullColor: '#ccc',
      pointPadding: 6,
      rowsize: 1,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'tilemap'
    },
    timeline: {
      colorAxis: 'some-id-goes-here',
      colorByPoint: false,
      colorIndex: 2,
      colorKey: 'some-key-goes-here',
      crisp: false,
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      ignoreHiddenPoint: true,
      linecap: 'round',
      relativeXValue: true,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'timeline'
    },
    treemap: {
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
      getExtremesForAll: true,
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
      ],
      type: 'treemap'
    },
    variablepie: {
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
      thickness: 2,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'variablepie'
    },
    variwide: {
      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'variwide'
    },
    vector: {
      cluster: {
        allowOverlap: true,
        animation: {
            defer: 5
        },
        dataLabels: {
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
          borderRadius: 24,
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
        drillToCluster: true,
        enabled: true,
        events: {
          drillToCluster: function(event) { return true; }
        },
        layoutAlgorithm: {
            distance: '20%',
            gridSize: 123,
            iterations: 5,
            kmeansThreshold: 1000
        },
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
        minimumClusterSize: 5,
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
             to: 123
            }
        ]
      },
      rotationOrigin: 'start',
      vectorLength: 12,

      animationLimit: 10,
      boostBlending: '#ccc',
      boostThreshold: 1234,
      colorAxis: 1,
      colorIndex: 5,
      colorKey: 'some-key-value',
      connectEnds: true,
      connectNulls: true,
      crisp: true,
      cropThreshold: 123,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'x',
      getExtremesForAll: true,
      linecap: 'round',
      lineWidth: 2,
      negativeColor: '#fff',
      pointInterval: 5,
      pointIntervalUnit: 'weeks',
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: false,
      softThreshold: true,
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
      ],

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'vector'
    },
    venn: {
      animationLimit: 10,
      borderDashStyle: 'Solid',
      brighten: 10,
      cluster: {
        allowOverlap: true,
        animation: {
            defer: 5
        },
        dataLabels: {
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
          borderRadius: 24,
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
        drillToCluster: true,
        enabled: true,
        events: {
          drillToCluster: function(event) { return true; }
        },
        layoutAlgorithm: {
            distance: '20%',
            gridSize: 123,
            iterations: 5,
            kmeansThreshold: 1000
        },
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
        minimumClusterSize: 5,
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
             to: 123
            }
        ]
      },
      colorAxis: 'some-id-goes-here',
      colorIndex: 2,
      colorKey: 'some-key-goes-here',
      crisp: true,
      relativeXValue: true,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'venn'
    },
    waterfall: {
      lineColor: '#fff',
      upColor: '#999',

      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'waterfall'
    },
    windbarb: {
      dataGrouping: {
        anchor: 'start',
        approximation: 'windbarb',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        enabled: true,
        firstAnchor: 'start',
        forced: true,
        groupAll: true,
        groupPixelWidth: 10,
        lastAnchor: 'end',
        units: [
            [
                'millisecond',
                [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
            ],
            [
                'second',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'minute',
                [1, 2, 5, 10, 15, 30]
            ],
            [
                'hour',
                [1, 2, 3, 4, 6, 8, 12]
            ],
            [
                'day',
                [1]
            ],
            [
                'week',
                [1]
            ],
            [
                'month',
                [1, 3, 6]
            ],
            [
                'year',
                null
            ]
        ]
      },
      onSeries: 'some-id-goes-here',
      vectorLength: 10,
      xOffset: 5,
      yOffset: 2,

      depth: 10,
      edgeColor: '#999',
      edgeWidth: 1,
      groupZPadding: 4,

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'windbarb'
    },
    wordcloud: {
      allowExtendPlayingField: false,
      animationLimit: 10,
      borderColor: '#ccc',
      borderRadius: 2,
      borderWidth: 1,
      centerInCategory: true,
      colorByPoint: false,
      colorIndex: 2,
      colorKey: 'some-key-goes-here',
      colors: [
          '#ccc',
          '#fff',
          '000000'
      ],
      edgeWidth: 1,
      maxFontSize: 36,
      minFontSize: 6,
      placementStrategy: 'center',
      rotation: {
          from: 0,
          orientations: 4,
          to: 135
      },
      spiral: 'rectangle',

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
            enabled: true
        }
      },
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'wordcloud'
    },
    xrange: {
      groupZPadding: 4,
      partialFill: {
        fill: '#cccccc'
      },

      borderColor: '#ccc',
      borderRadius: 4,
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
      pointRange: 24,
      pointWidth: 12,

      accessibility: {
          description: 'Description goes here',
          enabled: true,
          exposeAsGroupOnly: true,
          keyboardNavigation: {
              enabled: true
          },
          point: {
              dateFormat: 'format string',
              dateFormatter: function() { return true; },
              describeNull: false,
              descriptionFormatter: function() { return true; },
              valueDecimals: 2,
              valueDescriptionFormat: 'format string',
              valuePrefix: '$',
              valueSuffix: 'USD'
          },
      },
      allowPointSelect: true,
      animation: {
          defer: 5
      },
      className: 'some-class-name',
      clip: false,
      color: '#fff',
      cursor: 'alias',
      custom: {
          'item1': 'some value',
          'item2': 'some value'
      },
      dashStyle: 'Dash',
      dataLabels: {
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
        borderRadius: 24,
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
      description: 'Description goes here',
      enableMouseTracking: true,
      events: {
        afterAnimate: function(event) { return true; },
        click: function(event) { return true; },
        hide: function(event) { return true; },
        mouseOut: function(event) { return true; },
        show: function(event) { return true; }
      },
      includeInDataExport: true,
      keys: [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      label: {
          boxesToAvoid: [
              {
               bottom: 12,
               left: -46,
               right: 84,
               top: 24
              },
              {
               bottom: 48,
               left: -46,
               right: 84,
               top: 86
              }
          ],
          connectorAllowed: true,
          connectorNeighbourDistance: 12,
          enabled: true,
          format: 'format string',
          formatter: function() { return true; },
          maxFontSize: 18,
          minFontSize: 6,
          onArea: false,
          style: 'some style string'
      },
      linkedTo: 'some_id',
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
      onPoint: {
          connectorOptions: {
              dashstyle: 'Dash',
              stroke: '#ccc',
              width: 2
          },
          id: 'some-id',
          position: {
              align: 'left',
              verticalAlign: 'top',
              x: 15,
              y: -46
          }
      },
      opacity: 0.2,
      point: {
          events: {
            click: function(event) { return true; },
            drag: function(event) { return true; },
            drop: function(event) { return true; },
            mouseOut: function(event) { return true; }
          }
      },
      pointDescriptionFormatter: function (point) { return true; },
      selected: false,
      showCheckbox: true,
      showInLegend: true,
      skipKeyboardNavigation: false,
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
      stickyTracking: true,
      threshold: 123,
      tooltip: {
        animation: true,
        backgroundColor: '#ccc',
        borderColor: '#999',
        borderRadius: 4,
        borderWidth: 1,
        className: 'some-class-name',
        clusterFormat: 'format string',
        dateTimeLabelFormats: {
          day: 'test',
          hour: 'test',
          millisecond: 'test',
          minute: 'test',
          month: 'test',
          second: 'test',
          week: 'test',
          year: 'test'
        },
        distance: 12,
        enabled: true,
        followPointer: true,
        followTouchMove: true,
        footerFormat: 'format string',
        formatter: function() { return true; },
        headerFormat: 'format string',
        headerShape: 'circle',
        hideDelay: 3,
        nullFormat: 'format string',
        nullFormatter: function() { return true; },
        outside: false,
        padding: 6,
        pointFormat: 'format string',
        pointFormatter: function() { return true; },
        positioner: function() { return true; },
        shadow: false,
        shape: 'rect',
        shared: false,
        snap: 4,
        split: false,
        stickOnContact: true,
        style: 'style string goes here',
        useHTML: false,
        valueDecimals: 2,
        valuePrefix: '$',
        valueSuffix: ' USD',
        xDateFormat: 'format string'
       },
      turboThreshold: 456,
      visible: true,
      type: 'xrange'
    }
  },
  responsive: {
    rules: [
      {
        condition: {
          maxHeight: 20,
          maxWidth: 30,
          minHeight: 10,
          minWidth: 10
        }
      },
      {
        condition: {
          maxHeight: 123.45,
          maxWidth: 543.21,
          minHeight: 678.9,
          minWidth: 321
        }
      }
    ]
  },
  series: [],
  subtitle: {
    align: 'left',
    floating: true,
    text: 'Title aligned left',
    verticalAlign: 'middle',
    x: 70,
    y: 40
  },
  time: {
    timezone: 'Europe/Oslo',
    useUTC: false
  },
  title: {
    align: 'left',
    floating: true,
    margin: 30,
    text: 'Title aligned left',
    verticalAlign: 'middle',
    x: 70,
    y: 40
  },
  tooltip: {
    borderRadius: 3,
    borderWidth: 44,
    valueDecimals: 2,
    valuePrefix: '$',
    valueSuffix: ' USD'
   },
  xAxis: [
    {
      crosshair: {
          className: 'some-class-name',
          color: '#ccc',
          dashStyle: 'Dash',
          snap: true,
          width: 40,
          zIndex: 6
      },
      height: 60,
      left: 5,
      lineColor: '#999',
      lineWidth: 1,
      showEmpty: true,
      top: 340,
      width: 300,

      accessibility: {
           description: 'Description goes here',
           enabled: true,
           rangeDescription: 'Range description goes here'
       },
       angle: 15,
       ceiling: 120,
       className: 'some-class-name',
       endOnTick: false,
       events: {
         afterBreaks: function(event) { return true; },
         afterSetExtremes: function(event) { return true; },
         pointBreak: function(event) { return true; },
         setExtremes: function(event) { return true; }
       },
       floor: 0,
       gridLineColor: '#ccc',
       gridLineDashStyle: 'Solid',
       gridLineInterpolation: 'circle',
       gridLineWidth: 1,
       gridZIndex: 3,
       id: 'some-id',
       labels: {
           align: 'center',
           allowOverlap: false,
           autoRotation: [-45],
           autoRotationLimit: 80,
           distance: 12,
           enabled: true,
           format: 'some format string',
           formatter: function () { return true; },
           overflow: 'allow',
           padding: 12,
           position3d: 'offset',
           reserveSpace: true,
           rotation: 24,
           skew3d: false,
           staggerLines: 0,
           step: 2,
           style: 'some-style-string',
           useHTML: false,
           x: 5,
           y: -10,
           zIndex: 6
       },
       margin: 12,
       max: 1000,
       maxPadding: 12,
       min: 0,
       minorGridLineColor: '#999',
       minorGridLineDashStyle: 'Dash',
       minorGridLineWidth: 1,
       minorTickColor: '#ccc',
       minorTickInterval: 0.1,
       minorTickPosition: 'outside',
       minorTicks: true,
       minorTickWidth: 1,
       minPadding: 8,
       panningEnabled: true,
       reversed: false,
       showFirstLabel: true,
       showLastLabel: true,
       softMax: 10,
       softMin: 6,
       startOfWeek: 1,
       startOnTick: false,
       tickAmount: 5,
       tickColor: '#000',
       tickInterval: 5,
       tickLength: 8,
       tickmarkPlacement: 'on',
       tickPixelInterval: 8,
       tickPosition: 'outside',
       tickPositioner: function() { return true; },
       tickWidth: 1,
       type: 'linear',
       uniqueNames: true,
       units: [
           [
               'millisecond',
               [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
           ],
           [
               'second',
               [1, 2, 5, 10, 15, 30]
           ],
           [
               'minute',
               [1, 2, 5, 10, 15, 30]
           ],
           [
               'hour',
               [1, 2, 3, 4, 6, 8, 12]
           ],
           [
               'day',
               [1]
           ],
           [
               'week',
               [1]
           ],
           [
               'month',
               [1, 3, 6]
           ],
           [
               'year',
               null
           ]
       ],
       visible: true,
       zIndex: 3
    }
  ],
  yAxis: [
    {
      maxColor: '#ccc',
      minColor: '#000',
      stackLabels: {
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
        borderRadius: 24,
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
      stops: [
          [0.0, '#ccc'],
          [0.1, '#fff'],
          [0.25, '#999'],
          [1.0, '#ff0000']
      ],
      tooltipValueFormat: 'format string goes here',

      crosshair: {
          className: 'some-class-name',
          color: '#ccc',
          dashStyle: 'Dash',
          snap: true,
          width: 40,
          zIndex: 6
      },
      height: 60,
      left: 5,
      lineColor: '#999',
      lineWidth: 1,
      showEmpty: true,
      top: 340,
      width: 300,

      accessibility: {
           description: 'Description goes here',
           enabled: true,
           rangeDescription: 'Range description goes here'
       },
       angle: 15,
       ceiling: 120,
       className: 'some-class-name',
       endOnTick: false,
       events: {
         afterBreaks: function(event) { return true; },
         afterSetExtremes: function(event) { return true; },
         pointBreak: function(event) { return true; },
         setExtremes: function(event) { return true; }
       },
       floor: 0,
       gridLineColor: '#ccc',
       gridLineDashStyle: 'Solid',
       gridLineInterpolation: 'circle',
       gridLineWidth: 1,
       gridZIndex: 3,
       id: 'some-id',
       labels: {
           align: 'center',
           allowOverlap: false,
           autoRotation: [-45],
           autoRotationLimit: 80,
           distance: 12,
           enabled: true,
           format: 'some format string',
           formatter: function () { return true; },
           overflow: 'allow',
           padding: 12,
           position3d: 'offset',
           reserveSpace: true,
           rotation: 24,
           skew3d: false,
           staggerLines: 0,
           step: 2,
           style: 'some-style-string',
           useHTML: false,
           x: 5,
           y: -10,
           zIndex: 6
       },
       margin: 12,
       max: 1000,
       maxPadding: 12,
       min: 0,
       minorGridLineColor: '#999',
       minorGridLineDashStyle: 'Dash',
       minorGridLineWidth: 1,
       minorTickColor: '#ccc',
       minorTickInterval: 0.1,
       minorTickPosition: 'outside',
       minorTicks: true,
       minorTickWidth: 1,
       minPadding: 8,
       panningEnabled: true,
       reversed: false,
       showFirstLabel: true,
       showLastLabel: true,
       softMax: 10,
       softMin: 6,
       startOfWeek: 1,
       startOnTick: false,
       tickAmount: 5,
       tickColor: '#000',
       tickInterval: 5,
       tickLength: 8,
       tickmarkPlacement: 'on',
       tickPixelInterval: 8,
       tickPosition: 'outside',
       tickPositioner: function() { return true; },
       tickWidth: 1,
       type: 'linear',
       uniqueNames: true,
       units: [
           [
               'millisecond',
               [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
           ],
           [
               'second',
               [1, 2, 5, 10, 15, 30]
           ],
           [
               'minute',
               [1, 2, 5, 10, 15, 30]
           ],
           [
               'hour',
               [1, 2, 3, 4, 6, 8, 12]
           ],
           [
               'day',
               [1]
           ],
           [
               'week',
               [1]
           ],
           [
               'month',
               [1, 3, 6]
           ],
           [
               'year',
               null
           ]
       ],
       visible: true,
       zIndex: 3
    }
  ],
  zAxis: [
    {
      accessibility: {
          description: 'Description goes here',
          enabled: true,
          rangeDescription: 'Range description goes here'
      },
      alignTicks: false,
      allowDecimals: true,
      alternateGridColor: '#ccc',
      angle: 15,
      breaks: [
          {
           breakSize: 20,
           from: 0,
           repeat: 1,
           to: 100
          },
          {
           breakSize: 50,
           from: 100,
           repeat: 1,
           to: 1000
          }
      ],
      categories: [
          'Category 1',
          'Category 2',
          'Category 3',
          'Category 4'
      ],
      ceiling: 120,
      className: 'some-class-name',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      endOnTick: false,
      events: {
        afterBreaks: function(event) { return true; },
        afterSetExtremes: function(event) { return true; },
        pointBreak: function(event) { return true; },
        setExtremes: function(event) { return true; }
      },
      floor: 0,
      gridLineColor: '#ccc',
      gridLineDashStyle: 'Solid',
      gridLineInterpolation: 'circle',
      gridLineWidth: 1,
      gridZIndex: 3,
      id: 'some-id',
      labels: {
          align: 'center',
          allowOverlap: false,
          autoRotation: [-45],
          autoRotationLimit: 80,
          distance: 12,
          enabled: true,
          format: 'some format string',
          formatter: function () { return true; },
          overflow: 'allow',
          padding: 12,
          position3d: 'offset',
          reserveSpace: true,
          rotation: 24,
          skew3d: false,
          staggerLines: 0,
          step: 2,
          style: 'some-style-string',
          useHTML: false,
          x: 5,
          y: -10,
          zIndex: 6
      },
      linkedTo: 3,
      margin: 12,
      max: 1000,
      maxPadding: 12,
      min: 0,
      minorGridLineColor: '#999',
      minorGridLineDashStyle: 'Dash',
      minorGridLineWidth: 1,
      minorTickColor: '#ccc',
      minorTickInterval: 0.1,
      minorTickPosition: 'outside',
      minorTicks: true,
      minorTickWidth: 1,
      minPadding: 8,
      minRange: 5,
      minTickInterval: 1,
      offset: 0,
      opposite: false,
      pane: 1,
      panningEnabled: true,
      reversed: false,
      reversedStacks: false,
      showFirstLabel: true,
      showLastLabel: true,
      softMax: 10,
      softMin: 6,
      startOfWeek: 1,
      startOnTick: false,
      tickAmount: 5,
      tickColor: '#000',
      tickInterval: 5,
      tickLength: 8,
      tickmarkPlacement: 'on',
      tickPixelInterval: 8,
      tickPosition: 'outside',
      tickPositioner: function() { return true; },
      tickWidth: 1,
      title: {
          align: 'low',
          margin: 20,
          offset: 0,
          position3d: 'offset',
          reserveSpace: true,
          rotation: 0,
          skew3d: false,
          style: 'some-style-string',
          text: 'The Axis Title',
          textAlign: 'center',
          useHTML: false,
          x: 5,
          y: 10
      },
      type: 'linear',
      uniqueNames: true,
      units: [
          [
              'millisecond',
              [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
          ],
          [
              'second',
              [1, 2, 5, 10, 15, 30]
          ],
          [
              'minute',
              [1, 2, 5, 10, 15, 30]
          ],
          [
              'hour',
              [1, 2, 3, 4, 6, 8, 12]
          ],
          [
              'day',
              [1]
          ],
          [
              'week',
              [1]
          ],
          [
              'month',
              [1, 3, 6]
          ],
          [
              'year',
              null
          ]
      ],
      visible: true,
      zIndex: 3,
      zoomEnabled: true
    }
  ]
});
