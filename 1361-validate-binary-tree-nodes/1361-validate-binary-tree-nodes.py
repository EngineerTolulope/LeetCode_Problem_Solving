class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        has_parent = set(leftChild + rightChild)
        has_parent.discard(-1)
        if len(has_parent) == n:
            return False
        
        root = -1
        for i in range(n):
            if i not in has_parent:
                root = i
                break
                
        visited = set()
        def dfs(i):
            if i == -1:
                return True
            if i in visited:
                return False
            visited.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        
        return dfs(root) and len(visited) == n 