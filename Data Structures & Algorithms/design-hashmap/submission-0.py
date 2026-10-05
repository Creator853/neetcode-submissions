class MyHashMap:

    def __init__(self):
        self.maps = [[]]

    def put(self, key: int, value: int) -> None:
        map_len = len(self.maps)
        index = key % map_len
        for container in self.maps[index]:
            if key == container[0]:
                container[1] = value
                return 
        self.maps[index].append([key, value])

    def get(self, key: int) -> int:
        map_len = len(self.maps)
        index = key % map_len
        for container in self.maps[index]:
            if key == container[0]:
                return container[1]
        return -1 

    def remove(self, key: int) -> None:
        map_len = len(self.maps)
        index = key % map_len
        for container in self.maps[index]:
            if key == container[0]:
                self.maps[index].remove([key, container[1]])
                return 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)