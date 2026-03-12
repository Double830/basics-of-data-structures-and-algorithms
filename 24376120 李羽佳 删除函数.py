from typing import Iterable, Any
class RemoveItem:
    def __init__(self, iterable: Iterable[Any]):
        self.iterable = list(iterable)
    def remove(self, index_to_remove: int) -> list[Any]:
        length_of_iterable: int =len(self.iterable)
        flag = 0
        if index_to_remove <= 0 or index_to_remove > length_of_iterable:
            print("Out of range!")
            flag = 1
        if flag == 0:
            for i in range(index_to_remove, length_of_iterable):
                self.iterable[i - 1] = self.iterable[i]
            self.iterable.pop()
            return self.iterable
test_list=[1, 2, 3, 4, 5]
remover = RemoveItem(test_list)
result = remover.remove(3)
print(result)