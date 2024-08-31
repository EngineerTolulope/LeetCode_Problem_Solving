class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next  # Allows setting the next node upon creation

class MyHashMap:

    def __init__(self):
        self.size = 10 ** 4  # Use 'size' instead of 'length' for clarity
        self.map = [ListNode() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        current = self.map[index]

        # Traverse the linked list to find if the key exists; if so, update its value
        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next

        # If the key does not exist, add a new node at the end of the list
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        current = self.map[index].next  # Start directly from the first real node

        # Traverse the linked list to find the key
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return -1  # Return -1 if the key is not found

    def remove(self, key: int) -> None:
        index = key % self.size
        current = self.map[index]

        # Traverse the linked list to find the node to be removed
        while current.next:
            if current.next.key == key:
                current.next = current.next.next  # Remove the node by bypassing it
                return
            current = current.next


# Example usage:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)
