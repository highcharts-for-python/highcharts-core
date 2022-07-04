"""Defines a set of constants that are used throughout the library."""
import os

from dotenv import load_dotenv

load_dotenv()


JAVASCRIPT_INDENT_SPACES = os.getenv('JAVASCRIPT_INDENT_SPACES') or 2
JAVASCRIPT_INDENT = ''
indent_count = 1
while indent_count < int(JAVASCRIPT_INDENT_SPACES):
    JAVASCRIPT_INDENT += ' '
    indent_count += 1

DEFAULT_COLORS = ["#7cb5ec", "#434348", "#90ed7d", "#f7a35c", "#8085e9", "#f15c80",
                  "#e4d354", "#2b908f", "#f45b5b", "#91e8e1"]

DEFAULT_LANDMARK_VERBOSITY = 'all'
LANDMARK_VERBOSITY_VALUES = ['all',
                              'one',
                              'disabled'
                             ]

DEFAULT_LINKED_DESCRIPTION = '*[data-highcharts-chart="{index}"] + .highcharts-description'
