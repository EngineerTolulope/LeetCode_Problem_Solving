class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: buying or sellling?
        # If buy -> i + 1; if sell -> i + 2
        
        dp = {} # key = (i, buying); value = max_profit
        
        def depth_first_search(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = depth_first_search(i + 1, buying)
            if buying:
                buy = depth_first_search(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = depth_first_search(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return depth_first_search(0, True)
        