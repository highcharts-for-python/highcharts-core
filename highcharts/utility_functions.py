"""Collection of utility functions used across the library."""


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
