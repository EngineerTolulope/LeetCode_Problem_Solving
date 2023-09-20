class Solution:
    # bottom up dp approach
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for i in range(left + 1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    coins += dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]
    
    # recursive approach
    def maxCoins_(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def depth_first_search(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]

            max_coins = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += (depth_first_search(left, i - 1) 
                          + depth_first_search(i + 1, right))
                max_coins = max(max_coins, coins)
            
            cache[(left, right)] = max_coins
            return max_coins

        return depth_first_search(1, len(nums) - 2)