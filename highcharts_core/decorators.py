"""Implements decorators used throughout the library."""
import json
from functools import wraps
from collections import UserDict

from validator_collection import checkers

from highcharts_core import errors, constants


def validate_types(value,
                   types = None,
                   allow_dict = True,
                   allow_json = True,
                   allow_none = True,
                   allow_js_literal = True,
                   force_iterable = False,
                   function_name = None):
    """Validates that ``value`` is one or more of the allowed types, where the first
    type passed in ``types`` is the primary type that it will be returned as.

    :param value: The value to be validated.
    :type value: Any

    :param types: :class:`type <python:type>` object or iterable of
      :class:`type <python:type>` objects used to indicate which types are allowed. The
      first (or only) item in ``types`` will indicate the primary type that ``value`` will
      be returned as.
    :types: :class:`type <python:type>` or iterable of :class:`type <python:type>`

    :param allow_dict: If ``True``, will accept a :class:`dict <python:dict>` object as
      ``value``. Defaults to ``True``.
    :type allow_dict: :class:`bool <python:bool>`

    :param allow_json: If ``True``, will accept a :class:`str <python:str>` object as
      ``value``, under the assumption that is is deserializable as JSON. Defaults to
      ``True``.
    :type allow_json: :class:`bool <python:bool>`

    :param allow_none: If ``True``, will accept an empty or :obj:`None <python:None>`
      object as ``value``. Defaults to ``True``.
    :type allow_none: :class:`bool <python:bool>`

    :param allow_js_literal: If ``True``, will accept a :class:`str <python:str>` object
      as ``value``, under the assumption that it is deserializable as a JavaScript object
      literal. Defaults to ``True``.
    :type allow_js_literal: :class:`bool <python:bool>`

    :param force_iterable: If ``True``, will accept an iterable object as ``value``.
      Defaults to ``False`` (because most attributes are just singletons).
    :type force_iterable: :class:`bool <python:bool>`

    :param function_name: The optional name of the function that was originally called.
    :type function_name: :class:`str <python:str>`

    :returns: ``value`` de-serialized to the primary type (first
      :class:`type <python:type>` in ``types``)
    :rtype: first :class:`type <python:type>` in ``types``

    :raises HighchartsImplementationError: if ``types`` is empty

    :raises HighchartsValueError: if ``types`` does not contain a
      :class:`type <python:type>` or iterable of :class:`type <python:type>` objects

    :raises HighchartsValueError: if the primary type does not conform to the
      :class:`HighchartsMeta` interface definition

    """
    if not types:
        raise errors.HighchartsImplementationError('types cannot be empty - must be a type or '
                                         'iterable of types')

    if not types:
        raise errors.HighchartsImplementationError('types cannot be empty - must be a type or '
                                         'iterable of types')

    try:
        types_list = [x for x in types]
    except TypeError:
        types_list = [types]

    for item in types_list:
        if not isinstance(item, type):
            raise errors.HighchartsValueError(f'types must contain one or more type '
                                              f'objects. Received a {type(item)}.')

    primary_type = types_list[0]
    if not hasattr(primary_type, 'from_js_literal'):
        allow_js_literal = False

    if allow_none and force_iterable and checkers.is_iterable(value) and not value:
        value = []
    elif allow_none and isinstance(value, constants.EnforcedNullType):
        pass
    elif allow_none and not value:
        value = None
    elif not allow_none and not value:
        raise errors.HighchartsValueError('value is not expected to be empty, but was '
                                          'empty')
    elif allow_dict and isinstance(value, dict):
        try:
            value = primary_type.from_dict(value)
        except AttributeError as error:
            if not hasattr(primary_type, 'from_dict'):
                raise errors.HighchartsValueError(f'supplied type '
                                                  f'({primary_type.__name__}) '
                                                  f'does not conform to the '
                                                  f'HighchartsMeta interface')
            else:
                raise error
    elif allow_js_literal and isinstance(value, str):
        try:
            value = primary_type.from_js_literal(value)
        except ValueError:
            pass

    if (
        force_iterable and
        checkers.is_iterable(value, forbid_literals = (str, dict, bytes, UserDict)) and
        hasattr(primary_type, 'from_array')
    ):
        value = primary_type.from_array(value)
    elif allow_json and isinstance(value, (str, bytes)):
        try:
            value = primary_type.from_json(value)
        except AttributeError:
            raise errors.HighchartsValueError(f'supplied type '
                                              f'({primary_type.__class__.__name__}) '
                                              f'does not conform to the '
                                              f'HighchartsMeta interface')
        except TypeError:
            value = json.loads(value)

    if force_iterable and checkers.is_iterable(value):
        value = [validate_types(x,
                                types = types,
                                allow_dict = allow_dict,
                                allow_json = allow_json,
                                allow_js_literal = allow_js_literal,
                                force_iterable = force_iterable)
                 for x in value]
    elif allow_none and isinstance(value, constants.EnforcedNullType):
        pass
    elif allow_none and not value:
        pass
    elif not isinstance(value, primary_type):
        error_string = f'expects a {primary_type.__name__}'
        if function_name:
            error_string = f'{function_name} ' + error_string

        allow_js = allow_json or allow_js_literal
        if allow_dict and allow_js and force_iterable and allow_none:
            error_string += ', dict, str, iterable, or empty object.'
        elif allow_dict and allow_js and force_iterable:
            error_string += ', dict, str, or iterable object.'
        elif allow_dict and allow_js and allow_none:
            error_string += ', dict, str, or empty object.'
        elif allow_dict and force_iterable and allow_none:
            error_string += ', dict, iterable, or empty object.'
        elif allow_dict and allow_js:
            error_string += ', dict, or str object.'
        elif allow_dict and force_iterable:
            error_string += ', dict, or iterable object.'
        elif allow_dict and allow_none:
            error_string += ', dict, or empty object.'
        elif allow_js and force_iterable:
            error_string += ', str, or iterable object.'
        elif allow_js and allow_none:
            error_string += ', str, or empty object.'
        elif force_iterable and allow_none:
            error_string += ', iterable, or empty object.'
        elif allow_js:
            error_string += ' or str object.'
        elif force_iterable:
            error_string += ' or iterable object.'
        elif allow_none:
            error_string += ' or empty object.'

        error_string += f' Received {value.__class__.__name__}.'

        raise errors.HighchartsValueError(error_string)

    return value


def class_sensitive(types = None,
                    allow_dict = True,
                    allow_json = True,
                    allow_none = True,
                    allow_js_literal = True,
                    force_iterable = False):
    """Validates that the values passed to a decorated function or method are
    de-serialized to the appropriate type.

    :param types: :class:`type <python:type>` object or iterable of
      :class:`type <python:type>` objects used to indicate which types are allowed. The
      first (or only) item in ``types`` will indicate the primary type that ``value`` will
      be returned as.
    :types: :class:`type <python:type>` or iterable of :class:`type <python:type>`

    :param allow_dict: If ``True``, will accept a :class:`dict <python:dict>` object as
      ``value``. Defaults to ``True``.
    :type allow_dict: :class:`bool <python:bool>`

    :param allow_json: If ``True``, will accept a :class:`str <python:str>` object as
      ``value``, under the assumption that is is deserializable as JSON. Defaults to
      ``True``.
    :type allow_json: :class:`bool <python:bool>`

    :param allow_none: If ``True``, will accept an empty or :obj:`None <python:None>`
      object as ``value``. Defaults to ``True``.
    :type allow_none: :class:`bool <python:bool>`

    :param allow_js_literal: If ``True``, will accept a :class:`str <python:str>` object
      as ``value``, under the assumption that it is deserializable as a JavaScript object
      literal. Defaults to ``True``.
    :type allow_js_literal: :class:`bool <python:bool>`

    :param force_iterable: If ``True``, will accept an iterable object as ``value``.
      Defaults to ``False`` (because most attributes are just singletons).
    :type force_iterable: :class:`bool <python:bool>`

    .. note::

      To apply the decorator to a property setter method (the most-common use case), place
      it *after* the ``@<property name>.setter`` decorator and directly above the function
      name like so:

      .. code-block:: python

        @some_property.setter
        @class_sensitive(...)
        def some_property(self, value):
            ...

    :returns: The result of the decorated function or method having validated the class
      typing.

    :raises HighchartsImplementationError: if ``types`` is empty

    :raises HighchartsValueError: if ``types`` does not contain a
      :class:`type <python:type>` or iterable of :class:`type <python:type>` objects

    :raises HighchartsValueError: if the primary type does not conform to the
      :class:`HighchartsMeta` interface definition

    """
    def decorator(func):
        @wraps(func)
        def func_wrapper(*args,
                         **kwargs):
            function_name = func.__name__

            try:
                value = args[1]
            except IndexError:
                raise errors.HighchartsError('Something went wrong. Unsure how this '
                                             'might happen.')

            value = validate_types(value,
                                   types = types,
                                   allow_dict = allow_dict,
                                   allow_json = allow_json,
                                   allow_none = allow_none,
                                   allow_js_literal = allow_js_literal,
                                   force_iterable = force_iterable,
                                   function_name = function_name)

            result = func(args[0], value)

            return result

        return func_wrapper

    return decorator
