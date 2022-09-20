class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def get_slope_intercept(x1, y1, x2, y2):
            if x1 == x2:    # vertical line
                return x1, None
            if y1 == y2:
                return 0, y1
            
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            return slope, intercept
        
        
        if len(points) == 1:
            return 1
        
        neighbors = collections.defaultdict(set)
        for i in range(len(points)):
            for j in range(i, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                slope_intercept = get_slope_intercept(x1, y1, x2, y2)
                neighbors[slope_intercept].add(i)
                neighbors[slope_intercept].add(j)
        
        result = max([len(neighbors[slope_intercept]) for slope_intercept in neighbors])
        return result
                
                