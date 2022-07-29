class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom Up Approach
        infinity = float('+inf')
        min_coins = [infinity] * (amount + 1)
        min_coins[0] = 0
        
        for num in range(1, amount+1):
            for coin in coins:
                if (num - coin) >= 0:
                    min_coins[num] = min(min_coins[num], 1 + min_coins[num-coin])
        
        return min_coins[amount] if min_coins[amount] != infinity else -1 