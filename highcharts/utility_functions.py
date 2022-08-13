"""Collection of utility functions used across the library."""

from validator_collection import validators

from highcharts import errors


def mro_to_dict(obj):
    """Work through ``obj``'s multiple parent classes, executing the appropriate
    ``to_dict()`` method for each parent and consolidaitng the results to a single
    :class:`dict <python:dict>`.

    :param obj: An object that has a ``to_dict()`` method.

    :rtype: :class:`dict <python:dict>`
    """
    if not hasattr(obj, 'to_dict'):
        raise TypeError('obj does not have a to_dict() method.')

    classes = [x for x in obj.__class__.mro()
               if x.__name__ != 'object']
    as_dict = {}

    for item in classes:
        has_to_dict = hasattr(super(item, obj), 'to_dict')
        if not has_to_dict:
            break

        try:
            item_dict = super(item, obj).to_dict()
        except (NotImplementedError, AttributeError):
            continue
        for key in item_dict:
            as_dict[key] = item_dict[key]

    return as_dict


def validate_color(value):
    """Validate that ``value`` is either a :class:`Gradient`, :class:`Pattern`, or a
    :class:`str <python:str>`.

    :param value: The value to validate.

    :returns: The validated value.
    :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
      :obj:`None <python:None>`
    """
    from highcharts.utility_classes.gradients import Gradient
    from highcharts.utility_classes.patterns import Pattern

    if not value:
        return None
    elif isinstance(value, (Gradient, Pattern)):
        return value
    elif isinstance(value, (dict, str)) and 'linearGradient' in value:
        try:
            value = Gradient.from_json(value)
        except ValueError:
            if isinstance(value, dict):
                value = Gradient.from_dict(value)
            else:
                value = validators.string(value)
    elif isinstance(value, dict) and 'linear_gradient' in value:
        value = Gradient(**value)
    elif isinstance(value, (dict, str)) and 'patternOptions' in value:
        try:
            value = Pattern.from_json(value)
        except ValueError:
            if isinstance(value, dict):
                value = Pattern.from_dict(value)
            else:
                value = validators.string(value)
    elif isinstance(value, dict) and 'pattern_options' in value:
        value = Pattern(**value)
    elif isinstance(value, str):
        value = validators.string(value)
    else:
        raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                          f'Gradient, or Pattern. Value received '
                                          f'was: {value}')

    return value
