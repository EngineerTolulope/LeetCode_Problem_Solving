class FreqStack:
    
    def __init__(self):
        self.max_count = 0
        self.count_stacks = {}
        self.nums_count = {}

    def push(self, val: int) -> None:
        count = 1 + self.nums_count.get(val, 0)
        self.nums_count[val] = count
        if not count in self.count_stacks:
            self.count_stacks[count] = []
        self.count_stacks[count].append(val)
        if count > self.max_count:
            self.max_count = count          

    def pop(self) -> int:
        value = self.count_stacks[self.max_count].pop()
        self.nums_count[value] -= 1
        if not self.count_stacks[self.max_count]:
            self.max_count -= 1
        return value
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()