class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        min_heap = []   # (end, passenger count)
        
        total_pass = 0
        for trip in trips:
            pass_count, start, end = trip
            while min_heap and min_heap[0][0] <= start:
                total_pass -= min_heap[0][1]
                heapq.heappop(min_heap)
            
            total_pass += pass_count
            if total_pass > capacity:
                return False
            heapq.heappush(min_heap, (end, pass_count))
        return True