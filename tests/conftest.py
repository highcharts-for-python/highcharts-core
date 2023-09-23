# -*- coding: utf-8 -*-

"""
*******************
tests.conftest
*******************

Utility functions that are used to configure Py.Test context.

"""

import os
import pytest


def pytest_addoption(parser):
    """Define options that the parser looks for in the command-line.

    Pattern to use::

      parser.addoption("--cli-option",
                       action="store",
                       default=None,
                       help="cli-option: help text goes here")

    """
    parser.addoption("--inputs",
                     action="store",
                     default="/home/travis/build/highcharts-for-python/highcharts-core/tests/input_files",
                     help=("inputs: the absolute path to the directory where input"
                           " files can be found"))
    parser.addoption("--downloads",
                     action="store",
                     default="true",
                     help=("downloads: set to 'false' to disable tests of chart export "
                           "via the Highsoft-provided Export Server."))
    parser.addoption("--create-output-directory",
                     action = "store",
                     default = "true",
                     help=("create-output-directory: set to 'false' to error if the output "
                           "directory does not exist, otherwise creates it."))
    parser.addoption("--pyspark",
                     action="store",
                     default="false",
                     help=("pyspark: set to 'false' to disable tests of pyspark-related"
                           " functionality, or 'true' to enable those tests. Defaults to"
                           " 'false'"))
    parser.addoption("--openai",
                     action="store",
                     default="none",
                     help=("openai: The API key to use to authenticate against OpenAI."))
    parser.addoption('--disable-ai',
                     action='store',
                     default='true',
                     help=('disable-ai: set to "false" to enable tests of the AI'))
    parser.addoption('--pandas',
                     action = 'store',
                     default = os.getenv('ENABLE_PANDAS', 'true'),
                     help=('pandas: set to "false" to disable tests of pandas-related'))


def pytest_runtest_makereport(item, call):
    """Connect current incremental test to its preceding parent."""
    # pylint: disable=W0212
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    """Fail test if preceding incremental test failed."""
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail(
                "previous test failed (%s) for reason: %s" % (previousfailed.name,
                                                              previousfailed))
