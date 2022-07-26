class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()    # The default one sorts based on the start interval
        
        min_removal = 0
        previous_end = intervals[0][1]  # Starts with the first interval's end value
        
        # Goes through the remaining intervals
        for start, end in intervals[1:]:    
            # If the current start is less than our previous end then there is an overlap
            if start < previous_end:
                min_removal += 1
                previous_end = min(end, previous_end)   # Deletes the one with the largest end
            else:
                previous_end = end
                
        return min_removal
        