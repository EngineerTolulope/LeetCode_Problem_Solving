class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        divider = 1
        while x >= 10 * divider:
            divider *= 10
            
        while x:
            left_digit = x // divider
            right_digit = x % 10
            if left_digit != right_digit: return False
            
            x = (x % divider) // 10 # remove digits
            divider /= 100
        return True