.. code-block:: python

  # EXAMPLE 1
  # A simple array of numerical values which correspond to the Y value of the data
  # point

  my_series.load_from_array([0, 5, 3, 5])

  # EXAMPLE 2
  # An array containing 2-member arrays (corresponding to the X and Y values of the
  # data point)

  my_series.load_from_array([
      [0, 0],
      [1, 5],
      [2, 3],
      [3, 5]
  ])

  # EXAMPLE 3
  # An array of dict with named values

  my_series.load_from_array([
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

  # EXAMPLE 5
  # using a NumPy ndarray named "numpy_array"

  my_series.load_from_array(numpy_array)

.. collapse:: Method Signature

  .. method:: load_from_array(cls, value)
    :noindex:
    :classmethod:

    Update the :term:`series` instance's ``data`` property with data populated from
    an array-like ``value``.

    This method is specifically used to parse data that is input to
    **Highcharts for Python** without property names, in an array-organized structure as
    described in the `Highcharts JS <https://www.highcharts.com>`__ documentation.

    .. seealso::

      The specific structure of the expected array is highly dependent on the type of data
      point that the series needs, which itself is dependent on the series type itself.

      Please review the detailed :ref:`series documentation <series_documentation>` for
      series type-specific details of relevant array structures.

    :param value: The value that should contain the data which will be converted into data
      point instances.

      .. note::

        If ``value`` is not an iterable, it will be converted into an iterable to be
        further de-serialized correctly.

    :type value: iterable

