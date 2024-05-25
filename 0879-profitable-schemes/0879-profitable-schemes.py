class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
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