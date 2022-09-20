class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(dividend) == 2 ** 31 and divisor == -1:
            return (2 ** 31) - 1
        
        positive = True if (dividend >= 0) == (divisor >= 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend - divisor >= 0:
            count = 0
            while dividend - (divisor << 1 << count) >= 0:
                count += 1
            result += 1 << count
            dividend -= divisor << count
        return result if positive else -result