class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] # every node is a parent of itself initially
        rank = [1 for i in range(len(edges) + 1)]
        
        def find_parent(node):
            pt = parent[node]
            while pt != parent[pt]:
                parent[pt] = parent[parent[pt]]
                pt = parent[pt]
            return pt
        
        # return false if can't unionize the nodes
        def union_two_nodes(node_1, node_2):
            parent_1, parent_2 = find_parent(node_1), find_parent(node_2)
            
            if parent_1 == parent_2:
                return False
            
            if rank[parent_1] > rank[parent_2]:
                parent[parent_2] = parent_1
                rank[parent_1] += rank[parent_2]
            else:
                parent[parent_1] = parent_2
                rank[parent_2] += rank[parent_1]
            return True
        
        for node_1, node_2 in edges:
            if not union_two_nodes(node_1, node_2):
                return [node_1, node_2]