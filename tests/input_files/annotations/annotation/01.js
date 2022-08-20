{
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
}
