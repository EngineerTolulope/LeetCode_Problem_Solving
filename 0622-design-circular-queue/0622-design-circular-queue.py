class ListNode:
    def __init__(self, value=-1, previous=None, next_node=None):
        self.value = value
        self.previous = previous
        self.next = next_node

        
class MyCircularQueue:

    def __init__(self, k: int):
        self.remain_space = k
        self.left = ListNode(-1, None, None)
        self.right = ListNode(-1, self.left, None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        current_node = ListNode(value)
        current_node.next = self.right
        current_node.previous = self.right.previous
        
        self.right.previous.next = current_node
        self.right.previous = current_node
        self.remain_space -= 1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.previous = self.left
        self.remain_space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.value
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.previous.value

    def isEmpty(self) -> bool:
        return self.left.next == self.right        

    def isFull(self) -> bool:
        return self.remain_space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()