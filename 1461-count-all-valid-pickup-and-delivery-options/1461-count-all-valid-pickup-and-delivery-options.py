class Solution:
    def countOrders(self, n: int) -> int:
        MOD = int(1e9) + 7
        result = 1

        for i in range(1, n + 1):
            result = (result * (i * 2 - 1) * i) % MOD

        return result