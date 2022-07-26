class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])   # O(nlogn). Sorts based on the start interval
        output = [intervals[0]]     # Takes the first interval
        
        for start, end in intervals[1:]:    # Loops through the remaining
            most_recent_end = output[-1][1] 
            
            if start <= most_recent_end:    # Checks if there is an overlap between current and previous
                output[-1][1] = max(most_recent_end, end)
            else:
                output.append([start, end])
        return output
        
        