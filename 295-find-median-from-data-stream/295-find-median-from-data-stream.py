class MedianFinder:

    def __init__(self):
        # Two heaps, small heap is a max heap, large heap is a min heap
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # We start pushing to the small heap and re adjust as follows
        heapq.heappush(self.small, -1 * num)    # Python only allows us to implement min heaps
        
        # Make sure every number in small is <= every num in large heap.
        if (self.small and self.large and   # If both heaps are non empty
            (-1 * self.small[0]) > self.large[0]):   # Index 0 refers to the minimum number for both heaps.
            # For the small heap it's the maximum after taking the absolute number
            value = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value)
            
        # If the sizes are uneven. One size difference is still acceptable
        if len(self.small) > len(self.large) + 1:
            value = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value) 
        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * value) 
    
    
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0]  + self.large[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()