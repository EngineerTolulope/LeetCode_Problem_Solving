class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda x: x[0])

        result, min_heap = [], []
        current_time, i = tasks[0][0], 0

        while i < len(tasks) or min_heap:
            while i < len(tasks) and current_time >= tasks[i][0]:
                heapq.heappush(min_heap, tasks[i][1:])
                i += 1
            
            if min_heap:
                process_time, index = heapq.heappop(min_heap)
                result.append(index)
                current_time += process_time
            else:
                current_time = tasks[i][0]

        return result
