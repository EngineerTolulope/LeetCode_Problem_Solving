class ListNode:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.bucket_count = 10 ** 4
        self.hash_set = [None] * self.bucket_count

    def _get_bucket_index(self, key):
        return key % self.bucket_count

    def _find_node(self, key, index):
        current = self.hash_set[index]
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def add(self, key: int) -> None:
        index = self._get_bucket_index(key)
        if self._find_node(key, index):
            return
        new_node = ListNode(key)
        new_node.next = self.hash_set[index]
        self.hash_set[index] = new_node

    def remove(self, key: int) -> None:
        index = self._get_bucket_index(key)
        current = self.hash_set[index]
        if current and current.key == key:
            self.hash_set[index] = current.next
            return
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        index = self._get_bucket_index(key)
        node = self._find_node(key, index)
        return node is not None


# class ListNode:
#     def __init__(self, key = None):
#         self.key = key
#         self.next = None

# class MyHashSet:

#     def __init__(self):
#         self.hash_set = [ListNode() for _ in range(10 ** 4)]

#     def add(self, key: int) -> None:
#         index = key % (10 ** 4)
#         current = self.hash_set[index]

#         while current.next:
#             if current.next.key == key:
#                 return
#             current = current.next
#         current.next = ListNode(key)

#     def remove(self, key: int) -> None:
#         index = key % (10 ** 4)
#         current = self.hash_set[index]

#         while current.next:
#             if current.next.key == key:
#                 current.next = current.next.next
#                 return
#             current = current.next
        

#     def contains(self, key: int) -> bool:
#         index = key % (10 ** 4)
#         current = self.hash_set[index]

#         while current.next:
#             if current.next.key == key:
#                 return True
#             current = current.next
#         return False


# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)