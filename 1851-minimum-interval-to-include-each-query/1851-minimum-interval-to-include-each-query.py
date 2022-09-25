class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        result, min_heap, i = {}, [], 0
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            result[query] = min_heap[0][0] if min_heap else -1
        return [result[query] for query in queries]