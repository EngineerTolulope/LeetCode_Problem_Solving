class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        combined = list(zip(efficiency, speed))
        combined.sort(reverse = True)

        min_heap = []
        total_speed, result = 0, 0
        for eff, spd in combined:
            if len(min_heap) == k:
                total_speed -= heapq.heappop(min_heap)
            
            total_speed += spd
            result = max(result, total_speed * eff)
            heapq.heappush(min_heap, spd)
        return result % (10 ** 9 + 7)

        