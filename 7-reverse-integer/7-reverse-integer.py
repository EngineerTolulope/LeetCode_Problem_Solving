class Solution:
    def reverse(self, x: int) -> int:
        MIN_INTEGER, MAX_INTEGER = -(2 ** 31), (2 ** 31) - 1
        
        result = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            
            if ((result > MAX_INTEGER // 10) or (result == MAX_INTEGER and digit > MAX_INTEGER % 10) or
               (result < int(MIN_INTEGER / 10)) or (result == MIN_INTEGER 
                                                    and digit < int(math.fmod(MIN_INTERGER, 10)))):
                return 0
            result = result * 10 + digit
        return result