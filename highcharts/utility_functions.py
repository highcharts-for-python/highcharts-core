

def mro_to_dict(obj):
    """Work through ``obj``'s multiple parent classes, executing the appropriate
    ``to_dict()`` method for each parent and consolidaitng the results to a single
    :class:`dict <python:dict>`.

    :param obj: An object that has a ``to_dict()`` method.

    :rtype: :class:`dict <python:dict>`
    """
    if not hasattr(obj, 'to_dict'):
        raise TypeError('obj does not have a to_dict() method.')

    classes = obj.__class__.__mro__
    as_dict = {}

    for item in classes:
        if not hasattr(item, 'to_dict'):
            break

        item_dict = super(item, obj).to_dict()
        for key in item_dict:
            as_dict[key] = item_dict[key]

    return as_dict


def mro_init(obj, kwargs) -> None:
    """Work through the ``obj``'s multiple parent classes, executing the appropriate
    constructor (``__init__()``) method for each parent.

    :param obj: The object whose parent constructors will be executed.

    :param kwargs: The keyword arguments to pass to the constructor.
    :type kwargs: :class:`dict <python:dict>`

    """
    classes = obj.__class__.__mro__

    for item in classes:
        super(item, obj).__init__(**kwargs)
