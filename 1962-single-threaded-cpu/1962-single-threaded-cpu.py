import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        indexed_tasks.sort()

        result = []
        min_heap = []
        current_time = indexed_tasks[0][0]
        i = 0

        while i < len(indexed_tasks) or min_heap:
            while i < len(indexed_tasks) and current_time >= indexed_tasks[i][0]:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
            
            if min_heap:
                process_time, index = heapq.heappop(min_heap)
                result.append(index)
                current_time += process_time
            else:
                current_time = indexed_tasks[i][0]

        return result