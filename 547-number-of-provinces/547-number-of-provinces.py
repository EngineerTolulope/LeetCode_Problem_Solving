class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def depth_first_search(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    depth_first_search(end)
            
        
        visited, province_count = set(), 0
        for start in range(len(isConnected)):
            if start not in visited:
                province_count += 1
                depth_first_search(start)
        return province_count