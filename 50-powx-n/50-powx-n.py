class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def divide_and_conquer(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            if n % 2 == 0:
                result = divide_and_conquer(x * x, n // 2) 
            else:
                result = x * divide_and_conquer(x * x, n // 2)
            return result           
        
        result = divide_and_conquer(x, abs(n))
        return result if n >= 0 else 1 / result