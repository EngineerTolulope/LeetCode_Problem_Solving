class Solution:
    def minDays(self, n: int) -> int:
        dp = {0:0, 1:1}  # n -> minium number of days
        
        def dfs(n):
            if n in dp:
                return dp[n]
            
            two = 1 + (n % 2) + dfs(n // 2)
            three = 1 + (n % 3) + dfs(n // 3)
            dp[n] = min(two, three)
            
            return dp[n]
        
        
        return dfs(n)