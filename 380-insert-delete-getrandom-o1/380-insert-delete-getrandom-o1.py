class RandomizedSet:

    def __init__(self):
        self.nums_map, self.nums_list = {}, []        

    def insert(self, val: int) -> bool:
        result = val not in self.nums_map
        if result:
            self.nums_list.append(val)
            index = len(self.nums_list) - 1
            self.nums_map[val] = index
        return result

    def remove(self, val: int) -> bool:
        result = val in self.nums_map
        if result:
            index = self.nums_map[val]
            self.nums_list[index] = self.nums_list[-1]
            last_value = self.nums_list.pop()
            self.nums_map[last_value] = index
            self.nums_map.pop(val)
        return result
        
    def getRandom(self) -> int:
        return random.choice(self.nums_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()