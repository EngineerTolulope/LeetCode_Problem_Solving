class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbours = defaultdict(list)
        edges = set()

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
            edges.add((a, b))

        visited = set()
        changes_count = 0
        queue = deque([0])
        visited.add(0)

        while queue:
            city = queue.popleft()
            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                if (city, neighbour) in edges:  # check if the edge is reversed
                    changes_count += 1
                queue.append(neighbour)
                visited.add(neighbour)

        return changes_count