class HashTable:
    def __init__(self, cap=8):
        self.cap = cap
        self.size = 0
        self.buckets = [None] * cap
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.cap
    def __setitem__(self, key, val):
        idx = self._hash(key)
        while self.buckets[idx] is not None and self.buckets[idx][0] != key:
            idx = (idx + 1) % self.cap
        if self.buckets[idx] is None:
            self.size += 1
        self.buckets[idx] = (key, val)
    def __getitem__(self, key):
        idx = self._hash(key)
        while self.buckets[idx] is not None:
            if self.buckets[idx][0] == key:
                return self.buckets[idx][1]
            idx = (idx + 1) % self.cap
        raise KeyError(key)
    def _resize(self):
        old = self.buckets
        self.cap *= 2
        self.size = 0
        self.buckets = [None] * self.cap
        for pair in old:
            if pair:
                self[pair[0]] = pair[1]
ht = HashTable()
ht["abc"] = 1001
ht["acd"] = 1002
ht["abd"] = 1003
print(ht["abc"], ht["acd"], ht["abd"])