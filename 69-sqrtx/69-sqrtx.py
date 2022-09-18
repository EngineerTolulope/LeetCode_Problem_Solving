class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            middle = left + (right - left) // 2
            square = middle * middle
            next_square = (middle + 1) * (middle + 1)
            
            if square <= x < next_square:
                return middle
            elif square > x:
                right = middle - 1
            else:
                left = middle + 1