class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        left = right = 0
        result = []
        
        while right < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            # remove left value from window
            if left > queue[0]:
                queue.popleft()
            
            if (right + 1) >= k:
                result.append(nums[queue[0]])
                left += 1
            right += 1
        return result
            