class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7  # Define the modulo constant

        # Initialize the dp array
        # dp[k][j] represents the number of ways to achieve at least j profit with k members
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: one way to achieve 0 profit with 0 members

        # Iterate over each crime
        for g, p in zip(group, profit):
            # Traverse the dp array backwards to avoid overwriting values from the same iteration
            for members in range(n, g - 1, -1):
                for currentProfit in range(minProfit, -1, -1):
                    # Calculate the new profit, ensuring it doesn't exceed minProfit
                    newProfit = min(minProfit, currentProfit + p)
                    # Update the dp array with the number of ways to include this crime
                    dp[members][newProfit] += dp[members - g][currentProfit]
                    dp[members][newProfit] %= MOD  # Apply modulo to keep values manageable

        # Sum up all the ways to achieve at least minProfit with any number of members
        result = sum(dp[members][minProfit] for members in range(n + 1)) % MOD
        return result
    
    
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