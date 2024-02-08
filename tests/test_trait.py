import math

from python_trait import Trait, register_trait, trait_to, trait_impl_pool


class NumberPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class AABB:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max


class AsLine(Trait['AsLine']):
    def length(self):
        raise NotImplementedError


as_line = AsLine()


@trait_to(NumberPair)
class NumberPairAsLine(AsLine):
    def __init__(self, number_pair: NumberPair):
        self.number_pair = number_pair

    def length(self):
        x = self.number_pair.x
        y = self.number_pair.y
        return math.sqrt(x * x + y * y)


@register_trait(AABB, AsLine)
class AABBAsLine(AsLine):
    def __init__(self, aabb: AABB):
        self.aabb = aabb

    def length(self):
        x = self.aabb.x_max - self.aabb.x_min
        y = self.aabb.y_max - self.aabb.y_min
        return math.sqrt(x * x + y * y)


def test_register_trait():
    assert len(trait_impl_pool) == 2
    assert trait_impl_pool[NumberPair, AsLine] == NumberPairAsLine
    assert trait_impl_pool[AABB, AsLine] == AABBAsLine


def test_as_line_traits():
    obj_list = [NumberPair(1, 1), AABB(0, 1, 0, 1)]
    length = [AsLine.cls_trait_for(i).length() for i in obj_list]
    for i in length:
        assert math.isclose(i, math.sqrt(2))


def test_as_line_traits_update_value():
    number_pair = NumberPair(0, 0)
    aabb = AABB(0, 0, 0, 0)

    lines = [as_line(i) for i in (number_pair, aabb)]

    number_pair.x = 1
    number_pair.y = 1
    aabb.x_max = 1
    aabb.y_max = 1

    length = [i.length() for i in lines]
    for i in length:
        assert math.isclose(i, math.sqrt(2))
