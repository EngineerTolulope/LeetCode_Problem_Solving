class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Convert all numbers to negative integers for max-heap behavior
        max_heap = [-int(num) for num in nums]
        heapq.heapify(max_heap)

        # Pop elements until we reach the kth largest
        for _ in range(k - 1):
            heapq.heappop(max_heap)

        # Return the kth largest number as a string
        return str(-max_heap[0])