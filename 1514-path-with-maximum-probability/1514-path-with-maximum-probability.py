class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        neighbors = defaultdict(list)

        for i in range(len(edges)):
            start, end = edges[i]
            prob = succProb[i]

            neighbors[start].append((prob, end))
            neighbors[end].append((prob, start))
        
        visited = set()
        max_heap = [(-1, start_node)]
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            visited.add(node)

            if node == end_node:
                return abs(prob)
            
            for neigh_prob, neighbor in neighbors[node]:
                if neighbor not in visited:
                    heapq.heappush(max_heap, (prob * neigh_prob, neighbor))
        
        return 0

        