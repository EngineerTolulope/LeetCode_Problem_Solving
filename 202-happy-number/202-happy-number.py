class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = self.get_sum_of_squares(n)
            
            if n == 1:
                return True
        return False
    
    
    def get_sum_of_squares(self, num):
        result = 0
        
        while num:
            digit = num % 10
            result += digit * digit
            num //= 10
        return result
            