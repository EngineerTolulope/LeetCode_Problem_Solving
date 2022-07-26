class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Example prerequistes = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
        
        # Hash map to store the prerequiste of each course
        precourses = {i:[] for i in range(numCourses)} 
        for course, precourse in prerequisites:
            precourses[course].append(precourse)    # Appends the prerequiste for each course
        
        visited = set() # Visited set to store visited courses
        
        def dfs_search(course):
            # Base cases.
            if course in visited:   # Helps to detect a loop in dfs search
                return False
            if precourses[course] == []:    # If no preequiste then we can take the course
                return True
            
            visited.add(course) # Add current course to visited
            
            # Go through each precourse
            for precourse in precourses[course]:
                if not dfs_search(precourse):   # Returns false if a loop is detected 
                    return False
            
            # When we get here it means the course can be completed
            visited.remove(course)
            precourses[course] = [] 
            return True # Only the first one hasn't returned yet
        # End of Helper Function
        
        
        # We go through each course because what if courses are unrelated like, 1 -> 2, and 3 -> 4
        for course in range(numCourses):
            if not dfs_search(course):
                return False
        
        return True # We get here if all courses can be completed
        
        
        
        