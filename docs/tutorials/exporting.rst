#######################################################
Exporting Static Charts with Highcharts for Python
#######################################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

Highcharts (JS) and **Highcharts for Python** are designed to produce beautiful, powerful, highly-interactive
data visualizations. However, there are moments when you or your users want to create a static chart for inclusion in
presentations, documents, etc. Highcharts has you covered for that as well!

------------

**********************
Client-side Exporting
**********************

Using **Highcharts for Python**, you can configure client-side export within the 
:meth:`Chart.options <highcharts_core.chart.Chart.options>` settings by configuring the 
:meth:`options.exporting <highcharts_core.options.HighchartsOptions.exporting>` 
property. 

In particular, you can apply configuration through an 
:class:`Exporting <highcharts_core.options.exporting.Exporting>` instance, which 
lets you configure how your chart will support exporting from within the user's 
browser when the chart is rendered. Here’s a quick example, assuming you have a 
:meth:`Chart <highcharts_core.chart.Chart>`` instance called ``my_chart``:

  .. code-block:: python

    from highcharts_core.options.exporting import Exporting

    exporting_options = Exporting(enabled = True,
                                  filename = 'your-exported-chart',
                                  show_table = True,
                                  table_caption = "Your Chart's Caption Goes Here",
                                  accessibility = {
                                      'enabled': True
                                  })
    
    exporting_options.buttons['contextButton'].menu_items = ['printChart', 'separator', 'downloadPNG']
    
    my_chart.options.exporting = exporting_options

And that's it. With the code above you've now configured some basic logic that:

  * Enables client-side export of the ``my_chart`` visualization.
  * Gives an exported chart image a default filename of ``'your-exported-chart'`` (not 
    including the file's extension).
  * Makes sure that the exported or printed version of your chart includes the chart's 
    underlying data table (thanks to the ``show_table`` property being set to ``True``), 
    and
  * Gives users the ability to either print the chart or download a PNG version of the chart, 
    but nothing else (by setting the relevant buttons shown in the context menu).

Highcharts Core supports client-side export to a number of formats, including:

  * PNG
  * JPEG
  * SVG
  * CSV
  * Excel

And you can also configure the client-side export to fall back to server-side export should it fail. 

  .. seealso::
    
    * For more details on the extensive options, please see :mod:`highcharts_core.options.exporting`

---------

**************************************
Programmatic (Server-side) Export
**************************************

So now that your users can download a PNG image of your chart, maybe you want to create an image programmatically. **Highcharts for Python** makes that possible through an integration with the **Highcharts Export Server**. It's actually trivially easy to do since you can do it with just one method call in your Python code:

  .. code-block:: python

    # EXAMPLE 1.
    # Download a PNG version of the chart in memory within your Python code.

    my_png_image = my_chart.download_chart(format = 'png')

    # EXAMPLE 2.
    # Download a PNG version of the chart and save it the file "/images/my-chart-file.png"
    my_png_image = my_chart.download_chart(
        format = 'png',
        filename = '/images/my-chart-file.png'
    )

The two examples shown above both download a PNG of your chart:

  #. The first example keeps that PNG image in your Python code only, storing its binary data in the 
     ``my_png_image`` variable. 
  #. The second example not only stores its binary data in the ``my_png_image`` variable, but it *also* saves 
     the PNG image to the file ``'/images/my-chart-file.png'``.

The format argument is really the one doing the heavy lifting above. In the example above, it tells the method to generate a PNG image, but you can also create:

  * ``'jpeg'`` 
  * ``'pdf'``, and 
  * ``'svg'

And that's it! There's really nothing simpler.

.. note::

  Under the hood, this method defaults to calling the Highcharts Export Server that is maintained by 
  `Highsoft <https://www.highcharts.com>`__ (creators of Highcharts Core (JS)). This publicly-available server 
  is available to all licensees of Highcharts Core, and you are free to use it to generate downloadable 
  versions of your data visualizations. 
  
  However, it is rate-limited and it does mean transmitting your chart's data across the wire. There are 
  various situations in which this is inappropriate, which is why Highsoft allows you to configure and deploy 
  your own Highcharts Export Server. And Highcharts for Python supports using your own custom Export Server 
  for your programmatic chart exports.

------------------------

************************************
Using a Custom Export Server
************************************

.. tip::

  While deploying your own Highcharts Export Server is beyond the scope of this tutorial, we strongly recommend that 
  you review the 
  `Highcharts Export Server documentation <https://www.highcharts.com/docs/export-module/setting-up-the-server>`__

If you have your own Highcharts Export Server, you can override **Highcharts for Python**'s default to 
have your code rely on your own export server. While you can do this by creating an instance of 
:class:`highcharts_core.headless_export.ExportServer` with your custom configuration and passing it to the 
:meth:`.download_chart() <highcharts_core.chart.Chart.download_chart>` method in the ``server_instance`` 
argument, it is far easier to simply set some environment variables wherever your Python code will be running:

  * ``HIGHCHARTS_EXPORT_SERVER_DOMAIN`` is the environment variable that specifies the domain where the Highcharts 
    Export Server exists. If this environment variable is not set, it will default to ``"export.highcharts.com"``, 
    which is the Highsoft-provided export server.
  * ``HIGHCHARTS_EXPORT_SERVER_PATH`` is the path at the domain where your Export Server is reachable. If this 
    environment variable is not set, it will default to :obj:`None <python:None>` since there is no path when using the 
    Highsoft-provided export server.
  * ``HIGHCHARTS_EXPORT_SERVER_PORT`` is the port where your Export Server is reachable. If this environment variable 
    is not set, it will default to :obj:`None <python:None>` since there is no need to specify a port when using the 
    Highsoft-provided export server.

In addition to the three environment variables above, the 
:meth:`.download_chart() <highcharts_core.chart.Chart.download_chart>` method also supports 
three additional arguments which may prove useful:

  * ``auth_user`` which is the user to supply to your custom Export Server using Basic authentication. This defaults to 
    :obj:`None <python:None>` (since the default Highsoft-provided Export Server has no authentication).
  * ``auth_password`` which is the password to supply to your custom Export Server using Basic authentication. This
    :obj:`None <python:None>` (since the default Highsoft-provided Export Server has no authentication).
  * ``timeout`` which is the number of seconds to wait before issuing a timeout error. The timeout check is passed if 
    any bytes have been received on the socket in less than this number of seconds. It defaults to ``0.5``, but you may 
    want to adjust this when using your own custom Export Server.

