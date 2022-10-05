.. code-block:: python

  my_series = LineSeries()

  # A simple array of numerical values which correspond to the Y value of the data
  # point
  my_series.data = [0, 5, 3, 5]

  # An array containing 2-member arrays (corresponding to the X and Y values of the
  # data point)
  my_series.data = [
      [0, 0],
      [1, 5],
      [2, 3],
      [3, 5]
  ]

  # An array of dict with named values
  my_series.data = [
    {
        'x': 0,
        'y': 0,
        'name': 'Point1',
        'color': '#00FF00'
    },
    {
        'x': 1,
        'y': 5,
        'name': 'Point2',
        'color': '#CCC'
    },
    {
        'x': 2,
        'y': 3,
        'name': 'Point3',
        'color': '#999'
    },
    {
        'x': 3,
        'y': 5,
        'name': 'Point4',
        'color': '#000'
    }
  ]
