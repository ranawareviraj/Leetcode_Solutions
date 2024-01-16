class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.keys = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.keys)
        self.keys.append(val)        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # Swap it with last element in the list
        last, val_index = self.keys[-1], self.map[val]
        self.keys[val_index] = last
        self.map[last] = val_index

        # Remove from map and list
        self.map.pop(val)
        self.keys.pop()
            
        return True

    def getRandom(self) -> int:
        return choice(self.keys)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()