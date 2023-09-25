class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        def depth_first_search(is_alice, i, M):
            if i == len(piles):
                return 0
            if (is_alice, i , M) in cache:
                return cache[(is_alice, i, M)]
            
            result = 0 if is_alice else float("infinity")
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                total += piles[i +  X - 1]
                if is_alice:
                    result = max(result, total + depth_first_search(not is_alice, i + X, max(M, X)))
                else:
                    result = min(result, depth_first_search(not is_alice, i + X, max(M, X)))
            cache[(is_alice, i, M)] = result
            return result

        return depth_first_search(True, 0, 1) 