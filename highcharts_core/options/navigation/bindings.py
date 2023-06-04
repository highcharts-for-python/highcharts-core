from typing import Optional, List

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta


class Binding(HighchartsMeta):
    """Basic interface for an event binding."""

    _class_name_default = None
    _max_steps = None

    def _private_setup(self, **kwargs):
        self._class_name_default = None
        self._max_steps = None

    def __init__(self, **kwargs):
        self._private_setup(**kwargs)

        self._init = None
        self._start = None
        self._steps = None
        self._end = None

        # Seems to be an out-dated functionality and is deprecated.
        # self._annotations_options = None

        self.class_name = kwargs.get('class_name', self._class_name_default)
        self.init = kwargs.get('init', None)
        self.start = kwargs.get('start', None)
        self.steps = kwargs.get('steps', None)
        self.end = kwargs.get('end', None)

        # Seems to be an out-dated functionality and is deprecated.
        # self.annotations_options = kwargs.get('annotations_options', None)

    @property
    def class_name(self) -> Optional[str]:
        """The classname used to bind events to.

        :rtype: :class:`str <python:str>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def init(self) -> Optional[str]:
        """The initial event, fired when the button is clicked.

        :rtype: :class:`str <python:str>`
        """
        return self._init

    @init.setter
    def init(self, value):
        self._init = validators.string(value, allow_empty = True)

    @property
    def start(self) -> Optional[str]:
        """Event fired on the first click on the first click.

        :rtype: :class:`str <python:str>`
        """
        return self._start

    @start.setter
    def start(self, value):
        self._start = validators.string(value, allow_empty = True)

    @property
    def steps(self) -> Optional[List[str]]:
        """Collection of sequential events, fired one after another on each of the user's
        clicks.

        .. note::

          The maximum number of events is controlled by a private property on the class,
          ``_max_steps``.

        :rtype: :class:`str <python:str>`
        """
        return self._steps

    @steps.setter
    def steps(self, value):
        if not value:
            self._steps = None
        else:
            value = validators.iterable(value, maximum_length = self._max_steps)
            self._steps = [validators.string(x) for x in value]

    @property
    def end(self) -> Optional[str]:
        """Last event to be called after the last step event.

        :rtype: :class:`str <python:str>`
        """
        return self._end

    @end.setter
    def end(self, value):
        self._end = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', cls._class_name_default),
            'init': as_dict.get('init', None),
            'start': as_dict.get('start', None),
            'steps': as_dict.get('steps', None),
            'end': as_dict.get('end', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'init': self.init,
            'start': self.start,
            'steps': self.steps,
            'end': self.end
        }

        return untrimmed


class CircleAnnotationBinding(Binding):
    """A circle annotation bindings. Includes ``start`` and one event in ``steps``
    array."""

    _class_name_default = 'highcharts-circle-annotation'
    _max_steps = 1

    def _private_setup(self, **kwargs):
        self._class_name_default = 'highcharts-circle-annotation'
        self._max_steps = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class EllipseAnnotationBinding(Binding):
    """A ellipse annotation bindings. Includes ``start`` and two events in the
    ``steps`` array. The first event updates the second point, responsible for the rx
    width, and the second updates the ry width."""

    _class_name_default = 'highcharts-ellipse-annotation'
    _max_steps = 2

    def _private_setup(self, **kwargs):
        self._class_name_default = 'highcharts-ellipse-annotation'
        self._max_steps = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LabelAnnotationBinding(Binding):
    """A label annotation binding. Includes ``start`` event only."""

    _class_name_default = 'highcharts-label-annotation'
    _max_steps = 0

    def _private_setup(self, **kwargs):
        self._class_name_default = 'highcharts-label-annotation'
        self._max_steps = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RectangleAnnotationBinding(Binding):
    """A rectangle annotation binding. Includes ``start`` and one event in the
    ``steps`` array."""

    _class_name_default = 'highcharts-rectangle-annotation'
    _max_steps = 1

    def _private_setup(self, **kwargs):
        self._class_name_default = 'highcharts-rectangle-annotation'
        self._max_steps = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Bindings(HighchartsMeta):
    """JavaScript event bindings for custom HTML buttons.

    Each JavaScript binding implements a simple event-driven interface:

      * ``class_name``: classname used to bind event to
      * ``init``: initial event, fired on button click
      * ``start``: fired on first click on a chart
      * ``steps``: array of sequential events fired one after another on each of users
        clicks
      * ``end``: last event to be called after last step event

    """

    def __init__(self, **kwargs):
        self._circle_annotation = None
        self._ellipse_annotation = None
        self._label_annotation = None
        self._rectangle_annotation = None

        self.circle_annotation = kwargs.get('circle_annotation', None)
        self.ellipse_annotation = kwargs.get('ellipse_annotation', None)
        self.label_annotation = kwargs.get('label_annotation', None)
        self.rectangle_annotation = kwargs.get('rectangle_annotation', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'navigation.bindings'

    @property
    def circle_annotation(self) -> Optional[CircleAnnotationBinding]:
        """A circle annotation bindings. Includes ``start`` and one event in ``steps``
        array.

        :rtype: :class:`CircleAnnotationBinding` or :obj:`None <python:None>`
        """
        return self._circle_annotation

    @circle_annotation.setter
    @class_sensitive(CircleAnnotationBinding)
    def circle_annotation(self, value):
        self._circle_annotation = value

    @property
    def ellipse_annotation(self) -> Optional[EllipseAnnotationBinding]:
        """A ellipse annotation bindings. Includes ``start`` and two events in the
        ``steps`` array. The first event updates the second point, responsible for the rx
        width, and the second updates the ry width.

        :rtype: :class:`EllipseAnnotationBinding` or :obj:`None <python:None>`
        """
        return self._ellipse_annotation

    @ellipse_annotation.setter
    @class_sensitive(EllipseAnnotationBinding)
    def ellipse_annotation(self, value):
        self._ellipse_annotation = value

    @property
    def label_annotation(self) -> Optional[LabelAnnotationBinding]:
        """A label annotation binding. Includes ``start`` event only.

        :rtype: :class:`LabelAnnotationBinding` or :obj:`None <python:None>`
        """
        return self._label_annotation

    @label_annotation.setter
    @class_sensitive(LabelAnnotationBinding)
    def label_annotation(self, value):
        self._label_annotation = value

    @property
    def rectangle_annotation(self) -> Optional[RectangleAnnotationBinding]:
        """A rectangle annotation bindings. Includes ``start`` and one event in the
        ``steps`` array.

        :rtype: :class:`RectangleAnnotationBinding` or :obj:`None <python:None>`
        """
        return self._rectangle_annotation

    @rectangle_annotation.setter
    @class_sensitive(RectangleAnnotationBinding)
    def rectangle_annotation(self, value):
        self._rectangle_annotation = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'circle_annotation': as_dict.get('circleAnnotation', None),
            'ellipse_annotation': as_dict.get('ellipseAnnotation', None),
            'label_annotation': as_dict.get('labelAnnotation', None),
            'rectangle_annotation': as_dict.get('rectangleAnnotation', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'circleAnnotation': self.circle_annotation,
            'ellipseAnnotation': self.ellipse_annotation,
            'labelAnnotation': self.label_annotation,
            'rectangleAnnotation': self.rectangle_annotation
        }

        return untrimmed
