import math

from python_trait import Trait, register_trait, trait_impl_pool


class NumberPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class AsLine(Trait['AsLine']):
    def length(self):
        return 0


@register_trait(NumberPair, AsLine)
class NumberPairAsLine(AsLine):
    def __init__(self, number_pair: NumberPair):
        self.number_pair = number_pair

    def length(self):
        x = self.number_pair.x
        y = self.number_pair.y
        return math.sqrt(x * x + y * y)


def test_register_trait():
    assert len(trait_impl_pool) == 1
    assert trait_impl_pool[NumberPair, AsLine] == NumberPairAsLine


def test_number_pair_as_line_traits():
    number_pair = NumberPair(1, 1)
    length = AsLine()(number_pair).length()
    print(length)
