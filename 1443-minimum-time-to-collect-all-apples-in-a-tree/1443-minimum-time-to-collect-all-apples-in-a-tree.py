class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        neighbors = defaultdict(list)

        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(current, parent):
            time = 0

            for child in neighbors[current]:
                if child == parent:
                    continue
                
                childTime = dfs(child, current)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time
        return dfs(0, -1)