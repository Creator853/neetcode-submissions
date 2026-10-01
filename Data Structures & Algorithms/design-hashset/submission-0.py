class MyHashSet:

    def __init__(self, N:int = 1000):
        self.size = N
        self.buckets = [[] for _ in range(N)]

    def add(self, key: int) -> None:
        index = key % self.size
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
        

    def contains(self, key: int) -> bool:
        index = key % self.size
        if key in self.buckets[index]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)