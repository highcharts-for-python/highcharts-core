{
  chart: {
      type: 'bar'
  },
  title: {
      text: 'Fruit Consumption'
  },
  xAxis: {
      categories: ['Apples', 'Bananas', 'Oranges']
  },
  yAxis: {
      title: {
          text: 'Fruit eaten'
      }
  },
  series: [
    {
      name: 'Jane',
      data: [1, 0, 4],
      type: 'bar'
    },
    {
      name: 'John',
      data: [5, 7, 3],
      type: 'bar'
    }]
}
