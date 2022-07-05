from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class BoostDebug(HighchartsMeta):
    """Debugging options for boost. Useful for benchmarking, and general timing."""

    def __init__(self, **kwargs):
        self._show_skip_summary = False
        self._time_buffer_copy = False
        self._time_kd_tree = False
        self._time_rendering = False
        self._time_series_processing = False
        self._time_setup = False

        self.show_skip_summary = kwargs.pop('show_skip_summary', False)
        self.time_buffer_copy = kwargs.pop('time_buffer_copy', False)
        self.time_kd_tree = kwargs.pop('time_kd_tree', False)
        self.time_rendering = kwargs.pop('time_rendering', False)
        self.time_series_processing = kwargs.pop('time_series_processing', False)
        self.time_setup = kwargs.pop('time_setup', False)

    @property
    def show_skip_summary(self) -> bool:
        """When ``True``, the number of points skipped in series processing is outputted.
        Defaults to ``False``.

        Points are skipped if they are closer than 1 pixel from each other.

        :returns: Flag indicating whether the skip summary will be shown.
        :rtype: :class:`bool <python:bool>`
        """
        return self._show_skip_summary

    @show_skip_summary.setter
    def show_skip_summary(self, value):
        self._show_skip_summary = bool(value)

    @property
    def time_buffer_copy(self) -> bool:
        """When ``True``, the time it takes for the SVG buffer copy to complete is
        outputted. Defaults to ``False``.

        :returns: Flag indicating whether the buffer copy timing will be shown.
        :rtype: :class:`bool <python:bool>`
        """
        return self._time_buffer_copy

    @time_buffer_copy.setter
    def time_buffer_copy(self, value):
        self._time_buffer_copy = bool(value)

    @property
    def time_kd_tree(self) -> bool:
        """When ``True``, the time spent building the k-d tree used for markers, etc. will
        be rendered. Defaults to ``False``.

        .. note::

          Note that the k-d tree is built asynchronously, and runs post-rendering.
          Thus, it does not affect the performance of the rendering itself.

        :returns: Flag indicating whether the KD tree timing will be shown.
        :rtype: :class:`bool <python:bool>`
        """
        return self._time_kd_tree

    @time_kd_tree.setter
    def time_kd_tree(self, value):
        self._time_kd_tree = bool(value)

    @property
    def time_rendering(self) -> bool:
        """When ``True``, the time spent on actual rendering is outputted to the console.
        Defaults to ``False``.

        :returns: Flag indicating whether the rendering time will be shown.
        :rtype: :class:`bool <python:bool>`
        """
        return self._time_rendering

    @time_rendering.setter
    def time_rendering(self, value):
        self._time_rendering = bool(value)

    @property
    def time_series_processing(self) -> bool:
        """When ``True``, the time spent on transforming the series data to vertex buffers
        is outputted. Defaults to ``False``.

        :returns: Flag indicating whether the series processing time will be shown.
        :rtype: :class:`bool <python:bool>`
        """
        return self._time_series_processing

    @time_series_processing.setter
    def time_series_processing(self, value):
        self._time_series_processing = bool(value)

    @property
    def time_setup(self) -> bool:
        """When ``True``, the te time spent on setting up the WebGL context, creating
        shaders, and textures is outputted. Defaults to ``False``.

        :returns: Flag indicating whether the setup time will be shown.
        :rtype: :class:`bool <python:bool>`
        """
        return self._time_setup

    @time_setup.setter
    def time_setup(self, value):
        self._time_setup = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'show_skip_summary': as_dict.pop('showSkipSummary', False),
            'time_buffer_copy': as_dict.pop('timeBufferCopy', False),
            'time_kd_tree': as_dict.pop('timeKDTree', False),
            'time_rendering': as_dict.pop('timeRendering', False),
            'time_series_processing': as_dict.pop('timeSeriesProcessing', False),
            'time_setup': as_dict.pop('timeSetup', False)
        }

        return cls(**kwargs)

    def to_dict(self):
        return {
            'showSkipSummary': self.show_skip_summary,
            'timeBufferCopy': self.time_buffer_copy,
            'timeKDTree': self.time_kd_tree,
            'timeRendering': self.time_rendering,
            'timeSeriesProcessing': self.time_series_processing,
            'timeSetup': self.time_setup
        }


class Boost(HighchartsMeta):
    """Options for the Boost module.

    The Boost module allows certain series types to be rendered by WebGL instead of the
    default SVG. This allows hundreds of thousands of data points to be rendered in
    milliseconds. In addition to the WebGL rendering it saves time by skipping processing
    and inspection of the data wherever possible. This introduces some limitations to what
    features are available in boost mode. See
    `the docs <https://www.highcharts.com/docs/advanced-chart-features/boost-module>`_
    for details.

    .. note::

      In addition to the global :meth:`HighchartOptions.boost` property, each series has
      a :meth:`Series.boost_threshold` that defines when the boost should kick in.

    """

    def __init__(self, **kwargs):
        self._allow_force = True
        self._debug = None
        self._enabled = True
        self._pixel_ratio = constants.DEFAULT_BOOST_PIXEL_RATIO
        self._series_threshold = constants.DEFAULT_BOOST_SERIES_THRESHOLD
        self._use_gpu_translations = False
        self._use_preallocated = False

        self.allow_force = kwargs.pop('allow_force', True)
        self.debug = kwargs.pop('debug', None)
        self.enabled = kwargs.pop('enabled', True)
        self.pixel_ratio = kwargs.pop('pixel_ratio', constants.DEFAULT_BOOST_PIXEL_RATIO)
        self.series_threshold = kwargs.pop('series_threshold',
                                           constants.DEFAULT_BOOST_SERIES_THRESHOLD)
        self.use_gpu_translations = kwargs.pop('use_gpu_translations', False)
        self.use_preallocated = kwargs.pop('use_preallocated', False)

    @property
    def allow_force(self) -> bool:
        """If ``True``, the whole chart will be boosted if one of the series crosses its
        threshold and all the series can be boosted. Defaults to ``True``.

        :returns: Flag indicating whether the entire chart can be boosted in response to
          one series being boosted.
        :rtype: class:`bool <python:bool>`
        """
        return self._allow_force

    @allow_force.setter
    def allow_force(self, value):
        self._allow_force = bool(value)

    @property
    def debug(self) -> Optional[BoostDebug]:
        """Debugging options for boost. Useful for benchmarking, and general timing.

        :rtype: :class:`BoostDebug` or :obj:`None <python:None>`
        """
        return self._debug

    @debug.setter
    @class_sensitive(BoostDebug)
    def debug(self, value):
        self._debug = value

    @property
    def enabled(self) -> bool:
        """If ``True``, boost is enabled on the chart. If ``False``, boost is disabled.
        Defaults to ``True``.

        :returns: Flag indicating whether boost is enabled for the chart.
        :rtype: :class:`bool <python:bool>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

    @property
    def pixel_ratio(self) -> int:
        f"""The pixel ratio for the WebGL content. Defaults to
        ``{constants.DEFAULT_BOOST_PIXEL_RATIO}``.

        If ``0``, the ``window.devicePixelRatio`` is used. This ensures sharp graphics on
        high DPI displays like Apple's Retina, as well as when a page is zoomed.

        .. note::

          The default is left at {constants.DEFAULT_BOOST_PIXEL_RATIO} for now, as this
          is a new feature that has the potential to break existing setups. Over time,
          when it has been battle tested, the intention is to set it to ``0`` by default.

        .. hint::

          Another use case for this option is to set it to ``2`` in order to make
          exported and upscaled charts render sharp.

        .. warning::

          One limitation when using the ``pixel_ratio`` is that the line width of graphs
          is scaled down. Since the Boost module currently can only render ``1px`` line
          widths, it is scaled down to a thin ``0.5`` pixels on a Retina display.

        :rtype: :class:`int <python:int>`
        """
        return self._pixel_ratio

    @pixel_ratio.setter
    def pixel_ratio(self, value):
        self._pixel_ratio = validators.integer(value,
                                               allow_empty = False,
                                               minimum = 0)

    @property
    def series_threshold(self) -> int:
        f"""Set the series threshold for when the boost should kick in globally. Defaults
        to ``{constants.DEFAULT_BOOST_SERIES_THRESHOLD}``.

        Setting to e.g. ``20`` will cause the whole chart to enter boost mode if there are
        20 or more series active. When the chart is in boost mode, every series in it will
        be rendered to a common canvas. This offers a significant speed improvment in
        charts with a very high amount of series.

        :rtype: :class:`int <python:int>`
        """
        return self._series_threshold

    @series_threshold.setter
    def series_threshold(self, value):
        self._series_threshold = validators.integer(value, allow_empty = False)

    @property
    def use_gpu_translations(self) -> bool:
        """If ``True``, enables GPU translations. GPU translations are faster than doing
        the translation in JavaScript. Defaults to ``False``.

        .. warning::

          This option may cause rendering issues with certain datasets. Namely, if your
          dataset has large numbers with small increments (such as timestamps), it won't
          work correctly. This is due to floating point precission.

        :returns: Flag indicating whether to use GPU translations.
        :rtype: :class:`bool <python:bool>`
        """
        return self._use_gpu_translations

    @use_gpu_translations.setter
    def use_gpu_translations(self, value):
        self._use_gpu_translations = bool(value)

    @property
    def use_preallocated(self) -> bool:
        """If ``True``, enables the pre-allocation of vertex buffers. Defaults to
        ``False``.

        Enabling this will make it so that the binary data arrays required for storing the
        series data will be allocated prior to transforming the data to a WebGL-compatible
        format.

        .. warning::

          Enabling this feature saves a copy operation on the order of O(n) and so is
          significantly more performant. However, this is currently an experimental
          option, and may cause visual artifacts with some datasets.

          As such, care should be taken when using this setting to make sure that it
          doesn't cause any rendering glitches with the given use-case.

        :returns: Flag indicating whether pre-allocation of vertex buffers is enabled.
        :rtype: :class:`bool <python:bool>`
        """
        return self._use_preallocation

    @use_preallocated.setter
    def use_preallocated(self, value):
        self._use_preallocated = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'allow_force': as_dict.pop('allowForce', True),
            'debug': as_dict.pop('debug', None),
            'enabled': as_dict.pop('enabled', True),
            'pixel_ratio': as_dict.pop('pixelRatio', constants.DEFAULT_BOOST_PIXEL_RATIO),
            'series_threshold': as_dict.pop('seriesThreshold',
                                            constants.DEFALUT_BOOST_SERIES_THRESHOLD),
            'use_gpu_translations': as_dict.pop('useGPUTranslations', False),
            'use_preallocated': as_dict.pop('usePreallocated', False)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'allowForce': self.allow_force,
            'debug': self.debug,
            'enabled': self.enabled,
            'pixelRatio': self.pixel_ratio,
            'seriesThreshold': self.series_threshold,
            'useGPUTranslations': self.use_gpu_translations,
            'usePreallocated': self.use_preallocated
        }

        return self.trim_dict(untrimmed)
