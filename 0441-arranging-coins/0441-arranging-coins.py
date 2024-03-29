class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        result = 0

        while left <= right:
            middle = (left + right) // 2
            needed_coins = (middle / 2) * (middle + 1)
            if needed_coins > n:
                right = middle - 1
            else:
                result = max(result, middle)
                left = middle + 1
        return result

    # maths solution
    def arrangeCoins_(self, n: int) -> int:
        return math.floor(math.sqrt(2 * n + 0.25) - 0.5)