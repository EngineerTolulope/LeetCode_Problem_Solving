class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbours = collections.defaultdict(list)
        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        visited = set()
        changes_count = 0
        edges = {(a, b) for a, b in connections}
        queue = collections.deque([0])
        visited.add(0)

        while queue:
            city = queue.popleft()
            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                if (neighbour, city) not in edges:
                    changes_count += 1
                queue.append(neighbour)
                visited.add(neighbour)
        return changes_count