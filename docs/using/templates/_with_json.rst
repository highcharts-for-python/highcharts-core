You can use the same exact pattern as using a JS literal with a JSON file instead.
We don't really think there's an advantage to this - but there might be one
significant disadvantage: JSON files cannot be used to provide JavaScript functions
to your Highcharts configuration. This means that formatters, event handlers, etc.
will not be applied through your shared options if you use a JSON file.

If your chart templates don't require JavaScript functions? Then by all means, feel
free to use a JSON file and the ``.from_json()`` method instead of the
``.from_js_literal()`` method.

.. tip::

  In practice, we find that most chart templates differ in their formatter functions
  and event handlers. This makes JSON a particularly weak tool for templating those
  charts. We strongly prefer the JS literal method described above.
