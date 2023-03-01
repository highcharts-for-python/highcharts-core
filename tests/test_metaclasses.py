"""Unit tests for ``highcharts.metaclasses``."""

import pytest

from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core import constants

from json.decoder import JSONDecodeError
from validator_collection import checkers


class TestClass(HighchartsMeta):
    """Class used to test the :class:`HighchartsMeta` functionality."""

    def __init__(self, **kwargs):
        self.item1 = kwargs.get('item1', None)
        self.item2 = kwargs.get('item2', None)

        super().__init__(**kwargs)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'item1': as_dict.get('item1', None),
            'item2': as_dict.get('item2', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        return {
            'item1': self.item1,
            'item2': self.item2
        }


test_class_instance = TestClass(item1 = 123, item2 = 456)
test_class_trimmed_instance = TestClass(item1 = 123)
test_class_iterable = TestClass(item1 = [1, 2, constants.EnforcedNullType], item2 = 456)
test_class_none_iterable = TestClass(item1 = [1, None, 3], item2 = 456)

@pytest.mark.parametrize('kwargs, error', [
    ({'item1': 123,
      'item2': 456},
     None),
])
def test__init__(kwargs, error):
    if not error:
        result = TestClass(**kwargs)
        assert result is not None
        assert isinstance(result, HighchartsMeta)

    else:
        with pytest.raises(error):
            result = TestClass(**kwargs)


@pytest.mark.parametrize('cls, as_dict, error', [
    (TestClass, {'item1': 123, 'item2': 456}, None),
    (TestClass, {}, None),
    (TestClass, 'not-a-dict', (TypeError, AttributeError)),
])
def test_from_dict(cls, as_dict, error):
    if not error:
        original_dict = as_dict.copy()
        result = cls.from_dict(as_dict)
        assert result is not None
        assert isinstance(result, HighchartsMeta)
        print(original_dict)
        if not original_dict:
            assert result.item1 is None
            assert result.item2 is None
        else:
            for key in original_dict:
                attribute = getattr(result, key)
                assert attribute == original_dict[key]
    else:
        with pytest.raises(error):
            result = cls.from_dict(as_dict)


@pytest.mark.parametrize('cls, as_json, error', [
    (TestClass, '{"item1": 123, "item2": 456}', None),
    (TestClass, '{}', None),
    (TestClass, 'not-valid-json', JSONDecodeError),
])
def test_from_json(cls, as_json, error):
    if not error:
        result = cls.from_json(as_json)
        assert result is not None
        assert isinstance(result, HighchartsMeta)
    else:
        with pytest.raises(error):
            result = cls.from_json(as_json)


@pytest.mark.parametrize('instance, error', [
    (test_class_instance, None),
])
def test_to_json(instance, error):
    if not error:
        result = instance.to_json()
        assert result is not None
        assert isinstance(result, (str, bytes)) is True

        new_instance = instance.__class__.from_json(result)
        assert new_instance.item1 == instance.item1
        assert new_instance.item2 == instance.item2

    else:
        with pytest.raises(error):
            result = instance.to_json()


@pytest.mark.parametrize('instance, expected, error', [
    (test_class_instance, {'item1': 123, 'item2': 456}, None),
    (test_class_trimmed_instance, {'item1': 123}, None),
])
def test_to_dict(instance, expected, error):
    if not error:
        result = instance.to_dict()
        assert result is not None
        assert isinstance(result, dict) is True

        assert checkers.are_dicts_equivalent(result, expected) is True
    else:
        with pytest.raises(error):
            result = instance.to_dict()


@pytest.mark.parametrize('instance, error', [
    (test_class_trimmed_instance, None),
])
def test__to_untrimmed_dict(instance, error):
    if not error:
        result = instance._to_untrimmed_dict()
        assert result is not None
        assert isinstance(result, dict)
        assert len(result) == 2
        assert 'item1' in result
        assert 'item2' in result

        assert result.get('item1') is not None
        assert result.get('item2') is None
    else:
        with pytest.raises(error):
            result = instance._to_untrimmed_dict()


@pytest.mark.parametrize('untrimmed, expected_keys, error', [
    ({'item1': 123, 'item2': None}, 1, None),
    ({'item1': 123, 'item2': 456}, 2, None),
    ({'item1': test_class_instance, 'item2': None}, 1, None),
    ({'item1': constants.EnforcedNull, 'item2': None}, 1, None),
    ({'item1': {'test': 789}, 'item2': None}, 1, None),
    ('not-a-dict', None, AttributeError),
])
def test_trim_dict(untrimmed, expected_keys, error):
    if not error:
        result = HighchartsMeta.trim_dict(untrimmed)
        assert result is not None
        assert isinstance(result, dict) is True
        assert len(result) == expected_keys
    else:
        with pytest.raises(error):
            result = HighchartsMeta.trim_dict(untrimmed)


@pytest.mark.parametrize('untrimmed, expected_type, expected_length, error', [
    ([1, 2, 3], list, 3, None),
    (123, int, None, None),
    ([1, 2, None], list, 3, None),
    ([1, 2, constants.EnforcedNull], list, 3, None),
    ([1, 2, test_class_instance], list, 3, None),
])
def test_trim_iterable(untrimmed, expected_type, expected_length, error):
    if not error:
        result = TestClass.trim_iterable(untrimmed)
        assert result is not None
        assert isinstance(result, expected_type) is True
        if expected_length is not None:
            assert len(result) == expected_length
        if isinstance(untrimmed, list) and (None in untrimmed or
                                            constants.EnforcedNull in untrimmed):
            assert None not in result
            assert 'null' in result
    else:
        with pytest.raises(error):
            result = TestClass.trim_iterable(untrimmed)

"""
@pytest.mark.parametrize('error', [
    (None),
])
def test__mro_init(error):

    class ParentA(HighchartsMeta):
        def __init__(self, **kwargs):
            self._item1 = None
            self._item2 = None

            self.item1 = kwargs.get('item1', 123)
            self.item2 = kwargs.get('item2', 456)

        @property
        def item1(self):
            return self._item1

        @item1.setter
        def item1(self, value):
            self._item1 = value

        @property
        def item2(self):
            return self._item2

        @item2.setter
        def item2(self, value):
            self._item2 = value

        def _to_untrimmed_dict(self, in_cls = None) -> dict:
            return {
                'item1': self.item1,
                'item2': self.item2
            }

        @classmethod
        def from_dict(cls, as_dict):
            return cls(**as_dict)

    class ParentB(HighchartsMeta):
        def __init__(self, **kwargs):
            self._item3 = None
            self._item4 = None

            self.item3 = kwargs.get('item3', 789)
            self.item4 = kwargs.get('item4', 987)

        @property
        def item3(self):
            return self._item3

        @item3.setter
        def item3(self, value):
            self._item3 = value

        @property
        def item4(self):
            return self._item4

        @item4.setter
        def item4(self, value):
            self._item4 = value

        def _to_untrimmed_dict(self, in_cls = None) -> dict:
            return {
                'item3': self.item3,
                'item4': self.item4
            }

        @classmethod
        def from_dict(cls, as_dict):
            return cls(**as_dict)

    class Child(ParentA, ParentB):
        def __init__(self, **kwargs):
            self._item1 = None
            self._item2 = None
            self._item3 = None
            self._item4 = None

            self.child_item = kwargs.get('child_item', 'test value')

        def to_dict(self) -> dict:
            return {
                'child_item': self.child_item
            }

    class ChildError(ParentA):
        pass

    if not error:
        child_instance = Child()

        assert child_instance.item1 is None
        assert child_instance.item2 is None
        assert child_instance.item3 is None
        assert child_instance.item4 is None

        kwargs = {}
        child_instance.__mro_init__(kwargs)

        assert child_instance.item1 is not None
        assert child_instance.item2 is not None
        assert child_instance.item3 is not None
        assert child_instance.item4 is not None

    else:
        child_instance = ChildError()

        with pytest.raises(error):
            child_instance.__mro_init__({})
"""

@pytest.mark.parametrize('cls, as_str, error', [
    (TestClass, """{item1: function () {
      // The first returned item is the header, subsequent items are the
      // points
      return ['<b>' + this.x + '</b>'].concat(
          this.points ?
              this.points.map(function (point) {
                  return point.series.name + ': ' + point.y + 'm';
              }) : []
      );
     }}""", None)
])
def test_from_js_literal(cls, as_str, error):
    if not error:
        print('-------------------')
        print('ORIGINAL VALIDATION')
        parsed_original, original_str = cls._validate_js_literal(as_str, range = False)
        print('-------------')
        print('ORIGINAL CALL')
        result = cls.from_js_literal(as_str)
        assert result is not None
        assert isinstance(result, cls) is True

        as_js_literal = result.to_js_literal()
        print('-----------------')
        print('RESULT VALIDATION')
        parsed_output, output_str = cls._validate_js_literal(as_js_literal, range = False)
        assert str(parsed_output) == str(parsed_original)
    else:
        with pytest.raises(error):
            result = cls.from_js_literal(as_str)
