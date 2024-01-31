class ListNode:
    
    def __init__(self, value, previous = None, next_ = None):
        self.value = value
        self.previous = previous
        self.next = next_
        
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url, self.current)
        self.current = self.current.next
        

    def back(self, steps: int) -> str:
        while self.current.previous and steps > 0:
            self.current = self.current.previous
            steps -= 1
        return self.current.value

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)