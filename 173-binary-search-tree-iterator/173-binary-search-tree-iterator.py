# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.add_left_children(root)

    def next(self) -> int:
        result = self.stack.pop()
        self.add_left_children(result.right)
        return result.val
        
    def hasNext(self) -> bool:
        return bool(self.stack)
        
    def add_left_children(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()