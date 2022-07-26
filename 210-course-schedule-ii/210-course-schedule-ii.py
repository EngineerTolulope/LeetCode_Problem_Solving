class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {course:[] for course in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
            
        output=[]
        visit, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:    # If caught in a loop
                return False
            if crs in visit:    # If prerequiste has been visited
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:   # If caught in a loop
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output
                    
                