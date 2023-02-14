.. code-block:: python

  from highcharts_core.options.series.area import LineSeries
  from highcharts_core.options.series.data import CartesianData

  # A simple array of numerical values which correspond to the Y value of the data
  # point
  my_data = CartesianData.from_array([0, 5, 3, 5])

  # An array containing 2-member arrays (corresponding to the X and Y values of the
  # data point)
  my_data = CartesianData.from_array([
      [0, 0],
      [1, 5],
      [2, 3],
      [3, 5]
  ])

  # An array of dict with named values
  my_data = CartesianData.from_array([
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
  ])

  my_series = LineSeries(data = my_data)

.. collapse:: Method Signature

  .. method:: from_array(cls, value)
    :noindex:
    :classmethod:

    Creates a collection of data point instances, parsing the contents of ``value`` as an
    array (iterable). This method is specifically used to parse data that is input to
    **Highcharts for Python** without property names, in an array-organized structure as
    described in the `Highcharts JS <https://www.highcharts.com>`__ documentation.

    .. seealso::

      The specific structure of the expected array is highly dependent on the type of data
      point that the series needs, which itself is dependent on the series type itself.

      Please review the detailed :ref:`series documentation <series_documentation>` for
      series type-specific details of relevant array structures.

    .. note::

      An example of how this works for a simple
      :class:`LineSeries <highcharts_core.options.series.area.LineSeries>` (which uses
      :class:`CartesianData <highcharts_core.options.series.data.cartesian.CartesianData>`
      data points) would be:

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

    :param value: The value that should contain the data which will be converted into data
      point instances.

      .. note::

        If ``value`` is not an iterable, it will be converted into an iterable to be
        further de-serialized correctly.

    :type value: iterable

    :returns: Collection of :term:`data point` instances (descended from
      :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`)
    :rtype: :class:`list <python:list>` of
      :class:`DataBase <highcharts_core.options.series.data.base.DataBase>`-descendant
      instances
