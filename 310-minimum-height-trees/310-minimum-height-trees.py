class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]
        
        neighbours = [set() for x in range(n)]
        for left, right in edges:
            neighbours[left].add(right)
            neighbours[right].add(left)
            
        leaves = []
        for i in range(n):
            if len(neighbours[i]) == 1:
                leaves.append(i)
                
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            temp = []
            
            for leaf in leaves:
                for neighbour in neighbours[leaf]:
                    neighbours[neighbour].remove(leaf)
                    if len(neighbours[neighbour]) == 1:
                        temp.append(neighbour)
            leaves = temp
            
        return leaves