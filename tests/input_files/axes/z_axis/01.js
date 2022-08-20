{
    alignTicks: false,
    allowDecimals: true,
    alternateGridColor: '#ccc',
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
    linkedTo: 3,
    minRange: 5,
    minTickInterval: 1,
    offset: 0,
    opposite: false,
    pane: 1,
    reversedStacks: false,
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
    zoomEnabled: true
}
