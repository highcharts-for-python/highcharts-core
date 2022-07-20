from highcharts.plot_options.area import AreaOptions


class PolygonOptions(AreaOptions):
    """General options to apply to all Polygon series types.

    A polygon series can be used to draw any freeform shape in the cartesian
    coordinate system. A fill is applied with the :meth:`PolygonOptions.color`
    setting, and stroke is applied through :meth:`PolygonOptions.line_width` and
    :meth:`PolygonOptions.line_color`.

    .. figure:: _static/polygon-example.png
      :alt: Polygon Example Chart
      :align: center

    """
    pass
