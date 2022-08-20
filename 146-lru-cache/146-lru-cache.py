class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.previous = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps key to node
        
        # left = least recently used; right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.previous = self.right, self.left
        
    # removes node from list
    def remove(self, node):
        previous, next_one = node.previous, node.next
        previous.next, next_one.previous = next_one, previous
    
    # inserts node to the right
    def insert_to_right(self, node):
        previous, next_one = self.right.previous, self.right
        previous.next = next_one.previous = node
        node.next, node.previous = next_one, previous
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_to_right(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_to_right(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # removes the least recently used, and deletes it from the hashmap
            least_recent = self.left.next
            self.remove(least_recent)
            self.cache.pop(least_recent.key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)