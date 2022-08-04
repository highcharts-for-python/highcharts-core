from highcharts.series.funnel import FunnelSeries
from highcharts.plot_options.pyramid import PyramidOptions, Pyramid3DOptions


class PyramidSeries(FunnelSeries, PyramidOptions):
    """Options to configure a Pyramid series.

    A pyramid series is a special type of funnel, without neck and reversed by
    default.

    .. figure:: _static/pyramid-example.png
      :alt: Pyramid Example Chart
      :align: center

    """
    pass


class Pyramid3DSeries(FunnelSeries, Pyramid3DOptions):
    """Options to configure a Pyramid 3D series.

    A pyramid 3d series is a special type of funnel, without neck and reversed by
    default.

    .. figure:: _static/pyramid_3d-example.png
      :alt: Pyramid 3D Example Chart
      :align: center

    """
    pass
