class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.help_stack = []

    def push(self, x: int) -> None:
        while self.main_stack:
            self.help_stack.append(self.main_stack.pop())
        
        self.main_stack.append(x)
        while self.help_stack:
            self.main_stack.append(self.help_stack.pop())

    def pop(self) -> int:
        return self.main_stack.pop()
        

    def peek(self) -> int:
        return self.main_stack[-1]
        

    def empty(self) -> bool:
        return not self.main_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()