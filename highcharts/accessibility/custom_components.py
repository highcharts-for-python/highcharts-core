from highcharts.metaclasses import JavaScriptDict


class CustomComponents(JavaScriptDict):
    """A hook for adding custom components to the accessibility module.

    .. note::

      This class operates as a basic :class:`dict <python:dict>`, however with certain
      validation rules applied to keys and values:

        #. First, dictionary keys must all be valid variable names (no spaces, cannot start
           with numbers, etc.).
        #. Second, values must themselves be strings. It is expected that these strings will
           contain the JavaScript code you wish to return, but there is no validation
           performed on the code itself (just validating that the value is a string).

    The keys in this class are expected to be component names, while their values are
    expected to be instances of JavaScript classes inheriting from the
    `Highcharts.AccessibilityComponent <https://api.highcharts.com/class-reference/Highcharts.AccessibilityComponent>`_
    base class.

    .. hint::

      Remember to add the component to the :meth:`Accessibility.keyboard_navigation.order`
      for the keyboard navigation to be usable.

    """
    pass
