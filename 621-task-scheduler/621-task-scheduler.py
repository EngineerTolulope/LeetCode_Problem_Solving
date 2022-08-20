class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [(-count, task) for task, count in task_count.items()]   # using min heap for max heap
        heapq.heapify(max_heap)
        
        current_time, queue = 0, deque()
        while max_heap or queue:
            current_time += 1
            if max_heap:
                count, task = heapq.heappop(max_heap)
                count += 1
                if count:
                    queue.append((count, task, current_time + n))
            if queue and queue[0][2] == current_time:
                count, task, _ = queue.popleft()
                heapq.heappush(max_heap, (count, task))
        return current_time
                