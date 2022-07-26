class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:    # If new interval end is less than the start interval
                result.append(newInterval)
                return result + intervals[i:]   # Return immediately since the remaining wouldn't overlap
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:   # We get here is there's overlap. 
                # We take the longer interval, but append because the new one might have an overlap.
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        result.append(newInterval)
        return result