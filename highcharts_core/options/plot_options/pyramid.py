from highcharts_core.options.plot_options.funnel import FunnelOptions, Funnel3DOptions


class PyramidOptions(FunnelOptions):
    """General options to apply to all Pyramid series types.

    A pyramid series is a special type of funnel, without neck and reversed by
    default.

    .. figure:: ../../../_static/pyramid-example.png
      :alt: Pyramid Example Chart
      :align: center

    """
    pass

class Pyramid3DOptions(Funnel3DOptions):
    """General options to apply to all Pyramid 3D series types.

    A pyramid 3d series is a special type of funnel, without neck and reversed by
    default.

    .. figure:: ../../../_static/pyramid_3d-example.png
      :alt: Pyramid 3D Example Chart
      :align: center

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
