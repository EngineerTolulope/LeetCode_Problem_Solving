class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        neighbors = defaultdict(list)
        for start, end in enumerate(edges):
            neighbors[start].append(end)
        
    
        def bfs(start, distanceMap):
            queue = deque()
            queue.append((start, 0))
            distanceMap[start] = 0

            while queue:
                node, distance = queue.popleft()
                for neighbor in neighbors[node]:
                    if neighbor not in distanceMap:
                        queue.append((neighbor, distance + 1))
                        distanceMap[neighbor] = distance + 1
        
        node1Dist = {} # Map node -> distance from node1    
        node2Dist = {} # Map node -> distance from node2
        bfs(node1, node1Dist)
        bfs(node2, node2Dist)

        result = -1
        resultDistance = sys.maxsize
        for i in range(len(edges)):
            if i in node1Dist and i in node2Dist:
                distance = max(node1Dist[i], node2Dist[i])
                if distance < resultDistance:
                    result = i
                    resultDistance = distance
        
        return result

