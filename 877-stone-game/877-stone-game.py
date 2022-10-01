class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # (left, right) -> max alice total
        
        def depth_first_search(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
        
            alice_turn = True if (right - left + 1) % 2 == 0 else False 
            left_num = piles[left] if alice_turn else 0
            right_num = piles[right] if alice_turn else 0
            dp[(left, right)] = max(depth_first_search(left + 1, right) + left_num,
                                    depth_first_search(left, right - 1) + right_num)
            
            return dp[(left, right)]
        return depth_first_search(0, len(piles) - 1) > (sum(piles)) // 2