class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = collections.defaultdict(list)    
        for source, target, weight in times:
            neighbors[source].append((target, weight))
            
        result = 0
        min_heap, visited = [(0, k)], set()
        while min_heap:
            weight_1, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            result = max(result, weight_1)
            
            for next_node, weight_2 in neighbors[node]:
                if next_node in visited:
                    continue
                heapq.heappush(min_heap, (weight_1 + weight_2, next_node))
        return result if len(visited) == n else -1
    