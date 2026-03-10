"""Tests for the requires_js_object property optimization.

Verifies that the optimized requires_js_object implementation produces the same
results as the original to_dict()/trim_dict() approach across various data point
configurations.
"""

import pytest

from highcharts_core.options.series.data.cartesian import CartesianData
from highcharts_core.options.series.data.cartesian import Cartesian3DData
from highcharts_core.options.series.data.cartesian import CartesianValueData
from highcharts_core.options.series.data.bar import BarData
from highcharts_core.options.series.data.pie import PieData
from highcharts_core.options.series.data.range import RangeData
from highcharts_core.options.series.data.single_point import SinglePointData
from highcharts_core.utility_classes.markers import Marker
from highcharts_core.utility_classes.data_labels import DataLabel


class TestCartesianDataRequiresJSObject:
    """Tests for CartesianData.requires_js_object."""

    def test_xy_only_does_not_require_object(self):
        """A simple (x, y) point should serialize as an array."""
        point = CartesianData(x=1, y=2)
        assert point.requires_js_object is False

    def test_y_only_does_not_require_object(self):
        """A point with only y should serialize as an array."""
        point = CartesianData(y=42)
        assert point.requires_js_object is False

    def test_name_and_y_does_not_require_object(self):
        """A point with name and y should serialize as an array (name is an array prop)."""
        point = CartesianData(name='Category A', y=10)
        assert point.requires_js_object is False

    def test_empty_point_does_not_require_object(self):
        """An empty point with no properties set should serialize as an array."""
        point = CartesianData()
        assert point.requires_js_object is False

    def test_with_id_requires_object(self):
        """A point with id set requires JS object (id is not an array prop)."""
        point = CartesianData(x=1, y=2, id='point-1')
        assert point.requires_js_object is True

    def test_with_color_requires_object(self):
        """A point with color set requires JS object."""
        point = CartesianData(x=1, y=2, color='#ff0000')
        assert point.requires_js_object is True

    def test_with_class_name_requires_object(self):
        """A point with class_name set requires JS object."""
        point = CartesianData(x=1, y=2, class_name='highlighted')
        assert point.requires_js_object is True

    def test_with_description_requires_object(self):
        """A point with description set requires JS object."""
        point = CartesianData(x=1, y=2, description='An important point')
        assert point.requires_js_object is True

    def test_with_selected_requires_object(self):
        """A point with selected=True requires JS object."""
        point = CartesianData(x=1, y=2, selected=True)
        assert point.requires_js_object is True

    def test_with_drilldown_requires_object(self):
        """A point with drilldown set requires JS object."""
        point = CartesianData(x=1, y=2, drilldown='details')
        assert point.requires_js_object is True

    def test_with_data_labels_requires_object(self):
        """A point with non-empty data_labels requires JS object."""
        point = CartesianData(x=1, y=2, data_labels={'enabled': True})
        assert point.requires_js_object is True

    def test_with_marker_requires_object(self):
        """A point with non-empty marker requires JS object."""
        point = CartesianData(x=1, y=2, marker={'enabled': True, 'radius': 5})
        assert point.requires_js_object is True

    def test_with_empty_marker_does_not_require_object(self):
        """A point with an empty Marker() should not require JS object.

        This is the key edge case: Marker() has all None fields, so trim_dict
        would filter it out. The optimized code must handle this too.
        """
        point = CartesianData(x=1, y=2)
        point._marker = Marker()
        assert point.requires_js_object is False

    def test_with_empty_data_label_does_not_require_object(self):
        """A point with an empty DataLabel() should not require JS object."""
        point = CartesianData(x=1, y=2)
        point._data_labels = DataLabel()
        assert point.requires_js_object is False

    def test_with_color_index_requires_object(self):
        """A point with color_index set requires JS object."""
        point = CartesianData(x=1, y=2, color_index=3)
        assert point.requires_js_object is True

    def test_with_custom_requires_object(self):
        """A point with custom data requires JS object."""
        point = CartesianData(x=1, y=2, custom={'key': 'value'})
        assert point.requires_js_object is True

    def test_with_empty_custom_does_not_require_object(self):
        """A point with an empty custom dict should not require JS object."""
        point = CartesianData(x=1, y=2)
        point._custom = {}
        assert point.requires_js_object is False


class TestToArrayConsistency:
    """Verify that to_array() output is consistent with requires_js_object."""

    def test_array_form_for_simple_point(self):
        """A simple point should produce array output."""
        point = CartesianData(x=1, y=2)
        result = point.to_array()
        assert isinstance(result, list)
        assert result == [1, 2]

    def test_dict_form_for_complex_point(self):
        """A point with extra props should produce dict output."""
        point = CartesianData(x=1, y=2, color='#ff0000')
        result = point.to_array()
        assert isinstance(result, dict)

    def test_array_form_y_only(self):
        """A y-only point should produce a single-element array."""
        point = CartesianData(y=5)
        result = point.to_array()
        assert isinstance(result, list)
        assert result == [5]

    def test_array_form_name_and_y(self):
        """A name+y point should produce [name, y] array."""
        point = CartesianData(name='A', y=10)
        result = point.to_array()
        assert isinstance(result, list)
        assert result == ['A', 10]


class TestOtherDataTypes:
    """Verify requires_js_object works correctly across data point types."""

    def test_cartesian3d_xyz_only(self):
        """3D point with only x,y,z should not require object."""
        point = Cartesian3DData(x=1, y=2, z=3)
        assert point.requires_js_object is False

    def test_cartesian3d_with_color(self):
        """3D point with color requires object."""
        point = Cartesian3DData(x=1, y=2, z=3, color='#ff0000')
        assert point.requires_js_object is True

    def test_cartesian_value_xy_only(self):
        """CartesianValueData with only x,y should not require object."""
        point = CartesianValueData(x=1, y=2)
        assert point.requires_js_object is False

    def test_bar_data_xy_only(self):
        """BarData with only x,y should not require object."""
        point = BarData(x=1, y=2)
        assert point.requires_js_object is False

    def test_bar_data_with_color(self):
        """BarData with color requires object."""
        point = BarData(x=1, y=2, color='#ff0000')
        assert point.requires_js_object is True

    def test_range_data_simple(self):
        """RangeData with only low,high should not require object."""
        point = RangeData(low=1, high=5)
        assert point.requires_js_object is False

    def test_range_data_with_color(self):
        """RangeData with color requires object."""
        point = RangeData(low=1, high=5, color='#ff0000')
        assert point.requires_js_object is True

    def test_pie_data_name_y(self):
        """PieData with name,y should not require object (both are array props)."""
        point = PieData(name='Slice A', y=30)
        assert point.requires_js_object is False

    def test_single_point_value_only(self):
        """SinglePointData with only value should not require object."""
        point = SinglePointData(y=42)
        assert point.requires_js_object is False


class TestBulkSerialization:
    """Test that bulk serialization produces consistent results."""

    def test_many_simple_points_all_array(self):
        """All simple points should serialize as arrays."""
        points = [CartesianData(x=i, y=i * 2) for i in range(100)]
        for point in points:
            assert point.requires_js_object is False
            result = point.to_array()
            assert isinstance(result, list)

    def test_mixed_points(self):
        """Mix of simple and complex points should be handled correctly."""
        simple = CartesianData(x=1, y=2)
        complex_pt = CartesianData(x=1, y=2, color='red')

        assert simple.requires_js_object is False
        assert complex_pt.requires_js_object is True

        assert isinstance(simple.to_array(), list)
        assert isinstance(complex_pt.to_array(), dict)
