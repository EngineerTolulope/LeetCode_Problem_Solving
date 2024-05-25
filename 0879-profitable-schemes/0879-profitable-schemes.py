class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7

        # dp[k][j] means the number of ways to achieve at least j profit with k members
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # One way to achieve zero profit with zero members

        for g, p in zip(group, profit):
            for members in range(n, g - 1, -1):
                for currentProfit in range(minProfit, -1, -1):
                    newProfit = min(minProfit, currentProfit + p)
                    dp[members][newProfit] += dp[members - g][currentProfit]
                    dp[members][newProfit] %= MOD

        return sum(dp[members][minProfit] for members in range(n + 1)) % MOD
    
    
    def profitableSchemes_(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        modulo = 10**9 + 7

        dp = {}
        def dfs(i, n, p):
            if i == len(group):
                return 1 if p >= minProfit else 0
            if (i, n, p) in dp:
                return dp[(i, n, p)]
            dp[(i, n, p)] = dfs(i+1, n, p) #Skipped index i

            if n - group[i] >= 0:
                dp[(i, n, p)] += dfs(i + 1, n - group[i], min(minProfit, p + profit[i])) % modulo
            return dp[(i, n, p)]

        return dfs(0, n, 0)