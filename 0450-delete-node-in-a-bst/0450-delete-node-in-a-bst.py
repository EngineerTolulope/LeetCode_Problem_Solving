# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root  # If the tree is empty, return None
        
        # Traverse the tree to find the node to delete
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # Node to be deleted is found
            if not root.left:
                return root.right  # Return the right subtree if left is None
            elif not root.right:
                return root.left  # Return the left subtree if right is None
            
            # Node has two children, find the inorder successor (smallest in the right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace the node's value with the successor's value
            root.val = successor.val
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, successor.val)
        
        return root

# Example usage:
# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(7)
# solution = Solution()
# new_root = solution.deleteNode(root, 3)
# print(new_root.left.val)  # Should output 4 (new left child of the root)