
class HighchartsError(ValueError):
    """Basic error that all other Highcharts for Python exceptions inherit from."""
    pass


class HighchartsDependencyError(ImportError):
    """:exc:`ImportError <python:ImportError>` encountered when attempting to use a
    **Highcharts for Python** method that relies on a third-party library (e.g.
    `pandas <https://pandas.pydata.org>`_,
    `PySpark <https://spark.apache.org/docs/latest/api/python/>`_, etc.) which is not
    available in the runtime environment."""
    pass


class HighchartsReadOnlyError(HighchartsError, AttributeError):
    """:exc:`AttributeError <python:AttributeError>` encountered when attempting to set
    a **Highcharts for Python** property that is only available as a read-only property.
    """


class HighchartsImplementationError(HighchartsError):
    """Error that indicates you have implemented something incorrectly in your code."""
    pass


class HighchartsValueError(HighchartsImplementationError):
    """:exc:`ValueError <python:ValueError>` encountered in the operation of Highcharts
    for Python. Typically an implementation error.
    """
    pass


class HighchartsNotSupportedError(HighchartsError, TypeError):
    """:exc:`TypeError <python:TypeError>` encountered when attempting functionality that
    is not (and is not intended to be) supported."""
    pass


class HighchartsJavaScriptError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when a Python representation of
    some JavaScript code has been badly constructed. Typically an implementation error in
    your source code."""
    pass


class HighchartsParseError(HighchartsError):
    """:exc:`ValueError <python:ValueError>` encountered when Highcharts for Python is
    unable to parse a JavaScript object literal correctly."""
    pass


class HighchartsCSVDeserializationError(HighchartsError):
    """:exc:`ValueError <python:ValueError>` encountered when Highcharts for Python is
    unable to properly deserialize CSV data."""
    pass


class HighchartsPandasDeserializationError(HighchartsError):
    """:exc:`ValueError <python:ValueError>` encountered when Highcharts for Python is
    unable to properly deserialize Pandas data."""
    pass


class HighchartsPySparkDeserializationError(HighchartsError):
    """:exc:`ValueError <python:ValueError>` encountered when Highcharts for Python is
    unable to properly deserialize PySpark data."""
    pass


class HighchartsMissingKeyError(HighchartsParseError):
    """:exc:`ValueError <python:ValueError>` encountered when Highcharts for Python
    encounters a missing key when parsing a JavaScript object literal."""
    pass


class HighchartsCollectionError(HighchartsParseError):
    """:exc:`ValueError <python:ValueError>` encountered when Highcharts for Python
    encounters a collection with more members than expected when parsing a JavaScript
    object literal."""
    pass


class HighchartsVariableDeclarationError(HighchartsParseError):
    """:exc:`ValueError <python:ValueError>` encountered when Highcharts for Python
    tries to parse JavaScript code which is not represented as a proper variable
    declaration, and is unable to coerce the JavaScript code into a properly-formed
    variable declaration."""
    pass


class HighchartsMissingClassNameError(HighchartsJavaScriptError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to serialize a
    JavaScriptClass instance to JavaScript, but the instance has no class_name provided.
    """
    pass


class HighchartsExportServerError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to use the Node
    Export Server."""
    pass


class HighchartsUnsupportedProtocolError(HighchartsExportServerError):
    """:exc:`ValueError <pythoN:ValueError>` encountered when trying to use an unsupported
    protocol to communicate with the :term:`Export Server`."""
    pass


class HighchartsUnsupportedExportError(HighchartsExportServerError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to export a series type that 
    is not yet supported by the :term:`Export Server`.
    """
    pass

class HighchartsUnsupportedExportTypeError(HighchartsExportServerError):
    """:exc:`ValueError <python:ValueError>` encountered when requesting an unsupported
    image type from a :term:`Export Server`."""
    pass


class HighchartsUnsupportedConstructorError(HighchartsExportServerError):
    """:exc:`ValueError <python:ValueError>` encountered when supplying an unsupported
    constructor to an :term:`Export Server` instance."""
    pass


class HighchartsMissingExportSettingsError(HighchartsExportServerError):
    """:exc:`ValueError <python:ValueError>` encountered when attempting to
    programmatically export a chart image, but key settings were not supplied to the
    :class:`ExportServer` instance."""
    pass


class HighchartsMissingSeriesError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to reference a
    series that does not actually exist in the chart."""
    pass


class HighchartsPythonConversionError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when a generative AI model
    failed to convert a Python callable into a valid JavaScript function."""
    pass


class HighchartsModerationError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when a generative AI model
    determined that the content supplied to it fails its content moderation criteria."""
    pass