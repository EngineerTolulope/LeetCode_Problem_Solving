class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'
        
        num1_int, num2_int = 0, 0
        for digit in num1:
            num1_int = num1_int * 10 + ord(digit) - ord('0')
        for digit in num2:
            num2_int = num2_int * 10 + ord(digit) - ord('0')
        
        num1_num2 = num1_int * num2_int
        result = ''
        while num1_num2:
            digit = num1_num2 % 10
            result += str(digit)
            num1_num2 //= 10
            
        return result[::-1]