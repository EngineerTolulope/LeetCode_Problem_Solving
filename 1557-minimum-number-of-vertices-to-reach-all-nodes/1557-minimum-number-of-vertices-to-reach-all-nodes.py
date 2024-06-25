class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)
        for start, end in edges:
            incoming[end].append(start)
        
        result = []
        for node in range(n):
            if node not in incoming:
                result.append(node) 

        return result