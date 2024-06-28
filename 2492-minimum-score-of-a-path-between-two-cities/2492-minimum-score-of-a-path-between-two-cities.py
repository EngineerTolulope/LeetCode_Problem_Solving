class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        neighbors = defaultdict(list)

        for start, end, distance in roads:
            neighbors[start].append((end, distance))
            neighbors[end].append((start, distance))

        def dfs(node):
            nonlocal result
            if node in visited:
                return 
            
            visited.add(node)
            for neighbor, distance in neighbors[node]:
                result = min(result, distance)
                dfs(neighbor)
        
        result = sys.maxsize
        visited = set()
        dfs(1)
        return result
