import pytest

from validator_collection import checkers

from highcharts_core import utility_functions
from highcharts_core.metaclasses import HighchartsMeta


class Grandparent(HighchartsMeta):
    def __init__(self, **kwargs):
        self._item1 = None
        self._item2 = None

        self.item1 = kwargs.get('item1', 123)
        self.item2 = kwargs.get('item2', 345)

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

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        return as_dict

    def _to_untrimmed_dict(self, in_cls = None):
        untrimmed = {
            'item1': self.item1,
            'item2': self.item2
        }

        return untrimmed

    def return_value(self):
        return 'Grandparent'


class ParentA(Grandparent):
    def __init__(self, **kwargs):
        self._item3 = None
        self._item4 = None

        self.item3 = kwargs.get('item3', 567)
        self.item4 = kwargs.get('item4', 890)

        super().__init__(**kwargs)

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

    def _to_untrimmed_dict(self, in_cls = None):
        print(f'starting {self.__class__.__name__}._to_untrimmed_dict()')
        untrimmed = {
            'item3': self.item3,
            'item4': self.item4
        }
        parent_as_dict = utility_functions.mro__to_untrimmed_dict(self,
                                                                  in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        print(f'ending {self.__class__.__name__}._to_untrimmed_dict()')

        return untrimmed

    def return_value(self):
        return 'ParentA'


class ParentB(Grandparent):
    def __init__(self, **kwargs):
        self._item5 = None
        self._item6 = None

        self.item5 = kwargs.get('item5', 987)
        self.item6 = kwargs.get('item6', 654)

        super().__init__(**kwargs)

    @property
    def item5(self):
        return self._item5

    @item5.setter
    def item5(self, value):
        self._item5 = value

    @property
    def item6(self):
        return self._item6

    @item6.setter
    def item6(self, value):
        self._item6 = value

    def _to_untrimmed_dict(self, in_cls = None):
        print(f'starting {self.__class__.__name__}._to_untrimmed_dict()')
        untrimmed = {
            'item5': self.item5,
            'item6': self.item6
        }
        parent_as_dict = utility_functions.mro__to_untrimmed_dict(self,
                                                                  in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        print(f'ending  {self.__class__.__name__}._to_untrimmed_dict()')

        return untrimmed

    def return_value(self):
        return 'ParentB'


class Child(ParentA, ParentB):
    def __init__(self, **kwargs):
        self._item7 = None

        self.item7 = kwargs.get('item7', 321)

        super().__init__(**kwargs)

    @property
    def item7(self):
        return self._item7

    @item7.setter
    def item7(self, value):
        self._item7 = value

    def _to_untrimmed_dict(self, in_cls = None):
        print(f'starting {self.__class__.__name__}._to_untrimmed_dict()')
        untrimmed = {
            'item7': self.item7
        }
        parent_as_dict = utility_functions.mro__to_untrimmed_dict(self,
                                                                  in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        print(f'ending {self.__class__.__name__}._to_untrimmed_dict()')

        return untrimmed

    def return_value(self):
        return 'Child'


class GrandChild(Child):
    def __init__(self, **kwargs):
        self._item8 = None

        self.item8 = kwargs.get('item8', 12)

        super().__init__(**kwargs)

    @property
    def item8(self):
        return self._item8

    @item8.setter
    def item8(self, value):
        self._item8 = value

    def _to_untrimmed_dict(self, in_cls = None):
        untrimmed = {
            'item8': self.item8
        }

        parent_as_dict = utility_functions.mro__to_untrimmed_dict(self,
                                                                  in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        print('consolidated parent_as_dict:')
        print(parent_as_dict)

        print(f'ending {self.__class__.__name__}._to_untrimmed_dict()')

        return untrimmed

    def return_value(self):
        return 'GrandChild'


def mro_return(obj, exclude_self = False):
    cls = obj.__class__
    mro = cls.mro()
    if exclude_self:
        result = [x.return_value(obj) for x in mro
                  if hasattr(x, 'return_value') and
                  x != cls]
    else:
        result = [x.return_value(obj) for x in mro
                  if hasattr(x, 'return_value')]

    return result


@pytest.mark.parametrize('cls, kwargs, error', [
    (GrandChild, {}, None),
    (Child, {}, None),
])
def test__init(cls, kwargs, error):
    if not error:
        result = cls(**kwargs)
        assert isinstance(result, cls) is True
        assert isinstance(result, Grandparent) is True
        assert isinstance(result, HighchartsMeta) is True

        if isinstance(result, GrandChild):
            assert isinstance(result, Child) is True
            assert isinstance(result, ParentA) is True
            assert isinstance(result, ParentB) is True
            assert isinstance(result, Grandparent) is True
            assert hasattr(result, 'item8') is True
            assert result.item8 == kwargs.get('item8', 12)
            assert isinstance(result, ParentA) is True
            assert isinstance(result, ParentB) is True
            assert isinstance(result, Grandparent) is True
            assert hasattr(result, 'item7') is True
            assert result.item7 == kwargs.get('item7', 321)
            assert isinstance(result, Grandparent) is True
            assert hasattr(result, 'item3') is True
            assert hasattr(result, 'item4') is True
            assert result.item3 == kwargs.get('item3', 567)
            assert result.item4 == kwargs.get('item4', 890)
        if isinstance(result, Child):
            assert isinstance(result, ParentA) is True
            assert isinstance(result, ParentB) is True
            assert isinstance(result, Grandparent) is True
            assert hasattr(result, 'item7') is True
            assert result.item7 == kwargs.get('item7', 321)
        if isinstance(result, ParentA):
            assert isinstance(result, Grandparent) is True
            assert hasattr(result, 'item3') is True
            assert hasattr(result, 'item4') is True
            assert result.item3 == kwargs.get('item3', 567)
            assert result.item4 == kwargs.get('item4', 890)
        if isinstance(result, ParentB):
            assert isinstance(result, Grandparent) is True
            assert hasattr(result, 'item5') is True
            assert hasattr(result, 'item6') is True
            assert result.item5 == kwargs.get('item5', 987)
            assert result.item6 == kwargs.get('item6', 654)
        if isinstance(result, Grandparent):
            assert isinstance(result, HighchartsMeta) is True
            assert hasattr(result, 'item1') is True
            assert hasattr(result, 'item2') is True
            assert result.item1 == kwargs.get('item1', 123)
            assert result.item2 == kwargs.get('item2', 345)

    else:
        with pytest.raises(error):
            result = cls(**kwargs)


@pytest.mark.parametrize('cls, kwargs, expected, error', [
    (GrandChild,
     {},
     {
         'item1': 123,
         'item2': 345,
         'item3': 567,
         'item4': 890,
         'item5': 987,
         'item6': 654,
         'item7': 321,
         'item8': 12
     },
     None),
    (Child,
     {},
     {
         'item1': 123,
         'item2': 345,
         'item3': 567,
         'item4': 890,
         'item5': 987,
         'item6': 654,
         'item7': 321
     },
     None),
    (ParentB,
     {},
     {
         'item1': 123,
         'item2': 345,
         'item5': 987,
         'item6': 654,
     },
     None),
    (Grandparent,
     {},
     {
         'item1': 123,
         'item2': 345,
     },
     None),
])
def test__to_untrimmed_dict(cls, kwargs, expected, error):
    if not error:
        instance = cls(**kwargs)
        result = instance._to_untrimmed_dict()

        if isinstance(instance, GrandChild) is True:
            assert len(result) == 8

            assert 'item8' in result
            assert 'item7' in result
            assert 'item6' in result
            assert 'item5' in result
            assert 'item4' in result
            assert 'item3' in result
            assert 'item2' in result
            assert 'item1' in result

            assert result.get('item8') == kwargs.get('item8', 12) == instance.item8
            assert result.get('item7') == kwargs.get('item7', 321) == instance.item7
            assert result.get('item6') == kwargs.get('item6', 654) == instance.item6
            assert result.get('item5') == kwargs.get('item5', 987) == instance.item5
            assert result.get('item4') == kwargs.get('item4', 890) == instance.item4
            assert result.get('item3') == kwargs.get('item3', 567) == instance.item3
            assert result.get('item2') == kwargs.get('item2', 345) == instance.item2
            assert result.get('item1') == kwargs.get('item1', 123) == instance.item1

        if isinstance(instance, Child) is True and not isinstance(instance, GrandChild):
            print(result)
            assert len(result) == 7

            assert 'item8' not in result
            assert 'item7' in result
            assert 'item6' in result
            assert 'item5' in result
            assert 'item4' in result
            assert 'item3' in result
            assert 'item2' in result
            assert 'item1' in result

            assert result.get('item7') == kwargs.get('item7', 321) == instance.item7
            assert result.get('item6') == kwargs.get('item6', 654) == instance.item6
            assert result.get('item5') == kwargs.get('item5', 987) == instance.item5
            assert result.get('item4') == kwargs.get('item4', 890) == instance.item4
            assert result.get('item3') == kwargs.get('item3', 567) == instance.item3
            assert result.get('item2') == kwargs.get('item2', 345) == instance.item2
            assert result.get('item1') == kwargs.get('item1', 123) == instance.item1

        if isinstance(instance, ParentB) is True and not isinstance(instance, Child):
            print(result)
            assert len(result) == 4

            assert 'item8' not in result
            assert 'item7' not in result
            assert 'item6' in result
            assert 'item5' in result
            assert 'item4' not in result
            assert 'item3' not in result
            assert 'item2' in result
            assert 'item1' in result

            assert result.get('item6') == kwargs.get('item6', 654) == instance.item6
            assert result.get('item5') == kwargs.get('item5', 987) == instance.item5
            assert result.get('item2') == kwargs.get('item2', 345) == instance.item2
            assert result.get('item1') == kwargs.get('item1', 123) == instance.item1

        assert checkers.are_dicts_equivalent(result, expected) is True
    else:
        with pytest.raises(error):
            instance = cls(**kwargs)
            result = instance._to_untrimmed_dict()


@pytest.mark.parametrize('cls, exclude_self', [
    (Child, False),
    (ParentA, False),
    (ParentB, False),
    (GrandChild, False),
    (Grandparent, False),

    (Child, True),
    (ParentA, True),
    (ParentB, True),
    (GrandChild, True),
    (Grandparent, True),
])
def test_mro_return(cls, exclude_self):
    instance = cls()
    result = mro_return(instance, exclude_self = exclude_self)
    if instance.__class__.__name__ == 'Child':
        if exclude_self:
            assert len(result) == 3
            assert 'Child' not in result
        else:
            assert len(result) == 4
            assert 'Child' in result
        assert 'ParentA' in result
        assert 'ParentB' in result
        assert 'Grandparent' in result
    elif instance.__class__.__name__ == 'ParentA':
        if exclude_self:
            assert len(result) == 1
            assert 'ParentA' not in result
        else:
            assert len(result) == 2
            assert 'ParentA' in result
        assert 'Grandparent' in result
    elif instance.__class__.__name__ == 'ParentB':
        if exclude_self:
            assert len(result) == 1
            assert 'ParentB' not in result
        else:
            assert len(result) == 2
            assert 'ParentB' in result
        assert 'Grandparent' in result
    elif instance.__class__.__name__ == 'Grandparent':
        if exclude_self:
            assert len(result) == 0
            assert 'Grandparent' not in result
        else:
            assert len(result) == 1
            assert 'Grandparent' in result
    elif instance.__class__.__name__ == 'GrandChild':
        if exclude_self:
            assert len(result) == 4
            assert 'GrandChild' not in result
        else:
            assert len(result) == 5
            assert 'GrandChild' in result
        assert 'Child' in result
        assert 'ParentA' in result
        assert 'ParentB' in result
        assert 'Grandparent' in result
