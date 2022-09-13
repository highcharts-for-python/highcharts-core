##################################
Error Reference
##################################

.. module:: highcharts_python.errors

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
      :top-classes: Exception
      :parts: -1

----------------

HighchartsDependencyError (from :exc:`ImportError <python:ImportError>`)
==========================================================================================

.. autoexception:: HighchartsDependencyError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsDependencyError
      :top-classes: Exception
      :parts: -1

-----------------

HighchartsImplementationError (from :exc:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsImplementationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsImplementationError
      :top-classes: Exception
      :parts: -1

------------------

HighchartsValueError (from :exc:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsValueError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsValueError
      :top-classes: Exception
      :parts: -1

--------------------

HighchartsNotSupportedError (from :exc:`ValueError <python:ValueError>` and :exc:`TypeError <python:TypeError>`)
====================================================================================================================================

.. autoexception:: HighchartsNotSupportedError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsNotSupportedError
      :top-classes: Exception
      :parts: -1

--------------

HighchartsJavaScriptError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsJavaScriptError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsJavaScriptError
      :top-classes: Exception
      :parts: -1

---------------

HighchartsParseError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsParseError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsParseError
      :top-classes: Exception
      :parts: -1

--------------

HighchartsCSVDeserializationError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsCSVDeserializationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsCSVDeserializationError
      :top-classes: Exception
      :parts: -1

--------------

HighchartsMissingKeyError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsMissingKeyError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMissingKeyError
      :top-classes: Exception
      :parts: -1

----------------

HighchartsCollectionError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsCollectionError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsCollectionError
      :top-classes: Exception
      :parts: -1

--------------

HighchartsVariableDeclarationError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsVariableDeclarationError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsVariableDeclarationError
      :top-classes: Exception
      :parts: -1

-------------

HighchartsMissingClassNameError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsMissingClassNameError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMissingClassNameError
      :top-classes: Exception
      :parts: -1

---------------

HighchartsExportServerError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsExportServerError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsExportServerError
      :top-classes: Exception
      :parts: -1

--------------

HighchartsUnsupportedProtocolError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsUnsupportedProtocolError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsUnsupportedProtocolError
      :top-classes: Exception
      :parts: -1

--------------

HighchartsUnsupportedExportTypeError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsUnsupportedExportTypeError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsUnsupportedExportTypeError
      :top-classes: Exception
      :parts: -1

------------------

HighchartsUnsupportedConstructorError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsUnsupportedConstructorError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsUnsupportedConstructorError
      :top-classes: Exception
      :parts: -1

------------

HighchartsMissingExportSettingsError (from :class:`ValueError <python:ValueError>`)
==========================================================================================

.. autoexception:: HighchartsMissingExportSettingsError

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMissingExportSettingsError
      :top-classes: Exception
      :parts: -1
