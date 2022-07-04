# -*- coding: utf-8 -*-
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            v = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
                self.cache[key] = value
            else:
                self.cache[key] = value
