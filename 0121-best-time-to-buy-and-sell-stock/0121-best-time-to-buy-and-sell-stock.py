class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0
        
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                price_diff = prices[right] - prices[left]
                max_profit = max(price_diff, max_profit)
            right += 1
        
        return max_profit

        
        