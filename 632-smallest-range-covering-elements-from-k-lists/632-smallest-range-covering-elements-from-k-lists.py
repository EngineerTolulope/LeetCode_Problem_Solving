class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        queue = []
        k = len(nums)
        maximum = 0
        
        # populate initial state
        for i in range(k):
            heapq.heappush(queue, (nums[i][0], i, 0))
            maximum = max(maximum, nums[i][0])
        
        result = [queue[0][0], maximum]
        while True:
            _, k_index, num_index = heapq.heappop(queue)
            
            # if current smallest number is the last item in its list, then break
            if num_index == len(nums[k_index]) - 1:
                break
            
            next_num = nums[k_index][num_index + 1]
            maximum = max(maximum, next_num)
            heapq.heappush(queue, (next_num, k_index, num_index + 1))
            
            if maximum - queue[0][0] < result[1] - result[0]:
                result = [queue[0][0], maximum]
        return result