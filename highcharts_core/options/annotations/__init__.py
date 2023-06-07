from typing import Optional, List

from validator_collection import validators

from highcharts_core import constants, errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta

from highcharts_core.options.annotations.animation import AnnotationAnimation
from highcharts_core.options.annotations.control_point_options import AnnotationControlPointOption
from highcharts_core.options.annotations.events import AnnotationEvent
from highcharts_core.options.annotations.label_options import LabelOptions
from highcharts_core.options.annotations.label_options import AnnotationLabel
from highcharts_core.options.annotations.shape_options import ShapeOptions
from highcharts_core.options.annotations.shape_options import AnnotationShape


class Annotation(HighchartsMeta):
    """A basic type of an annotation. It allows adding custom labels or shapes. The
    items can be tied to points, axis coordinates or chart pixel coordinates."""

    def __init__(self, **kwargs):
        self._animation = None
        self._control_point_options = None
        self._crop = None
        self._draggable = None
        self._events = None
        self._id = None
        self._label_options = None
        self._labels = None
        self._shape_options = None
        self._shapes = None
        self._visible = None
        self._z_index = None

        self.animation = kwargs.get('animation', None)
        self.control_point_options = kwargs.get('control_point_options', None)
        self.crop = kwargs.get('crop', None)
        self.draggable = kwargs.get('draggable', None)
        self.events = kwargs.get('events', None)
        self.id = kwargs.get('id', None)
        self.label_options = kwargs.get('label_options', None)
        self.labels = kwargs.get('labels', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.shapes = kwargs.get('shapes', None)
        self.visible = kwargs.get('visible', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations'

    @property
    def animation(self) -> Optional[AnnotationAnimation]:
        """Enable or disable the initial animation when a series is displayed for the
        annotation. If not :obj:`None <python:None>`, is enabled. Otherwise, disabled.

        .. warning::

          This option only applies to the initial animation.

          For other animations, see ``chart.animation`` and the animation parameter under
          the API methods.

        :returns: The configuration settings for the annotation animation.
        :rtype: :class:`AnnotationAnimation`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnnotationAnimation)
    def animation(self, value):
        self._animation = value

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Options for annotation's control points.

        Each control point inherits options from this property, though the global
        options can be overwritten by options in a specific control point.

        :returns: Options configuring the annotations' control points.
        :rtype: :class:`AnnotationControlPointOption` or :obj:`None <python:None>`

        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def crop(self) -> Optional[bool]:
        """If ``True``, hide the part of the annotation that is outside the plot area.
        Defaults to ``True``.

        :returns: Flag indicating whether to clip an annotation that extends beyond the
          plot area.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crop

    @crop.setter
    def crop(self, value):
        if value is None:
            self._crop = None
        else:
            self._crop = bool(value)

    @property
    def draggable(self) -> Optional[str]:
        """Setting that allows an annotation to be draggable by a user. Defaults to
        ``'xy'``

        Supports values:

          * ``'x'``
          * ``'xy'``
          * ``'y'``
          * ``''`` (empty string - disables dragging)

        :returns: Configuration of annotation dragging by the user.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises HighchartsValueError: if an unsupported value is supplied
        """
        return self._draggable

    @draggable.setter
    def draggable(self, value):
        if value is None:
            self._draggable = None
        else:
            value = validators.string(value, allow_empty = True) or ''
            value = value.lower()
            if value not in ['x', 'xy', 'y', '']:
                raise errors.HighchartsValueError(f'draggable must be "x", "xy", "y", '
                                                  f'or "". Was: {value}')
            self._draggable = value

    @property
    def events(self) -> Optional[AnnotationEvent]:
        """JavaScript callback functions that fire in response to annotation-related
        events.

        :returns: Callback functions that fire in response to annotation-related events.
        :rtype: :class:`AnnotationEvent` or :obj:`None <python:None>`

        """
        return self._events

    @events.setter
    @class_sensitive(AnnotationEvent)
    def events(self, value):
        self._events = value

    @property
    def id(self) -> Optional[str]:
        """Sets an ID for the annotation. Can be user later when removing an annotation
        using the JavaScript ``Chart.removeAnnotation(id)`` method.

        :returns: The ID for the annotation.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Global options applied to all annotation labels.

        .. note::

          An option from the :meth:`Annotation.label_options` can be overwritten by the
          configuration for a specific label.

        :returns: Configuration options for annotation labels.
        :rtype: :class:`LabelOptions` or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def labels(self) -> Optional[List[AnnotationLabel]]:
        """An array of labels to display for annotations.

        .. seealso::

          * :meth:`Annotation.label_options`
          * :class:`LabelOptions`

        :returns: A collection of labels to display for annotation.
        :rtype: :class:`list <python:list>` of :class:`AnnotationLabel` or
          :obj:`None <python:None>`
        """
        return self._labels

    @labels.setter
    @class_sensitive(AnnotationLabel, force_iterable = True)
    def labels(self, value):
        self._labels = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Global options applied to all annotation shapes.

        .. note::

          An option from the :meth:`Annotation.shape_options` can be overwritten by the
          configuration for a specific shape.

        :returns: Configuration options for annotation shapes.
        :rtype: :class:`ShapeOptions` or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def shapes(self) -> Optional[List[AnnotationShape]]:
        """An array of shapes to display for annotations.

        .. seealso::

          * :meth:`Annotation.shape_options`
          * :class:`shapeOptions`

        :returns: A collection of shapes to display for annotation.
        :rtype: :class:`list <python:list>` of :class:`AnnotationShape` or
          :obj:`None <python:None>`
        """
        return self._shapes

    @shapes.setter
    @class_sensitive(AnnotationShape, force_iterable = True)
    def shapes(self, value):
        self._shapes = value

    @property
    def visible(self) -> Optional[bool]:
        """If ``True``, indicates the annotation is visible.

        :returns: Flag which indicates whether the annotation is visible or not.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value is None:
            self._visible = None
        else:
            self._visible = bool(value)

    @property
    def z_index(self) -> Optional[int]:
        """The Z-Index for the annotation. Defaults to ``6``.

        :returns: The z-index for the annotation.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.integer(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.get('animation', None),
            'control_point_options': as_dict.get('controlPointOptions', None),
            'crop': as_dict.get('crop', None),
            'draggable': as_dict.get('draggable', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_options': as_dict.get('labelOptions', None),
            'labels': as_dict.get('labels', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'shapes': as_dict.get('shapes', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'animation': self.animation,
            'controlPointOptions': self.control_point_options,
            'crop': self.crop,
            'draggable': self.draggable,
            'events': self.events,
            'id': self.id,
            'labelOptions': self.label_options,
            'labels': self.labels,
            'shapeOptions': self.shape_options,
            'shapes': self.shapes,
            'visible': self.visible,
            'zIndex': self.z_index
        }

        return untrimmed
