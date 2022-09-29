class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        num_count = {}
        for num in hand:
            num_count[num] = num_count.get(num, 0) + 1
        
        min_heap = list(num_count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            num = min_heap[0]
            for n in range(num, num + groupSize):
                if n not in num_count:
                    return False
                num_count[n] -= 1
                if num_count[n] == 0:
                    del num_count[n]
                    heapq.heappop(min_heap)
        return True
                