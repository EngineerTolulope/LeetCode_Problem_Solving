class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        cache = {}

        def depth_first_search(i, M):
            if i >= n:
                return 0
            if (i, M) in cache:
                return cache[(i, M)]
            
            maximum_stones = float("-inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                total += piles[i + X - 1]
                opponent_stones = depth_first_search(i + X, max(M, X))
                maximum_stones = max(maximum_stones, total - opponent_stones)
            
            cache[(i, M)] = maximum_stones
            return maximum_stones

        return (sum(piles) + depth_first_search(0, 1)) // 2