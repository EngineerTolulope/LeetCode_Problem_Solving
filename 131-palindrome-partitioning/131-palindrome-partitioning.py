class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        
        def ispalindrome(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtracking(i, partition):
            if i >= len(s):
                result.append(partition.copy())
                
            for j in range(i, len(s)):
                if ispalindrome(s, i, j):
                    partition.append(s[i:j + 1])
                    backtracking(j + 1, partition)
                    partition.pop()
            
            
        backtracking(0, [])
        return result