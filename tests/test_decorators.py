"""Tests for the Python decorators defined in ``highcharts.decorators``."""
import json

import pytest

from highcharts_core.decorators import class_sensitive, validate_types
from highcharts_core import errors


class TestClass:
    def __init__(self, **kwargs):
        self.prop = None

        self.prop = kwargs.get('prop', None)

    @classmethod
    def from_dict(cls, as_dict):
        return cls(**as_dict)

    @classmethod
    def from_json(cls, as_json):
        as_dict = json.loads(as_json)
        return cls.from_dict(as_dict)


class TestDecoratedClass:
    def __init__(self, **kwargs):
        self._prop = None
        self._list_prop = None

        self.prop = kwargs.get('prop', None)
        self.list_prop = kwargs.get('list_prop', None)

    @property
    def prop(self):
        return self._prop

    @prop.setter
    @class_sensitive(types = TestClass,
                     allow_dict = True,
                     allow_json = True,
                     allow_none = True,
                     force_iterable = False)
    def prop(self, value):
        self._prop = value

    @property
    def list_prop(self):
        return self._list_prop

    @list_prop.setter
    @class_sensitive(types = TestClass,
                     allow_dict = True,
                     allow_json = True,
                     allow_none = True,
                     force_iterable = True)
    def list_prop(self, value):
        self._list_prop = value

    @classmethod
    def from_dict(cls, as_dict):
        return cls(**as_dict)

    @classmethod
    def from_json(cls, as_json):
        as_dict = json.loads(as_json)
        return cls.from_dict(as_dict)


@pytest.mark.parametrize('kwargs, error, result_class', [
    # allow_dict and everything works
    ({
        'value': {
            'prop': 123
        },
        'types': TestClass,
        'allow_dict': True
    }, None, TestClass),
    ({
        'value': {
            'prop': 123
        },
        'types': [TestClass, str],
        'allow_dict': True
    }, None, TestClass),
    # not allow_dict and raises an error
    ({
        'value': {'prop': 123},
        'types': TestClass,
        'allow_dict': False
    }, errors.HighchartsError, TestClass),
    # allow_json and everything works
    ({
        'value': '{"prop": 123}',
        'types': TestClass,
        'allow_json': True
    }, None, TestClass),
    ({
        'value': bytes('{"prop": 123}', encoding = 'utf8'),
        'types': TestClass,
        'allow_json': True
    }, None, TestClass),
    # not allow_json and raises an error
    ({
        'value': '{"prop": 123}',
        'types': TestClass,
        'allow_json': False
    }, errors.HighchartsError, TestClass),
    ({
        'value': bytes('{"prop": 123}', encoding = 'utf8'),
        'types': TestClass,
        'allow_json': False
    }, errors.HighchartsError, TestClass),
])
def test_validate_types(kwargs, error, result_class):
    if not error:
        value = kwargs.get('value', {})
        if isinstance(value, dict):
            prop_value = value.get('prop', None)
        else:
            prop_value = None

        result = validate_types(**kwargs)
        assert isinstance(result, result_class) is True
        assert result.prop is not None
        if prop_value:
            assert result.prop == prop_value

    else:
        with pytest.raises(error):
            result = validate_types(**kwargs)


@pytest.mark.parametrize('kwargs, error', [
    # everything works
    ({
        'value': None,
        'types': TestClass,
        'allow_none': True
    }, None),
    ({
        'value': '',
        'types': TestClass,
        'allow_none': True
    }, None),
    # fails
    ({
        'value': None,
        'types': TestClass,
        'allow_none': False
    }, errors.HighchartsError),
    ({
        'value': '',
        'types': TestClass,
        'allow_none': False
    }, errors.HighchartsError),
])
def test_validate_types_none(kwargs, error):
    if not error:
        result = validate_types(**kwargs)
        assert result is None
    else:
        with pytest.raises(error):
            result = validate_types(**kwargs)


@pytest.mark.parametrize('kwargs, error, result_class', [
    # force_iterable and allow_dict and everything works
    ({
        'value': [{'prop': 123}, {'prop': 456}],
        'types': TestClass,
        'allow_dict': True,
        'force_iterable': True
    }, None, TestClass),
    # not allow iterable
    ({
        'value': [{'prop': 123}, {'prop': 456}],
        'types': TestClass,
        'allow_dict': True,
        'force_iterable': False
    }, errors.HighchartsError, TestClass),
    # force_iterable and allow_json and everything works
    ({
        'value': '[{"prop": 123}, {"prop": 456}]',
        'types': TestClass,
        'allow_dict': True,
        'force_iterable': True,
        'allow_json': True
    }, None, TestClass),
    # force_iterable and allow_json and everything works
    ({
        'value': bytes('[{"prop": 123}, {"prop": 456}]', encoding = 'utf8'),
        'types': TestClass,
        'allow_dict': True,
        'force_iterable': True,
        'allow_json': True
    }, None, TestClass),
    # force_iterable and allow_empty and everything works
    ({
        'value': [],
        'types': TestClass,
        'allow_dict': True,
        'force_iterable': True,
        'allow_json': True,
        'allow_none': True
    }, None, TestClass),

])
def test_validate_types_list(kwargs, error, result_class):
    if not error:
        value = kwargs.get('value', None)
        result = validate_types(**kwargs)
        assert isinstance(result, list) is True
        if kwargs.get('allow_dict', False) and isinstance(value, list):
            assert len(kwargs.get('value', [])) == len(result)
        for item in result:
            assert isinstance(item, result_class) is True
            assert item.prop is not None

    else:
        with pytest.raises(error):
            result = validate_types(**kwargs)


@pytest.mark.parametrize('value, error, result_class', [
    # dict
    ({ 'prop': 123 }, None, TestClass),
    # json
    ('{ "prop": 123 }', None, TestClass),
    # none
    (None, None, TestClass),
    # list and fails
    ([{ 'prop': 123 }, {'prop': 456 }], errors.HighchartsError, TestClass)
])
def test_class_sensitive(value, error, result_class):
    test_instance = TestDecoratedClass()
    if not error:
        test_instance.prop = value
        if value:
            assert test_instance.prop is not None
            assert isinstance(test_instance.prop, result_class)
        else:
            assert test_instance.prop is None
    else:
        with pytest.raises(error):
            test_instance.prop = value


@pytest.mark.parametrize('value, error, result_class', [
    # dict
    ([{ 'prop': 123 }, { 'prop': 456 }], None, TestClass),
    # json
    ('[{ "prop": 123 }, { "prop": 456 }]', None, TestClass),
    # none
    (None, None, TestClass),
    # empty list
    ([], None, TestClass)
])
def test_class_sensitive_list(value, error, result_class):
    test_instance = TestDecoratedClass()
    if not error:
        test_instance.list_prop = value
        if value:
            assert test_instance.list_prop is not None
            assert isinstance(test_instance.list_prop, list)
        elif value is not None:
            assert len(test_instance.list_prop) == 0
        else:
            assert test_instance.list_prop is None
    else:
        with pytest.raises(error):
            test_instance.list_prop = value
