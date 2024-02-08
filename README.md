# usage

for a example data class `NumberPair`.

```python
class NumberPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

define a trait `AsLine` with method `length()`.

```python
from python_trait import Trait


class AsLine(Trait['AsLine']):
    def length(self):
        raise NotImplementedError
```

implement trait `AsLine` of `NumberPair`.

```python
import math
from python_trait import trait_to

@trait_to(NumberPair)
class NumberPairAsLine(AsLine):
    def __init__(self, number_pair: NumberPair):
        self.number_pair = number_pair

    def length(self):
        x = self.number_pair.x
        y = self.number_pair.y
        return math.sqrt(x * x + y * y)
```

now we can use trait with type hint supported like this.

```python
as_line = AsLine()
obj = NumberPair(1, 1)
print('the length of line is:', as_line(obj).length())  # `.length()` method can be hint.
```