{
    ndarray: [
        [0, 15], 
        [10, -50], 
        [20, -56.5], 
        [30, -46.5], 
        [40, -22.1],
        [50, -2.5], 
        [60, -27.7], 
        [70, -55.7], 
        [80, -76.5]
    ],
    dataPoints: [
        {
            accessibility: {
                description: 'Some description goes here',
                enabled: true
            },
            className: 'some-class-name',
            color: '#ccc',
            colorIndex: 2,
            custom: 'invalid-value',
            description: 'Some description goes here',
            events: {
                click: function (event) { return true; },
                drag: function (event) { return true; },
                drop: function (event) { return true; },
                mouseOut: function (event) { return true; }
            },
            id: 'some-id-goes-here',
            labelrank: 3,
            name: 'Some Name Goes here',
            selected: false
        },
        {
            accessibility: {
                description: 'Some description goes here',
                enabled: true
            },
            className: 'some-class-name',
            color: '#ccc',
            colorIndex: 2,
            custom: {
                'some_key': 123,
                'other_key': 456
            },
            description: 'Some description goes here',
            events: {
                click: function (event) { return true; },
                drag: function (event) { return true; },
                drop: function (event) { return true; },
                mouseOut: function (event) { return true; }
            },
            id: 'some-id-goes-here',
            labelrank: 3,
            name: 'Some Name Goes here',
            selected: false
        }
    ]
}