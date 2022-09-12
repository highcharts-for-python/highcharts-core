
  .. method:: copy(self, other, overwrite = True, **kwargs)
    :noindex:

    Copy the properties from ``self`` to ``other``.

    :param other: The target instance to which the properties of this instance should
      be copied.
    :type other: :class:`HighchartsMeta`

    :param overwrite: if ``True``, properties in ``other`` that are already set will
      be overwritten by their counterparts in ``self``. Defaults to ``True``.
    :type overwrite: :class:`bool <python:bool>`

    :param kwargs: Additional keyword arguments. Some special descendents of
      :class:`HighchartsMeta` may have special implementations of this method which
      rely on additional keyword arguments.

    :returns: A mutated version of ``other`` with new property values

    :raises HighchartsValueError: if ``other`` is not the same class as (or subclass of)
      ``self``
