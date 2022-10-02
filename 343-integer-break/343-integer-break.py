class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def depth_first_search(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                value = depth_first_search(i) * depth_first_search(num - i)
                dp[num] = max(dp[num], value)
            return dp[num]
        
        return depth_first_search(n)