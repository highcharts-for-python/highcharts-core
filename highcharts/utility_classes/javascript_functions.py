from typing import Optional, List

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import validate_types
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

    def _to_untrimmed_dict(self) -> dict:
        return {
            'function_name': self.function_name,
            'arguments': self.arguments,
            'body': self.body
        }


class JavaScriptClass(HighchartsMeta):
    """Representation of a JavaScript class."""

    def __init__(self, **kwargs):
        self._methods = None

        self.methods = kwargs.pop('methods', None)

    @property
    def methods(self) -> Optional[List[CallbackFunction]]:
        """Collection of methods that are to be defined within the class. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          All methods *must* have a :meth:`function_name <CallbackFunction.function_name>`
          set.

        .. warning::

          One of the methods *must* have a
          :meth:`function_name <CallbackFunction.function_name>` of ``'constructor'`` and
          be used as a constructor for the class.

        .. note::

          For the sake of simplicity, the :class:`JavaScriptClass` does not support
          ECMAScript's more robust public/private field declaration syntax, nor does it
          support the definition of getters or generators.

        :rtype: :class:`list <python:list>` of :class:`CallbackFunction`, or
          :obj:`None <python:None>`
        """
        return self._methods

    @methods.setter
    def methods(self, value):
        if not value:
            self._methods = None
        else:
            value = validate_types(value,
                                   types = CallbackFunction,
                                   force_iterable = True)
            has_constructor = False
            for method in value:
                if not method.function_name:
                    raise errors.JavaScriptError('All JavaScriptClass methods '
                                                 'require a function name.')
                if method.function_name == 'constructor':
                    has_constructor = True

            if not has_constructor:
                raise errors.JavaScriptError('A JavaScriptClass requires at least '
                                             'one "constructor" method. Yours had none.')

            self._methods = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'methods': as_dict.pop('methods', None)
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        return {
            'methods': self.methods
        }
