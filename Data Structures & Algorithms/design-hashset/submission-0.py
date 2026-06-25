class MyHashSet:

    def hashfunction(self, num):
        return num%1000

    def __init__(self):
        self.myset = [[] for i in range(1000)]

    def add(self, key: int) -> None:
        bucket = self.hashfunction(key)
        if(not key in self.myset[bucket]):
            self.myset[bucket].append(key)
        

    def remove(self, key: int) -> None:
        bucket = self.hashfunction(key)
        if(not key in self.myset[bucket]):
            return 
        self.myset[bucket].remove(key)
        

    def contains(self, key: int) -> bool:
        bucket = self.hashfunction(key)
        if(key in self.myset[bucket]):
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)