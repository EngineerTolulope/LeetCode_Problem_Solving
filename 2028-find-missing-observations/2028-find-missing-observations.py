class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        remaining_total = mean * (m + n) - sum(rolls)
        if remaining_total < n or remaining_total > n * 6:
            return []
        
        result = []
        while n:
            dice_value = min(6, remaining_total - n + 1)
            result.append(dice_value)
            remaining_total -= dice_value
            n -= 1
        return result
        