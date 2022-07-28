# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        result = n
        
        while left <= right:
            middle = (left + right)//2
            if isBadVersion(middle):
                result = min(result, middle)
                right = middle - 1
            else:
                left = middle + 1
        
        return result
            