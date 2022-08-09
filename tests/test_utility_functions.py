"""Unit tests for ``highcharts/utility_functions``"""

import pytest

from abc import ABC, abstractmethod

from highcharts import utility_functions


@pytest.mark.parametrize('error', [
    (None),
    (TypeError),
])
def test_mro_to_dict(error):

    class GrandParent(ABC):
        def __mro_init__(self, kwargs) -> None:
            """Work through the ``self``'s multiple parent classes, executing the
            appropriate constructor (``__init__()``) method for each parent.

            :param self: The object whose parent constructors will be executed.

            :param kwargs: The keyword arguments to pass to the constructor.
            :type kwargs: :class:`dict <python:dict>`

            """
            classes = [x for x in self.__class__.mro()
                       if x.__name__ != 'object']

            for item in classes:
                try:
                    super(item, self).__init__(**kwargs)
                except NotImplementedError:
                    continue

        @abstractmethod
        def to_dict(self):
            raise NotImplementedError()

    class ParentA(GrandParent):
        def __init__(self, **kwargs):
            self.item1 = 123
            self.item2 = 456

        def to_dict(self) -> dict:
            return {
                'item1': self.item1,
                'item2': self.item2
            }

    class ParentB(GrandParent):
        def __init__(self, **kwargs):
            self.item3 = 789
            self.item4 = 987

        def to_dict(self) -> dict:
            return {
                'item3': self.item3,
                'item4': self.item4
            }

    class Child(ParentA, ParentB):
        def __init__(self, **kwargs):
            self.child_item = 'test value'

            self.__mro_init__(kwargs)

        def to_dict(self) -> dict:
            return {
                'child_item': self.child_item
            }

    class ChildError:
        def __init__(self, **kwargs):
            self.child_item = 'raises an error'

    if not error:
        parentA_instance = ParentA()
        parentB_instance = ParentB()
        child_instance = Child()

        result = utility_functions.mro_to_dict(child_instance)

        assert result is not None
        assert isinstance(result, dict) is True
        assert 'item1' in result
        assert 'item2' in result
        assert 'item3' in result
        assert 'item4' in result

        assert result.get('item1') == parentA_instance.item1
        assert result.get('item2') == parentA_instance.item2
        assert result.get('item3') == parentB_instance.item3
        assert result.get('item4') == parentB_instance.item4

    else:
        child_instance = ChildError()

        with pytest.raises(error):
            result = utility_functions.mro_to_dict(child_instance)
