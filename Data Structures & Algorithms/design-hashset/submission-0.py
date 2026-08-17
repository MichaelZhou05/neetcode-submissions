class MyHashSet:

    def __init__(self):
        self.HashSet = [[] for _ in range(5000)] 


    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.HashSet[self.HashCode(key)].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.HashSet[self.HashCode(key)].remove(key)        


    def contains(self, key: int) -> bool:
        for element in self.HashSet[self.HashCode(key)]:
            if element == key:
                return True
        
        return False

    def HashCode(self, key:int) -> int:
        return key%len(self.HashSet)    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)