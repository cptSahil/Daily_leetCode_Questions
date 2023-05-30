class MyHashSet:

    def __init__(self):
        self.size = 100
        self.storage = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            storageKey = key % self.size
            self.storage[storageKey].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            storageKey = key % self.size
            self.storage[storageKey].remove(key)

    def contains(self, key: int) -> bool:
        storageKey = key % self.size
        return key in self.storage[storageKey]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)