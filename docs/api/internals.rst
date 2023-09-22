#################################
Library Internals
#################################

.. contents:: Section Contents
  :local:
  :depth: 3
  :backlinks: entry

--------------

.. module:: highcharts_core.metaclasses

******************************************************************************
module: :mod:`.metaclasses <highcharts_core.metaclasses>`
******************************************************************************

The :mod:`.metaclasses <highcharts_core.metaclasses>` module contains - as one might
expect - :term:`metaclasses <metaclass>` that are used to ensure a consistent interface
throughout the **Highcharts for Python** library.


class: :class:`HighchartsMeta <highcharts_core.metaclasses.HighchartsMeta>`
===================================================================================

.. autoclass:: HighchartsMeta
  :members:
  :inherited-members:
  :private-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMeta
      :parts: -1

  |

class: :class:`JavaScriptDict <highcharts_core.metaclasses.JavaScriptDict>`
====================================================================================

.. autoclass:: JavaScriptDict
  :members:
  :inherited-members:
  :private-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: JavaScriptDict
      :parts: -1

  |

----------------------

.. module:: highcharts_core.decorators

******************************************************************************
module: :mod:`.decorators <highcharts_core.decorators>`
******************************************************************************

The :mod:`.decorators <highcharts_core.decorators>` module contains decorators and
decorator-assisting functions used throughout the **Highcharts for Python** library.

decorator: :deco:`@class_sensitive <highcharts_core.decorators.class_sensitive>`
=======================================================================================

.. autodecorator:: class_sensitive

function: :func:`validate_types() <highcharts_core.decorators.validate_types>`
===================================================================================

.. autofunction:: validate_types

----------------------------------

.. module:: highcharts_core.js_literal_functions

******************************************************************************************
module:: :mod:`.js_literal_functions <highcharts_core.js_literal_functions>`
******************************************************************************************

The :mod:`.js_literal_functions <highcharts_core.js_literal_functions>` module contains
functions that are used to parse, process, de-serialize, and serialize JavaScript literal
notation.

function: :func:`serialize_to_js_literal() <highcharts_core.js_literal_functions.serialize_to_js_literal>`
===================================================================================================================================

.. autofunction:: serialize_to_js_literal

function: :func:`attempt_variable_declaration() <highcharts_core.js_literal_functions.attempt_variable_declaration>`
===================================================================================================================================

.. autofunction:: attempt_variable_declaration

function: :func:`is_js_function_or_class() <highcharts_core.js_literal_functions.is_js_function_or_class>`
===================================================================================================================================

.. autofunction:: is_js_function_or_class

function: :func:`get_js_literal() <highcharts_core.js_literal_functions.get_js_literal>`
===================================================================================================================================

.. autofunction:: get_js_literal

function: :func:`assemble_js_literal() <highcharts_core.js_literal_functions.assemble_js_literal>`
===================================================================================================================================

.. autofunction:: assemble_js_literal

function: :func:`convert_js_literal_to_python() <highcharts_core.js_literal_functions.convert_js_literal_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_literal_to_python

function: :func:`convert_js_property_to_python() <highcharts_core.js_literal_functions.convert_js_property_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_property_to_python

function: :func:`convert_js_to_python() <highcharts_core.js_literal_functions.convert_js_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_to_python

function: :func:`get_key_value_pairs() <highcharts_core.js_literal_functions.get_key_value_pairs>`
===================================================================================================================================

.. autofunction:: get_key_value_pairs

-------------------------

.. module:: highcharts_core.utility_functions

********************************************************************
:mod:`.utility_functions <highcharts_core.utility_functions>`
********************************************************************

The :mod:`.utility_functions <highcharts_core.utility_functions>` module contains a
small number of functions which serve as utilities across the **Highcharts for Python**
library. Think of it as a function "catch all" module.

function:: :func:`mro_to_dict() <highcharts_core.utility_functions.mro_to_dict>`
=====================================================================================================

.. autofunction:: mro_to_dict

function:: :func:`get_remaining_mro() <highcharts_core.utility_functions.get_remaining_mro>`
=====================================================================================================

.. autofunction:: get_remaining_mro

function:: :func:`mro__to_untrimmed_dict() <highcharts_core.utility_functions.mro__to_untrimmed_dict>`
==============================================================================================================

.. autofunction:: mro__to_untrimmed_dict

function:: :func:`validate_color() <highcharts_core.utility_functions.validate_color>`
=====================================================================================================

.. autofunction:: validate_color

function:: :func:`to_camelCase() <highcharts_core.utility_functions.to_camelCase>`
=====================================================================================================

.. autofunction:: to_camelCase

function:: :func:`to_snake_case() <highcharts_core.utility_functions.to_snake_case>`
=====================================================================================================

.. autofunction:: to_snake_case

function:: :func:`parse_csv() <highcharts_core.utility_functions.parse_csv>`
=====================================================================================================

.. autofunction:: parse_csv

--------------

.. module:: highcharts_core.ai

******************************************************************************
module: :mod:`.ai <highcharts_core.ai>`
******************************************************************************

The :mod:`.ai <highcharts_core.ai>` module contains - as one might
expect - functions that enable Highcharts for Python to communicate with
supported generative AI platforms. These functions are used to convert
Python callables to their JavaScript equivalents in the 
:meth:`CallbackFunction.from_python() <highcharts_core.utility_classes.javascript_functions.CallbackFunction.from_python>` method.

function:: :func:`convert_to_js() <highcharts_core.ai.convert_to_js>`
=====================================================================================================

.. autofunction:: convert_to_js

function:: :func:`openai_moderate() <highcharts_core.ai.openai_moderate>`
=====================================================================================================

.. autofunction:: openai_moderate

function:: :func:`openai_conversion() <highcharts_core.ai.openai_conversion>`
=====================================================================================================

.. autofunction:: openai_conversion

function:: :func:`anthropic_conversion() <highcharts_core.ai.anthropic_conversion>`
=====================================================================================================

.. autofunction:: anthropic_conversion

function:: :func:`get_source() <highcharts_core.ai.get_source>`
=====================================================================================================

.. autofunction:: get_source
