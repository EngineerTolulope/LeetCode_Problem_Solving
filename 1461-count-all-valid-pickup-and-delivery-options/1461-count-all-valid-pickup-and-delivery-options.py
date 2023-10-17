class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        remaining_slots = 2 * n
        result = 1
        
        while remaining_slots > 0:
            valid_choices = remaining_slots * (remaining_slots - 1) // 2
            result = (result * valid_choices) % MOD
            remaining_slots -= 2
        
        return result

    def countOrders_(self, n: int) -> int:
        remaining_slots = 2 * n
        result = 1
        while remaining_slots > 0:
            valid_choices = (remaining_slots * (remaining_slots - 1)) // 2
            result *= valid_choices
            remaining_slots -= 2
        return result % (10**9 + 7)