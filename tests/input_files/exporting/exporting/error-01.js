{
    accessibility: {
        enabled: true
    },
    allowHTML: false,
    buttons: {
        test_key: {
            text: 'Test Text',
            enabled: true
        },
        test_key2: {
            text: 'Test Text 2',
            enabled: true
        }
    },
    enabled: true,
    error: function() { return true; },
    fallbackToExportServer: true,
    filename: 123,
    formAttributes: {
        test_attr: 'value-123',
        test_attr2: 'value-345'
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
}
