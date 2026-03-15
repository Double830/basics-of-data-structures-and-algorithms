from typing import Any
from collections.abc import Sequence
class SetOperation:
    def __init__(self):
        self.set_data = []
    def insert(self, element):
        if element not in self.set_data:
            self.set_data.append(element)
            return True
        return False
    def delete(self, element):
        if element in self.set_data:
            self.set_data.remove(element)
            return True
        return False
    def query(self, element):
        return element in self.set_data
    def show_set(self):
        return self.set_data
test_set = SetOperation()
print(test_set.insert("apple"))
print(test_set.insert("banana"))
print(test_set.insert("apple"))
print(test_set.show_set())
print(test_set.query("banana"))
print(test_set.query("cherry"))
print(test_set.show_set())
print(test_set.delete("banana"))
print(test_set.delete("cherry"))
print(test_set.show_set())