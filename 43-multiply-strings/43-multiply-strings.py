class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        int1 = 0
        int2 = 0
        
        # convert string to int
        for n in num1:
            int1 = int1 * 10 + (ord(n) - ord('0'))
        for n in num2:
            int2 = int2 * 10 + (ord(n) - ord('0'))
        
        int_res = int1 * int2
        
        res = ""
        
        while int_res:
            remainder = int_res % 10
            res = res + str(remainder)
            int_res = int_res // 10
        
        return res[::-1]