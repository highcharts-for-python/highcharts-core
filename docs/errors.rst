##################################
Error Reference
##################################

.. module:: highcharts_core.errors

.. contents::
  :local:
  :depth: 3
  :backlinks: entry

----------

*******************
Handling Errors
*******************

Because **Highcharts for Python** produces exceptions which inherit from the
standard library, it leverages the same API for handling stack trace information.
This means that it will be handled just like a normal exception in unit test
frameworks, logging solutions, and other tools that might need that information.

------------------

************************************
Highcharts for Python Errors
************************************

HighchartsError (from :exc:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsError
      :parts: -1

----------------

HighchartsDependencyError (from :exc:`ImportError <python:ImportError>`)
==========================================================================================

.. autoexception:: HighchartsDependencyError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsDependencyError
      :parts: -1

-----------------

HighchartsReadOnlyError (from :exc:`ValueError <python:ValueError>` and :exc:`AttributeError <python:AttributeError>`)
=============================================================================================================================

.. autoexception:: HighchartsReadOnlyError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsReadOnlyError
      :parts: -1

-----------------

HighchartsImplementationError (from :exc:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsImplementationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsImplementationError
      :parts: -1

------------------

HighchartsValueError (from :exc:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsValueError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsValueError
      :parts: -1

--------------------

HighchartsNotSupportedError (from :exc:`ValueError <python:ValueError>` and :exc:`TypeError <python:TypeError>`)
====================================================================================================================================

.. autoexception:: HighchartsNotSupportedError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsNotSupportedError
      :parts: -1

--------------

HighchartsJavaScriptError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsJavaScriptError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsJavaScriptError
      :parts: -1

---------------

HighchartsParseError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsParseError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsParseError
      :parts: -1

--------------

HighchartsCSVDeserializationError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsCSVDeserializationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsCSVDeserializationError
      :parts: -1

--------------

HighchartsPandasDeserializationError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsPandasDeserializationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsPandasDeserializationError
      :parts: -1

--------------

HighchartsPySparkDeserializationError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsPySparkDeserializationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsPySparkDeserializationError
      :parts: -1

--------------

HighchartsMissingKeyError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsMissingKeyError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMissingKeyError
      :parts: -1

----------------

HighchartsCollectionError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsCollectionError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsCollectionError
      :parts: -1

--------------

HighchartsVariableDeclarationError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsVariableDeclarationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsVariableDeclarationError
      :parts: -1

-------------

HighchartsMissingClassNameError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsMissingClassNameError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMissingClassNameError
      :parts: -1

---------------

HighchartsExportServerError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsExportServerError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsExportServerError
      :parts: -1

--------------

HighchartsUnsupportedProtocolError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsUnsupportedProtocolError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsUnsupportedProtocolError
      :parts: -1

--------------

HighchartsUnsupportedExportError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsUnsupportedExportError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsUnsupportedExportError
      :parts: -1

--------------

HighchartsUnsupportedExportTypeError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsUnsupportedExportTypeError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsUnsupportedExportTypeError
      :parts: -1

------------------

HighchartsUnsupportedConstructorError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsUnsupportedConstructorError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsUnsupportedConstructorError
      :parts: -1

------------

HighchartsMissingExportSettingsError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsMissingExportSettingsError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMissingExportSettingsError
      :parts: -1

------------

HighchartsMissingSeriesError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsMissingSeriesError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMissingSeriesError
      :parts: -1

------------

HighchartsPythonConversionError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsPythonConversionError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsPythonConversionError
      :parts: -1

------------

HighchartsModerationError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsModerationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsModerationError
      :parts: -1

