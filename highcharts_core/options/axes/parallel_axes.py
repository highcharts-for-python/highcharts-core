from typing import Optional
from highcharts_core.options.axes.y_axis import YAxis


class ParallelAxesOptions(YAxis):
    """Common options for all Y-axes rendered in a parallel coordinates plot.

    .. warning::

      This feature requires ``modules/parallel-coordinates.js``.

    """
    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'chart.parallelAxes'
