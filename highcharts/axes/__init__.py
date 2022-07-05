from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta


class AxisBase(HighchartsMeta):
    """Base class that is used for defining axis classes."""
    pass
