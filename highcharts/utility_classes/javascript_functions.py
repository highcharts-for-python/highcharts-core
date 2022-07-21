from typing import Optional, List

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class CallbackFunction(HighchartsMeta):
    """Representation of a JavaScript callback function's source code."""

    def __init__(self, **kwargs):
        self._function_name = None
        self._arguments = None
        self._body = None

        self.function_name = kwargs.pop('function_name', None)
        self.arguments = kwargs.pop('arguments', None)
        self.body = kwargs.pop('body', None)

    @property
    def function_name(self) -> Optional[str]:
        """An optional name to be given to the function.

        .. warning::

          Most Highcharts Callback function definitions are anonymous, meaning that they
          are named within the object into which they are embedded. As a result,
          this setting should be used sparingly.

        :rtype: :class:`str <python:str>`
        """
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = validators.variable_name(value, allow_empty = True)

    @property
    def arguments(self) -> Optional[List[str]]:
        """Collection of named arguments (parameters) that will be passed to the function.

        :rtype: :class:`list <python:list>` of :obj:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._arguments

    @arguments.setter
    def arguments(self, value):
        if not value:
            self._arguments = None
        else:
            self._arguments = [validators.variable_name(x)
                               for x in validators.iterable(value)]

    @property
    def body(self) -> Optional[str]:
        """The source code of the function itself.

        .. note::

          Should *not* be wrapped in ``{ ... }``. It should just be the source code of the
          the function itself.

        .. hint::

          When writing this code in Python, it is best to use the three-quotation-mark
          string pattern, like so:

          .. code-block:: python

            callback = CallbackFunction()
            callback.body = \"\"\"
            ... some JavaScript logic goes here
            \"\"\"

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._body

    @body.setter
    def body(self, value):
        self._body = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'function_name': as_dict.pop('function_name', None),
            'arguments': as_dict.pop('arguments', None),
            'body': as_dict.pop('body', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        return self.trim_dict({
            'function_name': self.function_name,
            'arguments': self.arguments,
            'body': self.body
        })
