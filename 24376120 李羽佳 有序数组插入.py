from typing import Any
from collections.abc import Sequence
class OrderArrayInsert:
    def __init__(self, iterable: Sequence[Any]):
        self.iterable = list(iterable)
    def insert(self, element: Any) -> None:
        insert_index: int = len(self.iterable)
        for index, value in enumerate(self.iterable):
            if element < value:
                insert_index = index
                break
        self.iterable.append("")
        self.len = len(self.iterable)
        for i in range(self.len - 1, insert_index - 1, -1):
            self.iterable[i] = self.iterable[i - 1]
        self.iterable[insert_index] = element
numarray = [1, 4, 21, 59, 69]
add_array = OrderArrayInsert(numarray)
add_array.insert(5555)
add_array.insert(0)
add_array.insert(25)
print(add_array.iterable)