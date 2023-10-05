class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1].copy()

        for row in triangle[-2::-1]:
            for i in range(len(row)):
                dp[i] = min(dp[i], dp[i + 1]) + row[i]

        return dp[0]

    def minimumTotal_(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, num in enumerate(row):
                dp[i] = min(dp[i] + num, dp[i + 1] + num)
        return dp[0]