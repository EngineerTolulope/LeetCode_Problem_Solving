class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            first, second = -heapq.heappop(stones), -heapq.heappop(stones)
            
            if first > second:
                new_stone = first - second
                heapq.heappush(stones, -new_stone)
        return -stones[0] if stones else 0
            