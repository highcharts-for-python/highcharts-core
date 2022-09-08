{
  chart: {
        backgroundColor: {
            linearGradient: {
              x1: 0,
              x2: 0,
              y1: 1,
              y2: 1
            },
            stops: [
                [0, 'rgb(255, 255, 255)'],
                [1, 'rgb(240, 240, 255)']
            ]
        },
        borderWidth: 2,
        plotBackgroundColor: 'rgba(255, 255, 255, .9)',
        plotBorderWidth: 1
  },
  caption: {
      align: 'center',
      floating: true,
      margin: 20,
      verticalAlign: 'top'
  },
  credits: {
      enabled: true,
      href: 'https://www.somewhere.com',
      style: {
          color: '#cccccc',
          fontSize: '8px'
      },
      text: 'Highcharts for Python'
  }
}
