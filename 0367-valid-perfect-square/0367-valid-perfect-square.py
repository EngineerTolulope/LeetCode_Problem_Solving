class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        left, right = 1, (num // 2)
        while left <= right:
            middle = left + (right - left) // 2
            square = middle * middle
            if square > num:
                right = middle - 1
            elif square < num:
                left = middle + 1
            else:
                return True
        return False