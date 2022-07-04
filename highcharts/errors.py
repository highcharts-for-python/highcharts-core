
class HighchartsError(ValueError):
    """Basic error that all other Highcharts for Python exceptions inherit from."""
    pass


class ImplementationError(HighchartsError):
    """Error that indicates you have implemented something incorrectly in your code."""
    pass


class HighchartsValueError(ImplementationError):
    """:exc:`ValueError <python:ValueError>` encountered in the operation of Highcharts
    for Python. Typically an implementation error.
    """
    pass

class NotSupportedError(HighchartsError, TypeError):
    """:exc:`TypeError <python:TypeError>` encountered when attempting functionality that
    is not (and is not intended to be) supported."""
    pass
