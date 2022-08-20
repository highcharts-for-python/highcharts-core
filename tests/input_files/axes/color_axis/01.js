{
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
}
