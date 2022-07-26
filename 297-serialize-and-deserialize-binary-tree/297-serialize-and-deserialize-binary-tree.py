# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        result = []
        
        def depth_first_search(node):
            # Base case. If null 
            if not node:
                result.append("None")
                return
            else:
                # Node values are usually stored as integers
                result.append(str(node.val))    
            
            # Calls it on the left and right node
            depth_first_search(node.left)
            depth_first_search(node.right)
        # End of helper method
        
        depth_first_search(root)
        return ",".join(result) # Return value is a comma separated string
    # End of Serialize Function       

    def deserialize(self, data):
        values = data.split(",")    
        self.index = 0  # Uses self so we could refer to it in the function
        
        def depth_first_search():
            if values[self.index] == "None":
                self.index += 1
                return None
            else:
                node = TreeNode(int(values[self.index]))
                self.index += 1
                
                # Performs the depth first search on the left or right until we reach "None"
                node.left = depth_first_search()
                node.right = depth_first_search()
                return node # At the end is only our starting point that hasn't returned anything
        return depth_first_search()
    # End of Deserialize function
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))