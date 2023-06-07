from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class BoostDebug(HighchartsMeta):
    """Debugging options for boost. Useful for benchmarking, and general timing."""

    def __init__(self, **kwargs):
        self._show_skip_summary = None
        self._time_buffer_copy = None
        self._time_kd_tree = None
        self._time_rendering = None
        self._time_series_processing = None
        self._time_setup = None

        self.show_skip_summary = kwargs.get('show_skip_summary', None)
        self.time_buffer_copy = kwargs.get('time_buffer_copy', None)
        self.time_kd_tree = kwargs.get('time_kd_tree', None)
        self.time_rendering = kwargs.get('time_rendering', None)
        self.time_series_processing = kwargs.get('time_series_processing', None)
        self.time_setup = kwargs.get('time_setup', None)

    @property
    def show_skip_summary(self) -> Optional[bool]:
        """When ``True``, the number of points skipped in series processing is outputted.
        Defaults to ``False``.

        Points are skipped if they are closer than 1 pixel from each other.

        :returns: Flag indicating whether the skip summary will be shown.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_skip_summary

    @show_skip_summary.setter
    def show_skip_summary(self, value):
        if value is None:
            self._show_skip_summary = None
        else:
            self._show_skip_summary = bool(value)

    @property
    def time_buffer_copy(self) -> Optional[bool]:
        """When ``True``, the time it takes for the SVG buffer copy to complete is
        outputted. Defaults to ``False``.

        :returns: Flag indicating whether the buffer copy timing will be shown.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._time_buffer_copy

    @time_buffer_copy.setter
    def time_buffer_copy(self, value):
        if value is None:
            self._time_buffer_copy = None
        else:
            self._time_buffer_copy = bool(value)

    @property
    def time_kd_tree(self) -> Optional[bool]:
        """When ``True``, the time spent building the k-d tree used for markers, etc. will
        be rendered. Defaults to ``False``.

        .. note::

          Note that the k-d tree is built asynchronously, and runs post-rendering.
          Thus, it does not affect the performance of the rendering itself.

        :returns: Flag indicating whether the KD tree timing will be shown.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._time_kd_tree

    @time_kd_tree.setter
    def time_kd_tree(self, value):
        if value is None:
            self._time_kd_tree = None
        else:
            self._time_kd_tree = bool(value)

    @property
    def time_rendering(self) -> Optional[bool]:
        """When ``True``, the time spent on actual rendering is outputted to the console.
        Defaults to ``False``.

        :returns: Flag indicating whether the rendering time will be shown.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._time_rendering

    @time_rendering.setter
    def time_rendering(self, value):
        if value is None:
            self._time_rendering = None
        else:
            self._time_rendering = bool(value)

    @property
    def time_series_processing(self) -> Optional[bool]:
        """When ``True``, the time spent on transforming the series data to vertex buffers
        is outputted. Defaults to ``False``.

        :returns: Flag indicating whether the series processing time will be shown.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._time_series_processing

    @time_series_processing.setter
    def time_series_processing(self, value):
        if value is None:
            self._time_series_processing = None
        else:
            self._time_series_processing = bool(value)

    @property
    def time_setup(self) -> Optional[bool]:
        """When ``True``, the te time spent on setting up the WebGL context, creating
        shaders, and textures is outputted. Defaults to ``False``.

        :returns: Flag indicating whether the setup time will be shown.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._time_setup

    @time_setup.setter
    def time_setup(self, value):
        if value is None:
            self._time_setup = None
        else:
            self._time_setup = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'show_skip_summary': as_dict.get('showSkipSummary', None),
            'time_buffer_copy': as_dict.get('timeBufferCopy', None),
            'time_kd_tree': as_dict.get('timeKDTree', None),
            'time_rendering': as_dict.get('timeRendering', None),
            'time_series_processing': as_dict.get('timeSeriesProcessing', None),
            'time_setup': as_dict.get('timeSetup', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
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
        self._allow_force = None
        self._debug = None
        self._enabled = None
        self._pixel_ratio = None
        self._series_threshold = None
        self._use_gpu_translations = None
        self._use_preallocated = None

        self.allow_force = kwargs.get('allow_force', None)
        self.debug = kwargs.get('debug', None)
        self.enabled = kwargs.get('enabled', None)
        self.pixel_ratio = kwargs.get('pixel_ratio', None)
        self.series_threshold = kwargs.get('series_threshold', None)
        self.use_gpu_translations = kwargs.get('use_gpu_translations', None)
        self.use_preallocated = kwargs.get('use_preallocated', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'boost'

    @property
    def allow_force(self) -> Optional[bool]:
        """If ``True``, the whole chart will be boosted if one of the series crosses its
        threshold and all the series can be boosted. Defaults to ``True``.

        :returns: Flag indicating whether the entire chart can be boosted in response to
          one series being boosted.
        :rtype: class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_force

    @allow_force.setter
    def allow_force(self, value):
        if value is None:
            self._allow_force = None
        else:
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
    def enabled(self) -> Optional[bool]:
        """If ``True``, boost is enabled on the chart. If ``False``, boost is disabled.
        Defaults to ``True``.

        :returns: Flag indicating whether boost is enabled for the chart.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def pixel_ratio(self) -> Optional[int]:
        """The pixel ratio for the WebGL content. Defaults to
        ``1``.

        If ``0``, the ``window.devicePixelRatio`` is used. This ensures sharp graphics on
        high DPI displays like Apple's Retina, as well as when a page is zoomed.

        .. note::

          The default is left at ``1`` for now, as this
          is a new feature that has the potential to break existing setups. Over time,
          when it has been battle tested, the intention is to set it to ``0`` by default.

        .. hint::

          Another use case for this option is to set it to ``2`` in order to make
          exported and upscaled charts render sharp.

        .. warning::

          One limitation when using the ``pixel_ratio`` is that the line width of graphs
          is scaled down. Since the Boost module currently can only render ``1px`` line
          widths, it is scaled down to a thin ``0.5`` pixels on a Retina display.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._pixel_ratio

    @pixel_ratio.setter
    def pixel_ratio(self, value):
        self._pixel_ratio = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def series_threshold(self) -> Optional[int]:
        """Set the series threshold for when the boost should kick in globally. Defaults
        to ``50``.

        Setting to e.g. ``20`` will cause the whole chart to enter boost mode if there are
        20 or more series active. When the chart is in boost mode, every series in it will
        be rendered to a common canvas. This offers a significant speed improvment in
        charts with a very high amount of series.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._series_threshold

    @series_threshold.setter
    def series_threshold(self, value):
        self._series_threshold = validators.integer(value, allow_empty = True)

    @property
    def use_gpu_translations(self) -> Optional[bool]:
        """If ``True``, enables GPU translations. GPU translations are faster than doing
        the translation in JavaScript. Defaults to ``False``.

        .. warning::

          This option may cause rendering issues with certain datasets. Namely, if your
          dataset has large numbers with small increments (such as timestamps), it won't
          work correctly. This is due to floating point precission.

        :returns: Flag indicating whether to use GPU translations.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None.`
        """
        return self._use_gpu_translations

    @use_gpu_translations.setter
    def use_gpu_translations(self, value):
        if value is None:
            self._use_gpu_translations = None
        else:
            self._use_gpu_translations = bool(value)

    @property
    def use_preallocated(self) -> Optional[bool]:
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
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_preallocated

    @use_preallocated.setter
    def use_preallocated(self, value):
        if value is None:
            self._use_preallocated = None
        else:
            self._use_preallocated = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'allow_force': as_dict.get('allowForce', None),
            'debug': as_dict.get('debug', None),
            'enabled': as_dict.get('enabled', None),
            'pixel_ratio': as_dict.get('pixelRatio', None),
            'series_threshold': as_dict.get('seriesThreshold', None),
            'use_gpu_translations': as_dict.get('useGPUTranslations', None),
            'use_preallocated': as_dict.get('usePreallocated', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allowForce': self.allow_force,
            'debug': self.debug,
            'enabled': self.enabled,
            'pixelRatio': self.pixel_ratio,
            'seriesThreshold': self.series_threshold,
            'useGPUTranslations': self.use_gpu_translations,
            'usePreallocated': self.use_preallocated
        }

        return untrimmed
