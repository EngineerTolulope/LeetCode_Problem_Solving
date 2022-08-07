class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -2 ** 31  # -2147483648
        MAX_INT = 2 ** 31 - 1 # 2147483647
        
        positive = True
        result = 0
        i = 0
        
        # whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # +/- symbol
        if i < len(s) and s[i] == '-':
            i += 1
            positive = False
        elif i < len(s) and s[i] == '+':
            i += 1
        
        # check number 0 - 9
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:
            result = result * 10 + int(s[i])
            i += 1
        
        result = result if positive else result * -1
        if result < MIN_INT:
            result = MIN_INT
        elif result > MAX_INT:
            result = MAX_INT
        return result 