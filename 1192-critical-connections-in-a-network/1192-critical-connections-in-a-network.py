class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def make_graph(connections):
            graph = collections.defaultdict(list)
            for node_1, node_2 in connections:
                graph[node_1].append(node_2)
                graph[node_2].append(node_1)
            return graph
        
        
        graph = make_graph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n
        
        
        def depth_first_search(node, depth):
            if rank[node] >= 0:
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue
                back_depth = depth_first_search(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            rank[node] = n
            return min_back_depth
        
        
        depth_first_search(0, 0)
        return list(connections)
            